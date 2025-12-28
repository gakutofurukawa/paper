# 📄 LaTeX 論文テンプレート

日本語卒業論文用のLaTeXテンプレート。AIコーディングアシスタントとの協調作業を前提としています。

## 🚀 セットアップ（エラーはAIアシスタントで解決してください）

```bash
git clone <this-repo>
cd paper
make start
```

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
└── output/latest/         生成されたPDF
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
   - 各章の主張と必要な参考文献をスロット形式で管理
   - AIに「S3のスロットを埋めて」と依頼可能

2. **`refs/` にPDFを配置**
   - `make refs` でDOIから自動的にBibTeX生成
   - AIに論文検索と配置を依頼可能

3. **セクション単位の作業**
   - `src/sections/` 内のファイルごとに作業
   - AIに「02_related.tex を書いて」と依頼可能

4. **構造化されたプロンプト例**
   ```
   citation_map.yaml のS5スロットに適した参考文献を3つ提案して、
   references.bib に追加してください。
   ```

### 推奨ワークフロー

1. AIと協力して各セクションを執筆
2. `citation_map.yaml` で必要な引用を計画
3. `make realtime` でリアルタイムプレビュー
4. `make refs` で参考文献を更新

## 📋 ライセンス

MIT License