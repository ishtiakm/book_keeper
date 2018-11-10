def inpmode():
    print("Welcome")
    print("Enter 1 for searching existing entry")
    print("Enter 2 for entering new entry")
    print("Enter 3 for displaying all entries")
    while True:
      try:
        mode=int(raw_input())
        if abs(mode)>3:
            print("Wrong input")
            print("Try again")
            print("Press 1,2 or 3")
            continue
        return mode
        break
      except:
        print("Wrong input")
        print("Try again")
        print("Press 1,2 or 3")

def inpentry():
    temp=[""]*6
    temp[0]=raw_input("First Name: ")
    temp[1]=raw_input("Last Name: ")
    temp[2]=raw_input("Catagory (Friend/Family,Others): ")
    temp[3]=raw_input("Mail (Type 'None' if not known): ")
    temp[4]=raw_input("Phone Number(Type 'None' if not known): ")
    temp[5]=raw_input("Lives in: ")
    return temp
def takecatagory():
    while True:
        print("On which basis you want to search:")
        print("For first name type 0")
        print("For last name type 1")
        print("For mail id type 2")
        print("For mobile number type 3")
        a=(raw_input())
        if a in '0123':
            if int (a)< 2:
                return a
            else:
                return int(a)+1
            break
        else:
            print("Wrong input")
            print("Type 0,1,2 or 3")



from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
def choice(x):

    mydic={"0":"First name","1":"Last name","3":"Mail Id","4":"Phone number"}

    catagory=takecatagory()
    print("Type known %s"%(mydic[str(catagory)]))
    queryname=raw_input().lower()
    t=int(catagory)
    temp=[]
    for i in range(len(x)):
        temp.append(similar(queryname,(x[i][t]).lower()))
    a=temp.index(max(temp))
    temp1=x[a]
    if max(temp)==1:
        print("The person you are looking for is: \n\n\n")
    else:
        print("Are you looking for: \n\n\n")
    print(" ".join(temp1))
