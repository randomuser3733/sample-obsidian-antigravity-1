# Next.jsのAPI Routes

**関連MOC**: [[_Next.js-MOC]] | [[_Tech-MOC]]

## 概要
Next.js App Routerでは、`route.ts`ファイルを使用してAPIエンドポイントを作成できます。GET、POST、PUT、DELETEなどのHTTPメソッドをサポートします。

## 詳細
API Routesは、Next.jsアプリケーション内でバックエンドAPIを構築する方法です。`app/api/`ディレクトリ内に`route.ts`ファイルを作成することで、RESTful APIエンドポイントを定義できます。

## 基本的な使い方

### 1. GETリクエスト

```tsx
// app/api/users/route.ts
export async function GET() {
  const users = [
    { id: 1, name: 'John' },
    { id: 2, name: 'Jane' },
  ];
  
  return Response.json(users);
}
```

### 2. POSTリクエスト

```tsx
// app/api/users/route.ts
export async function POST(request: Request) {
  const body = await request.json();
  
  // データベースに保存
  // const user = await db.user.create({ data: body });
  
  return Response.json({ success: true }, { status: 201 });
}
```

### 3. 複数のHTTPメソッド

```tsx
// app/api/users/route.ts
export async function GET() {
  return Response.json({ message: 'GET request' });
}

export async function POST(request: Request) {
  const body = await request.json();
  return Response.json({ message: 'POST request', data: body });
}

export async function PUT(request: Request) {
  const body = await request.json();
  return Response.json({ message: 'PUT request', data: body });
}

export async function DELETE() {
  return Response.json({ message: 'DELETE request' });
}
```

## 高度な使い方

### 1. 動的ルート

```tsx
// app/api/users/[id]/route.ts
export async function GET(
  request: Request,
  { params }: { params: Promise<{ id: string }> }
) {
  const { id } = await params;
  
  // ユーザーを取得
  // const user = await db.user.findUnique({ where: { id } });
  
  return Response.json({ id });
}
```

### 2. リクエストパラメータの取得

```tsx
// app/api/search/route.ts
export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const query = searchParams.get('q');
  
  return Response.json({ query });
}
```

### 3. ヘッダーの設定

```tsx
// app/api/data/route.ts
export async function GET() {
  return Response.json(
    { data: 'example' },
    {
      headers: {
        'Content-Type': 'application/json',
        'Cache-Control': 'no-store',
      },
    }
  );
}
```

### 4. エラーハンドリング

```tsx
// app/api/users/route.ts
export async function GET() {
  try {
    const users = await db.user.findMany();
    return Response.json(users);
  } catch (error) {
    return Response.json(
      { error: 'Failed to fetch users' },
      { status: 500 }
    );
  }
}
```

## 使用例

### 例1: ユーザーCRUD API

```tsx
// app/api/users/route.ts
import { db } from '@/lib/db';

export async function GET() {
  const users = await db.user.findMany();
  return Response.json(users);
}

export async function POST(request: Request) {
  const body = await request.json();
  const user = await db.user.create({
    data: {
      name: body.name,
      email: body.email,
    },
  });
  return Response.json(user, { status: 201 });
}
```

### 例2: 認証API

```tsx
// app/api/auth/login/route.ts
export async function POST(request: Request) {
  const { email, password } = await request.json();
  
  // 認証処理
  // const user = await authenticate(email, password);
  
  if (!user) {
    return Response.json(
      { error: 'Invalid credentials' },
      { status: 401 }
    );
  }
  
  // トークンを生成
  const token = generateToken(user);
  
  return Response.json({ token });
}
```

## メリット・デメリット

### ✅ メリット
- **統合**: フロントエンドとバックエンドを1プロジェクトで管理
- **型安全**: TypeScriptで型定義可能
- **シンプル**: 追加のサーバー設定が不要

### ❌ デメリット
- **スケーラビリティ**: 大規模なAPIには専用のバックエンドが必要な場合がある
- **制約**: Next.jsの制約に従う必要がある

## よくある問題と解決策

### 問題1: CORSエラー
**解決策**: ヘッダーを設定

```tsx
export async function GET() {
  return Response.json(
    { data: 'example' },
    {
      headers: {
        'Access-Control-Allow-Origin': '*',
      },
    }
  );
}
```

### 問題2: リクエストボディが取得できない
**解決策**: `request.json()`を使用

```tsx
export async function POST(request: Request) {
  const body = await request.json();
  // ...
}
```

## ベストプラクティス

1. **エラーハンドリング**: 適切なエラーハンドリングを実装
2. **型安全**: TypeScriptで型を定義
3. **バリデーション**: リクエストデータのバリデーション
4. **セキュリティ**: 認証・認可を実装

## 関連ノート
- [[Next.jsのデータフェッチング]]
- [[Next.jsの環境変数設定]]

---
tags: [nextjs, api-routes, backend, technical/programming]
created: 2025-11-13

