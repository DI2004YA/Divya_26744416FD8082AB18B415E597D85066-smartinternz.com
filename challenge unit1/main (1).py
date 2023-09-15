def isleapYear(year):
  if(year%4==0 and year%100!=0) or year%4==0:
    return True
  else:
    return False
year=int(input("Enter a year :"))
if isleapYear(year):
    print("{} is a leapyear .".format (year))
else:
    print("{} is not a leapyear.".format(year))
