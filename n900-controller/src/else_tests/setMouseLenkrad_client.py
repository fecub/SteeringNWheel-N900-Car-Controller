'''
Created on 25.11.2010

@author: fecub
'''

import socket, time
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#ip = raw_input("IP-adresse: ")
#ip='1.1.1.5'
ip = '192.168.2.14'
#ip = '10.12.41.175'
while True:
	f=open("/sys/class/i2c-adapter/i2c-3/3-001d/coord", 'r' )
	x, y, z = [int(w) for w in f.readline().split()]
	f.close()

	#print 'x = %d' % x
	#print 'y = %d' % y
	
	x1=(x+378)
	y1=(y+150)
	#print 'z = %d' % z
	x1=(x)
	y1=(y)

	coordi = str(x1) +','+ str(y1) +','+str(z)
	time.sleep(0.1)
	s.sendto(coordi, (ip, 50000))

s.close()

