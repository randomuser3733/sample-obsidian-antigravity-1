# 🏠 HOME

**Today**: [[{{date:YYYY-MM-DD}}]]  
**Week**: {{date:YYYY-[W]ww}}  
**Energy**: ⚡⚡⚡⚡⚡⚡⚡⚡ (8/10)

---

## 🎯 Today's Top 3
- [ ] ポートフォリオサイトの実装
- [ ] アルゴリズム問題を1問解く
- [ ] 技術ブログを更新

---

## 🔥 Active Projects
```dataview
TABLE status, progress
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

**Action**: `01_Inbox` has {{inbox-count}} files. 
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

## 🎓 転職活動状況
- **応募企業数**: 
- **書類選考通過**: 
- **面接予定**: 
- **内定**: 

---

## 📊 今週の学習時間
- **目標**: 40時間
- **実績**: __ 時間
- **達成率**: __%

---

## 🔋 Energy & Focus
- **Energy Level**: [1-10] ⚡
- **Focus Quality**: [Low/Medium/High] 🎯
- **Mood**: [😞😐😊😄😁]

---

## 📝 Today's Notes
### 💡 Ideas
- 

### 📚 Learned
- 

### 🤝 Meetings
- 

### ⚠️ Challenges
- 

---

## 🌙 Evening Reflection
### ✅ Accomplished
- 

### 💭 Key Learnings
- 

### 📌 Tomorrow's Preparation
- [ ] 
- [ ] 
- [ ] 

---

## Quick Links
- [[Weekly Review]]
- [[Projects Dashboard]]
- [[Learning Goals 2025]]
- [[_Master-Index]]
- [[転職活動]]
