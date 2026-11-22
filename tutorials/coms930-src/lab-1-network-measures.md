---
title: "Lab 1: Descriptive network measures"
subtitle: "Network analysis in R"
description: "Degree, in- and out-degree, closeness, betweenness and eigenvector centrality in an international diplomacy network, and how the measures correlate."
---

[Download R Markdown (.Rmd)](lab-1-network-measures.Rmd){.btn .btn-primary .btn-sm}

From this week's module, please download the iGraph data. I have also shared the description of the Comparative Networks Dataset (McMillan, Phadke, Goist, & Denny, 2017) on Canvas. There is a PDF file that explains the data collection procedures and an Excel file that has summaries of the data that are included.

## Reading in Data

The data itself in an R formatted data file that contains each of the data files in igraph format (iGraph_Data.rdata). You should be able to double click on the file to open it or use a line like the following to open it if you change the file path to where you have the file stored on your local device.

``` r
# load the igraph library
library(igraph)
```

``` r-output
## 
## Attaching package: 'igraph'
```

``` r-output
## The following objects are masked from 'package:stats':
## 
##     decompose, spectrum
```

``` r-output
## The following object is masked from 'package:base':
## 
##     union
```

``` r
# remember to load other libraries you need as well
library(dplyr)
```

``` r-output
## 
## Attaching package: 'dplyr'
```

``` r-output
## The following objects are masked from 'package:igraph':
## 
##     as_data_frame, groups, union
```

``` r-output
## The following objects are masked from 'package:stats':
## 
##     filter, lag
```

``` r-output
## The following objects are masked from 'package:base':
## 
##     intersect, setdiff, setequal, union
```

``` r
# set up working directory (Session --> Set Working Directory --> Choose Directory)
setwd("~/path/to/your/lab/folder")  # change this to your directory path

# read in the list of igraph data objects
load("iGraph_Data.rdata")
```

This should read in an object called igraph_data_list into your session of R. You can check that it worked with an ls() command. Once you have the data read in, you will be able to access the actual networks. They are stored in an R data type called a list. A list is R's way of collecting a set of R objects that may have different types. You can access elements of a list using double square brackets with the number of the corresponding element of the list that you want to access. Each element of the list contains three things: the network, any node-level data (i.e., individual-level variables), and metadata about the network.

For this homework, I will ask you to work with diplomacy data, which is number 18 in the list. This network has a node level data file that gives information about the nodes. You can access that in the following code:

``` r
my_net <- igraph_data_list[[18]]$network
my_net_node_data <- igraph_data_list[[18]]$node_level_data
V(my_net)$name <- my_net_node_data$COUNTRY
```

``` r-output
## This graph was created by an old(er) igraph version.
## ℹ Call `igraph::upgrade_graph()` on it to use with the current igraph version.
## For now we convert it on the fly...
```

In the above, the first line turns the network in the 18th position in the list into an object named my_net. The second line creates a separate object called my_net_node_data that has the node-level data associated with the network that is 18th in the list. Finally, the third line changes the names of the vertices in the my_net network object to be the values in the my_net_node_data\$COUNTRY column from the node-level data. There are other node-level attributes that you could add to the network with similar code if you so wished. By changing the name of the nodes to be the actual country names some of the parts of the assignment should be a little easier, but it is not actually necessary to do this.

## Questions for you to answer

Using the Diplomacy network, please answer the following: 1. What is the mean, median, and standard deviation of degree (without worrying about directionality)? What are the top 5 countries in terms of degree? 2. What is the mean, median, and standard deviation of in-degree? What are the top 5 countries in terms of in-degree? 3. What is the mean, median, and standard deviation of out-degree? What are the top 5 countries in terms of out-degree? 4. What is the mean, median, and standard deviation of closeness centrality? What are the top 5 countries in terms of closeness centrality? 5. What is the mean, median, and standard deviation of betweenness centrality? What are the top 5 countries in terms of betweenness centrality? 6. What is the mean, median, and standard deviation of eigenvector centrality? What are the top 5 countries in terms of eigenvector centrality? 7. What is the Pearson correlation between these various scores? Make a table that reports the correlation between each of degree, in-degree, outdegree, closeness centrality, betweenness centrality, and eigenvector centrality.

Write a few sentences that describe these values, noting any that are particularly high or particularly low and give a brief explanation for why that might be. Please give an explanation of at least two of the values, though you are free to describe more than two if you wish. Please share your code, either as an appendix or as a separate file, in addition to your assignment.

## Below are code that may be useful for you to answer the questions above

``` r
# Q1. Degree (ignore direction)
deg_all <- degree(my_net, mode = "all")

mean(deg_all); median(deg_all); sd(deg_all)
```

``` r-output
## [1] 30.75
```

``` r-output
## [1] 32
```

``` r-output
## [1] 9.913759
```

``` r
deg_all_top5 <- sort(deg_all, decreasing = TRUE)[1:5]
deg_all_top5
```

``` r-output
##          JAPAN  UNITED_STATES UNITED_KINGDOM          CHINA    SWITZERLAND 
##             46             46             43             41             39
```

``` r
names(deg_all_top5) 
```

``` r-output
## [1] "JAPAN"          "UNITED_STATES"  "UNITED_KINGDOM" "CHINA"         
## [5] "SWITZERLAND"
```

``` r
# Q2. In-degree
deg_in <- degree(my_net, mode = "in")

mean(deg_in); median(deg_in); sd(deg_in)
```

