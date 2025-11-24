# 📊 Weekly Dashboard

## 🗓 今週の視点
- 重点テーマ: Cursor動画 / SURVIBE演習 / プロンプト改善
- リスク: スケジュール過密、体力低下

## 📥 Inbox
```dataview
TABLE file.ctime as 追加日, length(file.tasks) as Tasks
FROM "01_Inbox"
SORT file.ctime DESC
LIMIT 15
```

## 🚀 プロジェクト状況
```dataview
TABLE progress, status
FROM "05_Output/Projects/@Active"
SORT file.name
```

## 🧠 学びログ（7日）
```dataview
LIST
FROM "04_Memory"
WHERE file.mtime >= date(today) - dur(7 days)
LIMIT 10
```
