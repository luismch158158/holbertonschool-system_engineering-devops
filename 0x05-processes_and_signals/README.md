# Shell, processes and signals
This project is about processes and signals, PID, how to kill a process, what is a signal and what are 2 signals that cannot be ignored
## PROJECTS
0. What is my PID (File: 0-what-is-my-pid)
        - Write a Bash script that displays its own PID.
1. List your processes (File: 1-list_your_processes)
        - Write a Bash script that displays a list of currently running processes.
2. Show your Bash PID (File: 2-show_your_bash_pid)
        - Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.
3. Show your Bash PID made easy (File: 3-show_your_bash_pid_made_easy)
        - Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.
4. To infinity and beyond (File: 4-to_infinity_and_beyond)
        - Write a Bash script that displays To infinity and beyond indefinitely.
5. Don't stop me now! (File: 5-dont_stop_me_now)
        - We stopped our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.
6. Stop me if you can (File: 6-stop_me_if_you_can)
        - Write a Bash script that stops 4-to_infinity_and_beyond process.
7. Highlander (File: 7-highlander)
        - Write a Bash script that displays: To infinity and beyond indefinitely, With a sleep 2 in between each iteration, I am invincible!!! when receiving a SIGTERM signal.
8. Beheaded process (File: 8-beheaded_process)
        - Write a Bash script that kills the process 7-highlander.
        - I started 7-highlander in Terminal #0 and then run 8-beheaded_process in terminal #1 and we can see that the 7-highlander has been killed.
9. Process and PID file (File: 10-process_and_pid_file)
        - Creates the file /var/run/myscript.pid containing its PID
        - Displays To infinity and beyond indefinitely
        - Displays I hate the kill command when receiving a SIGTERM signal
        - Displays Y U no love me?! when receiving a SIGINT signal
        - Deletes the file /var/run/myscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal
10. Manage my process (File: 11-manage_my_process, manage_my_process)
        - Write a manage_my_process Bash script that:
        - Indefinitely writes I am alive! to the file /tmp/my_process
        - In between every I am alive! message, the program should pause for 2 seconds.



Author: Luis Manrique (luismanrique158158@gmail.com)

Linkedin: https://www.linkedin.com/in/luis-manrique158158/

Twitter: https://twitter.com/LuisManriqueDev
