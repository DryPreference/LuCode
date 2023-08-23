import Lucode
print("Welcome to Lucode Version 1.0 \nTo Exit type quit \n")

while True:
		text = input('Lucode_V1.0 --> ')
		result, error = Lucode.run('<stdin>', text)
		if text == "quit":
			break

		if error: 
			print(error.as_string())
		else:
			 print(result)
