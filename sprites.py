# SPRITES
"""
Precondition: Function gets called
Postcondition: Sprite gets added
"""
def palbo_default():
    pd_rect = Rectangle(260,120)
    pd_rect.set_position(HALFWIDTH-130,HALFHEIGHT-60)
    pd_rect.set_color(Color.blue)
    add(pd_rect)
    pd_eye1 = Rectangle(20,100)
    pd_eye1.set_position(HALFWIDTH-60,HALFHEIGHT-50)
    pd_eye1.set_color(Color.red)
    add(pd_eye1)
    pd_eye2 = Rectangle(20,100)
    pd_eye2.set_position(HALFWIDTH+40,HALFHEIGHT-50)
    pd_eye2.set_color(Color.red)
    add(pd_eye2)

"""
Precondition: Function gets called
Postcondition: Sprite gets added
"""
def palbo_hat():
    ph_rect1 = Rectangle(200,25)
    ph_rect1.set_position(HALFWIDTH-100, HALFHEIGHT-85)
    ph_rect1.set_color(Color.black)
    add(ph_rect1)
    ph_rect2 = Rectangle(50,95)
    ph_rect2.set_position(HALFWIDTH-25,HALFHEIGHT-180)
    ph_rect2.set_color(Color.black)
    add(ph_rect2)

"""
Precondition: Function gets called
Postcondition: Sprite gets added
"""
def palbo_monacle():
    pm_circ1 = Circle(25)
    pm_circ1.set_position(HALFWIDTH+50,HALFHEIGHT)
    pm_circ1.set_color(Color.yellow)
    add(pm_circ1)
    pm_circ2 = Circle(15)
    pm_circ2.set_position(HALFWIDTH+50,HALFHEIGHT)
    pm_circ2.set_color(Color.red)
    add(pm_circ2)
    pm_circ3 = Circle(10)
    pm_circ3.set_position(HALFWIDTH+90,HALFHEIGHT)
    pm_circ3.set_color(Color.yellow)
    add(pm_circ3)
    pm_circ4 = Circle(10)
    pm_circ4.set_position(HALFWIDTH+115,HALFHEIGHT)
    pm_circ4.set_color(Color.yellow)
    add(pm_circ4)

"""
Precondition: Function gets called
Postcondition: Sprite gets added
"""
def palbo_watch():
    pc_circ1 = Circle(50)
    pc_circ1.set_position(get_width()-60,get_height()-60)
    pc_circ1.set_color(Color.yellow)
    add(pc_circ1)
    pc_circ2 = Circle(40)
    pc_circ2.set_position(get_width()-60,get_height()-60)
    pc_circ2.set_color(Color.brown)
    add(pc_circ2)
    pc_circ3 = Circle(14)
    pc_circ3.set_position(get_width()-75,get_height()-75)
    pc_circ3.set_color(Color.black)
    add(pc_circ3)
    pc_circ4 = Circle(8)
    pc_circ4.set_position(get_width()-40,get_height()-40)
    pc_circ4.set_color(Color.green)
    add(pc_circ4)
    pc_circ5 = Circle(14)
    pc_circ5.set_position(get_width()-43,get_height()-68)
    pc_circ5.set_color(Color.orange)
    add(pc_circ5)
    pc_circ6 = Circle(18)
    pc_circ6.set_position(get_width()-68,get_height()-42)
    pc_circ6.set_color(Color.purple)
    add(pc_circ6)
    pc_rect1 = Rectangle(20,20)
    pc_rect1.set_position(get_width()-70,get_height()-127)
    pc_rect1.set_color(Color.yellow)
    add(pc_rect1)
    pc_rect2 = Rectangle(50,15)
    pc_rect2.set_position(get_width()-85,get_height()-140)
    pc_rect2.set_color(Color.yellow)
    add(pc_rect2)

"""
Precondition: Function gets called
Postcondition: Sprite gets added
""" 
def palbo_walking_stick():
    pws_rect1 = Rectangle(15,130)
    pws_rect1.set_position(25,get_height()-160)
    pws_rect1.set_color(Color.red)
    add(pws_rect1)
    pws_rect2 = Rectangle(15,15)
    pws_rect2.set_position(25,get_height()-145)
    pws_rect2.set_color(Color.yellow)
    add(pws_rect2)
    pws_rect3 = Rectangle(15,4)
    pws_rect3.set_position(25,get_height()-130)
    pws_rect3.set_color(Color.black)
    add(pws_rect3)
    pws_rect4 = Rectangle(15,4)
    pws_rect4.set_position(25,get_height()-149)
    pws_rect4.set_color(Color.black)
    add(pws_rect4)
    pws_rect5 = Rectangle(15,4)
    pws_rect5.set_position(25,get_height()-95)
    pws_rect5.set_color(Color.black)
    add(pws_rect5)
    pws_rect6 = Rectangle(15,4)
    pws_rect6.set_position(25,get_height()-85)
    pws_rect6.set_color(Color.black)
    add(pws_rect6)
    pws_rect7 = Rectangle(15,4)
    pws_rect7.set_position(25,get_height()-75)
    pws_rect7.set_color(Color.black)
    add(pws_rect7)
    pws_rect8 = Rectangle(15,4)
    pws_rect8.set_position(25,get_height()-65)
    pws_rect8.set_color(Color.black)
    add(pws_rect8)
    pws_rect9 = Rectangle(15,4)
    pws_rect9.set_position(25,get_height()-55)
    pws_rect9.set_color(Color.black)
    add(pws_rect9)
    pws_rect10 = Rectangle(15,4)
    pws_rect10.set_position(25,get_height()-45)
    pws_rect10.set_color(Color.black)
    add(pws_rect10)

