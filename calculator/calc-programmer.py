def binary_operations(operation, x, y):
    if operation == 'AND':
        return x & y
    elif operation == 'OR':
        return x | y
    elif operation == 'XOR':
        return x ^ y
    else:
        return "無効な操作です。"

def not_operation(x):
    return ~x

def shift_operation(direction, x, n):
    if direction == 'LEFT':
        return x << n
    elif direction == 'RIGHT':
        return x >> n
    else:
        return "無効な方向です。"

def convert_base(x, base):
    if base == 'BINARY':
        return bin(x)
    elif base == 'OCTAL':
        return oct(x)
    elif base == 'HEXADECIMAL':
        return hex(x)
    else:
        return "無効な基数です。"

def main():
    while True:
        print("操作を選択してください。")
        print("1.ビット演算 2.ビット反転 3.シフト演算 4.進数変換 5.終了")
        choice = input("選択した操作 (1-5): ")

        if choice == '5':
            print("計算機を終了します。")
            break

        if choice == '1':
            operation = input("演算を入力してください (AND, OR, XOR): ").upper()
            x = int(input("第一数 (整数): "), 2)  # 2進数として入力
            y = int(input("第二数 (整数): "), 2)  # 2進数として入力
            result = binary_operations(operation, x, y)
            print("結果: ", bin(result))
        elif choice == '2':
            x = int(input("数値 (整数): "), 2)  # 2進数として入力
            result = not_operation(x)
            print("結果: ", bin(result))
        elif choice == '3':
            direction = input("方向を入力してください (LEFT, RIGHT): ").upper()
            x = int(input("数値 (整数): "), 2)  # 2進数として入力
            n = int(input("シフトするビット数: "))
            result = shift_operation(direction, x, n)
            print("結果: ", bin(result))
        elif choice == '4':
            base = input("変換する基数を入力してください (BINARY, OCTAL, HEXADECIMAL): ").upper()
            x = int(input("数値 (整数): "))
            result = convert_base(x, base)
            print("結果: ", result)
        else:
            print("無効な入力です。もう一度試してください。")
        print()

if __name__ == "__main__":
    main()