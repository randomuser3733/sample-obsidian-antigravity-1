# 📊 週次ワークフロー

**実行タイミング**: 毎週日曜夜

---

## 🎯 目的

週次でシステムを整理し、次の週に向けて準備する。

---

## 📋 実行タスク

### Step 1: 週次レビュー作成（15分）
```bash
/weekly-review
```

**実行内容:**
- [ ] 今週の全デイリーノートを確認
- [ ] ハイライト抽出
- [ ] 週次レビューファイル作成

**出力先:**
`02_Daily/Weekly-Reviews/YYYY/YYYY-W[週番号].md`

---

### Step 2: Inbox処理（10分）
```bash
/organize-inbox
```

**実行内容:**
- [ ] 01_Inbox内の全ファイルを確認
- [ ] 振り分け判定
- [ ] 適切なフォルダへ移動
- [ ] **目標**: 10ファイル以下

**判定フロー:**
1. プロジェクト関連？ → `05_Output/Projects/@Active/[Project]/`
2. 継続エリア関連？ → `05_Output/Areas/[Area]/@TODO/`
3. 汎用知識？ → `04_Memory/[Category]/`
4. 今週使う資料？ → `03_Input/`
5. デイリーログ？ → `02_Daily/YYYY/YYYY-MM/YYYY-MM-DD/`

---

### Step 3: 03_Inputクリーンアップ（5分）
```bash
# 1週間以上触っていないファイルをチェック
```

**実行内容:**
- [ ] 03_Input内のファイルを確認
- [ ] 最終更新日が7日以上前のファイルを検出
- [ ] 判定:
  - まだ使う → そのまま
  - 完了したタスク → `05_Output` へ移動
  - 未使用ファイル → `04_Memory` or `99_Archive`

---

### Step 4: Projects進捗確認（5分）
```bash
# アクティブプロジェクトの進捗を確認
```

**実行内容:**
- [ ] `05_Output/Projects/@Active/` 内のプロジェクトを確認
- [ ] 各プロジェクトの進捗を更新
- [ ] ブロッカーを特定
- [ ] 来週の優先順位を決定

---

### Step 5: Areas整理（5分）
```bash
# 継続エリアの@TODO/@Doingを整理
```

**実行内容:**
- [ ] 完了タスクを `@Completed` へ移動
- [ ] 停滞タスクを再評価
- [ ] 来週のFocus決定

---

### Step 6: ダッシュボード更新（5分）
```bash
/create-dashboards weekly
```

**実行内容:**
- [ ] 週次ダッシュボードを更新
- [ ] 今週のスケジュールを確認
- [ ] 来週の計画を確認

---

## ✅ チェックリスト

### 必須タスク
- [ ] 週次レビュー作成
- [ ] Inbox処理（10ファイル以下に）
- [ ] 03_Inputクリーンアップ
- [ ] Projects進捗確認
- [ ] ダッシュボード更新

### 推奨タスク
- [ ] Areas整理
- [ ] 孤立ノート検出・解消
- [ ] タグなしファイル検出・タグ付け

---

## 📊 週次レビュー例

```markdown
# 週次レビュー (2025-W02)

## 📊 今週の実績
- 作成ノート: 12件
- Memory作成: 3件
- Daily継続: 7日
- Inputクリーンアップ: 5件

## 📋 Inbox整理
- Memory候補: 3件
- Input候補: 2件
- Output候補: 2件

## 🎯 Projects進捗
- SURVIBE AI Dec2025: 80%完成
- YouTube Cursor Series: Ep01公開完了

## 💡 来週のアクション
- [ ] Memory作成: 3件
- [ ] Inbox整理: 未完了分を処理
- [ ] Projects進捗: SURVIBE AI 90%達成
```

---

## 🔧 自動化

### Cursorコマンドの組み合わせ
```bash
# 週次ワークフローの一括実行
1. /weekly-review
2. /organize-inbox
3. /create-dashboards weekly
4. /find-orphans
```

---

## 📚 関連ドキュメント

- [[daily-workflow.md]] - デイリーワークフロー
- [[inbox-processing-flow.md]] - Inbox処理フロー
- [[../Scripts/weekly-cleanup.md]] - 週次クリーンアップ

---

**最終更新**: 2025-01-13

