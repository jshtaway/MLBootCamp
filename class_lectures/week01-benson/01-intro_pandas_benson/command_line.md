## Command Line Crash Course
The Unix command line permeates everything we'll do in this course.  You can do a wide array of things with it from viewing and manipulating files to running Python programs and other applications.  The more comfortable you get with the command line, the more efficient you'll be with everything.  Think of it as a way to really get to know your computer in a personal way--if you do, your working relationship with your machine will improve tremendously.

### The Command Shell
Unix is a reference to any computer operating system that derives from the original **Unix operating system** from the 1970s.  This includes **Mac OS X** and basically all of the various versions of **Linux** (but not on Windows!  [See below](#windows)).  

The Unix command line is an interface for talking to your computer, usually through what's called a **shell**.  The shell is a program that allows you to type commands and performs the specified actions in response to your commands.  On a Mac, this is what the **Terminal** application is, and you will find a similar application on Linux machines.

There are a number of different "flavors" of shell with slightly different command line syntax for the standard (and other) commands.  The most common flavor of shell these days is **Bash**, and that's what we'll be assuming in this course and this tutorial.  Bash is the default for Terminal on a Mac.  When you open up a shell, you're ready to start typing commands and the computer will respond to these commands via the underlying Unix **Kernel** (the core of the operating system).

### <a href='windows'></a>For Windows Users
Windows has its own operating system kernel and thus its own "shell" for running commands.  In order to use Unix style commands on Windows, you'll need to download some sort of **Unix Command Line Emulator**, for instance [**Cygwin**]().

### The Unix Directory Structure
Unix-based filesystems will have a (mostly) common shared directory structure.  It should look something like the following:  
<img src="img/unix_fs.jpg"/>

#### The `bin` directory
Contains binaries for running many of the commands that you'll type at the command line.  When you type a command, the `/bin` directory is one of the main places that the operating system will search to know what you're asking it to do.  If it finds a matching **executable** (a runnable program matching the command name given), then it will run that.

#### The `etc` directory
Various configuration files etc (:laughing:), we won't worry about this too much right now.

#### The `lib` directory
System libraries and other essentials that the system needs to run various programs under the hood.

#### The `tmp` directory
Where temporary files that may be needed during running programs will/can be stored.

#### The `usr` directory
A secondary directory for user-specific libraries and executables.  The `bin` and `lib` directories are global (for all users).  The `usr` directory will have similar such directories within it which are specific to a given user on a system.  Obviously, this is important on systems that will be shared by multiple users.

#### Your home directory
Your home directory is your home base in a Unix system.  **On a Mac, your home directory is at /Users/<username>**, whereas on **Linux it is located at /home/<username>**.

You can instantly address or get to your home directory via the symbol `~`.  For instance, `cd ~` on a Mac will change your present working directory to /Users/<username>.  This is just like if you clicked your way to their using the Finder GUI.

### General Command Structure

#### Options and Arguments
Running commands in the shell will in general require 3 things:
* The name of the command:
  * e.g. `cd`, `ls`, `cat`, etc
* Arguments the command takes
  * e.g. `<directory_name>` in `cd <directory_name>` or `ls <directory_name>`
* Optional flags ("options") that you can set on the given command to dictate the way it runs
  * e.g. `-l` for `ls -l`, `-rf` for `rm -rf <directory_to_remove>`
  * Options are specified with a leading `-`
  * You can combine multiple options in one `-` (for instance `-rf` above is like `-r -f`)
  * Options usually have more informative alternatives by using `--`, for instance `-V` or `--version`

#### Getting Help
Many times you might know the command you want and not be totally certain about its usage, options, or arguments.  Unix provides various ways to find this by checking out the documentation straight from the command line (even if you're not totally sure of the command name, see `apropos` or `man -k`).

##### `man`
"Manual", calls out to the help manual with all sorts of documentation on the command you specify.
```
# Syntax: man <command_name>
$ man ls
```

**Userful options**:
* `-k`: works like `apropos` below in that it will search for commands that you likely mean.

##### `info`
Works the same way as `man` to give you some documentation on the desired command.
```
# Syntax: info <command_name>
$ info less
```

##### `help`
Not necessarily Unix, but many commands that you can run will accept a `--help` parameter (or something like it) that will print out similar helpful documentation to `man` and `info`.  For instance, try:

```
$ python --help
```

##### `apropos`
Works like `man -k`, searching for the command it thinks you might mean:

```
# Syntax: apropos <search_term>
$ apropos copy
```

**Tip:** `apropos` or `man -k` can be especially handy if you find yourself switching between different flavors of Unix or shell.

### Common Basic Commands
These are commands you'll use over and over, so bookmark this as a reference.  You probably know many of them, but some may be new.

#### Filesystem Navigation
##### `cd`
"Change Directory", switches you to the directory you specify.
```
# Syntax: cd <directory_to_go_to>
$ cd ~
```

What does this do?

##### `pwd`
"Print (or Present) Working Directory", checks the directory that you're currently in and prints it out for you.  All commands run from the directory that you're in.
```
# Syntax: pwd
$ pwd
/Users/paulburkard
```

##### `ls`
Lists the files/directories in your present working directory, or whatever directory you explicitly specify.  
```
# Syntax: ls <path_to_file/directory>
$ ls ~
Applications		Metis Google Drive	Public
Desktop			Movies			git
Documents		Music			scikit_learn_data
Downloads		OneDrive
Library			Pictures
$ ls /bin/
[		df		launchctl	pwd		tcsh
bash		domainname	link		rcp		test
cat		echo		ln		rm		unlink
chmod		ed		ls		rmdir		wait4path
cp		expr		mkdir		sh		zsh
csh		hostname	mv		sleep
date		kill		pax		stty
dd		ksh		ps		sync
```

**Useful `ls` options**:
* `-l`: displays more detailed information about the various files
* `-a`: include hidden files starting with a "."
* `-h`: human readable file sizes like MB or GB (rather than just in huge #s of bytes)

#### Viewing Files

##### `cat`
"Concatenate", prints the contents of the file to standard output (the console by default).

```
# Syntax: cat <filename>
$ echo 'Hello World' > hello.txt
$ cat hello.txt
```

##### `less`
Allow scrolling through files, much better for large files so they don't have to be all dumped to the console (RAM issues) like in `cat`.

```
# Syntax: less <filename>
$ cd ~/git/Metis/Bootcamps/sf16_ds4
$ less README.md
```

**Useful Things:**
* The space bar pages down in the file .
* The arrow keys scroll up/down line by line.
* Hit `q` to exit out of `less` and return to the command prompt.
* `less` can do a lot more!  Take a look [here](http://linux.about.com/od/commands/fl/The-Linux-Top-Command.htm) to see how `less` can help you with searching large files and more.

##### `head`
View the beginning of a file.

```
# Syntax: head <filename>
$ cd ~/git/Metis/Bootcamps/sf16_ds4
$ head README.md
```

**Useful Options:**
* `-n`: The number of lines

##### `tail`
View the end of a file.

```
# Syntax: tail <filename>
$ tail README.md
```

**Useful Options:**
* `-n`: The number of lines
* `-f`: Allow it to keep printing out if new lines are added (useful in logging for instance)

#### Moving Files Around

##### `cp`
"Copy", copy file(s) or directory(ies) from one location to another.

```
# Syntax: cp <from_file> <to_location>
$ cp README.md ~
```

**Useful Options:**
* `-R`: recursive, allows you to copy directories

##### `mv`
"Move" file(s) or directory(ies) from one place to another.

```
# Syntax: mv <from_loc> <to_loc>
mv ~/README.md ..
```

##### `mkdir`
"Make Directory" creates a directory.

```
# Syntax: mkdir <dirname>
$ cd ~
$ mkdir testdir
$ ls -lh
```

##### `rm`
"Remove" file(s)

```
# Syntax: rm <file_name>
$ rm -rf testdir
$ ls -lh
```

**Useful Options:**:
* `-r`: recursive, for directories
* `-f`: force it, aka don't ask if you're sure

#### Examining Disk Space
##### `df`
"Disk Free", Check out the total disk space used/available.

```
# Syntax: df
$ df -h
```

**Useful Options:**
* `-h`: human readable sizes like MB, GB

##### `du`
"Disk Usage", Check out the disk space used by a file or directory.

```
# Syntax: du <directory>
$ du -h -d 1 ~
```

**Useful Options:**
* `-h`: human readable file sizes
* `d`: depth to traverse within a directory

#### Others

##### `find`
Search for files in the filesystem.

```
# Syntax: find <path_to_search> <expression_to_look_for>
$ find ~ git
```

**TIP:** There are a done of things you can do with `find`, check out your manual.

**WARNING:** `find` seems to change a lot between shells and Unix distributions, so use the docs.

##### `grep`
Search text for lines matching a specific pattern.

```
# Syntax: grep <expression_to_look_for> <file>
$ grep data README.md
```

##### `wc`
"Word Count", does exactly what it sounds like.

```
# Syntax: wc <file>
$ wc -l README.md
```

**Useful Options:**
* `-l`: Count lines instead

##### `sort`
You guessed it.

```
# Syntax: sort <input_to_sort>
$ du -h -d 1 ~ | sort
```

##### `who`
Displays the active user(s).

```
# Syntax: who
$ who
```

##### `which`
Find the location of a binary file aka command that you are trying to run.

```
# Syntax: which <program_to_examine>
$ which python
```

##### `gzip`
Zip (compress) files in the gzip format.

```
# Syntax: gzip <file(s)>
$ gzip testdir
```

##### `gunzip`
Unzip gzipped files.

```
# Syntax: gunzip <file>
$ gunzip test.gz
```

##### `tar`
Tar or untar (archive or unarchive) a batch of files.


##### `zcat`
Peak into gzipped files without unzipping them.

##### `echo`
Print a string to standard output (console by default).

```
# Syntax: echo <string>
$ echo 'Hello World'
```

### Input/Output Redirection
So far, all of the output we've seen from commands has gone to the console and all of the input (arguments and options) have come from the Command Line Interface (CLI).  Why is this?

#### Standard Input and Output
The answer lies in 2 important concepts known as stdout and stdin, or Standard Output and Input.  Standard Output is the place where the results of commands will be sent. By default, it is set to be the shell console so command results print out for you.  Similarly, the input stream for the command is inherited from the parent shell as sys.stdin. The command line is parsed by the shell and the arguments passed to the new process so they can be accessed in the program through variables like sys.args.

The fun thing?  We can change both of these things.  There are a number of ways to do this but our simplest are with some basic **redirection operators**:

##### `|`
The "Pipe" will pipe the results of the command preceding it into the input for the command following it.  In effect, it redirects stdout for command 1 to be the input args for command 2 and the stdin for command 2 is now the output of command 1.  

```
$ du -d 1 ~ |  sort -n -r | head
```

What does this do?

**TIP:** You can use pipes to chain together almost any number of commands!

##### `>`, `>>`, and `<`
`>` Can take the output of a preceding command and send it to a specified file.
`>>` Does the same, but doesn't overwrite the file if it exists, just appends to it.
`<` The preceding command gets as arguments the contents of the file following the `<`

```
$ echo 'hello.txt' > goodbye.txt
$ echo 'Hello World' > hello.txt
$ echo 'Hello World' >> hello.txt
$ cat < goodbye.txt
```

### Configuration Files and Environment Variables

Unix Operating Systems run on environment variables.  These are variables that are specified to the system that it will use for running various applications and configuring settings.  Let's take a look at some of them.

##### `env`
Use the command `env` to take a look at your environment variables.

##### `HOME`
Your `$HOME` environment variable is your home directory in the filesystem.  Try this:

```
$ echo $HOME
```

Use this to print out environment variables.

To set environment variables, use `export`:

```
$ export FAKE_ENV_VAR=blah
```

##### `PATH`
The `$PATH` variable is where the Operating System will search for binaries, libraries, etc by default.  When applications have such executables to make use of, they often add them to your `$PATH` variable.

#### `.bashrc` and `.bash_profile` Files
As you know, files beginning with `.` are often special files in Unix systems.  There are (at least) a couple really special files for you to be aware of, the `.bashrc` and `.bash_profile` files.  These 2 files perform essentially the same function.  `.bashrc` is what you'll usually find on Linux systems and `.bash_profile` on your Mac.  

**What are they for?**
In these files you specify a series of startup commands that will get run for every time you open a new shell.  The most common thing to do is setting environment variables that you want to always be set for your user.

The files will always be under your home directory.

```
$ less ~/.bash_profile
```

### Permissions
Unix permissions may seem complicated but they're actually pretty simple.  **For all files in a Unix system there are 3 access classes with 3 types of access for each.**

**Access Classes:**
* User (`u`): The owner of the file being looked at
* Group (`g`): The user group the file belongs to
* Systemwide (`a` all or `o` other): All users on the system

**Access Types:**
* Read (`r`): Whether the user (of a given access class) can read the file
* Write (`w`): Whether the user can write the file
* Execute (`x`): Whether the user can run the file (assuming it's executable)

When you combine these access classes and types, you yield 3x3 = 9 permissions specifications for every file.  That is why when you `ls -lh` you might see a string of `rwx-` characters indicating the access rights for each file.

The order is User, Group, All, and within these it's read/write/execute.  Let's take a look at some examples and talk about what they mean.

```
drwxr-xr-x   5 paulburkard  staff   170B Sep  8 09:21 git
```
Here `paulburkard` has full access (read, write, execute).  The group `staff` has read and execute access but now write, and the same is true for anyone else who might use the system.

What about for this one?
```
drwx------   4 paulburkard  staff   136B Jun  6 10:16 Applications
```
#### Changing Permissions
Now that you understand the access model, here are a few commands that allow you to change the permissions.

##### `chmod`
Change the access permissions on the file.

```
# Syntax: chmod <access_specifier> <file_or_directory>
$ chmod go+w -R git
```

Here are what the various access specifier options mean:
| Symbol | Meaning |
|--------|---------|
| u | User |
| g | Group |
| o | Other |
| a | All |
| r | Read |
| w | Write |
| x | Execute |
| + | Add permission |
| - | Remove Permission |

##### `chown`
Change the owner of a file.

```
# Syntax: chown <user> <file>
$ chown paulburkard README.md
```

##### `chgrp`
Change the group of a file.

```
# Syntax: chgrp <group> <file>
$ chgrp staff README.md
```

### Processes
Anything that is running on a Unix OS is a process.  Here are some commands that help you monitor and control processes.

##### `ps`
List running processes.

**Useful Options:**
* `-e`: Display process environment details
* `-f`: Display all sorts of process details
* Certainly others

##### `top`
Brings up an interactive monitor for checking running processes.  Top has all sorts of different options, so just check it out on your own.

##### `kill` and `pkill`
Kill running processes by various means.

### Text Editors
A number of inline text editors might pop up (or you might open them) in a shell.  They have slightly different syntax, so you can choose whichever one you like best (or just find your own way to ignore them all together!).

These might include `vim` (or `vi`), `nano`, `emacs`, etc

##### vi(m)
An example is `vim`, so here are a few commands for that:
* `Shift+a`: Append mode lets you start editing
* `i`: Insert mode also lets you start editing
* `Esc`: exits out of editing mode
* `:q`: quit without saving (not in editing mode)
* `:x`: quit with saving (not in editing mode)

### Scripts
You can create scripts that run any number of commands, one by one.  Bash (and other shells) are a programming language in themselves, so you can get as fancy as you want with these scripts.  If you see a file that ends with the extensions `.sh`, they're shell scripts that you can execute from the command line.  When you do execute them, it simply runs each line in the script as a shell command.

### Common Tricks

##### Sudo! :no_entry_sign:
`sudo` or `su` are commands for operating as a superuser, or "root" to run programs/commands.  **DO NOT DO THIS** without either thinking very carefully or asking us first.  A lot of times you may need to use `sudo` before a command if the command needs root privileges to run what you're asking it, for instance reading some of the system files deep down in your mac.

##### Kill a Process
`Ctrl+c` will usually kill the active process in a shell.

##### Tab Complete
You can press tab at any point while typing a command to get familiar tab autocompleting functionality.

##### History
You can use the up and down arrows to cycle through previous commands that you've run in a shell, which is very helpful for quickly rerunning the same things.  Alternatively, you can view it all with the `history` command.

##### Clear the Shell
You can clear the output in the current shell with (usually) `Ctrl+l` or `clear`.

##### Jump Cursor Back/Forward
The following commands could be helpful for moving the cursor around:
* `Ctrl+a`: Jump to beginning of line
* `Ctrl+e`: Move to end of line
* `Meta + f`: Move forward a word (a word contains alphabets and digits, no symbols)
* `Meta + b`: Move backward a word
* `Meta` is a special character, it's `alt` on your Mac but you may need to enable it in System Preferences.
* [More](http://teohm.com/blog/shortcuts-to-move-faster-in-bash-command-line/)

##### Wildcards
Frequently you don't know the exact name of a file or files that you want to specify in a command argument, but you do know the pattern that you want to look for.  This is where wildcard characters can come into play:
* `*`: Matches 0 or more of any character
* `?`: Matches 1 character of any type

**Example:**
```
# Copy all .txt files in a directory to your home directory
cp sample_directory/*.txt ~
```

##### Customizing Your Command Prompt
The environment variable `$PS1` controls the prompt that you see in your shell.  If you'd like to change that prompt, you can do so by changing that environment variable.  Take a look at what it is currently by echoing it to the console:
```
$ echo $PS1
```

##### Running in the Background
Running a command proceeded by a `&` will run the resulting process in the background and return control of the shell to you.  This is very useful if you want to run perpetually running services (as opposed to processes that will be killed as soon as you close your shell window).  There are a number of ways you can do this nicely, so feel free to take a look around.

##### Searching for Running Processes
If you want to find a running process (perhaps to get its Process ID, needed to kill it or monitor it), you can do it pretty easilly with this handy command:
```
$ ps -ef | grep <search_term>
```

`search_term` will be the name of the program that you want to find, for instance I might search for "spotify" to take a look at the various processes associated with my Spotify app.

```
$ ps -ef | grep spotify
```
