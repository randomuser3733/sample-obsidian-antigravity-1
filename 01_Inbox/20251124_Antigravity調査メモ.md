# Antigravity調査メモ（回答案）

## 概要
Antigravityの仕様、Browser発動条件、ワークフローの考え方、Artifactsの場所などについての調査メモ。あきらパパさんとのセミナー準備用。

## 内容
### 1. AntigravityのBrowserの発動条件
- **発動トリガー**: プロンプトの意図（Intent）、Planのステップ（Verify/Research）、Tool Callによって自動発動。
- **必須条件**: Chrome拡張機能の有効化、設定ON。

### 2. ワークフロー.md と Claude Code Skills の比較
- **Antigravity**: タスク指向。エージェントへの「指示書・手順書」。Planのベース。
- **Claude Code**: 機能指向。モジュール化された「道具」。
- **確認ポイント**: Antigravityは「ゴールと制約条件を与えて任せる」スタイル。

### 3. ツール発動フックのワード
- **動詞（Action Verbs）**が重要: Orchestrate, Scaffold, Diagnose, Verify。
- 具体的な目的（いつ、何のために）をDescriptionに書く。

### 4. Acceptを完全になくす方法
- `// turbo-all` は存在しない。
- **設定**: Terminal Auto Execution: Turbo, Artifact Review Policy: Always Approve。
- 破壊的操作には安全装置が働く。

### 5. 保管場所
- `~/.gemini/antigravity/`: Brain, Browser Recordings, Playground。
- VS Code上では仮想的に表示される。

### 6. グローバルパス .antigravity
- IDE設定やAuthトークン用。

### 7. .gemini/antigravity
- AIの長期記憶と成果物。Session IDごとに保存。

### 8. ショートカット
- `Cmd+I`: インラインチャット
- `Cmd+E`: Editor ⇄ Manager 切り替え（重要）
- `Cmd+L`: Agent Manager

### Antigravity vs Cursor
- **Cursor**: スーパープログラマの助手（Copilot）。自分が主導。
- **Antigravity**: 新人エンジニアのチーム（Agents）。マネージャー業に近い。

## 次アクション
- [ ] あきらパパさんとのセミナーで共有
- [ ] ドキュメントとして整理

#inbox #antigravity #seminar #faq
