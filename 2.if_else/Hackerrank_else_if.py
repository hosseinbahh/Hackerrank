# start
N = int(input(" Please enter a number :"))

if N % 2 != 0:
    print(" Weird ")
elif N % 2 == 0:
    if 2 <= N <= 5:
        print(" Not Weird ")

    elif 6 <= N <= 20:
        print(" Weird ")

    elif N > 20:
        print(" Not Weird ")