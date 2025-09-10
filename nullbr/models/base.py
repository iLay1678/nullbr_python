from dataclasses import dataclass
from typing import Optional


@dataclass
class MediaItem:
    """媒体项目基础模型"""

    media_type: str  #: 媒体类型，如 "movie" 或 "tv"
    tmdbid: int  #: TMDB（The Movie Database）ID
    poster: str  #: 海报图片URL
    title: str  #: 标题
    overview: str  #: 简介/概述
    vote_average: Optional[float] = None  #: 评分，范围通常为0-10
    release_date: Optional[str] = None  #: 发布日期，格式为 YYYY-MM-DD
    rank: Optional[int] = None  #: 排名
