# 📝 コンテンツ作成フロー

**実行タイミング**: コンテンツ作成時

---

## 🎯 コンテンツの種類

### YouTube動画
- 動画シリーズ
- 単発動画

### ブログ記事
- 技術記事
- ビジネス記事
- 教育記事

### SNS投稿
- X（Twitter）
- LinkedIn
- Note

---

## 📋 YouTube動画作成フロー

### Step 1: アイデア段階
```bash
# 05_Output/Areas/Content-Creation/YouTube-Channel/@TODO/
```

**実行内容:**
- [ ] アイデアを `@TODO/` に保存
- [ ] テンプレート使用: `06_Templates/Content/YouTubeアイデアテンプレート.md`
- [ ] 基本情報を記入

---

### Step 2: 企画が固まったら
```bash
# @TODO/ から @Doing/ に移動
```

**実行内容:**
- [ ] フォルダ作成: `[動画タイトル]/`
- [ ] スクリプト執筆開始
- [ ] アセット準備

**フォルダ構造:**
```
@Doing/[動画タイトル]/
├─ script.md
├─ outline.md
└─ assets/
```

---

### Step 3: 制作中
```bash
# Daily Noteで進捗記録
```

**実行内容:**
- [ ] Daily Noteで進捗記録
- [ ] 必要な情報は04_Memoryから参照
- [ ] スクリプト完成

---

### Step 4: 完成・公開
```bash
# @Doing/ から @Completed/ に移動
```

**実行内容:**
- [ ] `@Completed/YYYY/MM/` へ移動
- [ ] アナリティクスを記録
- [ ] フィードバックを記録

---

## 📝 ブログ記事作成フロー

### Step 1: アイデア段階
```bash
# 05_Output/Areas/Content-Creation/Blog/@TODO/
```

**実行内容:**
- [ ] アイデアを `@TODO/` に保存
- [ ] テンプレート使用: `06_Templates/Content/ブログアウトラインテンプレート.md`
- [ ] アウトライン作成

---

### Step 2: 執筆開始
```bash
# @TODO/ から @Doing/ に移動
```

**実行内容:**
- [ ] アウトラインを基に執筆
- [ ] 必要な情報は04_Memoryから参照
- [ ] 下書き完成

---

### Step 3: 公開
```bash
# @Doing/ から @Completed/ に移動
```

**実行内容:**
- [ ] `@Completed/YYYY/MM/` へ移動
- [ ] 公開URLを記録
- [ ] アクセス数を記録

---

## 📱 SNS投稿作成フロー

### Step 1: アイデア記録
```bash
# 05_Output/Areas/Content-Creation/SNS/@TODO/
```

**実行内容:**
- [ ] アイデアを `@TODO/` に保存
- [ ] テンプレート使用: `06_Templates/Content/SNS投稿テンプレート.md`
- [ ] 投稿内容を作成

---

### Step 2: 投稿
```bash
# @TODO/ から @Doing/ に移動（投稿中）
```

**実行内容:**
- [ ] 投稿を実行
- [ ] 投稿URLを記録
- [ ] `@Completed/` へ移動

---

## 🔄 コンテンツパイプライン

### アイデア → 企画 → 制作 → 公開

```
@TODO (アイデア段階)
  ↓ 企画決定
@Doing (制作中)
  ↓ 完成・公開
@Completed (完了)
  ↓ 3ヶ月後
99_Archive (アーカイブ)
```

---

## 📊 コンテンツ統計

### Dataviewクエリ
```dataview
TABLE status, published-date
FROM "05_Output/Areas/Content-Creation"
WHERE status = "completed"
SORT published-date DESC
LIMIT 10
```

---

## ✅ チェックリスト

### YouTube動画作成時
- [ ] アイデアを `@TODO/` に保存
- [ ] 企画が固まったら `@Doing/` へ移動
- [ ] スクリプト完成
- [ ] 公開後 `@Completed/` へ移動

### ブログ記事作成時
- [ ] アイデアを `@TODO/` に保存
- [ ] アウトライン作成
- [ ] 執筆開始（`@Doing/` へ移動）
- [ ] 公開後 `@Completed/` へ移動

### SNS投稿時
- [ ] アイデアを `@TODO/` に保存
- [ ] 投稿内容を作成
- [ ] 投稿後 `@Completed/` へ移動

---

## 📚 関連ドキュメント

- [[daily-workflow.md]] - デイリーワークフロー
- [[project-management-flow.md]] - プロジェクト管理フロー
- [[../../06_Templates/Content/]] - コンテンツテンプレート

---

**最終更新**: 2025-01-13

