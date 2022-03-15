from datetime import datetime,timedelta

def nbu_dates():
    dddaaayys = 365*15
    a = [i for i in range(4,dddaaayys)]
    data = []

    for key in a:
        currentTimeDate = datetime.now() - timedelta(days=key)
        currentTime = currentTimeDate.strftime('%Y%m%d')

        data.append(currentTime)
    return data


# print(nbu_dates())