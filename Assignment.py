from datetime import date
import datetime

# All User Login
def userlogin():
    userid = input("Enter User ID: ")
    userpass = input("Enter Password: ")
    with open("logincredentials.txt", "r") as file:
        accvalid = "notvalid"
        for lines in file:
            data = lines.strip().split(":")
            if data[0] == userid and data[1] == userpass:
                accvalid = data
                break
        if accvalid == "notvalid":
            print("Incorrect Password or Username!")
        else:
            print("Account Login Successful!")
        return accvalid


# Check All Login Details
def checklogin():
    with open("logincredentials.txt", "r") as file:
        print("\n\t\t\t\t\tAll User Details")
        print("-"*100)  
        print("User ID".ljust(20)+"User Password".ljust(14)+"User Name".center(40)+"Account Type")
        print("-"*100+"\n")
        for lines in file:
            data = lines.strip().split(":")    
            print(data[0].ljust(20)+data[1].ljust(14)+data[2].center(35)+"\t\t"+data[3])  
    print("\n"+"-"*100+"\n")       


# Auto Generate ID 
def autogen(value):
    with open("allid.txt","r") as file:
        record = file.readline()
        data = record.strip().split(":")
    if value == "admin":
        prefix = "ADMIN"
        oldid = data[0][5:]
    elif value == "customer":
        prefix = "CUS"
        oldid = data[1][3:]
    elif value == "deposit":
        prefix = "DEP"
        oldid = data[2][3:]
    elif value == "withdrawal":
        prefix = "WTD"
        oldid = data[3][3:]    
    nextid = int(oldid) + 1
    if len(str(nextid)) == 1:
        newid = "0000" + str(nextid)
    elif (len(str(nextid))) == 2:
        newid = "000" + str(nextid)
    elif (len(str(nextid)) == 3):
        newid = "00" + str(nextid)
    elif (len(str(nextid))) == 4:
        newid = "0" + str(nextid)
    elif (len(str(nextid))) == 5:
        newid = str(nextid)
    newid = prefix + newid
    if value == "admin":
        data[0] = newid
    elif value == "customer":
        data[1] = newid
    elif value == "deposit":
        data[2] = newid
    elif value == "withdrawals":
        data[3] = newid
    record = ":".join(data)
    with open("allid.txt", "w") as file2:
        file2.write(record+"\n")
    return newid


# New Admin
def newstaff():
    print("\t\tCreate New Admin Staff\n")
    userid = autogen("admin")
    userpass = str(userid)+"def" 
    print("User ID: ", userid)
    print("Default Password: ", userpass)
    username = input("Please Enter your Name: ")
    acctype = "2"
    with open("logincredentials.txt","a") as file:
        save = userid+":"+userpass+":"+username+":"+acctype+"\n"
        file.write(save)


# New Customer
def newcustomer():
    print("\tCreate New Customer's Account")
    userid = autogen("customer")
    userpass = str(userid)+"def" 
    name_valid = False
    while name_valid == False:
        username = input("Please Enter your Name: ")
        if not username.isalpha():
            print("Only characters are allowed")
            name_valid == False
        else:
            name_valid == True
            break
    acctype = "3"
    address = input("Please Enter Your Current Address: ")
    email = input("Please Enter Your Email: ")

    contact_valid = False
    while contact_valid == False:
        try:
            contact = int(input("Enter contact number: "))
            contact_valid == True
            break
        except ValueError:
            print("Only numbers are allowed!")
            contact_valid == False

    account_valid = False
    while account_valid == False:
        account = input("Enter Account Type (Savings or Current): ")
        if account== "Savings":
            opening_valid = False
            while opening_valid == False:
                try:
                    balance = int(input("Enter an opening balance: RM"))
                    if balance >= 100:
                        opening_valid == True
                        break
                    else:
                        print("Minimum opening balance for Savings Account: RM100")
                        opening_valid == False
                except ValueError:
                        print("Only integers are allowed!")
            break

        elif account == "Current":
            opening_valid = False
            while opening_valid == False:
                try:
                    balance = int(input("Enter an opening balance: RM"))
                    if balance >= 500:
                        opening_valid == True
                        break
                    else:
                        print("Minimum opening balance for Savings Account: RM100")
                        opening_valid == False
                except ValueError:
                        print("Only integers are allowed!")
            break
        else:
            print("Invalid Input!")
            account_valid = False

    with open("logincredentials.txt","a") as file:
        save = userid+":"+userpass+":"+username+":"+acctype+"\n"
        file.write(save)
    with open("customeracc.txt","a") as file2:
        data = userid+":"+username+":"+address+":"+str(contact)+":"+email+":"+account+":"+str(balance)+"\n"
        file2.write(data)

    print("\n-------------Account Successfully Created--------------\n")
    print("\tUser ID: ", userid)
    print("\tDefault Password: ", userpass)
    print("\tUsername: ",username)
    print("\tContact Number: ",contact)
    print("\tEmail: ",email)
    print("\tAddress: ",address)
    print("\tAccount Type: ",account)
    print("\tOpening Balance: RM",balance)
    print("\n")


