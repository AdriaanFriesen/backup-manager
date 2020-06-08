from shutil import copyfile
import os, sys, shutil
def clr():
	print("\n" * 150)
def userinput(numofchoices, displaytext):
	noerror = False
	while not noerror:
		clr()
		alreadybeentold = False
		print(displaytext)
		try:
			choice = int(input())
		except:
			clr()
			input("You must input a number 1-" + str(numofchoices) + ".\nPress -ENTER- to try again.\n")
			alreadybeentold = True
		if alreadybeentold == False:
			if choice < 1 or choice > numofchoices:
				clr()
				input("You must input a number 1-" + str(numofchoices) + ".\nPress -ENTER- to try again.\n")
			else:
				noerror = True
		elif alreadybeentold == False:
			noerror = True
	return choice
def dynamicuserinput(displaytext):
	noerror = False
	listofbackups = []
	listofbackupstemp = []
	with open(sys.path[0] + "/resources/list.txt","r",encoding = "utf-8") as a:
		for line in a:
			listofbackups.append(line)
	for x in listofbackups:
		listofbackupstemp.append(x.replace("\n", ""))
	listofbackups = listofbackupstemp
	listofbackupstemp = []
	lengthoflist = str(len(listofbackups) + 1)
	while not noerror:
		clr()
		print(displaytext)
		alreadybeentold = False
		y = 0
		lookuptable = {}
		for x in listofbackups:
			y += 1
			print(str(y) + " - " + x)
			lookuptable[y] = x
		alreadybeentold = False
		try:
			choice = int(input())
		except:
			clr()
			input("You must input a number 1-" + str(y) + ".\nPress -ENTER- to try again.\n")
			alreadybeentold = True
		if alreadybeentold == False:
			if choice < 1 or choice > y:
				clr()
				input("You must input a number 1-" + str(y) + ".\nPress -ENTER- to try again.\n")
			else:
				noerror = True
		elif alreadybeentold == False:
			noerror = True
	return choice, lookuptable
