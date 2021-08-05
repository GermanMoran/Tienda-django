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