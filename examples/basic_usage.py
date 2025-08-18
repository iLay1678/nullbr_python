#!/usr/bin/env python3
"""
nullbr 基本使用示例

这个示例展示了如何使用 nullbr SDK 进行基本操作。
"""

import os

from nullbr import NullbrSDK


def main():
    # 从环境变量获取配置，或者直接设置
    app_id = os.getenv("NULLBR_APP_ID", "your_app_id_here")
    api_key = os.getenv("NULLBR_API_KEY")  # 可选

    # 初始化SDK
    sdk = NullbrSDK(app_id=app_id, api_key=api_key)

    print("=== nullbr SDK 基本使用示例 ===\n")

    # 1. 搜索示例
    print("1. 搜索电影...")
    try:
        search_results = sdk.search("复仇者联盟", page=1)
        print(f"搜索结果: {search_results.total_results} 个")
        print(f"总页数: {search_results.total_pages}")

        for i, item in enumerate(search_results.items[:3], 1):
            print(f"  {i}. {item.title} ({item.media_type})")
            print(f"     TMDB ID: {item.tmdbid}")
            print(f"     评分: {item.vote_average}")
            print()
    except Exception as e:
        print(f"搜索失败: {e}")

    # 2. 获取电影信息示例
    print("2. 获取电影详细信息...")
    try:
        # 使用复仇者联盟4的TMDB ID
        movie = sdk.get_movie(299536)
        print(f"电影名称: {movie.title}")
        print(f"简介: {movie.overview[:100]}...")
        print(f"评分: {movie.vote}")
        print(f"上映日期: {movie.release_date}")
        print(f"是否有115资源: {movie.has_115}")
        print(f"是否有磁力资源: {movie.has_magnet}")
        print()
    except Exception as e:
        print(f"获取电影信息失败: {e}")

    # 3. 获取电视剧信息示例
    print("3. 获取电视剧详细信息...")
    try:
        # 使用权力的游戏的TMDB ID
        tv = sdk.get_tv(1399)
        print(f"剧集名称: {tv.name}")
        print(f"简介: {tv.overview[:100]}...")
        print(f"评分: {tv.vote}")
        print(f"首播日期: {tv.first_air_date}")
        print(f"是否有115资源: {tv.has_115}")
        print()
    except Exception as e:
        print(f"获取电视剧信息失败: {e}")

    # 4. 获取资源示例（需要API Key）
    if api_key:
        print("4. 获取资源信息...")
        try:
            # 获取磁力资源
            magnet_resources = sdk.get_movie_magnet(299536)
            print(f"磁力资源数量: {len(magnet_resources.magnet)}")
            for i, resource in enumerate(magnet_resources.magnet[:2], 1):
                print(f"  {i}. {resource.name}")
                print(f"     大小: {resource.size}")
                print()

            # 获取电影ed2k资源
            print("5. 获取电影ed2k资源...")
            ed2k_resources = sdk.get_movie_ed2k(78)  # 银翼杀手
            print(f"ed2k资源数量: {len(ed2k_resources.ed2k)}")
            for i, resource in enumerate(ed2k_resources.ed2k[:2], 1):
                print(f"  {i}. {resource.name}")
                print(f"     大小: {resource.size}")
                print(f"     分辨率: {resource.resolution}")
                print(f"     中文字幕: {'是' if resource.zh_sub else '否'}")
                print()

            # 获取剧集单集ed2k资源
            print("6. 获取剧集单集ed2k资源...")
            tv_ed2k_resources = sdk.get_tv_episode_ed2k(1396, 1, 3)  # 绝命毒师 S01E03
            print(f"剧集ed2k资源数量: {len(tv_ed2k_resources.ed2k)}")
            for i, resource in enumerate(tv_ed2k_resources.ed2k[:2], 1):
                print(f"  {i}. {resource.name}")
                print(f"     大小: {resource.size}")
                print(f"     分辨率: {resource.resolution}")
                print(f"     中文字幕: {'是' if resource.zh_sub else '否'}")
                print()

            # 获取电影video资源
            print("7. 获取电影video资源...")
            video_resources = sdk.get_movie_video(78)  # 银翼杀手
            print(f"video资源数量: {len(video_resources.video)}")
            for i, resource in enumerate(video_resources.video[:3], 1):
                print(f"  {i}. {resource.name}")
                print(f"     类型: {resource.type}")
                print(f"     来源: {resource.source}")
                print(f"     链接: {resource.link[:50]}...")
                print()

            # 获取剧集单集video资源
            print("8. 获取剧集单集video资源...")
            tv_video_resources = sdk.get_tv_episode_video(1396, 3, 4)  # 绝命毒师 S03E04
            print(f"剧集video资源数量: {len(tv_video_resources.video)}")
            for i, resource in enumerate(tv_video_resources.video[:2], 1):
                print(f"  {i}. {resource.name}")
                print(f"     类型: {resource.type}")
                print(f"     来源: {resource.source}")
                print(f"     链接: {resource.link[:50]}...")
                print()
        except Exception as e:
            print(f"获取资源失败: {e}")
    else:
        print("4. 跳过资源获取（需要设置 API Key）")

    print("示例运行完成！")
    print("\n要设置API配置，请设置环境变量:")
    print("export NULLBR_APP_ID='your_app_id'")
    print("export NULLBR_API_KEY='your_api_key'")


if __name__ == "__main__":
    main()
