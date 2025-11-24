# Next.jsのページ作成

**関連MOC**: [[_Next.js-MOC]] | [[_Tech-MOC]]

## 概要
Next.jsでページを作成する方法と、ページコンポーネントの基本的な構造を説明します。

## 詳細
Next.js App Routerでは、`app/`ディレクトリ内に`page.tsx`ファイルを作成することで、そのディレクトリがルートとして機能します。

## 基本的な使い方

### 1. シンプルなページ

```tsx
// app/about/page.tsx
export default function AboutPage() {
  return (
    <div>
      <h1>About Us</h1>
      <p>This is the about page.</p>
    </div>
  );
}
```

このファイルは`/about`ルートとして機能します。

### 2. Server Componentページ（デフォルト）

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
      <h1>Products</h1>
      <ul>
        {products.map((product) => (
          <li key={product.id}>{product.name}</li>
        ))}
      </ul>
    </div>
  );
}
```

### 3. メタデータの設定

```tsx
// app/about/page.tsx
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'About Us',
  description: 'Learn more about our company',
  openGraph: {
    title: 'About Us',
    description: 'Learn more about our company',
    type: 'website',
  },
};

export default function AboutPage() {
  return (
    <div>
      <h1>About Us</h1>
    </div>
  );
}
```

## 高度な使い方

### 1. 動的ルートのページ

```tsx
// app/blog/[slug]/page.tsx
async function getPost(slug: string) {
  const res = await fetch(`https://api.example.com/posts/${slug}`);
  return res.json();
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string }>;
}): Promise<Metadata> {
  const { slug } = await params;
  const post = await getPost(slug);
  
  return {
    title: post.title,
    description: post.excerpt,
  };
}

export default async function BlogPostPage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const post = await getPost(slug);
  
  return (
    <article>
      <h1>{post.title}</h1>
      <div dangerouslySetInnerHTML={{ __html: post.content }} />
    </article>
  );
}
```

### 2. 検索パラメータの取得

```tsx
// app/search/page.tsx
export default function SearchPage({
  searchParams,
}: {
  searchParams: Promise<{ q?: string }>;
}) {
  const { q } = await searchParams;
  
  return (
    <div>
      <h1>Search Results</h1>
      {q && <p>Searching for: {q}</p>}
    </div>
  );
}
```

### 3. ストリーミングとSuspense

```tsx
// app/dashboard/page.tsx
import { Suspense } from 'react';

async function SlowComponent() {
  await new Promise(resolve => setTimeout(resolve, 2000));
  return <div>Slow Content</div>;
}

function Loading() {
  return <div>Loading...</div>;
}

export default function DashboardPage() {
  return (
    <div>
      <h1>Dashboard</h1>
      <Suspense fallback={<Loading />}>
        <SlowComponent />
      </Suspense>
    </div>
  );
}
```

### 4. エラーハンドリング

```tsx
// app/products/[id]/page.tsx
async function getProduct(id: string) {
  const res = await fetch(`https://api.example.com/products/${id}`);
  
  if (!res.ok) {
    throw new Error('Failed to fetch product');
  }
  
  return res.json();
}