# Display Customer Details (Admin)
def checkcus():
    print("\tAll AHD Customer's Details")
    with open("customeracc.txt","r") as file:
        print("\n"+"-"*130)
        print("Customer ID".ljust(15)+"Username".ljust(15)+"Current Address".ljust(15)+"Contact Number".center(30)+"Email".ljust(15)+"Account Type".ljust(15)+"Account Balance(RM)\n")
        for lines in file:
            data = lines.strip().split(":")
            print(data[0].ljust(15)+data[1].ljust(15)+data[2].ljust(15)+data[3].center(30)+data[4].ljust(15)+data[5].ljust(15)+data[6])
        print("\n"+"-"*130)


# Display Specific Customer Details (Admin)
def specus():
    print("\tEnter User Login Credentials")
    cusinfo = userlogin()
    if cusinfo != "notvalid":
        record = []
        with open ("customeracc.txt","r") as file:
            for lines in file:
                data = lines.strip().split(":")
                if cusinfo[0] == data[0]:
                    record.append(data)
        print("\n"+"-"*130)
        print("Customer ID".ljust(15)+"Username".ljust(15)+"Current Address".ljust(15)+"Contact Number".center(30)+"Email".ljust(15)+"Account Type".ljust(15)+"Account Balance(RM)\n")
        print(record[0][0].ljust(15)+record[0][1].ljust(15)+record[0][2].ljust(15)+record[0][3].center(30)+record[0][4].ljust(15)+record[0][5].ljust(15)+record[0][6]+"\n")
        print("-"*130)
    else:
        print("Please Try Again!")

#Admin Update User Contact
def adminup_cont(cusid):
    print("\tUpdate Customer's Contact Number")
    record = []
    with open("customeracc.txt","r") as file:
        for lines in file:
            data = lines.strip().split(":")
            record.append(data)
    newcontact = int(input("Enter New Contact Number: "))
    flag = -1
    numbersaved = len(record)
    for count in range(0,numbersaved):
        if cusid[0] == record[count][0]:
            flag = count
            break
    if flag >= 0:
        record[flag][3] = str(newcontact)
    with open("customeracc.txt","w") as file:
        numbersaved = len(record)
        for count in range(0,numbersaved):
            lines = ":".join(record[count])+"\n"
            file.write(lines)
    print("Contact Number Successfully Updated!\n")


#Admin Update User Email
def adminup_email(cusid):
    print("\tUpdate Customer's Email Address")
    record = []
    with open("customeracc.txt","r") as file:
        for lines in file:
            data = lines.strip().split(":")
            record.append(data)
    newemail = input("Enter New Email: ")
    flag = -1
    numberofsaved = len(record)
    for count in range(0,numberofsaved):
        if cusid[0] == record[count][0]:
            flag = count
    if flag >= 0:
        record[flag][4] = newemail
    with open("customeracc.txt","w") as file:
        numberofsaved = len(record)
        for count in range(0,numberofsaved):
            lines = ":".join(record[count])+"\n"
            file.write(lines)
    print("Email Successfully Updated!\n")


#Admin Update user Address
def adminup_add(cusid):
    print("\tUpdate Customer's Address")
    record = []
    with open("customeracc.txt","r") as file:
        for lines in file:
            data = lines.strip().split(":")
            record.append(data)
    print("Current Address: ",data[2])
    newadd = input("Enter New Address:")
    flag = -1
    numbersaved = len(record)
    for count in range(0,numbersaved):
        if cusid[0] == record[count][0]:
            flag = count
    if flag >= 0:
        record[flag][2] = newadd
    with open("customeracc.txt","w") as file:
        lines = ":".join(record[count])
        file.write(lines) 
        print("Address Successfully Updated!")


