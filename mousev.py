import pyautogui
print('''
#  ██████╗ ███████╗██╗     ██████╗  ██████╗ ███████╗███████╗██████╗
#  ██╔══██╗██╔════╝██║     ██╔══██╗██╔═══██╗╚══███╔╝██╔════╝██╔══██╗
#  ██████╔╝█████╗  ██║     ██║  ██║██║   ██║  ███╔╝ █████╗  ██████╔╝
#  ██╔══██╗██╔══╝  ██║     ██║  ██║██║   ██║ ███╔╝  ██╔══╝  ██╔══██╗
#  ██████╔╝███████╗███████╗██████╔╝╚██████╔╝███████╗███████╗██║  ██║
#  ╚═════╝ ╚══════╝╚══════╝╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
#
''')

# Depending on your program, pyautogui can "go rogue". As a failsafe,
# we may move the mouse to the upper left corner of the screen to
# halt the execution of a "rogue" program by setting the following:
pyautogui.FAILSAFE = True

# The location of the mouse cursor is provided as an (x,y) pair.
# This value of x and y are determined by the resolution of your
# monitor. My resolution is 2720x1024. For example:
#   The top right corner of my screen is (2720, 0)
#   The bottom left corner of my screen is (0, 1024),
#   etc.

# You can obtain the coordinates of your own computer screen here:
print(pyautogui.size())


# Getting the mouse position:
print(pyautogui.position())



