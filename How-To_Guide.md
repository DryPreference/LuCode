# A HOW TO GUIDE

### 1.Step create shell
1. create a shell program with a ininite loop that prints the text that is inputed

### 2. Create a Lexter 
A lexter will go through every char and break it up into so called tokens so 2 + 4 will become '2' '+' '4'

1. craete a token class in a sepereate file and initilize this class with self type_ and value
2. create a representation method which returns the type and the value of the  Tokens
3. define constans like Int, float, double, plus, minus etc. Also create a DIGIT constant with all numbers in a string
4. Create lexter class:
    4a. define a __init:: method.
    4b. define an advance method - this will advance to next char in the text 
    4c. create a make_tokens method. this will ittereate through the text and split it up into tokens
        - This make_tokens will be needed for each constant which was defined in 3.


### Add new Operator  
1.  Update Syntax 
2.  crate a new Token. and add to make_tokens
3. create new function in Parser that returns return self.bin_op(self.atom, (TOKEN, ), self.factor)
4.  Update Number Class - create new method that executes the new operator
5. Update the Interpreter/visit_BinOpNode and add the binary operation


### Adding Variables 

1. Update the Tokens (Identifier, Keyword, EQ)
2. Updating the Lexer and add the TOKEN
 


# What is?

## Representation method:

    Return a string containing a printable representation of an object. For many types, this function makes an attempt to return a string that would yield an object with the same value when passed to eval(); otherwise, the representation is a string enclosed in angle brackets that contains the name of the type of the object together with additional information often including the name and address of the object. A class can control what this function returns for its instances by defining a __repr__() method. If sys.displayhook() is not accessible, this function will raise RuntimeError.