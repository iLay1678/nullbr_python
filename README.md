# nullbr-python

![PyPI - Version](https://img.shields.io/pypi/v/nullbr-python)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

Python SDK for Nullbr API - 用于访问 Nullbr API 的 Python SDK

## 功能特性

- 🔍 搜索电影、电视剧、合集和人物
- 🎬 获取电影详细信息和资源链接
- 📺 获取电视剧详细信息和资源链接
- 📚 获取合集信息和资源链接
- 🔗 支持115网盘、磁力链接、电驴链接等多种资源类型
- 🛠️ 命令行工具支持
- 🔒 MIT 许可证

## 安装

### 使用 uv 安装

```bash
uv add nullbr-python
```

### 使用 pip 安装

```bash
pip install nullbr-python
```

### 从源码安装

```bash
git clone https://github.com/iLay1678/nullbr_python.git
cd nullbr_python
uv sync
uv pip install -e .
```

## 快速开始

### 基本用法

```python
from nullbr_python import NullbrSDK

# 初始化SDK
sdk = NullbrSDK(
    app_id="your_app_id",
    api_key="your_api_key"  # 可选，某些操作需要
)

# 搜索电影
results = sdk.search("复仇者联盟")
for item in results.items:
    print(f"{item.title} ({item.media_type})")

# 获取电影详细信息
movie = sdk.get_movie(299536)  # 复仇者联盟4的TMDB ID
print(f"电影名称: {movie.title}")
print(f"评分: {movie.vote}")
print(f"上映日期: {movie.release_date}")

# 获取电影资源（需要API Key）
if movie.has_115:
    resources = sdk.get_movie_115(299536)
    for resource in resources.items:
        print(f"资源: {resource.title} - {resource.size}")
```

### 命令行使用

使用uv：
```bash
# 搜索
uv run python -m nullbr_python.cli --app-id YOUR_APP_ID search "复仇者联盟"

# 获取电影信息
uv run python -m nullbr_python.cli --app-id YOUR_APP_ID movie 299536

# 获取电视剧信息
uv run python -m nullbr_python.cli --app-id YOUR_APP_ID tv 1396
```

如果已安装为全局包：
```bash
# 搜索
nullbr --app-id YOUR_APP_ID search "复仇者联盟"

# 获取电影信息
nullbr --app-id YOUR_APP_ID movie 299536

# 获取电视剧信息
nullbr --app-id YOUR_APP_ID tv 1396
```

## API 参考

### NullbrSDK

主要的SDK类，提供所有API方法。

#### 初始化

```python
sdk = NullbrSDK(
    app_id="your_app_id",
    api_key="your_api_key",  # 可选
    base_url="https://api.nullbr.eu.org"  # 默认值
)
```

#### 方法

##### search(query, page=1)
搜索媒体内容

- `query` (str): 搜索关键词
- `page` (int): 页码，默认为1
- 返回: `SearchResponse` 对象

##### get_movie(tmdbid)
获取电影详细信息

- `tmdbid` (int): 电影的TMDB ID
- 返回: `MovieResponse` 对象

##### get_movie_115(tmdbid, page=1)
获取电影115网盘资源（需要API Key）

- `tmdbid` (int): 电影的TMDB ID
- `page` (int): 页码，默认为1
- 返回: `Movie115Response` 对象

##### get_movie_magnet(tmdbid)
获取电影磁力资源

- `tmdbid` (int): 电影的TMDB ID
- 返回: `MovieMagnetResponse` 对象

##### get_tv(tmdbid)
获取电视剧详细信息

- `tmdbid` (int): 电视剧的TMDB ID
- 返回: `TVResponse` 对象

更多方法请参考源码文档。

## 数据模型

### MediaItem
媒体项目基础信息

### SearchResponse
搜索结果响应

### MovieResponse
电影信息响应

### TVResponse
电视剧信息响应

## 开发

### 安装开发依赖

```bash
uv sync --dev
```

或者使用pip：

```bash
pip install -e ".[dev]"
```

### 代码格式化

```bash
uv run black nullbr_python/
uv run isort nullbr_python/
```

### 运行测试

```bash
uv run pytest
```

## 许可证

本项目采用 MIT 许可证。详情请见 [LICENSE](LICENSE) 文件。

## 贡献

欢迎提交Issue和Pull Request！

## 更新日志

### 0.1.1
- 初始版本
- 支持基本的搜索和获取媒体信息功能
- 命令行工具支持
- MIT许可证
