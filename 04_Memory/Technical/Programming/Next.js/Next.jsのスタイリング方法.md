# Next.jsのスタイリング方法

**関連MOC**: [[_Next.js-MOC]] | [[_Tech-MOC]]

## 概要
Next.jsでは、複数のスタイリング方法をサポートしています。CSS Modules、Tailwind CSS、Styled Components、グローバルCSSなどが使用可能です。

## 詳細
Next.jsは、様々なスタイリング手法をサポートしており、プロジェクトの要件に応じて選択できます。`create-next-app`でTailwind CSSオプションを選択すると、自動的に設定が完了します。

## 基本的な使い方

### 1. グローバルCSS

```css
/* app/globals.css */
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
}
```

```tsx
// app/layout.tsx
import './globals.css';

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html>
      <body>{children}</body>
    </html>
  );
}
```

### 2. CSS Modules

```css
/* app/components/Button.module.css */
.button {
  padding: 10px 20px;
  background-color: blue;
  color: white;
  border: none;
  border-radius: 4px;
}
```

```tsx
// app/components/Button.tsx
import styles from './Button.module.css';

export default function Button() {
  return <button className={styles.button}>Click me</button>;
}
```

### 3. Tailwind CSS

```tsx
// app/components/Button.tsx
export default function Button() {
  return (
    <button className="px-4 py-2 bg-blue-500 text-white rounded">
      Click me
    </button>
  );
}
```

## 高度な使い方

### 1. Styled Components

```bash
npm install styled-components
npm install --save-dev @types/styled-components
```

```typescript
// lib/styled-components-registry.tsx
'use client';

import React, { useState } from 'react';
import { useServerInsertedHTML } from 'next/navigation';
import { ServerStyleSheet, StyleSheetManager } from 'styled-components';

export default function StyledComponentsRegistry({
  children,
}: {
  children: React.ReactNode;
}) {
  const [styledComponentsStyleSheet] = useState(() => new ServerStyleSheet());

  useServerInsertedHTML(() => {
    const styles = styledComponentsStyleSheet.getStyleElement();
    styledComponentsStyleSheet.instance.clearTag();
    return <>{styles}</>;
  });

  if (typeof window !== 'undefined') return <>{children}</>;

  return (
    <StyleSheetManager sheet={styledComponentsStyleSheet.instance}>
      {children}
    </StyleSheetManager>
  );
}
```

```tsx
// app/components/Button.tsx
import styled from 'styled-components';

const StyledButton = styled.button`
  padding: 10px 20px;
  background-color: blue;
  color: white;
  border: none;
  border-radius: 4px;
`;

export default function Button() {
  return <StyledButton>Click me</StyledButton>;
}
```

### 2. CSS-in-JS（Emotion）

```bash
npm install @emotion/react @emotion/styled
```

```tsx
// app/components/Button.tsx
'use client';

import { css } from '@emotion/react';

const buttonStyle = css`
  padding: 10px 20px;
  background-color: blue;
  color: white;
`;

export default function Button() {
  return <button css={buttonStyle}>Click me</button>;
}
```

## スタイリング方法の比較

| 方法 | 特徴 | 適用場面 |
|------|------|----------|
| **グローバルCSS** | シンプル、全体的なスタイル | 基本的なスタイリング |
| **CSS Modules** | スコープが限定される | コンポーネント単位のスタイル |
| **Tailwind CSS** | ユーティリティファースト | 迅速な開発、一貫性 |
| **Styled Components** | CSS-in-JS、動的スタイル | 動的なスタイリング |
| **Emotion** | CSS-in-JS、高性能 | 複雑なスタイリング |

## メリット・デメリット

### ✅ Tailwind CSSのメリット
- **迅速な開発**: ユーティリティクラスで迅速にスタイリング
- **一貫性**: デザインシステムの一貫性
- **バンドルサイズ**: 使用したクラスのみが含まれる

### ❌ Tailwind CSSのデメリット
- **学習コスト**: クラス名を覚える必要がある
- **可読性**: HTMLが長くなる場合がある

## 使用例

### 例1: Tailwind CSSでのレスポンシブデザイン

```tsx
// app/components/Card.tsx
export default function Card() {
  return (
    <div className="w-full md:w-1/2 lg:w-1/3 p-4">
      <div className="bg-white rounded-lg shadow-md p-6">
        <h2 className="text-xl font-bold mb-4">Card Title</h2>
        <p>Card content</p>
      </div>
    </div>
  );
}
```

### 例2: CSS Modulesでのコンポーネントスタイル

```css
/* app/components/Card.module.css */
.card {
  background: white;
  border-radius: 8px;
  padding: 24px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 16px;
}
```

```tsx
// app/components/Card.tsx
import styles from './Card.module.css';

export default function Card() {
  return (
    <div className={styles.card}>
      <h2 className={styles.title}>Card Title</h2>
      <p>Card content</p>
    </div>
  );
}
```

## よくある問題と解決策

### 問題1: Tailwind CSSのクラスが適用されない
**解決策**: `tailwind.config.js`を確認、クラス名を確認

```javascript
// tailwind.config.js
module.exports = {
  content: [
    './app/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
  ],
};
```

### 問題2: CSS Modulesのクラス名が長い
**解決策**: これは正常な動作（スコープを保つため）

## ベストプラクティス

1. **一貫性**: プロジェクト全体で同じスタイリング方法を使用
2. **Tailwind CSS**: 新規プロジェクトではTailwind CSSを推奨
3. **CSS Modules**: コンポーネント単位のスタイルにはCSS Modules
4. **パフォーマンス**: 不要なスタイルを削除

## 関連ノート
- [[Next.jsプロジェクトの作成方法]]
- [[Next.jsの設定ファイル]]

---
tags: [nextjs, styling, tailwind-css, css-modules, technical/programming]
created: 2025-11-13

