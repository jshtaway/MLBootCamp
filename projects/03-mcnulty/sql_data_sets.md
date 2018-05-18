# Project McNulty Optional Data Sets


These eight topic-based data sets can optionally be used for Project McNulty. There are multiple data tables for each topic. The tables should be cleaned and imported into PostgreSQL. You can also add your own data, if you like.

Your analysis for Project McNulty project should demonstrate SQL proficiency via table joins, group-by's, and other statistics. (In other words, don't just import each table with Pandas and then ignore SQL.) 

Please observe all citation requests when formally discussing or publishing your results.

If you do not wish to use one of these data sets, then you should complete all SQL exercises listed in the Challenges folder.



## 1. NYC Transportation

You already learned the ins-and-outs of New York City's turnstile (subway) data on Project Benson. However, NYC also has a rich set of data available for taxis, bike shares, and black cars.

The format of each file and the column abbreviations are available on each website.

* [Yellow Taxis, Green Taxis, and For-Hire Vehicles (FHV)](http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml)
* [CitiBike Data](https://s3.amazonaws.com/tripdata/index.html)
* [MTA Turnstile Data](http://web.mta.info/developers/turnstile.html)
* Uber Pickups in NYC on [Kaggle](https://www.kaggle.com/fivethirtyeight/uber-pickups-in-new-york-city) and on [GitHub](https://github.com/fivethirtyeight/uber-tlc-foil-response)

The transportation data can optionally be combined with other data, such as weather, which can be requested from NOAA:  

* [NOAA on-demand hourly weather data](https://www7.ncdc.noaa.gov/CDO/cdopoemain.cmd?datasetabbv=DS3505&countryabbv=&georegionabbv=NAMER&resolution=40)



## 2. Traffic Fatalities

Traffic fatalities in 2015, as released by the National Highway Traffic Safety Administration (NHTSA). This data set contains 17 tables of information. 

More information:  

* [Kaggle competition](https://www.kaggle.com/nhtsa/2015-traffic-fatalities)
* [Fatality Analysis Reporting System FARS Users's Manual](https://crashstats.nhtsa.dot.gov/Api/Public/ViewPublication/812315)



## 3. US Health Insurance Marketplace

Data provided by the Centers for Medicare & Medicaid Services (CMS). This data is for 2014-2016 and contains eight tables of about plans and benefits available in each US state. 

More information:  

* [Kaggle competition](https://www.kaggle.com/hhs/health-insurance-marketplace)
* [Centers for Medicare & Medicaid Services](https://www.cms.gov/cciio/resources/data-resources/marketplace-puf.html)

Depending on your project focus, the following additional table may be of interest:  

* [2015 US County-Level Population](https://www.kaggle.com/stevepalley/us-county-population)



## 4. Militarized Interstate Disputes

This [data set](http://www.correlatesofwar.org/data-sets/MIDs) is part of the Correlates of War Project. It contains all instances of when one country threatens, displays, or uses force against another. There are five tables in this data set. 

The Correlates of War Project also has additional [data sets](http://www.correlatesofwar.org/data-sets/folder_listing) that may be of interest.



## 5. Sports, Sports, and More Sports!

Can't get enough sports? In addition to the [Lahman Baseball Database](http://www.seanlahman.com/baseball-archive/statistics/) covered in class, you can use hockey, soccer, or basketball data.

#### Professional Hockey

A collection of historical hockey data for North American teams. There are twenty tables and the data span 1909-2012. 

More information:  

* [Kaggle competition](https://www.kaggle.com/open-source-sports/professional-hockey-database)
* [Open Source Sports](http://www.opensourcesports.com/hockey/)

#### European Football (Soccer)

Soccer data for European teams spanning 2008-2016, and including over 25,000 matches and 10,000 players. There are seven tables for this data set. 

More information:  

* [Kaggle competition](https://www.kaggle.com/hugomathien/soccer)
* [GitHub repo](https://github.com/hugomathien/football-data-collection/tree/master/footballData)

#### NBA Basketball

NBA data from 1927-2012, and containing eleven tables total. This [table](https://www.kaggle.com/dansbecker/nba-shot-logs) of shots taken in NBA games during the 2014-2015 season may also be of interest.

There is also a WNBA data set available at the original data source, Open Source Sports.

More information:  

* [Kaggle competition](https://www.kaggle.com/open-source-sports/mens-professional-basketball)
* [Open Source Sports](http://www.opensourcesports.com/basketball/)



## 6. The Simpson's Data

Information about characters, locations, episodes, and scripts for ~600 Simpsons episodes, dating back to 1989. The data set contains four tables. 

More information:  

* [Kaggle competition](https://www.kaggle.com/wcukierski/the-simpsons-by-the-data)
* [GitHub repo](https://github.com/toddwschneider/flim-springfield)



## 7. Climate Change

Land and ocean surface temperatures dating from 1750 have been aggregated by Berkley Earth from Lawrence-Berkley National Laboratory. There are five tables in this data set. 

More information:  

* [Kaggle competition](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data)
* [Berkley Earth](http://berkeleyearth.org/data/)


High resolution climate projections from the research program on Climate Change, Agriculture, and Food Security (CCAFS) are also available. This data is for future time periods (2030-2080) and is quite large (6 TB).

More information:  

* [CCAFS-CGIAR website](https://ccafs.cgiar.org/)
* [AWS data sets link](https://aws.amazon.com/datasets/ccafs-climate-data/)  
    [(for above link: How to connect to S3)](http://howto.lintel.in/how-to-mount-aws-s3-bucket-on-linux/)

## 8. Python StackOverflow Questions 

Full text, statistics, and answers of all StackOverflow questions that are tagged with "Python". This data set contains questions through October 16, 2016 and has three tables.

More information:  

* [Kaggle competition](https://www.kaggle.com/stackoverflow/pythonquestions)


There is also an [R version](https://www.kaggle.com/stackoverflow/rquestions) of the above data set. The [full StackOverflow data set](https://archive.org/details/stackexchange) is also available, however it is almost 30 GB (compressed). 
