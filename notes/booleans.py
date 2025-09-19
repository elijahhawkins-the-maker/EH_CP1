#EH 1st Booleans
import time
import datetime as date

current_time = time.time()
readable_time = time.ctime(current_time)
bruh = date.datetime.now()
hour = bruh.strftime("%H")


print(f"current time in seconds since the date January 1st, 1970(epoch): {current_time}" )
print(f"today is {readable_time} ")
print(f"this is the current time: {bruh}")
print(f"the hour is: {hour}")
#minutes = %M
#weekday = %A
#day = %d
#month = %B, %b
#month num = %m
# year = %Y, %y
# seconds = %S

print(f"The hour is saved as an integer: {isinstance(hour, int)}")
print(f"The hour is saved as an float: {isinstance(hour, float)}")
print(f"The hour is saved as an string: {isinstance(hour, str)}")

over = True

print(f"Hour has a value: {bool(0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000067)}")
