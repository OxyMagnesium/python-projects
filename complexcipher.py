dictionary = ['0', '!', 'a', 'b', '1', 'c', 'd', '2', 'e', 'f', ',', 'g', 'h', '3', 'i', 'j','.', 'k', 'l', '4', 'm', ' ', 'n', '5', 'o', 'p', ':', 'q', 'r', '6', 's', 't', '\'', 'u', 'v', '7', 'w', 'x', '8', 'y', 'z', '?', '9']

#Function start

def convert(text): #Main function.
  text = text.strip() #Setting up requirements for the algorithm.
  output = ""
  mult = 0

  if function == "encode": #Checking whether to encode or decode.
    mult = 1
  elif function == "decode":
    mult = -1

#Algorithm start

  for letter in range(len(text)): #Main algorithm.
    uppercase = "N/A"
    input = text[letter] #Taking the first character.

    input = input.lower() #Making it lowercase.

    if input == "`": #"`" Represents a space, since a space would be otherwise deleted by line 6. This turns it back into a space.
      input = " "

    if input not in dictionary: #Checking if the user entered an unsupported character.
      return "Sorry, \"" + input + "\" is not supported."

    key = (dictionary.index(input) + mult) #Converts the input character into its index in the dictionary, and then adds the multiplier to it toconvert it to something else.

    if key > 42: #Ensuring that the new index is in the range of the dictionary.
      key = (key - 42) - 1
    elif key < 0:
      key = (key + 42) + 1

    output += dictionary[key] #Converting the new index to a character and adding it to the output string.

    if mult > 0: #Increasing the multiplier to increase the scrambling. The multiplier must not exceed +-42 because if it does, then it will cause an error when added to the string.
      mult += 1
    elif mult < 0:
      mult -= 1
    mult *= -1
    if mult > 42:
      mult = 1
    elif mult < -42:
      mult = -1

#Algorithm end

  if output[0] == " ": #If the first or last characters are spaces, they are converted to "`" so they aren't lost.
    output = "`" + output[1:len(output)]
  if output[(len(output) - 1)] == " ":
    output = output[0:(len(output) - 1)] + "`"

  return output

#Function end
#Program start

print("")

print("Welcome to ComplexCipher v1.2.2 by Om Gupta!")

quit_wish = "y"

while quit_wish == "y":
  makes_sense = "n"
  while makes_sense == "n":
    function = input("Enter function to be performed. (Encode/Decode): ")
    function = function.lower()
    function = function.strip()
    if function == "encode" or function == "decode":
      makes_sense = "y"
    else:
      print("")
      print("Sorry, that doesn't make sense.")

  print("")

  print("Special characters except (!), (?), (.), (:), (,) and (') are not supported.")
  text = input("Enter text to be " + function + "d: ")

  print("")

  print("Output:")
  print(convert(text))

  print("")

  makes_sense = "n"
  while makes_sense == "n":
    quit_wish = input("Do you want to continue? (Y/N): ").lower()
    if quit_wish == "y" or quit_wish == "n":
      makes_sense = "y"
    else:
      print("")
      print("Sorry, that doesn't make sense.")

print("")

end_stop = input("Press enter to quit.")
