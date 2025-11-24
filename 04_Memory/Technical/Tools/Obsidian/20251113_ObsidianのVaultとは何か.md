# ObsidianのVaultとは何か

## 概要
Vault（ボルト）は、Obsidianにおける知識ベースの基本単位です。すべてのノート、フォルダ、設定、プラグインが1つのVault内に保存されます。

## 詳細

### Vaultの定義
**Vault = あなたの知識の金庫**

Vaultは単なるフォルダではなく、Obsidianが管理する特別なディレクトリです。1つのVaultには以下が含まれます：
- すべてのMarkdownファイル（.md）
- 画像、PDFなどの添付ファイル
- `.obsidian`フォルダ（設定、プラグイン、テーマ）
- プラグインのデータファイル

### Vaultの構造例
```
MySecondBrain/              ← Vaultのルート
├─ .obsidian/              ← 設定フォルダ（隠しフォルダ）
│  ├─ config.json         ← メイン設定
│  ├─ plugins/            ← プラグインフォルダ
│  ├─ themes/            ← テーマフォルダ
│  └─ workspace.json     ← ワークスペース設定
├─ 00_Memo/              ← あなたのノート
├─ 01_Inbox/
├─ 02_Daily/
└─ ...
```

## 基本的な使い方

### Vaultの作成
1. Obsidianを起動
2. "Create new vault"を選択
3. フォルダ名を入力（例: `SecondBrain`）
4. 保存場所を選択
5. "Create"をクリック

### 複数のVaultの管理
```
複数のVaultを使い分ける例:

1. Personal-Vault/      ← 個人の知識管理
2. Work-Vault/          ← 仕事用の知識管理
3. Learning-Vault/      ← 学習専用
```

**切り替え方法**:
- メニュー: File → Open Vault
- 最近使ったVaultが一覧表示される

## 高度な使い方

### Vault間でのデータ共有
Obsidianでは直接的なVault間リンクはできませんが、以下の方法があります：

1. **シンボリックリンク**: 特定のフォルダを共有
2. **エクスポート/インポート**: ノートを別Vaultにコピー
3. **外部リンク**: `[[vault:Vault名/ノート名]]`形式（有料版）

### Vaultのバックアップ
```bash
# Gitでバックアップ（推奨）
cd ~/Documents/SecondBrain
git init
git add .
git commit -m "Initial commit"

# 定期的なバックアップ
git add .
git commit -m "Daily backup"
```

### Vaultの同期
- **Obsidian Sync**: 公式の有料同期サービス
- **Git**: 無料の代替手段（手動）
- **Dropbox/iCloud**: フォルダ同期サービスを利用

## メリット・デメリット

### ✅ メリット
1. **完全な分離**: 仕事とプライベートを完全に分離
2. **設定の独立**: 各Vaultで異なる設定・プラグインが可能
3. **パフォーマンス**: 小さいVaultは動作が軽い
4. **バックアップ**: Vault単位でバックアップ可能

### ❌ デメリット
1. **Vault間リンク不可**: 無料版ではVault間の直接リンク不可
2. **設定の重複**: 各Vaultで設定を個別に管理する必要
3. **検索の分離**: Vaultをまたいだ検索ができない

## 使用例

### シナリオ1: 単一Vault戦略
```
SecondBrain/
├─ Personal/        ← プライベートノート
├─ Work/           ← 仕事ノート
└─ Learning/       ← 学習ノート

メリット: すべての知識が1箇所に
デメリット: プライバシー管理が難しい
```

### シナリオ2: 複数Vault戦略
```
Personal-Vault/     ← 完全に分離
Work-Vault/        ← 完全に分離

メリット: プライバシー、セキュリティ
デメリット: 知識の統合が難しい
```

### シナリオ3: ハイブリッド戦略
```
Main-Vault/         ← メインの知識ベース
├─ Personal/
└─ Work/

Project-Vault/      ← 特定プロジェクト専用
```

## よくある問題と解決策

### 問題1: Vaultが大きくなりすぎて重い
**解決策**:
- 古いノートをアーカイブVaultに移動
- 添付ファイルを外部ストレージに移動
- プラグインを最小限に

### 問題2: どのVaultに保存すべきか迷う
**解決策**:
- 明確なルールを設定（例: 仕事関連はWork-Vault）
- デフォルトVaultを設定
- 週次レビューで整理

### 問題3: Vault間でノートを共有したい
**解決策**:
- エクスポート/インポート機能を使用
- シンボリックリンクでフォルダ共有
- Obsidian Sync（有料）でVault間リンク

## ベストプラクティス

1. **Vault名は明確に**: `SecondBrain`より`Personal-Knowledge-Base`の方が明確
2. **1つのVaultから始める**: 必要に応じて分割
3. **定期的なバックアップ**: Gitまたはクラウドストレージで
4. **設定の統一**: 複数Vaultを使う場合、設定を統一すると管理しやすい
5. **サイズ管理**: 10,000ファイル以上になったら分割を検討

## 関連ノート
- [[20251113_Obsidianとは何か]]
- [[20251113_Obsidianのインストールとセットアップ]]
- [[20251113_Obsidianのフォルダ構造設計]]

#obsidian #vault #knowledge-management #memory候補
