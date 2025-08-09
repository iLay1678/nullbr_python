# nullbr

![PyPI - Version](https://img.shields.io/pypi/v/nullbr)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

Python SDK for Nullbr API - 用于访问 Nullbr API 的 Python SDK

## 功能特性

- 🔍 搜索电影、电视剧、合集和人物
- 🎬 获取电影详细信息和资源链接（115网盘、磁力、ed2k、video）
- 📺 获取电视剧详细信息和资源链接（115网盘、磁力、ed2k、video）
- 📚 获取合集信息和资源链接
- 🎯 支持剧集季度和单集资源获取
- 🛠️ 完整的命令行工具支持
- 🔒 MIT 许可证

## 安装

### 使用 uv 安装（推荐）

```bash
uv add nullbr
```

### 使用 pip 安装

```bash
pip install nullbr
```

### 从源码安装

```bash
git clone https://github.com/iLay1678/nullbr-python.git
cd nullbr
uv sync
uv pip install -e .
```

## 快速开始

### 基本用法

```python
from nullbr import NullbrSDK

# 初始化SDK
sdk = NullbrSDK(
    app_id="your_app_id",
    api_key="your_api_key"  # 可选，某些操作需要
)

# 搜索电影
results = sdk.search("复仇者联盟")
for item in results.items:
    print(f"{item.title} ({item.media_type}) - 评分: {item.vote_average}")

# 获取电影详细信息
movie = sdk.get_movie(299536)  # 复仇者联盟4的TMDB ID
print(f"电影名称: {movie.title}")
print(f"评分: {movie.vote}")
print(f"上映日期: {movie.release_date}")

# 获取电影ed2k资源
if movie.has_ed2k:
    ed2k_resources = sdk.get_movie_ed2k(299536)
    for resource in ed2k_resources.ed2k:
        print(f"资源: {resource.name}")
        print(f"大小: {resource.size}")
        print(f"分辨率: {resource.resolution}")
        print(f"中文字幕: {'是' if resource.zh_sub else '否'}")
```

### 命令行使用

#### 方式一：使用全局命令（推荐）

安装后可直接使用 `nullbr` 命令：

```bash
# 搜索
nullbr --app-id YOUR_APP_ID search "复仇者联盟"

# 获取电影信息
nullbr --app-id YOUR_APP_ID movie 299536

# 获取电视剧信息
nullbr --app-id YOUR_APP_ID tv 1396

# 获取电影ed2k资源
nullbr --app-id YOUR_APP_ID --api-key YOUR_API_KEY movie-ed2k 78

# 获取剧集单集ed2k资源
nullbr --app-id YOUR_APP_ID --api-key YOUR_API_KEY tv-episode-ed2k 1396 1 3

# 获取电影video资源（m3u8/http）
nullbr --app-id YOUR_APP_ID --api-key YOUR_API_KEY movie-video 78

# 获取剧集单集video资源（m3u8/http）
nullbr --app-id YOUR_APP_ID --api-key YOUR_API_KEY tv-episode-video 1396 3 4
```

#### 方式二：使用Python模块

```bash
# 搜索
python -m nullbr --app-id YOUR_APP_ID search "复仇者联盟"

# 获取电影信息
python -m nullbr --app-id YOUR_APP_ID movie 299536

# 获取电视剧信息
python -m nullbr --app-id YOUR_APP_ID tv 1396

# 获取电影ed2k资源
python -m nullbr --app-id YOUR_APP_ID --api-key YOUR_API_KEY movie-ed2k 78

# 获取剧集单集ed2k资源
python -m nullbr --app-id YOUR_APP_ID --api-key YOUR_API_KEY tv-episode-ed2k 1396 1 3

# 获取电影video资源（m3u8/http）
python -m nullbr --app-id YOUR_APP_ID --api-key YOUR_API_KEY movie-video 78

# 获取剧集单集video资源（m3u8/http）
python -m nullbr --app-id YOUR_APP_ID --api-key YOUR_API_KEY tv-episode-video 1396 3 4
```

#### 方式三：使用uv运行

```bash
# 搜索
uv run nullbr --app-id YOUR_APP_ID search "复仇者联盟"

# 获取电影信息
uv run nullbr --app-id YOUR_APP_ID movie 299536

# 或者使用Python模块方式
uv run python -m nullbr --app-id YOUR_APP_ID search "复仇者联盟"
```

## API 参考

### NullbrSDK

主要的SDK类，提供所有API方法。

#### 初始化

```python
sdk = NullbrSDK(
    app_id="your_app_id",        # 必需：您的APP ID
    api_key="your_api_key",      # 可选：某些资源操作需要
    base_url="https://api.nullbr.eu.org"  # 默认API地址
)
```

#### 搜索功能

##### search(query, page=1)

搜索电影、电视剧、合集和人物

**参数：**
- `query` (str): 搜索关键词
- `page` (int): 页码，默认为1

**返回：** `SearchResponse` 对象

```python
{
    "page": 1,
    "total_pages": 10,
    "total_results": 200,
    "items": [
        {
            "media_type": "movie",
            "tmdbid": 299536,
            "poster": "https://image.tmdb.org/t/p/w154/poster.jpg",
            "title": "复仇者联盟4：终局之战",
            "overview": "电影简介...",
            "vote_average": 8.4,
            "release_date": "2019-04-24",
            "rank": 1
        }
    ]
}
```

##### get_list(listid, page=1)

获取列表详细信息

**参数：**
- `listid` (int): 列表ID
- `page` (int): 页码，默认为1

**返回：** `ListResponse` 对象

#### 电影功能

##### get_movie(tmdbid)

获取电影详细信息

**参数：**
- `tmdbid` (int): 电影的TMDB ID

**返回：** `MovieResponse` 对象

```python
{
    "id": 299536,
    "poster": "https://image.tmdb.org/t/p/w154/poster.jpg",
    "title": "复仇者联盟4：终局之战",
    "overview": "电影简介...",
    "vote": 8.4,
    "release_date": "2019-04-24",
    "has_115": True,      # 是否有115网盘资源
    "has_magnet": True,   # 是否有磁力链接
    "has_ed2k": True,     # 是否有ed2k链接
    "has_video": False    # 是否有在线视频
}
```

##### get_movie_115(tmdbid, page=1)

获取电影115网盘资源（**需要API Key**）

**参数：**
- `tmdbid` (int): 电影的TMDB ID
- `page` (int): 页码，默认为1

**返回：** `Movie115Response` 对象

```python
{
    "id": 299536,
    "media_type": "movie",
    "page": 1,
    "total_page": 3,
    "items": [
        {
            "title": "复仇者联盟4：终局之战 (2019)",
            "size": "4.2 GB",
            "share_link": "https://115.com/s/sw1a2b3c4d5"
        }
    ]
}
```

##### get_movie_magnet(tmdbid)

获取电影磁力资源

**参数：**
- `tmdbid` (int): 电影的TMDB ID

**返回：** `MovieMagnetResponse` 对象

```python
{
    "id": 299536,
    "media_type": "movie",
    "magnet": [
        {
            "name": "Avengers.Endgame.2019.2160p.BluRay.x265.mkv",
            "size": "15.2 GB",
            "magnet": "magnet:?xt=urn:btih:...",
            "resolution": "2160p",
            "source": "Blu-ray",
            "quality": ["4K", "HDR"],
            "zh_sub": 1  # 1: 有中文字幕, 0: 无中文字幕
        }
    ]
}
```

##### get_movie_ed2k(tmdbid)

获取电影ed2k资源

**参数：**
- `tmdbid` (int): 电影的TMDB ID

**返回：** `MovieEd2kResponse` 对象

```python
{
    "id": 78,
    "media_type": "movie",
    "ed2k": [
        {
            "name": "Blade.Runner.1982.2160p.UHD.BluRay.Remux.HEVC.HDR.mkv",
            "size": "44.69 GB",
            "ed2k": "ed2k://|file|Blade.Runner.1982.2160p.UHD.BluRay.Remux.HEVC.HDR.mkv|47982811361|DBF0FC2DE8A047ABD35A1CDA29CAB5E6|/",
            "resolution": "2160p",
            "source": "Ultra HD Blu-ray",
            "quality": ["Remux", "HDR10", "HD"],
            "zh_sub": 1  # 1: 有中文字幕, 0: 无中文字幕
        }
    ]
}
```

**资源说明：**
- 返回最多8个ed2k资源
- 按是否包含中文字幕分类，从大到小排序
- 优先返回5个最大的有中文字幕资源
- 再返回3个最大的无中文字幕资源



**参数：**
- `tmdbid` (int): 电影的TMDB ID

**返回：** `MovieVideoResponse` 对象

```python
{
    "id": 78,
    "media_type": "movie",
    "video": [
        {
            "name": "1",
            "type": "m3u8",
            "link": "https://m3u8.heimuertv.com/play/82d683b472b04e0292b41d05a739f4e1.m3u8"
        },
        {
            "name": "HD中字",
            "type": "http",
            "link": "https://dow7.lzidw.com/20221016/17423_a0c8e991/银翼杀手.Blade.Runner.1982.国语.mp4"
        },
        {
            "name": "HD中字",
            "type": "m3u8",
            "link": "https://vip1.lz-cdn1.com/20221016/17423_a0c8e991/index.m3u8"
        }
    ]
}
```

**资源说明：**
- 包含m3u8和http两种类型的video资源
- m3u8适用于流媒体播放
- http为直链下载

#### 电视剧功能

##### get_tv(tmdbid)

获取电视剧详细信息

**参数：**
- `tmdbid` (int): 电视剧的TMDB ID

**返回：** `TVResponse` 对象

```python
{
    "id": 1396,
    "poster": "https://image.tmdb.org/t/p/w154/poster.jpg",
    "title": "绝命毒师",
    "overview": "剧集简介...",
    "vote": 9.5,
    "release_date": "2008-01-20",
    "number_of_seasons": 5,
    "has_115": True,
    "has_magnet": True,
    "has_ed2k": True,
    "has_video": False
}
```

##### get_tv_115(tmdbid, page=1)

获取电视剧115网盘资源（**需要API Key**）

**参数：**
- `tmdbid` (int): 电视剧的TMDB ID
- `page` (int): 页码，默认为1

**返回：** `TV115Response` 对象

##### get_tv_season(tmdbid, season_number)

获取电视剧单季详细信息

**参数：**
- `tmdbid` (int): 电视剧的TMDB ID
- `season_number` (int): 季数

**返回：** `TVSeasonResponse` 对象

```python
{
    "tv_show_id": 1396,
    "season_number": 1,
    "name": "第一季",
    "overview": "第一季简介...",
    "air_date": "2008-01-20",
    "poster": "https://image.tmdb.org/t/p/w154/season_poster.jpg",
    "episode_count": 7,
    "vote_average": 9.0,
    "has_magnet": True
}
```

##### get_tv_season_magnet(tmdbid, season_number)

获取电视剧季磁力资源

**参数：**
- `tmdbid` (int): 电视剧的TMDB ID
- `season_number` (int): 季数

**返回：** `TVSeasonMagnetResponse` 对象

##### get_tv_episode_ed2k(tmdbid, season_number, episode_number)

获取剧集单集ed2k资源

**参数：**
- `tmdbid` (int): 电视剧的TMDB ID
- `season_number` (int): 季数
- `episode_number` (int): 集数

**返回：** `TVEpisodeEd2kResponse` 对象

```python
{
    "tv_show_id": 1396,
    "season_number": 1,
    "episode_number": 3,
    "media_type": "tv",
    "ed2k": [
        {
            "name": "绝命毒师.第二季.2009.EP03.BD1080P.X264.AAC.English.CHS-ENG.BDYS.mp4",
            "size": "4.83 GB",
            "ed2k": "ed2k://|file|绝命毒师.第二季.2009.EP03.BD1080P.X264.AAC.English.CHS-ENG.BDYS.mp4|5182481944|594856F827D5F9553576428B8E29DE6A|/",
            "resolution": null,
            "source": null,
            "quality": null,
            "zh_sub": 1
        }
    ]
}
```

##### get_tv_episode_video(tmdbid, season_number, episode_number)

获取剧集单集video资源（m3u8/http）

**参数：**
- `tmdbid` (int): 剧集的TMDB ID
- `season_number` (int): 季数
- `episode_number` (int): 集数

**返回：** `TVEpisodeVideoResponse` 对象

```python
{
    "tv_show_id": 1396,
    "season_number": 3,
    "episode_number": 4,
    "media_type": "tv",
    "video": [
        {
            "type": "m3u8",
            "name": "4",
            "link": "https://m3u8.heimuertv.com/play/e8146ae6dbb14a22a00c841cd3c016b2.m3u8"
        },
        {
            "type": "http",
            "name": "第04集",
            "link": "https://dow4.lzidw.com/20220521/13365_133713b3/绝命毒师S0304.mp4"
        },
        {
            "type": "m3u8",
            "name": "第04集",
            "link": "https://vip.lz-cdn4.com/20220521/13365_133713b3/index.m3u8"
        }
    ]
}
```

#### 合集功能

##### get_collection(tmdbid)

获取电影合集详细信息

**参数：**
- `tmdbid` (int): 合集的TMDB ID

**返回：** `CollectionResponse` 对象

```python
{
    "id": 86311,
    "poster": "https://image.tmdb.org/t/p/w154/collection_poster.jpg",
    "title": "复仇者联盟系列",
    "overview": "合集简介...",
    "vote": "8.1",
    "release_date": "2012-04-25",
    "has_115": True,
    "items": [
        {
            "media_type": "movie",
            "tmdbid": 24428,
            "poster": "https://image.tmdb.org/t/p/w154/poster1.jpg",
            "title": "复仇者联盟",
            "overview": "电影简介...",
            "vote_average": 7.7,
            "release_date": "2012-04-25"
        }
    ]
}
```

##### get_collection_115(tmdbid, page=1)

获取电影合集115网盘资源（**需要API Key**）

**参数：**
- `tmdbid` (int): 合集的TMDB ID
- `page` (int): 页码，默认为1

**返回：** `Collection115Response` 对象

## 命令行工具

### 可用命令

| 命令 | 描述 | 参数 | 需要API Key |
|------|------|------|-------------|
| `search` | 搜索媒体内容 | `<query> [--page]` | ❌ |
| `movie` | 获取电影信息 | `<tmdbid>` | ❌ |
| `tv` | 获取电视剧信息 | `<tmdbid>` | ❌ |
| `movie-ed2k` | 获取电影ed2k资源 | `<tmdbid>` | ✅ |
| `tv-episode-ed2k` | 获取剧集单集ed2k资源 | `<tmdbid> <season> <episode>` | ✅ |
| `movie-video` | 获取电影video资源 | `<tmdbid>` | ✅ |
| `tv-episode-video` | 获取剧集单集video资源 | `<tmdbid> <season> <episode>` | ✅ |

### 使用示例

```bash
# 设置环境变量（推荐）
export NULLBR_APP_ID="your_app_id"
export NULLBR_API_KEY="your_api_key"

# 使用全局命令（推荐）
nullbr --app-id $NULLBR_APP_ID search "权力的游戏"
nullbr --app-id $NULLBR_APP_ID movie 299536
nullbr --app-id $NULLBR_APP_ID --api-key $NULLBR_API_KEY movie-ed2k 78
nullbr --app-id $NULLBR_APP_ID --api-key $NULLBR_API_KEY tv-episode-ed2k 1396 1 3

# 或者使用Python模块方式
python -m nullbr --app-id $NULLBR_APP_ID search "权力的游戏"
python -m nullbr --app-id $NULLBR_APP_ID movie 299536
python -m nullbr --app-id $NULLBR_APP_ID --api-key $NULLBR_API_KEY movie-ed2k 78
python -m nullbr --app-id $NULLBR_APP_ID --api-key $NULLBR_API_KEY tv-episode-ed2k 1396 1 3
python -m nullbr --app-id $NULLBR_APP_ID --api-key $NULLBR_API_KEY movie-video 78
python -m nullbr --app-id $NULLBR_APP_ID --api-key $NULLBR_API_KEY tv-episode-video 1396 3 4
```

### 输出格式

所有命令输出标准JSON格式，方便程序处理：

```bash
# 使用全局命令
nullbr --app-id YOUR_APP_ID search "复仇者联盟" | jq '.items[0].title'

# 或者使用Python模块
python -m nullbr --app-id YOUR_APP_ID search "复仇者联盟" | jq '.items[0].title'
```

## 数据模型

### 基础模型

#### MediaItem
媒体项目基础信息
```python
{
    "media_type": str,      # "movie", "tv", "collection", "person"
    "tmdbid": int,          # TMDB ID
    "poster": str,          # 海报URL
    "title": str,           # 标题
    "overview": str,        # 简介
    "vote_average": float,  # 评分
    "release_date": str,    # 发布日期
    "rank": int            # 搜索排名（仅搜索结果）
}
```

### 响应模型

#### SearchResponse
搜索结果响应
```python
{
    "page": int,           # 当前页码
    "total_pages": int,    # 总页数
    "total_results": int,  # 总结果数
    "items": [MediaItem]   # 媒体项目列表
}
```

#### ListResponse
列表响应
```python
{
    "id": int,             # 列表ID
    "name": str,           # 列表名称
    "description": str,    # 列表描述
    "updated_dt": str,     # 更新时间
    "page": int,           # 当前页码
    "total_page": int,     # 总页数
    "items": [MediaItem]   # 媒体项目列表
}
```

#### MovieResponse
电影信息响应
```python
{
    "id": int,             # 电影ID
    "poster": str,         # 海报URL
    "title": str,          # 电影标题
    "overview": str,       # 电影简介
    "vote": float,         # 评分
    "release_date": str,   # 上映日期
    "has_115": bool,       # 是否有115网盘资源
    "has_magnet": bool,    # 是否有磁力链接
    "has_ed2k": bool,      # 是否有ed2k链接
    "has_video": bool      # 是否有在线视频
}
```

#### TVResponse
电视剧信息响应
```python
{
    "id": int,                  # 电视剧ID
    "poster": str,              # 海报URL
    "title": str,               # 电视剧标题
    "overview": str,            # 电视剧简介
    "vote": float,              # 评分
    "release_date": str,        # 首播日期
    "number_of_seasons": int,   # 季数
    "has_115": bool,            # 是否有115网盘资源
    "has_magnet": bool,         # 是否有磁力链接
    "has_ed2k": bool,           # 是否有ed2k链接
    "has_video": bool           # 是否有在线视频
}
```

### 资源模型

#### Movie115Item / TV115Item
115网盘资源项目
```python
{
    "title": str,          # 资源标题
    "size": str,           # 文件大小
    "share_link": str      # 分享链接
}
```

#### MovieMagnetItem
磁力资源项目
```python
{
    "name": str,                    # 文件名
    "size": str,                    # 文件大小
    "magnet": str,                  # 磁力链接
    "resolution": str,              # 分辨率
    "source": str,                  # 来源（Blu-ray, Web等）
    "quality": str | [str],         # 质量标签
    "zh_sub": int                   # 中文字幕（1有0无）
}
```

#### MovieEd2kItem
ed2k资源项目
```python
{
    "name": str,                    # 文件名
    "size": str,                    # 文件大小
    "ed2k": str,                    # ed2k链接
    "resolution": str,              # 分辨率
    "source": str | null,           # 来源
    "quality": str | [str] | null,  # 质量标签
    "zh_sub": int                   # 中文字幕（1有0无）
}
```

#### MovieVideoItem
video资源项目
```python
{
    "name": str,                    # 资源名称
    "type": str,                    # 资源类型（"m3u8" 或 "http"）
    "link": str                     # 资源链接
}
```

## 完整示例

```python
import os
from nullbr import NullbrSDK

def main():
    # 初始化SDK
    sdk = NullbrSDK(
        app_id=os.getenv("NULLBR_APP_ID"),
        api_key=os.getenv("NULLBR_API_KEY")
    )
    
    # 搜索电影
    print("=== 搜索电影 ===")
    results = sdk.search("银翼杀手")
    for item in results.items[:3]:
        print(f"{item.title} ({item.release_date}) - 评分: {item.vote_average}")
    
    # 获取电影详情
    print("\n=== 电影详情 ===")
    movie = sdk.get_movie(78)  # 银翼杀手
    print(f"标题: {movie.title}")
    print(f"简介: {movie.overview}")
    print(f"评分: {movie.vote}")
    print(f"有ed2k资源: {movie.has_ed2k}")
    
    # 获取ed2k资源
    if movie.has_ed2k:
        print("\n=== ed2k资源 ===")
        ed2k_resources = sdk.get_movie_ed2k(78)
        for i, resource in enumerate(ed2k_resources.ed2k[:3], 1):
            print(f"{i}. {resource.name}")
            print(f"   大小: {resource.size}")
            print(f"   分辨率: {resource.resolution}")
            print(f"   来源: {resource.source}")
            print(f"   中文字幕: {'是' if resource.zh_sub else '否'}")
            print()
    
    # 获取剧集单集ed2k资源
    print("=== 剧集单集ed2k资源 ===")
    tv_ed2k = sdk.get_tv_episode_ed2k(1396, 1, 1)  # 绝命毒师 S01E01
    for resource in tv_ed2k.ed2k[:2]:
        print(f"剧集: 第{tv_ed2k.season_number}季第{tv_ed2k.episode_number}集")
        print(f"文件: {resource.name}")
        print(f"大小: {resource.size}")
        print(f"中文字幕: {'是' if resource.zh_sub else '否'}")
        print()
    
    # 获取电影video资源
    print("=== 电影video资源 ===")
    movie_video = sdk.get_movie_video(78)  # 银翼杀手
    for resource in movie_video.video[:3]:
        print(f"名称: {resource.name}")
        print(f"类型: {resource.type}")
        print(f"链接: {resource.link[:50]}...")
        print()
    
    # 获取剧集单集video资源
    print("=== 剧集单集video资源 ===")
    tv_video = sdk.get_tv_episode_video(1396, 3, 4)  # 绝命毒师 S03E04
    for resource in tv_video.video[:2]:
        print(f"剧集: 第{tv_video.season_number}季第{tv_video.episode_number}集")
        print(f"名称: {resource.name}")
        print(f"类型: {resource.type}")
        print(f"链接: {resource.link[:50]}...")
        print()

if __name__ == "__main__":
    main()
```

## 错误处理

SDK会抛出以下异常：

- `httpx.HTTPError`: API请求失败
- `ValueError`: 参数错误（如缺少API Key）

```python
try:
    movie = sdk.get_movie(299536)
except httpx.HTTPError as e:
    print(f"API请求失败: {e}")
except ValueError as e:
    print(f"参数错误: {e}")
```

## 开发

### 安装开发依赖

```bash
uv sync --dev
```

### 代码格式化和检查

```bash
# 格式化代码
uv run ruff format nullbr/

# 检查和修复代码
uv run ruff check --fix nullbr/

# 仅检查代码
uv run ruff check nullbr/
```

### 运行测试

```bash
uv run pytest
```

### 构建发布

```bash
uv build
```

## 许可证

本项目采用 MIT 许可证。详情请见 [LICENSE](LICENSE) 文件。

## 贡献

欢迎提交Issue和Pull Request！

### 贡献指南

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 更新日志

### v1.0.3

- ✅ 添加了电影video资源获取功能（m3u8/http）
- ✅ 添加了剧集单集video资源获取功能（m3u8/http）
- ✅ 添加了剧集单集ed2k资源获取功能
- ✅ 修复了CLI命令行使用问题，添加了`__main__.py`
- ✅ 优化了类型注解，使用Python 3.9+的内置泛型
- ✅ 完善了CLI命令行工具
- ✅ 增强了文档和示例代码

### v1.0.0

- 🎉 初始版本发布
- ✅ 支持搜索、电影、电视剧、合集信息获取
- ✅ 支持115、磁力、ed2k资源获取
- ✅ 提供完整的命令行工具