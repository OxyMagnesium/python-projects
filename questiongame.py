print("")

print("Welcome to the Python Question Game v1.1 by Om Gupta")

readychecker = input("Are you ready? Y/N: ")
if readychecker.upper() == "Y":
  print("")
  print("Great! Let's go!")
elif readychecker.upper() == "N":
  print("")
  print("Run the program again when you're ready")
  quit()
else:
  print("")
  print("That doesn't make sense. Run the program again and enter Y/N.")
  quit()
  
print("")

def cap(x):
  x = x[0].upper() + x[1:len(x)].lower()
  return x

print("Question 1")
name = input("What is your name?: ")
name = cap(name)

print("Question 2")
birthyear = input("In what year were you born?: ")
birthyear = cap(birthyear)

print("Question 3")
city = input("Which city do you live in?: ")
city = cap(city)

print("")

from datetime import datetime
datetime = datetime.today()
year = datetime.year
age = (int(year) - int(birthyear))

print("So, your name is " + str(name) +  ", you are " + str(age) + " years old and you live in " + str(city) + ". Nice to meet you!")
