# Git:  Add, Commit a File & Pull Request

--

## Part 1:  Sync repos

#### Step 1:  Sync your local (`remote upstream`) with `thisismetis/ds17_ds10`
```bash
git pull upstream master
```

**Always "git pull" before sending up any changes**
```
$ pwd
/Users/reshamashaikh/_ds/metis/metisgh/nyc16_ds8

$ git pull  (by default, it pulls from origin, SO DON'T DO THIS)

$ git pull upstream master (we want to pull from master)

$ git pull upstream master
remote: Counting objects: 55, done.
remote: Compressing objects: 100% (31/31), done.
remote: Total 55 (delta 9), reused 0 (delta 0), pack-reused 24
Unpacking objects: 100% (55/55), done.
From https://github.com/thisismetis/nyc16_ds8
 * branch            master     -> FETCH_HEAD
 * [new branch]      master     -> upstream/master
Updating 73c9b7f..e2fa70b
Fast-forward
```
#### Step 2:  Sync your local (`remote origin`) with your forked repo
```bash
git push origin master
```

## Practice - let's add a file
```
$ cd nyc17_ds10/student_submission/challenges/00-practice1
$ mkdir shaikh_reshama
$ cd shaikh_reshama
```

**Note: in the `00-practice1` folder, directories have been made for each student, as an example.  Going forward, you will need to make a folder with your name.**
**Naming Convention:  lastname_firstname  ----> lower case, under scores**

Make a small file
Redirect standard output to a file called “text.txt”
```
$ echo "Hello! Nice to meet you!" > test.txt
echo "Hello! Nice to meet you" > test.txt

$ cat test.txt 
Hello! Nice to meet you

$ git status

$ git log                              # lists past commits

$ git rm myfile.txt                    # use this command to delete a file in repo (not $ rm filename...)

$ git cp myfile.txt newfile.txt        # use this command to copy a file in repo (not $ cp filename...)

$ git                                  # lists commonly used git commands
```

### Adding, committing a file
```
$ git add test.txt                     # sets working copy to staged copy
$ git status
$ git commit -m "add a simple file"    # staged copy to revision history
$ git push origin master               # send it to (my forked) repo
```

### Adding, committing multiple (all) files in a directory (AVOID DOING THIS!!!!!)
```
$ git add .
$ git status
$ git commit -m "adding all files in this repo"
$ git status
$ git push origin master
```

#### Sync repo
```
$ git pull upstream master
$ git push origin master
```

## Pull Request

Go to your forked version
https://github.com/reshama/nyc17_ds10

Right column, go to **"New pull request"**

Click on green **"Create pull request"**

Fill in info at **"Leave a comment"**

Click on green **"Create pull request"**

Look in this repo and see that file has been updated.

--

## Git Commands

```
$ git remote
origin
upstream

$ git remote -v
origin	https://github.com/reshama/nyc17_ds10.git (fetch)
origin	https://github.com/reshama/nyc17_ds10.git (push)
upstream	https://github.com/thisismetis/nyc17_ds10.git (fetch)
upstream	https://github.com/thisismetis/nyc17_ds10.git (push)

$ git log               # gives log of commits

$ git remote origin master
```
>**remote**  origin

>**branch**  master

###Important:  To Remove a File from the Repo
`$ git rm filename`  

###Important:  To Rename or Move a File in the Repo
`$ git mv filename` 

**Note:**  
GitHub:  commit every day, green dots show up on user home page; looks good for potential employers.  
This is what my GitHub activity graph looks like:  
https://github.com/reshama


