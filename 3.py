
import msvcrt
print("Hola que tal con este simple programa te vamos a ayudar a que puedas llevar una vida saludable, solo necesitamos que respondas a las siguientes preguntas ")
print(""
      ""
      "")
a=input("mencione su genero varon o mujer ")
b= ["varon", "mujer"]
x= int(input("Ingrese su edad : "))
y= int(input("Ingrese su estatura en centimetros : "))
z= int(input("Ingrese su peso en Kilogramos : "))
n=["1 o 2","2 o 3","3 o 4"]
m=["150 ml","250 ml"]
d=[(10*z)+(6.25*y)-(5 * x)+ 5,(10*z)+(6.25*y)-(5*x)- 161]
formula_2=[z/((y/100)*(y/100))]
formula_3=[1.2*formula_2[0]+0.23*x-10.8*1-5.4,1.2*formula_2[0]+0.23*x-5.4]
IMC=["Delgad@","Normal o saludable","sobrepeso leve","sobrepeso moderado","obes@"]
vitaminaC1=["guayaba", "naranjas","kiwi","fresas","melón","papaya","piña","mango"]
vitaminaC2=["pimiento rojo crudo", "pimiento verde crudo" ,"coles de Bruselas","brocoli","papas","coliflor"]
print(""
      ""
      "")
#Calculo de la edad
if x>0 and  x<=13 :
    print("Usted es un niño ")
elif x>=14 and x<21 :
    print("Usted es un joven")
else :
    print("Usted es un adulto")
print(""
      ""
      "")
#Calculo de calorias
#Para porder hallar el consumo adecuado de calorias nosotros debemos de utilizar como elemento principal el 'Calculo de Tasa metabolica'
print("su Tasa metabolica Basal es :")
if b[0] :
       print (d[0])
elif b[1] :
       print(d[1])
if b[0]:
    print ("usted debe consumir",d[0]*1.2,"calorias ")
elif b[1]:
    print("usted debe consumir",d[1]*1.2,"calorias ")
print(""
      ""
      "")
#Calculo del numero de proteinas que debemos ingerir al dia
print("Usted debe ingerir ",z*0.85 ,"proteinas al dia ")
print(""
      ""
      "")
#Cuanta agua debo consumir al dia
if b[0] :
    print("Usted debe de ingerir",z//7*1.1,"vasos de agua",m[1],"al dia para poder mantener su cuerpo hidratado")
elif b[1]:
    print("Usted debe de ingerir",z//7*1.2,"vasos de agua",m[0],"al dia para poder mantener su cuerpo hidratado")
print(""
      ""
      "")
#Calculando su indice de masa corporal
print("Su indice de masa corporal es",formula_2[0])
if formula_2[0] <=18.5 :
   print("lo cual indica que usted es una persona",IMC[0],"recomendable comer alimentos altos en proteinas y gluten para incrementar su masa corporal")
elif formula_2[0]>=18.5 and formula_2[0]<=24.9 :
    print("lo cual indica que usted se encuentra en un estado",IMC[1],"recomendable seguir manteniendo su rutina para mantener su grasa corporal estable")
elif formula_2[0]>=25 and formula_2[0] <=27.5:
    print("lo cual indica que usted es una persona con ",IMC[2],"recomendable salir a hacer ejercicio ",n[0], " con rutinas de",n[0], "horas por semana para disminuir los sobrantes de grasas saturadas ")
elif formula_2[0]>=27.5 and formula_2[0] <=30 :
    print("lo cual indica que usted es una persona con",IMC[3], "recomendable hacer ejercicio ",n[1]," con rutinas de ",n[1]," horas por semana para disminuir 1.2kg en un mes ")
else :
    print("lo cual indica que usted es una persona",IMC[4],"recomendable salir a hacer ejercicio ",n[2]," veces por semana para poder disminuir su masa corporal")

print(""
      ""
      "")
#Calculo de el porcentaje de grasa corporal
if b[0] :
    print("Su porcentaje de grasa corporal es ",formula_3[0],"%")
elif b[1]:
    print("Su porcentaje de grasa corporal es ",formula_3[1],"%")
print(""
      ""
      "")
#Calculo de proteinas diarias al dia
print("Las proteinas no ayudan a ganar mayor fuerza a nuestras celulas pero estas son paulatinas por ende nosotros debemos seguir una ley para poder asi ganar mayor fuerza sin lograr subir de peso ")
if x>0 and  x<=13 :
    print("usted debe de consumir hasta un maximo de 34 gramos de proteinas al dia ")
elif x >= 14 and x < 21 and b[0]:
    print("usted debe de consumir hasta un maximo de 52 gramos de proteinas al dia ")
elif x >= 14 and x < 21 and b[1]:
    print("usted debe de consumir hasta un maximo de 46 gramos de proteinas al dia ")
elif  x>=21 and x<=70 and b[0]:
    print("usted debe de consumir hasta un maximo de 56 gramos de proteinas al dia ")
elif  x>=21 and x<=70 and b[1]:
    print("usted debe de consumir hasta un maximo de 46 gramos de proteinas al dia ")
print(""
      ""
      "")
#calculando la vitamina C
print("La vitamina C ayuda al cuerpo a formar colágeno (que es la principal proteína utilizada como tejido conectivo en el cuerpo) en los vasos sanguíneos, huesos, cartílagos y músculos.")
if b[0]:

    print("usted necesita 90 mg en vitamina c al dia que puede encontrar en las siguientes frutas",vitaminaC1,
          "usted necesita 90 mg en vitamina c al dia que puede encontrar en las siguientes verduras",vitaminaC2)
elif b[1] :
    print("usted necesita 75 mg en vitamina c al dia que puede encontrar en las siguientes frutas",vitaminaC1,
          "usted necesita 75 mg en vitamina c al dia que puede encontrar en las siguientes verduras", vitaminaC2 )

msvcrt.getch()