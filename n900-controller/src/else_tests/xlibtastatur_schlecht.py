import Xlib.display
import Xlib.X
import Xlib.XK
import Xlib.error
import time

display = Xlib.display.Display()

screen = display.screen()
root = screen.root
pointer=root.query_pointer() #Get info like window where pointer is on and pointer position
window=pointer.child

ev_d = dict(
time = 0, # Time of the event (useful for double-clicks for mouse events)
root = root,
window = pointer.child, #The window where is the
pointer
same_screen = 1,child = Xlib.X.NONE,root_x = pointer.root_x,root_y = pointer.root_y,event_x = pointer.win_x,event_y = pointer.win_y,state = Xlib.X.NONE,detail =Xlib.X.Button1 )

ev2_dict = ev_d.copy()
ev2_dict['state'] = Xlib.X.Button1  # that is ButtonXMask
ev=Xlib.protocol.event.ButtonPress(**ev_d)
ev2=Xlib.protocol.event.ButtonRelease(**ev2_dict)

display.send_event(Xlib.X.PointerWindow,ev)

display.sync() # Send the inserted events
time.sleep(500/1000)
display.send_event(Xlib.X.PointerWindow,ev2)
display.sync()

