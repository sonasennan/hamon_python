def panagram():
    a=s.lower()
    b=set(a)
    c=list(b)
    c.sort()
    d=[]
    for i in range(97,123):
        d.append(chr(i))
    if c == d:
        print("This is a panagram")
    
    else:
        print("Not a panagram")
   



            
if __name__ == '__main__':
    s=input("enter the  string")
    panagram()