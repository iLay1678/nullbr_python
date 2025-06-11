# 发布说明

本文档说明如何发布 nullbr-python 包到 PyPI。

## 自动发布设置

### 1. PyPI API Token 设置

首先需要在 PyPI 上创建 API Token：

1. 登录到 [PyPI](https://pypi.org)
2. 进入 Account Settings > API tokens
3. 点击 "Add API token"
4. 输入 token 名称（如：`nullbr-python-github-actions`）
5. 选择 Scope 为 "Entire account" 或指定项目
6. 创建并复制 token

### 2. GitHub Secrets 配置

在 GitHub 仓库中设置 secrets：

1. 进入仓库 Settings > Secrets and variables > Actions
2. 点击 "New repository secret"
3. Name: `PYPI_API_TOKEN`
4. Value: 粘贴从 PyPI 复制的 token（包括 `pypi-` 前缀）
5. 点击 "Add secret"

### 3. 发布流程

发布是通过 GitHub Releases 自动触发的：

1. **准备发布**：
   ```bash
   # 更新版本号（在 pyproject.toml 中）
   version = "0.1.1"
   
   # 提交更改
   git add .
   git commit -m "Bump version to 0.1.1"
   git push origin main
   ```

2. **创建 Release**：
   - 在 GitHub 上进入 Releases 页面
   - 点击 "Create a new release"
   - Tag version: `v0.1.1`
   - Release title: `Release v0.1.1`
   - 描述更新内容
   - 点击 "Publish release"

3. **自动发布**：
   - GitHub Action 会自动触发
   - 运行测试和代码格式检查
   - 构建包
   - 发布到 PyPI

## 手动发布

如果需要手动发布：

```bash
# 安装构建工具
uv sync --dev

# 运行测试
uv run pytest

# 代码格式检查
uv run black nullbr_python/
uv run isort nullbr_python/

# 构建包
uv build

# 检查包
uv run twine check dist/*

# 发布到 PyPI
uv run twine upload dist/*
```

## 版本控制

使用语义化版本控制：

- `0.1.1` - 初始版本
- `0.1.1` - 补丁版本（bug修复）
- `0.2.0` - 小版本（新功能，向后兼容）
- `1.0.0` - 大版本（重大更改，可能不向后兼容）

## 发布检查清单

发布前请确认：

- [ ] 更新了版本号
- [ ] 更新了 CHANGELOG 或 Release Notes
- [ ] 运行了所有测试
- [ ] 检查了代码格式
- [ ] 确认依赖项是最新的
- [ ] 验证了 CI/CD 流程

## 故障排除

### PyPI 发布失败

1. 检查 PyPI API Token 是否正确设置
2. 确认版本号没有重复
3. 检查包的元数据是否完整

### CI 测试失败

1. 检查代码格式：`uv run black --check nullbr_python/`
2. 检查导入排序：`uv run isort --check-only nullbr_python/`
3. 运行测试：`uv run pytest` 