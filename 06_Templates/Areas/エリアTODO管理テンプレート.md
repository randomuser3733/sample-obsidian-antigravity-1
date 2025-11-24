---
area: 
status: active
tags: [area, {{area-name}}, todo]
created: {{date:YYYY-MM-DD}}
updated: {{date:YYYY-MM-DD}}
---

# 📋 {{Area Name}} - TODO Management

## 🔥 @TODO - やるべきこと

### High Priority
- [ ] タスク1 #high-priority
  - 理由:
  - 期限:
  - リソース:

### Medium Priority
- [ ] タスク2 #medium-priority

### Low Priority
- [ ] タスク3 #low-priority

### Backlog
- [ ] いつかやりたいこと1
- [ ] いつかやりたいこと2

## ⚡ @Doing - 進行中

### Active Now
- [ ] 現在作業中のタスク
  - 開始日:
  - 進捗: ___%
  - 次のステップ:
  - ブロッカー:

## ✅ @Completed - 完了

### This Week
- [x] 完了したタスク1 ✅ YYYY-MM-DD
- [x] 完了したタスク2 ✅ YYYY-MM-DD

### This Month
- [x] 
- [x] 

## 📊 Progress Overview

```dataview
TASK
WHERE contains(file.folder, "{{area-folder}}")
GROUP BY file.link
```

## 🔄 Weekly Review
- 今週の進捗:

- 来週の計画:

- 改善点:

