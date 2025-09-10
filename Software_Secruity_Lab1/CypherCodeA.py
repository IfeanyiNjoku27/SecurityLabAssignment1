import pyperclip

# The string to be encrypted/decrypted:
message = input("Enter what you want encrypted or decrypted: ")

# The encryption/decryption key:
key = int(input("Enter key length: "))

# Whether the program encrypts or decrypts:
mode = input("Would you like to 'encrypt' or 'decrypt'? ")

# Every possible symbol that can be encrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Store the encrypted/decrypted form of the message:
translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        if mode == 'encrypt':
            translatedIndex = (symbolIndex + key) % len(SYMBOLS)
        elif mode == 'decrypt':
            translatedIndex = (symbolIndex - key) % len(SYMBOLS)

        translated += SYMBOLS[translatedIndex]
    else:
        translated += symbol

# Output
print(f"Message: {message}")
print(f"Key: {key}")
print(f"Mode: {mode}")
print(f"{mode.title()}ed Message: {translated}")

pyperclip.copy(translated)