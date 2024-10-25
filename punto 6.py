Alladir = open("demofile3.txt", "w")
Alladir.write("Woops! I have deleted the content!")
Alladir.close()#con esto puedes sobrecribir en el texto
Alladir= open("demofile3.txt", "r")
print(Alladir.read())
