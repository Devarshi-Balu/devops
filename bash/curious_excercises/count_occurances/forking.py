import os, sys, time

print("A tutorial on forking")
pid = os.fork()

print(pid)

if (pid == 0): 
    print("this is a child process")
    time.sleep(4.0)
    print("exiting the process")
    sys.exit(1)
else:
    os.waitpid(pid, 0)
    print("this is the parent process")
