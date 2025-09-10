# Makefile for Sphinx documentation

# 可以通过覆盖这些变量来自定义构建
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# 将其放在第一位，以便 "make" 无参数执行 "make help"。
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile clean html serve

# 捕获 "make html" 等命令，并将其委托给 Sphinx Makefile
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# 自定义命令
clean:
	rm -rf $(BUILDDIR)/*

html:
	$(SPHINXBUILD) -b html $(SOURCEDIR) $(BUILDDIR)/html

serve:
	@echo "serving docs on http://localhost:8000"
	@cd $(BUILDDIR)/html && /Users/ilay/project/nullbr_python/.venv/bin/python -m http.server 8000
