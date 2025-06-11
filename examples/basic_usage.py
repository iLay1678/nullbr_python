#!/usr/bin/env python3
"""
nullbr-python 基本使用示例

这个示例展示了如何使用 nullbr-python SDK 进行基本操作。
"""

import os
from nullbr_python import NullbrSDK


def main():
    # 从环境变量获取配置，或者直接设置
    app_id = os.getenv("NULLBR_APP_ID", "your_app_id_here")
    api_key = os.getenv("NULLBR_API_KEY")  # 可选
    
    # 初始化SDK
    sdk = NullbrSDK(app_id=app_id, api_key=api_key)
    
    print("=== nullbr-python SDK 基本使用示例 ===\n")
    
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
            print(f"磁力资源数量: {len(magnet_resources.items)}")
            for i, resource in enumerate(magnet_resources.items[:2], 1):
                print(f"  {i}. {resource.title}")
                print(f"     大小: {resource.size}")
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