######## Input file formatting instructions ####################################
# Each dataset should be placed in a separate column.
# Each column should have a name, which should be without spaces or special symbols.
# Data should comprise only numbers.
# Duplicates (multiple records with the same value should be avoided, such entries should be made different (e.g. three numbers 4 can be differentiated by adding decimals - 4.00, 4.33, and 4.66).
# Document should be saved as a csv file.
# Correct address of the saved input and output documents should be entered in rows 16 and 69 of the script, respectively.

####### Loading libraries, initiating time measuring (duration of the simuulations) ############################
library(beepr)

######## OLE calculation function (taken and adapted from sExtinct package) ####################################
OLE.test <-
  function(dd, alpha){
    # records are sorted in a reverse order, as required by OLE method
    sights <- rev(sort(dd))
    # calculation of k, v, e, lambda and other values
    k <- length(sights)
    v <- (1/(k-1)) * sum(log((sights[1] - sights[k])/(sights[1] - sights[2:(k-1)])))
    e <- matrix(rep(1,k), ncol=1)
    SU<-(-log(alpha)/length(sights))^-v
    myfun <- function(i,j,v){(gamma(2*v+i)*gamma(v+j))/(gamma(v+i)*gamma(j))}
    lambda <- outer(1:k, 1:k, myfun, v=v)
    lambda <- ifelse(lower.tri(lambda), lambda, t(lambda)) 
    a <- as.vector(solve(t(e)%*%solve(lambda)%*%e)) * solve(lambda)%*%e
    # calculation of CI ("upperCI") and extinction time ("extest")
    upperCI<-max(sights) + ((max(sights)-min(sights))/(SU-1))
    extest<-sum(t(a)%*%sights)
    # return of results produced by the function
    res<-data.frame(Estimate=extest, upperCI=upperCI)
    return(res)	
  }


##################################
########      PHASE A     ########
##################################


####### Loading file with data  ################################################################################
# data file that is loaded needs to have four columns: 1) number of the dataset; 2) mean age estimates; 3) minimum age range estimate; 4) maximum age range estimate
# Address of the data file should be corrected to its location on the computer
datalist_A <- read.csv("###file location###")[,-1]
datalist_A$Thickness[which(datalist_A$Thickness == max(datalist_A$Thickness))] <- mean(datalist_A$Thickness)

datalist_A_rn <- datalist_A

## Prepare data for randomised loop
it <- 1000 # Number of iterations

Length_A <- as.data.frame(matrix(nrow = it, ncol = 6))
colnames(Length_A) <- c("Min","Max","Min.TE","Min.CI","Max.TE","Max.CI")
Breadth_A <- as.data.frame(matrix(nrow = it, ncol = 6))
colnames(Breadth_A) <- c("Min","Max","Min.TE","Min.CI","Max.TE","Max.CI")
Thickness_A <- as.data.frame(matrix(nrow = it, ncol = 6))
colnames(Thickness_A) <- c("Min","Max","Min.TE","Min.CI","Max.TE","Max.CI")
Area_A <- as.data.frame(matrix(nrow = it, ncol = 6))
colnames(Area_A) <- c("Min","Max","Min.TE","Min.CI","Max.TE","Max.CI")

## Radomise x with mean x and standard deviation ssdd (to avoid to many identic numbers)
ssdd <- 0.001 ## Standard deviation for rand

## Start loop for randomisation

for (j in 1:it){
  for (i in 1:4){
    rnmdsd <- rnorm(nrow(datalist_A_rn),datalist_A[,i],ssdd)
    datalist_A_rn[,i] <- rnmdsd
  }
  
  ####### Alpha/significance value and size of the sighting record analyzed###################################
  alpha <- 0.05
  k.size <- 10
  
  ######### Creating tables for results ##########################################################################
  OLE.results_A_rn <- matrix(0,length(datalist_A_rn[1,])+1,7)
  OLE.results_A_rn[2:(length(datalist_A_rn[1,])+1),1] <- colnames(datalist_A_rn)
  OLE.results_A_rn[1,2:7] <- c("Min","Max","Min.TE","Min.CI","Max.TE","Max.CI")
  
  ####### applying OLE to each of the eight datasets ###########################################################
  for (i in 1:length(datalist_A_rn[1,])) {
    data.i <- sort(datalist_A_rn[,i])
    OLE.results_A_rn[i+1,2:3] <- c(min(data.i),max(data.i))
    max.range.data <- rev(sort(data.i)); max.range.data <- max.range.data[1:k.size]
    min.range.data <- sort(data.i); min.range.data <- min.range.data[1:k.size]
    min.range.data.b <- max(min.range.data) - min.range.data
    max.range.data.b <- max.range.data - min(max.range.data)
    # OLE function is applied to the data
    OLE.min <- max(min.range.data) - OLE.test(min.range.data.b,alpha)
    OLE.max <- min(max.range.data) + OLE.test(max.range.data.b,alpha)
    # results are included in the matrix with results
    OLE.results_A_rn[i+1,4:5] <- c(OLE.min[[1]],OLE.min[[2]])
    OLE.results_A_rn[i+1,6:7] <- c(OLE.max[[1]],OLE.max[[2]])
  }
  
  ####### show OLE results and generate csv files with results ##################################################
  rownames(OLE.results_A_rn) <- OLE.results_A_rn[,1]
  colnames(OLE.results_A_rn) <- OLE.results_A_rn[1,]
  OLE.results_A_rn <- OLE.results_A_rn[-1,-1]
  
  OLE.results_A_rn <- as.data.frame(OLE.results_A_rn)
  
  for (i in 1:ncol(OLE.results_A_rn)){
    OLE.results_A_rn[,i] <- round(as.numeric(OLE.results_A_rn[,i]),2)
  }
  
  Length_A[j,] <- OLE.results_A_rn[1,]
  Breadth_A[j,] <- OLE.results_A_rn[2,]
  Thickness_A[j,] <- OLE.results_A_rn[3,]
  Area_A[j,] <- OLE.results_A_rn[4,]
}

