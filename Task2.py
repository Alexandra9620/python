time = int(input("Введите время в секундах: "))
hour = time // 3600
minute = (time - hour * 3600) // 60
minute_second = (time - hour * 3600)
second = minute_second - minute * 60
if hour < 10:
    hour = "0"+str(hour)
if minute < 10:
    minute = "0"+str(minute)
if second < 10:
    second = "0"+str(second)
print(f"{hour}:{minute}:{second}")