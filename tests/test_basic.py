"""
基本测试用例
"""

# import pytest
from nullbr import NullbrSDK
from nullbr.models.base import MediaItem


def test_import():
    """测试包是否能正确导入"""
    assert NullbrSDK is not None


def test_sdk_initialization():
    """测试SDK初始化"""
    sdk = NullbrSDK(app_id="test_app_id")
    assert sdk.app_id == "test_app_id"
    assert sdk.api_key is None
    assert sdk.base_url == "https://api.nullbr.eu.org"


def test_sdk_initialization_with_api_key():
    """测试带API Key的SDK初始化"""
    sdk = NullbrSDK(app_id="test_app_id", api_key="test_api_key")
    assert sdk.app_id == "test_app_id"
    assert sdk.api_key == "test_api_key"


def test_sdk_initialization_with_custom_base_url():
    """测试自定义base_url的SDK初始化"""
    custom_url = "https://custom.api.example.com"
    sdk = NullbrSDK(app_id="test_app_id", base_url=custom_url)
    assert sdk.base_url == custom_url


def test_media_item_creation():
    """测试MediaItem对象创建"""
    item = MediaItem(
        media_type="movie",
        tmdbid=12345,
        poster="poster.jpg",
        title="Test Movie",
        overview="Test overview",
        vote_average=8.5,
        release_date="2024-01-01"
    )

    assert item.media_type == "movie"
    assert item.tmdbid == 12345
    assert item.title == "Test Movie"
    assert item.vote_average == 8.5
