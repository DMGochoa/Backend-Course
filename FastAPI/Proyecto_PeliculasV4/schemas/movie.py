from typing import Optional
from pydantic import BaseModel, Field

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(default="Mi Pelicula", min_length=5, max_length=30)
    overview: str = Field(
        default="Descripcion de la película", min_length=10, max_length=300)
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