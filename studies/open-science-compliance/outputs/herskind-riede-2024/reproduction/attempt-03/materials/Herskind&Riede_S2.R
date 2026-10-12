#SUPPLEMENTARY INFORMATION S2
#R CODE FOR THE ANALYSES PERFORMED IN HERSKIND & RIEDE 2024 (JAS)


#______________________________________________________________________________#
                          #CONTENTS#
#PART LINE No.         CALCULATION                                    USED IN:
#1    L19:  Loading packages and data
#2    L33:  Object counts, stacked by chronology                      (Fig. 2 )
#3    L76:  Function for generating skipgrams and calculating PMI
#4    L222: Skipgram frequencies at different n-levels                (Table 1)
#5    L265: Culture complex-subsets and associated PMI summary stats  (Table 2)
#6    L323: Stacked bar plots of skipgrams by frequency and PMI       (Fig. 3 )
#7    L626: PMI bigram heatmap                                        (Fig. 4 )
#8    L698: Exporting data tables                                     (Supplementary Information S3)
#______________________________________________________________________________#

################################################################################
#PART 1: Loading packages and data##############################################
library(quanteda)
library(readxl)
library(ggplot2)
library(dplyr)
library(data.table)
library(forcats)
library(extrafont)
font_import(pattern = "GIL", prompt = FALSE) #error message doesn't seem to affect font output

#Loading the Excel file
data <- read_excel("Herskind&Riede_S1.xlsx")

################################################################################
#PART 2: Object counts, stacked by chronology###################################
#This part of the code generates the artefact type frequencies, stacked by chronology,
#as used to accompany the map on Fig.2.

#Renaming the variable
DS <- data %>%
  rename(Artefact_Type = `Artefact type`)

#Defining the levels, ordered by frequency
Artefact_levels <- c("axe", "shaft", "pendant", "dagger", "knife", "mattock-head", 
                     "point", "harpoon-head", "figurine", "long bone", "pick", 
                     "sleeve", "ulna dagger", "core", "flake", "plate", 
                     "slotted point", "other")

Artefact_levels <- rev(Artefact_levels)

#Combining the more rare artefact types into one level called "other"
DS$Artefact_Type <- fct_collapse(DS$Artefact_Type,
                                 other = c("blade", "paddle", "chisel", "haft", "hammer", "leister", "mattock", 
                                           "needle case", "nodule", "beam", "bow", "burin", "endscraper", 
                                           "flint axe", "leister prong", "needle", "net sinker", "pebble", 
                                           "pickaxe", "retoucher", "tine", "fragment")
)

#Reordering the levels of the factor variable
DS$Artefact_Type <- fct_relevel(DS$Artefact_Type, Artefact_levels)

#Making a chronologically stacked bar plot of artefact types
artefact_type_chronology <- ggplot(DS, aes(y = Artefact_Type, fill = Chronology)) +
  geom_bar() +
  scale_fill_manual(values = c("#FAD02E", "#D98888", "#E8BB8B", "#B4A1C1")) +
  labs(x = NULL, y = NULL) +
  theme(plot.title = element_text(size = 15, face = "bold", hjust = 0.5),
        axis.text.x = element_text(vjust = 1, hjust = 0.5),
        text = element_text(family = "Gill Sans MT", size = 17)) +
  guides(fill = "none")

artefact_type_chronology

#The plot is then saved as a PNG with altered width and height
ggsave("artefact_type_chronology.png", plot = artefact_type_chronology, width = 3.5, height = 5.5, units = "in", dpi = 300)

################################################################################
#PART 3: Function for generating skipgrams and calculating PMI##################

#Converting the text data to a corpus
corpus <- corpus(data$Motifs_as_text)
#the 'NA is replace by empty string' message is due to one decorated object not 
#fitting with the motif classification scheme.

#Setting the 't' value (total number of rows/objects/"sentences" in the corpus).
#This is set to 482 rather than the actual number (483) because of the one
#empty string ("painted bands and fields")
t <- 482

#Setting the 'n' and 'k' values
#(We'll later change the 'n' value to 3 and 4 for tri- and quadrigram analyses)
n <- 2
k <- 0:13

