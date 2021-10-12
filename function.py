#Write a function

def is_leap(year):
    leap = False
    if(year%100==0):
        if(year%400==0):
            leap=True
    else:
        if(year%4==0):
            leap=True
    return leap
year=int(input())
if is_leap(year)==True:
    print('Leap Year')
else:
    print('Not a leap year')
