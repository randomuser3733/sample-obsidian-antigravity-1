# 🌙 Nightly Batch Processing v2.0

## 実行タイミング
- **毎日 23:00**: デイリー処理
- **日曜 23:00**: ウィークリー処理
- **月末 23:00**: マンスリー処理

---

## 📅 Daily Processing (23:00)

### Step 1: 00_Memo → 01_Inbox チェック
```bash
# 00_Memoにファイルが溜まりすぎていないか確認
# 目安: 20ファイル以内
```

- [ ] 00_Memoのファイル数を確認
- [ ] 20ファイル超過の場合、Cursor処理を促す

### Step 2: 01_Inbox → 適切なフォルダへ振り分け
```bash
# Inboxのファイルを週1回程度で処理
# 各ファイルの行き先を決定
```

**判定フロー:**
1. プロジェクト関連？ → `05_Output/Projects/@Active/[Project]/` へ
2. 継続エリア関連？ → `05_Output/Areas/[Area]/@TODO/` へ
3. 汎用知識？ → `04_Memory/[Category]/` へ
4. 今週使う資料？ → `03_Input/` へ
5. デイリーログ？ → `02_Daily/YYYY/YYYY-MM/YYYY-MM-DD/` へ

### Step 3: 02_Daily の整理
```bash
# 今日のデイリーノートから抽出
```

**抽出対象:**
- [ ] 💡 重要なアイデア → `01_Inbox` or `04_Memory`
- [ ] 📝 学んだこと → `04_Memory/[Category]/`
- [ ] 🎯 プロジェクトメモ → `05_Output/Projects/`
- [ ] 📊 KPI・数値 → `05_Output/Areas/[Area]/analytics/`

**判定基準 (3ヶ月ルール):**
「3ヶ月後も参照する価値があるか？」
- YES → Memoryへ
- NO → Dailyに残す

### Step 4: 03_Input のクリーンアップ
```bash
# 1週間以上参照していないファイルをチェック
```

- [ ] 未使用ファイル → `04_Memory` or `99_Archive`
- [ ] まだ使う → そのまま
- [ ] 完了したタスク → `05_Output` へ移動

### Step 5: タグ・リンクの自動検証
```dataview
# タグなしファイルを検出
LIST
FROM ""
WHERE file.tags = []
  AND file.folder != "00_Memo"
  AND file.folder != "99_Archive"
SORT file.mtime DESC
LIMIT 20
```

```dataview
# 孤立ノート（リンクなし）を検出
LIST
FROM ""
WHERE length(file.outlinks) = 0
  AND length(file.inlinks) = 0
  AND file.folder != "00_Memo"
  AND file.folder != "99_Archive"
SORT file.mtime DESC
LIMIT 10
```

---

## 📊 Weekly Processing (日曜 23:00)

### Step 1: 週次レビュー準備
- [ ] 今週の全デイリーノートを確認
- [ ] ハイライト抽出
- [ ] Weekly Review テンプレート作成

### Step 2: Projects 進捗確認
```dataview
TABLE status, progress
FROM "05_Output/Projects/@Active"
WHERE type = "project"
```

- [ ] 各プロジェクトの進捗を更新
- [ ] 来週の優先順位を決定
- [ ] ブロッカーを特定

### Step 3: Areas の @TODO/@Doing 整理
- [ ] 完了タスクを @Completed へ
- [ ] 停滞タスクを再評価
- [ ] 来週の Focus 決定

### Step 4: Content Pipeline 確認
- [ ] YouTube: アイデア→企画→制作の流れ確認
- [ ] Blog: 執筆中記事の進捗確認
- [ ] Social: 来週の投稿計画

---

## 📆 Monthly Processing (月末 23:00)

### Step 1: 月次アーカイブ
```bash
# 先月のDailyフォルダを確認
# 重要なものをMemoryへ、それ以外はそのまま
```

- [ ] 先月の Daily ノートレビュー
- [ ] 価値あるメモ→ `04_Memory`
- [ ] 不要ファイル→ `99_Archive`

### Step 2: Memory の大整理
- [ ] 各カテゴリーのMOC更新
- [ ] 重複ノートの統合
- [ ] リンク構造の最適化
- [ ] カテゴリー再編成

### Step 3: Projects クリーンアップ
- [ ] 完了プロジェクト→ `@Completed/YYYY/`
- [ ] 停止プロジェクト→ `99_Archive`
- [ ] 企画中→実行判断

### Step 4: Analytics & Insights
```dataview
# 今月作成したファイル数
LIST
WHERE date(file.cday) >= date(this.file.cday) - dur(30 days)
GROUP BY file.folder
```

- [ ] 生産性分析
- [ ] コンテンツ公開数
- [ ] プロジェクト完了率

---

## 🔧 自動化のヒント

### Dataview Queries

```dataview
# 今週処理すべきInbox
LIST
FROM "01_Inbox"
WHERE date(file.cday) < date(today) - dur(7 days)
SORT file.cday ASC
```

### Templater Scripts

```javascript
// Daily Noteから自動抽出
<%*
const dailyNote = tp.file.find_tfile("{{date:YYYY-MM-DD}}-Daily");
const content = await app.vault.read(dailyNote);
const ideas = content.match(/💡 (.+)/g);
%>
```

---

## ✅ チェックリスト

### 毎日
- [ ] Daily Note 作成
- [ ] Top 3 設定
- [ ] 夜: Evening Review

### 毎週
- [ ] Inbox 処理 (10ファイル以下に)
- [ ] Weekly Review
- [ ] 来週計画

### 毎月
- [ ] Monthly Review
- [ ] Memory 整理
- [ ] Projects 評価

