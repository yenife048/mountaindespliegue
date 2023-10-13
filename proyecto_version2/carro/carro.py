class Carro: #guardar sesiones
    def __init__(self, request):
        self.request = request
        self.session = request.session
        self.carro = self.session.get("carro", {})
        if "carro" not in self.session:
            self.session["carro"] = self.carro
            
    def agregar(self,hamburguesas):
        if(str(hamburguesas.id)not in self.carro.keys()): #si no se encuentra el id del producto que lo agregue
            self.carro[hamburguesas.id]={
                "hamburguesas_id":hamburguesas.id,
                "nombre":hamburguesas.title,
                "precio":str(hamburguesas.precio),
                "cantidad":1,  # Utiliza la cantidad proporcionada
                "imagen":hamburguesas.image1.url,
            }
        else:
            for key, value in self.carro.items():
                if key==str(hamburguesas.id):
                    value["cantidad"]=value["cantidad"]+1 #incrementando en 1
                    value["precio"]=float(value["precio"])+hamburguesas.precio
                    break
        self.guardar_carro()#guardar la sesion  actualizar

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminar(self, hamburguesas):
        hamburguesas.id=str(hamburguesas.id)
        if hamburguesas.id in self.carro:
            del self.carro[hamburguesas.id] #eliminar
            self.guardar_carro()     #guardar
        
    def restar_producto(self, hamburguesas):
        for key, value in self.carro.items():
                if key==str(hamburguesas.id):
                    value["cantidad"]=value["cantidad"]-1 #incrementando en 1
                    value["precio"]=float(value["precio"])-hamburguesas.precio
                    if value["cantidad"]<1:
                        self.eliminar(hamburguesas)
                    break
        self.guardar_carro()  

    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True
        
    def contar_productos(self):
        cantidad_productos = sum(item['cantidad'] for item in self.carro.values())
        return cantidad_productos
           


    
       


    
    