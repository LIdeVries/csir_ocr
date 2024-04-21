import autopy
import time

# Move the mouse cursor to coordinates (100, 100)
autopy.mouse.move(100, 100)

# Simulate a left mouse click
autopy.mouse.click()

# Wait for 1 second
time.sleep(1)

# Simulate a right mouse click at coordinates (200, 200)
autopy.mouse.click(autopy.mouse.Button.RIGHT, (200, 200))
