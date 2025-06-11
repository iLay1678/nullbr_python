"""
Models for nullbr-python SDK

This module contains all the data models used by the nullbr-python SDK.
"""

from .base import MediaItem
from .collection import (
    Collection115Response,
    CollectionResponse,
)
from .movie import (
    Movie115Item,
    Movie115Response,
    MovieEd2kItem,
    MovieEd2kResponse,
    MovieMagnetItem,
    MovieMagnetResponse,
    MovieResponse,
)
from .search import ListResponse, SearchResponse
from .tv import (
    TV115Response,
    TVResponse,
    TVSeasonMagnetResponse,
    TVSeasonResponse,
)

__all__ = [
    "MediaItem",
    "SearchResponse",
    "ListResponse",
    "Movie115Item",
    "MovieResponse",
    "Movie115Response",
    "MovieMagnetItem",
    "MovieMagnetResponse",
    "MovieEd2kItem",
    "MovieEd2kResponse",
    "TVResponse",
    "TV115Response",
    "TVSeasonResponse",
    "TVSeasonMagnetResponse",
    "CollectionResponse",
    "Collection115Response",
]
