Use the scripts in the /scripts directory to edit your clips' timecodes in batches inside DaVinci Resolve.

"add-frames.py" allows you to adjust all your timecodes by a positive value.
"subtract-frames.py" allows you to adjust all your timecodes by a negative value.
"set-timecode.py" is for setting all timecodes in the bin to the same value.
    ^ Make sure you back up your clips if in doubt because you can't reverse this one.
"timecode-calc.py" is for calculating how many frames you need to add or subtract to get to the timecode you want.

Read the comments at the tops of each script for more info on how to use them.

The "set-timecode.py" script is derivative of the "tcreset.py" script in the project 
ChangeClipTimecode by Igor Riđanović: https://github.com/IgorRidanovic/ChangeClipTimecode
When I tried to run Igor's script it didn't work - perhaps because my current version of Resolve is 18.6. 
So I fixed it and made it work for me before creating the other scripts, more tailored to my use case.

Thank you Igor Riđanović for your initial code which made this project possible.
