number=int(input("Guess a number between 1-10: "))

while number != 10:
    print("Wrong! Guess Again!")
    number=int(input("Enter a new number: "))
if number == 10:
	print("Congratulations! Good Guess! You Have Completed The Program!")

