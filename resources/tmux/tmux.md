Tmux is a terminal multiplexer.  With it, you can access a tmux terminal using multiple virtual terminals. 

Essentially, tmux allows you to run several terminals at once concurrently off of a single tmux session.  

Most importantly, disconnecting from your cloud server will not kill the processes running inside the tmux session!  This is incredibly powerful when dealing with running jobs on massive data sets (you no longer have to wait for the job to finish before shutting down)

Install tmux :

```bash
sudo apt-get update
sudo apt-get install tmux
```

Begin a new session & name it (ex: "newsession" or such) :

```bash
tmux new -s newsession
```

As mentioned, the tmux session will continue to run in
the background even when you are not connecting to the VPS.

(lets say you shut down for a bit..) 
you can ssh back in: 

```bash
ssh yourmachine 
```

Once on your remote server, simply run : 

```bash
tmux attach -t newsession
```

You will see that your processes are still running! 

You can also: 

```bash
# list all the names of your tmux sessions
tmux list-sessions
# or leave a session
cntl-b d
```


