README

This document relates to the article “A computational linguistic methodology for assessing semiotic structure in prehistoric art and the meaning of southern Scandinavian Mesolithic ornamentation” (Herskind & Riede) and its associated supplementary material, available at https://zenodo.org/records/10801706.

The supplementary material includes three documents:

- "Herskind&Riede_S1.xlsx" - the MS Excel data sheet on which the analysis is based. The data are a manually extracted and digitized version of the South Scandinavian objects from T. Płonka's 2003 analogue catalogue of European Mesolithic portable art. Some of Płonka's original columns have been maintained (columns B-C, E, I-J), and several columns have been added (columns A, D, F-H, K-KD) to prepare the data for statistical analysis. The long. and lat. coordinate columns were used to produce the fig.2 map.

- "Herskind&Riede_S2.R" - the annotated R code which imports the S1 data and produces the article's analyses. When running the code, refer to the code's annotations and references to tables and figures in the article.

R version: 4.3.2

R packages used:
extrafont (v. 0.19)
data.table (v. 1.15.0)
dplyr (v. 1.1.4)
ggplot2 (v. 3.5.0)
readxl (v. 1.4.3)
quanteda (v. 3.3.1)
forcats (v. 1.0.0)

- "Herskind&Riede_S3.xlsx" - data tables of skipgram analysis results, produced in the S2 code and imported into excel. The document holds three sheets, one for each level of n-gram analysis (bigrams, trigrams, and quadrigrams).


Reference:

Płonka, Tomasz. The Portable Art of Mesolithic Europe. Acta Universitatis Wratislaviensis 2527. Wrocław: Wydawnictwo Universytetu Wrocławskiego, 2003.