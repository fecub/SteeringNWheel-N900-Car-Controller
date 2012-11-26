
'''
Created on 12.03.2011

@author: fecub
'''


import socket
import win32api, win32con

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
keycode = None
try:
	s.bind(("", 49999))

	
	while True:
		daten, addr = s.recvfrom(1024)
		if (daten != 'ende'):
			keycode = daten
		if keycode == '111':
			# KEYUP
			win32api.keybd_event(win32con.VK_UP,0,0,0)
		if keycode == '116':
			# KEYDOWN
			win32api.keybd_event(win32con.VK_DOWN,0,win32con.KEYEVENTF_EXTENDEDKEY,0)
		if keycode == '117':
			# A
			win32api.keybd_event(0x41 ,0 ,win32con.KEYEVENTF_EXTENDEDKEY ,0)
		if keycode == '118':
			# Y
			win32api.keybd_event(0x59 ,0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
		if keycode == '119':
			# SPACE
			win32api.keybd_event(win32con.VK_SPACE,0,win32con.KEYEVENTF_EXTENDEDKEY,0)
		if daten == 'ende':
			if keycode != None:
				keycode = None
				win32api.keybd_event(win32con.VK_UP,0,win32con.KEYEVENTF_KEYUP,0)
				win32api.keybd_event(win32con.VK_DOWN,0,win32con.KEYEVENTF_KEYUP,0)
				win32api.keybd_event(0x41,0,win32con.KEYEVENTF_KEYUP,0)
				win32api.keybd_event(0x59,0,win32con.KEYEVENTF_KEYUP,0)
				win32api.keybd_event(win32con.VK_SPACE,0,win32con.KEYEVENTF_KEYUP,0)
			daten = None
			continue
finally:
	s.close()
