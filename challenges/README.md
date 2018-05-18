# Instructions for Submitting Challenges

## 1.  GitHub - notices
Your GitHub settings should be set to receive email notifications by email.  Below are instructions on setting this up:

a) In GitHub, on upper right corner, click on your profile picture, then "Settings"

b) On left menu, under "Personal Settings", click on "Notification Center"

c) On right menu, under "Participating", make sure both boxes, "Email" and "Web" are checked.

## 2.  GitHub Folder Naming Convention
a)  Create a folder with your name under submissions, for each set:  [student_submissions/challenges](../student_submissions/challenges)

b)  Use **lower-case last name and first name and underscores.**  (This is because GitHub folder/file names are case-sensitive.)  Example:  `lastname_firstname` for folder name

## 3.  File Naming Convention
Your notebook file name should be **lower-case, include the challenge set number, and your name.**  Here's an example:  `challenge_set_1_reshama.ipynb`

## 4.  Submitting Files
a) Submit **Jupyter notebook** for challenges instead of `*.py` files.  Makes it easier to follow:  code, output & graphs.

b) Submit one file.  (Do not submit several versions of files.)

c) **DO NOT SUBMIT data files.**  There will already be a copy of data file on GitHub in the challenges_data folder.  We want to avoid multiple copies of data files.  It takes up unnecessary space and slows server down needlessly.

## 5.  Setting up IPython Notebook
a) Add a header section to your notebook
```
Topic:        Challenge Set 1
Subject:      Explore MTA turnstile data
Date:         xx/xx/xxxx
Name:         student name
Worked with:  other students' name
```

b) **LABEL CHALLENGE NUMBERS in bold.**

## 6.  Graphs
a) To includes graphs in the Jupyter notebook, include the following code:
```
%matplotlib inline
import matplotlib.pyplot as plt
```

b) All graphs should have a title.  Also, label both x and y axes.

## 7.  Comparing results
To compare results consistently, where applicable, use:  `test_size=0.30`, `random_state=4444`.  You can always experiment with different test_size and random_state, but for submission purposes, use these given settings.

## 8.  Do not print copious output in your Jupyter notebook.
For dictionaries, print a few key/value pairs.  Don't print more than 10-20 lines of data (of data frame or array).
