def is_inside(x,y,x0,y0,width,height):
    x1 = x0 + width
    y1 = y0 + height
    if x >= x0 and x <= x1 and y >= y0 and y <= y1:
        result = True
    else:
        result = False
    print(result)

# is_inside(100,120,140,60,80,100)