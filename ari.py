from sys import argv               #importing argv module from sys library.
script,filename=argv               #unpacking command-line arguments into seperate variables.
                        
def wordcount():                #function to count number of words.                       
    global File                 #Global keyword makes the variable available outside the function.
    File=open(filename)
    global content
    content=File.read()
    word_list=content.split()
    global word_count
    word_count=0
    for word in word_list:
        word_count+=1
    print(f"Number of words in {filename} is :",word_count)        #accessing the filename using string formatting. 



def linecount():       #Function to count number of sentences.
    File.seek(0)       #To shift the file pointer position to the beginning.
    # line_list=File.readlines()
    # line_count=0
    # for line in line_list:
    #     line_count+=1
    # print(f"Number of lines in {filename} is :",line_count)
    line_list=list(content)
    global line_count
    line_count=0
    for i in line_list:
        if(i=="." or i=="!" or i=="?"):
            line_count+=1
    print(f"Number of lines in {filename} is :",line_count)





def charactercount():                   #Function to count number of characters.
    character_list=list(content)
    global character_count
    character_count=len(character_list)
    print(f"Number of characters in {filename} is :",character_count)


def ari():      #function to calculate automated readability index.
    Automated_Readability_Index = 4.71 * (character_count/word_count) + 0.5 * (word_count/line_count) - 21.43
    print("ARI = ",Automated_Readability_Index)






    if(1 <= Automated_Readability_Index < 2 ):
        print("Will be suitable for age group 5-6 (KINDER GARDEN STUDENTS)")

    elif(2 <= Automated_Readability_Index < 3 ):
        print("Will be suitable for age group 6-7 (FIRST STANDARD STUDENTS)")

    elif(3 <= Automated_Readability_Index < 4 ):
        print("Will be suitable for age group 7-8 (SECOND STANDARD STUDENTS)")

    elif(4 <= Automated_Readability_Index < 5 ):
        print("Will be suitable for age group 8-9 (THIRD STANDARD STUDENTS)")

    elif(5 <= Automated_Readability_Index < 6 ):
        print("Will be suitable for age group 9-10 (FOURTH STANDARD STUDENTS)")

    elif(6 <= Automated_Readability_Index < 7 ):
        print("Will be suitable for age group 10-11 (FIFTH STANDARD STUDENTS)")

    elif(7 <= Automated_Readability_Index < 8 ):
        print("Will be suitable for age group 11-12 (SIXTH STANDARD STUDENTS)")
    
    elif(8 <= Automated_Readability_Index < 9 ):
        print("Will be suitable for age group 12-13 (SEVENTH STANDARD STUDENTS)")
    
    elif(9 <= Automated_Readability_Index < 10 ):
        print("Will be suitable for age group 13-14 (EIGHTH STANDARD STUDENTS)")
    
    elif(10 <= Automated_Readability_Index < 11 ):
        print("Will be suitable for age group 14-15 (NINETH STANDARD STUDENTS)")
    
    elif(11 <= Automated_Readability_Index < 12 ):
        print("Will be suitable for age group 15-16 (TENTH STANDARD STUDENTS)")
    
    elif(12 <= Automated_Readability_Index < 13 ):
        print("Will be suitable for age group 16-17 (ELEVENTH STANDARD STUDENTS)")
    
    elif(13 <= Automated_Readability_Index < 14 ):
        print("Will be suitable for age group 17-18 (TWELFTH STANDARD STUDENTS)")
    
    elif(14 <= Automated_Readability_Index < 15 ):
        print("Will be suitable for age group 18-22 (FOURTH STANDARD STUDENTS)")
    
    else:
        print("This book is hard to make out.")

    
    
if __name__ == '__main__':
    wordcount()
    linecount()
    charactercount()
    ari()