#Admin Update Menu
def updatedetails():
    print("\n\t     Update Customer's Details Page")
    print("\n\tEnter Customer's Account Login Credentials")
    cusinfo = userlogin()
    if cusinfo != "notvalid":
        print("---------------------------------------")
        print("\n\t1. Update Contact Number")
        print("\t2. Update Email")
        print("\t3. Update Current Address")
        num = int(input("Select an Option: "))
        print("\n--------------------------------------")
        if num == 1:
            adminup_cont(cusinfo)
        elif num == 2:
            adminup_email(cusinfo)
        elif num == 3:
            adminup_add(cusinfo)
        else:
            pass
    else:
        print("Please Try Again")


#Admin Generate Customer Statement
def admgenstat():
    print("\n\t     Generate Customer's Statement of Account Report")
    print("\n\tEnter Customer's Account Login Credentials")
    cusid = userlogin()
    if cusid != "notvalid":
        record = []
        datevalid = False
        while datevalid == False:
            try:        
                startdate  = input("Enter Start Date (YY-MM-DD): ")
                enddate = input("Enter End Date (YY-MM-DD): ")  
                start = datetime.datetime.strptime(startdate,"%Y-%m-%d")
                end = datetime.datetime.strptime(enddate,"%Y-%m-%d")
                datevalid = True
                break
            except ValueError:
                print("Incorrect Date Format!")
                datevalid = False
        with open("transaction.txt","r") as file:
            for lines in file:
                data = lines.strip().split(":")
                if cusid[0] == data[1]:
                    record.append(data)
        strsave = datetime.datetime.strptime(data[4],"%Y-%m-%d")
        flag = -1
        numbersaved = len(record)
        for count in range (0,numbersaved):
            if cusid[0] == record[count][1]:
                flag = count
                break
        if flag >= 0:
            if strsave >= start and strsave<= end:   
                print("\n"+"-"*100+"\n\t\t\tCustomer’s Statement of Account Report\n")
                print("\t\tCustomer ID:",cusid[0]+"\tName:",cusid[2]+"\tAccount Type:",data[5]+"\n")
                print("Transaction ID".ljust(20)+"Account ID".ljust(20)+"Transaction Amount".ljust(20)+"Current Amount".ljust(20)+"Date".ljust(20))
                for count in range(0,numbersaved):      
                    print(record[count][0].ljust(20)+record[count][1].ljust(20)+record[count][2].ljust(20)+record[count][3].ljust(20)+record[count][4].ljust(20))   
                print("\n")
    else:
        print("Please Try Again")


#Customer Check Own Details
def cusdetails(cusinfo):
    record = []
    with open ("customeracc.txt","r") as file:
        for lines in file:
            data = lines.strip().split(":")
            if cusinfo[0] == data[1]:
                record.append(data)
    print("\n"+"-"*130)
    print("Customer ID".ljust(15)+"Username".ljust(15)+"Current Address".ljust(15)+"Contact Number".center(30)+"Email".ljust(15)+"Account Type".ljust(15)+"Account Balance(RM)\n")
    print(data[0].ljust(15)+data[1].ljust(15)+data[2].ljust(15)+data[3].center(30)+data[4].ljust(15)+data[5].ljust(15)+data[6]+"\n")
    print("-"*130)


# Customer Modify Password
def modifypass(logdetails):
    print("\tModify Password")
    record = []
    with open("logincredentials.txt","r") as file:
        for lines in file:
            savedinfo = lines.strip().split(":")
            record.append(savedinfo)
    passvalid = False
    while passvalid == False:
        newpass = input("Please Enter New Password: ")
        confirmpass = input("Please Confirm New Password: ")
        if newpass == confirmpass:
            flag = -1
            numberofsaved = len(record)
            for count in range(0,numberofsaved):
                if logdetails [0] == record[count][0]:
                    flag = count
                    break
            if flag >= 0:
                record[flag][1] = newpass
            with open("logincredentials.txt","w") as file:
                numberofsaved = len(record)
                for count in range (0,numberofsaved):
                    lines = ":".join(record[count])+"\n"
                    file.write(lines)
            print("Your Password has been Updated !\n") 
            print("Account ID:",logdetails[0])
            print("Password:",newpass)    
            passvalid == True
            break
        else:
            print("Password does not match! Please Try Again") 
            passvalid == False 
    

