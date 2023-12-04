from fastapi import FastAPI, Body, Path, Query, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer
from config.database import Session, engine, Base
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder

# Estamos creando una instancia de la clase FastAPI
app = FastAPI()
app.title = "La super API" 
app.version = "3.0.0"

Base.metadata.create_all(bind=engine)

class User(BaseModel):
    email: str
    password: str

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(default="Mi Pelicula", min_length=5, max_length=30)
    overview: str = Field(default="Descripcion de la película", min_length=10, max_length=300)
    year: int = Field(default=2022, le=2022)
    rating: float = Field(default=10, ge=0, le=10)
    category: str = Field(default="Comedia", min_length=3, max_length=15)
    
    # Configuracion de la documentacion
    class Config:
        model_config = {
        "json_schema_extra": {
                "examples": [
                    {
                        "id": 1,
                        "title": "Mi Pelicula",
                        "overview": "Descripcion de la pelicula",
                        "year": 2022,
                        "rating": 9.9,
                        "category": "Acción"
                    }
                ]
            }
        }

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=401, detail="Invalid user")
        #return 

# Ahora crearemos nuestro primer endpoint 
@app.get("/", tags=['home']) # Aqui se agrega la ruta de inicio
def message():
    return HTMLResponse(content="<h1> Bienvenido a mi API </h1>")

@app.get("/movies", tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    result = db.query(MovieModel).all()    
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Parte 2
@app.get("/movies/{id}", tags=['movies'], response_model=Movie, status_code=200)
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie: # se cambia y se dice que es igual a Path(int)
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "Movie not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Parte 3
@app.get("/movies/", tags=['movies'], response_model=List[Movie])
def get_movies_by_category(category: str = Query(min_length=3, max_length=15)) -> List[Movie]:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.category == category).all()
    if not result:
        return JSONResponse(status_code=404, content={"message": "Movies not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Parte 4
@app.post("/movies", tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    # Abrimos la conexion a la base de datos
    db = Session()
    # Creamos una instancia de la clase MovieModel con los datos del body
    new_movie = MovieModel(**movie.model_dump())
    # Agregamos la instancia a la base de datos
    db.add(new_movie)
    # Guardamos los cambios en la base de datos
    db.commit()
    return JSONResponse(content={"message": "Movie created successfully"}, status_code=201)

@app.put("/movies/{id}", tags=['movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie) -> dict:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(content={"message": "Movie not found"}, status_code=404)
    result.title = movie.title
    result.overview = movie.overview
    result.year = movie.year
    result.rating = movie.rating
    result.category = movie.category
    db.commit()
    return JSONResponse(content={"message": "Movie updated successfully"}, status_code=200)

@app.delete("/movies/{id}", tags=['movies'], response_model=dict)
def delete_movie(id: int) -> dict:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(content={"message": "Movie not found"}, status_code=404)
    db.delete(result)
    db.commit()
    return JSONResponse(content={"message": "Movie deleted successfully"})

@app.post("/login", tags=['auth'], response_model=dict, status_code=200)
def login(user: User) -> dict:
    if user.email == "admin@gmail.com" and user.password == "admin":
        token = create_token(data=user.model_dump())
        return JSONResponse(content={"token": token}, 
                            status_code=200)
    else:
        return JSONResponse(content={"message": "Invalid credentials"},
                            status_code=401)
