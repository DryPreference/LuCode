import Lucode

print("\nBeta Lucode V0.3 -- To exit type 'quit' \nThis is a personal project if you have any suggestions please contact me at: lukas.lschn.schneider@fau.de\n")

while True:
    text = input('(Beta)lucode_V0.3 --> ')
    result, error = Lucode.run('<stdin>', text)

    if text == 'quit' :
        break
    
    if error: print(error.as_string())
    else: print(result)
