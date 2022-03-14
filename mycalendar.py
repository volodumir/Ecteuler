from datetime import datetime,timedelta

a = [i for i in range(4,100)]

for key in a:
    currentTimeDate = datetime.now() - timedelta(days=key)
    currentTime = currentTimeDate.strftime('%Y-%m--%d')

    print(currentTime)