time_periods = '1h 45m,360s,25m,30m 120s,2h 60s'
time_periods = time_periods.replace(' ',',')
periods = time_periods.split(',')
total_minutes = 0
for period in periods:
    if 'h' in period:
        total_minutes += int(period[:-1]) * 60
    elif 'm' in period:
        total_minutes += int(period[:-1])
    elif 's' in period:
        total_minutes += int(period[:-1]) // 60
print(total_minutes)