def leapyear(year):
    n=int(year)
    if (n%100 == 0) and  (n%400 == 0):
        print("given century is a leap year")
    elif (n%4== 0) and (n%100 != 0) :
        print ("given year is a leap year....")
    else:
        print("given year is a common year!")

leapyear(345000)
leapyear(300)
leapyear(400)
leapyear(3000)