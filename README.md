# 📄 LaTeX 論文テンプレート

日本語卒業論文用のLaTeXテンプレート。AIコーディングアシスタントとの協調作業を前提としています。

## 🚀 まず初めにこれをやる

1.リポジトリのクローン
```bash
git clone <this-repo>
cd paper
```
2.初期セットアップ（make startでoutputディレクトリにpdfが作成されます）
```bash
make start
```
3.以降はsrcの中のファイルを編集して、必要なmakeコマンドを実行すれば成果物はできます。output/latest/には常に最新版が保存されます。

補足
1.githubの基礎（add commit push clone mergeあたり）は理解している前提です
2.標準的なtex環境があれば動くかと思います
3.binのpythonはPDFの構造上うまく動かないことが多いのでbib作成は頑張ってください
4.IDEとAIエージェントの設定ファイルは各自で作成してください

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
│   ├── preface.tex        読み込み設定とか（最初は無視で良い）
│   ├── sections/          各章
│   ├── references.bib     参考文献
│   └── citation_map.yaml  引用マップ
├── refs/                  論文PDFを置くと自動でBibTeX生成
├── images/                画像を置く（構造化はお任せ）
├── bin/                   今はbib自動生成（自分好きに実行したいコードを格納してみてください）
├── output/latest/         生成されたPDF
├── .gitignore             省略（最初は無視で良い）
├── .latexmkrc             ビルド設定（最初は無視で良い）
├── Makefile               makeコマンドの定義（最初は無視で良い）
└── README.md              使い方
```

## 🤖 AIアシスタントとの使い方

このテンプレートは以下のAIコーディングアシスタントとの協調作業を前提に設計されています：

### 想定対応ツール

| ツール | 説明 |
|--------|------|
| **VS Code Copilot** | GitHub Copilot拡張機能 |
| **Claude Code** | Anthropic Claude CLI |
| **Cursor** | AI-first コードエディタ |
| **Antigravity** | Google Deepmind AIエージェント |

### AI活用のポイント

1. **`citation_map.yaml`** を活用
   - 各章の主張サマリーと必要な参考文献をスロット形式で管理
   - 根幹の主張をここにまとめていくことでAIが参照可能&ブレが減ります
   - 使うかどうかはお任せします

2. **`refs/` にPDFを配置**
   - `make refs` でDOIから自動的にBibTeX生成（調子悪いので参考文献はある程度自分でやる必要があるかも）
   - AIに論文検索と配置を依頼可能

3. **セクション単位の作業**
   - `src/sections/` 内のファイルごとに作業
   - AIに「02_related.tex を書いて」と依頼可能

### 推奨ワークフロー

1. AIと協力して各セクションを執筆
2. `citation_map.yaml` で必要な引用を計画
3. `make realtime` でリアルタイムプレビュー
4. `make refs` で参考文献を更新

## 📋 ライセンス

MIT License