``` r-output
## [1] 15.375
```

``` r-output
## [1] 15
```

``` r-output
## [1] 4.301794
```

``` r
deg_in_top5 <- sort(deg_in, decreasing = TRUE)[1:5]
deg_in_top5
```

``` r-output
##          JAPAN  UNITED_STATES UNITED_KINGDOM          CHINA         BRAZIL 
##             23             23             21             20             19
```

``` r
names(deg_in_top5)
```

``` r-output
## [1] "JAPAN"          "UNITED_STATES"  "UNITED_KINGDOM" "CHINA"         
## [5] "BRAZIL"
```

``` r
# Q3. Out-degree
deg_out <- degree(my_net, mode = "out")

mean(deg_out); median(deg_out); sd(deg_out)
```

``` r-output
## [1] 15.375
```

``` r-output
## [1] 17
```

``` r-output
## [1] 5.918376
```

``` r
deg_out_top5 <- sort(deg_out, decreasing = TRUE)[1:5]
deg_out_top5
```

``` r-output
##          JAPAN  UNITED_STATES    SWITZERLAND UNITED_KINGDOM          CHINA 
##             23             23             22             22             21
```

``` r
names(deg_out_top5)
```

``` r-output
## [1] "JAPAN"          "UNITED_STATES"  "SWITZERLAND"    "UNITED_KINGDOM"
## [5] "CHINA"
```

``` r
# Q4. Closeness centrality (mode = "all" treats ties as undirected for distances)
close_all <- closeness(my_net, mode = "all", normalized = TRUE)

mean(close_all); median(close_all); sd(close_all)
```

``` r-output
## [1] 0.7991886
```

``` r-output
## [1] 0.807266
```

``` r-output
## [1] 0.1198336
```

``` r
close_top5 <- sort(close_all, decreasing = TRUE)[1:5]
close_top5
```

``` r-output
##          JAPAN  UNITED_STATES    SWITZERLAND UNITED_KINGDOM          CHINA 
##      1.0000000      1.0000000      0.9583333      0.9583333      0.9200000
```

``` r
names(close_top5)
```

``` r-output
## [1] "JAPAN"          "UNITED_STATES"  "SWITZERLAND"    "UNITED_KINGDOM"
## [5] "CHINA"
```

``` r
# Q5. Betweenness centrality
between <- betweenness(my_net, directed = TRUE, normalized = TRUE)

mean(between); median(between); sd(between)
```

``` r-output
## [1] 0.01506917
```

``` r-output
## [1] 0.00884423
```

``` r-output
## [1] 0.01819761
```

``` r
between_top5 <- sort(between, decreasing = TRUE)[1:5]
between_top5
```

``` r-output
##          JAPAN  UNITED_STATES UNITED_KINGDOM          CHINA          EGYPT 
##     0.05926370     0.05926370     0.04584539     0.04223896     0.02084578
```

``` r
names(between_top5)
```

``` r-output
## [1] "JAPAN"          "UNITED_STATES"  "UNITED_KINGDOM" "CHINA"         
## [5] "EGYPT"
```

``` r
# Q6. Eigenvector centrality
eig <- eigen_centrality(my_net, directed = TRUE, scale = TRUE)$vector
```

``` r-output
## Warning: The `scale` argument of `eigen_centrality()` is deprecated as of igraph 2.1.1.
## ℹ eigen_centrality() will always behave as if scale=TRUE were used.
## This warning is displayed once per session.
## Call `lifecycle::last_lifecycle_warnings()` to see where this warning was
## generated.
```

``` r
mean(eig); median(eig); sd(eig)
```

``` r-output
## [1] 0.731668
```

``` r-output
## [1] 0.7504538
```

``` r-output
## [1] 0.1735069
```

``` r
eig_top5 <- sort(eig, decreasing = TRUE)[1:5]
eig_top5
```

``` r-output
##          JAPAN  UNITED_STATES UNITED_KINGDOM          CHINA         BRAZIL 
##      1.0000000      1.0000000      0.9310392      0.9075430      0.8776935
```

``` r
names(eig_top5)
```

``` r-output
## [1] "JAPAN"          "UNITED_STATES"  "UNITED_KINGDOM" "CHINA"         
## [5] "BRAZIL"
```

``` r
## Q7. Correlations between measures
measures_mat <- cbind(
  degree      = as.numeric(deg_all),
  indegree    = as.numeric(deg_in),
  outdegree   = as.numeric(deg_out),
  closeness   = as.numeric(close_all),
  betweenness = as.numeric(between),
  eigenvector = as.numeric(eig)
)

cor(measures_mat, use = "pairwise.complete.obs", method = "pearson")
```

``` r-output
##                degree  indegree outdegree closeness betweenness eigenvector
## degree      1.0000000 0.9585781 0.9783347 0.9782882   0.8216894   0.9560925
## indegree    0.9585781 1.0000000 0.8788421 0.9413766   0.8588847   0.9912123
## outdegree   0.9783347 0.8788421 1.0000000 0.9544686   0.7521126   0.8810658
## closeness   0.9782882 0.9413766 0.9544686 1.0000000   0.8574023   0.9273738
## betweenness 0.8216894 0.8588847 0.7521126 0.8574023   1.0000000   0.7915612
## eigenvector 0.9560925 0.9912123 0.8810658 0.9273738   0.7915612   1.0000000
```
