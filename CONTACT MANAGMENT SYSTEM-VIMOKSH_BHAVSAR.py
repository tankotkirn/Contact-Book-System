print("       A  H  M  E  D  A  B  A  D     ")
print("=====================================")
print("            CONTACT BOOK             ")
print("               SYSYEM                ")
print("=====================================")
print("     U  N  I  V  E  R  S  I  T  Y    ")
def iniCntSys():
    cols,rows=5,int(input("Please enter initial number of contacts: "))
    CntBook=[]
    print(CntBook)
    for i in range(rows):
        print("\nEnter contact details in the following order (ONLY),:")
        print("NOTE: * indicates mandatory fields")
        print("----------------------------------------------------------------------")
        tp = []
        for j in range(cols):
            if j==0:
                tp.append(str(input("Enter name*: ")))
                if tp[j] == '' or tp[j] == ' ':
                    print("Name is a mandatory field. Process exiting due to blank field...")
                    exit()
            if j==1:
                tp.append(int(input("Enter number*: ")))
            if j==2:
                tp.append(str(input("Enter e-mail address: ")))
                if tp[j] == '' or tp[j] == ' ':
                    tp[j]=None
            if j==3:
                tp.append(str(input("Enter date of birth(dd/mm/yy): ")))
                if tp[j] == '' or tp[j] == ' ':
                    tp[j]=None
            if j==4:
                tp.append(str(input("Enter category(Family/Friends/Work/Others): ")))
                if tp[j] == '' or tp[j] == ' ':
                    tp[j]=None
        CntBook.append(tp)
    print(CntBook)
    return CntBook
def menu():
    print("-----------------------------------------------------------------")
    print("\nContact Book")
    print("-----------------------------------------------------------------")
    print("\nYou can operate the following operations in this Contact Book\n")
    print("1. Add a new contact")
    print("2. Delete contact")
    print("3. Delete all contacts")
    print("4. Search contact")
    print("5. Display all contacts")
    print("6. Quit contact book")
    choice=int(input("Please enter choice of operation: "))
    return choice
def addCntct(Cntct):
    addCntct=[]
    for i in range(len(Cntct[0])):
        if i==0:
            addCntct.append(str(input("Enter name: ")))
        if i==1:
            addCntct.append(int(input("Enter number: ")))
        if i==2:
            addCntct.append(str(input("Enter e-mail address: ")))
        if i==3:
            addCntct.append(str(input("Enter date of birth(dd/mm/yy): ")))
        if i==4:
            addCntct.append(str(input("Enter category(Family/Friends/Work/Others): ")))
    Cntct.append(addCntct)
    return Cntct
def rmvExst(Cntct):
    qry=str(input("Please enter the name of the contact you wish to remove: "))
    tp=0
    for i in range(len(Cntct)):
        if qry==Cntct[i][0]:
            tp+=1
            print(Cntct.pop(i))
            print("Removed successfully")
            return Cntct
    if tp==0:
        print("Sorry, you have entered invalid query.\
Please enter correct one.")
        return Cntct
def delAll(Cntct):
    return Cntct.clear()
def searchExst(Cntct):
    choice=int(input("Enter search criteria\n\
    \n1. Name\n2. Number\n3. Email-id\n4. DOB\n5. Category(Family/Friends/Work/Others)\
    \nPlease enter: "))
    tp=[]
    check = -1
    if choice==1:
        qry=str(input("Please enter the name of the contact to search: "))
        for i in range(len(Cntct)):
            if qry==Cntct[i][0]:
                check=i
                tp.append(Cntct[i])
    elif choice==2:
        qry=int(input("Please enter the number of the contact to search: "))
        for i in range(len(Cntct)):
            if qry==Cntct[i][1]:
                check=i
                tp.append(Cntct[i])
    elif choice==3:
        qry=str(input("Please enter the e-mail ID\
        of the contact to search: "))
        for i in range(len(Cntct)):
            if qry==Cntct[i][2]:
                check=i
                tp.append(Cntct[i])
    elif choice==4:
        qry=str(input("Please enter the DOB (in dd/mm/yyyy format ONLY)\
        of the contact to search: "))
        for i in range(len(Cntct)):
            if qry==Cntct[i][3]:
                check=i
                tp.append(Cntct[i])
    elif choice==5:
        qry=str(input("Please enter the category of the contact to search: "))
        for i in range(len(Cntct)):
            if qry==Cntct[i][4]:
                check=i
                tp.append(Cntct[i])
    else:
        print("Invalid search criteria")
        return -1
    if check==-1:
        return -1
    else:
        dsplyAll(tp)
        return check
def dsplyAll(Cntct):
    if not Cntct:
        print("List is empty: []")
    else:
        for i in range(len(Cntct)):
            print(Cntct[i])
def thks():
    print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
    print("Thank you for using Contact Book System,\
          \nYours Sincerly,\nAU2040003-VIMOKSH BHAVSAR, AU2040031-AVINASH RAVAL.")
    print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
ch=1
Cntct=iniCntSys()
while ch in (1,2,3,4,5):
    ch=menu()
    if ch==1:
        Cntct=addCntct(Cntct)
    elif ch==2:
        Cntct=rmvExst(Cntct)
    elif ch==3:
        Cntct=delAll(Cntct)
    elif ch==4:
        Cntct=searchExst(Cntct)
        if ch==-1:
            print("The contact does not exist. Please check and try again")
    elif ch==5:
        dsplyAll(Cntct)
    else:
        thks()
            
    
        

    
        
        
                
        
    
            








