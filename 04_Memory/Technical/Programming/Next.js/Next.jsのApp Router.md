# Next.jsのApp Router

**関連MOC**: [[_Next.js-MOC]] | [[_Tech-MOC]]

## 概要
App RouterはNext.js v13以降で導入された新しいルーティングシステムで、Server Components、並列ルーティング、ストリーミングなどの最新機能を提供します。

## 詳細
App Routerは`app/`ディレクトリを使用し、ファイルシステムベースのルーティングを提供します。Server ComponentsとClient Componentsを明確に分離し、パフォーマンスと開発体験を向上させます。

## 基本的な使い方

### 1. ページの作成

```tsx
// app/page.tsx（ホームページ）
export default function Home() {
  return <div>Home Page</div>;
}
```

```tsx
// app/about/page.tsx（/about ページ）
export default function About() {
  return <div>About Page</div>;
}
```

### 2. レイアウトの作成

```tsx
// app/layout.tsx（ルートレイアウト）
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="ja">
      <body>{children}</body>
    </html>
  );
}
```

```tsx
// app/blog/layout.tsx（ブログ専用レイアウト）
export default function BlogLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div>
      <nav>Blog Navigation</nav>
      {children}
    </div>
  );
}
```

### 3. Server Components（デフォルト）

```tsx
// app/products/page.tsx
// Server Component（デフォルト）

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

### 4. Client Components

```tsx
// app/components/Counter.tsx
'use client';

import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);
  
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

## 高度な使い方

### 1. 動的ルーティング

```tsx
// app/blog/[slug]/page.tsx
export default async function BlogPost({
  params,
}: {
  params: { slug: string };
}) {
  const post = await getPost(params.slug);
  
  return (
    <article>
      <h1>{post.title}</h1>
      <div>{post.content}</div>
    </article>
  );
}
```

### 2. ルートグループ

```
app/
├── (marketing)/        # URLに影響しないグループ
│   ├── about/
│   └── contact/
└── (shop)/             # 別のグループ
    ├── products/
    └── cart/
```

### 3. 並列ルート

```tsx
// app/@analytics/page.tsx
export default function Analytics() {
  return <div>Analytics</div>;
}

// app/@team/page.tsx
export default function Team() {
  return <div>Team</div>;
}

// app/layout.tsx
export default function Layout({
  children,
  analytics,
  team,
}: {
  children: React.ReactNode;
  analytics: React.ReactNode;
  team: React.ReactNode;
}) {
  return (
    <>
      {children}
      {analytics}
      {team}
    </>
  );
}
```

### 4. インターセプティングルート

```
app/
├── photo/
│   └── [id]/
│       └── page.tsx        # /photo/123
└── @modal/
    └── (.)photo/
        └── [id]/
            └── page.tsx    # /photo/123 をモーダルで表示
```

## Server Components vs Client Components

### Server Components（デフォルト）

**特徴**:
- サーバー側でレンダリング
- バンドルサイズに含まれない
- データベースやAPIに直接アクセス可能
- インタラクティブな機能は使用不可

**使用例**:
```tsx
// app/products/page.tsx
import { db } from '@/lib/db';

export default async function ProductsPage() {
  const products = await db.products.findMany();
  
  return (
    <div>
      {products.map((product) => (
        <div key={product.id}>{product.name}</div>
      ))}
    </div>
  );
}
```

### Client Components

**特徴**:
- クライアント側でレンダリング
- インタラクティブな機能が使用可能
- ブラウザAPIにアクセス可能
- `useState`、`useEffect`などのフックが使用可能

**使用例**:
```tsx
// app/components/InteractiveButton.tsx
'use client';

import { useState } from 'react';

export default function InteractiveButton() {
  const [clicked, setClicked] = useState(false);
  
  return (
    <button onClick={() => setClicked(!clicked)}>
      {clicked ? 'Clicked!' : 'Click me'}
    </button>
  );
}
```

## メリット・デメリット

### ✅ メリット
- **パフォーマンス**: Server Componentsによりバンドルサイズが削減
- **SEO**: サーバー側レンダリングによりSEOが向上
- **開発体験**: データフェッチングが簡単
- **柔軟性**: ネストされたレイアウト、並列ルートなど
- **ストリーミング**: 段階的なレンダリングが可能

### ❌ デメリット
- **学習コスト**: Server ComponentsとClient Componentsの理解が必要
- **互換性**: 一部のライブラリが未対応
- **複雑性**: ルーティングが複雑になる場合がある

## 使用例

### 例1: データフェッチング

```tsx
// app/posts/page.tsx
async function getPosts() {
  const res = await fetch('https://api.example.com/posts', {
    cache: 'no-store', // 常に最新データを取得
  });
  return res.json();
}

export default async function PostsPage() {
  const posts = await getPosts();
  
  return (
    <div>
      {posts.map((post) => (
        <article key={post.id}>
          <h2>{post.title}</h2>
          <p>{post.content}</p>
        </article>
      ))}
    </div>
  );
}
```

### 例2: メタデータの設定

```tsx
// app/about/page.tsx
export const metadata = {
  title: 'About Us',
  description: 'Learn more about our company',
};

export default function AboutPage() {
  return <div>About Page</div>;
}
```

## よくある問題と解決策

### 問題1: `'use client'`を忘れる
**解決策**: インタラクティブな機能を使用する場合は必ず`'use client'`を追加

```tsx
'use client';

import { useState } from 'react';
```

### 問題2: Server ComponentでブラウザAPIを使用
**解決策**: Client Componentに分離する

```tsx
// ❌ ダメな例
export default function Page() {
  const [mounted, setMounted] = useState(false);
  // ...
}

// ✅ 良い例
'use client';

export default function Page() {
  const [mounted, setMounted] = useState(false);
  // ...
}
```

### 問題3: 動的ルートのパラメータ取得
**解決策**: `params`を`async`で受け取る

```tsx
// app/blog/[slug]/page.tsx
export default async function BlogPost({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  // ...
}
```

## ベストプラクティス

1. **Server Componentsを優先**: デフォルトでServer Componentsを使用
2. **Client Componentsを最小化**: 必要な部分だけClient Componentsにする
3. **データフェッチング**: Server Componentsでデータを取得
4. **メタデータ**: 各ページに適切なメタデータを設定
5. **エラーハンドリング**: `error.tsx`でエラーを処理

## 関連ノート
- [[Next.jsとは何か]]
- [[Next.jsのServer Components]]
- [[Next.jsのClient Components]]
- [[Next.jsのルーティング]]

---
tags: [nextjs, app-router, server-components, technical/programming]
created: 2025-11-13

