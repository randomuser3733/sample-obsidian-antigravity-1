# システム概要

**バージョン**: 1.0  
**最終更新**: 2025-01-13

---

## 🎯 システムの目的

このObsidian Vaultは、**汎用セカンドブレイン**として機能する知識管理システムです。人間の脳の情報処理を模倣し、情報の流れを最適化することを目指しています。

---

## 🧠 システムの哲学

### 3つの基本原則

1. **完璧主義を捨てる**
   - 情報は「記録する」ことが第一優先
   - 整理は後からできる

2. **情報は「流れる」もの**
   - 時間とともに価値が変わる
   - 固定せず、流れに任せる

3. **リンクが知識を作る**
   - フォルダに閉じ込めない
   - 双方向リンクで知識を繋ぐ

---

## 📁 フォルダ構成の全体像

```
SecondBrain_Vault/
├─ 00_Memo/          # 何も考えず放り込む
├─ 01_Inbox/         # Cursor処理済み（週1回整理）
├─ 02_Daily/         # 毎日自動生成
├─ 03_Input/         # 今週〜今月使う資料
├─ 04_Memory/        # 永久保存の知識
├─ 05_Output/        # プロジェクト・継続活動
├─ 06_Templates/     # テンプレート集
├─ 07_System/        # システム設定・ダッシュボード
├─ 08_prompts/       # プロンプト集
└─ 99_Archive/       # 終わったもの
```

### フォルダの分類

- **00〜02**: 入力系（情報が入ってくる）
- **03〜04**: 記憶系（情報を保持する）
- **05**: 出力系（情報を使う）
- **06〜08**: メタ系（システム自体）
- **99**: 墓場系（もう使わない）

---

## 🔄 情報の流れ

```
00_Memo (生まれた瞬間)
   ↓
01_Inbox (Cursorで整理)
   ↓
03_Input (今週使う) or 04_Memory (ずっと使う) or 05_Output (アウトプット)
   ↓
99_Archive (役目を終えた)
```

---

## 📝 命名規則

### ファイル名
- デイリーノート: `YYYY-MM-DD-Daily.md`
- プロジェクト: `Project-Name/` フォルダ
- 知識ノート: `kebab-case.md`
- MOC: `_Category-MOC.md` (アンダースコアで先頭)

### タグ
- `#project/[プロジェクト名]` - プロジェクト関連
- `#area/[エリア名]` - エリア関連
- `#daily` - デイリーノート
- `#memory` - 長期記憶
- `#input` - 短期記憶

---

## 🛠️ 主要機能

### Cursorコマンド
- `/daily` - デイリーノート作成
- `/memo-to-inbox` - MemoをInboxに変換
- `/organize-inbox` - Inbox整理
- `/create-dashboards` - ダッシュボード作成
- `/weekly-review` - 週次レビュー

### ダッシュボード
- 🏠-HOME.md - 今日のホームダッシュボード
- 🎯-Projects-Dashboard.md - プロジェクト管理
- 📊-Weekly-Dashboard.md - 週次ダッシュボード
- 📈-Analytics-Dashboard.md - 分析ダッシュボード
- 🔥-Active-Focus.md - アクティブフォーカス

---

## 📚 関連ドキュメント

- [[best-practices.md]] - ベストプラクティス
- [[folder-structure-guide.md]] - フォルダ構造ガイド
- [[../Scripts/nightly-batch-process.md]] - 夜間バッチ処理
- [[../Workflows/daily-workflow.md]] - デイリーワークフロー
- [[../../AGENTS.md]] - Brain System Rules

---

## 🔗 外部リソース

- **Obsidian公式**: https://obsidian.md
- **Dataviewプラグイン**: https://github.com/blacksmithgu/obsidian-dataview
- **Templaterプラグイン**: https://github.com/SilentVoid13/Templater

---

**最終更新**: 2025-01-13
