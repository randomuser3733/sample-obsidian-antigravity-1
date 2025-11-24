# 🎯 プロジェクト管理フロー

**実行タイミング**: プロジェクト開始時、進行中、完了時

---

## 🎯 プロジェクトの種類

### Projects（期限あり）
- 具体的なプロジェクト
- 期限がある
- 終わりがある

**例:**
- SURVIBE AI 12月講座
- YouTube動画シリーズ
- 企業研修プロジェクト

### Areas（継続的）
- 継続的な活動
- 期限なし
- 終わりがない

**例:**
- YouTubeチャンネル運営
- Survibe AI Baib-Coding-School
- 企業研修事業

---

## 📋 プロジェクト開始フロー

### Step 1: プロジェクト作成
```bash
# 05_Output/Projects/@Planning/ または @Active/ に作成
```

**実行内容:**
- [ ] プロジェクトフォルダを作成
- [ ] `00-project-overview.md` を作成
- [ ] プロジェクト概要を記入

**フォルダ構造:**
```
Projects/@Active/[Project-Name]/
├─ 00-project-overview.md
├─ 01-planning/
├─ 02-curriculum/
├─ 03-materials/
├─ 04-delivery/
└─ 05-review-feedback/
```

---

### Step 2: プロジェクト概要記入
```markdown
# [プロジェクト名]

## 概要
[プロジェクトの概要]

## 目的
[プロジェクトの目的]

## 期間
開始: YYYY-MM-DD
終了: YYYY-MM-DD

## 成果物
- [成果物1]
- [成果物2]

## ステータス
- [ ] Planning
- [ ] Active
- [ ] Completed
```

---

### Step 3: 計画フェーズ
```bash
# 01-planning/ フォルダに計画を記入
```

**実行内容:**
- [ ] `requirements.md` - 要件定義
- [ ] `timeline.md` - タイムライン
- [ ] `stakeholders.md` - 関係者

---

## 📊 プロジェクト進行フロー

### Step 1: 進捗管理
```bash
# 定期的に進捗を更新
```

**実行内容:**
- [ ] 各フェーズの進捗を記録
- [ ] ブロッカーを記録
- [ ] 次のアクションを決定

---

### Step 2: タスク管理
```bash
# タスクを記録・追跡
```

**実行内容:**
- [ ] タスクリストを作成
- [ ] 完了タスクをチェック
- [ ] 優先順位を設定

---

### Step 3: ドキュメント管理
```bash
# プロジェクト関連のドキュメントを整理
```

**実行内容:**
- [ ] カリキュラムを `02-curriculum/` に保存
- [ ] 教材を `03-materials/` に保存
- [ ] 実施ログを `04-delivery/` に保存

---

## ✅ プロジェクト完了フロー

### Step 1: レビュー
```bash
# 05-review-feedback/ フォルダにレビューを記入
```

**実行内容:**
- [ ] `student-feedback.md` - 受講生フィードバック
- [ ] `improvements.md` - 改善点
- [ ] `next-cohort-ideas.md` - 次回へのアイデア

---

### Step 2: プロジェクト完了
```bash
# @Active/ から @Completed/ へ移動
```

**実行内容:**
- [ ] プロジェクトフォルダを `@Completed/YYYY/` へ移動
- [ ] プロジェクト概要を更新
- [ ] ステータスを「Completed」に変更

---

### Step 3: 学びの保存
```bash
# 重要な学びを04_Memory/に保存
```

**実行内容:**
- [ ] プロジェクトから学んだことを抽出
- [ ] `04_Memory/[Category]/` に保存
- [ ] 関連ノートにリンク

---

## 🔄 Areas管理フロー

### Step 1: エリア作成
```bash
# 05_Output/Areas/[Area-Name]/ に作成
```

**フォルダ構造:**
```
Areas/[Area-Name]/
├─ 00-channel-strategy.md
├─ @TODO/
├─ @Doing/
└─ @Completed/
```

---

### Step 2: ステータス管理
```bash
# @TODO → @Doing → @Completed の流れ
```

**実行内容:**
- [ ] アイデアは `@TODO/` に保存
- [ ] 制作開始時は `@Doing/` へ移動
- [ ] 完成・公開時は `@Completed/` へ移動

---

## 📊 プロジェクト統計

### Dataviewクエリ
```dataview
TABLE status, progress, priority
FROM "05_Output/Projects/@Active"
SORT priority DESC
```

---

## ✅ チェックリスト

### プロジェクト開始時
- [ ] プロジェクトフォルダ作成
- [ ] プロジェクト概要記入
- [ ] 計画フェーズ開始

### プロジェクト進行中
- [ ] 進捗を定期的に更新
- [ ] ブロッカーを記録
- [ ] 次のアクションを決定

### プロジェクト完了時
- [ ] レビューを記入
- [ ] プロジェクトを完了に
- [ ] 学びをMemoryに保存

---

## 📚 関連ドキュメント

- [[daily-workflow.md]] - デイリーワークフロー
- [[weekly-workflow.md]] - 週次ワークフロー
- [[../Dashboards/🎯-Projects-Dashboard.md]] - プロジェクトダッシュボード

---

**最終更新**: 2025-01-13

