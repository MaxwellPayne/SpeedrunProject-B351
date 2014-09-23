--#Reset|Power|#P1 Up|P1 Down|P1 Left|P1 Right|P1 Select|P1 Start|P1 Y|P1 B|P1 X|P1 A|P1 L|P1 R|#P2 Up|P2 Down|P2 Left|P2 Right|P2 Select|P2 Start|P2 Y|P2 B|P2 X|P2 A|P2 L|P2 R|
--RP|UDLRSSYBXALR|UDLRSSYBXALR|
myfile = io.open("SMW_Y1_test.txt", "r")

RAM_x = 0x000094

while true do
    savestate.load("Y1.State")
    myfile = io.open("SMW_Y1_test.txt", "r")
    if myfile then
        for line in myfile:lines() do
            -- Set the next frame's input, and display it to the screen
            joypad.setfrommnemonicstr(line)
            gui.text(0,0, line)
            -- Get Mario's position information (x position only)
            gui.text(0,24,memory.read_u16_le(RAM_x))
            -- Next frame...
            emu.frameadvance();
        end
    else
        break
    end
    myfile:close()
end