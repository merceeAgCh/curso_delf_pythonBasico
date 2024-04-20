def holis():
    print("Holis")
#holis()
class Librito:
    def __init__(self, titulo): #init es un metodo especial que se ejecuta al crear un objeto
        self.titulo = titulo
    def ver_titulo(self):
        return self.titulo