print("")

print("Welcome to SuperSimpleCipher v1.0 by Om Gupta.")

print("")

dictionary = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(word):
    result = ""
    for letter in range(len(word)):
        result += str(dictionary.index(word[letter])) + " "
    print(result)

def decode(code):
    code += " "
    result = ""
    l_start = ""
    l_end = ""
    for number in range(len(code)):
        if l_start == "":
            if code[number] != " ":
                l_start = number
        elif code[number] == " ":
            l_end = number
        if l_start != "" and l_end != "":
          result += dictionary[int(code[l_start:l_end])]
          l_start = ""
          l_end = ""
    print(result)

function = input("Select function (Encode/Decode): ")

print("")

print("Only lower case alphabets and spaces are allowed.")

while True:
  if function.lower() == "encode":
    word = input("Enter text to be encoded: ")
    break
  elif function.lower() == "decode":
    code = input("Enter text to be decoded: ")
    break
  else:
    print("Sorry, that doesn't make sense. Please try again.")
    quit()

print("")

if function.lower() == "encode":
    encode(word)
elif function.lower() == "decode":
    decode(code)
else:
    print("How did you trigger this line?!")

print("")

x = input("Press any key to exit...")
