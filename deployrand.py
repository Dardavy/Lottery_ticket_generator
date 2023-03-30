# This programm is to write a python program that Generate 'Lottery Number'
# This will be from a range of 1 - 50
# Six numbers will be radomly chosen from the available range number 1 - 50 x 6
# and the winning number wil be six number chosen from the range number

import random
#Initialise an emptylist that will be use to store the 6 lucky number!
lottery_numbers = []

for i in range (0, 6):
  number = random.randint(1, 50)
  #check if this number has already been picked and ...
  while number in lottery_numbers:
    #... if it has, pick a new number instead
    number = random.randint(1, 50)

  #now that we have a unique number, let's append it to our list.
  lottery_numbers.append(number)

#sort the list in ascending order
lottery_numbers.sort()

user_numbers = []
for i in range(0, 6):
  number = int(input("please enter a number between 1 and 50 "))
  while (number in user_numbers or number<1 or number>50):
    print("Invalid number, please try again")
    number = int(input("please enter annumber between 1 and 50 "))

  user_numbers.append(number)

#display the list on screen
print(">>> Today's lottery numbers are: ")
print(lottery_numbers)

print("Your selection:")
print(user_numbers)

counter = 0
for number in user_numbers:
  if number in lottery_numbers:
    counter +=1

print(" You guessed " + str(counter)+ " number(s) correctly.")





