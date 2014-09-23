SpeedrunProject-B351
====================

TODO:

    1) Decide how we will format input to the Mnemonic Reader, and make the reader accept this format.

    2) Decide on, and implement a feedback system, so that our Python code (which does the hard AI work) knows what worked and what didn't, and the Lua script knows when to run.  (I don't know how to do that last part, so we might just want to implement a timer, or something similarly simple.  We'll have to figure it out, or do the genetic simulation from Lua.)

    3) Make the Python code to run genetic simulations (AKA: the hard part)

    4) Run the system for a very, very long time (at 200% speed or above)

    5) Profit.


1.  BizHawk:

    a)  Because BizHawk can turn into a non-portable install, as each user will probably want their own settings for many of the display options, I have included the BizHawk zip, and taken care to make my code self contained.  Simply unpack the BizHawk zip outside of the git directory, launch EmuHawk.exe, and select "Open ROM" from the file menu.  Load the included "Super Mario World.smc" file, and you should be playing SMW!

2.  Lua:

    a)  I have included a "Lua" folder.  You can either copy this folder into your BizHawk install, or leave it where it is.  The code I wrote is just a proof of concept; we'll need to update this code to make the emulation run on multiple files, output the results, etc.  For now, we'll move on to how to run the Lua script I wrote.

    b)  In BizHawk, open the "Tools" menu, and select "Lua Console" to open the Lua Console.  Click the "Open Script" icon from the toolbar, or from the Script menu.  (Note: because sessions and scripts are not the same, you cannot use the File -> Open Session button to open a script.)  Navigate to the Lua script I wrote, ("Mnemonic_Reader.lua") and open it.  If the script doesn't run immediately, toggle it on with the green checkbox on the toolbar.  If something shows up in the Output window, I messed up, and it's all my fault.  In theory, Mario should start playing the first level of SMW once the script begins to run.