import random

def dardavy_lottery_gen():


# generates user data with input
    user_name = input("Enter your name's: ")
    user_number = int(input("Enter your Lucky number: "))
    rand_number = random.randint(0, 50)
    winning_number = 30
    
    print(rand_number)
    for i in range(0,1):
        if user_number == rand_number:
            print(">>> Congratulation", user_name,"You're luoky winner,your", 30 ,"with number 30 ." )
        elif user_number >50:
            print('Invalid input your number','input', "must not be greaterthan 50") 
        else:
            print(">>>Sorry!", user_name," Wish you good luck next try.")















dardavy_lottery_gen()