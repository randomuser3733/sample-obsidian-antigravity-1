# 📅 デイリーワークフロー

**実行タイミング**: 毎日

---

## 🌅 朝のルーティン（5分）

### Step 1: Dailyノート作成
```bash
/daily
```

**実行内容:**
- [ ] 今日のデイリーノートを作成
- [ ] Inboxから未完了タスクを3つ抽出
- [ ] Top 3 Prioritiesを設定

**出力先:**
`02_Daily/YYYY/YYYY-MM/YYYY-MM-DD/YYYY-MM-DD-Daily.md`

---

### Step 2: HOMEダッシュボード更新
```bash
/create-dashboards home
```

**実行内容:**
- [ ] HOMEダッシュボードを更新
- [ ] 今日のTop 3を確認
- [ ] アクティブプロジェクトを確認

---

### Step 3: エネルギーレベル記録
- [ ] エネルギーレベルを記録（1-10）
- [ ] フォーカス品質を記録
- [ ] 気分を記録

---

## 🌞 日中の使い方

### アイデアが浮かんだら（30秒）
1. `00_Memo/` を開く
2. 新規ファイル作成（適当な名前でOK）
3. とにかく書く
4. 保存して閉じる

---

### 何か学んだら（2分）
1. Daily Noteを開く
2. `### 📚 What I Learned` に追記
3. 関連リンクを貼る
   - 例: `[[Cursor]]` `[[Prompting]]`

---

### 会議があったら（5分）
1. Daily内に新規ファイル作成
   - 例: `meeting-client-abc.md`
2. テンプレート使用
3. メモを取る
4. Daily Noteからリンク

---

## 🌙 夜のルーティン（10分）

### Step 1: Evening Reflection記入
- [ ] 今日の成果を記録
- [ ] 学んだことを記録
- [ ] 改善点を記録

---

### Step 2: 明日の準備
- [ ] `Tomorrow's Preparation`に記入
- [ ] 明日のTODOを作成（任意）

---

### Step 3: 00_Memoチェック
- [ ] 今日のメモを確認
- [ ] 重要なものは01_Inboxへ移動（Cursorで処理）

---

## ✅ チェックリスト

### 毎日必須
- [ ] Daily Note作成
- [ ] Top 3 Priorities設定
- [ ] Evening Reflection記入

### 推奨
- [ ] HOMEダッシュボード確認
- [ ] 00_Memoチェック
- [ ] 明日の準備

---

## 🔧 自動化

### Cursorコマンド
- `/daily` - Dailyノート自動生成
- `/create-dashboards home` - HOMEダッシュボード自動更新

### Templater
- Dailyノートテンプレート自動適用
- 日付自動挿入

---

## 📚 関連ドキュメント

- [[weekly-workflow.md]] - 週次ワークフロー
- [[inbox-processing-flow.md]] - Inbox処理フロー
- [[../Scripts/nightly-batch-process.md]] - 夜間バッチ処理

---

**最終更新**: 2025-01-13

