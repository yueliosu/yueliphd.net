---
title: "Lab 2: Network visualization"
subtitle: "Network analysis in R"
description: "Visualizing networks for readers who don't know the data, using prisoner friendship, needle-sharing and other networks."
---

[Download R Markdown (.Rmd)](lab-2-network-visualization.Rmd){.btn .btn-primary .btn-sm}

From last week's module, please download the iGraph data. I have also shared the description of the Comparative Networks Dataset (McMillan, Phadke, Goist, & Denny, 2017) on Canvas. There is a PDF file that explains the data collection procedures and an Excel file that has summaries of the data that are included.

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

This should read in an object called igraph_data_list into your session of R. You can check that it worked with an ls() command. Once you have the data read in, you will be able to access the actual networks. They are stored in an R data type called a list. A list is R's way of collecting a set of R objects that may have different types. You can access elements of a list using double square brackets with the number of the corresponding element of the list that you want to access. Each element of the list contains three things: the network, any node-level data (i.e., individual-level variables), and metadata about the network. For now, the most important thing would be to access particular networks. Imagine you wanted to extract from the list the academic friendship network 1 (there are two of them in the data). You would use a process like:

``` r
# see the names of all of the networks
names(igraph_data_list)
```

``` r-output
##   [1] "Girls' Friendships 1"                   
##   [2] "Girls' Friendships 2"                   
##   [3] "Girls' Friendships 3"                   
##   [4] "Fraternity Interactions 1"              
##   [5] "Fraternity Interactions 2"              
##   [6] "Radio Calls 1"                          
##   [7] "Radio Calls 2"                          
##   [8] "Office Interactions 1"                  
##   [9] "Office Interactions 2"                  
##  [10] "Research Group 1"                       
##  [11] "Research Group 2"                       
##  [12] "Conference Likes 1"                     
##  [13] "Conference Likes 2"                     
##  [14] "Trade 1"                                
##  [15] "Trade 2"                                
##  [16] "Trade 3"                                
##  [17] "Trade 4"                                
##  [18] "Diplomacy "                             
##  [19] "Academic Friendship 1"                  
##  [20] "Academic Friendship 2"                  
##  [21] "Email Communication"                    
##  [22] "Prisoner Friendships"                   
##  [23] "Miner Interactions 1"                   
##  [24] "Miner Interactions 2"                   
##  [25] "Tailor Shop Interactions 1"             
##  [26] "Tailor Shop Interactions 2"             
##  [27] "Tailor Shop Interactions 3"             
##  [28] "Tailor Shop Interactions 4"             
##  [29] "Organizations Information"              
##  [30] "Organizations Monetary"                 
##  [31] "Managers Advice 1"                      
##  [32] "Managers Friendship 1"                  
##  [33] "Managers Interaction"                   
##  [34] "Managers Advice 2"                      
##  [35] "Managers Advice 3"                      
##  [36] "Managers Advice 4"                      
##  [37] "Managers Advice 5"                      
##  [38] "Managers Advice 6"                      
##  [39] "Managers Advice 7"                      
##  [40] "Managers Advice 8"                      
##  [41] "Managers Advice 9"                      
##  [42] "Managers Advice 10"                     
##  [43] "Managers Advice 11"                     
##  [44] "Managers Advice 12"                     
##  [45] "Managers Advice 13"                     
##  [46] "Managers Advice 14"                     
##  [47] "Managers Advice 15"                     
##  [48] "Managers Advice 16"                     
##  [49] "Managers Advice 17"                     
##  [50] "Managers Advice 18"                     
##  [51] "Managers Advice 19"                     
##  [52] "Managers Advice 20"                     
##  [53] "Managers Advice 21"                     
##  [54] "Managers Advice 22"                     
##  [55] "Managers Friendship 2"                  
##  [56] "Managers Friendship 3"                  
##  [57] "Managers Friendship 4"                  
##  [58] "Managers Friendship 5"                  
##  [59] "Managers Friendship 6"                  
##  [60] "Managers Friendship 7"                  
##  [61] "Managers Friendship 8"                  
##  [62] "Managers Friendship 9"                  
##  [63] "Managers Friendship 10"                 
##  [64] "Managers Friendship 11"                 
##  [65] "Managers Friendship 12"                 
##  [66] "Managers Friendship 13"                 
##  [67] "Managers Friendship 14"                 
##  [68] "Managers Friendship 15"                 
##  [69] "Managers Friendship 16"                 
##  [70] "Managers Friendship 17"                 
##  [71] "Managers Friendship 18"                 
##  [72] "Managers Friendship 19"                 
##  [73] "Managers Friendship 20"                 
##  [74] "Managers Friendship 21"                 
##  [75] "Managers Friendship 22"                 
##  [76] "Fraterninty Preferences 1"              
##  [77] "Fraterninty Preferences 2"              
##  [78] "Fraterninty Preferences 3"              
##  [79] "Fraterninty Preferences 4"              
##  [80] "Fraterninty Preferences 5"              
##  [81] "Fraterninty Preferences 6"              
##  [82] "Fraterninty Preferences 7"              
##  [83] "Fraterninty Preferences 8"              
##  [84] "Fraterninty Preferences 9"              
##  [85] "Fraterninty Preferences 10"             
##  [86] "Fraterninty Preferences 11"             
##  [87] "Fraterninty Preferences 12"             
##  [88] "Fraterninty Preferences 13"             
##  [89] "Fraterninty Preferences 14"             
##  [90] "Fraterninty Preferences 15"             
##  [91] "Families Marriage"                      
##  [92] "Families Business Ties"                 
##  [93] "Tribes Alliances"                       
##  [94] "Tribes Antagonisms"                     
##  [95] "Bank Wiring Horseplay"                  
##  [96] "Bank Wiring Arguments"                  
##  [97] "Bank Wiring Friendship"                 
##  [98] "Bank Wiring Antagonism"                 
##  [99] "Bank Wiring Help"                       
## [100] "Bank Wiring Trades"                     
## [101] "Monk Friendship 1"                      
## [102] "Monk Friendship 2"                      
## [103] "Monk Friendship 3"                      
## [104] "Monk Dislike"                           
## [105] "Monk Esteem"                            
## [106] "Monk Disesteem"                         
## [107] "Monk Positive Influence"                
## [108] "Monk Negative Influence"                
## [109] "Monk Praise"                            
## [110] "Monk Blame"                             
## [111] "Taro Exchange"                          
## [112] "Corporate Interlocks 1"                 
## [113] "Corporate Interlocks 2"                 
## [114] "Employee Associations 1"                
## [115] "Employee Associations 2"                
## [116] "Monkey Kinship"                         
## [117] "Monkey Interaction"                     
## [118] "Karate Club Binary"                     
## [119] "Karate Club Valued"                     
## [120] "Police Precinct Interaction"            
## [121] "Carter Administration 1"                
## [122] "Carter Administration 2"                
## [123] "Needle Sharing 1"                       
## [124] "Needle Sharing 2"                       
## [125] "Actor Costarring"                       
## [126] "Communication Network 1"                
## [127] "Communication Network 2"                
## [128] "Communication Network 3"                
## [129] "Communication Network 4"                
## [130] "Communication Network 5"                
## [131] "Communication Network 6"                
## [132] "Communication Network 7"                
## [133] "Communication Network 8"                
## [134] "Communication Network 9"                
## [135] "Communication Network 10"               
## [136] "Communication Network 11"               
## [137] "Communication Network 12"               
## [138] "Communication Network 13"               
## [139] "Communication Network 14"               
## [140] "Communication Network 15"               
## [141] "Communication Network 16"               
## [142] "Communication Network 17"               
## [143] "Communication Network 18"               
## [144] "Communication Network 19"               
## [145] "Communication Network 20"               
## [146] "Communication Network 21"               
## [147] "Communication Network 22"               
## [148] "Communication Network 23"               
## [149] "Communication Network 24"               
## [150] "Communication Network 25"               
## [151] "Communication Network 26"               
## [152] "Communication Network 27"               
## [153] "Communication Network 28"               
## [154] "Communication Network 29"               
## [155] "Communication Network 30"               
## [156] "Communication Network 31"               
## [157] "Communication Network 32"               
## [158] "Communication Network 33"               
## [159] "Communication Network 34"               
## [160] "Communication Network 35"               
## [161] "Communication Network 36"               
## [162] "Communication Network 37"               
## [163] "Communication Network 38"               
## [164] "Communication Network 39"               
## [165] "Villager Food Sharing"                  
## [166] "Villager Kinship 1"                     
## [167] "Villager Kinship 2"                     
## [168] "Villager Kinship 3"                     
## [169] "Villager Kinship 4"                     
## [170] "Character Co-Occurrence"                
## [171] "Office Advice"                          
## [172] "Office Conflict"                        
## [173] "Student Acquaintance 1"                 
## [174] "Student Socialize"                      
## [175] "Student Advice To"                      
## [176] "Student Advice From"                    
## [177] "Student Acquaintance 2"                 
## [178] "Drug User Association"                  
## [179] "Carbon Flow"                            
## [180] "Terrorism Affiliation "                 
## [181] "County_Email_1"                         
## [182] "County_Email_2"                         
## [183] "County_Email_3"                         
## [184] "County_Email_4"                         
## [185] "County_Email_5"                         
## [186] "County_Email_6"                         
## [187] "County_Email_7"                         
## [188] "County_Email_8"                         
## [189] "County_Email_9"                         
## [190] "County_Email_10"                        
## [191] "County_Email_11"                        
## [192] "County_Email_12"                        
## [193] "County_Email_13"                        
## [194] "County_Email_14"                        
## [195] "County_Email_15"                        
## [196] "County_Email_16"                        
## [197] "County_Email_17"                        
## [198] "Congress_Cosponsorship_93"              
## [199] "Congress_Cosponsorship_94"              
## [200] "Congress_Cosponsorship_95"              
## [201] "Congress_Cosponsorship_96"              
## [202] "Congress_Cosponsorship_97"              
## [203] "Congress_Cosponsorship_98"              
## [204] "Congress_Cosponsorship_99"              
## [205] "Congress_Cosponsorship_100"             
## [206] "Congress_Cosponsorship_101"             
## [207] "Congress_Cosponsorship_102"             
## [208] "Congress_Cosponsorship_103"             
## [209] "Congress_Cosponsorship_104"             
## [210] "Congress_Cosponsorship_105"             
## [211] "Congress_Cosponsorship_106"             
## [212] "Congress_Cosponsorship_107"             
## [213] "Congress_Cosponsorship_108"             
## [214] "Congress_Cosponsorship_109"             
## [215] "Congress_Cosponsorship_110"             
## [216] "Bison"                                  
## [217] "Dolphins"                               
## [218] "Kangaroo"                               
## [219] "Rhesus"                                 
## [220] "Zebra"                                  
## [221] "Cattle"                                 
## [222] "Hens"                                   
## [223] "Macaques"                               
## [224] "Sheep"                                  
## [225] "UCI_Staff"                              
## [226] "Infectious_Conference"                  
## [227] "Train_Bombing"                          
## [228] "Hypertext_Conference"                   
## [229] "Windsurfers"                            
## [230] "Jazz_Musicians"                         
## [231] "ResHall_Friendship"                     
## [232] "Seventh_Graders"                        
## [233] "Dutch_College"                          
## [234] "Euroads"                                
## [235] "US_Airports"                            
## [236] "Metabolic_Roundworms"                   
## [237] "Human_Proteins"                         
## [238] "PDZbase"                                
## [239] "Harry_Potter_1"                         
## [240] "Harry_Potter_2"                         
## [241] "Harry_Potter_3"                         
## [242] "Harry_Potter_4"                         
## [243] "Harry_Potter_5"                         
## [244] "Harry_Potter_6"                         
## [245] "Dutch_School1_Friendship_Delinquency_1" 
## [246] "Dutch_School1_Friendship_Delinquency_2" 
## [247] "Dutch_School1_Friendship_Delinquency_3" 
## [248] "Dutch_School1_Friendship_Delinquency_4" 
## [249] "Dutch_School1_Friendship"               
## [250] "Groningen_Freshmen_Friendship_1"        
## [251] "Groningen_Freshmen_Friendship_2"        
## [252] "Groningen_Freshmen_Friendship_3"        
## [253] "Groningen_Freshmen_Friendship_4"        
## [254] "Groningen_Freshmen_Friendship_5"        
## [255] "Teenage_Friends_Lifestyle_subset_1"     
## [256] "Teenage_Friends_Lifestyle_subset_2"     
## [257] "Teenage_Friends_Lifestyle_subset_3"     
## [258] "Teenage_Friends_Lifestyle_original_1"   
## [259] "Teenage_Friends_Lifestyle_original_2"   
## [260] "Teenage_Friends_Lifestyle_original_3"   
## [261] "Law_Firm_Partners_Advice"               
## [262] "Law_Firm_Lawyers_Advice"                
## [263] "Law_Firm_Partners_Coworker"             
## [264] "Law_Firm_Lawyers_Coworker"              
## [265] "Law_Firm_Partners_Friendship"           
## [266] "Law_Firm_Lawyers_Friendship"            
## [267] "Dutch_School2_Friendship_Delinquency_1" 
## [268] "Dutch_School2_Friendship_Delinquency_2" 
## [269] "Dutch_School3_Friendship_Delinquency_1" 
## [270] "Dutch_School3_Friendship_Delinquency_2" 
## [271] "Dutch_School4_Friendship_Delinquency_1" 
## [272] "Dutch_School4_Friendship_Delinquency_2" 
## [273] "Dutch_School5_Friendship_Delinquency_1" 
## [274] "Dutch_School5_Friendship_Delinquency_2" 
## [275] "Dutch_School6_Friendship_Delinquency_1" 
## [276] "Dutch_School6_Friendship_Delinquency_2" 
## [277] "Dutch_School7_Friendship_Delinquency_1" 
## [278] "Dutch_School7_Friendship_Delinquency_2" 
## [279] "Dutch_School8_Friendship_Delinquency_1" 
## [280] "Dutch_School8_Friendship_Delinquency_2" 
## [281] "Dutch_School9_Friendship_Delinquency_1" 
## [282] "Dutch_School9_Friendship_Delinquency_2" 
## [283] "Dutch_School10_Friendship_Delinquency_1"
## [284] "Dutch_School10_Friendship_Delinquency_2"
## [285] "Dutch_School11_Friendship_Delinquency_1"
## [286] "Dutch_School11_Friendship_Delinquency_2"
## [287] "Dutch_School12_Friendship_Delinquency_1"
## [288] "Dutch_School12_Friendship_Delinquency_2"
## [289] "Dutch_School13_Friendship_Delinquency_1"
## [290] "Dutch_School13_Friendship_Delinquency_2"
## [291] "Dutch_School14_Friendship_Delinquency_1"
## [292] "Dutch_School14_Friendship_Delinquency_2"
## [293] "Dutch_School15_Friendship_Delinquency_1"
## [294] "Dutch_School15_Friendship_Delinquency_2"
## [295] "Dutch_School16_Friendship_Delinquency_1"
## [296] "Dutch_School16_Friendship_Delinquency_2"
## [297] "Dutch_School17_Friendship_Delinquency_1"
## [298] "Dutch_School17_Friendship_Delinquency_2"
## [299] "Dutch_School18_Friendship_Delinquency_1"
## [300] "Dutch_School18_Friendship_Delinquency_2"
## [301] "Dutch_School19_Friendship_Delinquency_1"
## [302] "Dutch_School19_Friendship_Delinquency_2"
## [303] "Dutch_School20_Friendship_Delinquency_1"
## [304] "Dutch_School20_Friendship_Delinquency_2"
```

