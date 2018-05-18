# Luther Project Submission

Submitted by: Jeff Kao

## List of files

### luther_common.py
* common interface containing functions for prepping data, visualization, etc.

### LutherScrapePipelineTeam.ipynb, LutherScrapePipelinePlayer.ipynb, LutherScrapePipelineInjury.ipynb
* notebooks that scrape data from basketball-reference.com and prosportstransactions.com

### LutherDataExploration.ipynb
* initial data exploration

### LutherDataPrep.ipynb
* notebook to prep the scraped data for regression models (creation of player-seasons)

### LutherDataAnalysis-PlayerStats.ipynb
* simpler prediction models (no feature engineering); using linear regressor, and tree methods

### LutherDataAnalysis-FeatureEngineering.py
* more complex prediction model with feature engineering

### LutherDataAnalysis-Predictions-2018-prep.ipynb
* notebook to prep the scraped data for 2018 predictions (2018 player-seasons)

### LutherDataAnalysis-2018-predictions
* generate predictions for 2018

### luther_app.py
* flask app to use prediction results to generate stats for 2018 -- bootstrap was used (bootstrap files generally not included)
