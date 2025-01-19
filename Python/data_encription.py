#encrypt code 
def encrypt(text,key):
  result = ""
  for i in range(len(text)):
    char = text[i]
    if (char.isupper()):
      result += chr((ord(char) + key))
    else:
      result += chr((ord(char) + key))
  return result

#decrypt code
def decrypt(text,key):
  result = ""
  for i in range(len(text)):
    char = text[i]
    if (char.isupper()):
      result += chr((ord(char) - key))
    else:
      result += chr((ord(char) - key))
  return result

text = "HELLO this is yash"
key = 4
print("Text : " + text)
print("Shift : " + str(key))
print("Cipher: " + encrypt(text,key))
encrypted = encrypt(text,key)

print("Decrypted: " + decrypt(encrypted,key))
