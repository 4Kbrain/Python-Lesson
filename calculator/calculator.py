def add(x, y):
    """加算"""
    return x + y

def subtract(x, y):
    """減算"""
    return x - y

def multiply(x, y):
    """乗算"""
    return x * y

def divide(x, y):
    """除算"""
    if y == 0:
        return "0で割ることはできません！"
    else:
        return x / y

def main():
    while True:
        print("操作を選択してください。\n1.加算\n2.減算\n3.乗算\n4.除算\n5.終了")
        choice = input("選択した操作 (1/2/3/4/5): ")

        if choice == '5':
            print("計算機を終了します。")
            break

        if choice in ('1', '2', '3', '4'):
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
        else:
            print("無効な入力です。もう一度試してください。")

if __name__ == "__main__":
    main()