# Deposit
def deposit(cusinfo):
    transid = autogen("deposit")
    today = date.today()
    stringdate = date.isoformat(today)
    record = []
    with open("customeracc.txt","r") as file:
        for lines in file:
            data = lines.strip().split(":")
            record.append(data)
    flag = -1
    numbersaved = len(record)
    for count in range(0,numbersaved):
        if cusinfo[0] == record[count][0]:
            flag = count
            break
    amountvalid = False
    while amountvalid == False:
        if flag >= 0 and record[flag][5] == "Savings":
            print("Account Type: ",record[flag][5])
            print("Current Amount in Account: RM",record[flag][6])
            try:
                depositamt = int(input("Enter Deposit Amount: RM"))
            except ValueError:
                print("Only Integers are Allowed!")
            newamount = depositamt + (int(record[flag][6]))
            print("Updated Current Amount in Account: RM",newamount)
            if newamount < 100:
                print("Minimum Balance for Savings Account is RM100 !")
                amountvalid == False
            else:
                record[flag][6] = str(newamount)
                with open("customeracc.txt","w") as file:
                    numbersaved = len(record)
                    for count in range(0,numbersaved):
                        lines = ":".join(record[count])+"\n"
                        file.write(lines)
                amountvalid = True
        elif flag >= 0 and record[flag][5] == "Current":
            print("Account Type: ",record[flag][5])
            print("Current Amount in Account: RM",record[flag][6])
            try:
                depositamt = int(input("Enter Deposit Amount: RM"))
            except ValueError:
                print("Only Integers are Allowed!")
            newamount = depositamt + (int(record[flag][6]))
            print("Updated Current Amount in Account: RM",newamount)
            if newamount < 500:
                print("Minimum Balance for Current Account is RM500 !")
                amountvalid == False
            else:
                record[flag][6] = str(newamount)
                with open("customeracc.txt","w") as file:
                    numbersaved = len(record)
                    for count in range(0,numbersaved):
                        lines = ":".join(record[count])+"\n"
                        file.write(lines)
                amountvalid = True
    save = transid+":"+cusinfo[0]+":"+str(depositamt)+":"+str(newamount)+":"+stringdate+":"+data[5]+"\n"
    print("Deposit Transaction Successful!\n")
    with open("transaction.txt","a") as file2:
        file2.write(save)
        

# Request Transaction    
def askdeposit(cusinfo):
    user_input = input("Do you want to perform deposit transaction? (yes/no):")
    print("")
    if user_input == "yes":
        deposit(cusinfo)
    else:
        print("Returning you back to the main menu...")
        pass
    

# Withdrawal 
def withdrawal(cusinfo):
    transid = autogen("withdrawal")
    today = date.today()
    stringdate = date.isoformat(today)
    record = []
    with open("customeracc.txt","r") as file:
        for lines in file:
            data = lines.strip().split(":")
            record.append(data)
    flag = -1
    numbersaved = len(record)
    for count in range(0,numbersaved):
        if cusinfo[0] == record[count][0]:
            flag = count
            break
    amountvalid = False
    while amountvalid == False:
        if flag >= 0 and record[flag][5] == "Savings":
            print("Account Type: ",record[flag][5])
            print("Current Amount in Account:",record[flag][6])
            try:
                withamt = int(input("Enter Withdrawal Amount: RM"))
            except ValueError:
                print("Only Integers are Allowed!")
            newamount =  (int(record[flag][6])) - withamt
            print("Updated Current Amount in Account: RM",newamount)
            if newamount < 100:
                print("Minimum Balance for Savings Account is RM100 !")
                amountvalid == False
            else:
                record[flag][6] = str(newamount)
                with open("customeracc.txt","w") as file:
                    numbersaved = len(record)
                    for count in range(0,numbersaved):
                        lines = ":".join(record[count])+"\n"
                        file.write(lines)
                amountvalid = True
        elif flag >= 0 and record[flag][5] == "Current":
            print("Account Type: ",record[flag][5])
            print("Current Amount in Account:",record[flag][6])
            try:
                withamt = int(input("Enter Withdrawal Amount: RM"))
            except ValueError:
                print("Only Integers are Allowed!")
            newamount = (int(record[flag][6])) - withamt
            print("Updated Current Amount in Account: RM",newamount)
            if newamount < 500:
                print("Minimum Balance for Current Account is RM500 !")
                amountvalid == False
            else:
                record[flag][6] = str(newamount)
                with open("customeracc.txt","w") as file:
                    numbersaved = len(record)
                    for count in range(0,numbersaved):
                        lines = ":".join(record[count])+"\n"
                        file.write(lines)
                amountvalid = True
    save = transid+":"+cusinfo[0]+":"+str(withamt)+":"+str(newamount)+":"+stringdate+":"+data[5]+"\n"
    print("Deposit Transaction Successful!\n")
    with open("transaction.txt","a") as file2:
        file2.write(save)
        

