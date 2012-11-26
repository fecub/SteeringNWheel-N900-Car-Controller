'''
Created on 13.03.2011

@author: fecub
'''
import Xlib.display
import Xlib.X
import Xlib.XK
import Xlib.error
import Xlib.ext.xtest

display = Xlib.display.Display()
def mouse_click(button): #button= 1 left, 2 middle, 3 right
	Xlib.ext.xtest.fake_input(display,Xlib.X.ButtonPress, button)
	display.sync()
	Xlib.ext.xtest.fake_input(display,Xlib.X.ButtonRelease, button)
	display.sync()
	
def main():
	mouse_click(2)
	
main()