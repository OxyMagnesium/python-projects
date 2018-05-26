question = 1
total = 0
correct = 0

#import sys
#import os

#sys.stdout = open("target.txt", "w")

while True:
	intake = input("Question " + str(question) + ": ")
	if intake == "end":
		break
	if intake == "1":
		correct += 1
	total += 1
	question += 1

print("")

print("You got " + str(correct) + "/" + str(total) + " questions correct.")
print("Your percentage was " + str(round((correct/total)*100, 2)) + "%.")

#sys.stdout.close()

#save_bool = input("Do you want to archive this test? ")

#if save_bool == "yes":
#        file_name = input("Enter archival name: ")
#        os.rename("target.txt", file_name + ".txt")
#        print("Test was archived as " + file_name + ".txt.")
#else:
#        os.remove("target.txt")
#        print("Test was not archived.")

print("")

print("Press enter to exit.")

