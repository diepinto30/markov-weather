import graphics
from graphics import *
import random

precip_transitions = [ ["NN", "NL", "NH"], ["LN", "LL", "LH"], ["HN", "HL", "HH"] ]
precip_transition_matrix = [ [.7, .2, .1], [.4, .4, .2], [.4, .3, .3] ]

temp_transitions = [ ["HH", "HM", "HC"], ["MH", "MM", "MC"], ["CH", "CM", "CC"] ]
sept_transition_matrix = [ [.5, .4, .1], [.4, .5, .1], [.5, .3, .2] ]
oct_transition_matrix = [ [.4, .4, .2], [.3, .5, .2], [.3, .5, .2] ]
nov_transition_matrix = [ [.3, .3, .4], [.2, .3, .5], [.1, .3, .6] ]
dec_transition_matrix = [ [.2, .2, .6], [.1, .2, .7], [.1, .1, .8] ]

rain_state = "none"
temp_state = "hot"

outside_count = 0
prev_outside_count = 0

def draw_text(win) :
    
    format_month_text(win, "sept", 80)
    format_month_text(win, "oct", 150)
    format_month_text(win, "nov", 220)
    format_month_text(win, "dec", 290)
    
    format_day_text(win)
    
    format_key(win, 60)
    format_key(win, 130)
    format_key(win, 200)
    format_key(win, 270)
    
    Line(Point(45,45),Point(45,325)).draw(win)
    Line(Point(45, 35), Point(655, 35)).draw(win)
    Line(Point(655,45), Point(655,325)).draw(win)
    
    return

def format_month_text(win, month, y) :
    
    month = Text(Point(25, y), month)
    month.setFace("helvetica")
    month.setSize(12)
    
    month.draw(win)  
    
    return

def format_day_text(win) :
    
    day10 = Text(Point(240, 45), "10")
    day10.setFace("helvetica")
    day10.setSize(8)
    
    day20 = Text(Point(440, 45), "20")
    day20.setFace("helvetica")
    day20.setSize(8)
    
    day30 = Text(Point(640, 45), "30")
    day30.setFace("helvetica")
    day30.setSize(8)    
    
    day10.draw(win)
    day20.draw(win)
    day30.draw(win)
    
    return

def format_key(win, y) :
    
    temp = Text(Point(668.5, y+4), "temp")
    temp.setSize(9)
    temp.draw(win)
    
    rain = Text(Point(665.5, y+24), "rain")
    rain.setSize(9)
    rain.draw(win)
    
    outside = Text(Point(680.5, y+44), "good day?")
    outside.setSize(9)
    outside.draw(win)
    
    return
                     
def draw(win) :
    global prev_outside_count
    global outside_count
    
    temp = temp_state
    rain = rain_state   
    
    sept_x = 50
    oct_x = 50
    nov_x = 50
    dec_x = 50
    
    sept_y = 100
    oct_y = 170
    nov_y = 240
    dec_y = 310
    
    # for september
    for i in range(0, 30) :
        
        draw_outside(win, temp, rain, sept_x, sept_y)        
    
        temp = draw_temp(win, "September", sept_x)
            
        rain = draw_precip(win, "September", sept_x)
        
        sept_x += 20
     
    # for october       
    for i in range(0, 30) :
        
        draw_outside(win, temp, rain, oct_x, oct_y)                

        temp = draw_temp(win, "October", oct_x)
            
        rain = draw_precip(win, "October", oct_x)     
        
        oct_x += 20 
            
    # for november
    for i in range(0, 30) :
        
        draw_outside(win, temp, rain, nov_x, nov_y)                
        
        temp = draw_temp(win, "November", nov_x)
            
        rain = draw_precip(win, "November", nov_x)            
        
        nov_x += 20   
       
    # for december     
    for i in range(0, 30) :
        
        draw_outside(win, temp, rain, dec_x, dec_y)    
        
        temp = draw_temp(win, "December", dec_x)
            
        rain = draw_precip(win, "December", dec_x) 
        
        dec_x += 20           

    outside_count -= prev_outside_count
    
    white_out = Rectangle(Point(0,0), Point(300,30))
    white_out.setFill("beige")
    white_out.setOutline("beige")
    white_out.draw(win)
    
    outside = Text(Point(160,20), "Nice days in the fall: " + str(outside_count))
    outside.setFace("helvetica")
    outside.setSize(20)
    outside.draw(win)
    
    prev_outside_count = outside_count
    
    return

