######## Input file formatting instructions ####################################
# Each dataset should be placed in a separate column.
# Each column should have a name, which should be without spaces or special symbols.
# Data should comprise only numbers.
# Duplicates (multiple records with the same value should be avoided, such entries should be made different (e.g. three numbers 4 can be differentiated by adding decimals - 4.00, 4.33, and 4.66).
# Document should be saved as a csv file.
# Correct address of the saved input and output documents should be entered in rows 16 and 69 of the script, respectively.


####### Loading file with data  ################################################################################
# data file that is loaded needs to have four columns: 1) number of the dataset; 2) mean age estimates; 3) minimum age range estimate; 4) maximum age range estimate
# Address of the data file should be corrected to its location on the computer
datalist <- read.csv("###file location###", header=TRUE)

####### Alpha/significance value and size of the sighting record analyzed###################################
alpha <- 0.05
k.size <- 10

######### Creating tables for results ##########################################################################
OLE.results <- matrix(0,length(datalist[1,])+1,7)
OLE.results[2:(length(datalist[1,])+1),1] <- colnames(datalist)
OLE.results[1,2:7] <- c("Min","Max","Min.TE","Min.CI","Max.TE","Max.CI")


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

####### applying OLE to each of the eight datasets ###########################################################
for (i in 1:length(datalist[1,])) {
  data.i <- sort(datalist[,i])
  OLE.results[i+1,2:3] <- c(min(data.i),max(data.i))
  max.range.data <- rev(sort(data.i)); max.range.data <- max.range.data[1:k.size]
  min.range.data <- sort(data.i); min.range.data <- min.range.data[1:k.size]
  min.range.data.b <- max(min.range.data) - min.range.data
  max.range.data.b <- max.range.data - min(max.range.data)
  # OLE function is applied to the data
  OLE.min <- max(min.range.data) - OLE.test(min.range.data.b,alpha)
  OLE.max <- min(max.range.data) + OLE.test(max.range.data.b,alpha)
  # results are included in the matrix with results
  OLE.results[i+1,4:5] <- c(OLE.min[[1]],OLE.min[[2]])
  OLE.results[i+1,6:7] <- c(OLE.max[[1]],OLE.max[[2]])
}
  
####### show OLE results and generate csv files with results ##################################################
print(OLE.results)
print(summary(datalist))
write.csv(OLE.results, file="###file location###")

