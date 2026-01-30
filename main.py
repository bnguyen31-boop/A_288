<!DOCTYPE html>
<html>
<head>
    <title>Analog System</title>
    <link rel="stylesheet" href="https://pyscript.net">
    <script type="module" src="https://pyscript.net"></script>
</head>
<body style="background-color: black; margin: 0;">
    <script type="py" terminal worker>
import time
from pyscript import fetch
import asyncio

async def main():
    print("what up")
    time.sleep(3)
    print("please answer truthfully")
    time.sleep(2)
    name = input("what's ur full name? ")
    print("hello", name)
    time.sleep(0.2)
    house = input("whats ur address? ")
    time.sleep(0.2)

    # Simplified birth year check
    year_in = input("year of birth?(year only) ")
    year = int(year_in) if year_in.isdigit() else 0
    if year < 1900 and year != 0:
        print("ain't no way")
    
    month_input = input("month of birth? ")
    day = input("day of birth? ")

    # IP TRACE FIX: fetch real public IP from ipify
    print("Tracing connection...")
    try:
        response = await fetch("https://api.ipify.org")
        IPAddr = await response.text()
    except Exception:
        IPAddr = "REDACTED/FAILED"

    print("so your birthday is " + month_input + "/" + str(day) + "/" + str(year))
    time.sleep(1)
    print("and the time at your location is " + time.ctime())
    time.sleep(2)
    
    # Analog clear screen
    print("\033[H\033[J") 
    time.sleep(1)

    print("dont worry, I already know ur ip is " + IPAddr)
    time.sleep(5)

    print(f"ok, {name} living at {house} ip is: {IPAddr}")
    time.sleep(3)
    
    answer = input("are you sure you answered truthfully? ")
    if answer == "yes":
        sure = input("REALLY SURE!??? ")
        if sure == "yes":
            print("still gonna find you")
    else:
        print("im gonna find you if you don't restart this quiz correctly")

asyncio.ensure_future(main())
    </script>
</body>
</html>
