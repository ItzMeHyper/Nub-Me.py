def calc_min(hrs,mts):
    minutes = hrs * 60 + mts
    return minutes

h = int(input("Enter the hours\n"))
m = int(input("Enter the minutes\n"))
time = calc_min(h,m)
print("Time in minutes =", time)
