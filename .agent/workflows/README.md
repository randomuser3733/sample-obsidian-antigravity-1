# Cursor Commands for Obsidian Vault

このフォルダには、Obsidian Vault管理用のCursor AIコマンドが含まれています。

## 📖 使い方

### コマンドの実行方法

#### 方法1: Cursor Chat (Cmd/Ctrl + L)
チャットを開いて、`/コマンド名` を入力します。

#### 方法2: インライン (Cmd/Ctrl + K)
インライン編集で `/コマンド名` を入力します。

#### 方法3: コンポーザー (Cmd/Ctrl + I)
コンポーザーで `/コマンド名` を入力します。

---

## 🛠️ 利用可能なコマンド

### 1. /daily
**説明**: 今日のデイリーノートを作成  
**使用例**: `/daily`

### 2. /mtg [議題]
**説明**: MTG議事録を作成  
**使用例**: `/mtg ProjectX定例`

### 3. /inbox-review
**説明**: Inboxを分析して整理案を提示  
**使用例**: `/inbox-review`

### 4. /make-memory [ファイル名]
**説明**: InboxノートをMemory Note（長期記憶）に昇華  
**使用例**: `/make-memory 20241022_API設計メモ.md`

### 5. /find-unlinked-notes
**説明**: リンクされていないノート（バックリンク0）を検索してリンク候補を提案  
**使用例**: `/find-unlinked-notes`

### 6. /suggest-links
**説明**: 現在のノートに関連するノートを提案  
**使用例**: `/suggest-links`

### 7. /optimize-tags [ファイル名]
**説明**: 指定ファイルのタグを最適化  
**使用例**: `/optimize-tags` または `/optimize-tags 20241022_API設計.md`

### 8. /weekly-review
**説明**: 週次レビューを実行  
**使用例**: `/weekly-review`

### 9. /summarize [ファイル名]
**説明**: 指定ノートを要約  
**使用例**: `/summarize` または `/summarize 20241022_長文ノート.md`

### 10. /project-view [プロジェクト名]
**説明**: プロジェクトに関連する全ノートを統合表示  
**使用例**: `/project-view ProjectX`

### 11. /archive [ファイル名]
**説明**: 指定ファイルをアーカイブに移動  
**使用例**: `/archive` または `/archive 20241022_薄いメモ.md`

### 12. /archive-review
**説明**: 3ヶ月以上前のアーカイブをレビュー  
**使用例**: `/archive-review`

### 13. /research [テーマ]
**説明**: 指定テーマについて網羅的に知識を調査  
**使用例**: `/research React Hooks` または `/research TypeScript`

### 14. /memo-to-inbox [ファイル名]
**説明**: 00_Memoのメモを01_Inboxの形式に整理して移動（承認不要で自動実行）  
**使用例**: `/memo-to-inbox` または `/memo-to-inbox 雑メモ.md`

### 15. /organize-inbox [ファイル名]
**説明**: Inboxフォルダ内のファイルを適切なフォルダに振り分け  
**使用例**: `/organize-inbox` または `/organize-inbox 20241022_API設計メモ.md`

### 16. /self-analysis
**説明**: あきらパパの自己分析会議を実施（月1回推奨）  
**使用例**: `/self-analysis`

### 17. /create-dashboards [ダッシュボード名]
**説明**: 各種ダッシュボードを作成・更新  
**使用例**: 
- `/create-dashboards` - 全てのダッシュボードを作成
- `/create-dashboards home` - HOMEダッシュボードのみ作成
- `/create-dashboards 🏠` - HOMEダッシュボードのみ作成
- `/create-dashboards projects` - プロジェクトダッシュボードのみ作成
- `/create-dashboards 🎯` - プロジェクトダッシュボードのみ作成
- `/create-dashboards weekly` - 週次ダッシュボードのみ作成
- `/create-dashboards 📊` - 週次ダッシュボードのみ作成
- `/create-dashboards analytics` - 分析ダッシュボードのみ作成
- `/create-dashboards 📈` - 分析ダッシュボードのみ作成
- `/create-dashboards focus` - アクティブフォーカスダッシュボードのみ作成
- `/create-dashboards 🔥` - アクティブフォーカスダッシュボードのみ作成

**作成されるダッシュボード:**
- HOMEダッシュボード.md - 今日のホームダッシュボード
- プロジェクトダッシュボード.md - プロジェクト管理ダッシュボード
- 週次ダッシュボード.md - 週次ダッシュボード
- 分析ダッシュボード.md - 分析ダッシュボード
- アクティブフォーカス.md - アクティブフォーカスダッシュボード

---

## 🔄 よく使う組み合わせ

### 朝のルーティン
```
1. /daily
2. /create-dashboards home
3. 今日のタスクを追記
```

### 夕方のルーティン
```
1. Dailyに気づきを追記
2. /summarize で今日のInboxを要約
```

### 金曜日のルーティン
```
1. /weekly-review
2. /create-dashboards weekly
3. /inbox-review
4. /find-unlinked-notes
5. /archive (必要に応じて)
```

### 新技術の調査
```
1. /research [テーマ]
   → 網羅的に知識を調査
   → 複数のノートが自動生成
2. 週次整理で04_Memory/に移動
```

### 四半期ごと（3ヶ月に1回）
```
1. /archive-review
2. 古いアーカイブの削除判断
```

### Memo整理（月1回）
```
1. /memo-to-inbox [ファイル名]
   → 整理が必要なメモを01_Inboxに移動（自動実行）
   → 元のファイルは99_Archiveに移動
```

### Inbox整理（週1回）
```
1. /organize-inbox [ファイル名]
   → Inboxファイルを適切なフォルダに振り分け
   → 04_Memory, 03_Input, 05_Output等に移動
```

### 自己分析（月1回）
```
1. /self-analysis
   → あきらパパの自己分析会議を実施
   → 4人のキャラクターによる多角的な分析
   → 04_Memory/Personal/Self-Analysis/フォルダに分析結果を保存
```

---

## 📌 ヒント

- コマンド名の最初の数文字を入力すると補完されます
- ファイル名の引数がない場合、現在開いているファイルが対象になります
- 各コマンドは対話形式で実行され、確認や選択を求められる場合があります

---

## 📚 関連リソース

- **プロンプト集**: [[08_prompts/README.md]] - 効果的だったプロンプトをカテゴリ別に保存
- **Brain System Rules**: [[AGENTS.md]] - システム全体のルール
- **システムドキュメント**: [[07_System/Documentation/system-overview.md]]

詳細は各コマンドファイル（`.md`）を参照してください。

