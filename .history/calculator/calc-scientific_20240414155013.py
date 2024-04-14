<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> origin/main
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "0で割ることはできません！"
    else:
        return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def log(x):
    return math.log(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def main():
    while True:
        print("操作を選択してください。")
        print("1.加算 2.減算 3.乗算 4.除算 5.べき乗")
        print("6.平方根 7.自然対数 8.正弦 9.余弦 10.正接 11.終了")
        choice = input("選択した操作 (1-11): ")

        if choice == '11':
            print("計算機を終了します。")
            break

        if choice in ('6', '7', '8', '9', '10'):
            num = float(input("数値を入力してください: "))
            if choice == '6':
                print("結果: ", sqrt(num))
            elif choice == '7':
                print("結果: ", log(num))
            elif choice == '8':
                print("結果: ", sin(num))
            elif choice == '9':
                print("結果: ", cos(num))
            elif choice == '10':
                print("結果: ", tan(num))
        else:
            num1 = float(input("第一数: "))
            num2 = float(input("第二数: "))

            if choice == '1':
                print("結果: ", add(num1, num2))
            elif choice == '2':
                print("結果: ", subtract(num1, num2))
            elif choice == '3':
                print("結果: ", multiply(num1, num2))
            elif choice == '4':
                print("結果: ", divide(num1, num2))
            elif choice == '5':
                print("結果: ", power(num1, num2))
        print()

if __name__ == "__main__":
<<<<<<< HEAD
=======
=======
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "0で割ることはできません！"
    else:
        return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def log(x):
    return math.log(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def main():
    while True:
        print("操作を選択してください。")
        print("1.加算 2.減算 3.乗算 4.除算 5.べき乗")
        print("6.平方根 7.自然対数 8.正弦 9.余弦 10.正接 11.終了")
        choice = input("選択した操作 (1-11): ")

        if choice == '11':
            print("計算機を終了します。")
            break

        if choice in ('6', '7', '8', '9', '10'):
            num = float(input("数値を入力してください: "))
            if choice == '6':
                print("結果: ", sqrt(num))
            elif choice == '7':
                print("結果: ", log(num))
            elif choice == '8':
                print("結果: ", sin(num))
            elif choice == '9':
                print("結果: ", cos(num))
            elif choice == '10':
                print("結果: ", tan(num))
        else:
            num1 = float(input("第一数: "))
            num2 = float(input("第二数: "))

            if choice == '1':
                print("結果: ", add(num1, num2))
            elif choice == '2':
                print("結果: ", subtract(num1, num2))
            elif choice == '3':
                print("結果: ", multiply(num1, num2))
            elif choice == '4':
                print("結果: ", divide(num1, num2))
            elif choice == '5':
                print("結果: ", power(num1, num2))
        print()

if __name__ == "__main__":
>>>>>>> lazy/main
>>>>>>> origin/main
    main()