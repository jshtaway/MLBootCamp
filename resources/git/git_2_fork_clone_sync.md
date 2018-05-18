# Fork, Clone & Sync a repo

## Part 1:  Fork & Clone

#### Step 1:  Go to repo
In my personal account on GitHub, go to repo to be cloned.

In this example, it is:  https://github.com/thisismetis/nyc17_ds10  
:arrow_right: **NOTE:  bookmark this**

#### Step 2:  Fork repo
Upper right of github page:  "Fork" the repo

Go to my forked repo: https://github.com/reshama/nyc17_ds10  
:arrow_right: **NOTE:  bookmark this**
 
#### Step 3:  Clone repo
Clone that forked repo (which is now under my name)

In right column, find the link to **HTTPS clone URL** and copy that URL to be cloned.

In terminal: 
* go to directory where repo will be cloned
* clone repo
* cd into clone repo
```
$ metisgh
$ pwd
/Users/reshamashaikh/ds/metis/metisgh

$ cd metisgh/
$ ls

$ git clone https://github.com/reshama/nyc17_ds10.git
```
#### Step 4:  `cd` into cloned repo
```bash
$ cd nyc17_ds10
```

--

## Part 2:  Set upstream

If there are changes to the original repo, how do you get them?  You need to tell your local repo that it can also get updates from the original.

Origin:  reshama/nyc17_ds10


**Note:  Need to be in that directory on Unix to update repo**
```
$ git remote -v
origin	https://github.com/reshama/nyc17_ds10.git (fetch)
origin	https://github.com/reshama/nyc17_ds10.git (push)
```

Want to add reference to metis repo (which is master repo)
Note:  can call it “upstream” or “root” or any other name

```
$ git remote add upstream https://github.com/thisismetis/nyc17_ds10.git
```

Now we see we have two remotes: 
* origin
* upstream
```
$ git remote -v
origin	https://github.com/reshama/nyc17_ds10.git (fetch)
origin	https://github.com/reshama/nyc17_ds10.git (push)
upstream	https://github.com/thisismetis/nyc17_ds10.git (fetch)
upstream	https://github.com/thisismetis/nyc17_ds10.git (push)
```

--

## Part 3:  Sync repos

#### Workflow:  get files from metis (master) down to local (my computer) and up to origin (me/nyc17_ds10)

**Always "git pull" before sending up any changes**

`$ git pull`  (by default, it pulls from origin)

`$ git pull upstream master`  (we want to pull from master)

```
$ git pull upstream master
remote: Counting objects: 55, done.
remote: Compressing objects: 100% (31/31), done.
remote: Total 55 (delta 9), reused 0 (delta 0), pack-reused 24
Unpacking objects: 100% (55/55), done.
From https://github.com/thisismetis/nyc17_ds10
 * branch            master     -> FETCH_HEAD
 * [new branch]      master     -> upstream/master
Updating 73c9b7f..e2fa70b
Fast-forward
...
```

####Check status of your git repo
```
$ git status
```

`$ git push origin` or `$ git push origin master` (we want to push to our forked repo, changes will show up when we go to browser)  

`$ git push`
```
warning: push.default is unset; its implicit value is changing in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the current behavior after the default changes, use:

  git config --global push.default matching

To squelch this message and adopt the new behavior now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

In Git 2.0, Git will default to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

Counting objects: 57, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (52/52), done.
Writing objects: 100% (55/55), 51.21 MiB | 6.26 MiB/s, done.
Total 55 (delta 14), reused 0 (delta 0)
To https://github.com/reshama/nyc17_ds10.git
   73c9b7f..e2fa70b  master -> master

```

**Do this one time only**

`$ git config --global push.default simple`




