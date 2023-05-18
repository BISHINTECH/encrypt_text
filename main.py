def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr(
                (ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(text, shift):
    return encrypt(text, -shift)


text = input("ENTER TEXT:")
try:
    shift_value = int(input("Enter the shift value:"))
    option = int(input('''
    Select an option:
        1. Encrypt
        2. Decrypt
        Option:'''))
except:
    shift_value = 5
    option = 1


match option: 
    case 1:
        result = encrypt(text, shift_value)

    case 2:
        result = decrypt(text, shift_value)

print(result)
