import pygame as pg
pg.init()

def run(menu,color,size):
	"jmenu.run(menu=list,color=(r,g,b),size=int) : return str\n\
	 menu = liste de str, ex: ['choix1','choix2','choix3']\n\
	  return str de menu"

	screen = pg.display.get_surface()
	bg = screen.copy()
	mouse_rect = pg.Rect((0,0),(1,1))
	font = pg.font.get_default_font()
	font1 = pg.font.Font(font,size)
	size = font1.get_height()
	font2 = pg.font.Font(font,int(size*1.5))
	SIZE = font2.get_height()
	scr_w,scr_h = screen.get_size()
	H = font1.get_height()
	COLOR = map(lambda x:x+((255-x)*8/10),color)
	surfs = []
	rects = []
	RECTS = []
	for c in range(len(menu)):
		surfs.append((font1.render(menu[c],1,color),font2.render(menu[c],1,COLOR)))
		(w0,h0),(w1,h1) = surfs[c][0].get_size(),surfs[c][1].get_size()
		rects.append(surfs[c][0].get_rect().move(-w0/2,c*H))
		RECTS.append(rects[c].inflate(w1-w0,h1-h0))
	menu_rect = RECTS[0].unionall(RECTS)
	x = (scr_w-menu_rect.width)/2-menu_rect.x
	y = (scr_h-menu_rect.height)/2-menu_rect.y
	for c in rects+RECTS: c.move_ip(x,y)
	item = 0

	def update():
		screen.blit(bg,(0,0))
		for c in range(len(menu)):
			if c!=item :
				screen.blit(surfs[c][0],rects[c].topleft)
			screen.blit(surfs[item][1],RECTS[item].topleft)
		pg.display.flip()
	
	update()
	while True:
		e = pg.event.wait()
		mouse = mouse_rect.move(pg.mouse.get_pos())
		if e.type == pg.MOUSEMOTION or (e.type == pg.MOUSEBUTTONDOWN and e.button == 1):
			j = mouse.collidelist([RECTS[item]]+rects)
			if j>0:
				item = j-1
				update()
		elif e.type == pg.MOUSEBUTTONUP and e.button == 1 and mouse.collidelist([RECTS[item]]+rects)==0: break
		elif e.type == pg.QUIT or pg.key.get_pressed()[pg.K_ESCAPE]: return None
	screen.blit(bg,(0,0))
	pg.display.flip()
	return menu[item]

