#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 14:55:38 2017

@author: j2kao
"""
###############
#The sklearn and pandas stuff
import pandas as pd
import numpy as np

###############

from flask import Flask, render_template, flash, request, redirect, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
 
##SETUP##
# categories to predict
pred_categories = ['pts_per_g',
         'fg_per_g','fga_per_g',
         'fg3_per_g','fg3a_per_g',
         'ft_per_g','fta_per_g',
         'trb_per_g','blk_per_g',
         'stl_per_g','ast_per_g',
         'tov_per_g'
        ]

# load data
pred_df = pd.read_csv('LEBRON_2018_FINAL_PREDICTIONS.csv', index_col=0)
pred_df['name_match'] = pred_df['name'].str.lower()

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])


def row_containing_name(name):
    df = pred_df[pred_df['name_match'] == name.strip().lower()]
    return df
    
@app.route("/", methods=['GET', 'POST']) 
def hello2():
    return redirect(url_for('hello', player='start'))
@app.route("/<string:player>", methods=['GET', 'POST'])
def hello(player):
    form = ReusableForm(request.form)
    print(form.errors)
    if request.method == 'POST':
        name=request.form['name']
        if form.validate():
            row = row_containing_name(name)
            # Save the comment here.
            if len(row) > 0: # there are stats to pull up
                real_name = row.iloc[0,3]
                if not pd.isnull(row.iloc[0,4]):
                    flash('Thanks for following the instructions. Here is LEBRON\'s prediction for ' + real_name + ':')
                    return redirect(url_for('hello', player=real_name))
                else:
                    flash('Sorry: LEBRON knows ' + real_name + ' but doesn\'t have enough data to make a prediction.')
            else:
                flash('Sorry: LEBRON has no idea who "' + name + '" is (if that\'s his real name!).')
        else:
            flash('Sorry: You must enter a name -- LEBRON can\'t read your mind!')
        return render_template('hello.html', form=form)
    if request.method == 'GET':
        name = request.path.split('/')[-1]
        row = row_containing_name(name)
        positions = ['','Point Guard','Shooting Guard','Small Forward','Power Forward','Center']
        if len(row) > 0:
            team_str = row.iloc[0,1]
            age_str = '{0:.0f}'.format(row.iloc[0,4])
            ht_str = '{0:.0f}'.format(row.iloc[0,5]) + ' inches'
            wt_str = '{0:.0f}'.format(row.iloc[0,7]) + ' pounds'
            pos_str = positions[int(row.iloc[0,6])]
            exp_str = '{0:.0f}'.format(row.iloc[0,8]) + ' years'
            
            ppg_str = '{0:.1f}'.format(row.iloc[0,9])
            fgp_str = '{0:.3f}'.format(row.iloc[0,10]/row.iloc[0,11]) + ' ({0:.1f}/{1:.1f})'.format(row.iloc[0,10],row.iloc[0,11])
            fg3p_str = '{0:.3f}'.format(row.iloc[0,12]/row.iloc[0,13]) + ' ({0:.1f}/{1:.1f})'.format(row.iloc[0,12],row.iloc[0,13])
            ftp_str = '{0:.3f}'.format(row.iloc[0,14]/row.iloc[0,15]) + ' ({0:.1f}/{1:.1f})'.format(row.iloc[0,14],row.iloc[0,15])
            rpg_str = '{0:.1f}'.format(row.iloc[0,16])
            apg_str = '{0:.1f}'.format(row.iloc[0,19])
            bpg_str = '{0:.1f}'.format(row.iloc[0,17])
            spg_str = '{0:.1f}'.format(row.iloc[0,18])
            tpg_str = '{0:.1f}'.format(row.iloc[0,20])
            return render_template('hello.html', 
                                   form=form, 
                                   row=row, 
                                   row_exists=True, 
                                   name=name,
                                   team_str=team_str,
                                   age_str=age_str,
                                   ht_str=ht_str,
                                   wt_str=wt_str,
                                   pos_str=pos_str,
                                   exp_str=exp_str,
                                   ppg_str=ppg_str,
                                   fgp_str=fgp_str,
                                   fg3p_str=fg3p_str,
                                   ftp_str=ftp_str,
                                   rpg_str=rpg_str,
                                   apg_str=apg_str,
                                   bpg_str=bpg_str,
                                   spg_str=spg_str,
                                   tpg_str=tpg_str)
        else:
            return render_template('hello.html', form=form, row_exists=False)
  
    
if __name__ == "__main__":
    app.run()