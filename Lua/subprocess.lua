local rundatafile = 'SMW_Y1_test.txt'

local file = assert(io.popen('python heavylifting.py SMW_Y1_test.txt', 'r'))
local output = file:read('*all')
file:close()
print('Lua sees:')
print(output)
print("Wow that was cool. Now I have all that data stored \
in my output variable I can communicate with the \
emulator again.")
