# 🤖 Cursor統合設定

**最終更新**: 2025-01-13

---

## 🎯 Cursorとの統合

このObsidian Vaultは、Cursor AIエディタと統合して使用することを前提としています。

---

## 📁 Cursorコマンド

### コマンドの場所
`.cursor/commands/` フォルダに各種コマンドが定義されています。

### 主要コマンド
- `/daily` - デイリーノート作成
- `/memo-to-inbox` - MemoをInboxに変換
- `/organize-inbox` - Inbox整理
- `/create-dashboards` - ダッシュボード作成
- `/weekly-review` - 週次レビュー

---

## 🔧 Cursor設定

### ワークスペース設定
- **ワークスペースパス**: `/path/to/second-brain-vault`
- **デフォルトエディタ**: Cursor

### AI設定
- **モデル**: Claude Sonnet 4（推奨）
- **コンテキスト**: システム全体のルールを参照

---

## 📝 プロンプト管理

### プロンプトの場所
`08_prompts/` フォルダにカテゴリ別にプロンプトを保存。

### カテゴリ
- `01_整理系/` - Inbox整理、Memory作成
- `02_生成系/` - Daily作成、コンテンツ生成
- `03_レビュー系/` - ノート品質チェック
- `04_学習系/` - 技術調査
- `05_改善系/` - 改善作業用
- `06_一括作業系/` - 全量作業

---

## 🤖 AIへの指示

### システムルールの参照
Cursorに作業を依頼する際は、以下のファイルを参照させます：
- `AGENTS.md` - Brain System Rules
- `07_System/Documentation/system-overview.md` - システム概要

### コマンドの実行
Cursorコマンドは `/コマンド名` の形式で実行します。

---

## 🔄 ワークフロー統合

### 朝のルーティン
1. `/daily` - デイリーノート作成
2. `/create-dashboards home` - HOMEダッシュボード更新
3. 今日のタスクを追記

### 週次ルーティン
1. `/weekly-review` - 週次レビュー
2. `/organize-inbox` - Inbox整理
3. `/create-dashboards weekly` - 週次ダッシュボード更新

---

## 📚 関連ドキュメント

- [[../Documentation/system-overview.md]] - システム概要
- [[../../.cursor/commands/README.md]] - コマンド一覧
- [[../../08_prompts/README.md]] - プロンプト集

---

**最終更新**: 2025-01-13
