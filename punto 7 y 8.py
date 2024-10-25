import os
os.remove("Borrar archivos/algo.txt")
#con esto borras archivos
#hise otro por si quieres ver pero porfavor buelbe a haser otro despues

#El archivo: aabo de naser que escribiran sobre mi
#el archivo es eliminado

#Nota: tambien funsiona otros archivos

if os.path.exists("Borrar archivos/algo.txt"):
  os.remove("Borrar archivos/algo.txt")
  ("el archivo no existe")
else:
  print("el archivo existia")