#The function below generates a data table with skipgrams and associated
#PMI measures, and allows us to later run the function again at different n-values
#and data subsets. It is also possible to run the function manually one line at a
#time in order to more closely follow the calculation steps.
ngramfunction <- function(n, k, corpus, token_freqs) {
  # tokenizing the corpus
  toks <- tokens(corpus)
  
  # creating the k-skip-n-grams
  ksngrams <- tokens_ngrams(toks, n = n, skip = k, concatenator = " ")
  
  # creating a document-feature matrix
  dfm <- dfm(ksngrams)
  
  # calculating the frequency of each k-skip-n-gram:
  if (n == 2) {
    bigramfreqs <- colSums(dfm)
  }
  if (n == 3) {
    trigramfreqs <- colSums(dfm)
  }
  if (n == 4) {
    quadrigramfreqs <- colSums(dfm)
  }
  
  # Creating a data frame with k-skip-n-grams and their observed frequencies
  if (n == 2) {
    ksngram_freq <- data.frame(ksngrams = names(bigramfreqs), observed_freq = bigramfreqs)
  }
  if (n == 3) {
    ksngram_freq <- data.frame(ksngrams = names(trigramfreqs), observed_freq = trigramfreqs)
  }
  if (n == 4) {
    ksngram_freq <- data.frame(ksngrams = names(quadrigramfreqs), observed_freq = quadrigramfreqs)
  }
  ksngram_freq$token1 <- sapply(strsplit(ksngram_freq$ksngrams, " "), `[`, 1)
  ksngram_freq$token2 <- sapply(strsplit(ksngram_freq$ksngrams, " "), `[`, 2)
  ##NEXT LINE IF RUNNING TRIGRAMS##
  if (n >= 3) {
    ksngram_freq$token3 <- sapply(strsplit(ksngram_freq$ksngrams, " "), `[`, 3)
  }
  ##NEXT LINE IF RUNNING QUADRIGRAMS##
  if (n >= 4) {
    ksngram_freq$token4 <- sapply(strsplit(ksngram_freq$ksngrams, " "), `[`, 4)
  }
  
  # Creating a vector of all tokens
  dfm_toks <- dfm(toks)
  token_freqs <- colSums(dfm_toks)
  all_tokens <- names(token_freqs)
  
  # Adding columns for token frequencies
  ksngram_freq$token1_freq <- token_freqs[match(ksngram_freq$token1, all_tokens)]
  ksngram_freq$token2_freq <- token_freqs[match(ksngram_freq$token2, all_tokens)]
  # Next line if we're running trigrams
  if (n >= 3) {
    ksngram_freq$token3_freq <- token_freqs[match(ksngram_freq$token3, all_tokens)]
  }
  # Next line if we're running quadrigrams
  if (n >= 4) {
    ksngram_freq$token4_freq <- token_freqs[match(ksngram_freq$token4, all_tokens)]
  }
  
  # Calculating the expected frequency for each ksngram
  # For bigrams:
  if (n == 2) {
    ksngram_freq$expected_freq <- ((ksngram_freq$token1_freq/t) * (ksngram_freq$token2_freq/t)) * t
  }
  # For trigrams:
  if (n == 3) {
    ksngram_freq$expected_freq <- ((ksngram_freq$token1_freq/t) * (ksngram_freq$token2_freq/t) * (ksngram_freq$token3_freq/t)) * t
  }
  # For quadrigrams:
  if (n == 4) {
    ksngram_freq$expected_freq <- ((ksngram_freq$token1_freq/t) * (ksngram_freq$token2_freq/t) * (ksngram_freq$token3_freq/t) * (ksngram_freq$token4_freq/t)) * t
  }
  
  # Calculating PMI for bigrams:
  if (n == 2) {
    # Defining PMI function
    calculate_PMI <- function(observed_freq, token1_freq, token2_freq, expected_freq) {
      pmi <- log(observed_freq / expected_freq)
      return(pmi)
    }
    
    # Apply the function to create the PMI column
    ksngram_freq$PMI <- with(ksngram_freq, calculate_PMI(observed_freq, token1_freq, token2_freq, expected_freq))
  }
  
  # Calculating PMI for trigrams:
  if (n == 3) {
    # Defining PMI function for trigrams
    calculate_PMI_trigram <- function(observed_freq, token1_freq, token2_freq, token3_freq, expected_freq) {
      pmi <- log(observed_freq / expected_freq)
      return(pmi)
    }
    
    ksngram_freq$PMI <- with(ksngram_freq, calculate_PMI_trigram(observed_freq, token1_freq, token2_freq, token3_freq, expected_freq))
  }
  
  # Calculating PMI for quadrigrams:
  if (n == 4) {
    # Defining PMI function for quadrigrams
    calculate_PMI_quadrigram <- function(observed_freq, token1_freq, token2_freq, token3_freq, token4_freq, expected_freq) {
      pmi <- log(observed_freq / expected_freq)
      return(pmi)
    }
    
    ksngram_freq$PMI <- with(ksngram_freq, calculate_PMI_quadrigram(observed_freq, token1_freq, token2_freq, token3_freq, token4_freq, expected_freq))
  }
  
  return(ksngram_freq)
}

