import pandas as pd 

name_lst = ["Ram", "Sam", "Prabhu", "Kavya", "Rajesh"]
acc_no_lst = [100329468858, 365672000483, 897746530868, 862046529578, 668650947593]
acc_typ_lst = ["SB","CA","CA","SB","SB"]
aadh_no_lst = [255377470982, 904858839950, 256488639957, 599036586628, 577398576383]
bal_lst = [15000, 56000, 580, 6000, 60000]

accountHolders = {
    "Name":name_lst,
    "Account_num":acc_no_lst,
    "Account_type":acc_typ_lst,
    "Aadhar_no":aadh_no_lst,
    "Balance":bal_lst
}

df = pd.DataFrame(accountHolders)
print(df)

df.to_csv("acc_holder.csv", index=False)

def display_options():
    print("\nchoose '1' to Add Account Holder")
    print("choose '2' to Delete Account of a Holder")
    print("choose '3' to Add the Credit to Account")
    print("choose '4' to Debit the amount from the Account")
    print("choose '5' to know the Account Info")
    print("choose '6' to merge csv files")
    print("choose '7' to exit")

def appendRow():
    nm = input("Enter name of account-Holder: ")
    ac_no = int(input("Enter {}'s account number: ".format(nm)))
    ac_typ = input("Enter {}'s Account type [SB/CA]: ".format(nm))
    ad_no = int(input("Enter {}'s Aadhar Number: ".format(nm)))
    bal = int(input("Enter {}'s Balance Amount: ".format(nm)))

    ndf = pd.DataFrame({
            "Name":[nm], 
            "Account_num":[ac_no], 
            "Account_type":[ac_typ], 
            "Aadhar_no":[ad_no], 
            "Balance":[bal]
        })

    ndf.to_csv("acc_holder.csv", mode='a', index=False, header=False)
    print("Record Created Successfully..")

def deleteRecord():
    nm = input("Enter name of account-Holder: ")
    ac_no = int(input("Enter {}'s Account number: ".format(nm)))
    df = pd.read_csv("acc_holder.csv")

    flag = False
    for x in range(0, len(df)):
            if df.Account_num[x] == ac_no:
                flag = True
    if flag:
        df = df[df["Account_num"]!=ac_no]
        df.to_csv("acc_holder.csv", index=False)
        print("Account with account Number: {} deleted successfully..".format(ac_no))
    else:
        print("Record not found with Ac/no {}".format(ac_no))


def credit_to_acc():
    ac_no = int(input("Enter account Number: "))
    credit = int(input("Enter the Ammount to be credited: "))
    chc = input("Credit {}RS to {} ? [y/n]: ".format(credit, ac_no))
    if chc=="y":
        df = pd.read_csv("acc_holder.csv")
        for x in range(0, len(df)):
            if df.Account_num[x] == ac_no:
                df.at[x, "Balance"] += credit
                df.to_csv("acc_holder.csv", index=False)
                print("Amount: {} Credited successfuly..".format(credit))
                return
        print("Record not found with acc/no {}".format(ac_no))
    else:
        print("Transaction is cncelled.")

def debit_from_acc():
    ac_no = int(input("Enter account number: "))
    debit = int(input("Enter the amount to be debited: "))
    chc = input("Debit {}RS from {} ? [y/n]: ".format(debit, ac_no))
    if chc=="y":
        df = pd.read_csv("acc_holder.csv")
        for x in range(0, len(df)):
            if df.Account_num[x] == ac_no:
                if df.at[x, "Balance"]<debit:
                    print("The Current available Balance: {}".format(df.at[x, "Balance"]))
                    print("Transaction Failed.. due lo low balance")
                    return
                df.at[x, "Balance"]-=debit
                df.to_csv("acc_holder.csv", index=False)
                print("Amount: {} Debited successfuly..".format(credit))
                return
        print("Record not found with ac/no {}".format(ac_no))
    else:
        print("Transaction is cancelled.")

def printAcc_info():
    nm = input("Enter name of account-Holder: ")
    ac_no = int(input("Enter {}'s Account number: ".format(nm)))
    df = pd.read_csv("acc_holder.csv")
    for x in range(0, len(df)):
            if df.Account_num[x] == ac_no:
                print("[STATUS]: Details Matched")
                print("\n> Name of the Account Holder: {}".format(df.Name[x]))
                print("> Account Number: {}".format(df.Account_num[x]))
                print("> Account Type: {}".format(df.Account_type[x]))
                print("> Aadhar Number: {}".format(df.Aadhar_no[x]))
                print("> Available Balance: {}".format(df.Balance[x]))
                return
    print("No Record Found..")

def create_csv():
    nmList = ["Ram", "Sam", "Prabhu", "Kavya", "Rajesh"]
    adNo_lst = [100329468858, 365672000483, 897746530868, 862046529578, 668650947593]
    cnct_lst = [9849894910, 9582654858, 9652839050, 9582454929, 9790865338]
    dob_lst = ["12-2-1990", "13-6-1982", "17-2-2002", "15-10-1992", "18-10-2002"]
    addr_lst = [
        "Opp VjaBuilding, 14-22, RamakrishnaNagar, Guntupalli",
        "Beside Swathi Theater, 23-78, Bhavanipuram, Vijayawada",
        "Opp stationeryPoint, 33-17, Nampally, Hyderabad",
        "Near Bustand, 23-33, Kandigai, Chennai",
        "Near viharPalace, 12-33, Mushirabad, New-Delhi"
    ]

    accHolder_info = {
        "Name": nmList,
        "Aadhar_no": adNo_lst,
        "Contact": cnct_lst,
        "DOB": dob_lst,
        "Address": addr_lst
    }

    df1 = pd.DataFrame(accHolder_info)
    print("\n ACCOUNT HOLDER INFORMATION --")
    print("\n",df1)

    # creating csv file with the above content
    df1.to_csv("acc_holderInfo.csv", sep='|')

    df2 = pd.read_csv("acc_holder.csv")
    print("\n ACCOUNT HOLDERS--")
    print("\n",df2)

    c = input("Do you want to merge Both the CSV files? [y/n]: ")
    if c == "y":
        # concatinating dataframes using INNER JOIN
        res = pd.concat([df1, df2], axis=1, join='inner')
        res.to_csv("Aadhar_db.csv", sep="|")
    else:
        print("Both the CSV files are not merged..")

var = True
while var:
    display_options()
    chc = int(input("> Enter your choice: "))
    if chc == 1:
        appendRow()
    elif chc == 2:
        deleteRecord()
    elif chc == 3:
        credit_to_acc()
    elif chc == 4:
        debit_from_acc()
    elif chc == 5:
        printAcc_info()
    elif chc == 6:
        create_csv()
    elif chc == 7:
        var = False
    else:
        print("[CHOICE_ERROR]: Please Try again..")