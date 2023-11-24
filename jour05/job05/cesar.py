def cesar_cipher(message, decalage):
    resultat = ""
    for char in message:
        if char.isalpha():  
            decalage_direction = 1 if char.islower() else -1  

            char_decale = chr(((ord(char) - ord('a' if char.islower() else 'A') + decalage) % 26) + ord('a' if char.islower() else 'A'))

            resultat += char_decale
        else:
            resultat += char 
    return resultat

message = "Hello, World!"
decalage = 3
message_decode = cesar_cipher(message, decalage)
print("Message chiffré:", message_decode)
