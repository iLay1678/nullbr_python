# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Nullbr Python SDK"
copyright = "2025 iLay1678"
author = "iLay1678"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.autosummary",  # 添加自动摘要扩展
    "myst_parser",
    "sphinx_copybutton",
]

# templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "zh_CN"

# -- MyST Parser configuration ----------------------------------------------
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "substitution",
    "strikethrough",
    "tasklist",
]

# Allow both .rst and .md files
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True
# -- Options for autodoc ----------------------------------------------------
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": "__weakref__",
    "show-inheritance": True,
}

# Autodoc settings for better method documentation
autodoc_member_order = "bysource"
autodoc_typehints = "description"
autodoc_class_signature = "mixed"

# Autosummary settings
autosummary_generate = True
autosummary_generate_overwrite = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
# html_static_path = ["_static"]
html_title = f"{project}"

# TOC tree settings for better navigation
html_show_sourcelink = True

# Global TOC tree depth
master_doc = "index"
html_use_index = True
html_split_index = False

# Theme options for sphinx_book_theme
html_theme_options = {
    "repository_url": "https://github.com/iLay1678/nullbr-python",
    "use_repository_button": False,
    "use_issues_button": False,
    "use_download_button": False,
    "path_to_docs": "docs",
    "repository_branch": "main",
    "show_toc_level": 3,  # 增加到3级以显示方法
    "collapse_navigation": False,  # 不折叠导航
    "navigation_depth": 4,  # 导航深度
}
