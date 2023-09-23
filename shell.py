import Lucode

print("\n Lucode V1.5 -- To exit type 'quit' or 'Quit' \n This is a personal project if you have any suggestions please contact me at: lukas.lschn.schneider@fau.de\n")

while True:
    text = input('lucode_V1.5 --> ')
    result, error = Lucode.run(' <stdin>', text)

    if text == 'quit' or text == 'Quit':
        break
    
    if error: print(error.as_string())
    else: print(result)

