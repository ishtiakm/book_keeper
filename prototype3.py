import time
from funcs import inpmode,inpentry,similar,choice


filename="info.txt"
mode=inpmode()
if mode==2:
    n=int(raw_input("How many new person you want to include in the database:\n"))
    f=open(filename,"a+")
    for i in range(n):
        print("Give the following information of the person you want to enter")
        temp=inpentry()
        temp2=" ".join(j for j in temp)+"\n"
        f.write(temp2)


elif mode==1:
    f=open(filename,"r")
    people=[]
    person={}
    for line in f:
        person=line.split(" ")
        people.append(person)



    '''search=raw_input("Enter First Name: ")
    result=(filter(lambda x: x[0] == search, people))
    print(" ".join(i for i in result[0]))'''
    choice(people)


else:
    f=open(filename,"r")
    people=[]
    person={}
    for line in f:
        person=line.split(" ")
        people.append(person)
    for i in people:
        print(" ".join(i))
