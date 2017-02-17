from notes import notass
lista=[]
notas=0
a=0
respuesta="si"
while respuesta!="no":
		nota=int(input("ingrese notas"))
		if nota<=100:
			b=a+1.01
			suma=notas+nota
		respuesta=str(input("desea continuar: "))
print(suma/b)