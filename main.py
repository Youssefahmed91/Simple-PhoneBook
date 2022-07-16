print("-----------------PhoneBook------------------")
print("0.QUIT")
print("1.ADD PHONE NUMBER TO THE PHONEBOOK")
print("2.SEARCH PHONE NUMBER IN THE PHONEBOOK")

d1={}
while True:
    n=int(input("Enter Number[0/1/2]:-"))
    if n == 1:
        name=input("enter name:-")
        phone=int(input("Enter Phone Number:-"))
        d1[name]=phone
    elif n==2:
        name1=input("enter name to search for phone number in the phone book")
        print("phone number of", name1 ,"is",d1[name1])
    elif n==0:
        break