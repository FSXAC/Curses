import curses,math
def c(s,u,v,r):
	def f(u,v,x,y):
		x,y=int(x),int(y)
		a,b=[y,y,-y,-y,x,x,-x,-x],[x,-x,x,-x,y,-y,y,-y]
		for p in zip(a,b):s.addstr(v+p[0],u+p[1],'*')
	x,y,d=0,r,3-2*r
	f(u,v,x,y)
	while y>=x:
		x+=1
		if d>0:y,d=y-1,d+4*(x-y)+10
		else:d+=4*x+6
		f(u,v,x,y)
	s.refresh()
def m(s):
	i=0
	curses.curs_set(0)
	s.nodelay(True)
	while True:
		key=s.getch()
		if key==ord('q'):break
		h,w = s.getmaxyx()
		s.clear()
		c(s,w//2,h//2,10*(math.sin(i*0.05)+1)+5)
		i+=1
curses.wrapper(m)








