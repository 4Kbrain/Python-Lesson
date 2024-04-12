def decode_message(encoded_message, encoding_type):
    """
    作られた Aditya Dwi Nugroho

    メッセージを指定されたエンコーディングタイプでデコードします。
    
    """
    import base64
    from codecs import decode as codecs_decode

    if encoding_type == 'base64':
        
        decoded_bytes = base64.b64decode(encoded_message)
    elif encoding_type == 'hex':
        
        decoded_bytes = bytes.fromhex(encoded_message)
    elif encoding_type == 'rot13':
        
        return codecs_decode(encoded_message, 'rot_13')
    else:
        raise ValueError("サポートされていないエンコーディングタイプです。")

    # デコードされたバイト列を文字列に変換
    return decoded_bytes.decode()

def main():
    print("デコードするメッセージのタイプを選択してください: base64, hex, rot13")
    encoding_type = input("タイプ: ")
    encoded_message = input("デコードするメッセージ: ")
    
    try:
        decoded_message = decode_message(encoded_message, encoding_type)
        print("デコードされたメッセージ:", decoded_message)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()