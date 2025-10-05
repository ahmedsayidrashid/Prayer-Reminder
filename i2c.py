from RPLCD.i2c import CharLCD
import time

from datetime import datetime

from main import get_prayer_times_for_date, fetch_prayer_times

time_dict = fetch_prayer_times()
prayer_times = get_prayer_times_for_date(time_dict)

todays_date = datetime.now().strftime("%d-%m-%Y")

rns_date = datetime.now().strftime("%H:%M")

time_to_pray = False
for prayer_time in prayer_times:
    if prayer_times[prayer_time] == rns_date:
        print(f"It's time for {prayer_time} prayer now!")
        time_to_pray = True
        break
    
if not time_to_pray:
    print("No prayer at this time! Get back to work!")
print(f"Prayer times for {todays_date}, {rns_date}:" )
print(prayer_times)

lcd = CharLCD(i2c_expander='PCF8574', address =0x27, port=1, cols=16, rows=2, charmap='A00')

#while True:
lcd.clear()
lcd.write_string("No prayer at this time! Get back to work!")
time.sleep(2)
current_row, current_col = lcd.cursor_pos  
lcd.cursor_pos = (current_row, current_col + 1)  # move cursor one to the right
lcd.clear()
