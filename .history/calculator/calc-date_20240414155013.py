<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> origin/main
"""
作られた Aditya Dwi Nugroho

日付計算プログラム
"""


from datetime import datetime, timedelta

def date_calculator():
    date_str = input("Enter a date (YYYY-MM-DD): ")
    date = datetime.strptime(date_str, "%Y-%m-%d")

    print("1. Add")
    print("2. Subtract")
    operation = int(input("Choose an operation (1 or 2): "))

    if operation == 1:
        print("1. Days")
        print("2. Weeks")
        print("3. Months")
        print("4. Years")
        unit = int(input("Choose a unit (1, 2, 3, or 4): "))
    else:
        print("1. Days")
        print("2. Weeks")
        print("3. Months")
        print("4. Years")
        unit = int(input("Choose a unit (1, 2, 3, or 4): "))

    amount = int(input("Enter the amount: "))

    if operation == 1:
        if unit == 1:
            new_date = date + timedelta(days=amount)
        elif unit == 2:
            new_date = date + timedelta(weeks=amount)
        elif unit == 3:
            new_date = date + timedelta(days=amount*30)
        else:
            new_date = date + timedelta(days=amount*365)
    else:
        if unit == 1:
            new_date = date - timedelta(days=amount)
        elif unit == 2:
            new_date = date - timedelta(weeks=amount)
        elif unit == 3:
            new_date = date - timedelta(days=amount*30)
        else:
            new_date = date - timedelta(days=amount*365)

    print("The new date is:", new_date.strftime("%Y-%m-%d"))

<<<<<<< HEAD
=======
=======
"""
作られた Aditya Dwi Nugroho

日付計算プログラム
"""


from datetime import datetime, timedelta

def date_calculator():
    date_str = input("Enter a date (YYYY-MM-DD): ")
    date = datetime.strptime(date_str, "%Y-%m-%d")

    print("1. Add")
    print("2. Subtract")
    operation = int(input("Choose an operation (1 or 2): "))

    if operation == 1:
        print("1. Days")
        print("2. Weeks")
        print("3. Months")
        print("4. Years")
        unit = int(input("Choose a unit (1, 2, 3, or 4): "))
    else:
        print("1. Days")
        print("2. Weeks")
        print("3. Months")
        print("4. Years")
        unit = int(input("Choose a unit (1, 2, 3, or 4): "))

    amount = int(input("Enter the amount: "))

    if operation == 1:
        if unit == 1:
            new_date = date + timedelta(days=amount)
        elif unit == 2:
            new_date = date + timedelta(weeks=amount)
        elif unit == 3:
            new_date = date + timedelta(days=amount*30)
        else:
            new_date = date + timedelta(days=amount*365)
    else:
        if unit == 1:
            new_date = date - timedelta(days=amount)
        elif unit == 2:
            new_date = date - timedelta(weeks=amount)
        elif unit == 3:
            new_date = date - timedelta(days=amount*30)
        else:
            new_date = date - timedelta(days=amount*365)

    print("The new date is:", new_date.strftime("%Y-%m-%d"))

>>>>>>> lazy/main
>>>>>>> origin/main
date_calculator()