#By changing the n-value and then running the above function, we can generate data
#tables for all bigrams, trigrams, and quadrigrams, respectively:
n <- 2
bigrams <- ngramfunction(n, k, corpus, token_freqs)
head(bigrams)

n <- 3
trigrams <- ngramfunction(n, k, corpus, token_freqs)
head(trigrams)

n <- 4
quadrigrams <- ngramfunction(n, k, corpus, token_freqs)
head(quadrigrams)

################################################################################
#PART 4: Skipgram frequencies at different n-levels#############################
#The below code is the output used to produce Table 1 ("The combination of ornament
#variants on the corpus of southern Scandinavian Mesolithic art as revealed by
#the successive levels of skipgram analysis (with skip distance, k, set to 13).")
#The table was not produced directly here in R, but subsequently copied into an MS Word table.


#Unigram frequencies
freqs <- colSums(data[,31:289])
freqs <- freqs[freqs != 0]
table(freqs)
#Bigram frequencies
{n <- 2
  toks <- tokens(corpus)
  ksngrams <- tokens_ngrams(toks, n = n, skip = k, concatenator = " ")
  dfm <- dfm(ksngrams)
  bigramfreqs <- colSums(dfm)
  table(bigramfreqs)}
#Trigram frequencies
{n <- 3
  toks <- tokens(corpus)
  ksngrams <- tokens_ngrams(toks, n = n, skip = k, concatenator = " ")
  dfm <- dfm(ksngrams)
  trigramfreqs <- colSums(dfm)
  table(trigramfreqs)}
#Quadrigram frequencies
{n <- 4
  toks <- tokens(corpus)
  ksngrams <- tokens_ngrams(toks, n = n, skip = k, concatenator = " ")
  dfm <- dfm(ksngrams)
  quadrigramfreqs <- colSums(dfm)
  table(quadrigramfreqs)}

#Total no. of unigrams
length(freqs)
#Total no. of bigrams
length(bigramfreqs)
#Total no. of trigrams
length(trigramfreqs)
#Total no. of quadrigrams
length(quadrigramfreqs)

################################################################################
#PART 5: Culture complex-subsets and associated PMI summary statistics###############
#The following calculations produce Table 2, by subsetting the corpus to each of
#the three culture complexes and comparing PMI summary statistics. We'll use the
#'ngramfunction' function from line 97.

#Subsetting the Maglemose data
maglemosedata <- subset(data, Chronology == "Maglemose")

#Subsetting the Kongemose data
kongemosedata <- subset(data, Chronology == "Kongemose")

#Subsetting the Ertebølle data
ertebølledata <- subset(data, Chronology == "Ertebølle")

#Generate skipgrams and PMI values for each of the culture-complex subsets
#(at the level of bigrams only)
n <- 2

corpus <- corpus(maglemosedata$Motifs_as_text)
magle_ksngrams <- ngramfunction(n, k, corpus, token_freqs)
head(magle_ksngrams)

corpus <- corpus(kongemosedata$Motifs_as_text)
konge_ksngrams <- ngramfunction(n, k, corpus, token_freqs)
head(konge_ksngrams)

#Once again, the error message "NA is replaced by empty string" is simply due to
#one motif code not conforming to the classification scheme
corpus <- corpus(ertebølledata$Motifs_as_text)
erte_ksngrams <- ngramfunction(n, k, corpus, token_freqs)
head(erte_ksngrams)

#Matching skipgrams occurring in each period with the overall stats:
#In other words, this step ensures that the PMI value of a given motif
#co-occurrence is not calculated based on the culture-complex-subsetted data,
#but rather the data in its entirety. The data is also subset to observed freqs.
#>2, as those below are deemed too statistically uncertain.

corpus <- corpus(data$Motifs_as_text)
bigrams <- ngramfunction(n, k, corpus, token_freqs)

magle_ksngram_stats <- bigrams[match(magle_ksngrams$ksngrams, bigrams$ksngrams, nomatch = 0), ]
magle_ksngram_subset <- magle_ksngram_stats[magle_ksngram_stats$observed_freq > 2,]

konge_ksngram_stats <- bigrams[match(konge_ksngrams$ksngrams, bigrams$ksngrams, nomatch = 0), ]
konge_ksngram_subset <- konge_ksngram_stats[konge_ksngram_stats$observed_freq > 2,]

erte_ksngram_stats <- bigrams[match(erte_ksngrams$ksngrams, bigrams$ksngrams, nomatch = 0), ]
erte_ksngram_subset <- erte_ksngram_stats[erte_ksngram_stats$observed_freq > 2,]

