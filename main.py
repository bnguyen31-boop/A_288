import time
import socket
import os  # Fixed: Added missing import for clear_screen to work

print("what up")
time.sleep(3)
print("please answer truthfully")
time.sleep(2)
name = input ("what's ur full name?")
print("hello", name)
time.sleep(0.2)
house = input ("whats ur address?")
time.sleep(0.2)

# Fixed: Wrapped input in int() so you can compare numbers
year = int(input ("year of birth?(year only)"))
if year < 1900:
  print("ain't no way")
time.sleep(0.2)

# Fixed: Wrapped input in int() for the comparison below
month_input = input ("month of birth?")
try:
    month = int(month_input)
except ValueError:
    month = month_input # Keep as string if they typed "january"

if isinstance(month, int) and month > 12:
 print("ain't no way!")
time.sleep(0.2)
day = input ("day of birth?")

if month == "january":
 month = 1
if month == "feburary":
 month = 2
if month == "march":
 month = 3
if month == "april":
 month = 4
if month == "may":
 month = 5
if month == "june":
 month = 6
if month == "july":
 month = 7
if month == "august":
 month = 8
if month == "september":
 month = 9
if month == "october":
 month = 10
if month == "november":
 month = 11
if month == "december":
 month = 12

# Fixed: Use 'and' for multiple conditions
if day == "30" and month == 1:
  print("aww too bad so sad")
  time.sleep(0.3)
  
# Fixed: Converted numbers to strings so they can be added to the text
print("so your birthday is " + str(month) + "/" + str(day) + "/" + str(year))
time.sleep(1)

# Fixed: time is a module; use time.ctime() to show the actual time
print("and the time at your location is " + time.ctime())
time.sleep(2)
print ("correct?")
time.sleep(4)

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
clear_screen()

time.sleep(1)

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("dont worry, I already know ur ip is " + IPAddr)
time.sleep(10)

print("ok, ", name, " living at ", house, " ip is: ", IPAddr)
time.sleep(3)
answer = input ("are you sure you answered truthfully?")
if answer == "yes":
 sure = input ("REALLY SURE!???")
 if sure == "yes":
   print("still gonna find you")
else:
 print("im gonna find you if you don't restart this quiz correctly")
