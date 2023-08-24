# A HOW TO GUIDE


### Add new Operator  
1.  Update Syntax 
2.  crate a new Token. and add to make_tokens
2a. create new function in Parser that returns return self.bin_op(self.atom, (TOKEN, ), self.factor)
3.  Update Number Class - create new method that executes the new operator
3a. Update the Interpreter/visit_BinOpNode and add the binary operation


### Adding Variables

1. Update the Tokens (Identifier, Keyword, EQ)
2. Updating the Lexer and add the TOKEN
 
