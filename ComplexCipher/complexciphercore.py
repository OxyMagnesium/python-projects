#Core function for ComplexCipher.
def convert(text,type): #Main function.
  import random
  dictionary = ['0', '!', 'a', 'b', '1', 'c', 'd', '2', 'e', 'f', ',', 'g', 'h', '3', 'i', 'j','.', 'k', 'l', '4', 'm', ' ', 'n', '5', 'o', 'p', ':', 'q', 'r', '6', 's', 't', '\'', 'u', 'v', '7', 'w', 'x', '8', 'y', 'z', '?', '9']

  text = text.strip() #Setting up requirements for the algorithm.
  offset_included = 0

  if type == "encode" or type == "e": #Checking whether to encode or decode. If encoding, a random offset is added to the front of the string and used to offset the multiplier, increasing scrambling.
    random.seed()
    offset = random.randint(1,9999)
    offset_l = len(str(offset))

    mult = 1 * offset
    output = "%s%s" % (str(offset_l),str(offset))

  elif type == "decode" or type == "d": #If decoding, the initial offset is retrieved from the front of the string and that character is skipped by the algorithm.
    offset_l = int(text[0])
    offset = int(text[1:(offset_l + 1)])
    offset_included = offset_l + 1

    mult = -1 * offset
    output = ""

#Algorithm start

  for letter in range(offset_included,len(text)):
    input = text[letter].lower() #Taking the first character.

    if input == "`": #"`" is converted back into a space.
      input = " "

    if input not in dictionary: #Checking if the user entered an unsupported character.
      return "Sorry, \"%s\" is not supported." % (input)

    key = (dictionary.index(input) + mult) #Converts the input character into its index in the dictionary, and then adds the multiplier to it to convert it to something else.
    key %= 42 #Ensuring that the index is in the range of the dictionary.

    output += dictionary[key] #Converting the new index to a character and adding it to the output string.
    print("%s -> %s (%s)" % (input,dictionary[key],key))

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
