from datetime import datetime, timedelta    # Gets dates and time

schedule = """
┌───────────────────────────────┐ ┌───────────────────────────────┐
│ Late Start Schedule           │ │ Odd Schedule                  │
│ ─────────────────────────────	│ │ ───────────────────────────── │
│  7:25 -  7:55 Intervention	│ │  6:55 -  7:50 Choir      (0)  │
│  9:00 -  9:30 Choir      (0)	│ │  7:55 -  8:25 Breakfast       │
│  9:35 - 10:05 Chinese    (1)	│ │  8:30 -  9:55 Chinese    (1)  │
│ 10:10 - 10:40 English    (2)	│ │ 10:05 - 11:30 Physics    (3)  │
│ 10:40 - 10:45 Break           │ │ 11:40 -  1:00 Statistics (5)  │
│ 10:50 - 11:20 Physics    (3)  │ └───────────────────────────────┘
│ 11:25 - 11:55 US History (4)  │ ┌───────────────────────────────┐
│ 12:00 - 12:30 Statistics (5)  │ │ Even Schedule                 │
└───────────────────────────────┘ │ ───────────────────────────── │
┌───────────────────────────────┐ │  6:55 -  7:50 Choir      (0)  │
│ Placeholder A --------------- │ │  7:55 -  8:25 Breakfast       │
│ Placeholder B --------------- │ │  8:30 -  9:55 English    (1)  │
│ Placeholder C --------------- │ │ 10:05 - 11:30 US History (3)  │
└───────────────────────────────┘ └───────────────────────────────┘
"""

# Today's day of the week
date = datetime.today()
DoTW = datetime.today().weekday() # 0-7, Mon-Sun

# Date of today 
month = int(date.strftime('%m'))        # 1-12, Month
day = int(date.strftime('%d'))          # 1-31, Date
today = f"{month}/{day}"
hour = int(date.strftime("%H"))
minute = int(date.strftime("%M"))
time = date.strftime("%m/%d %a %I:%M")

# __ min until __

minute_time = hour*60 + minute

if DoTW==0: # Late Start
    today_sched = ((540,570), (575,605), (610,640), (650,680), (685,715), (720,750))
    today_classes = ("Choir", "Chinese", "English", "Physics", "US History", "Statistics")
elif DoTW==1 or DoTW==3: # Odd
    today_sched = ((415,470), (475,505), (510,595), (605, 690), (700,780))
    today_classes = ("Choir", "Breakfast", "Chinese", "Physics", "Statistics")
else: # Even
    today_sched = ((415,470), (475,505), (510,595), (605, 690))
    today_classes = ("Choir", "Breakfast", "English", "US History")

links = {
    "Choir": "zoommtg://nmusd.zoom.us/join?confno=4130515482",
    "Chinese": "zoommtg://nmusd.zoom.us/join?confno=93757689317&pwd=Leifeng1",
    "English": "zoommtg://nmusd.zoom.us/join?confno=6799693127",
    "Physics": "zoommtg://nmusd.zoom.us/join?confno=95973021704",
    "US History": "zoommtg://nmusd.zoom.us/join?confno=5190214576",
    "Statistics": "zoommtg://nmusd.zoom.us/join?confno=92086986489&pwd=TDNUYk9KWlJvdGlxODZrT253VHRJQT09"
}

for current_class, class_time in zip(today_classes, today_sched):
    if minute_time < class_time[0]: # In between classes
        next_class_when = f"\033[1;31m{current_class}\033[0m starts in \033[1;31m{class_time[0] - minute_time}\033[0m min".ljust(51)
        zoom_link = links[current_class]
        zoom_message = f"Click to Zoom into {current_class}"
        break
    elif minute_time < class_time[1]: # In between classes
        next_class_when = f"\033[1;31m{current_class}\033[0m ends in \033[1;31m{class_time[1] - minute_time}\033[0m min".ljust(51)
        zoom_link = links[current_class]
        zoom_message = f"Click to Zoom into {current_class}"
        break

# Prints schedule and replaces key items with colored text

print(schedule
    .replace("Placeholder A ---------------", 
             f"Current Time: \033[1;31m{time}\033[0m")
    .replace("Placeholder B ---------------", 
             f"{next_class_when}")
    .replace("Placeholder C ---------------", 
             f"\u001b]8;;{zoom_link}\u001b\\{zoom_message}\u001b]8;;\u001b\\"
             + " "*(29-len(zoom_message)))
    )

# echo -e '\e]8;;zoommtg://nmusd.zoom.us/join?confno=4130515482\aThis is a link\e]8;;\a'
