import mycalendar as mycalendar
import myjson as myjson
import time

start = time.time()
nbu_dates = mycalendar.nbu_dates()

for datesgen in nbu_dates:
    myjson.myjson(datesgen)


stop = time.time()-start

# 1835.448443889618
print(stop)