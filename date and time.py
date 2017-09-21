from datetime import datetime
now = datetime.now()
print(now)



# different version of date and time

print (('%s/%s/%s') % (now.month   , now.day, now.year))


# hours and minutes

print(('%s:%s:%s')%(now.hour, now.minute, now.second))