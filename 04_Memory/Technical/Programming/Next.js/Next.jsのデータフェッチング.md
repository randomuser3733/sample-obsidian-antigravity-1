# Next.jsのデータフェッチング

**関連MOC**: [[_Next.js-MOC]] | [[_Tech-MOC]]

## 概要
Next.js App Routerでは、Server Componentsで直接データをフェッチできます。fetch APIを拡張し、キャッシング、再検証、ストリーミングなどの機能を提供します。

## 詳細
Next.jsのデータフェッチングは、Server Componentsで`fetch`を使用するか、データベースに直接接続することで実現します。自動的なキャッシングと再検証により、パフォーマンスを最適化します。

## 基本的な使い方

### 1. 基本的なデータフェッチング

```tsx
// app/products/page.tsx
async function getProducts() {
  const res = await fetch('https://api.example.com/products');
  return res.json();
}

export default async function ProductsPage() {
  const products = await getProducts();
  
  return (
    <div>
      {products.map((product) => (
        <div key={product.id}>{product.name}</div>
      ))}
    </div>
  );
}
```

### 2. データベースへの直接アクセス

```tsx
// app/users/page.tsx
import { db } from '@/lib/db';

export default async function UsersPage() {
  const users = await db.user.findMany();
  
  return (
    <div>
      {users.map((user) => (
        <div key={user.id}>{user.name}</div>
      ))}
    </div>
  );
}
```

### 3. エラーハンドリング

```tsx
// app/products/page.tsx
async function getProducts() {
  try {
    const res = await fetch('https://api.example.com/products');
    
    if (!res.ok) {
      throw new Error('Failed to fetch products');
    }
    
    return res.json();
  } catch (error) {
    console.error('Error fetching products:', error);
    return [];
  }
}
```

## 高度な使い方

### 1. キャッシュの制御

```tsx
// キャッシュを無効化
async function getProducts() {
  const res = await fetch('https://api.example.com/products', {
    cache: 'no-store', // 常に最新データを取得
  });
  return res.json();
}

// 再検証時間を設定
async function getProducts() {
  const res = await fetch('https://api.example.com/products', {
    next: { revalidate: 3600 }, // 1時間ごとに再検証
  });
  return res.json();
}
```

### 2. 並列データフェッチング

```tsx
// app/dashboard/page.tsx
async function getUser() {
  const res = await fetch('https://api.example.com/user');
  return res.json();
}

async function getPosts() {
  const res = await fetch('https://api.example.com/posts');
  return res.json();
}

export default async function DashboardPage() {
  // 並列でデータを取得
  const [user, posts] = await Promise.all([
    getUser(),
    getPosts(),
  ]);
  
  return (
    <div>
      <h1>Welcome, {user.name}</h1>
      <div>
        {posts.map((post) => (
          <div key={post.id}>{post.title}</div>
        ))}
      </div>
    </div>
  );
}
```

### 3. ストリーミング

```tsx
// app/dashboard/page.tsx
import { Suspense } from 'react';

async function SlowComponent() {
  await new Promise(resolve => setTimeout(resolve, 2000));
  const data = await fetch('https://api.example.com/slow-data');
  return <div>Slow Data: {data.json()}</div>;
}

export default function DashboardPage() {
  return (
    <div>
      <div>Fast Content</div>
      <Suspense fallback={<div>Loading...</div>}>
        <SlowComponent />
      </Suspense>
    </div>
  );
}
```

## データフェッチングのパターン

### 1. Server Componentsでのフェッチ

```tsx
// app/products/page.tsx
async function getProducts() {
  const res = await fetch('https://api.example.com/products');
  return res.json();
}

export default async function ProductsPage() {
  const products = await getProducts();
  return <div>{/* レンダリング */}</div>;
}
```

### 2. Route Handlerでのフェッチ

```tsx
// app/api/products/route.ts
export async function GET() {
  const res = await fetch('https://api.example.com/products');
  return Response.json(await res.json());
}
```

### 3. Server Actions

```tsx
// app/actions.ts
'use server';

export async function createProduct(data: FormData) {
  const name = data.get('name');
  // データベースに保存
  // ...
}
```

## メリット・デメリット

### ✅ メリット
- **自動キャッシング**: デフォルトでキャッシングが有効
- **パフォーマンス**: サーバー側でデータを取得し、高速
- **SEO**: サーバー側レンダリングによりSEOが向上
- **セキュリティ**: 機密情報をクライアントに送信しない

### ❌ デメリット
- **リアルタイム更新**: リアルタイム更新には追加の設定が必要
- **キャッシュ管理**: キャッシュ戦略の理解が必要

## 使用例

### 例1: ブログ記事の取得

```tsx
// app/blog/[slug]/page.tsx
async function getPost(slug: string) {
  const res = await fetch(`https://api.example.com/posts/${slug}`, {
    next: { revalidate: 3600 },
  });
  
  if (!res.ok) {
    return null;
  }
  
  return res.json();
}

export default async function BlogPost({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const post = await getPost(slug);
  
  if (!post) {
    return <div>Post not found</div>;
  }
  
  return (
    <article>
      <h1>{post.title}</h1>
      <div>{post.content}</div>
    </article>
  );
}
```

## よくある問題と解決策

### 問題1: キャッシュが更新されない
**解決策**: `cache: 'no-store'`または`revalidate`を設定

```tsx
const res = await fetch(url, {
  cache: 'no-store',
});
```

### 問題2: 環境変数が使用できない
**解決策**: Server Componentでは`process.env`を直接使用

```tsx
const apiKey = process.env.API_KEY; // NEXT_PUBLIC_は不要
```

## ベストプラクティス

1. **Server Componentsでフェッチ**: デフォルトでServer Componentsを使用
2. **並列フェッチ**: `Promise.all`で並列にデータを取得
3. **キャッシュ戦略**: 適切なキャッシュ設定を使用
4. **エラーハンドリング**: 適切なエラーハンドリングを実装

## 関連ノート
- [[Next.jsのServer Components]]
- [[Next.jsのAPI Routes]]

---
tags: [nextjs, data-fetching, server-components, technical/programming]
created: 2025-11-13

