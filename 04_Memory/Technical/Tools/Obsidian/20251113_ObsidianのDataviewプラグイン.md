# ObsidianのDataviewプラグイン

## 概要
Dataviewは、Obsidianのノートをデータベースのように扱える強力なプラグインです。フロントマターやタグ、リンクなどのメタデータをクエリして、動的なリストやテーブルを作成できます。

## 詳細

### Dataviewとは
**Dataview = ノートをデータベースのようにクエリするプラグイン**

```
従来のノートアプリ:
- ノートを手動で整理
- リストを手動で作成・更新

Dataview:
- ノートを自動的にクエリ
- 動的なリスト・テーブルを自動生成
- メタデータに基づいて自動集計
```

### Dataviewのインストール
1. 設定を開く（`Ctrl+,` または `Cmd+,`）
2. 「コミュニティプラグイン」を選択
3. 「安全モードをオフにする」を有効化
4. 「参照」をクリック
5. "Dataview"を検索してインストール

## 基本的な使い方

### 基本的なクエリ
```dataview
LIST
FROM ""
```

```
説明:
- LIST: リスト形式で表示
- FROM "": すべてのノートから検索
```

### タグでフィルター
```dataview
LIST
FROM #react
```

```
説明:
- FROM #react: #reactタグを持つノートのみ表示
```

### フォルダでフィルター
```dataview
LIST
FROM "04_Memory/AI"
```

```
説明:
- FROM "04_Memory/AI": 指定フォルダ内のノートのみ表示
```

## 高度な使い方

### テーブル形式の表示
```dataview
TABLE status, priority, created
FROM "05_Output/Projects"
WHERE status = "active"
SORT priority DESC
```

```
説明:
- TABLE: テーブル形式で表示
- status, priority, created: 表示する列
- WHERE: 条件（status = "active"）
- SORT: 並び替え（priority DESC = 優先度の降順）
```

### 複合条件
```dataview
TABLE status, priority
FROM "05_Output/Projects"
WHERE status = "active" AND priority = "high"
SORT created DESC
```

### 日付フィルター
```dataview
LIST
FROM ""
WHERE file.ctime >= date(today) - dur(7 days)
SORT file.ctime DESC
```

```
説明:
- file.ctime: ファイルの作成日
- date(today) - dur(7 days): 7日前から今日まで
```

### タスクの集計
```dataview
TASK
FROM ""
WHERE !completed
GROUP BY file.link
```

```
説明:
- TASK: タスク形式で表示
- !completed: 未完了のタスクのみ
- GROUP BY: ファイルごとにグループ化
```

### 統計情報
```dataview
TABLE length(rows) as "ノート数"
FROM #react
GROUP BY file.folder
```

```
説明:
- length(rows): 行数（ノート数）
- GROUP BY: フォルダごとにグループ化
```

## メリット・デメリット

### ✅ メリット
1. **自動更新**: ノートを追加・更新すると自動で反映
2. **柔軟なクエリ**: 複雑な条件で検索・集計可能
3. **動的リスト**: 手動でリストを更新する必要がない
4. **統計情報**: ノートの統計を自動計算
5. **ダッシュボード**: 動的なダッシュボードを作成可能

### ❌ デメリット
1. **学習曲線**: クエリ構文の習得に時間がかかる
2. **パフォーマンス**: 大量のノートがあると動作が遅い
3. **フロントマター必須**: メタデータが必要
4. **エラー**: 構文エラーで表示されない

## 使用例

### シナリオ1: プロジェクトダッシュボード
```dataview
TABLE status, priority, deadline
FROM "05_Output/Projects/@Active"
SORT priority DESC, deadline ASC
```

```
→ アクティブなプロジェクトを優先度順に表示
```

### シナリオ2: 学習ノート一覧
```dataview
LIST
FROM #learning
WHERE file.ctime >= date(today) - dur(30 days)
SORT file.ctime DESC
```

```
→ 過去30日間の学習ノートを新しい順に表示
```

### シナリオ3: タスク管理
```dataview
TASK
FROM ""
WHERE !completed AND contains(tags, "#todo")
GROUP BY file.link
```

```
→ 未完了のタスクをファイルごとにグループ化
```

## よくある問題と解決策

### 問題1: クエリが表示されない
**解決策**:
- クエリ構文を確認（スペルミス、大文字小文字）
- フロントマターが正しく記述されているか確認
- Dataviewプラグインが有効化されているか確認

**例**:
```dataview
❌ 悪い例:
TABLE status
FROM "05_Output/Projects"
WHERE status = "active"  ← クォートが不一致

✅ 良い例:
TABLE status
FROM "05_Output/Projects"
WHERE status = "active"
```

### 問題2: パフォーマンスが遅い
**解決策**:
- 検索範囲を限定（FROM句でフォルダ指定）
- 表示する列を減らす
- インデックスの再構築

### 問題3: フロントマターが認識されない
**解決策**:
- フロントマターの構文を確認（YAML形式）
- キー名が正しいか確認
- データ型が正しいか確認（文字列、数値、日付）

## ベストプラクティス

1. **フロントマターを統一**: チームで統一したフォーマットを使用
2. **クエリをシンプルに**: 複雑なクエリは分割
3. **パフォーマンスを意識**: 検索範囲を限定
4. **エラーハンドリング**: クエリが表示されない場合の対処法を準備
5. **ドキュメント参照**: 公式ドキュメントを参照

## 関連ノート
- [[20251113_Obsidianのプラグインシステム]]
- [[20251113_Obsidianのフロントマター]]
- [[20251113_Obsidianのダッシュボード作成]]

#obsidian #dataview #プラグイン #knowledge-management #memory候補
