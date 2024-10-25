Alladir = open("extra.txt", "a")
Alladir.write("10/10")
Alladir.close()
print("\nSe alladio el 10/10 al archivo")#con esto allades a texto
Alladir= open("extra.txt", "r")
print(Alladir.read())
