# examples

## 使用示例

### 基本用法

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
    
    # 获取剧集单集信息
    print("\n=== 剧集单集信息 ===")
    episode = sdk.get_tv_episode(1396, 1, 3)  # 绝命毒师 S01E03
    print(f"剧集: {episode.name}")
    print(f"第{episode.season_number}季第{episode.episode_number}集")
    print(f"简介: {episode.overview}")
    print(f"播出日期: {episode.air_date}")
    print(f"评分: {episode.vote_average}")
    print(f"时长: {episode.runtime}分钟")
    print(f"有磁力资源: {episode.has_magnet}")
    print(f"有ed2k资源: {episode.has_ed2k}")
    
    # 获取剧集单集磁力资源
    if episode.has_magnet:
        print("\n=== 剧集单集磁力资源 ===")
        episode_magnet = sdk.get_tv_episode_magnet(1396, 1, 3)
        for i, resource in enumerate(episode_magnet.magnet[:2], 1):
            print(f"{i}. {resource.name}")
            print(f"   大小: {resource.size}")
            print(f"   来源: {resource.source}")
            print(f"   质量: {resource.quality}")
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
        print(f"来源: {resource.source}")
        print(f"链接: {resource.link[:50]}...")
        print()
    
    # 获取剧集单集video资源
    print("=== 剧集单集video资源 ===")
    tv_video = sdk.get_tv_episode_video(1396, 3, 4)  # 绝命毒师 S03E04
    for resource in tv_video.video[:2]:
        print(f"剧集: 第{tv_video.season_number}季第{tv_video.episode_number}集")
        print(f"名称: {resource.name}")
        print(f"类型: {resource.type}")
        print(f"来源: {resource.source}")
        print(f"链接: {resource.link[:50]}...")
        print()

if __name__ == "__main__":
    main()
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

# 获取剧集单集信息
nullbr --app-id YOUR_APP_ID tv-episode 1396 1 3

# 获取剧集单集磁力资源
nullbr --app-id YOUR_APP_ID --api-key YOUR_API_KEY tv-episode-magnet 1396 1 3

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

# 获取剧集单集信息
python -m nullbr --app-id YOUR_APP_ID tv-episode 1396 1 3

# 获取剧集单集磁力资源
python -m nullbr --app-id YOUR_APP_ID --api-key YOUR_API_KEY tv-episode-magnet 1396 1 3

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

