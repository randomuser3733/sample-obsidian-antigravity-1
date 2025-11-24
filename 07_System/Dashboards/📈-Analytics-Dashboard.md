# 📈 Analytics Dashboard

## KPIサマリー
| 指標 | 目標 | 実績 | コメント |
|------|------|------|-----------|
| YouTube登録者 | +300 | +120 | ショートを増やす |
| メール開封率 | 45% | 42% | 件名ABテスト継続 |
| SURVIBE応募 | 30 | 28 | 次回キャンペーン準備 |

## データビュー
```dataview
TABLE trend, notes
FROM "05_Output"
WHERE contains(file.tags, "analytics")
SORT file.mtime DESC
```

## コメント
- 数値の急変があった週は必ず原因をメモする。
- 週次レビューと月次レビューの両方で振り返る。
