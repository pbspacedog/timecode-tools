# Copyright (c) 2024 Patrick Burton aka Space Dog

# BEFORE RUNNING THIS SCRIPT, BACK UP YOUR CLIPS unless you're okay with your timecodes being modified forever.

# This script adds the specified timecode to the start timecode of all clips in the current bin 
# Before running this script, arrange the clips you want to add the timecode to into a bin, 
# and make sure the bin is selected in the Project window.
# Inside this script, edit the time_to_subtract variable (at the bottom) to the desired timecode you want to subtract.

# To run the script, click Window > Console and then paste the script into the console and press enter. 

import sys
from datetime import datetime, timedelta

def _validate(x):
    # Validate and reformat timecode string
    if len(x) != 11:
        sys.exit('Invalid timecode. Try again.')

    c = ':'
    colonized = x[:2] + c + x[3:5] + c + x[6:8] + c + x[9:]

    if colonized.replace(':', '').isdigit():
        return colonized
    else:
        sys.exit('Invalid timecode. Try again.')

def timecode_to_timedelta(tc):
    # Convert timecode string to timedelta
    hours, minutes, seconds, frames = map(int, tc.split(':'))
    return timedelta(hours=hours, minutes=minutes, seconds=seconds, milliseconds=frames * (1000 / 24))

def subtract_timecode(tc, subtract_tc):
    # Convert both timecodes to timedelta objects
    original_td = timecode_to_timedelta(tc)
    subtract_td = timecode_to_timedelta(subtract_tc)

    # Subtract the timecode durations
    if original_td < subtract_td:
        # Ensure no negative timecode by returning zero if the result would be negative
        new_td = timedelta(0)
    else:
        new_td = original_td - subtract_td

    # Convert back to timecode format
    total_seconds = int(new_td.total_seconds())
    frames = int((new_td.total_seconds() - total_seconds) * 24)
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}:{frames:02}"

def reset_clip_timecode(subtract_tc):
    projectmanager = resolve.GetProjectManager()
    project = projectmanager.GetCurrentProject()
    mediapool = project.GetMediaPool()
    currentbin = mediapool.GetCurrentFolder()
    clips = currentbin.GetClips()

    for clip in clips.values():
        # Get the current start timecode
        current_tc = clip.GetClipProperty('Start TC')
        # Subtract specific time from the current timecode
        new_tc = subtract_timecode(current_tc, subtract_tc)
        # Set new starting timecode to each clip
        clip.SetClipProperty('Start TC', new_tc)

        # Check back new timecodes
        print(new_tc, clip.GetClipProperty('Clip Name'))

if __name__ == '__main__':
    resolve = bmd.scriptapp("Resolve")

    # Define the timecode to subtract (e.g., 02:23:10:01)
    time_to_subtract = "02:23:10:01"
    reset_clip_timecode(time_to_subtract)