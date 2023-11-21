from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

# Estamos creando una instancia de la clase FastAPI
app = FastAPI()

# Cambios a la documentacion
app.title = "La super API" 
app.version = "1.0.0"

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    },
    {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    } 
]

# Ahora crearemos nuestro primer endpoint 
@app.get("/", tags=['home']) # Aqui se agrega la ruta de inicio
def message():
    return HTMLResponse(content="<h1> Bienvenido a mi API </h1>")

@app.get("/movies", tags=['movies'])
def get_movies():
    return movies

# Parte 2
@app.get("/movies/{id}", tags=['movies'])
def get_movie(id: int):
    movie = list(filter(lambda movie: movie['id'] == id, movies))
    return movie

# Parte 3
@app.get("/movies/", tags=['movies'])
def get_movies_by_category(category: str):
    movies_by_category = [movie for movie in movies if movie['category'] == category]
    return movies_by_category

# Parte 4
@app.post("/movies", tags=['movies'])
def create_movie(id: int = Body(),
                 title: str = Body(),
                 overview: str = Body(),
                 year: str = Body(),
                 rating: float = Body(),
                 category: str = Body()):
    movies.append({
        'id': id,
        'title': title,
        'overview': overview,
        'year': year,
        'rating': rating,
        'category': category
    })
    return movies

@app.put("/movies/{id}", tags=['movies'])
def update_movie(id: int,
                 title: str = Body(),
                 overview: str = Body(),
                 year: str = Body(),
                 rating: float = Body(),
                 category: str = Body()):
    for movie in movies:
        if movie['id'] == id:
            movie['title'] = title
            movie['overview'] = overview
            movie['year'] = year
            movie['rating'] = rating
            movie['category'] = category
    return movies

@app.delete("/movies/{id}", tags=['movies'])
def delete_movie(id: int):
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
    return movies