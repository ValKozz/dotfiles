import subprocess
import sys

FILE = '/sys/class/backlight/intel_backlight/brightness'

DESC =''' 
-dec [Value]  Decrease brigthness by given value.
-inc [Value]    Increase by given value.
'''

MAX_BRIGHTNESS = 700
MIN_BRIGHTNESS = 10

OP_ARG = sys.argv[1]

if OP_ARG != '-inc' and OP_ARG != '-dec':
    print(OP_ARG)
    print('ERROR: Invalid operational argument')
    print(DESC)
    sys.exit(1)

try:
    ARG_VALUE = int(sys.argv[2])
except ValueError:
    print('ERROR: Arguments regarding bightness value can only be Numeric.')
    print(DESC)
    sys.exit(1)


with open(FILE, 'r') as file:
    light_level = int(file.read())


    if OP_ARG == '-dec':
        if light_level - ARG_VALUE > MIN_BRIGHTNESS:
            if light_level < 30:
                light_level -= 10
            else:
                light_level -= ARG_VALUE
                print(f'\n{light_level}')

    elif OP_ARG == '-inc':
        if light_level + ARG_VALUE < MAX_BRIGHTNESS:
            light_level += ARG_VALUE
            print(f'\n{light_level}')
        else:
            light_level = MAX_BRIGHTNESS
        
with open(FILE, 'w') as file:
    file.write(str(light_level) + '\n')

# subprocess.call(["killall", "notify-osd"])
# subprocess.call(["notify", f"{light_level}"])
