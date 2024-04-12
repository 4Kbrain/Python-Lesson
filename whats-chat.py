import pywhatkit

def list_unread_messages():
    
    unread_messages = pywhatkit.history()
    

    for message in unread_messages:
        print(message)

list_unread_messages()
