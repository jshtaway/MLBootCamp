# <center>Git and Github</center>

![alt text](https://imgs.xkcd.com/comics/git.png "XKCD")


---
# The Basic Cycle

Remember this and everything will be fine
```
git pull
<make your changes>
git add .
git commit -m'change description'
git pull
git push
```
---

![git commands](http://i.stack.imgur.com/caci5.png)

---
#Don't worry its hard to mess up too badly

![burn it all down](http://i.imgur.com/XFQLB.jpg)


---


# Getting started  

This flow works well for personal use and small teams, but with this many git newbs it would be chaos.
Instead we are going to have you each fork the curriculum repo, where you will have complete control,
        and then you can 'pull request' when you are ready to submit your work  

#### A Note for Windows Users  
We will work with Git as a command line utility.  The Unix command line is native on Mac OS X, but in order to emulate it on Windows you will need to download [Git Bash](https://git-for-windows.github.io/).

---


## Step 1:  Go to repo
In your personal account on GitHub, go to repo to be cloned.

In this example, it is:  https://github.com/thisismetis/sf17_ds6  
**>> NOTE:  bookmark this**

---


## Step 2:  Fork repo
Upper right of github page:  "Fork" the repo

Go to your forked repo: https://github.com/your_username/sf17_ds6  
**>> NOTE:  bookmark this**

---



## Step 3:  Clone repo
Clone that forked repo (which is now under your name)

In right column, find the link to **HTTPS clone URL** and copy that URL to be cloned.

In terminal:
* go to directory where repo will be cloned
* clone repo
* cd into cloned repo

```
$ git clone https://github.com/<your user name>/sf17_ds6.git
$ cd sf17_ds6
```
---


## Set upstream

If there are changes to the original repo, how do you get them?  You need to tell your local repo that it can also get updates from the original.

Origin:  <your name>/sf17_ds6

**Note:  Need to be in that directory on Unix to update repo**
```
$ git remote -v
origin	https://github.com/<your name>/sf17_ds6.git (fetch)
origin	https://github.com/<your name>/sf17_ds6.git (push)
```
---
Want to add reference to metis repo (which is master repo)
Note:  can call it “upstream” or “root” or any other name
```
$ git remote add upstream https://github.com/thisismetis/sf17_ds6.git
```

Now we see we have two remotes:
* origin
* upstream
```
$ git remote -v
origin	https://github.com/<your name>/sf17_ds6.git (fetch)
origin	https://github.com/<your name>/sf17_ds6.git (push)
upstream	https://github.com/thisismetis/sf17_ds6.git (fetch)
upstream	https://github.com/thisismetis/sf17_ds6.git (push)
```
---
## Sync repos

**Always "git pull" before sending up any changes**

$ git pull  (by default, it pulls from origin)

$ git pull upstream master (we want to pull from master)

```
$ git pull upstream master
remote: Counting objects: 55, done.
remote: Compressing objects: 100% (31/31), done.
remote: Total 55 (delta 9), reused 0 (delta 0), pack-reused 24
Unpacking objects: 100% (55/55), done.
From https://github.com/thisismetis/sf17_ds6
 * branch            master     -> FETCH_HEAD
 * [new branch]      master     -> upstream/master
Updating 73c9b7f..e2fa70b
Fast-forward
...
```
---
`$ git status`

git push or git push origin master
change from local master branch (my computer) and up to origin (<your_name>/sf17_ds6)

**Do this one time only**

`$ git config --global push.default simple`

---
### Sync repos

**Always "git pull" before sending up any changes**
```
$ git pull  (by default, it pulls from origin)
```
---
## Practice - let's add a file
```
$ cd sf17_ds6/challenges/00-practice
$ mkdir <your name>
$ cd <your name>
```

Make a small file
Redirect standard output to a file called “text.txt”
```
$ echo "Hello! Nice to meet you!" > test.txt
echo "Hello! Nice to meet you" > test.txt

$ cat test.txt
Hello! Nice to meet you
```
---
```
$ git status
```
---
```
$ git rm myfile.txt                    # use this command to delete a file in repo (not $ rm filename...)

$ git cp myfile.txt newfile.txt        # use this command to copy a file in repo (not $ cp filename...)
```
---
```
$ git                                  # lists commonly used git commands
```
---
### Adding, committing a file
```
$ git add test.txt                     # sets working copy to staged copy
$ git status
$ git commit -m "add a simple file"    # staged copy to revision history
$ git push                             # send it to (my forked) repo
```
---
### Adding, committing multiple (all) files in a directory
```
$ git add .
$ git status
$ git commit -m "adding all files in this repo"
$ git push
```
---
### Adding, committing all .txt files in a directory
```
$ git add *.txt
$ git status
$ git commit -m "adding all txt files in this repo"
$ git push
```
---
### Adding, committing all .txt files that contain the word "llama" in a directory
```
$ grep “llama” . -rlw | xargs git add
$ git status
$ git commit -m "adding all the llama files in this repo"
$ git push
```
---
#### Sync repo
```
$ git pull upstream master
$ git push
```
---
## Pull Request

Go to your forked version
https://github.com/<your name>/sf17_ds6

Right column, go to "New pull request"

Click on green "Create pull request"

Fill in info at "Leave a comment"

Click on green "Create pull request" at bottom of page.

Look in this repo and see that file has been updated.

---

**Note:**  
GitHub:  commit every day, green dots show up on user home page; looks good for potential employers.
