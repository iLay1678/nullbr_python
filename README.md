# nullbr

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/nullbr)
![PyPI - Version](https://img.shields.io/pypi/v/nullbr)
![PyPI - Downloads](https://img.shields.io/pypi/dm/nullbr)
![PyPI - Format](https://img.shields.io/pypi/format/nullbr)
![PyPI - Status](https://img.shields.io/pypi/status/nullbr)

Python SDK for Nullbr API - 用于访问 Nullbr API 的 Python SDK

## 功能特性

- 🔍 搜索电影、电视剧、合集和人物
- 🎬 获取电影详细信息和资源链接（115网盘、磁力、ed2k、video）
- 📺 获取电视剧详细信息和资源链接（115网盘、磁力、ed2k、video）
- 📚 获取合集信息和资源链接
- 🎯 支持剧集季度和单集资源获取
- 🛠️ 完整的命令行工具支持
- 🔄 内置HTTP重试机制，提高请求可靠性
- 🔒 MIT 许可证

## 安装

### 使用 uv 安装（推荐）

```bash
uv add nullbr
```

### 使用 [pip](https://pypi.org/project/nullbr/) 安装

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


## 文档

- **[完整API文档](https://nullbr.readthedocs.io/zh-cn/latest/reference/api.html)** - 详细的API参考和使用指南
- **[使用示例](https://nullbr.readthedocs.io/zh-cn/latest/reference/examples.html)** - 各种功能的使用示例

## 特性说明

### 内置重试机制

- 自动重试失败的HTTP请求，默认最多重试3次
- 针对临时错误状态码：429、500/502/503/504、408
- 指数退避策略，重试间隔逐渐增加
- 适用于所有HTTP方法，提高请求稳定性

### 错误处理

```python
import httpx

try:
    movie = await sdk.get_movie(299536)
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

### 构建文档

```bash
uv run pytest
```

### 构建发布

```bash
uv build
```

## 许可证

本项目采用 MIT 许可证。详情请见 [LICENSE](https://github.com/iLay1678/nullbr_python/blob/main/LICENSE) 文件。

## 贡献

欢迎提交Issue和Pull Request！

### 贡献指南

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 更新日志

### v1.0.7

- 🔧 **代码重构**：TV相关响应类不再使用Movie的响应类
  - 📺 新增 `TVMagnetItem`、`TVEd2kItem`、`TVVideoItem` 专用于TV资源
  - 🎯 提升代码结构清晰度和类型安全性
  - ✅ 向后兼容，功能保持不变

### v1.0.6

- ✅ **新增剧集单集信息功能**：`get_tv_episode()` - 获取剧集单集详细信息
  - 📺 支持获取单集名称、简介、播出日期、评分、时长等详细信息
  - 🔍 返回单集的资源可用性标识（磁力、ed2k等）
- ✅ **新增剧集单集磁力资源功能**：`get_tv_episode_magnet()` - 获取剧集单集磁力资源
  - 🧲 支持获取单集的磁力链接资源
  - 📋 按中文字幕分类排序，返回最多5个资源
  - 🎯 优先返回有中文字幕的资源
- ✅ **扩展CLI命令**：新增 `tv-episode` 和 `tv-episode-magnet` 命令
- ✅ 完善API文档和使用示例
- ✅ 向后兼容，所有原有功能保持不变

### v1.0.5

- ✅ **API 同步更新**：同步上游API更新内容
  - 🎬 video资源接口新增 `source` 字段，标识资源来源（HD、WebRip等）
  - 💾 115网盘资源接口新增 `resolution`、`quality`、`season_list` 字段
  - 📚 增强资源信息展示，提供更详细的资源质量信息
- ✅ 更新数据模型以支持新字段
- ✅ 完善API文档和示例代码
- ✅ 向后兼容，新字段均为可选参数

### v1.0.4

- ✅ 添加HTTP重试机制，提高请求稳定性和可靠性

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