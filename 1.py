def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
      
        if char.isalpha():
            if char.islower():
                shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            shifted_char = char
        encrypted_text += shifted_char
    return encrypted_text

# 
text = "Hello, World!"
shift = 3
encrypted_text = caesar_cipher(text, shift)
print("Зашифрованный текст:", encrypted_text)