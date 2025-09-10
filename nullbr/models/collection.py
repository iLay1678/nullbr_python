from dataclasses import dataclass

from .base import MediaItem
from .movie import Movie115Item


@dataclass
class CollectionResponse:
    """合集响应模型"""

    id: int  #: 合集ID
    poster: str  #: 海报图片URL
    title: str  #: 合集标题
    overview: str  #: 合集简介
    vote: str  #: 评分（注意：这里是字符串类型）
    release_date: str  #: 发布日期
    has_115: bool  #: 是否有115云盘资源
    items: list[MediaItem]  #: 媒体项目列表


@dataclass
class Collection115Response:
    """合集115云盘资源响应模型"""

    id: int  #: 合集ID
    media_type: str  #: 媒体类型
    page: int  #: 当前页码
    total_page: int  #: 总页数
    items: list[Movie115Item]  #: 115云盘资源列表
