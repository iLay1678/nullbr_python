"""
Command Line Interface for nullbr

This module provides a simple CLI for the nullbr SDK.
"""

import argparse
import json
import sys
from dataclasses import asdict

from . import NullbrSDK


def to_dict(obj):
    """将数据类对象递归转换为字典，以便JSON序列化"""
    if hasattr(obj, "__dataclass_fields__"):
        # 这是一个数据类对象
        return asdict(obj)
    elif isinstance(obj, list):
        # 这是一个列表，递归处理每个元素
        return [to_dict(item) for item in obj]
    elif isinstance(obj, dict):
        # 这是一个字典，递归处理每个值
        return {key: to_dict(value) for key, value in obj.items()}
    else:
        # 其他类型直接返回
        return obj


def create_parser() -> argparse.ArgumentParser:
    """创建命令行参数解析器"""
    parser = argparse.ArgumentParser(
        description="nullbr: Python SDK for Nullbr API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument("--app-id", required=True, help="Nullbr API App ID")

    parser.add_argument(
        "--api-key", help="Nullbr API Key (optional, required for some operations)"
    )

    parser.add_argument(
        "--base-url",
        default="https://api.nullbr.eu.org",
        help="API base URL (default: https://api.nullbr.eu.org)",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Search command
    search_parser = subparsers.add_parser("search", help="Search for media")
    search_parser.add_argument("query", help="Search query")
    search_parser.add_argument("--page", type=int, default=1, help="Page number")

    # Movie command
    movie_parser = subparsers.add_parser("movie", help="Get movie information")
    movie_parser.add_argument("tmdbid", type=int, help="TMDB ID")

    # TV command
    tv_parser = subparsers.add_parser("tv", help="Get TV show information")
    tv_parser.add_argument("tmdbid", type=int, help="TMDB ID")

    # Movie ed2k command
    movie_ed2k_parser = subparsers.add_parser(
        "movie-ed2k", help="Get movie ed2k resources"
    )
    movie_ed2k_parser.add_argument("tmdbid", type=int, help="TMDB ID")

    # TV episode ed2k command
    tv_ed2k_parser = subparsers.add_parser(
        "tv-episode-ed2k", help="Get TV episode ed2k resources"
    )
    tv_ed2k_parser.add_argument("tmdbid", type=int, help="TMDB ID")
    tv_ed2k_parser.add_argument("season", type=int, help="Season number")
    tv_ed2k_parser.add_argument("episode", type=int, help="Episode number")

    # Movie video command
    movie_video_parser = subparsers.add_parser(
        "movie-video", help="Get movie video resources (m3u8/http)"
    )
    movie_video_parser.add_argument("tmdbid", type=int, help="TMDB ID")

    # TV episode video command
    tv_video_parser = subparsers.add_parser(
        "tv-episode-video", help="Get TV episode video resources (m3u8/http)"
    )
    tv_video_parser.add_argument("tmdbid", type=int, help="TMDB ID")
    tv_video_parser.add_argument("season", type=int, help="Season number")
    tv_video_parser.add_argument("episode", type=int, help="Episode number")

    # TV episode info command
    tv_episode_parser = subparsers.add_parser(
        "tv-episode", help="Get TV episode information"
    )
    tv_episode_parser.add_argument("tmdbid", type=int, help="TMDB ID")
    tv_episode_parser.add_argument("season", type=int, help="Season number")
    tv_episode_parser.add_argument("episode", type=int, help="Episode number")

    # TV episode magnet command
    tv_episode_magnet_parser = subparsers.add_parser(
        "tv-episode-magnet", help="Get TV episode magnet resources"
    )
    tv_episode_magnet_parser.add_argument("tmdbid", type=int, help="TMDB ID")
    tv_episode_magnet_parser.add_argument("season", type=int, help="Season number")
    tv_episode_magnet_parser.add_argument("episode", type=int, help="Episode number")

    return parser


def main():
    """主入口函数"""
    parser = create_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    # 创建SDK实例
    sdk = NullbrSDK(app_id=args.app_id, api_key=args.api_key, base_url=args.base_url)

    try:
        if args.command == "search":
            result = sdk.search(args.query, args.page)
        elif args.command == "movie":
            result = sdk.get_movie(args.tmdbid)
        elif args.command == "tv":
            result = sdk.get_tv(args.tmdbid)
        elif args.command == "movie-ed2k":
            result = sdk.get_movie_ed2k(args.tmdbid)
        elif args.command == "tv-episode-ed2k":
            result = sdk.get_tv_episode_ed2k(args.tmdbid, args.season, args.episode)
        elif args.command == "movie-video":
            result = sdk.get_movie_video(args.tmdbid)
        elif args.command == "tv-episode-video":
            result = sdk.get_tv_episode_video(args.tmdbid, args.season, args.episode)
        elif args.command == "tv-episode":
            result = sdk.get_tv_episode(args.tmdbid, args.season, args.episode)
        elif args.command == "tv-episode-magnet":
            result = sdk.get_tv_episode_magnet(args.tmdbid, args.season, args.episode)
        else:
            print(f"Unknown command: {args.command}")
            sys.exit(1)

        # 输出结果
        result_dict = to_dict(result)
        print(json.dumps(result_dict, indent=2, ensure_ascii=False))

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
