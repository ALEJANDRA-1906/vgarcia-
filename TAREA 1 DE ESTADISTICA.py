# Nombre: Vanessa Alejandra Garcia Cortez
# Curso: Tercer semestre de Ingenieria de Software C1
class deber:
    def ejercicio_1(self):
    #De cual tipo de dato seria la variable donde se almacena lo siguiente
variable_n1= "HOLA MUNDO" #string
variable_n2= True        #Booleano
variable_n3= 1            #Entero
variable_n4= 'c'          #string
variable_n5= 256         #Entero
variable_n6= 8>19         #Booleano

print("Los tipos de datos serian: ")

def ejercicio_2(self):
     
# ¿Siguiendo la prioridad de operadores, convierta a expresión matemática, 
#resuelva e indique en cuál tipo de variable almacenará el resultado de las 
#siguientes expresiones:
    
	(5 + 3 * 2) + 9 > 3 * 5 * 14 % 3		= booleano 
(5+6)+9>3*5*14/100*3 
11+9>3*14/20*3 
20>3*7/10*3 
20>63/10 
20>6,3    
verdadero 

	2 *(4 – 10 + 8) /2* 36 *(1/2)			= Numérico 
2*(4-10+8)/2*36*1/1 
2*2/2*36*1/2 
2/2*36 
1*36 
36 

 
	260 / 12 + 54 % 3 – 85 % 7			= Float  
260 / 12 + 54 % 3 – 85 % 7 
21.67+0-1 
20.67 
	(48 < 2 * 3) | | (2 * 7 < 12)			=booleano 
(48 < 2 * 3)| |(2 * 7 < 12) 
(48<6)| | (14<12)  
falso| |falso   
falso 
	
	((8 > 2) | | (932 < 23)) && 4 == 2		=booleano 
