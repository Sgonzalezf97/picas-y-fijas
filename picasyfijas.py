#se importa para poder utilizar los numeros aleatorios
from random import randint

#genera un numero para adivinar
def generar_secreto(cantidad):
    secreto = []
    while True:
        d = randint(0, 9)
        if d not in secreto:
            secreto.append(d)
        if len(secreto) == cantidad:
            break
    return secreto

#este apartado verifica que el numero que ingresas tenga el mismo tamaño que el que se va a adivinar
def verificacion(s, n):
    if len(s) != len(n):
        print('Las listas no tiene el mismo tamaño')
    for item_s, item_n in zip(n, s):
        if item_s == item_n:
            return True
        else: 
            return False

#este apartado nos deja almacenar el nombre del concursante
nombres=[]
nombre= nombres
nombre=(input("por favor dijite su nombre: "))

# este apartado nos dice si tenemos fijas o picas en nuestro numero
def picas(s,n):
    pica=0
    fija=0
    for x in s:
        for y in n:
            if x==y:
                if(s.index(x)==n.index(y)):
                    fija=fija+1
                else:
                    pica=pica+1
    f = open("picasyfijas.txt", "a")            
    f.write(str(nombre)+","+str(len(s))+","+str(pica)+","+ str(fija)+",")   
    f.close()         
    print(int(pica)," picas")
    print(int(fija),"fijas")
            
# se genera el numero secreto
s = generar_secreto(int(input("ingrese cantidad de cifras(3,4,5): ")))

#realiza el inicio del juego poniendo el nivel del juego
def inicio():
    ganador=False
    if(len(s)<=3):
        vidas=15
    if(len(s)==4):
        vidas=25
    if(len(s)>5):
        vidas=30
    while(vidas>0):
        print("tiene ",vidas," intentos")
        print(s)
        n = [int(x) for x in input("ingrese un numero: ")]
        verificacion(s,n)
        picas(s,n)
        vidas=vidas-1
        if (s==n):
            ganador=True
            print("ganó")
            f = open("picasyfijas.txt", "a")            
            f.write(str(vidas)+","+str(ganador)+"\n") 
            f.close()    
            break     
        f = open("picasyfijas.txt", "a")            
        f.write(str(vidas)+","+str(ganador)+"\n") 
        f.close()    
    print("intenta con otra cantidad de cifras")

#nos muestra y almacena los registros de cada intento segun el usuario
def resultados():
    f = open("picasyfijas.txt", "r")
    ganador= []
    for linea in f.readlines():
        elementos =[str(x) for x in linea.split(",")]
        if (elementos[3]== elementos[1]):
            ganador.append(int(elementos[4])) 
    f.close()
    f = open("picasyfijas.txt", "r")
    for line in f.readlines():
        elemento =[str(y) for y in line.split(",")]
        if (((elemento[3]== elemento[1]) & (elemento[4]== str(max(ganador))))):     
            print("el ganador en "+elemento[1]+" cifras es: "+elemento[0]+" con: "+elemento[4]+" vidas")     
    f.close()

# se inicializa todo
i=inicio()
r=resultados()