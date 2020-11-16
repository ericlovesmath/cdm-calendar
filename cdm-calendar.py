import requests, pdftotext                  # Scrapes website to pdf
from bs4 import BeautifulSoup               # Parses HTML
import os, sys                              # Changes paths and checks args
import webbrowser                           # Opens URL
from datetime import datetime, timedelta    # Gets dates and time

#page = requests.get("http://cdm.nmusd.us")                   # Scrapes CDM website
#soup = BeautifulSoup(page.content, 'html.parser')            # Parses html
#cal = soup.body.div("a", string="Printable")[0].get("href")  # Gets hyperlink named "Printable"

calPath = os.path.expanduser("~/Desktop/Bash/cal.pdf")       # Directory to create cal.pdf in

#if len(sys.argv) >= 2:
#    webbrowser.open(cal)

# Writes cal.pdf and reads it
#with requests.get(cal) as r:
#    with open(calPath, "wb") as f:
#        f.write(r.content)



with open(calPath, "rb") as f:
    pdf = pdftotext.PDF(f, "secret")

# Today's day of the week
date = datetime.today()
dayOfWeek = date.strftime('%A')
weekDayNum = datetime.today().weekday()

# Date of today
month = int(date.strftime('%m'))
day = int(date.strftime('%d'))
today = f"{month}/{day}"

# Date of start of school week
startWeekMonth = int( (date + timedelta(days=(-weekDayNum))).strftime('%m') ) 
startWeekDay = int( (date + timedelta(days=(-weekDayNum))).strftime('%d') )
startDay = f"{startWeekMonth}/{startWeekDay}"

# Date of end of school week
endWeekMonth = int( (date + timedelta(days=(4 - weekDayNum))).strftime('%m') )
endWeekDay = int( (date + timedelta(days=(4 - weekDayNum))).strftime('%d') )
endDay = f"{endWeekMonth}/{endWeekDay}"

# Prints schedule and replaces key items with colored text
print("      " + pdf[0]
    .replace("\n", "\n")                             # Adds space to front of each line
#    .replace(startDay, f"\033[0;36m{startDay}\033[0m")     # Color the start of the week cyan
#    .replace(endDay, f"\033[0;36m{endDay}\033[0m")         # Color the end of the week cyan
    .replace(dayOfWeek,f"\033[1;31m{dayOfWeek}\033[0m")    # Color the day of the week red
    .replace(today, f"\033[1;31m{today}\033[0m")           # Color today's date red
    )

print(f"Current Week Dates: {startDay} - {endDay}, Current Date: {month}/{day}, Day of the Week: {dayOfWeek}")

# Opens calendar in default browser if there are extra args


# Delete cal.pdf
# if os.path.exists(calPath):
#     os.remove(calPath)
