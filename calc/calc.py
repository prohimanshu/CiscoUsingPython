while True:
   print("Options:")
   print("Enter 'add' to add two numbers")
   print("Enter 'subtract' to subtract two numbers")
   print("Enter 'multiply' to multiply two numbers")
   print("Enter 'divide' to divide two numbers")
   print("Enter 'quit' to end the program")
   user_input = input(": ")

   if user_input == "quit":
      break
   elif user_input == "add":
      numa = float(input("Enter a number: "))
      numb = float(input("Enter another number: "))
      result = str(numa + numb)
      print("The addition is " + result)
   elif user_input == "subtract":
      numa = float(input("Enter a number: "))
      numb = float(input("Enter another number: "))
      result = str(numa - numb)
      print("The subtraction is " + result)
   elif user_input == "multiply":
      numa = float(input("Enter a number: "))
      numb = float(input("Enter another number: "))
      result = str(numa * numb)
      print("The multiplication is " + result)
   elif user_input == "divide":
      numa = float(input("Enter a number: "))
      numb = float(input("Enter another number: "))
      result = str(numa / numb)
      print("The division is " + result)
   else:
      print("Unknown input")
