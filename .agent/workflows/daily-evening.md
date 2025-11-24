# Dailyまとめ（夕方）

## Description
夕方にDailyノートに今日の気づきを追記します（10分）。

## Prompt
今日のDailyノートに、今日の活動から重要な気づきを追記してください。

要件:
- 今日のDailyノートを読み込む（`02_Daily/YYYY/YYYY-MM/YYYY-MM-DD/YYYY-MM-DD-Daily.md`）
- Inboxフォルダ（`01_Inbox/`）から今日作成されたノートを抽出
- 重要な3つを選んで追記
- 「🌙 Evening Reflection」セクションに追記

出力形式:
```markdown
## 🌙 Evening Reflection
### ✅ Accomplished
- [今日達成したこと1]
- [今日達成したこと2]

### 💭 Key Learnings
- [具体的な気づき1]
  → 関連: [[Inboxノート1]]
- [具体的な気づき2]
  → 関連: [[Inboxノート2]]
- [具体的な気づき3]
  → 関連: [[Inboxノート3]]

### 📌 Tomorrow's Preparation
- [ ] [明日の準備1]
- [ ] [明日の準備2]
```

手順:
1. 今日の日付のDailyノートを読み込む
   - `02_Daily/YYYY/YYYY-MM/YYYY-MM-DD/YYYY-MM-DD-Daily.md`
2. `01_Inbox/`から今日の日付が含まれるファイルを検索
3. 各ノートの内容を分析
4. 最も重要だと思われる3つを選択
5. Dailyノートの「🌙 Evening Reflection」セクションに追記

ヒント:
- 気づきは簡潔に1-2文で
- 必ずInboxノートへのリンクを追加
- Brain System Rules: [[07_System/Documentation/system-overview.md]]
- 関連プロンプト: [[08_prompts/02_生成系/20250113_Dailyまとめ（夕方）.md]]