#Outputting the summary PMI stats - these are the values used in Table 2.  As in
#the above section, the table was not produced in R, but the outputs copied into
#a word table and rounded to two decimal places.
summary(magle_ksngram_subset$PMI)
summary(konge_ksngram_subset$PMI)
summary(erte_ksngram_subset$PMI)

################################################################################
#PART 6: Stacked bar plots of skipgrams by frequency and PMI####################
#In the following, six chronologically stacked bar plots are produced, as seen in
#Fig. 3: bigrams, trigrams, and quadrigrams, sorted by frequency and PMI, respectively.
#The first part generates the bigram plots, and the code is then more or less
#repeated for the tri- and quadrigrams.

#Subsetting by raw frequency (>9 is just an arbitrary threshold)
bigrams_subset <- subset(bigrams, observed_freq > 9)

#Sorting by observed freq.
bigrams_subset <- bigrams_subset %>% arrange(desc(observed_freq))

#Creating a new object, sorted by PMI in descending order
bigrams_PMI <- bigrams %>% arrange(desc(PMI))

#Subsetting this object to exclude observed freq's below 3 (as these PMI's are
#the most dubious)
bigrams_PMI <- subset(bigrams_PMI, observed_freq > 2)

#Only including the highest 21 PMI scores (once again, an arbitrary number, simply
#set to 21 because there are only 21 bigrams with observed frequencies above 9. Making
#this equal results in visually matching bar plots)
bigrams_PMI21 <- head(bigrams_PMI, 21)

#To make the bar plots stacked, we need to add the chronology variable. As most
#of the skipgrams are attributed to more than one chronology level, we need to
#change the shape of the data, connecting each co-occurrence to its corresponding
#chronology

#Changing the 'ksngrams' column contents to uppercase, in order to match it to
#the original data
bigrams_subset$ksngrams <- toupper(bigrams_subset$ksngrams)
bigrams_PMI21$ksngrams <- toupper(bigrams_PMI21$ksngrams)

#Making a new object with only the chronology variable and the individual motifs
chrongrams <-data[,c(11,31:289)]

#The following function reshapes the data to include the chronological attribution
#of each individual artefact with a given motif combination
createResultTable <- function(data) {
  result_tables <- list()
  skipgrams <- unique(data$ksngrams)
  
  for (skipgram in skipgrams) {
    filter_condition <- paste(strsplit(skipgram, " ")[[1]], "== 1", collapse = " & ")
    filtered_data <- chrongrams %>% filter(eval(parse(text = filter_condition)))
    
    result_table <- table(filtered_data$Chronology)
    result_tables[[skipgram]] <- data.frame(Skipgram = skipgram, Chronology = names(result_table), Frequency = as.numeric(result_table))
  }
  
  final_result <- do.call(rbind, result_tables)
  return(final_result)
}

skipgramsFreq <- createResultTable(bigrams_subset)
skipgramsPMI <- createResultTable(bigrams_PMI21)

#Adding PMI values
bigrams$ksngrams <- toupper(bigrams$ksngrams)

skipgramsFreq$PMI <- bigrams$PMI[match(skipgramsFreq$Skipgram, bigrams$ksngrams)]
skipgramsPMI$PMI <- bigrams$PMI[match(skipgramsPMI$Skipgram, bigrams$ksngrams)]

#Extracting unique skipgrams from ksngram_freq_subset and set the order
skipgram_order1 <- unique(bigrams_subset$ksngrams)

#Making sure to plot only one PMI value per stacked bar
summary_freq <- skipgramsFreq %>%
  distinct(Skipgram, .keep_all = TRUE)

#Plotting the skipgrams by frequency, stacked by chronology
bigramsBYfrequency <- ggplot(skipgramsFreq, aes(x = Frequency, fill = Chronology, y = reorder(Skipgram, desc(match(Skipgram, skipgram_order1))))) +
  geom_col(position = "stack") +
  geom_text(data = summary_freq, aes(label = sprintf("%.4f", PMI)), #Paste sprintf("%.4f", PMI instead on '""' to show the PMI)
            position = position_stack(vjust = 0), color = "black", size = 3) +
  scale_fill_manual(values = c("#FAD02E", "#D98888", "#E8BB8B", "#B4A1C1")) +
  xlab("Frequency") +
  ylab("Co-occurrence") +
  theme(plot.title = element_text(size = 13, face = "bold", hjust = 0.5),
        legend.text = element_text(size = 10),
        legend.title = element_blank(),
        legend.position = c(0.85, 0.15), #I get an error message due to this legend.position, but it seems to work nonetheless
        legend.background = element_rect(fill = "transparent"),
        axis.text.x = element_text(vjust = 0.4, hjust = 1),
        text = element_text(size = 14, family = "Gill Sans MT")) +
  ggtitle("Most frequent bigrams")

