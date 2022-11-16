#DATOS DE ENTRADA

#nota hito individual -- hi
#nota hito grupal -- hg
#nota de examen -- ex

#DATOS DE SALIDA

#nota del trimestre -- tri

#PROCESO 

# hi*0,3 = nota hito individual
# hg*0,2 = nota hito grupal
# ex*0,5 = nota de examen

# nota hito individual + nota hito grupal + nota examen = nota trimestre

#PSEUDOCÒDIGO

hi=int(input('dime la nota del hito individual'))
hg=int(input('dime la nota del hito grupal'))
ex=int(input('dime tu nota del examen'))

notadeltrimestre=(hi*0.3)+(hg*0.2)+(ex*0.5)

print(f'la nota final del trimestre es {round(notadeltrimestre)}')
