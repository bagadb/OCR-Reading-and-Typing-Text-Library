
import time
import pyautogui
import pytesseract as ias

from PIL import Image
from pynput.keyboard import Key , Controller
from pynput.mouse import Listener

class bagad:

	def __init__(self):
		print "i n s t a n t i a t e d"
		pass

	def getRegion(self):
		count = [0]
		corners = [[0,0], [0,0]]
		print "1. Click Topleft corner of desired Region"
		print "2. Click Lower Right corner of desired region"				
		def on_click(x,y,button,pressed):
			count[0] += 1
			if count[0] == 2:
				corners[0] = list(pyautogui.position())
				pass
			if count[0] == 4:
				corners[1] = list([pyautogui.position()[0] - corners[0][0],pyautogui.position()[1] - corners[0][1]])
				print p				
				listener.stop()
				pass

		with Listener(on_click=on_click) as listener:
			listener.join()
		
		self.Image = pyautogui.screenshot(region=p[0]+p[1])
		pass

	def readText(self):
		unformatted_text = ias.image_to_string(self.Image , lang = 'eng')
		for c in unformatted_text:
			unformatted_text.replace('\n',' ')[0:]
		self.extracted_text = unformatted_text
		pass

	def typeText(self):
		for c in self.extracted_text:
			keyboard.press(c)
			keyboard.release(c)
			time.sleep(0.1)
		pass

	def printText(self):
		print self.extracted_text
		pass

	def showImage(self):
		self.Image.show()
		pass

