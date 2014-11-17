SpeedrunProject-B351
====================

Done:

    1) Decide how we will format input to the Mnemonic Reader, and make the reader accept this format.
        
        We are using the simple Mnemonic format, with no alterations.  Any complexity or simplification will happen inside of python, and only inside of python.

    2) Decide on, and implement a feedback system, so that our Python code (which does the hard AI work) knows what worked and what didn't, and the Lua script knows when to run.  (I don't know how to do that last part, so we might just want to implement a timer, or something similarly simple.  We'll have to figure it out, or do the genetic simulation from Lua.)
    
        Each Lua worker will drop a resultX.txt file for every run into the generation's Results folder, and condenseRuns() (inside of condenseRuns.py) can turn these text files into a .csv (allResults.csv) which can be read by the genetic simulation code.  In addition to the .csv, condenseRuns() will return a list of strings of all of the results.  The text files are formatted as maximumX,FrameCountWhenReached.  The list of strings returned by condenseRuns() (and the .csv) is formatted as runNumber,maximumX,FrameCountWhenReached. The Lua workers will wait for runs to be generated, and do not have to be told when to run.

TODO:

    3) Make the Python code to run genetic simulations (AKA: the hard part)

    4) Run the system for a very, very long time (at 200% speed or above)

    5) Profit.


1.  BizHawk:

    a)  Because BizHawk can turn into a non-portable install, as each user will probably want their own settings for many of the display options, I have included the BizHawk zip, and taken care to make my code self contained.  Simply unpack the BizHawk zip outside of the git directory, (or in a BizHawk directory, which is ignored) launch EmuHawk.exe, and select "Open ROM" from the file menu.  Load the included "Super Mario World.smc" file, and you should be playing SMW!

2.  Lua:

    a)  I have included a "Lua" folder.  You can either copy this folder into your BizHawk install, or leave it where it is.

    b)  In BizHawk, open the "Tools" menu, and select "Lua Console" to open the Lua Console.  Click the "Open Script" icon from the toolbar, or from the Script menu.  (Note: because sessions and scripts are not the same, you cannot use the File -> Open Session button to open a script.)  Navigate to the Lua script I wrote, ("Mnemonic_Reader.lua") and open it.  If the script doesn't run immediately, toggle it on with the green checkbox on the toolbar.  If something shows up in the Output window, I messed up, and it's all my fault.  In theory, Mario should start playing the first level of SMW, based on the generated runs in the Output directory, once the script begins to run.

3.   Python:
     
     a) In order to make our lives substantially easier, we should be able to use open source python packages registered in the Python Package Index (PyPI). This is pretty simple once you install pip, Python's package manager, on your machine. Follow the instructions [here](http://pip.readthedocs.org/en/latest/installing.html) to install pip. These directions are geared more towards Linux/OSX, though, so if you are a Windows user you can use these more detailed [Windows-specific](http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows) instructions. After installing pip and making sure that your Python installation's `Scripts` directory is on your PATH, you should be able to run pip from the command line. I'm keeping track of all the package dependencies we use in the "requirements.txt" file so that you can simply run `pip install -r requirements.txt` and keep your Python packages in sync with everyone else in the project. 
