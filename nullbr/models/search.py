from dataclasses import dataclass

from .base import MediaItem


@dataclass
class SearchResponse:
    """搜索结果响应模型"""

    page: int  #: 当前页码
    total_pages: int  #: 总页数
    total_results: int  #: 搜索结果总数
    items: list[MediaItem]  #: 媒体项目列表


@dataclass
class ListResponse:
    """列表响应模型"""

    id: int  #: 列表ID
    name: str  #: 列表名称
    description: str  #: 列表描述
    updated_dt: str  #: 更新时间
    page: int  #: 当前页码
    total_page: int  #: 总页数
    items: list[MediaItem]  #: 媒体项目列表
