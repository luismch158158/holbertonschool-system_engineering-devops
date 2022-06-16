# 0x04. Loops, conditions and parsing
This project is about create SSH Keys, use while, until, for loops.
Use if, else, elif and case condition statements, and what are files and other comparison operators and how to use them
## PROJECTS

0. Create a SSH RSA key pair (file: 0-RSA_public_key.pub)
	- Create SSH key pair and share your public key
1. For Best School loop (file: 1-for_best_school)
	- Write a Bash script that displays Best School 10 times with for loop.
2. While Best School loop (file: 2-while_best_school)
	- Write a Bash script that displays Best School 10 times with while loop.
3. Until Best School loop (file: 3-until_best_school)
	- Write a Bash script that displays Best School 10 times with until loop.
4. If 9, say Hi! (file: 4-if_9_say_hi)
	- Write a Bash script that displays Best School 10 times, but for the 9th iteration, displays Best School and then Hi on a new line.
	- You must use the while loop and if statement
5. 4 bad luck, 8 is your chance (File: 5-4_bad_luck_8_is_your_chance)
	- Write a Bash script that loops from 1 to 10 and:
		- displays bad luck for the 4th loop iteration
		- displays good luck for the 8th loop iteration
		- displays Best School for the other iterations
	- Requirements:
		- You must use the while loop (for and until are forbidden)
		- You must use the if, elif and else statements
6. Superstitious numbers (File: 6-superstitious_numbers)
	- Write a Bash script that displays numbers from 1 to 20 and:
		- displays 4 and then bad luck from China for the 4th loop iteration
		- displays 9 and then bad luck from Japan for the 9th loop iteration
		- displays 17 and then bad luck from Italy for the 17th loop iteration
	- Requirements:
		- You must use the while loop (for and until are forbidden)
		- You must use the case statement
7. Clock (File: 7-clock)
	- Write a Bash script that displays the time for 12 hours and 59 minutes:
		- display hours from 0 to 12
		- display minutes from 1 to 59
	- Requirements:
		- You must use the while loop (for and until are forbidden)
8. For ls (File: 8-for_ls)
	- Write a Bash script that displays:
		- The content of the current directory
		- In a list format
		- Where only the part of the name after the first dash is displayed (refer to the example)
	- Requirements:
		- You must use the for loop (while and until are forbidden)
		- Do not display hidden files
9. To file, or not to file (File: 9-to_file_or_not_to_file)
	- Write a Bash script that gives you information about the school file.
	- Requirements:
		- You must use if and, else (case is forbidden)
		- Your Bash script should check if the file exists and print:
			- if the file exists: school file exists
			- if the file does not exist: school file does not exist
		- If the file exists, print:
			- if the file is empty: school file is empty
			- if the file is not empty: school file is not empty
			- if the file is a regular file: school is a regular file
			- if the file is not a regular file: (nothing)
10. FizzBuzz (File: 10-fizzbuzz)
	- Write a Bash script that displays numbers from 1 to 100.
	- Requirements:
		- Displays FizzBuzz when the number is a multiple of 3 and 5
		- Displays Fizz when the number is multiple of 3
		- Displays Buzz when the number is a multiple of 5
		- Otherwise, displays the number
		- In a list format
11. Read and cut (File: 100-read_and_cut)
	- help: read
	- Write a Bash script that displays the content of the file /etc/passwd.
	- Your script should only display:
		- username
		- user id
		- Home directory path for the user
	- Requirements:
		- You must use the while loop (for and until are forbidden)
12. Tell the story of passwd (File: 101-tell_the_story_of_passwd)
	- The file /etc/passwd has already been covered in a previous project and you should be familiar with it. Today we will make up a story based on it.
	- Write a Bash script that displays the content of the file /etc/passwd, using the while loop + IFS.
	- Format: The user USERNAME is part of the GROUP_ID gang, lives in HOME_DIRECTORY and rides COMMAND/SHELL. USER ID's place is protected by the passcode PASSWORD, more info about the user here: USER ID INFO
	- Requirements:
		- You must use the while loop (for and until are forbidden)
13. Let's parse Apache logs (File: 102-lets_parse_apache_logs)
	- Write a Bash script that displays the visitor IP along with the HTTP status code from the Apache log file.
	- Requirement:
		- Format: IP HTTP_CODE
			- in a list format
			- See example
		- You must use awk
		- You are not allowed to use while, for, until and cut
		- Download and commit the apache-access.log file along with your answers files
14. Dig the data (File: 103-dig_the-data)
	- Now that you’ve parsed the Apache log file, let’s sort the data so you can get a better idea of what is going on.
	- Using what you did in the previous exercise, write a Bash script that groups visitors by IP and HTTP status code, and displays this data.
	- Requirements:
		- The exact format must be:
			- OCCURENCE_NUMBER IP HTTP_CODE
			- In list format
		- Ordered from the greatest to the lowest number of occurrences
			- See example
		- You must use awk
		- You are not allowed to use while, for, until and cut



Author: Luis Manrique (luismanrique158158@gmail.com)

Linkedin: https://www.linkedin.com/in/luis-manrique158158/

Twitter: https://twitter.com/LuisManriqueDev

