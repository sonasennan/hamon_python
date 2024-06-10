import random

def random_word():
    wordfile=open('hangman_words.txt','r')        #opening the text file in read mode.
    random_word=random.choice((wordfile.readlines())).strip()   #picking random word from the text file and removing the starting and trailing \n.
    return random_word    #returning the output for further use.


def print_statements():
    print("Lets play an interesting game............")
    print("I have a secret word for you.....")
    print("Can you guess the word????")
    answer=input("Y/N????")   
    if(answer.lower()=="y"):
        print("You have only 7 chances..........")
        print("Are you ready?")
        answer=input("Y/N???")
        if(answer.lower()=="y"):
            print("Lets Start")
        else:
            print("Oops..")
            exit()
    else:
        print("Oops..")
        exit()
    



def play():
    secret_word=random_word()
    # print(secret_word)
    blanks=""
    for i in range(len(secret_word)):       #printing the blank lines to be replaced.Its number is set proportional to the length of secret word.
        blanks=blanks+"-"
    print("Guess this",len(secret_word),"letter secret word :",blanks)

    
    chances=7
    choice_check=[]   #creating an empty list to add the guessed choices.
    while chances>0 and '-' in blanks:   #setting the number of chances for the user.
        choice=input("Enter your guess : ").lower()
        
        if choice in choice_check:
            print("You already quessed",{ choice },"Try a new one instead..")
            print("You have",chances,"chances left")
        else:
            choice_check.append(choice)
        
            if(len(choice)!=1 or not choice.isalpha()):    #to display a message if the entered choice is invalid.
                print("Enter a valid single alphabet.")
            else:
                match=False      #predefining the variable as False.
                for index in range(len(secret_word)):  #iterating through the length of secret word.
                    if(secret_word[index] == choice):   #checking if the guessed alphabel is present in the secret word.
                        blanks=blanks[:index] + choice + blanks[index + 1:]   #replacing the guessed alphabel in the exact index position.
                        match=True
                
            if not match:
                chances -= 1   #decrementing the number of chances if the choice is wrong.
                death(chances)   #calling the death() function.
            print(blanks)    #printing the current output.
            
            print("You have",chances,"chances left.")

    
    if '-' not in blanks:     #checks whether all the blank spaces are filled.
        print("Congratulations...! You guessed the word correctly.")    
    else:
        print("Oops..You ran out of chances.The secret word was",{ secret_word })
        
            
        
   

def death(chances):          
    deathh={                             #dictionary having key as the number of chances and the corresponding value will be its print statement.ie,the image to be printed.
    6:"|_______\n|  |\n|\n|\n|\n|\n|_",
    5:"|_______\n|  |\n|  0\n|\n|\n|\n|_",
    4:"|_______\n|  |\n|  0\n| / \n|\n|\n|_",
    3:"|_______\n|  |\n|  0\n| / \\ \n|\n|\n|_",
    2:"|_______\n|  |\n|  0\n| /|\\ \n|\n|\n|_",
    1:"|_______\n|  |\n|  0\n| /|\\ \n| /\n|\n|_",
    0:"|_______\n|  |\n|  0\n| /|\\ \n| / \\\n|\n|_"
    }         
    
    print(deathh[chances])

            

            


if __name__ == '__main__':
    print_statements()
    play()