def draw_outside(win, temp, rain, month_x, month_y) :
    global outside_count
    
    outside = Circle(Point(month_x+10, month_y), 10)
    
    if (temp == "hot" and rain == "none") :
        outside.setFill(color_rgb(0, 150, 0))
        outside_count += 1
        
    elif (temp == "hot" and rain == "light") :
        outside.setFill(color_rgb(0, 150, 0))
        outside_count += 1
        
    elif (temp == "med" and rain == "none") :
        outside.setFill(color_rgb(0, 150, 0))
        outside_count += 1
        
    else :
        outside.setFill("white")
    
    outside.draw(win)    
    
    return

def draw_temp(win, month, month_x) :
    global temp_state
    
    transitions = temp_transitions
    
    if month == "September" :
        temp = Circle(Point((month_x+10),60), 10)
        transition_matrix = sept_transition_matrix    
            
    elif month == "October" :
        temp = Circle(Point((month_x+10),130), 10)
        transition_matrix = oct_transition_matrix
            
    elif month == "November" :
        temp = Circle(Point((month_x+10),200), 10)
        transition_matrix = nov_transition_matrix
            
    elif month == "December" :
        temp = Circle(Point((month_x+10),270), 10) 
        transition_matrix = dec_transition_matrix
        
    if temp_state == "hot" :
        temp.setFill(color_rgb(255, 50, 0))
        transition = calc_transition(0, transition_matrix, transitions) 
        
        if (transition == "HH") :
            temp_state = "hot"
            
        if (transition == "HM") :
            temp_state = "med"
            
        if (transition == "HC") :
            temp_state = "cold"        
        
    elif temp_state == "med" :
        temp.setFill(color_rgb(255, 160, 0))
        transition = calc_transition(1, transition_matrix, transitions)     
        
        if (transition == "MH") :
            temp_state = "hot"
            
        if (transition == "MM") :
            temp_state = "med"
            
        if (transition == "MC") :
            temp_state = "cold"        
        
    elif temp_state == "cold" :
        temp.setFill(color_rgb(0, 180, 255))
        transition = calc_transition(2, transition_matrix, transitions)  
        
        if (transition == "CH") :
            temp_state = "hot"
            
        if (transition == "CM") :
            temp_state = "med"
            
        if (transition == "CC") :
            temp_state = "cold"        
    
    temp.draw(win)
        
    return temp_state    

def draw_precip(win, month, month_x) :
    global rain_state
    transition_matrix = precip_transition_matrix
    transitions = precip_transitions
    
    if month == "September" :
        precip = Circle(Point((month_x+10),80), 10)
        
    elif month == "October" :
        precip = Circle(Point((month_x+10),150), 10)
        
    elif month == "November" :
        precip = Circle(Point((month_x+10),220), 10)
        
    elif month == "December" :
        precip = Circle(Point((month_x+10),290), 10)
    
    # if no current rain, chances are avg for month
    if rain_state == "none" :
        
        precip.setFill(color_rgb(255,255,255))
        # get random transition
        transition = calc_transition(0, transition_matrix, transitions)
        
        if (transition == "NN") :
            rain_state = "none"
            
        if (transition == "NL") :
            rain_state = "light"
            
        if (transition == "NH") :
            rain_state = "heavy"
                    
    elif rain_state == "light" :
        
        precip.setFill(color_rgb(0,100,250))
        transition = calc_transition(1, transition_matrix, transitions)
        
        if (transition == "LN") :
            rain_state = "none"
            
        if (transition == "LL") :
            rain_state = "light"
            
        if (transition == "LH") :
            rain_state = "heavy"
    
    elif rain_state == "heavy" :
        
        precip.setFill(color_rgb(0,50,150))
        transition = calc_transition(2, transition_matrix, transitions)
        
        if (transition == "HN") :
            rain_state = "none"
            
        if (transition == "HL") :
            rain_state = "light"
            
        if (transition == "HH") :
            rain_state = "heavy"
        
    precip.draw(win)

    return rain_state

def calc_transition(state, transition_matrix, transitions) :
    
    random_num = random.randint(1,10)

    if (random_num <= 10*transition_matrix[state][0]) :
        transition = transitions[state][0]
        
    elif (random_num <= 10*transition_matrix[state][1] + 10*transition_matrix[state][0]) :
        transition = transitions[state][1]    
            
    else :   
        transition = transitions[state][2]        
    
    return transition
    
def main():
    
    win = GraphWin('window', 710, 350)   
    win.setBackground("beige")

    exit = 1;
    while(exit) :
        
        draw_text(win)
        draw(win)

        if(win.checkMouse()) :
            exit = 0

    win.close()
    
main()
    