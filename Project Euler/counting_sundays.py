months=[6,2,2,5,0,3,5,1,4,6,2,4]
days=["sun","mon","tues","wed","thur","fri","sat"]

date = months[6]+15+3

while date-7 >= 0:
    date-=7

print(days[date])

year = year%400
year/4 + year/4 + day + month