# Request Withdrawal
def askwithdrawal(cusinfo):
    userinput = input("Do you want to perform withdrawal transaction? (yes/no):")
    print("")
    if userinput == "yes":
        withdrawal(cusinfo)
    else:
        print("Returning you back to the main menu...")
        pass
        

#Customer Generate Statement
def genstate(logininfo):
    record = []
    datevalid = False
    while datevalid == False:
        try:        
            startdate  = input("Enter Start Date (YY-MM-DD): ")
            enddate = input("Enter End Date (YY-MM-DD): ")  
            start = datetime.datetime.strptime(startdate,"%Y-%m-%d")
            end = datetime.datetime.strptime(enddate,"%Y-%m-%d")
            datevalid = True
            break
        except ValueError:
            print("Incorrect Date Format!")
    with open("transaction.txt","r") as file:
        for lines in file:
            data = lines.strip().split(":")
            if logininfo[0] == data[1]:
                record.append(data)
    strsave = datetime.datetime.strptime(data[4],"%Y-%m-%d")
    numbersaved = len(record)
    for count in range (0,numbersaved):
        if strsave >= start and strsave<= end:  
            if logininfo[0] == record[count][1]: 
                print("\n"+"-"*100+"\n\t\t\tCustomer’s Statement of Account Report")
                print("\t\tCustomer ID:",logininfo[0]+"\tName:",logininfo[2]+"\tAccount Type:",data[5]+"\n")
                print("Transaction ID".ljust(20)+"Account ID".ljust(20)+"Transaction Amount".ljust(20)+"Current Amount".ljust(20)+"Date".ljust(20)+"\n")
                for count in range(0,numbersaved):      
                    print(record[count][0].ljust(20)+record[count][1].ljust(20)+record[count][2].ljust(20)+record[count][3].ljust(20)+record[count][4].ljust(20))   
                print("\n"+"-"*100+"\n")
    else:
        print("\n**No Transaction Made on Requested Date Range**\n")

        
# Super User Menu
def supermenu(logininfo):
    while True:
        print("====================Super User Menu====================")
        print("\t Welcome to AHD Bank, Mr/Ms", logininfo[2]+"\n")
        print("\t1. New Admin Staff Account Registration")
        print("\t2. Check All Account Details")
        print("\t3. Logout\n")
        num = int(input("Select an option: "))
        print("=======================================================")
        if num == 1:
            newstaff()
        elif num == 2:
            checklogin()
        elif num == 3:
            break


# Admin Menu          
def adminmenu(logininfo):
    while True:
        print("======================Admin Menu=========================")
        print("\t Welcome to AHD Bank, Mr/Ms", logininfo[2]+"\n")
        print("\t1. New Customer Account Registration")
        print("\t2. Check All Customer Account Details")
        print("\t3. Check Specific Customer's Details")
        print("\t4. Update Customer Details")
        print("\t5. Generate Customer's Statement of Account Report")
        print("\t6. Logout\n")
        num = int(input("Select an option: "))
        print("=========================================================")
        if num == 1:
            newcustomer()
        elif num == 2:
            checkcus()
        elif num == 3:
            specus()
        elif num == 4:
            updatedetails()
        elif num == 5:
            admgenstat()
        elif num == 6:
            break    


#Customer Menu
def cusmenu(logininfo):
    while True:
        print("===================Customer Menu===================")
        print("\t Welcome to AHD Bank, Mr/Ms ",logininfo[2]+"\n")
        print("\t1. Check Account Details")
        print("\t2. Deposit")
        print("\t3. Withdrawal")
        print("\t4. Modify Password")
        print("\t5. Generate Statement of Account Report")
        print("\t6. Logout\n")
        num = int(input("Select an Option: "))
        print("===================================================")
        if num == 1:
            cusdetails(logininfo)
        if num == 2:
            askdeposit(logininfo)
        elif num == 3:
            askwithdrawal(logininfo)
        elif num == 4:
            modifypass(logininfo)
        elif num == 5:
            genstate(logininfo)
        elif num == 6:
            break


# Main Logic
while True:
    print("============================== AHD Bank ============================")
    userinput = input("Enter C to continue to Login Page , Q to Quit the System")
    if userinput == "C":
        print("")
        start = userlogin()
        if start[3] == "1":
            supermenu(start)
        elif start[3] == "2":
            adminmenu(start)
        elif start[3] == "3":
            cusmenu(start)
        else:
            print("Please Try Again")
    elif userinput =="Q":
        break
    else:
        print("Invalid Input")



