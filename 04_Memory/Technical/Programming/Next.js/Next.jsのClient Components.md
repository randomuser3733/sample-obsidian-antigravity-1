# Next.jsのClient Components

**関連MOC**: [[_Next.js-MOC]] | [[_Tech-MOC]]

## 概要
Client Componentsは、ブラウザで実行されるReactコンポーネントで、インタラクティブな機能やReact Hooksを使用できます。App Routerでは`'use client'`ディレクティブで明示的に指定します。

## 詳細
Client Componentsは、クライアント側でJavaScriptとして実行され、インタラクティブなUI、状態管理、ブラウザAPIへのアクセスが可能です。Server Componentsと組み合わせて使用します。

## 基本的な使い方

### 1. Client Componentの作成

```tsx
// app/components/Counter.tsx
'use client';

import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);
  
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>
      <button onClick={() => setCount(count - 1)}>
        Decrement
      </button>
    </div>
  );
}
```

### 2. Server Componentから使用

```tsx
// app/page.tsx (Server Component)
import Counter from '@/components/Counter';

export default function HomePage() {
  return (
    <div>
      <h1>Home</h1>
      <Counter />
    </div>
  );
}
```

### 3. フォーム処理

```tsx
// app/components/ContactForm.tsx
'use client';

import { useState } from 'react';

export default function ContactForm() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: '',
  });
  
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    // APIに送信
    const response = await fetch('/api/contact', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData),
    });
    // 処理...
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={formData.name}
        onChange={(e) =>
          setFormData({ ...formData, name: e.target.value })
        }
        placeholder="Name"
      />
      <input
        type="email"
        value={formData.email}
        onChange={(e) =>
          setFormData({ ...formData, email: e.target.value })
        }
        placeholder="Email"
      />
      <textarea
        value={formData.message}
        onChange={(e) =>
          setFormData({ ...formData, message: e.target.value })
        }
        placeholder="Message"
      />
      <button type="submit">Send</button>
    </form>
  );
}
```

## 高度な使い方

### 1. useEffectの使用

```tsx
// app/components/ClientOnly.tsx
'use client';

import { useState, useEffect } from 'react';

export default function ClientOnly() {
  const [mounted, setMounted] = useState(false);
  
  useEffect(() => {
    setMounted(true);
  }, []);
  
  if (!mounted) {
    return null; // またはローディング表示
  }
  
  return <div>Client-side content</div>;
}
```

### 2. カスタムフックの使用

```tsx
// hooks/useLocalStorage.ts
'use client';

import { useState, useEffect } from 'react';

export function useLocalStorage(key: string, initialValue: string) {
  const [storedValue, setStoredValue] = useState(() => {
    if (typeof window === 'undefined') {
      return initialValue;
    }
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      return initialValue;
    }
  });
  
  const setValue = (value: string) => {
    try {
      setStoredValue(value);
      if (typeof window !== 'undefined') {
        window.localStorage.setItem(key, JSON.stringify(value));
      }
    } catch (error) {
      console.error(error);
    }
  };
  
  return [storedValue, setValue] as const;
}

// app/components/ThemeToggle.tsx
'use client';

import { useLocalStorage } from '@/hooks/useLocalStorage';

export default function ThemeToggle() {
  const [theme, setTheme] = useLocalStorage('theme', 'light');
  
  return (
    <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
      Current theme: {theme}
    </button>
  );
}
```

### 3. ブラウザAPIの使用

```tsx
// app/components/Geolocation.tsx
'use client';

import { useState, useEffect } from 'react';

export default function Geolocation() {
  const [location, setLocation] = useState<GeolocationCoordinates | null>(null);
  
  useEffect(() => {
    if ('geolocation' in navigator) {
      navigator.geolocation.getCurrentPosition((position) => {
        setLocation(position.coords);
      });
    }
  }, []);
  
  if (!location) {
    return <div>Loading location...</div>;
  }
  
  return (
    <div>
      <p>Latitude: {location.latitude}</p>
      <p>Longitude: {location.longitude}</p>
    </div>
  );
}
```

