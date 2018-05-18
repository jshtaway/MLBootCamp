# Project Luther

## Project Data

  project data was scraped from flightaware.com.
  The scraping took 2 parts:
  1) get the flight number of non-stop flights between a list of 20 airports. [notebook here](CW_FlightsByAirport-20.ipynb)
  2) with each flight number, go into the flight history of that flight and pull out all the available flight history of that flight - on average each flight has about 7 - 10 days data. [notebook here](CW_Luther-Iter-AllFLT-Copy9.ipynb)
  
  
## Project Data Cleaning and Pre-Processing

  The data was converted to datetime with consideration of timezone and the actual flight duration, delay or any 'time period' kind of information was calculated.
  
## Project Modeling

  The data were fitted with linear regression, lasso (lassoCV), tree and random forest. 
  
  There are three jupyter notebook files representing three sets of modelings with different target variables:
  
  [Modeling-log y.ipynb](Modeling-log y.ipynb)
  
  [Modeling-log y_Dep.ipynb](Modeling-log y_Dep.ipynb)
  
  [Modeling.ipynb](Modeling.ipynb)
  
  
  

