from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class Movie115Item:
    """115云盘电影资源项目"""

    title: str  #: 电影标题
    size: str  #: 文件大小
    share_link: str  #: 分享链接
    resolution: Optional[str] = None  #: 分辨率，如 "1080p", "4K" 等
    quality: Optional[Union[str, list[str]]] = None  #: 视频质量标签
    season_list: Optional[list[str]] = None  #: 季数列表（主要用于电视剧）


@dataclass
class MovieResponse:
    """电影详情响应模型"""

    id: int  #: 电影ID
    poster: str  #: 海报图片URL
    title: str  #: 电影标题
    overview: str  #: 电影简介
    vote: float  #: 评分
    release_date: str  #: 发布日期
    has_115: bool  #: 是否有115云盘资源
    has_magnet: bool  #: 是否有磁力链接
    has_ed2k: bool  #: 是否有ed2k链接
    has_video: bool  #: 是否有在线视频


@dataclass
class Movie115Response:
    """电影115云盘资源响应模型"""

    id: int  #: 电影ID
    media_type: str  #: 媒体类型
    page: int  #: 当前页码
    total_page: int  #: 总页数
    items: list[Movie115Item]  #: 115云盘资源列表


@dataclass
class MovieMagnetItem:
    """电影磁力链接项目"""

    name: str  #: 资源名称
    size: str  #: 文件大小
    magnet: str  #: 磁力链接
    resolution: str  #: 分辨率
    source: str  #: 资源来源
    quality: Union[str, list[str]]  #: 视频质量标签
    zh_sub: int  #: 中文字幕标识（1表示有，0表示无）


@dataclass
class MovieMagnetResponse:
    """电影磁力链接响应模型"""

    id: int  #: 电影ID
    media_type: str  #: 媒体类型
    magnet: list[MovieMagnetItem]  #: 磁力链接列表


@dataclass
class MovieEd2kItem:
    """电影ed2k链接项目"""

    name: str  #: 资源名称
    size: str  #: 文件大小
    ed2k: str  #: ed2k链接
    resolution: str  #: 分辨率
    source: Optional[str]  #: 资源来源
    quality: Union[str, list[str]]  #: 视频质量标签
    zh_sub: int  #: 中文字幕标识（1表示有，0表示无）


@dataclass
class MovieEd2kResponse:
    """电影ed2k链接响应模型"""

    id: int  #: 电影ID
    media_type: str  #: 媒体类型
    ed2k: list[MovieEd2kItem]  #: ed2k链接列表


@dataclass
class MovieVideoItem:
    """电影在线视频项目"""

    name: str  #: 视频名称
    type: str  #: 视频类型，如 "m3u8" 或 "http"
    link: str  #: 视频链接
    source: Optional[str] = None  #: 视频来源


@dataclass
class MovieVideoResponse:
    """电影在线视频响应模型"""

    id: int  #: 电影ID
    media_type: str  #: 媒体类型
    video: list[MovieVideoItem]  #: 在线视频列表
