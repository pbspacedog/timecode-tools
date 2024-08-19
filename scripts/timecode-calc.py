# Copyright (c) 2024 Patrick Burton aka Space Dog

# This script calculates the difference between two timecodes and returns the result in timecode format.

# To run this script, navigate to the directory containing the script and run the following command:
# python timecode-calculator.py OR python3 timecode-calculator.py
# This script will prompt you to enter the starting timecode and the target timecode, 
# then it will calculate the difference between the two timecodes and return the result in timecode format.

from datetime import datetime, timedelta

def timecode_to_timedelta(tc):
    print(f"Converting timecode {tc} to timedelta")
    hours, minutes, seconds, frames = map(int, tc.split(':'))
    return timedelta(hours=hours, minutes=minutes, seconds=seconds, milliseconds=frames * (1000 / 24))

def calculate_timecode_difference(current_tc, target_tc):
    print(f"Calculating difference between {current_tc} and {target_tc}")
    current_td = timecode_to_timedelta(current_tc)
    target_td = timecode_to_timedelta(target_tc)

    difference_td = target_td - current_td

    if difference_td.total_seconds() < 0:
        operation = "subtract"
        difference_td = abs(difference_td)
    else:
        operation = "add"

    total_seconds = int(difference_td.total_seconds())
    frames = int((difference_td.total_seconds() - total_seconds) * 24)
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    difference_tc = f"{hours:02}:{minutes:02}:{seconds:02}:{frames:02}"

    return operation, difference_tc

def main():
    print("Timecode Difference Calculator")
    current_tc = input("Enter the current timecode (HH:MM:SS:FF): ")
    target_tc = input("Enter the desired timecode (HH:MM:SS:FF): ")

    operation, difference_tc = calculate_timecode_difference(current_tc, target_tc)
    
    if operation == "subtract":
        print(f"\nYou need to subtract {difference_tc} from your clips to achieve the target timecode.")
    else:
        print(f"\nYou need to add {difference_tc} to your clips to achieve the target timecode.")

if __name__ == "__main__":
    main()