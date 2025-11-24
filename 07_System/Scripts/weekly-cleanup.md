# 📊 週次クリーンアップ

**実行タイミング**: 毎週日曜 23:00

---

## 🎯 目的

週次でシステムを整理し、次の週に向けて準備する。

---

## 📋 実行タスク

### Step 1: Inbox整理
```bash
# 01_Inbox内のファイルを確認
# 目標: 10ファイル以下
```

**実行内容:**
- [ ] 01_Inbox内のファイル数をカウント
- [ ] 10ファイル超過の場合、振り分けを実行
- [ ] `/organize-inbox` コマンドで自動振り分け

**判定フロー:**
1. プロジェクト関連？ → `05_Output/Projects/@Active/[Project]/`
2. 継続エリア関連？ → `05_Output/Areas/[Area]/@TODO/`
3. 汎用知識？ → `04_Memory/[Category]/`
4. 今週使う資料？ → `03_Input/`
5. デイリーログ？ → `02_Daily/YYYY/YYYY-MM/YYYY-MM-DD/`

---

### Step 2: 03_Inputのクリーンアップ
```bash
# 1週間以上参照していないファイルをチェック
```

**実行内容:**
- [ ] 03_Input内のファイルを確認
- [ ] 最終更新日が7日以上前のファイルを検出
- [ ] 判定:
  - まだ使う → そのまま
  - 完了したタスク → `05_Output` へ移動
  - 未使用ファイル → `04_Memory` or `99_Archive`

**Dataviewクエリ:**
```dataview
LIST
FROM "03_Input"
WHERE file.mtime < date(today) - dur(7 days)
SORT file.mtime ASC
```

---

### Step 3: 孤立ノート検出
```bash
# リンクがないノートを検出
```

**実行内容:**
- [ ] バックリンク0のノートを検出
- [ ] フォワードリンク0のノートを検出
- [ ] リンク候補を提案

**Dataviewクエリ:**
```dataview
LIST
FROM ""
WHERE length(file.outlinks) = 0
  AND length(file.inlinks) = 0
  AND file.folder != "00_Memo"
  AND file.folder != "99_Archive"
  AND file.folder != "06_Templates"
  AND file.folder != "07_System"
SORT file.mtime DESC
LIMIT 20
```

---

### Step 4: タグなしファイル検出
```bash
# タグが付いていないファイルを検出
```

**実行内容:**
- [ ] タグなしファイルを検出
- [ ] タグ候補を提案

**Dataviewクエリ:**
```dataview
LIST
FROM ""
WHERE file.tags = []
  AND file.folder != "00_Memo"
  AND file.folder != "99_Archive"
  AND file.folder != "06_Templates"
SORT file.mtime DESC
LIMIT 20
```

---

### Step 5: Projects進捗確認
```bash
# アクティブプロジェクトの進捗を確認
```

**実行内容:**
- [ ] `05_Output/Projects/@Active/` 内のプロジェクトを確認
- [ ] 各プロジェクトの進捗を更新
- [ ] ブロッカーを特定
- [ ] 来週の優先順位を決定

**Dataviewクエリ:**
```dataview
TABLE status, progress, priority
FROM "05_Output/Projects/@Active"
SORT priority DESC
```

---

### Step 6: Areasの整理
```bash
# 継続エリアの@TODO/@Doingを整理
```

**実行内容:**
- [ ] 完了タスクを `@Completed` へ移動
- [ ] 停滞タスクを再評価
- [ ] 来週のFocus決定

**対象エリア:**
- Content-Creation
- Business
- Personal
- Community

---

### Step 7: 週次レビュー作成
```bash
# 週次レビューファイルを作成
```

**実行内容:**
- [ ] `/weekly-review` コマンドを実行
- [ ] 今週のハイライトを抽出
- [ ] 来週のアクションを決定

**出力先:**
`02_Daily/Weekly-Reviews/YYYY/YYYY-W[週番号].md`

---

### Step 8: ダッシュボード更新
```bash
# 週次ダッシュボードを更新
```

**実行内容:**
- [ ] `/create-dashboards weekly` を実行
- [ ] 週次ダッシュボードを更新

---

## ✅ チェックリスト

### 必須タスク
- [ ] Inbox整理（10ファイル以下に）
- [ ] 03_Inputクリーンアップ
- [ ] 週次レビュー作成
- [ ] ダッシュボード更新

### 推奨タスク
- [ ] 孤立ノート検出・解消
- [ ] タグなしファイル検出・タグ付け
- [ ] Projects進捗確認
- [ ] Areas整理

---

## 🔧 自動化のヒント

### Cursorコマンドの組み合わせ
```bash
# 週次クリーンアップの一括実行
1. /organize-inbox
2. /weekly-review
3. /create-dashboards weekly
4. /find-orphans
```

### Dataviewクエリの活用
- 03_Inputの古いファイル検出
- 孤立ノート検出
- タグなしファイル検出

---

## 📚 関連ドキュメント

- [[nightly-batch-process.md]] - 夜間バッチ処理
- [[monthly-archive.md]] - 月次アーカイブ
- [[../Workflows/weekly-workflow.md]] - 週次ワークフロー

---

**最終更新**: 2025-01-13

