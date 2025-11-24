# Next.jsのServer Components

**関連MOC**: [[_Next.js-MOC]] | [[_Tech-MOC]]

## 概要
Server ComponentsはNext.js App Routerの核心機能で、サーバー側でレンダリングされるReactコンポーネントです。クライアントにJavaScriptを送信せず、パフォーマンスとSEOを大幅に向上させます。

## 詳細
Server Componentsは、サーバー側でレンダリングされ、HTMLとしてクライアントに送信されます。これにより、バンドルサイズが削減され、データベースやAPIへの直接アクセスが可能になります。

## 基本的な使い方

### 1. デフォルトでServer Component

```tsx
// app/products/page.tsx
// 'use client'がない = Server Component

async function getProducts() {
  const res = await fetch('https://api.example.com/products');
  return res.json();
}

export default async function ProductsPage() {
  const products = await getProducts();
  
  return (
    <div>
      <h1>Products</h1>
      {products.map((product) => (
        <div key={product.id}>
          <h2>{product.name}</h2>
          <p>{product.description}</p>
        </div>
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
  // Server Componentでは直接データベースにアクセス可能
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

### 3. 環境変数の使用

```tsx
// app/api-data/page.tsx
export default async function ApiDataPage() {
  // Server Componentでは環境変数を直接使用可能
  const apiKey = process.env.API_KEY;
  const data = await fetch(`https://api.example.com/data?key=${apiKey}`);
  
  return <div>Data loaded</div>;
}
```

## 高度な使い方

### 1. ストリーミング

```tsx
// app/dashboard/page.tsx
import { Suspense } from 'react';

async function SlowComponent() {
  await new Promise(resolve => setTimeout(resolve, 2000));
  return <div>Slow Content</div>;
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

### 3. キャッシュの制御

```tsx
// app/products/page.tsx
async function getProducts() {
  // キャッシュを無効化
  const res = await fetch('https://api.example.com/products', {
    cache: 'no-store',
  });
  return res.json();
}

// または、再検証時間を設定
async function getProductsWithRevalidate() {
  const res = await fetch('https://api.example.com/products', {
    next: { revalidate: 3600 }, // 1時間ごとに再検証
  });
  return res.json();
}
```

## Server Componentsの特徴

### ✅ できること

1. **データベースアクセス**: 直接データベースに接続可能
2. **バックエンドAPIアクセス**: 内部APIや外部APIにアクセス可能
3. **環境変数**: `process.env`を使用可能
4. **ファイルシステム**: Node.jsのファイルシステムAPIを使用可能
5. **バンドルサイズ削減**: クライアントにJavaScriptを送信しない

### ❌ できないこと

1. **インタラクティブな機能**: `onClick`、`onChange`などのイベントハンドラ
2. **React Hooks**: `useState`、`useEffect`などのフック
3. **ブラウザAPI**: `window`、`document`などのブラウザAPI
4. **状態管理**: クライアント側の状態管理

## メリット・デメリット

### ✅ メリット
- **パフォーマンス**: バンドルサイズが削減され、初期読み込みが高速
- **SEO**: サーバー側でHTMLを生成するため、SEOが向上
- **セキュリティ**: 機密情報をクライアントに送信しない
- **データフェッチング**: サーバー側で直接データを取得可能
- **コスト削減**: クライアント側の処理が減る

### ❌ デメリット
- **インタラクティブ性**: インタラクティブな機能は使用不可
- **リアルタイム更新**: クライアント側のリアルタイム更新が難しい
- **学習コスト**: Server ComponentsとClient Componentsの使い分けが必要

## 使用例

### 例1: ブログ記事一覧

```tsx
// app/blog/page.tsx
import { db } from '@/lib/db';

async function getPosts() {
  return await db.post.findMany({
    orderBy: { createdAt: 'desc' },
  });
}

export default async function BlogPage() {
  const posts = await getPosts();
  
  return (
    <div>
      <h1>Blog Posts</h1>
      {posts.map((post) => (
        <article key={post.id}>
          <h2>{post.title}</h2>
          <p>{post.excerpt}</p>
          <time>{post.createdAt.toLocaleDateString()}</time>
        </article>
      ))}
    </div>
  );
}
```

### 例2: ユーザープロフィール

```tsx
// app/profile/[id]/page.tsx
async function getUser(id: string) {
  const res = await fetch(`https://api.example.com/users/${id}`, {
    cache: 'no-store',
  });
  return res.json();
}

export default async function ProfilePage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  const user = await getUser(id);
  
  return (
    <div>
      <h1>{user.name}</h1>
      <p>{user.bio}</p>
      <img src={user.avatar} alt={user.name} />
    </div>
  );
}
```

## よくある問題と解決策

### 問題1: インタラクティブな機能が必要
**解決策**: Client Componentに分離

```tsx
// app/products/page.tsx (Server Component)
import ProductList from '@/components/ProductList';

export default async function ProductsPage() {
  const products = await getProducts();
  
  return <ProductList products={products} />;
}

// components/ProductList.tsx (Client Component)
'use client';

export default function ProductList({ products }) {
  const [selected, setSelected] = useState(null);
  
  return (
    <div>
      {products.map((product) => (
        <button
          key={product.id}
          onClick={() => setSelected(product)}
        >
          {product.name}
        </button>
      ))}
    </div>
  );
}
```

### 問題2: 環境変数がundefined
**解決策**: 環境変数名に`NEXT_PUBLIC_`プレフィックスを付けない（Server Componentでは不要）

```tsx
// ✅ 良い例（Server Component）
const apiKey = process.env.API_KEY; // NEXT_PUBLIC_は不要

// ❌ ダメな例
const apiKey = process.env.NEXT_PUBLIC_API_KEY; // クライアントに公開される
```

## ベストプラクティス

1. **デフォルトでServer Component**: 特別な理由がない限りServer Componentを使用
2. **データフェッチング**: Server Componentでデータを取得
3. **Client Componentを最小化**: 必要な部分だけClient Componentにする
4. **並列データフェッチング**: `Promise.all`で並列にデータを取得
5. **キャッシュ戦略**: 適切なキャッシュ設定を使用

## 関連ノート
- [[Next.jsのApp Router]]
- [[Next.jsのClient Components]]
- [[Next.jsのデータフェッチング]]

---
tags: [nextjs, server-components, app-router, technical/programming]
created: 2025-11-13

