import datetime

now = datetime.datetime.now()
print("Current date and time is {}".format(now))
print(now.strftime("%y-%m-%d %H:%M:%S"))