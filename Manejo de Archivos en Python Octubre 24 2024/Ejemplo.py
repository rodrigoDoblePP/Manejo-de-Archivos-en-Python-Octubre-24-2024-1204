"""DE LECTURA1
Abrir un archivo en el servidor
Supongamos que tenemos el siguiente archivo, ubicado en la misma carpeta que Python:"""

#Ejemplo.txt


#2
#Para abrir el archivo, utilice la función incorporada open().
#La open()función devuelve un objeto de archivo, que tiene un read()método para leer el contenido del archivo:

ejemplo = open("ejemplo.txt", "r")
print(ejemplo.readable())
print (" ")

print (ejemplo.readline())
print (" ")

print (ejemplo.read())

ejemplo.close()

#Estructura

ejemplo_estructura = open ("demofile2.txt", "a")
ejemplo_estructura.write(" Ahora el ejemplo tiene mas espacio para contenido: \n")
ejemplo_estructura .close()

ejemplo_estructura = open ("demofile2.txt" , "r")
print (ejemplo_estructura.read())
ejemplo_estructura.close

ejemplo_sobreescribir = open ("demofile3.txt", "w")
ejemplo_sobreescribir.write("Uy ELimine el contenido pasado :o  \n")
ejemplo_sobreescribir.close()

ejemplo_sobreescribir = open ("demofile3.txt", "r")
print(ejemplo_sobreescribir.read())
ejemplo_sobreescribir.close()

#Eliminar Archivos
import os 

if os.path.exists("demofile.txt"):
    os.rdmir("demofile.txt")
    print ("El Archivo demofile.txt ha sido eliminado.")
else:
    print ("El archivo demofile.txt no se encuentra en este dispositvo")
    
#ELiminar carpeta completa

if os.path.exists("myfolder"):
    os.rdmir("myfolder")
    print("La Carpeta myfolder ha sido eliminad. ")
else:
    print("La carpeta myfolder no existe.")
    