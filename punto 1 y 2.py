archivo=open("alubno.txt.txt","r")#Abrir mi archivo de texto
print(archivo.read())#esto lee el archivo
print("------------")
print(archivo.readable())#esto redacta el archivo
print("------------")
#print(archivo.readline())
#print(archivo.readline())
print(archivo.readline())#este separa el conetedio por un espasio hasia abajo y dise un elemento.
#Pero solo funsiona si no esta el read
print("------------")
archivo = open("alubno.txt.txt", "r")
print(archivo.read(30))#con esto puedes controlar el numero de carapteres que se mostraran
print("------------")
archivo = open("extra.txt", "a")
archivo.write("")
archivo.write("algo nuevo")
archivo.close()

print("------------")

print("------------")
archivo.close()#Mink: hohohohohoh feliz nadivdad, Mr.Ink: es close no clous, Mink. Oh mmm Huhuhuhuhu feliz haloween
#24/10/2024.... aun falta