``` r
# the academic friendship 1 network is number 19 in the list
# let's see what it is in it
summary(igraph_data_list[[19]])
```

``` r-output
## This graph was created by an old(er) igraph version.
## ℹ Call `igraph::upgrade_graph()` on it to use with the current igraph version.
## For now we convert it on the fly...
```

``` r-output
##                 Length Class      Mode
## network         32     igraph     list
## node_level_data  2     data.frame list
## metadata         9     -none-     list
```

``` r
# this extracts the network
acad_friends_net <- igraph_data_list[[19]]$network
```

In the above, line 2 shows the names of all of the networks in the list. This should correspond to the names in the Excel file. Line 6 gives a summary of all of the elements of the list at position 19, which is the network we are looking for. Finally, line 9 takes the network object that is in the 19th position in the list and sets it to a new object that is called acad_friends_net. That is an igraph object that can be used in the ways we have been doing in class.

## Questions for you to answer

Using a process like that described above, select 1. the prisoner friendships network (number 22) 2. the needle sharing 2 network (number 124) 3. a third network of your choosing

For each of the above, create a visualization of the network that helps to display the data for a reader who is unfamiliar with these data. For each of your visualizations, write a one paragraph description of the network and the visualization, pointing out the aspects of the visualization that you might want to draw a reader's attention to. These descriptions do not need to go into a great deal of depth on the data (i.e., no need to read the full paper that describes the data). Please share your code, either as an appendix or as a separate file, in addition to your assignment.

Tips: You may find section #4 in Dr. Ognyanova's tutorial on network visualization very helpful:) You can find the link to it in this week's module on Canvas.
