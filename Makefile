# LaTeX論文コンパイル用Makefile

# 変数定義
TARGET = main
SRC_DIR = src
OUTPUT_DIR = output/latest
LATEX = platex
BIBTEX = pbibtex
DVIPDF = dvipdfmx
VIEWER = open

# デフォルトターゲット
.PHONY: start pdf realtime refs clean help

# 🚀 初期セットアップ（ディレクトリ作成＋初回ビルド）
start:
	@echo "🚀 初期セットアップを開始..."
	@mkdir -p $(OUTPUT_DIR)
	@echo "✅ ディレクトリを作成しました"
	@$(MAKE) pdf
	@echo ""
	@echo "✨ セットアップ完了！以下のコマンドが使えます："
	@echo "  make pdf       - PDFビルド"
	@echo "  make realtime  - 自動ビルド＆プレビュー"
	@echo "  make refs      - 参考文献の再コンパイル"
	@echo "  make clean     - 一時ファイル削除"

# 📄 通常ビルド（高速モード）
pdf:
	@echo "📄 PDFをビルドしています..."
	@mkdir -p $(OUTPUT_DIR)
	@cd $(SRC_DIR) && $(LATEX) $(TARGET).tex
	@cd $(SRC_DIR) && $(DVIPDF) $(TARGET).dvi
	@cp $(SRC_DIR)/$(TARGET).pdf $(OUTPUT_DIR)/
	@echo "✅ PDFを $(OUTPUT_DIR)/$(TARGET).pdf に出力しました"

# 🔄 自動ビルド＋プレビュー更新（ファイル変更検知）
realtime:
	@echo "🔄 リアルタイムプレビューを開始（Ctrl+C で停止）..."
	@echo "📝 src/sections/*.tex を編集すると自動でPDF更新されます"
	@mkdir -p $(OUTPUT_DIR)
	@cd $(SRC_DIR) && latexmk -pvc -pdf $(TARGET).tex

# 📚 参考文献の完全処理（自動生成 → コンパイル）
refs:
	@echo "📚 参考文献を処理しています..."
	@echo ""
	@echo "⚙️  ステップ1: refs/内のPDFから自動生成"
	@python3 bin/update_bib.py
	@echo ""
	@echo "⚙️  ステップ2: 参考文献込みで完全コンパイル"
	@mkdir -p $(OUTPUT_DIR)
	@cd $(SRC_DIR) && $(LATEX) $(TARGET).tex
	@cd $(SRC_DIR) && $(BIBTEX) $(TARGET)
	@cd $(SRC_DIR) && $(LATEX) $(TARGET).tex
	@cd $(SRC_DIR) && $(LATEX) $(TARGET).tex
	@cd $(SRC_DIR) && $(DVIPDF) $(TARGET).dvi
	@cp $(SRC_DIR)/$(TARGET).pdf $(OUTPUT_DIR)/
	@echo "✅ 参考文献込みでPDFを $(OUTPUT_DIR)/$(TARGET).pdf に出力しました"

# 🧹 一時ファイル削除
clean:
	@echo "�� 一時ファイルを削除しています..."
	@cd $(SRC_DIR) && rm -f *.aux *.log *.dvi *.bbl *.blg *.toc *.lof *.lot *.out *.fdb_latexmk *.fls *.synctex.gz
	@rm -rf $(OUTPUT_DIR)/*.dvi $(OUTPUT_DIR)/*.aux $(OUTPUT_DIR)/*.log
	@echo "✅ 削除完了"

# 📖 PDFを開く
view:
	@$(VIEWER) $(OUTPUT_DIR)/$(TARGET).pdf

# ❓ ヘルプ
help:
	@echo "📘 利用可能なコマンド："
	@echo ""
	@echo "  make start     - 🚀 初期セットアップ（初回のみ）"
	@echo "  make pdf       - 📄 通常ビルド（高速）"
	@echo "  make realtime  - 🔄 自動ビルド＋プレビュー更新"
	@echo "  make refs      - 📚 参考文献の完全コンパイル"
	@echo "  make clean     - 🧹 一時ファイル削除"
	@echo ""
	@echo "  make view      - 📖 PDFを開く"
	@echo "  make help      - ❓ このヘルプを表示"
	@echo ""
	@echo "📁 出力先: $(OUTPUT_DIR)/$(TARGET).pdf"

# 依存関係の明示
$(SRC_DIR)/$(TARGET).tex: 
$(SRC_DIR)/references.bib:
