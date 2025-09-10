"""
nullbr: Python SDK for Nullbr API

A Python SDK for accessing the Nullbr API to search and retrieve information
about movies, TV shows, collections, and their resources.
"""

__version__ = "1.0.7"
__author__ = "nullbr"
__license__ = "MIT"

import time

import httpx

from .models.base import MediaItem
from .models.collection import Collection115Response, CollectionResponse
from .models.movie import (
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
from .models.search import ListResponse, SearchResponse
from .models.tv import (
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

# 导出主要的类和函数
__all__ = [
    "NullbrSDK",
    "MediaItem",
    "SearchResponse",
    "ListResponse",
    "MovieResponse",
    "Movie115Response",
    "MovieMagnetResponse",
    "MovieEd2kResponse",
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


class NullbrSDK:
    def __init__(
        self,
        app_id: str,
        api_key: str = None,
        base_url: str = "https://api.nullbr.eu.org",
        max_retries: int = 3,
        backoff_factor: float = 1.0,
    ):
        """
        初始化 Nullbr SDK

        Args:
            app_id: App ID
            api_key: API Key (可选，获取具体资源时需要)
            base_url: base URL (default: https://api.nullbr.eu.org)
            max_retries: 最大重试次数 (default: 3)
            backoff_factor: 重试的指数等待时间 单位秒 (default: 1.0)"""
        self.app_id = app_id
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

        # 重试的HTTP状态码
        self.retry_status_codes = {429, 500, 502, 503, 504, 408}

        self.session = httpx.Client()
        self.session.headers.update({"X-APP-ID": app_id})
        if api_key:
            self.session.headers.update({"X-API-KEY": api_key})

    def _request(self, method: str, url: str, params: dict = None) -> dict:
        """
        统一的API请求方法，包含重试机制和日志记录

        Args:
            method: HTTP方法 (GET/POST等)
            url: 请求URL
            params: 请求参数

        Returns:
            响应的JSON数据

        Raises:
            httpx.HTTPError: 当API返回非200状态码时
        """
        import logging

        logger = logging.getLogger(__name__)

        last_exception = None

        for attempt in range(self.max_retries + 1):
            try:
                logger.info(f"Requesting {method} {url} (attempt {attempt + 1})")
                if params is not None:
                    logger.debug(f"Request params: {params}")

                response = self.session.request(method, url, params=params)

                if response.is_success:
                    logger.info(f"Response status: {response.status_code}")
                    logger.debug(f"Response data: {response.json()}")
                    return response.json()

                # 检查是否是可重试的状态码
                if response.status_code in self.retry_status_codes:
                    if attempt < self.max_retries:
                        wait_time = self.backoff_factor * (2**attempt)
                        logger.warning(
                            f"API returned {response.status_code}, retrying in {wait_time:.1f}s "
                            f"(attempt {attempt + 1}/{self.max_retries + 1})"
                        )
                        time.sleep(wait_time)
                        continue

                # 不是可重试状态码或者重试次数用完，直接抛出异常
                logger.error(f"API returned {response.status_code}")
                try:
                    error_data = response.json()
                    logger.error(f"Response data: {error_data}")
                except Exception:
                    logger.error(f"Response text: {response.text}")
                response.raise_for_status()

            except httpx.RequestError as e:
                last_exception = e
                if attempt < self.max_retries:
                    wait_time = self.backoff_factor * (2**attempt)
                    logger.warning(
                        f"Request failed: {e}, retrying in {wait_time:.1f}s "
                        f"(attempt {attempt + 1}/{self.max_retries + 1})"
                    )
                    time.sleep(wait_time)
                    continue
                else:
                    logger.error(
                        f"Request failed after {self.max_retries + 1} attempts: {e}"
                    )
                    raise

        # 如果所有重试都失败了，抛出最后的异常
        if last_exception:
            raise last_exception

    def search(self, query: str, page: int = 1) -> SearchResponse:
        """搜索合集、电影、剧集、人物

        Args:
            query: 搜索关键词
            page: 页码，默认为1

        Returns:
            SearchResponse 对象

        Raises:
            requests.exceptions.HTTPError: 当API返回非200状态码时
        """
        data = self._request(
            "GET", f"{self.base_url}/search", {"query": query, "page": page}
        )

        items = [
            MediaItem(
                media_type=item.get("media_type"),
                tmdbid=item.get("tmdbid"),
                poster="https://image.tmdb.org/t/p/w154/" + item.get("poster", ""),
                title=item.get("title"),
                overview=item.get("overview"),
                vote_average=item.get("vote_average"),
                release_date=item.get("release_date"),
                rank=item.get("rank"),
            )
            for item in data.get("items", [])
        ]

        return SearchResponse(
            page=data.get("page"),
            total_pages=data.get("total_pages"),
            total_results=data.get("total_results"),
            items=items,
        )

    def get_list(self, listid: int, page: int = 1) -> ListResponse:
        """获取列表详细信息

        Args:
            listid: 列表id
            page: 页码，默认为1

        Returns:
            ListResponse 对象

        Raises:
            requests.exceptions.HTTPError: 当API返回非200状态码时
        """
        data = self._request("GET", f"{self.base_url}/list/{listid}", {"page": page})

        items = [
            MediaItem(
                media_type=item.get("media_type"),
                tmdbid=item.get("tmdbid"),
                poster="https://image.tmdb.org/t/p/w154/" + item.get("poster", ""),
                title=item.get("title"),
                overview=item.get("overview"),
                vote_average=item.get("vote_average"),
                release_date=item.get("release_date"),
            )
            for item in data.get("items", [])
        ]

        return ListResponse(
            id=data.get("id"),
            name=data.get("name"),
            description=data.get("description"),
            updated_dt=data.get("updated_dt"),
            page=data.get("page"),
            total_page=data.get("total_page"),
            items=items,
        )

    def get_movie(self, tmdbid: int) -> MovieResponse:
        """获取电影详细信息

        Args:
            tmdbid: 电影的TMDB ID

        Returns:
            MovieResponse 对象

        Raises:
            requests.exceptions.HTTPError: 当API返回非200状态码时
        """
        data = self._request("GET", f"{self.base_url}/movie/{tmdbid}")

        return MovieResponse(
            id=data.get("id"),
            poster="https://image.tmdb.org/t/p/w154/" + data.get("poster", ""),
            title=data.get("title"),
            overview=data.get("overview"),
            vote=data.get("vote"),
            release_date=data.get("release_date"),
            has_115=data.get("115-flg") == 1,
            has_magnet=data.get("magnet-flg") == 1,
            has_ed2k=data.get("ed2k-flg") == 1,
            has_video=data.get("video-flg") == 1,
        )

    def get_movie_115(self, tmdbid: int, page: int = 1) -> Movie115Response:
        """获取电影网盘资源

        Args:
            tmdbid: 电影的TMDB ID
            page: 页码，默认为1

        Returns:
            Movie115Response 对象

        Raises:
            requests.exceptions.HTTPError: 当API返回非200状态码时
            ValueError: 当未设置API KEY时
        """
        if not self.api_key:
            raise ValueError("API KEY is required for this operation")

        data = self._request(
            "GET", f"{self.base_url}/movie/{tmdbid}/115", {"page": page}
        )

        items = [
            Movie115Item(
                title=item.get("title"),
                size=item.get("size"),
                share_link=item.get("share_link"),
                resolution=item.get("resolution"),
                quality=item.get("quality"),
                season_list=item.get("season_list"),
            )
            for item in data.get("115", [])
        ]

        return Movie115Response(
            id=data.get("id"),
            media_type=data.get("media_type"),
            page=data.get("page"),
            total_page=data.get("total_page"),
            items=items,
        )

    def get_movie_magnet(self, tmdbid: int) -> MovieMagnetResponse:
        """获取电影磁力资源

        Args:
            tmdbid: 电影的TMDB ID

        Returns:
            MovieMagnetResponse 对象

        Raises:
            requests.exceptions.HTTPError: 当API返回非200状态码时
            ValueError: 当未设置API KEY时
        """
        data = self._request("GET", f"{self.base_url}/movie/{tmdbid}/magnet")

        items = [
            MovieMagnetItem(
                name=item.get("name"),
                size=item.get("size"),
                magnet=item.get("magnet"),
                resolution=item.get("resolution"),
                source=item.get("source"),
                quality=item.get("quality"),
                zh_sub=item.get("zh_sub"),
            )
            for item in data.get("magnet", [])
        ]

        return MovieMagnetResponse(
            id=data.get("id"), media_type=data.get("media_type"), magnet=items
        )

    def get_movie_ed2k(self, tmdbid: int) -> MovieEd2kResponse:
        """获取电影电驴资源

        Args:
            tmdbid: 电影的TMDB ID

        Returns:
            MovieEd2kResponse 对象

        Raises:
            requests.exceptions.HTTPError: 当API返回非200状态码时
            ValueError: 当未设置API KEY时
        """
        data = self._request("GET", f"{self.base_url}/movie/{tmdbid}/ed2k")

        items = [
            MovieEd2kItem(
                name=item.get("name"),
                size=item.get("size"),
                ed2k=item.get("ed2k"),
                resolution=item.get("resolution"),
                source=item.get("source"),
                quality=item.get("quality"),
                zh_sub=item.get("zh_sub"),
            )
            for item in data.get("ed2k", [])
        ]

        return MovieEd2kResponse(
            id=data.get("id"), media_type=data.get("media_type"), ed2k=items
        )

    def get_collection(self, tmdbid: int) -> CollectionResponse:
        """获取电影合集详细信息

        Args:
            tmdbid: 合集的TMDB ID

        Returns:
            CollectionResponse 对象

        Raises:
            requests.exceptions.HTTPError: 当API返回非200状态码时
        """
        data = self._request("GET", f"{self.base_url}/collection/{tmdbid}")

        items = [
            MediaItem(
                media_type=item.get("media_type"),
                tmdbid=item.get("tmdbid"),
                poster="https://image.tmdb.org/t/p/w154/" + item.get("poster", ""),
                title=item.get("title"),
                overview=item.get("overview"),
                vote_average=item.get("vote_average"),
                release_date=item.get("release_date"),
            )
            for item in data.get("items", [])
        ]

        return CollectionResponse(
            id=data.get("id"),
            poster="https://image.tmdb.org/t/p/w154/" + data.get("poster", ""),
            title=data.get("title"),
            overview=data.get("overview"),
            vote=data.get("vote"),
            release_date=data.get("release_date"),
            has_115=data.get("115-flg") == 1,
            items=items,
        )

    def get_tv(self, tmdbid: int) -> TVResponse:
        """获取剧集详细信息

        Args:
            tmdbid: 剧集的TMDB ID

        Returns:
            TVResponse 对象

        Raises:
            requests.exceptions.HTTPError: 当API返回非200状态码时
        """
        data = self._request("GET", f"{self.base_url}/tv/{tmdbid}")

        return TVResponse(
            id=data.get("id"),
            poster="https://image.tmdb.org/t/p/w154/" + data.get("poster", ""),
            title=data.get("title"),
            overview=data.get("overview"),
            vote=data.get("vote"),
            release_date=data.get("release_date"),
            number_of_seasons=data.get("number_of_seasons"),
            has_115=data.get("115-flg") == 1,
            has_magnet=data.get("magnet-flg") == 1,
            has_ed2k=data.get("ed2k-flg") == 1,
            has_video=data.get("video-flg") == 1,
        )

    def get_tv_115(self, tmdbid: int, page: int = 1) -> TV115Response:
        """获取剧集网盘资源

        Args:
            tmdbid: 剧集的TMDB ID
            page: 页码，默认为1

        Returns:
            TV115Response 对象

        Raises:
            requests.exceptions.HTTPError: 当API返回非200状态码时
            ValueError: 当未设置API KEY时
        """
        if not self.api_key:
            raise ValueError("API KEY is required for this operation")

        data = self._request("GET", f"{self.base_url}/tv/{tmdbid}/115", {"page": page})

        items = [
            Movie115Item(
                title=item.get("title"),
                size=item.get("size"),
                share_link=item.get("share_link"),
                resolution=item.get("resolution"),
                quality=item.get("quality"),
                season_list=item.get("season_list"),
            )
            for item in data.get("115", [])
        ]

        return TV115Response(
            id=data.get("id"),
            media_type=data.get("media_type"),
            page=data.get("page"),
            total_page=data.get("total_page"),
            items=items,
        )

    def get_collection_115(self, tmdbid: int, page: int = 1) -> Collection115Response:
        """获取电影合集网盘资源

        Args:
            tmdbid: 合集的TMDB ID
            page: 页码，默认为1

        Returns:
            Collection115Response 对象

        Raises:
            requests.exceptions.HTTPError: 当API返回非200状态码时
            ValueError: 当未设置API KEY时
        """
        data = self._request(
            "GET", f"{self.base_url}/collection/{tmdbid}/115", {"page": page}
        )

        items = [
            Movie115Item(
                title=item.get("title"),
                size=item.get("size"),
                share_link=item.get("share_link"),
                resolution=item.get("resolution"),
                quality=item.get("quality"),
                season_list=item.get("season_list"),
            )
            for item in data.get("115", [])
        ]

        return Collection115Response(
            id=data.get("id"),
            media_type=data.get("media_type"),
            page=data.get("page"),
            total_page=data.get("total_page"),
            items=items,
        )

    def get_tv_season(self, tmdbid: int, season_number: int) -> TVSeasonResponse:
        """获取剧集单季详细信息

        Args:
            tmdbid: 剧集的TMDB ID
            season_number: 季数

        Returns:
            TVSeasonResponse 对象

        Raises:
            requests.exceptions.HTTPError: 当API返回非200状态码时
        """
        data = self._request(
            "GET", f"{self.base_url}/tv/{tmdbid}/season/{season_number}"
        )

        return TVSeasonResponse(
            tv_show_id=data.get("tv_show_id"),
            season_number=data.get("season_number"),
            name=data.get("name"),
            overview=data.get("overview"),
            air_date=data.get("air_date"),
            poseter=data.get("poseter"),
            episode_count=data.get("episode_count"),
            vote_average=data.get("vote_average"),
            has_magnet=data.get("magnet-flg") == 1,
        )

    def get_tv_season_magnet(
        self, tmdbid: int, season_number: int
    ) -> TVSeasonMagnetResponse:
        """获取剧集季磁力资源

        Args:
            tmdbid: 剧集的TMDB ID
            season_number: 季数

        Returns:
            TVSeasonMagnetResponse 对象

        Raises:
            requests.exceptions.HTTPError: 当API返回非200状态码时
            ValueError: 当未设置API KEY时
        """
        data = self._request(
            "GET", f"{self.base_url}/tv/{tmdbid}/season/{season_number}/magnet"
        )

        items = [
            TVMagnetItem(
                name=item.get("name"),
                size=item.get("size"),
                magnet=item.get("magnet"),
                resolution=item.get("resolution"),
                source=item.get("source"),
                quality=item.get("quality"),
                zh_sub=item.get("zh_sub"),
            )
            for item in data.get("magnet", [])
        ]

        return TVSeasonMagnetResponse(
            id=data.get("id"),
            season_number=data.get("season_number"),
            media_type=data.get("media_type"),
            magnet=items,
        )

    def get_tv_episode_ed2k(
        self, tmdbid: int, season_number: int, episode_number: int
    ) -> TVEpisodeEd2kResponse:
        """获取剧集单集ed2k资源

        Args:
            tmdbid: 剧集的TMDB ID
            season_number: 季数
            episode_number: 集数

        Returns:
            TVEpisodeEd2kResponse 对象

        Raises:
            requests.exceptions.HTTPError: 当API返回非200状态码时
            ValueError: 当未设置API KEY时
        """
        data = self._request(
            "GET",
            f"{self.base_url}/tv/{tmdbid}/season/{season_number}/episode/{episode_number}/ed2k",
        )

        items = [
            TVEd2kItem(
                name=item.get("name"),
                size=item.get("size"),
                ed2k=item.get("ed2k"),
                resolution=item.get("resolution"),
                source=item.get("source"),
                quality=item.get("quality"),
                zh_sub=item.get("zh_sub"),
            )
            for item in data.get("ed2k", [])
        ]

        return TVEpisodeEd2kResponse(
            tv_show_id=data.get("tv_show_id"),
            season_number=data.get("season_number"),
            episode_number=data.get("episode_number"),
            media_type=data.get("media_type"),
            ed2k=items,
        )

    def get_movie_video(self, tmdbid: int) -> MovieVideoResponse:
        """获取电影video资源（m3u8/http）

        Args:
            tmdbid: 电影的TMDB ID

        Returns:
            MovieVideoResponse 对象

        Raises:
            requests.exceptions.HTTPError: 当API返回非200状态码时
            ValueError: 当未设置API KEY时
        """
        if not self.api_key:
            raise ValueError("API KEY is required for this operation")

        data = self._request("GET", f"{self.base_url}/movie/{tmdbid}/video")

        items = [
            MovieVideoItem(
                name=item.get("name"),
                type=item.get("type"),
                link=item.get("link"),
                source=item.get("source"),
            )
            for item in data.get("video", [])
        ]

        return MovieVideoResponse(
            id=data.get("id"), media_type=data.get("media_type"), video=items
        )

    def get_tv_episode_video(
        self, tmdbid: int, season_number: int, episode_number: int
    ) -> TVEpisodeVideoResponse:
        """获取剧集单集video资源（m3u8/http）

        Args:
            tmdbid: 剧集的TMDB ID
            season_number: 季数
            episode_number: 集数

        Returns:
            TVEpisodeVideoResponse 对象

        Raises:
            requests.exceptions.HTTPError: 当API返回非200状态码时
            ValueError: 当未设置API KEY时
        """
        if not self.api_key:
            raise ValueError("API KEY is required for this operation")

        data = self._request(
            "GET",
            f"{self.base_url}/tv/{tmdbid}/season/{season_number}/episode/{episode_number}/video",
        )

        items = [
            TVVideoItem(
                name=item.get("name"),
                type=item.get("type"),
                link=item.get("link"),
                source=item.get("source"),
            )
            for item in data.get("video", [])
        ]

        return TVEpisodeVideoResponse(
            tv_show_id=data.get("tv_show_id"),
            season_number=data.get("season_number"),
            episode_number=data.get("episode_number"),
            media_type=data.get("media_type"),
            video=items,
        )

    def get_tv_episode(
        self, tmdbid: int, season_number: int, episode_number: int
    ) -> TVEpisodeResponse:
        """获取剧集单集详细信息

        Args:
            tmdbid: 剧集的TMDB ID
            season_number: 季数
            episode_number: 集数

        Returns:
            TVEpisodeResponse 对象

        Raises:
            requests.exceptions.HTTPError: 当API返回非200状态码时
        """
        data = self._request(
            "GET",
            f"{self.base_url}/tv/{tmdbid}/season/{season_number}/episode/{episode_number}",
        )

        return TVEpisodeResponse(
            tv_show_id=data.get("tv_show_id"),
            season_number=data.get("season_number"),
            episode_number=data.get("episode_number"),
            episode_type=data.get("episode_type"),
            name=data.get("name"),
            overview=data.get("overview"),
            air_date=data.get("air_date"),
            vote_average=data.get("vote_average"),
            poseter=data.get("poseter"),
            runtime=data.get("runtime"),
            has_magnet=data.get("magnet-flg") == 1,
            has_ed2k=data.get("ed2k-flg") == 1,
        )

    def get_tv_episode_magnet(
        self, tmdbid: int, season_number: int, episode_number: int
    ) -> TVEpisodeMagnetResponse:
        """获取剧集单集磁力资源

        Args:
            tmdbid: 剧集的TMDB ID
            season_number: 季数
            episode_number: 集数

        Returns:
            TVEpisodeMagnetResponse 对象

        Raises:
            requests.exceptions.HTTPError: 当API返回非200状态码时
            ValueError: 当未设置API KEY时
        """
        if not self.api_key:
            raise ValueError("API KEY is required for this operation")

        data = self._request(
            "GET",
            f"{self.base_url}/tv/{tmdbid}/season/{season_number}/episode/{episode_number}/magnet",
        )

        items = [
            TVMagnetItem(
                name=item.get("name"),
                size=item.get("size"),
                magnet=item.get("magnet"),
                resolution=item.get("resolution"),
                source=item.get("source"),
                quality=item.get("quality"),
                zh_sub=item.get("zh_sub"),
            )
            for item in data.get("magnet", [])
        ]

        return TVEpisodeMagnetResponse(
            tv_show_id=data.get("tv_show_id"),
            season_number=data.get("season_number"),
            episode_number=data.get("episode_number"),
            media_type=data.get("media_type"),
            magnet=items,
        )
