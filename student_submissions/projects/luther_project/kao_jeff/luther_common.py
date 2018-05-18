#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 19:04:30 2017

@author: j2kao
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from sklearn.preprocessing import StandardScaler

# common function: add season_year column to a pandas dataframe
def season_str_to_season_year(season_str):
    return float(season_str.split('-')[0]) + 1

# categories to fit to
categories = ['pts_per_g',
         'fg_per_g','fga_per_g',
         'fg3_per_g','fg3a_per_g',
         'ft_per_g','fta_per_g',
         'trb_per_g','blk_per_g',
         'stl_per_g','ast_per_g',
         'tov_per_g',
         'g','mp_per_g','eff_ratio' #these last 3 are also included in year 0 to predict the other target values 
        ]

# visualization settings
factors_table = \
[
 ['height_inches',None,None,None],
 ['weight',None,None,None],
 ['poscat_0_ya','poscat_1_ya','poscat_2_ya','poscat_3_ya'],
 ['season_year_0_ya','season_year_1_ya','season_year_2_ya','season_year_3_ya'],
 ['team_pace_0_ya','team_pace_1_ya','team_pace_2_ya','team_pace_3_ya'],
 ['yrs_in_league_0_ya','yrs_in_league_1_ya','yrs_in_league_2_ya','yrs_in_league_3_ya'],
 ['age_0_ya','age_1_ya','age_2_ya','age_3_ya'],
 ['g_0_ya','g_1_ya','g_2_ya','g_3_ya'],
 ['mp_per_g_0_ya','mp_per_g_1_ya','mp_per_g_2_ya','mp_per_g_3_ya'],
 ['eff_ratio_0_ya','eff_ratio_1_ya','eff_ratio_2_ya','eff_ratio_3_ya'],
 [None,'pts_per_g_1_ya','pts_per_g_2_ya','pts_per_g_3_ya'],
 [None,'fg_per_g_1_ya','fg_per_g_2_ya','fg_per_g_3_ya'],
 [None,'fga_per_g_1_ya','fga_per_g_2_ya','fga_per_g_3_ya'],
 [None,'fg2_per_g_1_ya','fg2_per_g_2_ya','fg2_per_g_3_ya'],
 [None,'fg2a_per_g_1_ya','fg2a_per_g_2_ya','fg2a_per_g_3_ya'],
 [None,'fg3_per_g_1_ya','fg3_per_g_2_ya','fg3_per_g_3_ya'],
 [None,'fg3a_per_g_1_ya','fg3a_per_g_2_ya','fg3a_per_g_3_ya'],
 [None,'ft_per_g_1_ya','ft_per_g_2_ya','ft_per_g_3_ya'],
 [None,'fta_per_g_1_ya','fta_per_g_2_ya','fta_per_g_3_ya'],
 [None,'trb_per_g_1_ya','trb_per_g_2_ya','trb_per_g_3_ya'],
 [None,'orb_per_g_1_ya','orb_per_g_2_ya','orb_per_g_3_ya'],
 [None,'drb_per_g_1_ya','drb_per_g_2_ya','drb_per_g_3_ya'],
 [None,'ast_per_g_1_ya','ast_per_g_2_ya','ast_per_g_3_ya'],
 [None,'blk_per_g_1_ya','blk_per_g_2_ya','blk_per_g_3_ya'],
 [None,'stl_per_g_1_ya','stl_per_g_2_ya','stl_per_g_3_ya'],
 [None,'tov_per_g_1_ya','tov_per_g_2_ya','tov_per_g_3_ya'],
 [None,'pf_per_g_1_ya','pf_per_g_2_ya','pf_per_g_3_ya']
]

# set up visualization dataframe
viz_headers_df = pd.DataFrame(factors_table)
viz_headers_df.columns = ['This year','1 Year Ago','2 Years Ago','3 Years Ago']
viz_index = [
    'Height (in.)',
    'Weight',
    'Position',
    'Season Year',
    'Team Pace',
    'No. Years Played',
    'Age',
    'Games',
    'Minutes/G',
    'Positional Contribution',
    'PTS/G',
    'FG/G',
    'FGA/G',
    '2PT FG/G',
    '2PT FGA/G',
    '3PT FG/G',
    '3PT FGA/G',
    'FT/G',
    'FTA/G',
    'TRB/G',
    'ORB/G',
    'DRB/G',
    'AST/G',
    'BLK/G',
    'STL/G',
    'TO/G',
    'PF/G'
]
viz_headers_df.set_index([viz_index], inplace=True)

# options for the explanatory variables, from simple to complex: 
# NB: options B, C and D are implemented directly in the prep data function itself
X_mask_0 = {}
for category in categories:
    X_mask_0[category] = [category+'_1_ya','poscat_0_ya']

X_mask_a = {}
for category in categories:
    X_mask_a[category] = [
              'height_inches','weight',
              'age_0_ya','season_year_0_ya','poscat_0_ya','yrs_in_league_0_ya',
              category+'_1_ya',
              category+'_2_ya',
              category+'_3_ya'
             ]
    
# options for the target variables: 
# pts/g, 3pts, reb, ast, blk, stl, fg%, ft%, fta/g, to, g, mp_per_g
y_mask = {}
for col in categories:
    y_mask[col] = col

