# Next.jsとは何か

**関連MOC**: [[_Next.js-MOC]] | [[_Tech-MOC]]

## 概要
Next.jsは、ReactベースのフルスタックWebアプリケーションフレームワークで、サーバーサイドレンダリング（SSR）、静的サイト生成（SSG）、API Routesなどの機能を提供します。

## 詳細
Next.jsはVercelが開発・メンテナンスしているReactフレームワークで、以下の特徴があります：

- **Reactベース**: Reactのコンポーネントベースの開発をサポート
- **フルスタック**: フロントエンドとバックエンドの両方を1つのプロジェクトで開発可能
- **サーバーサイドレンダリング（SSR）**: サーバー側でHTMLを生成し、SEOとパフォーマンスを向上
- **静的サイト生成（SSG）**: ビルド時にHTMLを生成し、高速な配信を実現
- **API Routes**: バックエンドAPIをNext.jsプロジェクト内で作成可能
- **自動コード分割**: ページ単位で自動的にコード分割し、パフォーマンスを最適化
- **ファイルベースルーティング**: ファイルシステムをルーティングとして使用

## Next.jsのバージョン

### App Router（v13以降、推奨）
- 最新のルーティングシステム
- Server ComponentsとClient Componentsの分離
- より柔軟なデータフェッチング
- レイアウトとテンプレートのサポート

### Pages Router（v12以前、レガシー）
- 従来のルーティングシステム
- `pages/`ディレクトリベース
- 安定性が高い
- 既存プロジェクトで広く使用

## 基本的な使い方

Next.jsプロジェクトの作成：

```bash
# 最新版でプロジェクト作成
npx create-next-app@latest my-app

# TypeScriptを使用する場合
npx create-next-app@latest my-app --typescript

# Tailwind CSSを含める場合
npx create-next-app@latest my-app --tailwind
```

## メリット・デメリット

### ✅ メリット
- **SEO対応**: SSRにより検索エンジン最適化が容易
- **パフォーマンス**: 自動コード分割と最適化により高速
- **開発体験**: ホットリロード、エラーメッセージが分かりやすい
- **フルスタック**: フロントエンドとバックエンドを1プロジェクトで管理
- **デプロイが簡単**: Vercelへのワンクリックデプロイ
- **豊富な機能**: 画像最適化、フォント最適化など標準搭載

### ❌ デメリット
- **学習コスト**: Reactの知識が必要、App Routerの概念理解が必要
- **柔軟性**: フレームワークの制約に従う必要がある
- **ビルド時間**: 大規模プロジェクトではビルド時間が長くなる可能性
- **サーバーコスト**: SSRを使用する場合、サーバーリソースが必要

## 使用例

### 基本的なページ作成

```tsx
// app/page.tsx (App Router)
export default function Home() {
  return (
    <div>
      <h1>Hello Next.js</h1>
    </div>
  );
}
```

### 動的ルーティング

```tsx
// app/blog/[slug]/page.tsx
export default function BlogPost({ params }: { params: { slug: string } }) {
  return <div>Blog Post: {params.slug}</div>;
}
```

## よくある問題と解決策

### 問題1: クライアントコンポーネントでエラーが出る
**解決策**: `'use client'`ディレクティブを追加

```tsx
'use client';

export default function ClientComponent() {
  return <div>Client Component</div>;
}
```

### 問題2: 画像が表示されない
**解決策**: Next.jsの`Image`コンポーネントを使用

```tsx
import Image from 'next/image';

<Image src="/image.jpg" alt="Description" width={500} height={300} />
```

## ベストプラクティス

1. **App Routerを使用**: 新規プロジェクトはApp Routerを推奨
2. **Server Componentsを優先**: デフォルトでServer Componentsを使用
3. **動的インポート**: 大きなコンポーネントは動的インポートで遅延読み込み
4. **画像最適化**: Next.jsの`Image`コンポーネントを必ず使用
5. **メタデータ**: 各ページに適切なメタデータを設定

## 関連技術との比較

| 技術 | 特徴 | 適用場面 |
|------|------|----------|
| **Next.js** | SSR/SSG、フルスタック | 本格的なWebアプリケーション |
| **React** | クライアントサイドのみ | SPA、動的なUIが必要な場合 |
| **Remix** | フルスタック、データローディング重視 | データ中心のアプリケーション |
| **Gatsby** | 静的サイト生成特化 | ブログ、ポートフォリオサイト |

## 関連ノート
- [[Next.jsプロジェクトの作成方法]]
- [[Next.jsのApp Router]]
- [[Next.jsのプロジェクト構造]]
- [[Next.jsのルーティング]]

---
tags: [nextjs, react, framework, technical/programming]
created: 2025-11-13

