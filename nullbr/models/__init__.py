"""
Models for nullbr SDK

This module contains all the data models used by the nullbr SDK.
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
    MovieVideoItem,
    MovieVideoResponse,
)
from .search import ListResponse, SearchResponse
from .tv import (
    TV115Response,
    TVEd2kItem,
    TVEpisodeEd2kResponse,
    TVEpisodeMagnetResponse,
    TVEpisodeResponse,
    TVEpisodeVideoResponse,
    TVMagnetItem,
    TVResponse,
    TVSeasonMagnetResponse,
    TVSeasonResponse,
    TVVideoItem,
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
    "MovieVideoItem",
    "MovieVideoResponse",
    "TVResponse",
    "TV115Response",
    "TVSeasonResponse",
    "TVSeasonMagnetResponse",
    "TVEpisodeResponse",
    "TVEpisodeMagnetResponse",
    "TVEpisodeEd2kResponse",
    "TVEpisodeVideoResponse",
    "TVMagnetItem",
    "TVEd2kItem",
    "TVVideoItem",
    "CollectionResponse",
    "Collection115Response",
]
