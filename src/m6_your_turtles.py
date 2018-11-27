"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Thomas Hoevener.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
Dante = rg.SimpleTurtle('turtle')
Dante.pen = rg.Pen('purple',5)
Dante.speed = 10

for k in range(8):

    Dante.draw_regular_polygon(7,100)
    Dante.right(45)
    Dante.forward(30)

Alex = rg.SimpleTurtle('triangle')
Alex.pen = rg.Pen('blue',2)
Alex.speed = 20
Alex.pen_up()
Alex.forward(200)
Alex.left(90)
Alex.forward(50)
Alex.pen_down()

for k in range(9):
    Alex.pen_up()
    Alex.left(40)
    Alex.forward(50)
    Alex.pen_down()
    for k in range(7):
        Alex.pen_up()
        Alex.forward(15)
        Alex.pen_down()
        Alex.draw_circle(5)

window.close_on_mouse_click()
