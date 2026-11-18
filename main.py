expenses=[]
while True:
    print("=================")
    print('    PERSONAL EXPENSE TRACKER')
    print("=================")

    print("1.Add Expense")
    print("2.View Expense")
    print("3.Total Expense")
    print("4.Exit")
    choice=input("Choose options given above (1-4):")
    if choice not in ("1","2","3","4"):
        print("Invalid Choice")


    elif choice=="1":
        print("\n.....ADD NEW EXPENSE.....")
        name=input("Enter expense name: ")
        category=input("Enter category of your expense :")
        amount=float(input("Enter the amount :"))
        expense= {
            "name":name,
            "category":category ,
            "amount":amount
        }
        expenses.append(expense)
        print("Expense added successfully")

    elif choice=="2":
        print("\n.....View Expense .....")
        if not expenses:
            print("No expense found")
        else:
            for i , expense in enumerate(expenses,start=1):
                print("\nExpense:",i)
                print("Name:",expense["name"])
                print("Category:",expense["category"])
                print("Amount: Rs.",expense["amount"])
    elif choice=="3":
        print("\n.....Total Expense Selected.....")
        if not expenses:
            print("No expenses available")
        else:
            total=sum(expense["amount"] for expense in expenses)
            print("Total expenses: Rs.",total)
    elif choice=="4":
        print("Thank you for using Expense Tracker")
        break


