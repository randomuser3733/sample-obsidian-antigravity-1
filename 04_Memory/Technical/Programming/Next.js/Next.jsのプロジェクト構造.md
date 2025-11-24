# Next.jsのプロジェクト構造

**関連MOC**: [[_Next.js-MOC]] | [[_Tech-MOC]]

## 概要
Next.jsプロジェクトのディレクトリ構造と、各ファイル・フォルダの役割を説明します。

## 詳細
Next.jsプロジェクトは、App RouterとPages Routerの2つのルーティングシステムがあります。App Router（v13以降）が推奨されています。

## App Routerの構造

### 基本的な構造

```
my-app/
├── app/                      # App Routerのルートディレクトリ
│   ├── layout.tsx           # ルートレイアウト（全ページ共通）
│   ├── page.tsx            # ホームページ（/）
│   ├── loading.tsx         # ローディングUI
│   ├── error.tsx           # エラーハンドリングUI
│   ├── not-found.tsx       # 404ページ
│   ├── globals.css         # グローバルスタイル
│   │
│   ├── about/              # /about ルート
│   │   └── page.tsx
│   │
│   ├── blog/               # /blog ルート
│   │   ├── layout.tsx     # ブログ専用レイアウト
│   │   ├── page.tsx       # /blog ページ
│   │   └── [slug]/        # 動的ルート
│   │       └── page.tsx
│   │
│   └── api/                # API Routes
│       └── hello/
│           └── route.ts
│
├── components/              # 再利用可能なコンポーネント
│   ├── ui/
│   └── layout/
│
├── lib/                     # ユーティリティ関数
│   └── utils.ts
│
├── public/                  # 静的ファイル
│   ├── images/
│   └── favicon.ico
│
├── styles/                  # スタイルファイル（オプション）
│
├── types/                   # TypeScript型定義
│   └── index.ts
│
├── .env.local              # 環境変数（ローカル）
├── .env.example            # 環境変数の例
├── .gitignore              # Git除外設定
├── next.config.js          # Next.js設定
├── package.json            # 依存関係
├── tsconfig.json           # TypeScript設定
└── tailwind.config.js      # Tailwind設定（使用時）
```

## 主要ディレクトリの説明

### `app/`ディレクトリ

App Routerのルートディレクトリ。ファイルシステムベースのルーティングを提供します。

#### 特殊ファイル

- **`layout.tsx`**: ページの共通レイアウト
- **`page.tsx`**: ページコンポーネント（必須）
- **`loading.tsx`**: ローディング状態のUI
- **`error.tsx`**: エラー状態のUI
- **`not-found.tsx`**: 404ページ
- **`route.ts`**: API Route（GET、POSTなど）
- **`template.tsx`**: テンプレート（レイアウトと似ているが、再マウントされる）

### `components/`ディレクトリ

再利用可能なReactコンポーネントを配置します。

```
components/
├── ui/              # UIコンポーネント（Button、Inputなど）
├── layout/          # レイアウトコンポーネント（Header、Footerなど）
└── features/        # 機能別コンポーネント
```

### `lib/`ディレクトリ

ユーティリティ関数、ヘルパー関数を配置します。

```typescript
// lib/utils.ts
export function cn(...classes: string[]) {
  return classes.filter(Boolean).join(' ');
}
```

### `public/`ディレクトリ

静的ファイル（画像、アイコン、フォントなど）を配置します。

```
public/
├── images/
├── icons/
└── favicon.ico
```

アクセス方法：
```tsx
<Image src="/images/logo.png" alt="Logo" width={100} height={100} />
```

### `types/`ディレクトリ

TypeScriptの型定義を配置します。

```typescript
// types/index.ts
export interface User {
  id: string;
  name: string;
  email: string;
}
```

## Pages Routerの構造（レガシー）

```
my-app/
├── pages/                   # Pages Routerのルートディレクトリ
│   ├── _app.tsx           # カスタムAppコンポーネント
│   ├── _document.tsx      # カスタムDocumentコンポーネント
│   ├── index.tsx          # ホームページ（/）
│   ├── about.tsx          # /about ページ
│   ├── blog/
│   │   ├── index.tsx      # /blog ページ
│   │   └── [slug].tsx     # /blog/[slug] 動的ルート
│   └── api/               # API Routes
│       └── hello.ts
│
├── components/
├── lib/
├── public/
└── styles/
```

## ファイル命名規則

### App Router

- **ページ**: `page.tsx`（必須）
- **レイアウト**: `layout.tsx`
- **ローディング**: `loading.tsx`
- **エラー**: `error.tsx`
- **404**: `not-found.tsx`
- **API Route**: `route.ts`

### 動的ルート

```
app/
├── [id]/           # 動的セグメント
│   └── page.tsx
├── [...slug]/      # キャッチオール
│   └── page.tsx
└── [[...slug]]/    # オプショナルキャッチオール
    └── page.tsx
```

## メリット・デメリット

### ✅ App Routerのメリット
- **最新機能**: Server Components、並列ルーティングなど
- **柔軟なレイアウト**: ネストされたレイアウトが可能
- **データフェッチング**: より強力なデータフェッチング機能

### ❌ App Routerのデメリット
- **学習コスト**: 新しい概念（Server Componentsなど）の理解が必要
- **互換性**: 一部のライブラリが未対応の場合がある

## 使用例

### 例1: 基本的なページ構造

```
app/
├── layout.tsx
├── page.tsx              # /
├── about/
│   └── page.tsx         # /about
└── blog/
    ├── layout.tsx       # ブログ専用レイアウト
    ├── page.tsx         # /blog
    └── [slug]/
        └── page.tsx     # /blog/[slug]
```

### 例2: ルートグループ

```
app/
├── (marketing)/         # ルートグループ（URLに影響しない）
│   ├── about/
│   └── contact/
└── (shop)/              # 別のルートグループ
    ├── products/
    └── cart/
```

## よくある問題と解決策

### 問題1: ページが表示されない
**解決策**: `page.tsx`ファイルが存在するか確認

```tsx
// app/about/page.tsx が存在する必要がある
export default function About() {
  return <div>About</div>;
}
```

### 問題2: レイアウトが適用されない
**解決策**: `layout.tsx`の構造を確認

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

## ベストプラクティス

1. **App Routerを使用**: 新規プロジェクトはApp Routerを推奨
2. **コンポーネントの分離**: `components/`に再利用可能なコンポーネントを配置
3. **型定義の整理**: `types/`に型定義を集約
4. **ユーティリティの分離**: `lib/`にヘルパー関数を配置
5. **静的ファイルの管理**: `public/`に静的ファイルを配置

## 関連ノート
- [[Next.jsとは何か]]
- [[Next.jsプロジェクトの作成方法]]
- [[Next.jsのApp Router]]
- [[Next.jsのルーティング]]

---
tags: [nextjs, project-structure, app-router, technical/programming]
created: 2025-11-13