bigramsBYfrequency

#Doing the same thing as above, but plotting by PMI

# Making sure to plot only one PMI value per stacked bar
summary_pmi <- skipgramsPMI %>%
  distinct(Skipgram, .keep_all = TRUE)

bigramsBYpmi <- ggplot(skipgramsPMI, aes(x = Frequency, fill = Chronology, y = reorder(Skipgram, PMI))) +
  geom_col(position = "stack") +
  geom_text(data = summary_pmi, aes(label = sprintf("%.4f", PMI)), #Paste sprintf("%.4f", PMI instead on '""' to show the PMI)
            position = position_stack(vjust = 0), color = "black", size = 3) +
  scale_fill_manual(values = c("#FAD02E", "#D98888", "#E8BB8B", "#B4A1C1")) +
  xlab("Frequency") +
  ylab("Co-occurrence") +
  theme(plot.title = element_text(size = 13, face = "bold", hjust = 0.5),
        axis.text.x = element_text(vjust = 1, hjust = 0.5),
        text = element_text(size = 14, family = "Gill Sans MT")) +
  ggtitle("Bigrams by highest PMI value")+
  guides(fill = "none")

bigramsBYpmi

#Next up are tri- and quadrigrams, both sorted by frequency and by PMI. The above
#code is more or less repeated in the following, only with different object names
#and thresholds. You may run the code all at once (using the below curly braces),
#or go through it one line at a time while reading the annotations.
{

  n <- 3
  trigrams <- ngramfunction(n, k, corpus, token_freqs)
  
#Subsetting by raw frequency (the >4 arbitrary threshold is fitting for our trigrams)
trigrams_subset <- subset(trigrams, observed_freq > 4)

#Sorting by observed freq.
trigrams_subset <- trigrams_subset %>% arrange(desc(observed_freq))

#Creating a new object, sorted by PMI in descending order
trigrams_PMI <- trigrams %>% arrange(desc(PMI))

#Subsetting this object to exclude observed frequencies below 3 (as these PMI's are
#the most dubious)
trigrams_PMI <- subset(trigrams_PMI, observed_freq > 2)

#Only including the highest 23 PMI scores (once again, an arbitrary number, this
#time set to 23 as there are only 23 bigrams with observed frequencies above 4.
trigrams_PMI23 <- head(trigrams_PMI, 23)

#To make the bar plots stacked, we need to add the chronology variable. As most
#of the skipgrams are attributed to more than one chronology level, we need to
#change the shape of the data, connecting each co-occurrence to its corresponding
#chronology

#Changing the 'ksngrams' column contents to uppercase, in order to match it to
#the original data
trigrams_subset$ksngrams <- toupper(trigrams_subset$ksngrams)
trigrams_PMI23$ksngrams <- toupper(trigrams_PMI23$ksngrams)

skipgramsFreq <- createResultTable(trigrams_subset)
skipgramsPMI <- createResultTable(trigrams_PMI23)

#Adding PMI values
trigrams$ksngrams <- toupper(trigrams$ksngrams)

skipgramsFreq$PMI <- trigrams$PMI[match(skipgramsFreq$Skipgram, trigrams$ksngrams)]
skipgramsPMI$PMI <- trigrams$PMI[match(skipgramsPMI$Skipgram, trigrams$ksngrams)]

#Extracting unique skipgrams from ksngram_freq_subset and setting the order
skipgram_order2 <- unique(trigrams_subset$ksngrams)

#Making sure to plot only one PMI value per stacked bar
summary_freq <- skipgramsFreq %>%
  distinct(Skipgram, .keep_all = TRUE)

#Plotting the skipgrams by frequency, stacked by chronology
trigramsBYfrequency <- ggplot(skipgramsFreq, aes(x = Frequency, fill = Chronology, y = reorder(Skipgram, desc(match(Skipgram, skipgram_order2))))) +
  geom_col(position = "stack") +
  geom_text(data = summary_freq, aes(label = sprintf("%.4f", PMI)), #Paste sprintf("%.4f", PMI instead on '""' to show the PMI)
            position = position_stack(vjust = 0), color = "black", size = 3) +
  scale_fill_manual(values = c("#FAD02E", "#D98888", "#E8BB8B", "#B4A1C1")) +
  xlab("Frequency") +
  ylab("Co-occurrence") +
  theme(plot.title = element_text(size = 13, face = "bold", hjust = 0.5),
        legend.text = element_text(size = 10),
        legend.title = element_blank(),
        legend.position = c(0.85, 0.15),
        legend.background = element_rect(fill = "transparent"),
        axis.text.x = element_text(vjust = 0.4, hjust = 1),
        text = element_text(size = 14, family = "Gill Sans MT")) +
  ggtitle("Most frequent trigrams")

#Doing the same thing as above, but plotting by PMI

# Making sure to plot only one PMI value per stacked bar
summary_pmi <- skipgramsPMI %>%
  distinct(Skipgram, .keep_all = TRUE)

trigramsBYpmi <- ggplot(skipgramsPMI, aes(x = Frequency, fill = Chronology, y = reorder(Skipgram, PMI))) +
  geom_col(position = "stack") +
  geom_text(data = summary_pmi, aes(label = sprintf("%.4f", PMI)), #Paste sprintf("%.4f", PMI instead on '""' to show the PMI)
            position = position_stack(vjust = 0), color = "black", size = 3) +
  scale_fill_manual(values = c("#FAD02E", "#D98888", "#B4A1C1")) +
  xlab("Frequency") +
  ylab("Co-occurrence") +
  theme(plot.title = element_text(size = 13, face = "bold", hjust = 0.5),
        axis.text.x = element_text(vjust = 1, hjust = 0.5),
        text = element_text(size = 14, family = "Gill Sans MT")) +
  ggtitle("Trigrams by highest PMI value")+
  guides(fill = "none")

#Finally, we'll do the same thing as above but for quadrigrams:
n <- 4
quadrigrams <- ngramfunction(n, k, corpus, token_freqs)

#Subsetting by raw frequency (the >2 arbitrary threshold is fitting for our quadrigrams)
quadrigrams_subset <- subset(quadrigrams, observed_freq > 2)

#Sorting by observed freq.
quadrigrams_subset <- quadrigrams_subset %>% arrange(desc(observed_freq))

#Creating a new object, sorted by PMI in descending order
quadrigrams_PMI <- quadrigrams %>% arrange(desc(PMI))

#Subsetting this object to exclude observed freq's below 3 (as these PMI's are
#the most dubious)
quadrigrams_PMI <- subset(quadrigrams_PMI, observed_freq > 2)

#Only including the highest 20 PMI scores (once again, an arbitrary number, this
#time set to 20 as there are only 20 quadrigrams with observed freq's above 2.
quadrigrams_PMI20 <- head(quadrigrams_PMI, 20)

#To make the bar plots stacked, we need to add the chronology variable. As most
#of the skipgrams are attributed to more than one chronology level, we need to
#change the shape of the data, connecting each co-occurrence to its corresponding
#chronology

#Changing the 'ksngrams' column contents to uppercase, in order to match it to
#the original data
quadrigrams_subset$ksngrams <- toupper(quadrigrams_subset$ksngrams)
quadrigrams_PMI20$ksngrams <- toupper(quadrigrams_PMI20$ksngrams)

skipgramsFreq <- createResultTable(quadrigrams_subset)
skipgramsPMI <- createResultTable(quadrigrams_PMI20)

#Adding PMI values
quadrigrams$ksngrams <- toupper(quadrigrams$ksngrams)

skipgramsFreq$PMI <- quadrigrams$PMI[match(skipgramsFreq$Skipgram, quadrigrams$ksngrams)]
skipgramsPMI$PMI <- quadrigrams$PMI[match(skipgramsPMI$Skipgram, quadrigrams$ksngrams)]

#Extracting unique skipgrams from ksngram_freq_subset and set the order
skipgram_order3 <- unique(quadrigrams_subset$ksngrams)

#Making sure to plot only one PMI value per stacked bar
summary_freq <- skipgramsFreq %>%
  distinct(Skipgram, .keep_all = TRUE)

#Plotting the skipgrams by frequency, stacked by chronology
quadrigramsBYfrequency <- ggplot(skipgramsFreq, aes(x = Frequency, fill = Chronology, y = reorder(Skipgram, desc(match(Skipgram, skipgram_order3))))) +
  geom_col(position = "stack") +
  geom_text(data = summary_freq, aes(label = sprintf("%.4f", PMI)),
            position = position_stack(vjust = 0), color = "black", size = 3) +
  scale_fill_manual(values = c("#FAD02E", "#D98888", "#B4A1C1")) +
  xlab("Frequency") +
  ylab("Co-occurrence") +
  theme(plot.title = element_text(size = 13, face = "bold", hjust = 0.5),
        legend.text = element_text(size = 10),
        legend.title = element_blank(),
        legend.position = c(0.85, 0.15),
        legend.background = element_rect(fill = "transparent"),
        axis.text.x = element_text(vjust = 0.4, hjust = 1),
        text = element_text(size = 14, family = "Gill Sans MT")) +
  ggtitle("Most frequent quadrigrams")

#Doing the same thing, but plotting by PMI

# Making sure to plot only one PMI value per stacked bar
summary_pmi <- skipgramsPMI %>%
  distinct(Skipgram, .keep_all = TRUE)

quadrigramsBYpmi <- ggplot(skipgramsPMI, aes(x = Frequency, fill = Chronology, y = reorder(Skipgram, PMI))) +
  geom_col(position = "stack") +
  geom_text(data = summary_pmi, aes(label = sprintf("%.4f", PMI)), #Paste sprintf("%.4f", PMI instead on '""' to show the PMI)
            position = position_stack(vjust = 0), color = "black", size = 3) +
  scale_fill_manual(values = c("#FAD02E", "#D98888", "#B4A1C1")) +
  xlab("Frequency") +
  ylab("Co-occurrence") +
  theme(plot.title = element_text(size = 13, face = "bold", hjust = 0.5),
        axis.text.x = element_text(vjust = 1, hjust = 0.5),
        text = element_text(size = 14, family = "Gill Sans MT")) +
  ggtitle("Quadrigrams by highest PMI value")+
  guides(fill = "none")
}

