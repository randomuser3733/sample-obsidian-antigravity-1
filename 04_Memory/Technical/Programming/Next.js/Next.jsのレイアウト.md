# Next.jsのレイアウト

**関連MOC**: [[_Next.js-MOC]] | [[_Tech-MOC]]

## 概要
レイアウトは、複数のページ間で共有されるUIコンポーネントです。`layout.tsx`ファイルで定義し、ネストされたレイアウトを作成できます。

## 詳細
レイアウトは、ページが変更されても保持されるUI要素（ヘッダー、フッター、サイドバーなど）を定義します。App Routerでは、`layout.tsx`ファイルがレイアウトコンポーネントとして機能します。

## 基本的な使い方

### 1. ルートレイアウト（必須）

```tsx
// app/layout.tsx
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

### 2. ネストされたレイアウト

```tsx
// app/blog/layout.tsx
export default function BlogLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div>
      <nav>Blog Navigation</nav>
      <main>{children}</main>
      <aside>Blog Sidebar</aside>
    </div>
  );
}
```

このレイアウトは`/blog`配下のすべてのページに適用されます。

### 3. メタデータの設定

```tsx
// app/layout.tsx
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: {
    default: 'My Website',
    template: '%s | My Website',
  },
  description: 'Welcome to my website',
};

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

## 高度な使い方

### 1. 条件付きレイアウト

```tsx
// app/dashboard/layout.tsx
import { redirect } from 'next/navigation';
import { getSession } from '@/lib/auth';

export default async function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const session = await getSession();
  
  if (!session) {
    redirect('/login');
  }
  
  return (
    <div>
      <header>Dashboard Header</header>
      <main>{children}</main>
    </div>
  );
}
```

### 2. レイアウト間のデータ共有

```tsx
// app/layout.tsx
import { getSiteConfig } from '@/lib/config';

export default async function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const config = await getSiteConfig();
  
  return (
    <html lang={config.locale}>
      <body>
        <header>
          <h1>{config.siteName}</h1>
        </header>
        {children}
      </body>
    </html>
  );
}
```

### 3. テンプレート

`template.tsx`は`layout.tsx`と似ていますが、ナビゲーション時に再マウントされます。

```tsx
// app/template.tsx
export default function Template({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="fade-in">
      {children}
    </div>
  );
}
```

## レイアウトの種類

### 1. ルートレイアウト

`app/layout.tsx`は必須で、すべてのページに適用されます。

```tsx
// app/layout.tsx
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

### 2. セクション別レイアウト

特定のセクションにのみ適用されるレイアウト。

```tsx
// app/blog/layout.tsx
export default function BlogLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="blog-container">
      <aside>Blog Sidebar</aside>
      <main>{children}</main>
    </div>
  );
}
```

### 3. ルートグループのレイアウト

ルートグループごとに異なるレイアウトを適用。

```
app/
├── (marketing)/
│   ├── layout.tsx         # マーケティング用レイアウト
│   ├── about/
│   └── contact/
└── (shop)/
    ├── layout.tsx         # ショップ用レイアウト
    ├── products/
    └── cart/
```

## メリット・デメリット

### ✅ メリット
- **コードの再利用**: 共通UIを1箇所で管理
- **パフォーマンス**: レイアウトは再レンダリングされない
- **ネスト**: 複数のレイアウトをネスト可能
- **型安全**: TypeScriptで型定義可能

### ❌ デメリット
- **複雑性**: ネストが深くなると理解が難しくなる場合がある
- **制約**: レイアウトの構造に制約がある

## 使用例

### 例1: 基本的なレイアウト構造

```tsx
// app/layout.tsx
import Header from '@/components/Header';
import Footer from '@/components/Footer';

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="ja">
      <body>
        <Header />
        <main>{children}</main>
        <Footer />
      </body>
    </html>
  );
}
```

### 例2: ダッシュボードレイアウト

```tsx
// app/dashboard/layout.tsx
import Sidebar from '@/components/dashboard/Sidebar';
import Header from '@/components/dashboard/Header';

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="dashboard-layout">
      <Sidebar />
      <div className="dashboard-content">
        <Header />
        <main>{children}</main>
      </div>
    </div>
  );
}
```

### 例3: 認証が必要なレイアウト

```tsx
// app/dashboard/layout.tsx
import { redirect } from 'next/navigation';
import { getSession } from '@/lib/auth';

export default async function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const session = await getSession();
  
  if (!session) {
    redirect('/login');
  }
  
  return (
    <div>
      <header>Dashboard</header>
      {children}
    </div>
  );
}
```

## よくある問題と解決策

### 問題1: レイアウトが適用されない
**解決策**: `layout.tsx`の構造を確認

```tsx
// ✅ 良い例
export default function Layout({
  children,
}: {
  children: React.ReactNode;
}) {
  return <div>{children}</div>;
}
```

### 問題2: ネストされたレイアウトが機能しない
**解決策**: ディレクトリ構造を確認

```
app/
├── layout.tsx           # ルートレイアウト
└── blog/
    ├── layout.tsx       # ブログレイアウト（ネスト）
    └── page.tsx
```

### 問題3: レイアウトで状態管理ができない
**解決策**: Client Componentに分離

```tsx
// app/components/LayoutClient.tsx
'use client';

import { useState } from 'react';

export default function LayoutClient({
  children,
}: {
  children: React.ReactNode;
}) {
  const [theme, setTheme] = useState('light');
  
  return (
    <div data-theme={theme}>
      {children}
    </div>
  );
}

// app/layout.tsx
import LayoutClient from '@/components/LayoutClient';

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html>
      <body>
        <LayoutClient>{children}</LayoutClient>
      </body>
    </html>
  );
}
```

## ベストプラクティス

1. **ルートレイアウト**: `app/layout.tsx`は必須
2. **ネスト**: セクションごとにレイアウトを分離
3. **メタデータ**: ルートレイアウトでグローバルメタデータを設定
4. **パフォーマンス**: レイアウトは再レンダリングされないことを活用
5. **型安全**: TypeScriptで`children`の型を定義

## 関連ノート
- [[Next.jsのルーティング]]
- [[Next.jsのページ作成]]
- [[Next.jsのApp Router]]

---
tags: [nextjs, layout, app-router, technical/programming]
created: 2025-11-13

