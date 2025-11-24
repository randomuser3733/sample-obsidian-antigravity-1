# Next.jsの環境変数設定

**関連MOC**: [[_Next.js-MOC]] | [[_Tech-MOC]]

## 概要
Next.jsでは、環境変数を使用して設定値を管理します。`.env.local`ファイルに環境変数を定義し、アプリケーション内で使用できます。

## 詳細
Next.jsの環境変数は、`.env.local`、`.env.development`、`.env.production`などのファイルで定義します。Server Componentでは`process.env`で直接アクセスでき、Client Componentでは`NEXT_PUBLIC_`プレフィックスが必要です。

## 基本的な使い方

### 1. 環境変数ファイルの作成

```bash
# .env.local
DATABASE_URL=postgresql://user:password@localhost:5432/mydb
API_KEY=your-api-key-here
NEXT_PUBLIC_API_URL=https://api.example.com
```

### 2. Server Componentでの使用

```tsx
// app/api-data/page.tsx
export default async function ApiDataPage() {
  // Server Componentでは直接アクセス可能
  const apiKey = process.env.API_KEY;
  const data = await fetch(`https://api.example.com/data?key=${apiKey}`);
  
  return <div>Data loaded</div>;
}
```

### 3. Client Componentでの使用

```tsx
// app/components/ClientComponent.tsx
'use client';

export default function ClientComponent() {
  // NEXT_PUBLIC_プレフィックスが必要
  const apiUrl = process.env.NEXT_PUBLIC_API_URL;
  
  return <div>API URL: {apiUrl}</div>;
}
```

## 環境変数の種類

### 1. `.env.local`

すべての環境で読み込まれる（gitignoreに追加推奨）

```bash
# .env.local
DATABASE_URL=postgresql://...
SECRET_KEY=your-secret-key
```

### 2. `.env.development`

開発環境でのみ読み込まれる

```bash
# .env.development
DATABASE_URL=postgresql://localhost:5432/dev-db
```

### 3. `.env.production`

本番環境でのみ読み込まれる

```bash
# .env.production
DATABASE_URL=postgresql://prod-server:5432/prod-db
```

### 4. `.env.example`

環境変数の例（コミット推奨）

```bash
# .env.example
DATABASE_URL=postgresql://user:password@localhost:5432/mydb
API_KEY=your-api-key-here
NEXT_PUBLIC_API_URL=https://api.example.com
```

## 高度な使い方

### 1. 環境変数の型定義

```typescript
// env.d.ts
declare namespace NodeJS {
  interface ProcessEnv {
    DATABASE_URL: string;
    API_KEY: string;
    NEXT_PUBLIC_API_URL: string;
  }
}
```

### 2. 環境変数のバリデーション

```typescript
// lib/env.ts
function getEnvVar(key: string): string {
  const value = process.env[key];
  if (!value) {
    throw new Error(`Environment variable ${key} is not set`);
  }
  return value;
}

export const env = {
  databaseUrl: getEnvVar('DATABASE_URL'),
  apiKey: getEnvVar('API_KEY'),
};
```

### 3. ランタイム環境変数

```tsx
// next.config.js
module.exports = {
  env: {
    CUSTOM_KEY: 'my-value',
  },
};
```

## メリット・デメリット

### ✅ メリット
- **セキュリティ**: 機密情報をコードから分離
- **環境別設定**: 環境ごとに異なる設定が可能
- **簡単**: 設定が簡単

### ❌ デメリット
- **型安全性**: 型定義が必要
- **バリデーション**: 手動でバリデーションが必要

## 使用例

### 例1: データベース接続

```typescript
// lib/db.ts
import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient({
  datasources: {
    db: {
      url: process.env.DATABASE_URL,
    },
  },
});

export { prisma };
```

### 例2: APIクライアント

```typescript
// lib/api.ts
const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:3000';

export async function fetchData() {
  const res = await fetch(`${API_URL}/api/data`);
  return res.json();
}
```

## よくある問題と解決策

### 問題1: 環境変数がundefined
**解決策**: 環境変数名を確認、`.env.local`が正しい場所にあるか確認

```bash
# .env.localがプロジェクトルートにあるか確認
```

### 問題2: Client Componentで環境変数が使用できない
**解決策**: `NEXT_PUBLIC_`プレフィックスを追加

```bash
# .env.local
NEXT_PUBLIC_API_URL=https://api.example.com
```

### 問題3: 環境変数が更新されない
**解決策**: 開発サーバーを再起動

```bash
npm run dev
```

## ベストプラクティス

1. **`.env.local`をgitignoreに追加**: 機密情報をコミットしない
2. **`.env.example`を作成**: 必要な環境変数をドキュメント化
3. **型定義**: TypeScriptで環境変数の型を定義
4. **バリデーション**: 起動時に環境変数をバリデーション

## 関連ノート
- [[Next.jsの設定ファイル]]
- [[Next.jsのAPI Routes]]

---
tags: [nextjs, environment-variables, configuration, technical/programming]
created: 2025-11-13

