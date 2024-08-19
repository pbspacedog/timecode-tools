# Copyright (c) 2024 Patrick Burton aka Space Dog
# Thank you to Igor Riđanović, igor ( at ) hdhead.com who wrote the original ChangeClipTimecode script this was based on

# BEFORE RUNNING THIS SCRIPT, BACK UP YOUR CLIPS unless you're okay with your timecodes being modified forever.

# This script sets the timecode of all clips in the current bin to the specified timecode in DaVinci Resolve.
# Before running this script, arrange the clips you want to set the timecode of into a bin, 
# and make sure the bin is selected in the Project window.
# Inside this script, edit the timecode variable (at the bottom) to the desired timecode.

# To run the script, click Window > Console and then paste the script into the console and press enter.

import sys

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

def reset_clip_timecode(x):
    tcValid = _validate(x)

    projectmanager = resolve.GetProjectManager()
    project = projectmanager.GetCurrentProject()
    mediapool = project.GetMediaPool()
    currentbin = mediapool.GetCurrentFolder()
    clips = currentbin.GetClips()

    for clip in clips.values():
        # Set new starting timecode to each clip
        clip.SetClipProperty('Start TC', tcValid)

        # Check back new timecodes
        new_tc = clip.GetClipProperty('Start TC')
        clip_name = clip.GetClipProperty('Clip Name')
        print(new_tc, clip_name)

if __name__ == '__main__':
    resolve = bmd.scriptapp("Resolve")

    # Set the desired timecode directly here
    timecode = "01:00:00:00"  # Example: 01:00:00:00
    reset_clip_timecode(timecode)