six = False
while not six:
	listofbackups = []
	listofbackupstemp = []
	with open(sys.path[0] + "/resources/list.txt","r",encoding = "utf-8") as a:
		for line in a:
			listofbackups.append(line)
		for x in listofbackups:
			listofbackupstemp.append(x.replace("\n", ""))
			listofbackups = listofbackupstemp
			listofbackupstemp = []
			lengthoflist = str(len(listofbackups) + 1)
	noerror = False
	choice = userinput(6, """Hello! Here you can create and load backups.
Make sure you have put in the paths of the
files you want to backup in files.txt.
Select an option:
1 - Create backup
2 - Load backup
3 - View backups
4 - Delete backup
5 - View an example of files.txt
6 - Exit program""")
	if choice == 1:
		noerror = False
		choice = userinput(2, """Would you like to make a new backup or overwrite an old one?
1 - New backup
2 - Update existing backup""")
		if choice == 1:
			noerror = False
			while not noerror:
				clr()
				name = str(input("Ok, name your backup:\n"))
				clr()
				desc = str(input("Now input a description:\n"))
				clr()
				if os.path.exists(sys.path[0] + "\\backups\\backup " + name):
					clr()
					input("A backup with that name already exists.\nPress -ENTER- to try again.\n")
				else:
					noerror = True
					print("Creating folder...")
					if not os.path.exists(sys.path[0] + "\\backups\\backup " + name):
						os.makedirs(sys.path[0] + "\\backups\\backup " + name)
					else:
						print("A fatal error occured.")
					if not os.path.exists(sys.path[0] + "\\backups\\backup " + name + "\\info.txt"):
						with open(sys.path[0] + "\\backups\\backup " + name + "\\info.txt","w",encoding = "utf-8") as a:
							a.write(name + "\n" + desc + "\n")
					else:
						print("A fatal error occured.")
					with open(sys.path[0] + "\\resources\\list.txt","a",encoding = "utf-8") as a:
						a.write(name + "\n")
					with open(sys.path[0] + "\\files.txt","r",encoding = "utf-8") as a:
						for line in a:
							b = line.replace("\n", "")
							c = b.replace("/", "\\")
							list1 = c.split("\\")
							for x in range(len(list1) - 1):
								list1.pop(0)
							copyfile(c, sys.path[0] + "\\backups\\backup " + name + "\\" + list1[0])
					input("Done!\nPress -ENTER- to go back to the menu.\n")
		elif choice == 2:
			try:
				oops = listofbackups[0]
				results = dynamicuserinput("Select a backup to update:")
				choice = results[0]
				lookuptable = results[1]
				name = lookuptable.get(choice)
				with open(sys.path[0] + "\\backups\\backup " + name + "\\info.txt") as a:
					a.readline()
					choice = userinput(2, "Here's the description for " + str(name) + ":\n\n" + a.readline() + "\nAre you sure you want to update " + str(name) + "?\n1 - No\n2 - Yes")
				if choice == 1:
					clr()
					input("Press -ENTER- to go back to the menu\n")
				elif choice == 2:
					clr()
					print("Copying files...")
					with open(sys.path[0] + "\\files.txt","r",encoding = "utf-8") as a:
						for line in a:
							b = line.replace("\n", "")
							c = b.replace("/", "\\")
							list1 = c.split("\\")
							for x in range(len(list1) - 1):
								list1.pop(0)
							copyfile(c, sys.path[0] + "\\backups\\backup " + name + "\\" + list1[0])
					input("Done!\nPress -ENTER- to go back to the menu.\n")
			except:
				clr()
				input("You dont have any backups to update.\nPress -ENTER- to go back to the menu\n")
	elif choice == 2:
		try:
			oops = listofbackups[0]
			results = dynamicuserinput("Select a backup to load:")
			choice = results[0]
			lookuptable = results[1]
			name = lookuptable.get(choice)
			with open(sys.path[0] + "\\backups\\backup " + name + "\\info.txt") as a:
					a.readline()
					choice = userinput(2, "Here's the description for " + str(name) + ":\n\n" + a.readline() + "\nAre you sure you want to load " + str(name) + "?\n1 - No\n2 - Yes")
			if choice == 1:
				clr()
				input("Press -ENTER- to go back to the menu\n")
			elif choice == 2:
				clr()
				print("Copying files...")
				with open(sys.path[0] + "\\files.txt","r",encoding = "utf-8") as a:
					for line in a:
						b = line.replace("\n", "")
						c = b.replace("/", "\\")
						list1 = c.split("\\")
						for x in range(len(list1) - 1):
							list1.pop(0)
						copyfile(sys.path[0] + "\\backups\\backup " + name + "\\" + list1[0], c)
				input("Done!\nPress -ENTER- to go back to the menu.\n")
		except:
			clr()
			input("You dont have any backups to load.\nPress -ENTER- to go back to the menu\n")
	elif choice == 3:
		try:
			oops = listofbackups[0]
			results = dynamicuserinput("Select a backup to read its description:")
			clr()
			choice = results[0]
			lookuptable = results[1]
			name = str(lookuptable.get(choice))
			with open(sys.path[0] + "\\backups\\backup " + name + "\\info.txt","r",encoding = "utf-8") as a:
				a.readline()
				input("Here is the description for " + name + ":\n\n" + a.readline() + "\nPress -ENTER- to go back to the menu\n")
		except:
			clr()
			input("You dont have any backups.\nPress -ENTER- to go back to the menu\n")
	elif choice == 4:
		try:
			oops = listofbackups[0]
			results = dynamicuserinput("Select a backup to delete:")
			choice = results[0]
			lookuptable = results[1]
			name = str(lookuptable.get(choice))
			with open(sys.path[0] + "\\backups\\backup " + name + "\\info.txt","r",encoding = "utf-8") as a:
				a.readline()
				choice = userinput(2, "Here's the description for " + name + ":\n\n" + a.readline() + "\nAre you sure you want to delete " + name + "?\n1 - No\n2 - Yes")
			if choice == 1:
				clr()
				input("Press -ENTER- to return to the menu\n")
			if choice == 2:
				clr()
				print("Deleting files...")
				with open(sys.path[0] + "\\resources\\list.txt","r+",encoding = "utf-8") as a:
					lines = a.readlines()
					a.seek(0)
					a.truncate()
					for b in lines:
						if b.strip("\n") != name:
							a.write(b)
				shutil.rmtree(sys.path[0] + "\\backups\\backup " + name)
				input("Done!\nPress -ENTER- to go back to the menu.\n")
		except:
			clr()
			input("You dont have any backups to delete.\nPress -ENTER- to go back to the menu\n")
	elif choice == 5:
		clr()
		with open(sys.path[0] + "/resources/filesexample.txt", encoding = "utf-8") as a:
			print(a.read())
		input("\nPress -ENTER- to go back to the menu.\n")
	elif choice == 6:
		six = True
	else:
		six = True
		input("A fatal error occured.\n")
