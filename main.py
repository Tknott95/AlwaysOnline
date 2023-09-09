
import time

# NOT USING MOUSE
import mouse
# mouse.move(100, 100, absolute=False, duration=0.2) - works without sudo
# mouse wants sudo access to do things like mouse.click('left') - wants sudo which is bad
# instead I use pytautogui.

import pyautogui
pyautogui.click(100, 100)

while(True):
  _pos = mouse.get_position()
  if _pos != (100, 100):
    pyautogui.click(100, 100)
  else:
    pyautogui.click(400, 400)

  time.sleep(270)