#In the above, we have generated these six stacked bar plots, as used in Fig. 3:
bigramsBYfrequency
bigramsBYpmi
trigramsBYfrequency
trigramsBYpmi
quadrigramsBYfrequency
quadrigramsBYpmi

#Exporting the plots as PNG's
ggsave("bigramsBYfrequency.png", plot = bigramsBYfrequency, width = 6, height = 5, units = "in", dpi = 300)
ggsave("bigramsBYpmi.png", plot = bigramsBYpmi, width = 6, height = 5, units = "in", dpi = 300)
ggsave("trigramsBYfrequency.png", plot = trigramsBYfrequency, width = 6, height = 5, units = "in", dpi = 300)
ggsave("trigramsBYpmi.png", plot = trigramsBYpmi, width = 6, height = 5, units = "in", dpi = 300)
ggsave("quadrigramsBYfrequency.png", plot = quadrigramsBYfrequency, width = 6, height = 5, units = "in", dpi = 300)
ggsave("quadrigramsBYpmi.png", plot = quadrigramsBYpmi, width = 6, height = 5, units = "in", dpi = 300)

#Combining the six plots and a few additional, aesthetic tweaks were performed
#in the free image editing software GIMP

################################################################################
#PART 7: PMI bigram heatmap#####################################################
#This part produces the 'skeleton' for the Fig. 4 heatmap, visualising the bigrams
#with the highest PMI values in an attempt at chronological ordering. Quite a lot
#of additional aesthetics were subsequently added in the 'GIMP' software.

