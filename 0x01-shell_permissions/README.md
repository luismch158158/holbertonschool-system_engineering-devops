# 0x01. Shell, permissions
Project about Linux SO permissions.

## TASKS

0. My name is Betty
	- Switches the current user to the user betty
1. Who am I
	- This script prints the effective username of the current user.
2. Groups
	- This script prints all the groups the current user is part of.
3. New owner
	- This script changes the owner of the file hello to the user betty.
4. Empty!
	- This script creates an empty file called hello
5. Execute
	- This script adds execute permission to the owner of the file hello.
6. Multiple permissions
	- This script execute permission to the owner and the group owner, and read permission to other users, to the file hello.
7. Everybody!
	- This script adds execution permission to the owner, the group owner and the other users, to the file hello, without use commas.
8. James Bond
	- This script sets the permission to the file hello as follows: owner and group (no permission at all) and other user (all the permissions)
9. John Doe
	- This script sets the mode of the file hello to this: -rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
10. Look in the mirror
	- This script sets the mode of the file hello the same as olleh’s mode.
11. Directories
	- This script adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.
12. More Directories
	- This script creates a directory called my_dir with permissions 751 in the working directory.
13. Change group
	- This script changes the group owner to school for the file hello
14. Owner and group (file: 100-change_owner_and_group)
	- This script changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.
15. Symbolic links (file: 101-symbolic_link_permissions)
	- This script changes the owner and the group owner of _hello to vincent and staff respectively. Where the _hello is a symbolic link and is located in the current directory
16. If only (file: 102-if_only)
	- This script changes the owner of the file hello to vincent only if it is owned by the user guillaume.
17. Star Wars (file: 103-Star_Wars)
	- With this script play the StarWars IV episode in the terminal
	- Note: For close or stop the animations, press ctrl + ], after write quit in your terminal.

**Author**:
Luis Manrique (luismanrique158158@gmail.com)
