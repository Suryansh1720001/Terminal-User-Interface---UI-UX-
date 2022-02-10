import os
import getpass
os.system("tput setaf 1")
print("\t\tHey Welcome ! to my TUI thats makes life Simple")
os.system("tput setaf 7")
print("\t\t---------------------------------------------")
print("Enter the password : ")
password = getpass.getpass()
wrong_pass=1
flag=True
while password!="Suryansh":
	if wrong_pass==1:
		os.system("tput setaf 4")
		print("You entered wrong job- Now you have 2 chances to write it correct")
		os.system("tput setaf 7")
	print("You entered wrong password! ")
	print("Again, Enter your password: ")
	password = getpass.getpass()
	wrong_pass+=1
	if wrong_pass==3:
		if password!="Suryansh":
			os.system("tput setaf 1")
			print("Sorry! You entered wrong password 3 times!")
			os.system("tput setaf 7")
			exit() 
else:
	print("Where you would like to perform your job (local/remote): ", end='')
	location = input()

	wrongjob=1
	flag=True
	while wrongjob<=3 and flag==True:
		if location!="local" and location!="remote":
			if wrongjob==1:
				print("you entered wrong job - you have now only 2 times to write correct Job!")
			location=input("Please! Enter the valid job (local/remote): ")
			wrongjob+=1
		else:
			flag=False
	if wrongjob==4:
		os.system("tput setaf 1")
		print("You entered wrong job 3 times! \n plz try again after some time")
		os.system("tput setaf 7")
		exit()

	if location=="remote":
		os.system("tput setaf 3")
		print("In which server you want to run : ")
		remoteIp = input("Enter remote Ip address: ")
	os.system("tput setaf 7")

	while True:
	 	#print("********************************************************************************")
		os.system("tput setaf 6")
		print("\t\t    Press 1 : For Printing the date")
		print("\t\t    Press 2 : For Checking the Calender")
		print("\t\t    Press 3 : For Add New User")
		print("\t\t    Press 8 : For checking the user")
		print("\t\t    Press 4 : For Creating the folder")
		print("\t\t    Press 5 : For Download any software")
		print("\t\t    Press 6 : For Unistall any software")
		print("\t\t    Press 9 : For Configure your Web Server")
		print("\t\t    Press 10: To check all Network card and IP address")
		print("\t\t    Press 11: For seeing the Port number related to many servers")
		print("\t\t    Press 7 : for exit from this software")
		print("*******************************************************************************")
							      
		os.system("tput setaf 7")
		print("Enter your choice: ", end ="")
		ch = int(input())

		if location=="local":
			if ch==1:
				os.system("date")
			elif ch==2:
				os.system("cal")
			elif ch==3:
				print("Can you plz. tell me the name of user you want to add")
				New_User = input()
				os.system("useradd {}".format(New_User))
				print("enter your password for New User")
				os.system("passwd {}".format(New_User))
			elif ch==4:
				print("Enter your New Folder Name: ", end="")
				Folder_name = input()
				os.system("mkdir {}".format(Folder_name))
			elif ch==5:
				print("Enter the software name")
				Download_software = input()
				os.system("dnf install {}".format(Download_software))
			elif ch==6:
				print("Enter the software name")
				Unisatall_Software = input()
				os.system("dnf remove {}".format(  Unisatall_Software))
				os.system("tput setaf 2")
				print("Software is completed removed!")
				os.system("tput setaf 7")
			elif ch==7:
				os.system("tput setaf 2")
				print("Thank you! for using this Software.")
				os.system("tput setaf 7")
				exit()
			elif ch==8:
				print("Enter User Name you want to check: ", end="")
				User_Name = input()
				os.system("id {}".format(User_Name))
			elif ch==9:
				os.system("tput setaf 2")
				print("Initilizing web server: HTTPD")
				os.system("tput setaf 7")
				os.system("dnf install httpd")
				os.system("tput setaf 2")
				print("Your web server is installed")
				os.system("tput setaf 7")
				os.system("systemctl start httpd")
				os.system("tput setaf 2")
				print("your services HTTPD are started")
				os.system("tput setaf 7")
				os.system("systemctl stop firewalld")
			elif ch==10:
				os.system("tput setaf 2")
				print("Network cards are : ")
				os.system("tput setaf 7")
				os.system("ifconfig")
			elif ch==11:
				os.system("tput setaf 2")
				print("Network cards are : ")
				os.system("tput setaf 7")
				os.system("netstat -tnlp")

			
			else:
				print("wrong input")
			input("Enter to continue....")		
			os.system("clear")
		
	 
		else:


			#os.system("ssh roo@{}".format(remoteIp)) 
											 
			if ch==1:
				os.system("ssh {} date".format(remoteIp))
				
			elif ch==2:
				os.system("ssh {} cal".format(remoteIp))
				
			elif ch==3:
				print("Can you plz. tell me the name of user you want to add")
				New_User = input()
				os.system("ssh {0} useradd {1}".format(remoteIp ,New_User))
				print("enter your password for New User")
				os.system("ssh {0} passwd {1}".format(remoteIp,New_User))
			elif ch==4:
				print("Enter your New Folder Name: ", end="")
				Folder_name = input()
				os.system("ssh {0} mkdir {1}".format( remoteIp,Folder_name))
			elif ch==5:
				print("Enter the software name")
				Download_software = input()
				os.system("ssh {} dnf install {}".format(remoteIp,Download_software))
			elif ch==6:
				print("Enter the software name")
				Unisatall_Software = input()
				os.system("ssh {} dnf remove  {}".format( remoteIp,Unisatall_Software ))
				os.system("tput setaf 2")
				print("Software is completed removed!")
				os.system("tput setaf 7")
			elif ch==7:
				os.system("tput setaf 2")
				print("Thank you! for using this Software.")
				os.system("tput setaf 7")
				exit()
			elif ch==8:
				print("Enter User Name you want to check: ",end="")
				User_Name = input()
				os.system("ssh {0} id {1}".format(remoteIp,User_Name))
			elif ch==9:
				os.system("tput setaf 2")
				print("Initilizing web server: HTTPD")
				os.system("tput setaf 7")
				os.system("ssh {} dnf install httpd".format(remoteIp))
				os.system("tput setaf 2")
				print("Your web server is installed")
				os.system("tput setaf 7")
				os.system("ssh {} systemctl start httpd".format(remoteIp))
				os.system("tput setaf 2")
				print("your services HTTPD are started")
				os.system("tput setaf 7")
				os.system("ssh {} systemctl stop firewalld".format(remoteIp))
			elif ch==10:
				os.system("tput setaf 2")
				print("Network cards are : ")
				os.system("tput setaf 7")
				os.system("ssh {} ifconfig".format(remoteIp))

			elif ch==11:
				os.system("tput setaf 2")
				print("Network cards are : ")
				os.system("tput setaf 7")
				os.system("ssh {} 'netstat -tnlp'".format(remoteIp))
				
			else:
				print("wrong input")
			input("Enter to clear....")
			os.system("clear")
			
				
			