export default async function ProductPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  const product = await getProduct(id);
  
  return (
    <div>
      <h1>{product.name}</h1>
      <p>{product.description}</p>
    </div>
  );
}
```

## ページの種類

### 1. 静的ページ

ビルド時に生成されるページ。

```tsx
// app/about/page.tsx
export default function AboutPage() {
  return <div>About</div>;
}
```

### 2. 動的ページ

リクエスト時に生成されるページ。

```tsx
// app/blog/[slug]/page.tsx
export default async function BlogPost({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  // データを取得
  return <div>Post: {slug}</div>;
}
```

### 3. 静的生成（SSG）

`generateStaticParams`を使用して静的ページを生成。

```tsx
// app/blog/[slug]/page.tsx
export async function generateStaticParams() {
  const posts = await getPosts();
  
  return posts.map((post) => ({
    slug: post.slug,
  }));
}

export default async function BlogPost({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const post = await getPost(slug);
  
  return <article>{post.content}</article>;
}
```

## メタデータの設定

### 基本的なメタデータ

```tsx
// app/page.tsx
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Home Page',
  description: 'Welcome to our website',
};
```

### 動的メタデータ

```tsx
// app/blog/[slug]/page.tsx
export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string }>;
}): Promise<Metadata> {
  const { slug } = await params;
  const post = await getPost(slug);
  
  return {
    title: post.title,
    description: post.excerpt,
  };
}
```

### Open Graphメタデータ

```tsx
export const metadata: Metadata = {
  openGraph: {
    title: 'My Page',
    description: 'Page description',
    url: 'https://example.com',
    siteName: 'My Site',
    images: [
      {
        url: 'https://example.com/og-image.jpg',
        width: 1200,
        height: 630,
      },
    ],
    locale: 'ja_JP',
    type: 'website',
  },
};
```

## メリット・デメリット

### ✅ メリット
- **自動ルーティング**: ファイル構造がそのままURL構造
- **コード分割**: ページ単位で自動的にコード分割
- **SEO対応**: メタデータを簡単に設定可能
- **パフォーマンス**: Server Componentsにより高速

### ❌ デメリット
- **ファイル構造**: ファイル構造に依存するため、柔軟性がやや低い
- **学習コスト**: App Routerの概念理解が必要

## 使用例

### 例1: ブログ記事ページ

```tsx
// app/blog/[slug]/page.tsx
import { notFound } from 'next/navigation';

async function getPost(slug: string) {
  const res = await fetch(`https://api.example.com/posts/${slug}`);
  
  if (!res.ok) {
    return null;
  }
  
  return res.json();
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const post = await getPost(slug);
  
  if (!post) {
    return {
      title: 'Post Not Found',
    };
  }
  
  return {
    title: post.title,
    description: post.excerpt,
  };
}

export default async function BlogPostPage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const post = await getPost(slug);
  
  if (!post) {
    notFound();
  }
  
  return (
    <article>
      <h1>{post.title}</h1>
      <time>{post.publishedAt}</time>
      <div>{post.content}</div>
    </article>
  );
}
```

### 例2: 商品一覧ページ

```tsx
// app/products/page.tsx
async function getProducts() {
  const res = await fetch('https://api.example.com/products', {
    next: { revalidate: 3600 }, // 1時間キャッシュ
  });
  return res.json();
}

export const metadata: Metadata = {
  title: 'Products',
  description: 'Browse our products',
};

export default async function ProductsPage() {
  const products = await getProducts();
  
  return (
    <div>
      <h1>Products</h1>
      <div className="grid">
        {products.map((product) => (
          <div key={product.id}>
            <h2>{product.name}</h2>
            <p>{product.price}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
```

## よくある問題と解決策

### 問題1: ページが表示されない
**解決策**: `page.tsx`ファイルが正しい場所にあるか確認

```
app/
└── about/
    └── page.tsx  # これが /about になる
```

### 問題2: メタデータが反映されない
**解決策**: `metadata`エクスポートを確認

```tsx
export const metadata: Metadata = {
  title: 'Page Title',
};
```

### 問題3: 動的ルートのパラメータが取得できない
**解決策**: `params`を`async`で受け取る（Next.js 15以降）

```tsx
export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  // ...
}
```

## ベストプラクティス

1. **Server Componentを優先**: デフォルトでServer Componentを使用
2. **メタデータを設定**: 各ページに適切なメタデータを設定
3. **エラーハンドリング**: `not-found.tsx`と`error.tsx`を使用
4. **型安全性**: TypeScriptでパラメータの型を定義
5. **パフォーマンス**: 適切なキャッシュ戦略を使用

## 関連ノート
- [[Next.jsのルーティング]]
- [[Next.jsのレイアウト]]
- [[Next.jsのServer Components]]

---
tags: [nextjs, pages, app-router, technical/programming]
created: 2025-11-13

