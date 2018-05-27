print("")

question = 1
total = 0
correct = 0

output = ""

import os

os.chdir(r"C:\Users\Om Gupta\Documents\Test archives")

while True:
	intake = input("Question " + str(question) + ": ")
	if intake == "end":
		break
	elif intake == "1":
		intake_p = "Correct"
		correct += 1
	else:
		intake_p = "Incorrect"
	output += ("Question " + str(question) + ": " + intake_p + "\n")
	total += 1
	question += 1

print("")
output += "\n"

print("You got " + str(correct) + "/" + str(total) + " questions correct.")
output += ("You got " + str(correct) + "/" + str(total) + " questions correct.\n")
print("Your percentage was " + str(round((correct/total)*100, 2)) + "%.")
output += ("Your percentage was " + str(round((correct/total)*100, 2)) + "%.\n")

print("")
output += "\n"

archive = open("newtest.txt", "w")
archive.write(output)
archive.close()

save_bool = input("Do you want to archive this test? (Y/N): ")

if save_bool.lower() == "y":
		file_name = input("Enter archival name: ")
		os.rename("newtest.txt", file_name + ".txt")
		print("Test was archived as " + file_name + ".txt under Documents - Test archives.")
else:
        os.remove("newtest.txt")
        print("Test was not archived.")

print("")

end_stop = input("Press enter to quit.")
