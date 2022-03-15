import datetime as dt

now = dt.datetime.now()
print(now)
output_a = now.strftime("%Y.%m.%d %H:%M:%S")

print(output_a)

day5 = now.replace(day = (now.day+ 5))

print(day5)
