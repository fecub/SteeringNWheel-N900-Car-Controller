import pygame
import jmenu
screen = pygame.display.set_mode((750,500))
pygame.display.flip()
color = (50,255,255)
font = None
just = True
pos = ('center','center')
while pygame.event.poll().type != pygame.QUIT:
	selection = jmenu.run(['justifie centre','aligne droit','autre font','red','quit'],color,50,font=font,light=10,justify=just,pos=pos)
	if selection == 'justifie centre':
		just = True
		pos = ('center','center')
		color = (50,255,255)
		font = None
	elif selection == 'aligne droit':
		just = False
		pos = ('left','center')
		color = (50,255,255)
		font = None
	elif selection == 'red' :
		color = (150,0,0)
	elif selection == 'autre font' :
		font = '321impact.ttf'
	elif selection == 'quit' : break
