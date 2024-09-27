def is_leap_year():
    # Werite your logic here
    year = int(input(" Please enter a year :"))
    if ( year % 4 == 0 and year % 100 == 0 ) or ( year % 400 == 0  ):
        print(" This is a leap year ")
    else:
        print(f"{year}is not a leap year ")

is_leap_year()