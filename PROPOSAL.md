# Investigating Crime In Chicago
Group: pract_04-tue-1pm-_group-c

**Members**: 
* Canh Thanh Nguyen (45551936)
* Jarred Reilly (43264204)
* Soham Sarfare (45812748)
* Sukhmani Arora (45574715)

## Summary
Chicago, the third most populous city in the United States of America, has a crime problem. Violent crime per capita in Chicago is almost three times the national average, and in 2016 the city saw a large surge in homicides while the rest of the nation's crime rates remain near historic lows [1] [2] [3]. As Chicago is a unique case, we plan to do an investigation into what factors impact crime rates across the city. This is possible because the City of Chicago releases huge amounts of data that's freely available to the public for analysis [4]. Many of the datasets are updated daily and stretch back many years, which is prefect for a detailed analysis.
## Goal
Our goal is to do a thorough analysis of the factors influencing crime in the City of Chicago with the help of modelling and visualisation techniques. While we won't be finding any solutions to the problems facing Chicago, we do hope to bring to light some of the key factors affecting the city's crime problem.

## Data Sources
Our plan is to use three public data sets provided by the City of Chicago:
1. Chicago Reported Crimes: In CSV format, this dataset contains records of 10 million crimes reported to police in Chicago from 2001 to present. As this is a huge data set, we have decided to use a subset of crimes which have occurred in the last 5 years. This data is originally from the Chicago Police Department's CLEAR (Citizen Law Enforcement Analysis and Reporting) system [5].    
2. Chicago Socioeconomic Factors: In CSV format, this dataset contains socioeconomic indicators for all community areas in Chicago. This data is originally from the 2012 Census and contains information like unemployment rate, per capita income, and hardship index [6].	
3. Chicago Police Stations: In CSV format, this dataset contains the location of all the police stations the city of Chicago. This could be useful to discover if there's positive or negative correlations between the location of crime and location of police stations [7].  
4. Chicago City 2017 Demographics: In PDF format, this file contains the racial and age demographics of the city of Chicago in 2017, as well as population, for each of the community area. The file has been exported into an .xlxs file to be import into the notebooks [8].
  
The project will also use 2 shape-files of the city of Chicago to visualise the geographic structure of the city. This will be used in the visualisations of crime distribution across the community areas or districts of Chicago.  
## Data Preparation
We have extensive data preparation planned to ensure quality data for our later analysis.
1. Analyze the data for missing values or duplicates and apply techniques to remedy these where appropriate.  
2. Combine Chicago crimes, socioeconomic, and police station datasets.  
3. Explore correlations between the variables in the datasets.  
4. Investigate the distribution of variables within the datasets and handle outliers.  
5. The crimes dataset consists of 10 million crimes, so we plan to use a subset of the original dataset. Depending on the distribution results we may do this randomly, or try to improve the representation of values in the subset.

## Planned Techniques
1. Multinomial logistic regression to establish a baseline model for predicting crimes across Chicago. This will help us investigate which factors influence different types of crimes.  
2. Compare the baseline results with other classification techniques, such as: support-vector machines, k-nearest neighbors, and artificial neural networks.   
3. Visualise the regional differences in crime using a heat map overlaid on a map of Chicago.  

## Project Plan
1. By week 8 we plan to have completed the data preparation component of our investigation. This is the most important part to get right, as without quality data our models and analysis will be worthless.   
2. By week 10 we plan to have a fine-tuned baseline model and to have made at least two different classifiers to compare the baseline results with.    
3. By week 12 we plan to finish our visualisations of the data, the most important being a heat map to explore regional distribution of different types of crime.

## Extra packages used
1. Geopandas plotting module. To install, run this in anaconda prompt (conda install geopandas), remove open and closing brackets.
2. Imbalanced learning module. To install, run this in anaconda prompt (conda install -c conda-forge imbalanced-learn), remove open and closing brackets.
3. Yellowbrick module. To install, run this in anaconda prompt (conda install -c districtdatalabs yellowbrick), remove open and closing brackets.
4. Bokeh plotting module. To install, run this in anaconda prompt (conda install bokeh), remove open and closing brackets.
5. Bokeh plotting figure export module. To install, run this in anaconda prompt (conda install -c bokeh selenium), remove open and closing brackets.
6. PhantomJS module. To install, run this in anaconda prompt (conda install -c conda-forge phantomjs), remove open and closing brackets.
7. Pillow module. To install, run this in anaconda prompt (conda install -c anaconda pillow), remove open and closing brackets.

## References
[1] https://www.usnews.com/news/articles/2016-09-19/chicago-drives-uptick-in-murders-national-crime-rate-stays-near-historic-lows  
[2] http://www.city-data.com/crime/crime-Chicago-Illinois.html  
[3] http://time.com/4497814/chicago-murder-rate-u-s-crime/  
[4] https://data.cityofchicago.org/     
[5] https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2   
[6] https://data.cityofchicago.org/Health-Human-Services/Census-Data-Selected-socioeconomic-indicators-in-C/kn9c-c2s2   
[7] https://data.cityofchicago.org/Public-Safety/Police-Stations/z8bn-74gv  
[8] http://www.actforchildren.org/wp-content/uploads/2018/01/Census-Data-by-Chicago-Community-Area-2017.pdf