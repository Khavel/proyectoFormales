import turtle

brackets = []
def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString
    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'f':
        newstr = 'f[+f[+f-f][-f+f]][-f[-f+f][+f-f]]fffffff'   # Rule 1
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    global brackets
    for cmd in instructions:
        if cmd == 'f':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '[':
            brackets.append((aTurtle.position(),aTurtle.heading()))
        elif cmd == ']':
            pos,head = brackets.pop()
            aTurtle.penup()
            aTurtle.setposition(pos)
            aTurtle.setheading(head)
            aTurtle.pendown()
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)

def main():

    inst = createLSystem(2, "f")   # create the string
    print inst
    t = turtle.Turtle()            # create the turtle
    wn = turtle.Screen()
    t.up()
    t.back(200)
    t.down()
    t.speed(9)
    drawLsystem(t, inst, 80, 15)   # draw the picture
                                  # angle 60, segment length 5
    wn.exitonclick()

main()
