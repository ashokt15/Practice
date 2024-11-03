def weekday(number):
    n = int(number)
    if (n<0) or (n>6):
      print("enter a valid number between 0 to 6")
    elif (n == 0):
       print("sunday")
    elif (n == 1):
       print("Monday")
    elif (n == 2):
       print("Tuesday")
    elif (n == 3):
       print("Wenesday")
    elif (n == 4):
       print("Thursday")
    elif (n == 5):
       print("Friday")
    elif (n == 6):
       print("Saturday")    
weekday(1)
weekday(7)
weekday(-1)
weekday(6)
weekday(4)  
       