OLE.results_A_rn[1,] <- round(apply(Length_A,2,mean),2)
OLE.results_A_rn[2,] <- round(apply(Breadth_A,2,mean),2)
OLE.results_A_rn[3,] <- round(apply(Thickness_A,2,mean),2)
OLE.results_A_rn[4,] <- round(apply(Area_A,2,mean),2)

print(OLE.results_A_rn)
print(summary(datalist_A_rn))
write.csv(OLE.results_A_rn, file="###file location###")


##################################
########      PHASE B     ########
##################################


####### Loading file with data  ################################################################################
# data file that is loaded needs to have four columns: 1) number of the dataset; 2) mean age estimates; 3) minimum age range estimate; 4) maximum age range estimate
# Address of the data file should be corrected to its location on the computer

#datalist_B <- read.csv("###file location###")[,-1]
datalist_B_rn <- datalist_B

## Prepare data for randomisation

Length_B <- as.data.frame(matrix(nrow = it, ncol = 6))
colnames(Length_B) <- c("Min","Max","Min.TE","Min.CI","Max.TE","Max.CI")
Breadth_B <- as.data.frame(matrix(nrow = it, ncol = 6))
colnames(Breadth_B) <- c("Min","Max","Min.TE","Min.CI","Max.TE","Max.CI")
Thickness_B <- as.data.frame(matrix(nrow = it, ncol = 6))
colnames(Thickness_B) <- c("Min","Max","Min.TE","Min.CI","Max.TE","Max.CI")
Area_B <- as.data.frame(matrix(nrow = it, ncol = 6))
colnames(Area_B) <- c("Min","Max","Min.TE","Min.CI","Max.TE","Max.CI")

## Radomise x with mean x and standard deviation ssdd (to avoid to many identic numbers)
ssdd <- 0.001 ## Standard deviation for rand

## Start loop for randomisation

for (j in 1:it){
  for (i in 1:4){
    rnmdsd <- rnorm(nrow(datalist_B_rn),datalist_B[,i],ssdd)
    datalist_B_rn[,i] <- rnmdsd
  }
  
  ####### Alpha/significance value and size of the sighting record analyzed###################################
  alpha <- 0.05
  k.size <- 10
  
  ######### Creating tables for results ##########################################################################
  OLE.results_B_rn <- matrix(0,length(datalist_B_rn[1,])+1,7)
  OLE.results_B_rn[2:(length(datalist_B_rn[1,])+1),1] <- colnames(datalist_B_rn)
  OLE.results_B_rn[1,2:7] <- c("Min","Max","Min.TE","Min.CI","Max.TE","Max.CI")
  
  ####### applying OLE to each of the eight datasets ###########################################################
  for (i in 1:length(datalist_B_rn[1,])) {
    data.i <- sort(datalist_B_rn[,i])
    OLE.results_B_rn[i+1,2:3] <- c(min(data.i),max(data.i))
    max.range.data <- rev(sort(data.i)); max.range.data <- max.range.data[1:k.size]
    min.range.data <- sort(data.i); min.range.data <- min.range.data[1:k.size]
    min.range.data.b <- max(min.range.data) - min.range.data
    max.range.data.b <- max.range.data - min(max.range.data)
    # OLE function is applied to the data
    OLE.min <- max(min.range.data) - OLE.test(min.range.data.b,alpha)
    OLE.max <- min(max.range.data) + OLE.test(max.range.data.b,alpha)
    # results are included in the matrix with results
    OLE.results_B_rn[i+1,4:5] <- c(OLE.min[[1]],OLE.min[[2]])
    OLE.results_B_rn[i+1,6:7] <- c(OLE.max[[1]],OLE.max[[2]])
  }
  
  ####### show OLE results and generate csv files with results ##################################################
  rownames(OLE.results_B_rn) <- OLE.results_B_rn[,1]
  colnames(OLE.results_B_rn) <- OLE.results_B_rn[1,]
  OLE.results_B_rn <- OLE.results_B_rn[-1,-1]
  
  OLE.results_B_rn <- as.data.frame(OLE.results_B_rn)
  
  for (i in 1:ncol(OLE.results_B_rn)){
    OLE.results_B_rn[,i] <- round(as.numeric(OLE.results_B_rn[,i]),2)
  }
  
  Length_B[j,] <- OLE.results_B_rn[1,]
  Breadth_B[j,] <- OLE.results_B_rn[2,]
  Thickness_B[j,] <- OLE.results_B_rn[3,]
  Area_B[j,] <- OLE.results_B_rn[4,]
}

OLE.results_B_rn[1,] <- round(apply(Length_B,2,mean),2)
OLE.results_B_rn[2,] <- round(apply(Breadth_B,2,mean),2)
OLE.results_B_rn[3,] <- round(apply(Thickness_B,2,mean),2)
OLE.results_B_rn[4,] <- round(apply(Area_B,2,mean),2)

OLE.results_B_rn
print(OLE.results_B_rn)
print(summary(datalist_B_rn))
write.csv(OLE.results_B_rn, file="###file location###")

OLE.results_A
OLE.results_A_rn
OLE.results_B
OLE.results_B_rn