## Client Componentsの特徴

### ✅ できること

1. **インタラクティブな機能**: `onClick`、`onChange`などのイベントハンドラ
2. **React Hooks**: `useState`、`useEffect`、`useContext`など
3. **ブラウザAPI**: `window`、`document`、`localStorage`など
4. **状態管理**: クライアント側の状態管理
5. **アニメーション**: CSSアニメーションやライブラリ（Framer Motionなど）

### ❌ できないこと（Server Componentで行うべきこと）

1. **データベースアクセス**: 直接データベースに接続できない
2. **環境変数**: `NEXT_PUBLIC_`プレフィックスが必要（クライアントに公開される）
3. **サーバー側の処理**: ファイルシステムアクセスなど

## メリット・デメリット

### ✅ メリット
- **インタラクティブ性**: ユーザーインタラクションに対応
- **リアルタイム更新**: クライアント側でリアルタイムに更新可能
- **状態管理**: 複雑な状態管理が可能
- **ブラウザAPI**: ブラウザの機能を活用可能

### ❌ デメリット
- **バンドルサイズ**: クライアントにJavaScriptを送信するため、バンドルサイズが増加
- **初期読み込み**: 初期読み込み時間が増加する可能性
- **SEO**: クライアント側レンダリングのため、SEOに影響する場合がある

## 使用例

### 例1: 検索機能

```tsx
// app/components/Search.tsx
'use client';

import { useState, useMemo } from 'react';

interface SearchProps {
  items: string[];
}

export default function Search({ items }: SearchProps) {
  const [query, setQuery] = useState('');
  
  const filteredItems = useMemo(() => {
    return items.filter((item) =>
      item.toLowerCase().includes(query.toLowerCase())
    );
  }, [items, query]);
  
  return (
    <div>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search..."
      />
      <ul>
        {filteredItems.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </div>
  );
}
```

### 例2: モーダル

```tsx
// app/components/Modal.tsx
'use client';

import { useState } from 'react';

export default function Modal() {
  const [isOpen, setIsOpen] = useState(false);
  
  return (
    <>
      <button onClick={() => setIsOpen(true)}>Open Modal</button>
      {isOpen && (
        <div className="modal-overlay" onClick={() => setIsOpen(false)}>
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <h2>Modal Title</h2>
            <p>Modal content</p>
            <button onClick={() => setIsOpen(false)}>Close</button>
          </div>
        </div>
      )}
    </>
  );
}
```

## よくある問題と解決策

### 問題1: `'use client'`を忘れる
**解決策**: インタラクティブな機能を使用する場合は必ず`'use client'`を追加

```tsx
'use client'; // 必須

import { useState } from 'react';
```

### 問題2: Server ComponentでClient Componentをインポートできない
**解決策**: Client Componentは別ファイルに分離し、Server Componentからインポート

```tsx
// ✅ 良い例
// app/page.tsx (Server Component)
import Counter from '@/components/Counter'; // Client Component

export default function Page() {
  return <Counter />;
}
```

### 問題3: ハイドレーションエラー
**解決策**: クライアント側でのみレンダリングする部分を分離

```tsx
'use client';

import { useState, useEffect } from 'react';

export default function ClientOnly() {
  const [mounted, setMounted] = useState(false);
  
  useEffect(() => {
    setMounted(true);
  }, []);
  
  if (!mounted) return null;
  
  return <div>Client content</div>;
}
```

## ベストプラクティス

1. **最小限の使用**: 必要な部分だけClient Componentにする
2. **Server Componentを優先**: デフォルトでServer Componentを使用
3. **境界の明確化**: Server ComponentとClient Componentの境界を明確にする
4. **プロップスの受け渡し**: Server Componentからデータを受け取る
5. **ハイドレーション**: クライアント側でのみ必要な部分を分離

## 関連ノート
- [[Next.jsのApp Router]]
- [[Next.jsのServer Components]]
- [[Next.jsのデータフェッチング]]

---
tags: [nextjs, client-components, react-hooks, technical/programming]
created: 2025-11-13

