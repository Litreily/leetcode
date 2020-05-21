# About

得益于 My Best Friend [小田君](https://www.smslit.top/) 的诱导，嗯~是诱导，肯定是诱导，我也开始使用上了 ==mkdocs==

## Installation

### mkdocs-material

本站点使用 [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) 部署，使用 `pip3` 安装，由于安装过程包含了`mkdocs`，所以无需单独安装。

```zsh
pip3 install mkdocs-material
```

### extensions

mkdocs-material 包含大量的 [extensions](https://squidfunk.github.io/mkdocs-material/extensions/admonition/) ，可以在配置文件 `mkdocs.yml` 中启用，目前尚未开启所有扩展，实际使用过程中有新的需求再取消注释即可。

```zsh
markdown_extensions:
  - admonition
  - codehilite
  - footnotes
  - meta
  - toc:
      permalink: true
  # - pymdownx.arithmatex
  - pymdownx.betterem:
      smart_enable: all
  # - pymdownx.caret
  # - pymdownx.critic
  # - pymdownx.details
  - pymdownx.emoji:
      emoji_index: !!python/name:materialx.emoji.twemoji
      emoji_generator: !!python/name:materialx.emoji.to_svg
  # - pymdownx.highlight:
  #     linenums_style: pymdownx-inline
  # - pymdownx.inlinehilite
  # - pymdownx.keys
  # - pymdownx.magiclink
  - pymdownx.mark
  # - pymdownx.smartsymbols
  # - pymdownx.snippets:
  #     check_paths: true
  - pymdownx.superfences
  - pymdownx.tabbed
  - pymdownx.tasklist:
      custom_checkbox: true
  - pymdownx.tilde
```

### plugins

站点可以使用一些额外的插件，其中某些插件需要单独安装

!!! note "plugins"
    - [X] [search](https://squidfunk.github.io/mkdocs-material/plugins/search/): 搜索功能，目前貌似不支持中文，遗憾😓
    - [X] [minification](https://squidfunk.github.io/mkdocs-material/plugins/minification/): 压缩html文件
    ```zsh
    pip3 install mkdocs-minify-plugin
    ```
    - [ ] [Revision Date](https://squidfunk.github.io/mkdocs-material/plugins/revision-date/): 在页尾显示 `last updated` 时间
    ```zsh
    pip3 install mkdocs-git-revision-date-localized-plugin
    ```
    - [ ] [Awesome pages](https://squidfunk.github.io/mkdocs-material/plugins/awesome-pages/): 页面管理功能，可以对目录下的文档进行折叠、隐藏、排序等操作
    ```zsh
    pip3 install mkdocs-awesome-pages-plugin
    ```

## mkdocs

安装后，使用 `mkdocs` 创建文档目录、运行本地server、生成站点文件或部署至远程server

```zsh
# Create docs for leetcode
mkdocs new leetcode

# Running server on localhost:8000
mkdocs serve

# Build site
mkdocs build [--clean]

# deploy to github branch gh-pages
mkdocs gh-deploy
```

## Reference

- [mkdocs docs](https://www.mkdocs.org)
- [mkdocs 中文文档](https://markdown-docs-zh.readthedocs.io/zh_CN/latest/)
- [material for mkdocs](https://squidfunk.github.io/mkdocs-material/)
- [PyMdown Extensions Documentation](https://facelessuser.github.io/pymdown-extensions/)
