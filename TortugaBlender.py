import random


class TortugaBlender:

    def __init__(self):
        self.verts  = []
        self.edges  = []
        self.faces  = []
        self.vverts = []

    def aplicarRegla(self,simbolo):
        if simbolo == "f":
            rand = random.randrange(1, 5)
            if rand == 1.0:
                return "*f[+f[++f-f]][-f[-f+f][+f-f]]ff"
            elif rand == 2.0:
                return "+*f[+f[++f-f][-f+f]][-f]fff"
            elif rand == 3.0:
                return "fff--f/"
            elif rand == 4.0:
                return "*f[+f[-f+f]][+f-f]fff"
            elif rand == 5.0:
                return "*f++"
        else:
            return simbolo

    def aplicarProducciones(self,palabra):

        nuevaPalabra = ""
        for simbolo in palabra:
            nuevaPalabra = nuevaPalabra + self.aplicarRegla(simbolo)

        return nuevaPalabra

    def makePoly(self,cadena):
        step = 0.5
        stepV = 0.4
        orientacion = [step,step,stepV]
        pos = [0,0,0]
        brackets = []
        ant = 0
        vertCont = 0
        trasBracket = False
        posPre = []
        cAnt = 'x'

        for c in cadena:

            if c == 'f':
                v = [pos[0] + orientacion[0],pos[1] + orientacion[1],pos[2] + orientacion[2]]
                pos = v
                if not v in self.verts:
                    self.verts.append(v)
                    vertCont = vertCont + 1
                    if not trasBracket:
                        self.edges.append((vertCont-1,vertCont-2))
                    else:
                        trasBracket = False
                        self.edges.append((vertCont-1,ant))

            #Guarda la posicion
            elif c == '[':
                brackets.append((pos,orientacion))
                if not cAnt == ']':
                    posPre.append(vertCont-1)
                else:
                    posPre.append(ant)


            #Retorna a la ultima posicion guardada
            elif c == ']':
                pos_brackets,head_brackets = brackets.pop()
                pos = pos_brackets
                orientacion = head_brackets
                trasBracket = True
                ant = posPre.pop()
                self.vverts.append(vertCont-1)


            elif c == '+':
                dirX = orientacion[0]
                dirY = orientacion[1]
                dirZ = orientacion[2]
                if dirX == 0 and dirY == step:
                    orientacion = [step,step,dirZ]

                elif dirX == step and dirY == step:
                    orientacion = [step,0,dirZ]

                elif dirX == step and dirY == 0:
                    orientacion = [step,-step,dirZ]

                elif dirX == step and dirY == -step:
                    orientacion = [0,-step,dirZ]

                elif dirX == 0 and dirY == -step:
                    orientacion = [-step,-step,dirZ]

                elif dirX == -step and dirY == -step:
                    orientacion = [-step,0,dirZ]

                elif dirX == -step and dirY == 0:
                    orientacion = [-step,step,dirZ]

                elif dirX == -step and dirY == step:
                    orientacion = [0,step,dirZ]


            elif c == '-':
                dirX = orientacion[0]
                dirY = orientacion[1]
                dirZ = orientacion[2]

                if dirX == 0 and dirY == step:
                    orientacion = [-step,step,dirZ]

                elif dirX == step and dirY == step:
                    orientacion = [0,step,dirZ]

                elif dirX == step and dirY == 0:
                    orientacion = [step,step,dirZ]

                elif dirX == step and dirY == -step:
                    orientacion = [step,0,dirZ]

                elif dirX == 0 and dirY == -step:
                    orientacion = [step,-step,dirZ]

                elif dirX == -step and dirY == -step:
                    orientacion = [0,-step,dirZ]

                elif dirX == -step and dirY == 0:
                    orientacion = [-step,-step,dirZ]

                elif dirX == -step and dirY == step:
                    orientacion = [-step,0,dirZ]

                #Hacia arriba
            elif c == '*':
                dirX = orientacion[0]
                dirY = orientacion[1]
                dirZ = orientacion[2]

                if dirZ == 0:
                    orientacion = [dirX,dirY,stepV]

                elif dirZ == stepV:
                    v = [pos[0],pos[1],pos[2] + stepV]
                    pos = v
                    if not v in self.verts:
                        self.verts.append(v)
                        vertCont = vertCont + 1
                        if not trasBracket:
                            self.edges.append((vertCont-1,vertCont-2))
                        else:
                            trasBracket = False
                            self.edges.append((vertCont-1,ant))

                elif dirZ == -stepV:
                    orientacion = [dirX,dirY,0]
                #Hacia abajo
            elif c == '/':
                dirX = orientacion[0]
                dirY = orientacion[1]
                dirZ = orientacion[2]

                if dirZ == 0:
                    orientacion = [dirX,dirY,-stepV]

                elif dirZ == stepV:
                    orientacion = [dirX,dirY,0]

                elif dirZ == -stepV:
                    v = [pos[0],pos[1],pos[2] - stepV]
                    pos = v
                    if not v in self.verts:
                        self.verts.append(v)
                        vertCont = vertCont + 1
                        if not trasBracket:
                            self.edges.append((vertCont-1,vertCont-2))
                        else:
                            trasBracket = False
                            self.edges.append((vertCont-1,ant))
            cAnt = c
        return self.verts,self.edges,self.faces,self.vverts
