# Next.jsのビルドとデプロイ

**関連MOC**: [[_Next.js-MOC]] | [[_Tech-MOC]]

## 概要
Next.jsアプリケーションをビルドしてデプロイする方法を説明します。Vercelへのデプロイが最も簡単ですが、他のプラットフォームにもデプロイ可能です。

## 詳細
Next.jsは、`next build`コマンドでプロダクションビルドを作成し、静的エクスポートやサーバーレス関数としてデプロイできます。

## 基本的な使い方

### 1. プロダクションビルド

```bash
# ビルド
npm run build

# ビルド後のローカルプレビュー
npm run start
```

### 2. Vercelへのデプロイ

```bash
# Vercel CLIをインストール
npm i -g vercel

# デプロイ
vercel

# 本番環境にデプロイ
vercel --prod
```

### 3. 静的エクスポート

```javascript
// next.config.js
module.exports = {
  output: 'export',
};
```

```bash
npm run build
# out/ディレクトリに静的ファイルが生成される
```

## 高度な使い方

### 1. 環境別のビルド設定

```javascript
// next.config.js
module.exports = {
  env: {
    CUSTOM_KEY: process.env.CUSTOM_KEY,
  },
};
```

### 2. 画像最適化の設定

```javascript
// next.config.js
module.exports = {
  images: {
    domains: ['example.com'],
    formats: ['image/avif', 'image/webp'],
  },
};
```

### 3. リダイレクトとリライト

```javascript
// next.config.js
module.exports = {
  async redirects() {
    return [
      {
        source: '/old-page',
        destination: '/new-page',
        permanent: true,
      },
    ];
  },
};
```

## デプロイプラットフォーム

### 1. Vercel（推奨）

```bash
# GitHubと連携して自動デプロイ
# vercel.comでプロジェクトをインポート
```

### 2. Netlify

```bash
# netlify.tomlを作成
[build]
  command = "npm run build"
  publish = ".next"

[[plugins]]
  package = "@netlify/plugin-nextjs"
```

### 3. AWS Amplify

```yaml
# amplify.yml
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - npm install
    build:
      commands:
        - npm run build
  artifacts:
    baseDirectory: .next
    files:
      - '**/*'
```

## メリット・デメリット

### ✅ メリット
- **簡単**: Vercelへのデプロイが非常に簡単
- **高速**: 自動的な最適化とCDN配信
- **スケーラブル**: 自動スケーリング

### ❌ デメリット
- **制約**: プラットフォームごとに制約がある
- **コスト**: 大規模なアプリケーションではコストがかかる場合がある

## 使用例

### 例1: Vercelへのデプロイ

1. GitHubリポジトリにプッシュ
2. Vercelでプロジェクトをインポート
3. 自動的にデプロイ

### 例2: 静的サイトとしてデプロイ

```javascript
// next.config.js
module.exports = {
  output: 'export',
  images: {
    unoptimized: true,
  },
};
```

## よくある問題と解決策

### 問題1: ビルドエラー
**解決策**: エラーメッセージを確認し、依存関係を確認

```bash
npm install
npm run build
```

### 問題2: 環境変数が設定されない
**解決策**: デプロイプラットフォームで環境変数を設定

## ベストプラクティス

1. **環境変数**: 本番環境の環境変数を設定
2. **ビルド最適化**: 不要な依存関係を削除
3. **パフォーマンス**: 画像最適化を有効化
4. **監視**: エラーログを監視

## 関連ノート
- [[Next.jsの設定ファイル]]
- [[Next.jsの環境変数設定]]

---
tags: [nextjs, deployment, build, technical/programming]
created: 2025-11-13