def mask_data(category, level, X_train, y_train):
    #check we're inputting the right params
    assert category in categories
    assert level in ['0','A','B','C','D']
    if level == '0':
        # the dumb case - regression on last year's data
        ready_X = X_train.loc[:,X_mask_0[category]]
    elif level == 'A':
        # ready_X takes on a specific mask
        ready_X = X_train.loc[:,X_mask_a[category]]
    else:
        # drop non-numerical
        ready_X = X_train.select_dtypes(exclude=['object'])
        # drop others including anything involving current year, position, efficiency, prediction
        exclusion_criteria = ['pos_','_0_ya','eff_raw','_pred']
        exclusion_exceptions = []
        if level == 'B':
            # except for INDIVIDUAL items that will be projected with ABSOLUTE certainty
            exclusion_exceptions = [
                'age_0_ya','season_year_0_ya','poscat_0_ya','yrs_in_league_0_ya'
            ]
        elif level == 'C':
            # save INDIVIDUAL items that will be projected (with certainty AND without (e.g., games, meff_ratio, team_pace))
            exclusion_exceptions = [
                'age_0_ya','season_year_0_ya','poscat_0_ya','yrs_in_league_0_ya',
                'g_0_ya','team_pace_0_ya','eff_ratio_0_ya'
            ]
        elif level == 'D':
            exclusion_exceptions = [
                'age_0_ya','season_year_0_ya','poscat_0_ya','yrs_in_league_0_ya'
                'team_pace_pred','eff_ratio_pred'
            ]
        excluded_columns = []
        for col in ready_X.columns:
            #if fits exclusion criteria but does not MATCH an exception
            if (        any(excrit in col for excrit in exclusion_criteria)
                and not any(exexcp == col for exexcp in exclusion_exceptions)):
                excluded_columns.append(col)
        ready_X.drop(excluded_columns, axis=1, inplace=True)
    
    #y is always the same but masked
    ready_y = None
    if y_train:
        ready_y = y_train[y_mask[category]]
    return ready_X, ready_y

# this function returns a formatted (and standardized) X and y given our desired options
def prep_data(category, level, X_train, y_train):
    #mask
    ready_X, ready_y = mask_data(category, level, X_train, y_train)

    # standardize predictor variables
    std = StandardScaler()
    std.fit(ready_X)
    std_ready_X = std.transform(ready_X)
    return std_ready_X, ready_X, ready_y, std

def prep_data_for_prediction(category, level, X_train, y_train, std):
    #piggyback off the existing mask function to mask the X and y
    ready_X, ready_y = mask_data(category, level, X_train, y_train)
    std_ready_X = std.transform(ready_X)
    return std_ready_X, ready_X, ready_y, std
    
### helper function to help us get a background gradient across all columns
from matplotlib import colors
def background_gradient(s, m, M, cmap='hot', low=0, high=0):
    rng = M - m
    norm = colors.Normalize(m - (rng * low),
                            M + (rng * high))
    normed = norm(abs(s.values))
    c = [colors.rgb2hex(x) for x in plt.cm.get_cmap(cmap)(normed)]
    return ['background-color: %s' % color for color in c]

def visualize_scores(grid_est, params, log_keys_list=[]):
    # visualize all scores on successive scatter charts
    # log_keys_list gives us list of expl. variables that we want to plot on a log scale
    result_df = pd.DataFrame(grid_est.grid_scores_)
    for key, value in params.items():
        result_df[key] = result_df.parameters.apply(lambda val: val[key])
        fig = plt.figure()
        if key in log_keys_list:
            plt.scatter(np.log10(result_df[key]), result_df.mean_validation_score,marker='+')
        else:
            plt.scatter(result_df[key], result_df.mean_validation_score,marker='+')
        fig.suptitle(key)
        
def check_overfit(grid_est, hold_X, hold_y):
    print('Best Estimator:')
    print(grid_est.best_estimator_)
    result_df = pd.DataFrame(grid_est.grid_scores_)
    print('Best Trained Score: {}'.format(np.max(result_df.mean_validation_score)))
    print('Applied to Holdout Set: {}'.format(grid_est.best_estimator_.score(hold_X, hold_y)))
    
def visualize_factors_heat_map(grid_est,ready_X,regression_or_tree,num_factors=10, poly=None):
    assert regression_or_tree in ['regression','poly_regression','tree']
    # Visualize coeffs/importances for best estimator
    # note: need to use ready_X columns bc columns are scrubbed when standardizing
    factors = None
    factor_desc = 'N/A'
    if regression_or_tree == 'regression':
        factors = list(zip(ready_X.columns,grid_est.best_estimator_.coef_))
        factor_desc = 'Regression Coefficients'
    elif regression_or_tree == 'tree':
        factors = list(zip(ready_X.columns,grid_est.best_estimator_.feature_importances_))
        factor_desc = 'Feature Importances'
    else:# regression_or_tree == 'poly_regression'
        column_names = poly.get_feature_names(ready_X.columns)
        factors = list(zip(column_names,grid_est.best_estimator_.coef_))
        factor_desc = 'Polynomial Regression Coefficients'
        # we don't have a heat map for poly
    print('Top {} {} (desc):'.format(num_factors,factor_desc))
    print(sorted(factors, key=lambda x: abs(x[1]), reverse=True)[:num_factors])
    
    if regression_or_tree == 'poly_regression':
        return
    
    print('Heat Map:'.format(factor_desc))
    factors_dict = defaultdict(int)
    for factor in factors:
        #abs value so we can use a heat map
        factors_dict[factor[0]] = factor[1]
    # if there is no key, set value to zero
    factors_dict[None] = 0
    factors_df = viz_headers_df.applymap(lambda x: factors_dict[x])
    factors_df.set_index([viz_index])
    # here's the heat map style
    s = factors_df.style.apply(background_gradient,
                   cmap='hot',
                   m=0,
                   M=factors_df.max().max(),
                   low=0.1,
                   high=0.1)
    return s