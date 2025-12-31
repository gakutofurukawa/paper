# 📄 LaTeX 論文テンプレート

日本語卒業論文用のLaTeXテンプレート。AIコーディングアシスタントとの協調作業を前提としています。

## 🚀 クイックスタート

1. リポジトリのクローン
   ```bash
   git clone <this-repo>
   cd paper
   ```

2. 初期セットアップ（pdfがoutputに作成されます）
   ```bash
   make start
   ```

3. `src/` 内のファイルを編集して `make pdf` で成果物を生成

**前提条件**
- Git の基本操作（add, commit, push, merge）
- 標準的な TeX 環境

## 📝 コマンド

| コマンド | 内容 |
|---------|------|
| `make start` | 初期セットアップ |
| `make realtime` | 自動ビルド・プレビュー |
| `make pdf` | 高速PDFビルド |
| `make refs` | 参考文献更新と再コンパイル |
| `make clean` | 一時ファイル削除 |
| `make view` | PDFを開く |

## 📁 ディレクトリ構造

```
paper/
├── src/
│   ├── main.tex           メイン文書
│   ├── sections/          各章
│   ├── references.bib     参考文献
│   └── citation_map.yaml  引用マップ
├── refs/                  論文PDFを置くと自動でBibTeX生成
├── images/                画像ファイル
├── output/latest/         生成されたPDF
└── Makefile               makeコマンドの定義
```

## 🤖 AIアシスタントとの使い方

### 想定対応ツール

- **VS Code Copilot** - GitHub Copilot拡張機能
- **Antigravity** - Google AIエージェントIDE
- **Claude Code** - Anthropic Claude CLI
- **Cursor** - AI-first コードエディタ

### AI活用のポイント

1. **セクション単位の作業**
   - `src/sections/` 内のファイルごとに作業
   - AIに「02_related.tex を書いて」と依頼可能

2. **`citation_map.yaml` を活用**（オプション）
   - 各章の主張と参考文献をスロット形式で管理
   - AIが参照しやすく、論文の一貫性が保たれる

3. **参考文献の管理**
   - `refs/` にPDFを配置して `make refs` で自動生成
   - または `references.bib` を直接編集

### 推奨ワークフロー

1. AIと協力して各セクションを執筆
2. `make realtime` でリアルタイムプレビュー
3. `make refs` で参考文献を更新

## 📋 ライセンス

MIT License