--For reference, here is the mnemonic string format:
--#Reset|Power|#P1 Up|P1 Down|P1 Left|P1 Right|P1 Select|P1 Start|P1 Y|P1 B|P1 X|P1 A|P1 L|P1 R|#P2 Up|P2 Down|P2 Left|P2 Right|P2 Select|P2 Start|P2 Y|P2 B|P2 X|P2 A|P2 L|P2 R|
--RP|UDLRSSYBXALR|UDLRSSYBXALR|

-- Functions:

function getConfig()
------------------------------------------------------------------
-- Create a key-value table of all the items in the config file --
------------------------------------------------------------------
    -- Build a table (lines) of the lines inside the config file
    lines = {}
    for line in io.lines("../Output/genConfig.config") do
        lines[#lines + 1] = line
    end
    -- Now, build the config table from the lines table
    configTable = {}
    for k,v in pairs(lines) do                          -- For every key-value (k,v) pair in lines,
        key, value = string.match(v,"([^:]+):([^:]+)")  -- Create "key" and "value" by splitting v on the ":"
        if tonumber(value) ~= nil then                  -- Check if the value is numeric
            value = tonumber(value)                     -- If it is, make it a number
        end                                             -- If it isn't, just leave it as a string
        configTable[key] = value                        -- Set the new key and value in the config table
    end
    -- TODO: create workerNumber.temp if it doesn't exist already, and use that file to get my worker number
    return configTable
end

function getNextRun()
    runNumber = runNumber + numberOfWorkers -- Increase our run number
    if runNumber >= runsPerGen then         -- Check if we need to change the generation (we're zero-indexed)
        genNumber = genNumber + 1           -- Increment the generation
        runNumber = myWorkerNumber          -- Reset the run counter
    end
    
    -- Now that we know the run and the generation, hand back the path
    return "../Output/gen" .. genNumber .. "/Runs/run" .. runNumber .. ".txt"
end

function trackMaxX(maxXPos,currentFrameNumber)
    currentXPos = memory.read_u16_le(RAM_x)
    if currentXPos > maxXPos then               -- We have a new max X
        maxXPos = currentXPos
        maxXFrameNumber = currentFrameNumber    -- Save the frame number
    end
    return maxXPos, maxXFrameNumber
end

function printToScreen(line, currentXPos)
    gui.text(0,0, line)         -- Write the current line of input to the screen
    gui.text(470,0, runNumber)  -- Write the current run number
    gui.text(0,24,currentXPos)  -- Write Mario's position information (x position only)
end

function saveResults(maxXPos, maxXFrameNumber)
-- Save the results to a file
    resultsFile = io.open("../Output/gen" .. genNumber .. "/Results/result" .. runNumber .. ".txt","w")
    resultsFile:write(maxXPos .. "," .. maxXFrameNumber)
    resultsFile:close()
end

-- Constants:
RAM_x = 0x000094

-- Settings:
configTable = getConfig()                        -- Read in the configuration file
runsPerGen = configTable["runsPerGen"]           -- How many runs we do in each generation
numberOfWorkers = configTable["numberOfWorkers"] -- How many workers are running, in total?  This value isn't zero-indexed, because we use it for our mod
genNumber = configTable["currentGenNumber"]      -- Tracks our current generation

-- Other Globals:
myWorkerNumber = 0                               -- Which worker am I?  This value is zero-indexed, because we add it to the result of the mod
runNumber = myWorkerNumber - numberOfWorkers     -- Tracks the current run

while true do   -- infinite loop (this loop is our "main")

    -- Reset our "max score" counters for each run
    maxXPos = 0
    maxXFrameNumber = 0
    currentFrameNumber = 0
    
    -- First, pick a file to load
    nextRunPath = getNextRun()
    
    -- Loop until the file opens
    runFile = io.open(nextRunPath, "r") 
    while not runFile do                    -- Loop until we open the file
        gui.text(0,0, nextRunPath)
        emu.frameadvance();                 -- Advance to the next frame while we wait, so bizHawk doesn't crash out.
        runFile = io.open(nextRunPath, "r") -- Try to open it again
    end
    
    if runFile then                                 -- If we managed to open the file...
        savestate.load("Y1.State")                  -- Load the provided savestate
        for line in runFile:lines() do              -- For every line of input provided...
            joypad.setfrommnemonicstr(line)                                     -- Set the next frame's input
            maxXPos, maxXFrameNumber = trackMaxX(maxXPos,currentFrameNumber)    -- Keep track of the maximum X position reached
            printToScreen(line, currentXPos)                                    -- Output information to the screen
            emu.frameadvance();                                                 -- Advance to the next frame
            currentFrameNumber = currentFrameNumber + 1                         -- Update the frame counter
        end
        -- The run is over, so close the run file, and write the results to a file
        runFile:close()
        saveResults(maxXPos, maxXFrameNumber)
    end
end
