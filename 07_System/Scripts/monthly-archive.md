# 📆 月次アーカイブ

**実行タイミング**: 毎月末日 23:00

---

## 🎯 目的

月次でシステムを大整理し、古いファイルをアーカイブする。

---

## 📋 実行タスク

### Step 1: Dailyノートのレビュー
```bash
# 先月のDailyフォルダを確認
# 重要なものをMemoryへ、それ以外はそのまま
```

**実行内容:**
- [ ] 先月のDailyノートを確認
- [ ] 重要なメモを抽出
  - 💡 重要なアイデア → `04_Memory`
  - 📝 学んだこと → `04_Memory/[Category]/`
  - 🎯 プロジェクトメモ → `05_Output/Projects/`
- [ ] 不要ファイル → `99_Archive`

**判定基準 (3ヶ月ルール):**
「3ヶ月後も参照する価値があるか？」
- YES → Memoryへ
- NO → Dailyに残す or Archiveへ

---

### Step 2: Memoryの大整理
```bash
# 各カテゴリーのMOC更新
# 重複ノートの統合
# リンク構造の最適化
```

**実行内容:**
- [ ] 各カテゴリーのMOC更新
  - `04_Memory/AI/_AI-MOC.md`
  - `04_Memory/Business/_Business-MOC.md`
  - `04_Memory/Education/_Education-MOC.md`
  - `04_Memory/Personal/_Personal-MOC.md`
  - `04_Memory/Technical/_Tech-MOC.md`
- [ ] 重複ノートの統合
- [ ] リンク構造の最適化
- [ ] カテゴリー再編成（必要に応じて）

**Dataviewクエリ:**
```dataview
TABLE length(rows) as "Count"
FROM "04_Memory"
GROUP BY file.folder
SORT length(rows) DESC
```

---

### Step 3: Projectsクリーンアップ
```bash
# 完了プロジェクトを@Completedへ移動
# 停止プロジェクトをArchiveへ
```

**実行内容:**
- [ ] 完了プロジェクト → `@Completed/YYYY/` へ移動
- [ ] 停止プロジェクト → `99_Archive` へ移動
- [ ] 企画中プロジェクト → 実行判断

**判定基準:**
- **完了**: 全ての成果物が完成し、レビュー完了
- **停止**: 3ヶ月以上進捗なし
- **企画中**: 実行判断が必要

---

### Step 4: Analytics & Insights
```bash
# 今月の生産性分析
# コンテンツ公開数
# プロジェクト完了率
```

**実行内容:**
- [ ] 今月作成したファイル数をカウント
- [ ] フォルダ別の統計
- [ ] 生産性分析
- [ ] コンテンツ公開数
- [ ] プロジェクト完了率

**Dataviewクエリ:**
```dataview
TABLE length(rows) as "Count"
FROM ""
WHERE date(file.cday) >= date(today) - dur(30 days)
GROUP BY file.folder
SORT length(rows) DESC
```

---

### Step 5: 月次レビュー作成
```bash
# 月次レビューファイルを作成
```

**実行内容:**
- [ ] 今月のハイライトを抽出
- [ ] 数値分析
- [ ] 来月の目標設定

**出力先:**
`02_Daily/Monthly-Reviews/YYYY/YYYY-MM.md`

---

### Step 6: Archive整理
```bash
# 古いアーカイブを整理
```

**実行内容:**
- [ ] 1年以上前のアーカイブを確認
- [ ] 完全に不要なファイルを削除（慎重に）
- [ ] 年別フォルダに整理

---

## ✅ チェックリスト

### 必須タスク
- [ ] Dailyノートレビュー
- [ ] Memory大整理
- [ ] Projectsクリーンアップ
- [ ] 月次レビュー作成

### 推奨タスク
- [ ] Analytics & Insights
- [ ] Archive整理
- [ ] システム改善提案

---

## 📊 月次レポート例

```markdown
# 月次レビュー (2025-01)

## 📊 今月の実績
- 作成ノート: 45件
- Memory作成: 12件
- Daily継続: 31日
- プロジェクト完了: 2件

## 📚 Memory成長
- AI: +5件
- Business: +3件
- Education: +2件
- Technical: +2件

## 🎯 Projects完了
- SURVIBE AI Dec2025講座
- YouTube Cursor Series Ep01-04

## 💡 来月の目標
- [ ] Memory作成: 15件
- [ ] プロジェクト完了: 3件
- [ ] コンテンツ公開: 8件
```

---

## 🔧 自動化のヒント

### Cursorコマンドの組み合わせ
```bash
# 月次アーカイブの一括実行
1. /archive-review
2. /create-dashboards analytics
3. 月次レビュー作成
```

### Dataviewクエリの活用
- 今月作成したファイル数
- フォルダ別統計
- プロジェクト完了率

---

## 📚 関連ドキュメント

- [[nightly-batch-process.md]] - 夜間バッチ処理
- [[weekly-cleanup.md]] - 週次クリーンアップ
- [[../Workflows/weekly-workflow.md]] - 週次ワークフロー

---

**最終更新**: 2025-01-13

