import simplegui
x = 5
y = 5
z = 600
a = 0
def draw_handler(canvas):
    global x, y ,z
    colorR = 'RGB(255,0,0)'
    colorG = 'RGB(0,255,0)'
    colorB = 'RGB(0,0,255)'
    
    x += 5
    y += 5
    z -= 5
    if x >= 600:
        x = 5
    if y >= 600:
        y = 5
    if z <= 0:
        z = 600

    
    
    canvas.draw_circle((x,y),50,2,'white','white')
    
    canvas.draw_circle((x,z),50,2,'white','yellow')
    
    canvas.draw_polygon([(x,a+590),(x+50,a+590),(x+50,a+640),(x,a+640)],5,'white',colorG)
    
    canvas.draw_polygon([(x,a+530),(x+50,a+530),(x+50,a+580),(x,a+580)],5,'white',colorG)
    
    canvas.draw_polygon([(x,a+480),(x+50,a+470),(x+50,a+520),(x,a+520)],5,'white',colorG)
    
    canvas.draw_polygon([(x,a+420),(x+50,a+420),(x+50,a+470),(x,a+470)],5,'white',colorG)
    
    canvas.draw_polygon([(x,a+360),(x+50,a+360),(x+50,a+410),(x,a+410)],5,'white',colorG)
    
    canvas.draw_polygon([(x,a+300),(x+50,a+300),(x+50,a+350),(x,a+350)],5,'white',colorG)
    
    canvas.draw_polygon([(x,a+240),(x+50,a+240),(x+50,a+290),(x,a+290)],5,'white',colorG)
    
    canvas.draw_polygon([(x,a+180),(x+50,a+180),(x+50,a+230),(x,a+230)],5,'white',colorG)
    
    canvas.draw_polygon([(x,a+120),(x+50,a+120),(x+50,a+170),(x,a+170)],5,'white',colorG)
    
    canvas.draw_polygon([(x,a+60),(x+50,a+60),(x+50,a+110),(x,a+110)],5,'white',colorG)
    
    canvas.draw_polygon([(x,a),(x+50,a),(x+50,a+50),(x,a+50)],5,'white',colorG)
   
    canvas.draw_circle((x,150),50,2,'white','red')
    
    canvas.draw_circle((x,450),50,2,'white','purple')
    
    canvas.draw_circle((x,300),50,2,'white','green')
    
    
    
    
frame = simplegui.create_frame('Testing', 600, 600)
frame.set_canvas_background("Black")
frame.set_draw_handler(draw_handler)
frame.start()



