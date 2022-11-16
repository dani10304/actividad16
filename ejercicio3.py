#numero de preguntas
#numero de aciertos
#numero de fallos 
#numero de preguntas sin contestar

#DATOS DE SALIDA

#nota del examen -- tri

#PROCESO 

#numero de preguntas acertadas + 0,5
#numero de preguntas  falladas - 0,25


#PSEUDOCÒDIGO
acertadas=int(input('dime el numero de aciertos en el test'))
falladas=int(input('dime el numero de fallos en el test'))


notadelexamen=acertadas*0.5-falladas*0.25
print(f'la nota del examen tipo text es {notadelexamen}')
