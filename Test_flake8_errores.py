Variable1 = "NuncaSeUsaEstaVariable" #F841  local variable name is assigned to but never used
Variable2 = ["Tarea1:","Errores","detectables","por","Flake8"]
import math #F401   module imported but unused \\ F404  future import(s) name after other statements
contador = 0
while (contador< (len(Variable2))):
 print (Variable2[contador])
 contador = contador+1