#Subsetting to observed frequencies of 3 or above (once again, due to the PMI values
#being increasingly uncertain at low observed freqs)
bigrams <- subset(bigrams, observed_freq > 2)

#Getting unique token values from ksngram_freq
tokens <- unique(c(as.character(bigrams$token1), as.character(bigrams$token2)))

#Creating empty matrix with token names as column and row names
m <- matrix(0, nrow = length(tokens), ncol = length(tokens), dimnames = list(tokens, tokens))

#Filling the matrix with PMI values from ksngram_freq
for (i in 1:nrow(bigrams)) {
  row_index <- match(bigrams[i, "token1"], tokens)
  col_index <- match(bigrams[i, "token2"], tokens)
  m[row_index, col_index] <- bigrams[i, "PMI"]
  m[col_index, row_index] <- bigrams[i, "PMI"]
}

# Defining the matrix and reorder the rows and columns
#(this manual chronological ordering is based on analyses not presented here)
m <- m[c("a14","b3","a24","b10","b2","b12","e4","a5","d5","b13","b4","b1","a1","a3","ant",
         "f12","e1","b6","e5","f5","f13","f38","d29","b8","d33","h1","g2","c1","f14","i1",
         "f35","zoo","d19","g1","d3","d15","f15","c12","c14","c5","c13","c4","c6","d7",
         "f55","g7","i13","i5","relief"), 
       c("a14","b3","a24","b10","b2","b12","e4","a5","d5","b13","b4","b1","a1","a3","ant",
         "f12","e1","b6","e5","f5","f13","f38","d29","b8","d33","h1","g2","c1","f14","i1",
         "f35","zoo","d19","g1","d3","d15","f15","c12","c14","c5","c13","c4","c6","d7",
         "f55","g7","i13","i5","relief")]

#Converting the matrix to a data frame for ggplot2
df <- as.data.frame.table(m)
names(df) <- c("token1", "token2", "PMI")

