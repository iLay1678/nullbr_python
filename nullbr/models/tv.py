from dataclasses import dataclass

from .movie import Movie115Item


@dataclass
class TVMagnetItem:
    """电视剧磁力链接项目模型"""

    name: str  #: 文件名
    size: str  #: 文件大小
    magnet: str  #: 磁力链接
    resolution: str  #: 分辨率
    source: str  #: 来源
    quality: str  #: 质量
    zh_sub: bool  #: 是否有中文字幕


@dataclass
class TVEd2kItem:
    """电视剧ed2k链接项目模型"""

    name: str  #: 文件名
    size: str  #: 文件大小
    ed2k: str  #: ed2k链接
    resolution: str  #: 分辨率
    source: str  #: 来源
    quality: str  #: 质量
    zh_sub: bool  #: 是否有中文字幕


@dataclass
class TVVideoItem:
    """电视剧在线视频项目模型"""

    name: str  #: 名称
    type: str  #: 类型
    link: str  #: 链接
    source: str  #: 来源


@dataclass
class TVResponse:
    """电视剧详情响应模型"""

    id: int  #: 电视剧ID
    poster: str  #: 海报图片URL
    title: str  #: 电视剧标题
    overview: str  #: 电视剧简介
    vote: float  #: 评分
    release_date: str  #: 首播日期
    number_of_seasons: int  #: 季数
    has_115: bool  #: 是否有115云盘资源
    has_magnet: bool  #: 是否有磁力链接
    has_ed2k: bool  #: 是否有ed2k链接
    has_video: bool  #: 是否有在线视频


@dataclass
class TV115Response:
    """电视剧115云盘资源响应模型"""

    id: int  #: 电视剧ID
    media_type: str  #: 媒体类型
    page: int  #: 当前页码
    total_page: int  #: 总页数
    items: list[Movie115Item]  #: 115云盘资源列表


@dataclass
class TVSeasonResponse:
    """电视剧季度响应模型"""

    tv_show_id: int  #: 电视剧ID
    season_number: int  #: 季数
    name: str  #: 季度名称
    overview: str  #: 季度简介
    air_date: str  #: 播出日期
    poseter: str  #: 海报图片URL（注意：可能是拼写错误，应为poster）
    episode_count: int  #: 集数
    vote_average: float  #: 平均评分
    has_magnet: bool  #: 是否有磁力链接


@dataclass
class TVSeasonMagnetResponse:
    """电视剧季度磁力链接响应模型"""

    id: int  #: 电视剧ID
    season_number: int  #: 季数
    media_type: str  #: 媒体类型
    magnet: list[TVMagnetItem]  #: 磁力链接列表


@dataclass
class TVEpisodeEd2kResponse:
    """电视剧剧集ed2k链接响应模型"""

    tv_show_id: int  #: 电视剧ID
    season_number: int  #: 季数
    episode_number: int  #: 集数
    media_type: str  #: 媒体类型
    ed2k: list[TVEd2kItem]  #: ed2k链接列表


@dataclass
class TVEpisodeResponse:
    """电视剧剧集响应模型"""

    tv_show_id: int  #: 电视剧ID
    season_number: int  #: 季数
    episode_number: int  #: 集数
    episode_type: str  #: 剧集类型
    name: str  #: 剧集名称
    overview: str  #: 剧集简介
    air_date: str  #: 播出日期
    vote_average: float  #: 评分
    poseter: str  #: 海报图片URL（注意：可能是拼写错误，应为poster）
    runtime: int  #: 运行时长（分钟）
    has_magnet: bool  #: 是否有磁力链接
    has_ed2k: bool  #: 是否有ed2k链接


@dataclass
class TVEpisodeMagnetResponse:
    """电视剧剧集磁力链接响应模型"""

    tv_show_id: int  #: 电视剧ID
    season_number: int  #: 季数
    episode_number: int  #: 集数
    media_type: str  #: 媒体类型
    magnet: list[TVMagnetItem]  #: 磁力链接列表


@dataclass
class TVEpisodeVideoResponse:
    """电视剧剧集在线视频响应模型"""

    tv_show_id: int  #: 电视剧ID
    season_number: int  #: 季数
    episode_number: int  #: 集数
    media_type: str  #: 媒体类型
    video: list[TVVideoItem]  #: 在线视频列表
