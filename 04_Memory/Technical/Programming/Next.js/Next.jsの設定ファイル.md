# Next.jsの設定ファイル

**関連MOC**: [[_Next.js-MOC]] | [[_Tech-MOC]]

## 概要
`next.config.js`（または`next.config.mjs`）は、Next.jsアプリケーションの設定をカスタマイズするファイルです。画像最適化、リダイレクト、環境変数などの設定が可能です。

## 詳細
`next.config.js`は、Next.jsのビルド時とランタイムの動作を制御します。TypeScriptを使用する場合は`next.config.ts`も使用可能です。

## 基本的な使い方

### 1. 基本的な設定

```javascript
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
};

module.exports = nextConfig;
```

### 2. TypeScript設定

```typescript
// next.config.ts
import type { NextConfig } from 'next';

const nextConfig: NextConfig = {
  reactStrictMode: true,
};

export default nextConfig;
```

## 主要な設定オプション

### 1. 画像最適化

```javascript
// next.config.js
module.exports = {
  images: {
    domains: ['example.com'],
    formats: ['image/avif', 'image/webp'],
  },
};
```

### 2. リダイレクト

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

### 3. リライト

```javascript
// next.config.js
module.exports = {
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: 'https://api.example.com/:path*',
      },
    ];
  },
};
```

### 4. 環境変数

```javascript
// next.config.js
module.exports = {
  env: {
    CUSTOM_KEY: 'my-value',
  },
};
```

### 5. 静的エクスポート

```javascript
// next.config.js
module.exports = {
  output: 'export',
};
```

## 高度な使い方

### 1. Webpack設定のカスタマイズ

```javascript
// next.config.js
module.exports = {
  webpack: (config, { isServer }) => {
    if (!isServer) {
      config.resolve.fallback = {
        ...config.resolve.fallback,
        fs: false,
      };
    }
    return config;
  },
};
```

### 2. 実験的機能

```javascript
// next.config.js
module.exports = {
  experimental: {
    appDir: true,
    serverActions: true,
  },
};
```

## メリット・デメリット

### ✅ メリット
- **柔軟性**: 幅広いカスタマイズが可能
- **パフォーマンス**: 最適化設定が可能

### ❌ デメリット
- **複雑性**: 設定が複雑になる場合がある

## 使用例

### 例1: 基本的な設定

```javascript
// next.config.js
module.exports = {
  reactStrictMode: true,
  swcMinify: true,
  images: {
    domains: ['example.com'],
  },
};
```

## よくある問題と解決策

### 問題1: 設定が反映されない
**解決策**: 開発サーバーを再起動

```bash
npm run dev
```

## ベストプラクティス

1. **型安全**: TypeScript設定ファイルを使用
2. **ドキュメント**: 設定の理由をコメントで記述
3. **環境別設定**: 環境ごとに異なる設定を検討

## 関連ノート
- [[Next.jsのビルドとデプロイ]]
- [[Next.jsの環境変数設定]]

---
tags: [nextjs, configuration, next-config, technical/programming]
created: 2025-11-13

