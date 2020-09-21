import requests
import os
from bs4 import BeautifulSoup
import webbrowser
import pdftotext
from datetime import datetime,timedelta
import time
import json
import sys
import re

page = requests.get("http://cdm.nmusd.us")
soup = BeautifulSoup(page.content, 'html.parser')
cal = soup.body.div("a", string="Printable")[0].get("href")

with requests.get(cal) as r:
    with open("cal.pdf", "wb") as f:
        f.write(r.content)

print("\n"*10)

with open("cal.pdf", "rb") as f:
    pdf = pdftotext.PDF(f, "secret")

month = int(time.strftime('%m'))
day = int(time.strftime('%d'))

dayOfWeek = time.strftime('%A')
weekDayNum = datetime.today().weekday()

startWeekMonth = int((datetime.today() + timedelta(days=(-weekDayNum))).strftime('%m'))
startWeekDay = int((datetime.today() + timedelta(days=(-weekDayNum))).strftime('%d'))

endWeekMonth = int((datetime.today() + timedelta(days=(5 - weekDayNum))).strftime('%m'))
endWeekDay = int((datetime.today() + timedelta(days=(5 - weekDayNum))).strftime('%d'))

timeText = f"{startWeekMonth}/{startWeekDay}-{endWeekMonth}/{endWeekDay}"

print("      " + pdf[0]
    .replace("\n", "\n      ")
    .replace(timeText, f"\033[0;36m{timeText}\033[0m")
    .replace(dayOfWeek,f"\033[0;36m{dayOfWeek}\033[0m")
    )

print(f"Current Week Dates: {timeText}, Current Date: {month}/{day}")

if len(sys.argv) >= 2:
    webbrowser.open(cal)