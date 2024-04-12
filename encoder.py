def encode_message(message, encoding_type):
    """
    作られた Aditya Dwi Nugroho
    
    メッセージを指定されたエンコーディングタイプでエンコードします。
    
    """
    import base64
    from codecs import encode as codecs_encode

    if encoding_type == 'base64':
        
        encoded_bytes = base64.b64encode(message.encode())
    elif encoding_type == 'hex':
        
        encoded_bytes = message.encode().hex()
    elif encoding_type == 'rot13':
        
        return codecs_encode(message, 'rot_13')
    elif encoding_type == 'binary':
        
        return ' '.join(format(ord(x), 'b') for x in message)
    elif encoding_type == 'reverse':
        
        return message[::-1]
    else:
        raise ValueError("サポートされていないエンコーディングタイプです。")

    # エンコードされたバイト列を文字列に変換
    if isinstance(encoded_bytes, bytes):
        return encoded_bytes.decode()
    else:
        return encoded_bytes

def main():
    print("エンコードするメッセージのタイプを選択してください: base64, hex, rot13, binary, reverse")
    encoding_type = input("タイプ: ")
    message = input("エンコードするメッセージ: ")
    
    try:
        encoded_message = encode_message(message, encoding_type)
        print("エンコードされたメッセージ:", encoded_message)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()