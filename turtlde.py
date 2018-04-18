class turtle:

    def __init__(self):
        self.pos = [0,0,0]

    def avanza(x,y,z):
        self.pos = [self.pos[0]+x,self.pos[1]+y,self.pos[2]+z]
        return [x,y,z]

    def retrocede(x,y,z):
        self.pos = [self.pos[0]-x,self.pos[1]-y,self.pos[2]-z]
        return [x,y,z]
