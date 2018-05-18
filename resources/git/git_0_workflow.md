# Git Workflow

## Table of Contents
[Part 1:  Sync repos (do this first thing in the morning)](#section-a)  
[Part 2:  Launch Jupyter notebook from working branch.  (Mine is `reshama_wip`)](#section-b)  
[Part 3:  Your working branch](#section-c)  
[Part 4:  Add & Commit File in working branch](#section-d)  
[Part 5:  Submit pull request from `master` branch](#section-e)  
 

## <a name="section-a"></a>Part 1:  Sync repos (do this first thing in the morning)

#### Step 1:  Make sure you are in your repo and in the `master` branch
```bash
pwd
```
>```bash
pwd
/Users/reshamashaikh/_ds/metis/metisgh/nyc17_ds10
```  

```bash
git branch
```  

>```bash
 git branch
* master
  reshama_wip
```
  
#### Step 2a:  sync `thisismetis/nyc17_ds10` with your local copy (remote `upstream` and branch `master`)
```bash
git pull upstream master
```

#### Step 2b:  sync your remote `origin` & branch `master` with your forked repo `reshama/nyc17_ds10`
```bash
git push origin master
```

#### Step 3:  switch to working branch.  Mine is `reshama_wip`
```bash
git checkout reshama_wip
```
```bash
 git branch
  master
* reshama_wip
```
#### Step 4a:   sync `thisismetis/nyc17_ds10` with your remote `upstream` and branch `reshama_wip`
```bash
git pull upstream master
```
#### Step 4b:  sync your remote `origin` & branch `reshama_wip` with your forked repo `reshama/nyc17_ds10`
```bash
git push origin reshama_wip
```

Viola!  Everything will be synced up now, and it's a good place to begin the day.  :sunny:

---

## <a name="section-b"></a>Part 2:  Launch Jupyter notebok from working branch.  (Mine is `reshama_wip`)

#### Step 1:  Check which branch you are in  
```bash
git branch
``` 

>```bash
metis/metisgh/nyc17_ds10  master ✔                                                                                                  39d  
▶ git branch
* master
  reshama_wip
```

#### Step 2:  Switch to working branch 
```bash
git checkout reshama_wip
```

>```bash
git checkout reshama_wip
Switched to branch 'reshama_wip'
```
```bash
git branch
  master
* reshama_wip
```

#### Step 3:  Launch Jupyter Notebook
```bash
metis/metisgh/nyc17_ds10  reshama_wip ✔                                                                                             39d  
▶ jupyter notebook
```

---

## <a name="section-c"></a>Part 3:  Your working branch

### Note:  this is where you will do any work, in the working branch.  For me, it is `reshama_wip`**  

### Classwork
 * If you're going to edit a Jupyter notebook in `class_lectures`, make a copy and rename it.  Can add your name to end of notebook.  
   * Example:  `Intro-to-Pandas.ipynb` --- > `intro_to_pandas_reshama.ipynb`
   
### Challenges

 
#### Step 1:  Navigate to working directory
```bash
pwd
/Users/reshamashaikh/_ds/metis/metisgh/nyc17_ds10/student_submissions/challenges/01-mta/shaikh_reshama         
```

#### Step 2:  Create a notebook (in working branch)
 * launch Jupyter Notebook
 * Example:  `ch_set_1_reshama.ipynb`
 * Work in this file

When challenge set is ready for submission, go to next step

---

## <a name="section-d"></a>Part 4:  Add & Commit File in working branch


```bash
▶ pwd
/Users/reshamashaikh/_ds/metis/metisgh/nyc17_ds10/student_submissions/01-mta/shaikh_reshama

student_submissions/01-mta/shaikh_reshama  reshama_wip ✗                                         39d ◒  
▶ ls
total 8
-rw-r--r--  1   20 Jan  1 21:40 ch_set_1_reshama.py

student_submissions/01-mta/shaikh_reshama  reshama_wip ✗                                         39d ◒  
▶ pwd
/Users/reshamashaikh/_ds/metis/metisgh/nyc17_ds10/student_submissions/01-mta/shaikh_reshama

student_submissions/01-mta/shaikh_reshama  reshama_wip ✗                                         39d ◒  
▶ ls
total 8
-rw-r--r--  1   20 Jan  1 21:40 ch_set_1_reshama.py

student_submissions/01-mta/shaikh_reshama  reshama_wip ✗                                         39d ◒  
▶ git add ch_set_1_reshama.py 

student_submissions/01-mta/shaikh_reshama  reshama_wip ✗                                         39d ✚  
▶ git commit -m 'adding challenge set 1 for reshama'
[reshama_wip 72c1638] adding challenge set 1 for reshama
 1 file changed, 1 insertion(+)
 create mode 100644 student_submissions/01-mta/shaikh_reshama/ch_set_1_reshama.py
```

---

## <a name="section-e"></a>Part 5:  Submit pull request from `master` branch
 
 
### Copy file/folder from one branch to current branch (`master`)

#### Copy file from one branch to current branch (`master`)
Run this from the branch where you want the file to end up:  
on:  `master` branch
```
git checkout branch_wip myfile.txt
```

#### Copy directory from one branch to current branch (`master`)
on:  `master` branch
```
git checkout branch_wip myfolder/** 
```

