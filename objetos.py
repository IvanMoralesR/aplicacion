###################################
#Programaación orientada a objetos#
###################################

################################
#Una clase para un objeto vacio #
#No está tan vacio, necesita####
#la palabra pass################
#

class ObjetoVacio:
    pass

########################
#nada es un ObjetoVacio#
########################

nada= ObjetoVacio()
print(type(nada))

#################
#La clase llanta#
#################

class Llanta:
    #La variable cuenta es para toda la clase
    cuenta=0

    ##################################
    #Función contructors de identidad
    #__init__ es una función reservad
    #comienza con un mismo: self
    #pero puede ser otro nombre(mi)
    #pramétros de entrada= default
    ##################################

    def __init__ (mi,radio=50, ancho=30, presión=1.5) :
        #variaable de la estrucruta completa Llanta
        Llanta.cuenta += 1

        #variables exclisivas de cada objeto
        mi.radio=radio
        mi.ancho=ancho
        mi.presión=presión

######################
#Objetos instanciados
######################

llanta1= Llanta(50,30,1.5)
llanta2= Llanta(presión=1.2)
llanta3= Llanta()
llanta4= Llanta(40,30,1.6)

####################################
#Objeto que contiene otros objetos
####################################

class Coche:
    def __init__(mi,ll1,ll2,ll3,ll4):
        mi.llanta1=ll1
        mi.llanta2=ll2
        mi.llanta3=ll3
        mi.llanta4=ll4

miTsurito= Coche(llanta1,llanta2,llanta3,llanta4,)

print("Total de llantas", Llanta.cuenta)  #Variable global de la clase

print("Presion total de la llanta 4 =", llanta4.presión)# Presió total de la llanta4
print("Radio de la llanta 4 =", llanta4.radio)
print("Radio de la llanta 3 =",llanta4.radio)
print("Presion de la llanta 1 de mi tsurito", miTsurito.llanta1.presión)

#################
#Encapsulamiento
#################

#########################################################################
#Uso de la fucnió de python property para poner y obteber atributos UwU
#########################################################################
class Estudiante:
    def __init__(mi):
        mi.__nombre = ''
    def ponerme_nombre(mi, nombre):
        print('se llamó a ponerme nombre')
        mi.__nombre= nombre
    def obtener_nombre(mi):
        print ('se llamó a obtener_nombre')
        return mi.__nombre
    nombre= property(obtener_nombre,ponerme_nombre)

########################
#Crea objeto sin nombre
########################

estudiante = Estudiante()

####################################################################
#Pnerle nobre usando la propieda nombre y el método ponerme_nombre
#(sin tener que llamar a explicitamente a la función)
####################################################################
estudiante.nombre= 'Ivan'

##################################################################
#Obtener el nombre con el método obtener_nombre
#__nombre es una variable encapsulada(no visible desde fuera)
#(sin tenernque llamr explicitamente a la dfución obtener_nombre)
##################################################################
print(estudiante.nombre)

#Esto no funciona
#print(estudiante.__nombre)

####################
#Herencia de clases
####################

class Cuadrilatero:
    def __init__ (mi, a ,b ,c ,d):
        mi.lado1=a
        mi.lado2=b
        mi.lado3=c
        mi.lado4=d
    
    def perimetro (mi):
        p= mi.lado1+mi.lado2+mi.lado3+mi.lado4
        print("perimetro=", p)
        return p
#########################################
#Su hijo rectángulo
#Rectángulo es hijo de cuadrilatero
#Rectángulo (Cuadrilatero)
##########################################

class Rectangulo (Cuadrilatero):
    def __init__(self,a,b):
        #########################
        #Constructor de su madre 
        #########################
        super().__init__(a, b, c, d)

#####################
#Su nieto Cuadrado
#Hijo de Rectángulo
######################
#OwO

class Cuadrado(Rectangulo):
    def __init__(self,a):
        super().__init(a,a)

    def area(self):
        area=self.lado**2
        return area
