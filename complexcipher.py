import random

dictionary = ['0', '!', 'a', 'b', '1', 'c', 'd', '2', 'e', 'f', ',', 'g', 'h', '3', 'i', 'j','.', 'k', 'l', '4', 'm', ' ', 'n', '5', 'o', 'p', ':', 'q', 'r', '6', 's', 't', '\'', 'u', 'v', '7', 'w', 'x', '8', 'y', 'z', '?', '9']

#Function start

def convert(text): #Main function.
  text = text.strip() #Setting up requirements for the algorithm.
  offset_included = False

  if function == "encode" or function == "e": #Checking whether to encode or decode. If encoding, a random offset is added to the front of the string and used to offset the multiplier, increasing scrambling.
    random.seed()
    offset = random.randint(1,9)

    mult = 1 * offset
    output = "%s" % offset

  elif function == "decode" or function == "d": #If decoding, the initial offset is retrieved from the front of the string and that character is skipped by the algorithm.
    offset = int(text[0])
    offset_included = True

    mult = -1 * offset
    output = ""

#Algorithm start

  for letter in range(offset_included,len(text)):
    input = text[letter].lower() #Taking the first character.

    if input == "`": #"`" is converted back into a space.
      input = " "

    if input not in dictionary: #Checking if the user entered an unsupported character.
      return "Sorry, \"" + input + "\" is not supported."

    key = (dictionary.index(input) + mult) #Converts the input character into its index in the dictionary, and then adds the multiplier to it to convert it to something else.
    key %= 42 #Ensuring that the index is in the range of the dictionary.

    output += dictionary[key] #Converting the new index to a character and adding it to the output string.
    print("%s -> %s (%s,%s)" % (input,dictionary[key],mult,key))

    offset += 1 #Increasing offset, increasing and flipping multiplier for maximum scrambling.
    if mult > 0:
      mult += offset
    elif mult < 0:
      mult -= offset
    mult *= -1

#Algorithm end

  if output[(len(output) - 1)] == " ": #If the last character is a space, it is replaced with "`" so it isn't lost.
    output = output[0:(len(output) - 1)] + "`"

  print("")
  return output

#Function end
#Program start

print("")

print("Welcome to ComplexCipher v1.3.3 by Om Gupta!")

quit_wish = "y"

while quit_wish == "y":
  while True:
    function = (input("Enter function to be performed. (Encode/Decode): ").lower()).strip()
    if function == "encode" or function == "decode" or function == "e" or function == "d":
      break
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

  while True:
    quit_wish = input("Do you want to continue? (Y/N): ").lower()
    if quit_wish == "y" or quit_wish == "n":
      break
    else:
      print("")
      print("Sorry, that doesn't make sense.")

print("")

end_stop = input("Press enter to quit.")

#Program end
