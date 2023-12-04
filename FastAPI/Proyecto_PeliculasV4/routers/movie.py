from fastapi import APIRouter, Path, Query, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from models.movie import Movie as MovieModel
from config.database import Session
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()


@movie_router.get("/movies", tags=['movies'], response_model=List[Movie],
                  status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    result = MovieService(Session()).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@movie_router.get("/movies/{id}", tags=['movies'], response_model=Movie,
                  status_code=200)
# se cambia y se dice que es igual a Path(int)
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    result = MovieService(Session()).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={
            "message": "Movie not found"
            })
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@movie_router.get("/movies/", tags=['movies'], response_model=List[Movie])
def get_movies_by_category(category: str = Query(min_length=3, max_length=15)) -> List[Movie]:
    result = MovieService(Session()).get_movies_by_category(category)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Movies not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@movie_router.post("/movies", tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    MovieService(Session()).create_movie(movie)
    return JSONResponse(content={"message": "Movie created successfully"}, status_code=201)


@movie_router.put("/movies/{id}", tags=['movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie) -> dict:
    if not MovieService(Session()).get_movie(id):
        return JSONResponse(content={"message": "Movie not found"}, status_code=404)
    MovieService(MovieService(Session()).get_movie(id)).update_movie(id, movie)
    return JSONResponse(content={"message": "Movie updated successfully"}, status_code=200)


@movie_router.delete("/movies/{id}", tags=['movies'], response_model=dict)
def delete_movie(id: int) -> dict:
    if not MovieService(Session()).get_movie(id):
        return JSONResponse(content={"message": "Movie not found"}, status_code=404)
    MovieService(Session()).delete_movie(id)
    return JSONResponse(content={"message": "Movie deleted successfully"})