"""
Precondition: Function gets called
Postcondition: Sprite gets added
"""
def palbo_body():
    pb_rect1 = Rectangle(260,20)
    pb_rect1.set_position(HALFWIDTH-130,HALFHEIGHT+60)
    pb_rect1.set_color(Color.black)
    add(pb_rect1)
    pb_rect2 = Rectangle(130,200)
    pb_rect2.set_position(HALFWIDTH-65,HALFHEIGHT+60)
    pb_rect2.set_color(Color.black)
    add(pb_rect2)
    pb_rect3 = Rectangle(100,20)
    pb_rect3.set_position(40,get_height()-120)
    pb_rect3.set_color(Color.black)
    add(pb_rect3)

"""
Precondition: Function gets called
Postcondition: Sprite gets added
"""
def palbo_estate_crest():
    pec_circ1 = Circle(20)
    pec_circ1.set_position(HALFWIDTH,HALFHEIGHT-90)
    pec_circ1.set_color(Color.green)
    add(pec_circ1)
    pec_circ2 = Circle(18)
    pec_circ2.set_position(HALFWIDTH,HALFHEIGHT-90)
    pec_circ2.set_color(Color.red)
    add(pec_circ2)
    pec_circ3 = Circle(16)
    pec_circ3.set_position(HALFWIDTH,HALFHEIGHT-90)
    pec_circ3.set_color(Color.orange)
    add(pec_circ3)
    pec_circ4 = Circle(14)
    pec_circ4.set_position(HALFWIDTH,HALFHEIGHT-90)
    pec_circ4.set_color(Color.yellow)
    add(pec_circ4)
    pec_circ5 = Circle(12)
    pec_circ5.set_position(HALFWIDTH,HALFHEIGHT-90)
    pec_circ5.set_color(Color.blue)
    add(pec_circ5)
    pec_circ6 = Circle(10)
    pec_circ6.set_position(HALFWIDTH,HALFHEIGHT-90)
    pec_circ6.set_color(Color.purple)
    add(pec_circ6)
    pec_circ7 = Circle(8)
    pec_circ7.set_position(HALFWIDTH,HALFHEIGHT-90)
    pec_circ7.set_color(Color.brown)
    add(pec_circ7)
    pec_circ8 = Circle(6)
    pec_circ8.set_position(HALFWIDTH,HALFHEIGHT-90)
    pec_circ8.set_color(Color.white)
    add(pec_circ8)
    pec_circ9 = Circle(4)
    pec_circ9.set_position(HALFWIDTH,HALFHEIGHT-90)
    pec_circ9.set_color(Color.black)
    add(pec_circ9)
    pec_circ10 = Circle(2)
    pec_circ10.set_position(HALFWIDTH,HALFHEIGHT-90)
    pec_circ10.set_color(Color.red)
    add(pec_circ10)
 
"""
Precondition: Function gets called
Postcondition: Sprite gets added
"""   
def palbo_tie():
    pt_rect1 = Rectangle(20,150)
    pt_rect1.set_position(HALFWIDTH-10,HALFHEIGHT+60)
    pt_rect1.set_color(Color.red)
    add(pt_rect1)
    pt_rect2 = Rectangle(20,10)
    pt_rect2.set_position(HALFWIDTH-10,HALFHEIGHT+110)
    pt_rect2.set_color(Color.white)
    add(pt_rect2)
    pt_rect3 = Rectangle(20,10)
    pt_rect3.set_position(HALFWIDTH-10,HALFHEIGHT+130)
    pt_rect3.set_color(Color.white)
    add(pt_rect3)
    pt_rect4 = Rectangle(20,10)
    pt_rect4.set_position(HALFWIDTH-10,HALFHEIGHT+150)
    pt_rect4.set_color(Color.white)
    add(pt_rect4)
    pt_rect5 = Rectangle(20,10)
    pt_rect5.set_position(HALFWIDTH-10,HALFHEIGHT+170)
    pt_rect5.set_color(Color.white)
    add(pt_rect5)
    pt_rect6 = Rectangle(20,10)
    pt_rect6.set_position(HALFWIDTH-10,HALFHEIGHT+190)
    pt_rect6.set_color(Color.white)
    add(pt_rect6)

"""
Precondition: Function gets called
Postcondition: Sprite gets added
"""
def palbo_glasses():
    pg_circ1 = Circle(25)
    pg_circ1.set_position(HALFWIDTH-50,HALFHEIGHT)
    pg_circ1.set_color(Color.black)
    add(pg_circ1)
    pg_circ2 = Circle(15)
    pg_circ2.set_position(HALFWIDTH-50,HALFHEIGHT)
    pg_circ2.set_color(Color.red)
    add(pg_circ2)
    pg_circ3 = Circle(25)
    pg_circ3.set_position(HALFWIDTH+50,HALFHEIGHT)
    pg_circ3.set_color(Color.black)
    add(pg_circ3)
    pg_circ4 = Circle(15)
    pg_circ4.set_position(HALFWIDTH+50,HALFHEIGHT)
    pg_circ4.set_color(Color.red)
    add(pg_circ4)
    pg_rect = Rectangle(63,15)
    pg_rect.set_position(HALFWIDTH-35,HALFHEIGHT-5)
    pg_rect.set_color(Color.black)
    add(pg_rect)
