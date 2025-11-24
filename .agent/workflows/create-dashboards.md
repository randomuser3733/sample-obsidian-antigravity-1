# ダッシュボード作成

## Description
各種ダッシュボードファイルを作成・更新します。

## Prompt
指定されたダッシュボードを作成または更新してください。

引数:
- ダッシュボード名（省略可）: 作成するダッシュボード
  - `home` または `🏠` - HOMEダッシュボード
  - `projects` または `🎯` - プロジェクトダッシュボード
  - `weekly` または `📊` - 週次ダッシュボード
  - `analytics` または `📈` - 分析ダッシュボード
  - `focus` または `🔥` - アクティブフォーカスダッシュボード
  - `all` - 全てのダッシュボードを作成

実行内容:
1. 今日の日付を取得
2. 指定されたダッシュボードの内容を生成
3. `07_System/Dashboards/` フォルダに保存
4. 既存のファイルがある場合は更新

## ダッシュボードの内容

### 🏠 HOMEダッシュボード
```markdown
# 🏠 HOME

**Today**: [[2025-01-13-Daily]]  
**Week**: W02  
**Energy**: ⚡⚡⚡⚡⚡⚡⚡⚡ (8/10)

---

## 🎯 Today's Top 3
- [ ] [Inboxから抽出したタスク1]
- [ ] [Inboxから抽出したタスク2]
- [ ] [Inboxから抽出したタスク3]

---

## 🔥 Active Projects
```dataview
TABLE status, progress, priority
FROM "05_Output/Projects/@Active"
SORT priority DESC
LIMIT 5
```

---

## 📥 Inbox Status
```dataview
LIST
FROM "01_Inbox"
SORT file.ctime DESC
LIMIT 10
```

**Action**: `01_Inbox` のファイル数を確認してください。  
💡 Goal: Keep under 10!

---

## 📚 Recent Learning
```dataview
LIST
FROM "04_Memory"
WHERE file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
LIMIT 5
```

---

## 🔥 Hot Topics (03_Input)
```dataview
LIST
FROM "03_Input"
SORT file.mtime DESC
LIMIT 5
```

---

## Quick Links
- [[週次ダッシュボード]]
- [[プロジェクトダッシュボード]]
- [[分析ダッシュボード]]
- [[アクティブフォーカス]]
- [[Weekly Review]]
- [[Content Calendar]]
```

### 🎯 Projectsダッシュボード
```markdown
# 🎯 プロジェクトダッシュボード

**最終更新**: 2025-01-13

---

## 🚀 Active Projects
```dataview
TABLE status, progress, priority, deadline
FROM "05_Output/Projects/@Active"
SORT priority DESC, deadline ASC
```

---

## 📋 Planning Projects
```dataview
TABLE status, priority
FROM "05_Output/Projects/@Planning"
SORT priority DESC
```

---

## ✅ Completed Projects (Recent)
```dataview
TABLE status, completed-date
FROM "05_Output/Projects/@Completed"
WHERE completed-date >= date(today) - dur(30 days)
SORT completed-date DESC
LIMIT 10
```

---

## 📊 Project Statistics
- **Active**: アクティブプロジェクト数を確認
- **Planning**: 企画中プロジェクト数を確認
- **Completed (30 days)**: 最近完了したプロジェクト数を確認

---

## 🔗 Quick Links
- [[HOMEダッシュボード]]
- [[週次ダッシュボード]]
- [[分析ダッシュボード]]
```

### 📊 Weeklyダッシュボード
```markdown
# 📊 週次ダッシュボード

**Week**: 2025-W02  
**Date Range**: 2025-01-13 ~ 2025-01-19

---

## 📅 This Week's Schedule
```dataview
TABLE date, type, title
FROM "02_Daily"
WHERE date >= date(2025-01-13) AND date <= date(2025-01-19)
SORT date ASC
```

---

## 🎯 Weekly Goals
- [ ] [Goal 1]
- [ ] [Goal 2]
- [ ] [Goal 3]

---

## 📝 This Week's Notes
```dataview
LIST
FROM "02_Daily"
WHERE date >= date(2025-01-13) AND date <= date(2025-01-19)
SORT date DESC
```

---

## 🔥 Active Focus Areas
```dataview
LIST
FROM "05_Output/Areas"
WHERE contains(file.name, "@Doing")
SORT file.mtime DESC
LIMIT 5
```

---

## 📚 Learning This Week
```dataview
LIST
FROM "04_Memory"
WHERE file.mtime >= date(2025-01-13) AND file.mtime <= date(2025-01-19)
SORT file.mtime DESC
```

---

## 🔗 Quick Links
- [[HOMEダッシュボード]]
- [[プロジェクトダッシュボード]]
- [[Weekly Review]]
```

