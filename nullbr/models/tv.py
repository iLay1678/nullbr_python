from dataclasses import dataclass

from .movie import Movie115Item, MovieEd2kItem, MovieMagnetItem, MovieVideoItem


@dataclass
class TVResponse:
    id: int
    poster: str
    title: str
    overview: str
    vote: float
    release_date: str
    number_of_seasons: int
    has_115: bool
    has_magnet: bool
    has_ed2k: bool
    has_video: bool


@dataclass
class TV115Response:
    id: int
    media_type: str
    page: int
    total_page: int
    items: list[Movie115Item]


@dataclass
class TVSeasonResponse:
    tv_show_id: int
    season_number: int
    name: str
    overview: str
    air_date: str
    poseter: str
    episode_count: int
    vote_average: float
    has_magnet: bool


@dataclass
class TVSeasonMagnetResponse:
    id: int
    season_number: int
    media_type: str
    magnet: list[MovieMagnetItem]


@dataclass
class TVEpisodeEd2kResponse:
    tv_show_id: int
    season_number: int
    episode_number: int
    media_type: str
    ed2k: list[MovieEd2kItem]


@dataclass
class TVEpisodeVideoResponse:
    tv_show_id: int
    season_number: int
    episode_number: int
    media_type: str
    video: list[MovieVideoItem]
