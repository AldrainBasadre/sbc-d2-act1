#str method

word = input("Thy Enter Thus Word:")
#summer bootcamp
#01234567891011121314
loot = word.replace("b","L")
alpha = word.replace(" ", "")
print(f"{word[0:7].capitalize() + word[7:].capitalize()}\n{word[0:14].capitalize() + word[-1].capitalize()}")
print(loot[7:11])
print(word[11:14] + word[4].upper())
print(word[-3].upper() + word[5].upper())
print(alpha.isalpha())


#history log



# indexing
# text = "Hello World"
# #       012345678910
# #       -11-10-9-8-7-6-5-4-3-2-1
# word = input("enter secret key: ")
# print (text[6],text[-5],word + " " + text)
# # kuhaon ang length
# print (len(text),len(word))

# print(word[len(word)-1])

# #slicing

# text = "Hello World"

# print(text[0:])
# print(text[0:5])
# print(text[0:-6])
# print(text[-5:])
# print(text[-8:-6])
# #diff of , and +
# print(text[0:2] + text[-5:-3])
# print(text[0:2] + text[-5:-3])
# #oldf and f string 
# print("{0}{1}".format(text[0:2],text[6:8]))
# print(f"{text[0:2]}{text[6:8]}")

# #str method

# word = "HeLLo"



# print(f"{word.upper()}\n{word.lower()}\n{word.swapcase()}")

# print(word.capitalize())
# print(word.title())
# print(word.replace("H","X"))
# print(word.find("e"))
# print(word.isalpha())
# print(word.isnumeric())
# print(word.isalnum())