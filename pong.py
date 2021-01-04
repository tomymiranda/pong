from turtle import *
import turtle

#ventana
ventanaJuego = turtle.Screen()
ventanaJuego.title("pong")
ventanaJuego.bgcolor("black")
ventanaJuego.setup(width = 800, height = 600)
ventanaJuego.tracer(0)


#puntos
puntosA = 0
puntosB = 0


#JugadorA
jugadorA = turtle.Turtle()
jugadorA.speed(0)#para que aparezca instantaneamente
jugadorA.shape("square")
jugadorA.color("white")
jugadorA.penup()#para que no quede una linea cuando se crea y se redirecciona
jugadorA.goto(-350,0)
jugadorA.shapesize(stretch_wid = 5,stretch_len = 1)#se cambia el tamanio del cuadrado ya que cuando se crea es de 20 pixeles, lo que hace es multiplicar los pix por 5 y 1


#JugdorB
jugadorB = turtle.Turtle()
jugadorB.speed(0)#para que aparezca instantaneamente
jugadorB.shape("square")
jugadorB.color("white")
jugadorB.penup()#para que no quede una linea cuando se crea y se redirecciona
jugadorB.goto(350,0)
jugadorB.shapesize(stretch_wid = 5,stretch_len = 1)#se cambia el tamanio del cuadrado ya que cuando se crea es de 20 pixeles, lo que hace es multiplicar los pix por 5 y 1

#Pelota
pelota = turtle.Turtle()
pelota.speed(0)#para que aparezca instantaneamente
pelota.shape("square")
pelota.color("white")
pelota.penup()#para que no quede una linea cuando se crea y se redirecciona
pelota.goto(0,0)
pelota.dx = 2 #cambio de pixeles en x, no acepta numeros con coma
pelota.dy = 2 #cambio de pixeles en y, no acepta numeros con coma

#division de cancha
division = turtle.Turtle()
division.color("white")
division.goto(0,400)
division.goto(0,-400)


#marcador
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(0,260)
marcador.write("jugadorA:0       jugadorB:0", align = "center", font =("Courier",24,"normal"))


#funciones
def jugadorA_arriba():
    y = jugadorA.ycor()
    y +=30
    jugadorA.sety(y)

def jugadorA_abajo():
    y = jugadorA.ycor()
    y -=30
    jugadorA.sety(y)

def jugadorB_arriba():
    y = jugadorB.ycor()
    y +=30
    jugadorB.sety(y)

def jugadorB_abajo():
    y = jugadorB.ycor()
    y -=30
    jugadorB.sety(y)



#teclado
ventanaJuego.listen()
ventanaJuego.onkeypress(jugadorA_arriba,"w")
ventanaJuego.onkeypress(jugadorA_abajo,"s")
ventanaJuego.onkeypress(jugadorB_arriba,"Up")
ventanaJuego.onkeypress(jugadorB_abajo,"Down")

while True:
    ventanaJuego.update()
    
    pelota.setx(pelota.xcor() + pelota.dx )
    pelota.sety(pelota.ycor() + pelota.dy )

    #Bordes
    if pelota.ycor() > 290 or pelota.ycor() < -290:
        pelota.dy *= -1

    #Bordes izq y der
    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *=-1
        puntosA +=1
        marcador.clear()
        marcador.write("jugadorA: {}        jugadorB:{}".format(puntosA,puntosB), align = "center", font =("Courier",24,"normal"))

    if pelota.xcor() < -390:
        pelota.goto(0,0)
        pelota.dx *=-1
        puntosB +=1
        marcador.clear()
        marcador.write("jugadorA: {}        jugadorB:{}".format(puntosA,puntosB), align = "center", font =("Courier",24,"normal"))

    if((pelota.xcor() > 340 and pelota.xcor() < 350)
           and( pelota.ycor() < jugadorB.ycor() + 50
           and pelota.ycor() > jugadorB.ycor() - 50)):
        pelota.dx *= -1


    if((pelota.xcor() < -340 and pelota.xcor() > -350)
           and( pelota.ycor() < jugadorA.ycor() + 50
           and pelota.ycor() > jugadorA.ycor() - 50)):
        pelota.dx *= -1    
