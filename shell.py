import lucode

print("Beta Lucode V0.1 -- To exit type 'quit' \nThis is a personal project if you have any suggestions please contact me at: lukas.lschn.schneider@fau.de")

while True:
    text = input('lucode_V1.0_--> ')
    result, error = lucode.run('<stdin>', text)

    if text == 'quit' :
        break
    
    if error: print(error.as_string())
    else: print(result)
