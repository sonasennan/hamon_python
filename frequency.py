def freq(string):
    dictionary={}                         #created empty dictionary to add each elements in the entered string as keys and its no: of occurence as values.
    for i in string:
        if(i not in dictionary.keys()):   #check whether the keys are repeated 
            key=i
            value=1
            dictionary[key]=value
        else:
            value=dictionary[key]+1
            dictionary[key]=value
    print(dictionary)
   



if __name__ == '__main__':
    string=input("enter the string")
    freq(string)














    