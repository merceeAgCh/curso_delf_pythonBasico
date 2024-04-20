def leer_archivo():
    archivo = open("archivo.txt")
    contenido = archivo.read()
    archivo.close()
    print(contenido)
#leer_archivo()

def leer_archivo2():
    with open("archivo.txt") as f:
        contenido = f.read()
        print(contenido)
#leer_archivo2()

import os # modulo para manejar archivos y directorios
def leer_archivo3():
    if os.path.exists("archivo3.txt"):
        with open("archivo.txt") as f:
            contenido = f.read()
            print(contenido)
    else:
        print("El archivo no existe")
#leer_archivo3()

def escribir_archivo():
    with open("archivo4.txt","w") as f:
        f.write("Hola mundo")
        print ("Archivo escrito")
#escribir_archivo()

def escribir_en_archivo_exist_v2():
    with open("archivo4.txt","a") as f:
        f.write("\n Testeando mucho...")
        print ("Archivo escrito")
escribir_en_archivo_exist_v2()