#Plotting the heatmap
heatmap <- ggplot(df, aes(x = token2, y = token1, fill = PMI)) +
  geom_tile(color = "gray90") +
  scale_fill_gradient2(low = "white", mid = "white", high = "red",
                       midpoint = 0.5, name = "PMI") +
  labs(x = "Token 2", y = "Token 1", title = "Co-occurrence matrix") +
  theme(axis.text.x = element_text(angle = 90, hjust = 1, vjust = 0.4),
        plot.title = element_text(size = 14, face = "bold", hjust = 0.5),
        text = element_text(family = "Gill Sans MT", size = 12),
        legend.text = element_text(size = 10)) +
  scale_x_discrete(limits = c("a14","b3","a24","b10","b2","b12","e4","a5","d5","b13","b4","b1","a1","a3","ant",
                              "f12","e1","b6","e5","f5","f13","f38","d29","b8","d33","h1","g2","c1","f14","i1",
                              "f35","zoo","d19","g1","d3","d15","f15","c12","c14","c5","c13","c4","c6","d7",
                              "f55","g7","i13","i5","relief"),
                   labels = toupper,
                   name = NULL,
                   drop = FALSE) +
  scale_y_discrete(limits = c("a14","b3","a24","b10","b2","b12","e4","a5","d5","b13","b4","b1","a1","a3","ant",
                              "f12","e1","b6","e5","f5","f13","f38","d29","b8","d33","h1","g2","c1","f14","i1",
                              "f35","zoo","d19","g1","d3","d15","f15","c12","c14","c5","c13","c4","c6","d7",
                              "f55","g7","i13","i5","relief"),
                   labels = toupper,
                   name = NULL,
                   drop = FALSE) +
  ggtitle("Motif co-occurrence heatmap by PMI")

heatmap

ggsave("heatmapPMI.png", plot = heatmap, width = 8, height = 8, units = "in", dpi = 300)

#The rest of the figure (adjusting axis labels and adding coloured boxes etc.)
#was then subsequently performed in the free image editing software GIMP.

################################################################################
#PART 8: Exporting data tables##################################################

#Exporting all generated bi-, tri-, and quadrigrams. We once again subset to
#observed freqs >2 and sort by PMI. The exported data tables are available as
#Supplementary Material "Herskind&Riede_S3.xlsx"

#Bigrams:
bigrams$token1 <- toupper(bigrams$token1)
bigrams$token2 <- toupper(bigrams$token2)

bigrams <- bigrams %>%
  select(token1, token2, token1_freq, token2_freq, observed_freq, expected_freq, PMI)

#Converting the data frame to a data table
bigrams_dt <- as.data.table(bigrams)

#Subsetting to observed frequencies >2 and arranging by PMI
bigrams_dt <- subset(bigrams_dt, observed_freq > 2)
bigrams_dt <- bigrams_dt %>% arrange(desc(PMI))

#Writing the data table to a file (adjust name correspondingly)
fwrite(bigrams_dt, "Bigrams.csv")

#Trigrams:
trigrams$token1 <- toupper(trigrams$token1)
trigrams$token2 <- toupper(trigrams$token2)
trigrams$token3 <- toupper(trigrams$token3)

trigrams <- trigrams %>%
  select(token1, token2, token3, token1_freq, token2_freq, token3_freq, observed_freq, expected_freq, PMI)

#Converting the data frame to a data table
trigrams_dt <- as.data.table(trigrams)

#Subsetting to observed frequencies >2 and arranging by PMI
trigrams_dt <- subset(trigrams_dt, observed_freq > 2)
trigrams_dt <- trigrams_dt %>% arrange(desc(PMI))

#Writing the data table to a file (adjust name correspondingly)
fwrite(trigrams_dt, "Trigrams.csv")

#Quadrigrams:
quadrigrams$token1 <- toupper(quadrigrams$token1)
quadrigrams$token2 <- toupper(quadrigrams$token2)
quadrigrams$token3 <- toupper(quadrigrams$token3)
quadrigrams$token4 <- toupper(quadrigrams$token4)

quadrigrams <- quadrigrams %>%
  select(token1, token2, token3, token4, token1_freq, token2_freq, token3_freq, token4_freq, observed_freq, expected_freq, PMI)

#Converting the data frame to a data table
quadrigrams_dt <- as.data.table(quadrigrams)

#Subsetting to observed frequencies >2 and arranging by PMI
quadrigrams_dt <- subset(quadrigrams_dt, observed_freq > 2)
quadrigrams_dt <- quadrigrams_dt %>% arrange(desc(PMI))

#Writing the data table to a file (adjust name correspondingly)
fwrite(quadrigrams_dt, "Quadrigrams.csv")

#Combining the data tables into one Excel document, as well as some aesthetic
#adjustments were subsequently performed in Excel.