((8 > 2) | | (932 < 23)) && 4 == 2 
((verdadero)||(falso)&&falso  
verdadero && falso  
falso 
 
def ejercicio_4(self):
    #   Dados dos (2) números calcule la suma, resta, multiplicación, división y módulo.

        numero1=int(input("ingrese el primer numero: "))
        numero2=int(input("ingrese el segundo numero: "))
        print("A continuacion las operaciones.....")
        suma = numero1 + numero2
        print("La suma es: ", suma)
        resta= numero1 - numero2
        print("La resta es: ", resta)
        división= numero1/numero2
        print("La division es: ", división)
        multiplicacion=numero1*numero2
        print("la multiplicacion es: ", multiplicacion)
        modulo= numero1 % numero2
        print("el modulo es: ", modulo)
        
def ejercicio_5(self):
    #Dados tres (3) números, Hacer una aplicación que calcule la resolvente.

        a=0
        b=0
        c=0
        while a<=0:
            a=float(input("Ingrese el primer numero: "))
        while b<=0:   
            b=float(input("Ingrese el segundo numero: "))
        while c<=0:
            c=float(input("Ingrese el tercer numero: "))
        try:
            if a!=0:
                x1=(-b+((b**2)-(4*a*c)))/(2*a)
                x2=(-b-((b**2)-(4*a*c)))/(2*a)
                if x1==0 and x2==0:
                    print("solucion: x=%4.3f"%x1)
                else:
                    print("soluciones: x1=%4.3f y x2=%4.3f"%(x1,x2))
            else:
                if b!=0:
                    x=-c/b
                    print("solucion: x=%4.3f"%x)
                else:
                    if c!=0:
                        print("la ecuacion no tiene solucion.")
                    else:
                        print("la ecuacion tiene infinitas soluciones.")
        except:
            print("sin soluciones: no se pudo realizar la ecuacion con los datos introduciones.")
            
def ejercicio_6(self):
     #   Dados dos (2) lados de un triángulo en cm, calcular la hipotenusa del mismo.

        Lado_A=int(input("ingrese el la distancia (cm) de el LADO A: "))
        Lado_B=int(input("ingrese el la distancia (cm) de el LADO B: "))

        print("El lado A es de: ", Lado_A,"(cm)")
        print("El lado B es de: ", Lado_B,"(cm)")
        ladoA=Lado_A*Lado_A
        ladoB=Lado_B*Lado_B
        hipot= ladoA + ladoB
        hipotensa=hipot ** 0.5
        hipotensa1=round(hipotensa,2)
        print("LA Hipotenusa es de: ",hipotensa1,"(cm)")

def ejercicio_7(self):
    #   Dado un (1) número, imprimir 0 si es par y 1 si es impar. 

        numero=int(input("ingrese un mumero entero: "))
        if numero % 2==0:
            print("el numero", numero,"es par")
        else: 
            print("el numero", numero,"es impar")
            
def ejercicio_9(self):
     #   Dado un (1) número binario de cuatro (4) dígitos imprimir su bit da paridad. El bit 
        #   de paridad es 1 si el número de bits 1 es impar y 0 en caso contrario.

        numero=input("ingrese cantidad (*4dijitos*): ")
        contador=0


        numero_bit=str(numero)
        contador= int(numero_bit[0])+int(numero_bit[1])+int(numero_bit[2])+int(numero_bit[3])

        if contador  % 2==0:
            print("0")
        else: 
            print("1")
def ejercicio_10(self):
    #   Dado un (1) número binario de cuatro (4) dígitos imprimir su valor

        cantidad=int(input("ingrese cantidad (*4dijitos*): "))

        umil = cantidad / 1000
        tmp = cantidad % 1000

        cent = tmp / 100
        tmp = tmp % 100

        dece = tmp / 10
        unid = tmp % 10

        unimil=round(umil)
        centena=round(cent)
        decenas=round(dece)
        unidad=round(unid)

        a_unimil= unimil*8
        a_centena= centena*4
        a_decenas= decenas*2
        a_unidad= unidad*1

        suma= a_unimil + a_centena + a_decenas + a_unidad

        print(suma)
        
def ejercicio_11(self):
    #   Dado un (1) número de cuatro (4) dígitos imprimirlo por separado en unidades, 
        #   decenas, centenas y unidades de mil.


        cantidad=int(input("ingrese cantidad (*4dijitos*): "))

        umil = cantidad / 1000
        tmp = cantidad % 1000

        cent = tmp / 100
        tmp = tmp % 100

        dece = tmp / 10
        unid = tmp % 10


        print ("Unidades de millar: %i" % umil )
        print ("Centenas: %i" % cent)
        print ("Decenas: %i" % dece)
        print ("Unidades: %i" % unid)

def ejercicio_12(self):
    #   exactamente entre 4 y no son divisibles exactamente entre 100 son años bisiestos. 
        #   Usando estas premisas crea un algoritmo que lea una fecha como un número 
        #   entero con el formato ddmmaaaa, y luego extraiga el año de la fecha indicando si 
        #   el mismo es un año bisiesto o no.


        a = int(input("Ingrese fecha (ddmmaaaa): "))
        b = str(a)
        c = int(b[4] + b[5] + b[6] + b[7])
        lb = [(c%400),(c%4),(c%100)]

        res = False
        if lb[1] == 0 and not(lb[2] == 0):
            res = True

        if lb[0] == 0 or res:
            print("Es un año bisiesto")
        else:
            print("No es un año bisiesto")

def ejercicio_13(self):
    #   Dado un número entero cuya cantidad de dígitos es igual a 5, determine si es 
        #   capicúa.
        #   Nota: un número capicúa es aquel que se lee igual hacia adelante que hacia atrás.


        numero=0
        while numero<=0:
            numero=int(input("ingrese un numero de 5 dijitos: "))
        a=str(numero)
        if a[0] == a[4] and a[1] == a[3]:
            print("Si es capicúa.")
        else:
            print("No es capicúa ")
            
def ejercicio_14(self):
    #   Cree un algoritmo que tome por entrada las horas y minutos de un día y dé como 
        #   resultado su equivalente en segundos.


        horas=0
        minutos=0
        while horas<=0:
            horas=int(input("ingrese las horas: "))
        while minutos<=0:
            minutos=int(input("ingrese los minutos: "))

        segund= horas*3600
        segun= minutos*60

        segundos= segund+segun

        print("los segundos totales son: ", segundos )
        
def ejercicio_15(self):
    #   Para un valor entero positivo que representa una cantidad en segundos, indicar 
        #   su equivalente en minutos, horas y días.


        numero=0
        while numero<=0:
            numero=int(input("ingrese cantidad deseada: "))


        dia= numero/86400
        horas= numero/3600
        minutos= numero/60

        print("Días: ", dia )
        print("Horas: ",horas)
        print("Minutos: ", minutos)
        
def ejercicio_16(self):
    #   Dados tres números enteros positivos A, B y C, determine ¿cuál de ellos es el 
        #   mayor? y ¿cuál es el segundo mayor?


        a=0
        b=0
        c=0
        while a<=0:
            a=int(input("Ingrese el primer numero entero positivo: "))
        while b<=0:   
            b=int(input("Ingrese el segundo numero entero positivo: "))
        while c<=0:
            c=int(input("Ingrese el tercer numero entero positivo: "))



        if a>b:   
            if a>c:
                print("Mumero mayor: ", a)
            else:
                print("Mumero mayor: ",c)
        else:
            if b>c:
                print("Mumero mayor: ",b)
            else:
                print("Mumero mayor: ",c)


        if a>b and a<c: 
            print("Mumero segundo mayor: ", a)
        if a<b and a>c: 
            print("Mumero segundo mayor: ", a)
        elif b>a and b<c:
            print("Mumero segundo mayor: ", b)
        elif b<a and b>c:
            print("Mumero segundo mayor: ", b)
        elif c>a and c<b:
            print("Mumero segundo mayor: ", c)
        elif c<a and c>b:
            print("Mumero segundo mayor: ", c)
            
def ejercicio_17(self):
    #   En un estacionamiento el monto a pagar se calcula multiplicando el número de 
        #   horas que permaneció el automóvil dentro del estacionamiento por Bs. 4 y se 
        #   incrementa esta cantidad en Bs. 2,50 por cada media hora adicional.
        #   Ahora se desea que usted elabore un algoritmo que a partir de la hora de entrada 
        #   y la hora de salida de un vehículo (las mismas corresponden a un mismo día) 
        #   calcule el monto a pagar por el dueño del vehículo.
        #   La entrada vendrá dada por dos enteros positivos el primero representa las horas 
        #   y el segundo los minutos, además por último se debe leer un carácter (A o P) que 
        #   indica si la hora es AM o PM.

        horas=0
        minutos=0
        salida=0

        while horas<=0 or horas>=13:
            horas=int(input("ingrese la hora de entrada horas : "))


        while minutos<=0 or minutos>=60:
            minutos=int(input("ingrese la hora de entrada minutos : "))

        am_pm=input("ingrese A o P: ")

        if am_pm=="a":
            am_pm_hora=horas+0
        else:
            am_pm_hora=horas+12

        while salida<=0 or salida>=12:
            salida=int(input("ingrese la hora de salida: "))




        am_pm=input("ingrese A o P: ")

        if am_pm=="a":
            am_pm_salida=salida+0
        else:
            am_pm_salida=salida+12



        if minutos>=30:
            valor_minutos=1*2.50
        else:
            valor_minutos=0+0

        minutos1=minutos*0.01
        lapso_de_tiempo=am_pm_salida-am_pm_hora
        lapso_de_tiempo1=lapso_de_tiempo+minutos1
        valor_hora=lapso_de_tiempo*4
        valor_total=(lapso_de_tiempo*4)+valor_minutos
        lapso_de_tiempo2=round(lapso_de_tiempo1,2)


        print("entrada: ",am_pm_hora)
        print("salida: ",am_pm_salida)
        print("minutos:",minutos)
        print("tiempo que estuvo estacionado : ",lapso_de_tiempo2)
        print("valor por cada media hora adicional: ",valor_minutos)
        print("valor por las hora:",valor_hora)
        print("valor total a pagar: ",valor_total)
        
def ejercicio_18(self):
    #   El IMC resulta de la división de la masa del individuo (en kilogramos) entre el 
        #   cuadrado de la estatura (en metros). El índice de masa corporal es un indicador 
        #   del peso de una persona en relación con su altura.
        #   Clasificación del IMC de acuerdo con la OMS de la ONU:
        #   a. Menor a 16: Criterio de ingreso.
        #   b. 16 a 16.9: infra peso.
        #   c. 17 a 18.4: bajo peso.
        #   d. 18.5 a 24.9: peso normal.
        #   e. 25 a 29.9: sobrepeso.
        #   f. 30 a 34.9: obesidad pre-mórbida.
        #   g. 40 a 45: obesidad mórbida.
        #   h. Mayor a 45: obesidad híper-mórbida.
        #   Dado el peso de una persona en libras (1 libra = 0,453592 Kg) y su estatura en 
        #   centímetros, calcule su IMC e indique como salida el peso en kilogramos, el valor 
        #   de IMC de la persona y la categoría en la cual fue clasificado.

        libra=0
        while libra<=0:
            libra=int(input("ingrese su masa(libras): "))

        estatura=0
        while estatura<=0:
            estatura=float(input("ingrese su estatura (en metros): "))
        masa=libra/2.2046


        imc=masa/(estatura**2)

        imc1=round(imc,2)

        if imc<=16:
            print("*Criterio de ingreso.*")
        elif imc>16 and imc <= 18.4:
            print("*Bajo peso.*")
        elif imc>=17 and imc <=  18.4:
            print("*Bajo peso.*")
        elif imc>=18.5 and imc <= 24.9:
            print("*Peso normal.*")
        elif imc>=25 and imc <=29.9:
            print("*Sobrepeso.*")
        elif imc>=30 and imc <=39.9:
            print("*Obesidad pre-mórbida.*")
        elif imc>=40 and imc <=45:
            print("*Obesidad mórbida.*")
        elif imc >=45:
            print("*Obesidad híper-mórbida.*")

        print("El valor de IMC de la persona es:",imc1)

def ejercicio_19(self):
     #   Escriba un algoritmo que reciba una fecha (día y mes) correspondiente al año 
        #   2014 e imprima por pantalla el número de días que han pasado desde el 1 de 
        #   Enero de 2014 hasta la fecha dada.


        dia=int(input("ingrese una fecha (día): "))
        mes=int(input("ingrese una fecha (mes): "))

        lista=[31,59,90,120,151,181,212,243,273,304,334,365]


        if mes==1:
            lapso_de_tiempo=lista[0]+dia
            print(" Dias que han pasado desde el 1 de Enero: ",lapso_de_tiempo)
        elif mes==2:
            lapso_de_tiempo=lista[1]+dia
            print(" Dias que han pasado desde el 1 de Enero: ",lapso_de_tiempo)
        elif mes==3:
            lapso_de_tiempo=lista[2]+dia
            print(" Dias que han pasado desde el 1 de Enero: ",lapso_de_tiempo)
        elif mes==4:
            lapso_de_tiempo=lista[3]+dia
            print(" Dias que han pasado desde el 1 de Enero: ",lapso_de_tiempo)
        elif mes==5:
            lapso_de_tiempo=lista[4]+dia
            print(" Dias que han pasado desde el 1 de Enero: ",lapso_de_tiempo)
        elif mes==6:
            lapso_de_tiempo=lista[5]+dia
            print(" Dias que han pasado desde el 1 de Enero: ",lapso_de_tiempo)
        elif mes==7:
            lapso_de_tiempo=lista[6]+dia
            print(" Dias que han pasado desde el 1 de Enero: ",lapso_de_tiempo)
        elif mes==8:
            lapso_de_tiempo=lista[7]+dia
            print(" Dias que han pasado desde el 1 de Enero: ",lapso_de_tiempo)
        elif mes==9:
            lapso_de_tiempo=lista[8]+dia
            print(" Dias que han pasado desde el 1 de Enero: ",lapso_de_tiempo)
        elif mes==10:
            lapso_de_tiempo=lista[9]+dia
            print(" Dias que han pasado desde el 1 de Enero: ",lapso_de_tiempo)
        elif mes==11:
            lapso_de_tiempo=lista[10]+dia
            print(" Dias que han pasado desde el 1 de Enero: ",lapso_de_tiempo)
        elif mes==12:
            lapso_de_tiempo=lista[11]+dia
            print(" Dias que han pasado desde el 1 de Enero: ",lapso_de_tiempo)
            
def ejercicio_20(self):
    
    #   Solicitar un número entre el 1 y el 12 e imprimir el mes correspondiente a dicho 
        #   número.


        numero=0
        while numero<=0 or numero >=13:
            numero=int(input("ingrese cantidad deseada: "))

        if numero== 1:
            print("Enero")
        elif numero== 2:
            print("febrero")
        elif numero==3:
            print("marzo")
        elif numero==4:
            print("abril")
        elif numero==5:
            print("mayo")
        elif numero==6:
            print("junio")
        elif numero==7:
            print("julio")
        elif numero==8:
            print("agosto")
        elif numero==9:
            print("septiembre")
        elif numero==10:
            print("octubre")
        elif numero==11:
            print("noviembre")
        elif numero==12:
            print("diciembre")

def ejercicio_21(self):
    #   En un almacén se hace un 20% de descuento a los clientes cuya compra supere 
        #   los Bs 1000, se desea que realice un algoritmo el cual tome por entrada el monto a 
        #   pagar por el cliente y arroje como salida el monto aplicando el descuento de ser 
        #   necesario.


        numero=0
        while numero<=0:
            numero=int(input("ingrese cantidad deseada: "))

        if numero>=1000:
            descuento=numero*0.2
            total=numero-descuento
            print("su monto a pagar es de:", total)
        else:
            print("su monto a pagar es de:",numero)
            
def ejercicio_22(self):
    def Ejercicio3_1(self):
        #   Dado un número entero N, calcular e informar al usuario cuántos dígitos tiene 
        #   dicho número.

        numero=0
        while numero<=0:
            numero=int(input("ingrese un numero: "))

        cont=0
        while numero>0:
            numero//=10
            cont+=1


        print("la cantidad de dijitos que tiene la canatidad es de:",cont)
        
def ejercicio_23(self):
     #   Dado un número, determine si es capicúa.
        #   Nota: un número capicúa es aquel que se lee igual hacia adelante que hacia atrás.


        numero=0
        while numero<=0:
            numero=int(input("ingrese un numero: "))
        a=str(numero)
        contador=0

        while numero>0:
            numero//=10
            contador+=1

        if contador==2:
            if a[0] == a[1]:
                print("Si es capicúa.")
            else:
                print("No es capicúa ")
        elif contador==3:
            if a[0] == a[2]:
                print("Si es capicúa.")
            else:
                print("No es capicúa ")
        elif contador==4:
            if a[0] == a[3] and a[1] == a[2]:
                print("Si es capicúa.")
            else:
                print("No es capicúa ")
        elif contador==5:
            if a[0] == a[4] and a[1] == a[3]:
                print("Si es capicúa.")
            else:
                print("No es capicúa ")
        elif contador==6:
            if a[0] == a[5] and a[1] == a[4] and a[2] == a[3] :
                print("Si es capicúa.")
            else:
                print("No es capicúa ")
        elif contador==7:
            if a[0] == a[6] and a[1] == a[5] and a[2] == a[4]:
                print("Si es capicúa.")
            else:
                print("No es capicúa ")
        elif contador==8:
            if a[0] == a[7] and a[1] == a[6] and a[2] == a[5] and a[3] == a[4]:
                print("Si es capicúa.")
            else:
                print("No es capicúa ")
                
def ejercicio_24(self):
    #   Dado un número N determinar si es un número primo.
        #       Nota: Un número primo es aquel que solo es divisible por 1(uno) y por el mismo. 

        numero=0
        while numero<=0:
            numero=int(input("ingrese un numero: "))
        contador=0

        for i in range(2,numero):
            resta=numero%i
            if resta==0:
                contador+=1

        if contador==0:
            print("el",numero, "si es primo.")
        else:
            print("el",numero, "no es primo.")
            
def ejercicio_25(self):
     #   Construya un programa que dado un valor entero N, haga el cálculo de la función 
        #   factorial utilizando estructuras iterativas.

        numero=int(input("ingrese un valor entero: "))
        a=numero
        for i in range(1,numero):
            i=i
            a=a*i

        print(a) 
def ejercicio_26(self):
    
     #   Dado un número entero N que representa una contraseña y asumiendo que una 
        #   contraseña debe tener al menos 10 dígitos para ser segura, determine si la 
        #   contraseña ingresada por el usuario es correcta, de no serlo debe pedirla 
        #   nuevamente hasta que tenga los 10 (diez) dígitos solicitados y al ser correcta 
        #   mostrar un mensaje de éxito al usuario, por salida estándar.
        contraseña=0
        while contraseña<=1000000000 or contraseña>=10000000000:
            contraseña=int(input("ingrese contraseña : "))


        if contraseña>=1000000000:
            print("**Contraseña correcta.**")
        else:
            print("**Contraseña incorrecta.**")
            
def ejercicio_27(self):
    #   Dada una secuencia de números terminada en cero (0), elaborar un algoritmo que 
        #   informe al usuario qué valor tiene el número mayor y qué valor tiene el número 
        #   menor, sin contar el cero (0).

        lista=[]

        numero=int(input("ingrese cantidad deseada: "))
        while numero !=0:
            lista.append(numero)
            numero=int(input("ingrese cantidad deseada: "))


        mayor=max(lista) 
        print("numero mayor: ", mayor)
        menor=min(lista)
        print("numero menor: ", menor)
        
def ejercicio_28(self):
    #   Se tiene una secuencia de enteros terminada en cero, que corresponde a la edad, 
        #   peso y estatura de una muestra de hombres y mujeres mayores de 18 años. Con 
        #   base en dicha secuencia se desea realizar un estudio a fin de conocer:
        #   Edad promedio de todas las personas en la muestra.
        #   Peso promedio de todas las personas en la muestra.
        #   Estatura promedio de todas las personas en la muestra.
        #   Cuántas personas hay con edad entre los 18 y 25 años.
        #   Cuántas personas son mayores a 36 años.
        #   Cuál es el promedio de peso de las personas con edades entre 18 y 35 
        #   años.

        a = 0
        posicion = ["La edad", "El peso(kg)", "La estatura(cm)"]
        lista = [24, 74, 182, 30, 70, 170, 41, 60, 169, 22, 75, 183, 31, 83, 178, 35, 76, 172, 22, 68, 164, 23, 77, 163,
                23, 58, 163, 26, 89, 185, 23, 55, 162, 26, 47, 160, 26, 60, 163, 22, 54, 170, 23, 58, 165, 26, 75, 178,
                24, 65, 170, 28, 82, 177, 42, 85, 183, 25, 75, 174, 35, 53, 150, 19, 60, 169, 35, 59, 160, 45, 74, 162,
                40, 58, 160, 33, 69, 167, 55, 70, 158, 24, 64, 160, 29, 79, 180, 52, 69, 160, 42, 78, 169, 34, 63, 152, 0]

        personas = [0, 0, 0,0]
        acumulador = [0, 0, 0]
        contador = 0
        while a < 3: # 3 para control de posición de lista acumulador
                acumulador[a] = acumulador[a] + lista[contador]

                if lista[contador] == lista[96] or lista[contador] == lista[95] or lista[contador] == lista[94]:
                        a += 1
                        contador = 0
                        contador += a
                else:
                        if a == 0:
                                if lista[contador]>18 and lista[contador]<25:
                                        personas[0] += 1
                                        personas[3] += lista[contador+1]
                        elif lista[contador]>36:
                                personas[1] += 1
                        contador += 3

        for i in posicion:
                contador+=1
                print("{} promedio de todas las personas en la muestra es {}".format(i,round(((acumulador[contador-4])/32))))

        print("Hay {} personas con edad entre los 18 y 25 años con un peso promedio de {}".format(personas[0],round((personas[3]/personas[0]))))
        print("Hay {} personas mayores a 36 años".format(personas[1]))
        
def ejercicio_29(self):
    #   Construye un algoritmo que calcule e imprima la tabla de multiplicar, desde la tabla 
        #   del 1 hasta la del 10.


        numero=0
        while numero<=0 or numero>=11:
            numero=int(input("ingrese la tabla que desea imprimir:"))

        for i in range(0,13):
            suma= i * numero
            print(numero,"X",i,"=",suma)
            
def ejercicio_30(self):
     #Escribir un algoritmo que muestre todas las fichas de dominó, sin repetir. 
        acumulador = 0
        contador = 0

        for i in range(0, 7, 1):
            for j in range(i,7,1):
                print(i," ", j) 

def ejercicio_31(self):
     #Dados N número positivos (N>1) calcular el promedio de esta serie. Considere que 
        #la serie termina al leer un 0.

        numero = 1
        total = 0
        contador = 0
        lista = ["Ingrese", "Error, Ingrese"]
        posicion = 0
        while numero != 0:
            numero = int(input(lista[posicion] + " un número positivo: "))
            if numero>1:
                posicion = 0
                total += numero
                contador += 1
            else:
                posicion = 1

        print("Su promedio de la serie dada es: ",(total/(contador)))
        
def ejercicio_32(self):
    #Construya una función que solicite edades al usuario y determine el promedio de 
        #las edades mayores a 18 años. El usuario indicará cuando desea dejar de 
        #suministrar datos de entrada. En la Acción Principal se informará el promedio 
        #calculado.

        bandera = input("Desea ingresar datos? sí (y) o no (n) ")

        if bandera.lower() == "y":
            print("Si desea salir, ingrese una 'x'")
            promedio = Ejercicios()
            pro_final = promedio.SoliUser(bandera)
            if pro_final != 0:
                print("El promedio de las edades mayores a 18 años es: ",pro_final)
            elif pro_final == 0:
                print("No hay edades mayores a 18 años.")
            else:
                print("Dado que no ha dado valores, no hay promedio.")
        else:
            print("Ha salido!")


def SoliUser(self,bandera):
        lista = []

        while bandera.lower() != "x":
            edad = input("Ingrese edad: ")
            if edad == "x":
                bandera = "x"
            elif edad != "x" and int(edad) <= 0:
                print("Ingrese un valor acorde por favor, o 'x' para dejar de ingrear datos")
            elif int(edad) > 18:
                lista.append(int(edad))


        if len(lista) > 0:
            promedio = (sum(lista))/len(lista)
        else:
            promedio = 0
        return promedio
        
def ejercicio_33(self):}
#Construya una función “Eleva” Que reciba como parámetros una base y un 
        #exponente y retorne al algoritmo principal el resultado de elevar un numero al otro.
        base = int(input("Ingrese la base: "))
        exponente = int(input("Ingrese su exponente: "))
        resultado = "Ejercicios"()
        calculo = resultado.Eleva(base,exponente)
        print("El resultado de elevar {} a la {} es {}".format(base,exponente,calculo))

def Eleva(self,base,exponente):
    calculo = base**exponente
    return calculo
