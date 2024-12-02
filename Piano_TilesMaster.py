import pyautogui
import win32api, win32con
import keyboard
from time import sleep

color = (0, 0, 0)

##web https://gameforge.com/en-US/littlegames/magic-piano-tiles/

# X: 343 Y: 583
# X: 423 Y: 583
# X: 513 Y: 583
# X: 608 Y: 583
			
#Start X: 468 Y:540

pyautogui.click(468, 540)

def click(x, y):
	win32api.SetCursorPos((x, y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
	sleep(0.02)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

while keyboard.is_pressed('q') == False:
	screen = pyautogui.screenshot()
	ad = screen.getpixel((618, 678))
	if ad[0] == 0:
		click(731, 666)
	button_1 = screen.getpixel((343, 583))
	if button_1[0] == 0:
		click(343, 583)
	button_2 = screen.getpixel((423, 583))
	if button_2[0] == 0:
		click(423, 583)
	button_3 = screen.getpixel((513, 583))
	if button_3[0] == 0:
		click(513, 583)
	button_4 = screen.getpixel((608, 583))
	if button_4[0] == 0:
		click(608, 583)