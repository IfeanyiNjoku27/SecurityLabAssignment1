from CypherCodeA import symbolIndex, translatedIndex

# Code Section to brute force decryption
message = input("Enter a message: ")
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

for key in range(len(SYMBOLS)):
    translated = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key
        if translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)
        translated += SYMBOLS[translatedIndex]
    else:
        translated += symbol

print('Key #%s: %s' % (key, translated))