def digit_of_life(date):
    while len(date) > 1:
        total = sum(int(d) for d in date)
        date = str(total)
    return date

birthday = input("Enter your birthday (YYYYMMDD, YYYYDDMM, or MMDDYYYY): ")
print("Digit of Life:", digit_of_life(birthday))