### 📈 Analyticsダッシュボード
```markdown
# 📈 分析ダッシュボード

**最終更新**: 2025-01-13

---

## 📊 Note Statistics
```dataview
TABLE length(rows) as "Count"
FROM ""
WHERE file.folder != "99_Archive"
GROUP BY file.folder
SORT length(rows) DESC
```

---

## 🏷️ Top Tags
```dataview
TABLE length(rows) as "Count"
FROM ""
WHERE file.folder != "99_Archive"
FLATTEN file.tags as tag
GROUP BY tag
SORT length(rows) DESC
LIMIT 10
```

---

## 📚 Memory Growth
```dataview
TABLE file.mtime as "Created"
FROM "04_Memory"
WHERE file.mtime >= date(today) - dur(30 days)
SORT file.mtime DESC
```

---

## 🎯 Project Completion Rate
- **This Month**: 今月の完了率を確認
- **Active Projects**: アクティブプロジェクト数
- **Completed This Month**: 今月完了したプロジェクト数

---

## 📥 Inbox Health
- **Current Files**: 現在のファイル数
- **Goal**: < 10 files
- **Status**: 健康状態を確認

---

## 🔗 Quick Links
- [[HOMEダッシュボード]]
- [[プロジェクトダッシュボード]]
- [[週次ダッシュボード]]
```

### 🔥 Active Focusダッシュボード
```markdown
# 🔥 アクティブフォーカス

**Today**: 2025-01-13

---

## 🎯 Today's Focus
- [ ] [Priority 1]
- [ ] [Priority 2]
- [ ] [Priority 3]

---

## 🚀 Active Projects (Top 3)
```dataview
TABLE priority, progress
FROM "05_Output/Projects/@Active"
SORT priority DESC
LIMIT 3
```

---

## 🔥 Hot Topics (03_Input)
```dataview
LIST
FROM "03_Input"
SORT file.mtime DESC
LIMIT 5
```

---

## 📝 Recent Inbox Items
```dataview
LIST
FROM "01_Inbox"
SORT file.ctime DESC
LIMIT 5
```

---

## 💡 Quick Actions
- [[HOMEダッシュボード]] - ホームに戻る
- [[週次ダッシュボード]] - 週次ダッシュボード
- [[プロジェクトダッシュボード]] - プロジェクトダッシュボード
- [[Daily Note]] - 今日のデイリーノート
```

## 手順

### HOMEダッシュボード作成
1. 今日の日付を取得
2. 週番号を計算（ISO週番号）
3. Inboxから未完了タスクを3つ抽出
4. アクティブプロジェクトを取得（最大5件）
5. Inboxファイル数をカウント
6. 最近の学習ノートを取得（7日以内、最大5件）
7. `07_System/Dashboards/HOMEダッシュボード.md` を作成または更新

### Projectsダッシュボード作成
1. `05_Output/Projects/@Active/` からアクティブプロジェクトを取得
2. `05_Output/Projects/@Planning/` から企画中プロジェクトを取得
3. `05_Output/Projects/@Completed/` から最近完了したプロジェクトを取得（30日以内）
4. プロジェクト統計を計算
5. `07_System/Dashboards/プロジェクトダッシュボード.md` を作成または更新

### Weeklyダッシュボード作成
1. 今週の日付範囲を計算
2. 今週のDailyノートを取得
3. 今週の学習ノートを取得
4. アクティブフォーカスエリアを取得
5. `07_System/Dashboards/週次ダッシュボード.md` を作成または更新

### Analyticsダッシュボード作成
1. フォルダ別のノート数をカウント
2. タグ使用状況を分析（Top 10）
3. Memoryの成長を分析（30日以内）
4. プロジェクト完了率を計算
5. Inboxの健康状態を評価
6. `07_System/Dashboards/分析ダッシュボード.md` を作成または更新

### Active Focusダッシュボード作成
1. 今日の優先タスクを取得（Inboxから）
2. アクティブプロジェクトTop 3を取得
3. Hot Topics（03_Input）を取得（最大5件）
4. 最近のInboxアイテムを取得（最大5件）
5. `07_System/Dashboards/アクティブフォーカス.md` を作成または更新

## 使用例

```
/create-dashboards              # 全てのダッシュボードを作成
/create-dashboards home         # HOMEダッシュボードのみ作成
/create-dashboards 🏠           # HOMEダッシュボードのみ作成
/create-dashboards projects     # プロジェクトダッシュボードのみ作成
/create-dashboards 🎯           # プロジェクトダッシュボードのみ作成
/create-dashboards weekly       # 週次ダッシュボードのみ作成
/create-dashboards 📊           # 週次ダッシュボードのみ作成
/create-dashboards analytics    # 分析ダッシュボードのみ作成
/create-dashboards 📈           # 分析ダッシュボードのみ作成
/create-dashboards focus        # アクティブフォーカスダッシュボードのみ作成
/create-dashboards 🔥           # アクティブフォーカスダッシュボードのみ作成
```

## 注意事項

- DataviewクエリはObsidianのDataviewプラグインが必要です
- 日付は自動的に計算されます
- 既存のファイルがある場合は内容を更新します
- ファイルが存在しない場合は新規作成します
- ファイル名は日本語で作成します

## 関連コマンド

- [[daily.md]] - デイリーノート作成
- [[weekly-review.md]] - 週次レビュー
- [[project-view.md]] - プロジェクト統合ビュー

## 関連ファイル

- [[07_System/Dashboards/]] - ダッシュボードフォルダ
- [[AGENTS.md]] - Brain System Rules

