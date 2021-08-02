#! /usr/local/bin/python3

# Last 14 days highs and lows script
# For WeatherCat - https://trixology.com
# By Jason Snell <jsnell@sixcolors.com>

import re
import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import date

# Path to folder containing WeatherCat data files in year-folder format
# It's usually '/Users/[your-username]/Library/WeatherCatData/[your-location]/'

weatherCatPath = '/Users/jsnell/Dropbox/Location1/'

# Path to folder where you want image to be saved

savePath = '/Users/jsnell/Desktop/'

# F or C switch; F is default

useFahrenheit = True

hitemp = defaultdict(lambda: -99999)
lotemp = defaultdict(lambda: 99999)
diff = {}
today = date.today()
month = int(today.strftime('%m'))
day = today.strftime('%d')
year = today.strftime('%Y')
datelist = []
daysList = ['S', 'M', 'T', 'W', 'Th', 'F', 'S', 'S']
todaysday = int(today.strftime('%w'))
chartlist = []

for i in range(0, 14):
    if todaysday == 0:
        todaysday = 7
    chartlist.append(daysList[todaysday])
    todaysday -= 1

chartlist.reverse()

datapoint = re.compile(r't:([0-9]{2})[0-9]{4}')
temppoint = re.compile(r'T:(-?[0-9]{1,3}\.[0-9]{2})')

for i in range(month-1, month+1, 1):

    if i < 1:
        monthcode = 12
        yearcode = (year - 1)
    else:
        monthcode = i
        yearcode = year

    filepath = (weatherCatPath + f'{yearcode}/{monthcode}_WeatherCatData.cat')
    file = open(filepath, 'r')
    monthstring = str(i)
    if i < 10:
        monthstring = "0" + monthstring

    for count, line in enumerate(file):
        if count > 10:
            theday = datapoint.search(line)
            todayDay = monthstring + (theday.group(1))
            thetemp = temppoint.search(line)
            tempfloat = float(thetemp.group(1))
            if useFahrenheit is True:
                theTempF = round(9.0/5.0 * tempfloat + 32, 0)
                hitemp[todayDay] = max(theTempF, hitemp[todayDay])
                lotemp[todayDay] = min(theTempF, lotemp[todayDay])
            else:
                theTempC = round(tempfloat, 0)
                hitemp[todayDay] = max(theTempC, hitemp[todayDay])
                lotemp[todayDay] = min(theTempC, lotemp[todayDay])

for k in hitemp:
    diff[k] = round((hitemp[k] - lotemp[k]), 1)

# now loop through from monthstring + day
# plucking values for 14 days and putting them in a new list or dict

theHighs = list(diff.values())
theHighs = theHighs[-14:]
theLows = list(lotemp.values())
theLows = theLows[-14:]
theDates = list(diff.keys())
theDates = theDates[-14:]

# Graphing

fig, ax = plt.subplots()

font = {'fontname': 'Helvetica Neue'}
lomin = min(theLows) - 1
ax.bar(theDates, theHighs, bottom=theLows, color="green")
ax.bar(theDates, theLows, label='Lo', color="white")
ax.bar_label(ax.containers[0], color="black", fontweight='bold')
ax.bar_label(ax.containers[1], color="white", fontweight='bold')
ax.set_aspect(aspect=0.2)
ax.set_yticks([])
plt.box(False)
plt.ylim(ymin=lomin)
plt.xticks(theDates, chartlist, color="black", **font)
plt.savefig(f'{savePath}latesttemps.png', bbox_inches='tight',
            dpi=300, pad_inches=0.05)
