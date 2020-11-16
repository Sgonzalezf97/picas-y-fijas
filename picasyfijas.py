from random import randint

def generar_secreto(cantidad):
    secreto = []
    while True:
        d = randint(0, 9)
        if d not in secreto:
            secreto.append(d)
        if len(secreto) == cantidad:
            break
    return secreto

def verificacion(s, n):
    if len(s) != len(n):
        print('Las listas no tiene el mismo tamaño')
    for item_s, item_n in zip(n, s):
        if item_s == item_n:
            return True
        else: 
            return False
nombres=[]
nombre= nombres
nombre=(input("porfavor dijite su nombre: "))
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
            

s = generar_secreto(int(input("ingrese cantidad de cifras: ")))
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

def resultados():
    f = open("picasyfijas.txt", "r")
    ganador= []
    for linea in f.readlines():
        elementos =[str(x) for x in linea.split(",")]
        if (elementos[3]== elementos[1]):
            ganador.append(int(elementos[4]))      
    if (elementos[4]== str(max(ganador))):
        print("el ganador es: "+elementos[0]+" con: "+elementos[4]+" vidas")     
    f.close()

i=inicio()
r=resultados()


