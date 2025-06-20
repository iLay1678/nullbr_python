from dataclasses import dataclass

from .base import MediaItem


@dataclass
class SearchResponse:
    page: int
    total_pages: int
    total_results: int
    items: list[MediaItem]


@dataclass
class ListResponse:
    id: int
    name: str
    description: str
    updated_dt: str
    page: int
    total_page: int
    items: list[MediaItem]
