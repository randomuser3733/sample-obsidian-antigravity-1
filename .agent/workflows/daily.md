# Daily作成

## Description
今日のデイリーノートを作成します。

## Prompt
今日のデイリーノートを作成してください（朝のルーティン5分）。

要件:
- ファイル名: `02_Daily/YYYY/YYYY-MM/YYYY-MM-DD/YYYY-MM-DD-Daily.md`（今日の日付を使用）
- 今日の日付を自動挿入
- Inboxフォルダ（`01_Inbox/`）から未完了タスクを3つ抽出
- 前日のDailyへのリンクを追加
- テンプレートを使用: `06_Templates/Daily/デイリーノートテンプレート.md`

テンプレート:
```markdown
---
date: YYYY-MM-DD
day: [曜日]
week: YYYY-W[週番号]
tags: [daily, YYYY, YYYY-MM]
---

# YYYY-MM-DD - [曜日]

## 🔋 Today's Energy & Focus
- Energy Level: [1-10]/10 ⚡
- Focus Quality: [High/Medium/Low] 🎯
- Mood: [😊/😐/😔]

## ⭐ Top 3 Priorities
- [ ] [Inboxから抽出したタスク1]
- [ ] [Inboxから抽出したタスク2]
- [ ] [Inboxから抽出したタスク3]

## 📝 Today's Notes
### 💡 Ideas
（重要なアイデアをここに）

### 📚 Learned
（今日学んだことをここに）

### 🤝 Meetings
（会議メモへのリンク）

## 🌙 Evening Reflection
### ✅ Accomplished
（夕方に追記）

### 💭 Key Learnings
（夕方に追記）

### 📌 Tomorrow's Preparation
- [ ] （夕方に追記）
```

手順:
1. 今日の日付を取得
2. `02_Daily/YYYY/YYYY-MM/YYYY-MM-DD/` フォルダを作成（存在しない場合）
3. `02_Daily/YYYY/YYYY-MM/YYYY-MM-DD/YYYY-MM-DD-Daily.md` を作成
4. Inbox内のタスクファイル（`01_Inbox/`）を検索
5. チェックボックス形式のタスクを抽出（最大3つ）
6. 前日のDailyへのリンクを追加
7. テンプレート（`06_Templates/Daily/デイリーノートテンプレート.md`）を参照してファイルを作成

ヒント:
- 「Top 3 Priorities」は簡潔に
- 「Evening Reflection」は夕方に追記する想定
- Brain System Rules: [[07_System/Documentation/system-overview.md]]
- 関連プロンプト: [[08_prompts/02_生成系/20250113_Daily作成.md]]

