# Next.jsのルーティング

**関連MOC**: [[_Next.js-MOC]] | [[_Tech-MOC]]

## 概要
Next.jsのルーティングは、ファイルシステムベースで、`app/`ディレクトリ内のファイル構造がそのままURL構造になります。

## 詳細
Next.js App Routerでは、`app/`ディレクトリ内のファイル構造がルーティングを決定します。`page.tsx`がページコンポーネント、`layout.tsx`がレイアウトコンポーネントとして機能します。

## 基本的な使い方

### 1. 静的ルート

```
app/
├── page.tsx              # /
├── about/
│   └── page.tsx          # /about
└── contact/
    └── page.tsx          # /contact
```

```tsx
// app/about/page.tsx
export default function AboutPage() {
  return <div>About Page</div>;
}
```

### 2. 動的ルート

```
app/
└── blog/
    └── [slug]/
        └── page.tsx      # /blog/[slug]
```

```tsx
// app/blog/[slug]/page.tsx
export default async function BlogPost({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  return <div>Blog Post: {slug}</div>;
}
```

### 3. キャッチオールルート

```
app/
└── docs/
    └── [...slug]/
        └── page.tsx      # /docs/[...slug]
```

```tsx
// app/docs/[...slug]/page.tsx
export default async function DocsPage({
  params,
}: {
  params: Promise<{ slug: string[] }>;
}) {
  const { slug } = await params;
  return <div>Docs: {slug.join('/')}</div>;
}
```

## 高度な使い方

### 1. ルートグループ

ルートグループは`()`で囲み、URLには影響しません。

```
app/
├── (marketing)/
│   ├── about/
│   └── contact/
└── (shop)/
    ├── products/
    └── cart/
```

URL:
- `/about` - (marketing)グループ
- `/products` - (shop)グループ

### 2. 並列ルート

`@`プレフィックスを使用して、同じレイアウト内で複数のページを並列に表示できます。

```
app/
├── @analytics/
│   └── page.tsx
├── @team/
│   └── page.tsx
├── layout.tsx
└── page.tsx
```

```tsx
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

### 3. インターセプティングルート

同じURLを異なるビューで表示できます。

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

プレフィックス:
- `(.)` - 同じレベル
- `(..)` - 1レベル上
- `(..)(..)` - 2レベル上
- `(...)` - ルートレベル

### 4. 条件付きルート

```tsx
// app/dashboard/page.tsx
import { redirect } from 'next/navigation';
import { getSession } from '@/lib/auth';

export default async function DashboardPage() {
  const session = await getSession();
  
  if (!session) {
    redirect('/login');
  }
  
  return <div>Dashboard</div>;
}
```

## ルーティングの種類

### 静的ルート

ビルド時に生成されるルート。

```tsx
// app/about/page.tsx
export default function AboutPage() {
  return <div>About</div>;
}
```

### 動的ルート

リクエスト時に生成されるルート。

```tsx
// app/blog/[slug]/page.tsx
export default async function BlogPost({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  // データを取得
  const post = await getPost(slug);
  return <div>{post.title}</div>;
}
```

### 動的セグメントの種類

1. **単一セグメント**: `[id]`
2. **キャッチオール**: `[...slug]` - すべてのパスをキャッチ
3. **オプショナルキャッチオール**: `[[...slug]]` - 0個以上のセグメント

## ナビゲーション

### Linkコンポーネント

```tsx
// app/components/Navigation.tsx
import Link from 'next/link';

export default function Navigation() {
  return (
    <nav>
      <Link href="/">Home</Link>
      <Link href="/about">About</Link>
      <Link href="/blog">Blog</Link>
    </nav>
  );
}
```

### useRouterフック（Client Component）

```tsx
// app/components/ClientNavigation.tsx
'use client';

import { useRouter } from 'next/navigation';

export default function ClientNavigation() {
  const router = useRouter();
  
  const handleClick = () => {
    router.push('/about');
  };
  
  return <button onClick={handleClick}>Go to About</button>;
}
```

### プログラム的なナビゲーション

```tsx
// app/components/RedirectButton.tsx
'use client';

import { useRouter } from 'next/navigation';

export default function RedirectButton() {
  const router = useRouter();
  
  return (
    <button onClick={() => router.push('/dashboard')}>
      Go to Dashboard
    </button>
  );
}
```

## メリット・デメリット

### ✅ メリット
- **直感的**: ファイル構造がそのままURL構造
- **自動コード分割**: ページ単位で自動的にコード分割
- **型安全**: TypeScriptでパラメータの型を定義可能
- **柔軟性**: ルートグループ、並列ルートなど高度な機能

### ❌ デメリット
- **学習コスト**: ルートグループ、並列ルートなどの概念理解が必要
- **複雑性**: 大規模プロジェクトでは構造が複雑になる場合がある

## 使用例

### 例1: ブログサイト

```
app/
├── page.tsx                    # /
├── blog/
│   ├── page.tsx                # /blog
│   └── [slug]/
│       └── page.tsx            # /blog/[slug]
└── about/
    └── page.tsx                # /about
```

### 例2: ダッシュボード

```
app/
├── (auth)/
│   ├── login/
│   └── register/
├── (dashboard)/
│   ├── dashboard/
│   ├── settings/
│   └── profile/
└── page.tsx
```

### 例3: 多言語サイト

```
app/
├── [lang]/
│   ├── page.tsx                # /en, /ja
│   ├── about/
│   └── contact/
└── page.tsx                     # /
```

## よくある問題と解決策

### 問題1: 動的ルートのパラメータが取得できない
**解決策**: `params`を`async`で受け取る（Next.js 15以降）

```tsx
// ✅ 良い例（Next.js 15以降）
export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  // ...
}

// ✅ 良い例（Next.js 14以前）
export default function Page({
  params,
}: {
  params: { id: string };
}) {
  const { id } = params;
  // ...
}
```

### 問題2: ルートグループがURLに表示される
**解決策**: ルートグループは`()`で囲むとURLに影響しない

```
app/
├── (marketing)/        # URLに表示されない
│   └── about/
└── about/              # これは /about になる
```

### 問題3: 404ページが表示されない
**解決策**: `not-found.tsx`を作成

```tsx
// app/not-found.tsx
export default function NotFound() {
  return (
    <div>
      <h1>404 - Page Not Found</h1>
    </div>
  );
}
```

## ベストプラクティス

1. **App Routerを使用**: 新規プロジェクトはApp Routerを推奨
2. **ルートグループを活用**: 関連するルートをグループ化
3. **動的ルート**: 適切に動的ルートを使用
4. **型安全性**: TypeScriptでパラメータの型を定義
5. **404ページ**: カスタム404ページを作成

## 関連ノート
- [[Next.jsのApp Router]]
- [[Next.jsのページ作成]]
- [[Next.jsのレイアウト]]

---
tags: [nextjs, routing, app-router, technical/programming]
created: 2025-11-13

