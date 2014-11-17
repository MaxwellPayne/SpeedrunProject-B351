--For reference, here is the mnemonic string format:
--#Reset|Power|#P1 Up|P1 Down|P1 Left|P1 Right|P1 Select|P1 Start|P1 Y|P1 B|P1 X|P1 A|P1 L|P1 R|#P2 Up|P2 Down|P2 Left|P2 Right|P2 Select|P2 Start|P2 Y|P2 B|P2 X|P2 A|P2 L|P2 R|
--RP|UDLRSSYBXALR|UDLRSSYBXALR|

-- Constants:
RAM_x = 0x000094

-- Settings:
-- TODO: Load in settings from a central file?
runsPerGen = 2      -- How many runs we do in each generation (placeholder value is 2)
numberOfWorkers = 1 -- How many workers are running, in total?  This value isn't zero-indexed, because we use it for our mod
myWorkerNumber = 0  -- Which worker am I?  This value is zero-indexed, because we add it to the result of the mod

-- Globals:
genNumber = 0                                   -- Tracks our current generation
runNumber = myWorkerNumber - numberOfWorkers    -- Tracks the current run

while true do   -- infinite loop

    maxXPos = 0     -- Reset our "score" counter
    currentXPos = 0
    maxXFrameNumber = 0

    -- First, pick a file to load
    runNumber = runNumber + numberOfWorkers -- Increase our run number
    if runNumber >= runsPerGen then         -- Check if we need to change the generation (we're zero-indexed)
        genNumber = genNumber + 1           -- Increment the generation
        runNumber = myWorkerNumber          -- Reset the run counter
    end
    
    -- Now we know the run and the generation, so try to open the correct file
    nextRunPath = "../Output/gen" .. genNumber .. "/Runs/run" .. runNumber .. ".txt"
    runFile = io.open(nextRunPath, "r") 
    
    while not runFile do                    -- Loop until we open the file
        gui.text(0,0, nextRunPath)
        emu.frameadvance();                 -- Advance to the next frame while we wait, so bizHawk doesn't crash out.
        runFile = io.open(nextRunPath, "r") -- Try to open it again
    end
    
    if runFile then                                      -- If we managed to open the file...
        savestate.load("Y1.State")                      -- Load the provided savestate
        for line in runFile:lines() do                   -- For every line of input provided...
            joypad.setfrommnemonicstr(line)             -- Set the next frame's input, and display it to the screen
            gui.text(0,0, line)                         -- Write the current line of input to the screen
            
            -- Keep track of the maximum X position reached
            currentXPos = memory.read_u16_le(RAM_x)
            if currentXPos > maxXPos then           -- We have a new max X
                maxXPos = currentXPos
                maxXFrameNumber = emu.framecount()  -- Remember to save the frame number!
            end
            
            gui.text(0,24,currentXPos)                  -- Write Mario's position information (x position only)
            emu.frameadvance();                         -- Advance to the next frame...
        end
        runFile:close()                                      -- The run is over, so close the file
        
        -- Write the results to a file
        resultsFile = io.open("../Output/gen" .. genNumber .. "/Results/result" .. runNumber .. ".txt","w")
        resultsFile:write(maxXPos .. "," .. maxXFrameNumber)
        resultsFile:close()
        
    end
    
end