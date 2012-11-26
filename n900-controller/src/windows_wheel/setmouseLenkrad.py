'''
Created on 12.03.2011

@author: fecub
'''
import win32api
import socket, time
from win32api import GetSystemMetrics



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
	s.bind(("", 50000))
	x1 = 0
	y1 = 0
	aufloesung = GetSystemMetrics(0)/2
	print aufloesung
	while True:
		time.sleep(.01)
		daten, addr = s.recvfrom(1024)
		
		coord = daten
		coord=coord.split(',')
		x = int(coord[1])
		y = int(coord[0])
		
		y+=aufloesung
		#y*=-1
		win32api.SetCursorPos((y,300))

		# see http://msdn.microsoft.com/en-us/library/ms646260(VS.85).aspx for details
		#ctypes.windll.user32.SetCursorPos(y, 300)
		

finally:
	s.close()
