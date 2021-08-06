class carro:
    # Constructor que inicia las tareas mas importantes

    def __init__(self, request):
        self.request = request
        # Con esto ya tenemos iniciada la sección
        self.session = request.session

        # Ahora debemos construir un carro de compra para esta seccion
        carro = self.session.get("carro")
        if not carro:
            carro=self.session['carro']={}
        else:
            self.carro=carro

        
    # Metodo para agregar productos al carro
    def agregar(self, producto):
        # Comprobamos si el producto no este en el carro
        if (str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]= {
                "producto_id":producto.id,
                "nombre": producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url
            }
        
        # En caso de que el producto ya este en el carro

        else:
            for key,value in self.carro.items:
                if key == str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    # ya encontramos el articulo, no recorra mas 
                    break

        # Si agregamos un producto por primera vez y7o aumentamos la cantidad, se almacena en la seccion
        # Funcion que nos permite guardar la seccion
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"]= self.carro
        self.session.modified= True

    
    def eliminar_producto(self,producto):
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            # Volvemos a guaradar el carro
            self.guardar_carro()


    # Restar unidades
    def restar_productos(self,producto):
        for key,value in self.carro.items:
                if key == str(producto.id):
                    value["cantidad"]=value["cantidad"]-1
                    # ya encontramos el articulo, no recorra mas
                    if value["cantidad"] < 1:
                        self.eliminar_producto(producto)
                    break
        self.guardar_carro()


    def limpiar_carro(self):
        # Construyo un diccionario vacio
        self.session['carro']={}
        # Modificamos la seccion
        self.session.modified= True
