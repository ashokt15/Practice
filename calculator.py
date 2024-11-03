def calculator(num1 , num2 , operand):
    print("welcome 2 calculator app")
    if operand == 'add':
        result = num1+num2
        print(num1,operand,num2,result)
    elif operand  == 'subtract':
       result = num1 - num2
       print(num1,operand,num2,result)
    elif operand  == 'multiply':
       result = num1 * num2
       print(num1,operand,num2,result)
    elif operand  == 'remainder':
       result = num1%num2
       print(num1,operand,num2,result)
    elif operand  == 'division':
      if num2 != 0:
       result = num1 / num2
       print(num1,operand,num2,result)
      else:
       print("enter a valid expression or exit")
calculator(5,4,"add")
calculator(5,4,"subtract")
calculator(5,4,"multiply")
calculator(10,4,"division")
calculator(8,4,"remainder")
