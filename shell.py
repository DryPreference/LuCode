import Lucode

print("\n Lucode V1.4 -- To exit type 'quit' \nThis is a personal project if you have any suggestions please contact me at: lukas.lschn.schneider@fau.de\n")

while True:
    text = input('lucode_V1.4 --> ')
    result, error = Lucode.run(' <stdin>', text)

    if text == 'quit' :
        break
    
    if error: print(error.as_string())
    else: print(result)
