"""
Models for nullbr-python SDK

This module contains all the data models used by the nullbr-python SDK.
"""

from .base import MediaItem
from .search import SearchResponse, ListResponse
from .movie import (
    Movie115Item,
    MovieResponse,
    Movie115Response,
    MovieMagnetItem,
    MovieMagnetResponse,
    MovieEd2kItem,
    MovieEd2kResponse,
)
from .tv import (
    TVResponse,
    TV115Response,
    TVSeasonResponse,
    TVSeasonMagnetResponse,
)
from .collection import (
    CollectionResponse,
    Collection115Response,
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