def palindrome(s):
    a=s.lower()
    if(a == a[::-1]):                 #Checks whether the string matches with reverse of the string
        print(a,"is Palindrome")
    else:
        print(a,"is not a palindrome")


if __name__ == '__main__':
    s=input("Enter the  string")
    palindrome(s)