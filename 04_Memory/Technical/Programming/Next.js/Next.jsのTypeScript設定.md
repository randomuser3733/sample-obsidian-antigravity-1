# Next.jsのTypeScript設定

**関連MOC**: [[_Next.js-MOC]] | [[_Tech-MOC]]

## 概要
Next.jsでTypeScriptを使用する場合の設定方法と、型定義のベストプラクティスを説明します。

## 詳細
Next.jsはTypeScriptを完全にサポートしており、`create-next-app`でTypeScriptオプションを選択すると、自動的に設定が完了します。

## 基本的な使い方

### 1. TypeScriptプロジェクトの作成

```bash
npx create-next-app@latest my-app --typescript
```

### 2. tsconfig.jsonの確認

```json
{
  "compilerOptions": {
    "target": "ES2017",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
```

## 高度な使い方

### 1. パスエイリアスの設定

```json
// tsconfig.json
{
  "compilerOptions": {
    "paths": {
      "@/*": ["./*"],
      "@/components/*": ["./components/*"],
      "@/lib/*": ["./lib/*"]
    }
  }
}
```

### 2. 型定義ファイルの作成

```typescript
// types/index.ts
export interface User {
  id: string;
  name: string;
  email: string;
}

export interface Post {
  id: string;
  title: string;
  content: string;
}
```

### 3. 環境変数の型定義

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

## メリット・デメリット

### ✅ メリット
- **型安全**: コンパイル時にエラーを検出
- **開発体験**: IDEの補完が充実
- **リファクタリング**: 安全にリファクタリング可能

### ❌ デメリット
- **学習コスト**: TypeScriptの学習が必要
- **ビルド時間**: 型チェックによりビルド時間が増加

## 使用例

### 例1: コンポーネントの型定義

```typescript
// app/components/Button.tsx
interface ButtonProps {
  label: string;
  onClick: () => void;
  disabled?: boolean;
}

export default function Button({
  label,
  onClick,
  disabled = false,
}: ButtonProps) {
  return (
    <button onClick={onClick} disabled={disabled}>
      {label}
    </button>
  );
}
```

### 例2: API Routeの型定義

```typescript
// app/api/users/route.ts
import { NextRequest, NextResponse } from 'next/server';

export async function GET(request: NextRequest) {
  const users = [
    { id: '1', name: 'John' },
    { id: '2', name: 'Jane' },
  ];
  
  return NextResponse.json(users);
}
```

## よくある問題と解決策

### 問題1: 型エラーが発生する
**解決策**: `tsconfig.json`の設定を確認、型定義を追加

```typescript
// 型を明示的に定義
interface Props {
  // ...
}
```

### 問題2: パスエイリアスが機能しない
**解決策**: `tsconfig.json`と`next.config.js`の両方で設定

```json
// tsconfig.json
{
  "compilerOptions": {
    "paths": {
      "@/*": ["./*"]
    }
  }
}
```

## ベストプラクティス

1. **厳格モード**: `strict: true`を有効化
2. **型定義**: 適切な型定義を作成
3. **パスエイリアス**: `@/*`を使用してインポートを簡潔に

## 関連ノート
- [[Next.jsプロジェクトの作成方法]]
- [[Next.jsの設定ファイル]]

---
tags: [nextjs, typescript, type-safety, technical/programming]
created: 2025-11-13

