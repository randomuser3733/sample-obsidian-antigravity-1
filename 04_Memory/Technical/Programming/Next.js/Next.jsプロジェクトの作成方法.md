# Next.jsプロジェクトの作成方法

**関連MOC**: [[_Next.js-MOC]] | [[_Tech-MOC]]

## 概要
Next.jsプロジェクトを作成する方法と、初期セットアップの手順を説明します。

## 詳細
Next.jsプロジェクトは`create-next-app`コマンドを使用して作成します。このコマンドは、Next.jsの最新機能を含む完全なプロジェクト構造を自動生成します。

## 基本的な使い方

### 1. 基本的なプロジェクト作成

```bash
npx create-next-app@latest my-app
```

このコマンドを実行すると、対話形式で以下の設定を選択できます：

- **プロジェクト名**: デフォルトは`my-app`
- **TypeScript**: TypeScriptを使用するか
- **ESLint**: ESLintを設定するか
- **Tailwind CSS**: Tailwind CSSを使用するか
- **`src/`ディレクトリ**: `src/`ディレクトリを使用するか
- **App Router**: App Routerを使用するか（推奨）
- **インポートエイリアス**: `@/*`エイリアスを設定するか

### 2. TypeScriptを使用する場合

```bash
npx create-next-app@latest my-app --typescript
```

または対話形式でTypeScriptを選択します。

### 3. すべてのオプションを指定する場合

```bash
npx create-next-app@latest my-app \
  --typescript \
  --tailwind \
  --eslint \
  --app \
  --src-dir \
  --import-alias "@/*"
```

### 4. 最小構成で作成（すべてNo）

```bash
npx create-next-app@latest my-app --no-typescript --no-tailwind --no-eslint
```

## プロジェクト作成後の手順

### 1. ディレクトリに移動

```bash
cd my-app
```

### 2. 開発サーバーを起動

```bash
npm run dev
# または
yarn dev
# または
pnpm dev
```

開発サーバーは通常`http://localhost:3000`で起動します。

### 3. ブラウザで確認

ブラウザで`http://localhost:3000`を開き、Next.jsのウェルカムページが表示されることを確認します。

## プロジェクト構造

作成される基本的な構造：

```
my-app/
├── app/                    # App Router（v13以降）
│   ├── layout.tsx         # ルートレイアウト
│   ├── page.tsx          # ホームページ
│   └── globals.css       # グローバルスタイル
├── public/                # 静的ファイル
├── next.config.js         # Next.js設定ファイル
├── package.json          # 依存関係
├── tsconfig.json         # TypeScript設定（TypeScript使用時）
└── tailwind.config.js    # Tailwind設定（Tailwind使用時）
```

## パッケージマネージャーの選択

### npm（デフォルト）

```bash
npx create-next-app@latest my-app
```

### yarn

```bash
yarn create next-app my-app
```

### pnpm

```bash
pnpm create next-app my-app
```

## 高度な使い方

### 1. 既存のディレクトリに作成

```bash
mkdir my-app
cd my-app
npx create-next-app@latest .
```

### 2. 特定のバージョンを指定

```bash
npx create-next-app@13.4.0 my-app
```

### 3. テンプレートを使用

```bash
npx create-next-app@latest my-app --example blog
```

利用可能なテンプレート：
- `blog`: ブログテンプレート
- `dashboard`: ダッシュボードテンプレート
- `e-commerce`: ECサイトテンプレート

## メリット・デメリット

### ✅ メリット
- **自動セットアップ**: 必要な設定が自動で完了
- **ベストプラクティス**: 推奨される構成で開始
- **最新機能**: 最新のNext.js機能が含まれる
- **型安全性**: TypeScriptオプションで型安全な開発が可能

### ❌ デメリット
- **初期ファイルが多い**: 不要なファイルが含まれる場合がある
- **カスタマイズが必要**: プロジェクトに応じて設定を調整する必要がある

## 使用例

### 例1: TypeScript + Tailwind CSSプロジェクト

```bash
npx create-next-app@latest my-blog \
  --typescript \
  --tailwind \
  --app \
  --import-alias "@/*"
```

### 例2: 最小構成のプロジェクト

```bash
npx create-next-app@latest simple-app \
  --no-typescript \
  --no-tailwind \
  --no-eslint \
  --app
```

## よくある問題と解決策

### 問題1: `create-next-app`が見つからない
**解決策**: Node.jsのバージョンを確認（v18.17以上推奨）

```bash
node --version
# v18.17.0以上であることを確認
```

### 問題2: プロジェクト作成が遅い
**解決策**: インターネット接続を確認、または`--use-npm`を指定

```bash
npx create-next-app@latest my-app --use-npm
```

### 問題3: パーミッションエラー
**解決策**: `sudo`を使用するか、npmのグローバル設定を確認

```bash
# npmのグローバルディレクトリを確認
npm config get prefix
```

## ベストプラクティス

1. **最新版を使用**: `@latest`タグを使用して最新版を取得
2. **TypeScriptを推奨**: 型安全性のためTypeScriptを使用
3. **App Routerを使用**: 新規プロジェクトはApp Routerを推奨
4. **パッケージマネージャーを統一**: チーム内で同じパッケージマネージャーを使用
5. **`.gitignore`を確認**: 不要なファイルがコミットされないように確認

## 次のステップ

プロジェクト作成後：

1. **開発サーバー起動**: `npm run dev`
2. **プロジェクト構造の理解**: [[Next.jsのプロジェクト構造]]を参照
3. **ルーティングの学習**: [[Next.jsのルーティング]]を参照
4. **ページ作成**: [[Next.jsのページ作成]]を参照

## 関連ノート
- [[Next.jsとは何か]]
- [[Next.jsのプロジェクト構造]]
- [[Next.jsの設定ファイル]]
- [[Next.jsのTypeScript設定]]

---
tags: [nextjs, setup, create-next-app, technical/programming]
created: 2025-11-13

