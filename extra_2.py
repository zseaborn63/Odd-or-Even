print("Welcome to the Number Program!")
print("We are going to play a little different today.\n"
"I'm going to ask for two numbers.\n"
"The first, that is your number."
"The second, a 'checker', to see if your number is divisible by the 'checker'\n"
"Let's Play!\n")
num = int(input("What is your number!?\n"))
check = int(input("What is your chekcer!?\n"))
if num % check == 0:
    print("{} is a multiple of {}!".format(num, check))
else:
    print("I'm sorry, those two are not divisible evenly.")
