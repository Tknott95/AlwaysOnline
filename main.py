import mouse
import time

while(True):
  _pos = mouse.get_position()
  if _pos != (100, 100):
    mouse.move(100, 100, absolute=False, duration=0.2)
    mouse.click('left')
  else:
    mouse.move(400, 400, absolute=False, duration=0.2)
    mouse.click('left')

  time.sleep(2400)

