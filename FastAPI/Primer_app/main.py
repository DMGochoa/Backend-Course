from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Estamos creando una instancia de la clase FastAPI
app = FastAPI()

# Cambios a la documentacion
app.title = "La super API" 
app.version = "1.0.0"

# Ahora crearemos nuestro primer endpoint 
@app.get("/", tags=['home']) # Aqui se agrega la ruta de inicio
def message():
    return HTMLResponse(content="<h1> Bienvenido a mi API </h1>")
