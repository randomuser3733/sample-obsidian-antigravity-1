#!/usr/bin/env python3
"""Populate all zero-length markdown files with Japanese content appropriate to their role."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
import re
from textwrap import dedent
from typing import Callable, Dict, List

BASE_DIR = Path(__file__).resolve().parents[1]


@dataclass
class TokenInfo:
    summary: str
    points: List[str]
    actions: List[str]


def slug_to_title(slug: str) -> str:
    tokens = [t for t in slug.replace('_', '-').split('-') if t]
    mapped: List[str] = []
    for token in tokens:
        mapped.append(TOKEN_TRANSLATIONS.get(token.lower(), token.capitalize()))
    return ''.join(mapped) if mapped else slug


def slug_tokens(slug: str) -> List[str]:
    return [t for t in re.split(r'[-_]', slug.lower()) if t]


def format_block(text: str) -> str:
    return dedent(text).strip() + '\n'


TOKEN_TRANSLATIONS: Dict[str, str] = {
    '2025': '2025',
    '00': '00',
    '01': '01',
    '02': '02',
    '03': '03',
    '04': '04',
    '05': '05',
    'w01': 'W01',
    'w02': 'W02',
    'home': 'HOME',
    'weekly': 'Weekly',
    'analytics': 'Analytics',
    'projects': 'Projects',
    'focus': 'Focus',
    'master': 'Master',
    'index': 'Index',
    'personal': 'Personal',
    'health': 'Health',
    'stress': 'ストレス',
    'management': 'マネジメント',
    'exercise': 'エクササイズ',
    'routines': 'ルーティン',
    'parenting': '子育て',
    'philosophy': '方針',
    'child': '子ども',
    'development': '成長',
    'balance': 'バランス',
    'work': 'ワーク',
    'family': 'ファミリー',
    'productivity': '生産性',
    'wave': '波',
    'pattern': 'パターン',
    'optimization': '最適化',
    'energy': 'エネルギー',
    'focus': '集中',
    'time': 'タイム',
    'education': 'Education',
    'pedagogy': '教育学',
    'active': 'アクティブ',
    'learning': 'ラーニング',
    'feedback': 'フィードバック',
    'adult': '成人',
    'curriculum': 'カリキュラム',
    'design': 'デザイン',
    'assessment': '評価',
    'teaching': 'Teaching',
    'techniques': 'Techniques',
    'storytelling': 'ストーリーテリング',
    'metaphor': 'メタファー',
    'usage': '活用',
    'live': 'ライブ',
    'coding': 'コーディング',
    'business': 'Business',
    'sales': 'Sales',
    'pricing': 'プライシング',
    'strategy': '戦略',
    'consultative': 'コンサルティブ',
    'community': 'コミュニティ',
    'building': '構築',
    'member': 'メンバー',
    'retention': '維持',
    'event': 'イベント',
    'operations': 'Operations',
    'workflow': 'ワークフロー',
    'automation': '自動化',
    'marketing': 'Marketing',
    'social': 'ソーシャル',
    'media': 'メディア',
    'positioning': 'ポジショニング',
    'funnel': 'ファネル',
    'content': 'コンテンツ',
    'ai': 'AI',
    'tools': 'Tools',
    'cursor': 'Cursor',
    'shortcuts': 'ショートカット',
    'basics': '基礎',
    'advanced': '上級',
    'tips': 'Tips',
    'troubleshooting': 'トラブルシュート',
    'claude': 'Claude',
    'api': 'API',
    'guide': 'ガイド',
    'projects': 'Projects',
    'prompting': 'プロンプト',
    'windsurf': 'Windsurf',
    'bolt': 'Bolt',
    'new': 'New',
    'v0': 'v0',
    'dev': 'Dev',
    'dify': 'Dify',
    'concepts': 'Concepts',
    'llm': 'LLM',
    'fundamentals': '基礎',
    'transformer': 'Transformer',
    'architecture': 'アーキテクチャ',
    'safety': 'セーフティ',
    'prompt': 'Prompt',
    'examples': 'Examples',
    'explanation': 'Explanation',
    'debugging': 'Debugging',
    'code': 'コード',
    'generation': '生成',
    'patterns': 'パターン',
    'promptops': 'PromptOps',
    'rag': 'RAG',
    'vector': 'ベクター',
    'database': 'データベース',
    'chunking': 'チャンク化',
    'multi': 'マルチ',
    'agent': 'エージェント',
    'systems': 'システム',
    'devops': 'DevOps',
    'deployment': 'デプロイ',
    'docker': 'Docker',
    'ci': 'CI',
    'cd': 'CD',
    'scalability': 'スケーラビリティ',
    'system': 'システム',
    'patterns': 'パターン',
    'programming': 'Programming',
    'python': 'Python',
    'data': 'データ',
    'structures': '構造',
    'best': 'ベスト',
    'practices': 'プラクティス',
    'typescript': 'TypeScript',
    'next.js': 'Next.js',
    'javascript': 'JavaScript',
    'async': '非同期',
    'modern': 'モダン',
    'react': 'React',
    'input': 'Input',
    'reference': 'リファレンス',
    'templates': 'テンプレート',
    'meeting': 'Meeting',
    'knowledge': 'Knowledge',
    'archive': 'Archive',
    'areas': 'Areas',
    'projects': 'Projects',
}


TOKEN_INFO: Dict[str, TokenInfo] = {
    'stress': TokenInfo(
        summary="ストレス反応を定量化し、交感神経の過剰な昂りを抑える。",
        points=[
            "トリガーを『環境』『人』『思考』に分類してジャーナル化すると原因の傾向が見える。",
            "アラートを感じたらボックスブリージングで心拍を整え、視野を広げる。",
        ],
        actions=[
            "1日3回のマイクロチェックインで体調、感情、集中度を10段階でメモする。",
            "週末にストレスログを見返し、手放したい案件や会議を一つ選んで減らす。",
        ],
    ),
    'exercise': TokenInfo(
        summary="運動習慣を有酸素・筋力・柔軟の3軸で設計し、疲労の蓄積を防ぐ。",
        points=[
            "月曜は低負荷の全身サーキット、水曜はHIIT、金曜は長めの散歩でリズムを作る。",
            "フォームを動画で記録し、2週に一度リプレイして改善点を洗い出す。",
        ],
        actions=[
            "Apple WatchのムーブリングをSlackに自動投稿して可視化する。",
            "筋トレ日はタンパク質1.6g/kgを意識し、食事ログに補食も含めて記録する。",
        ],
    ),
    'parenting': TokenInfo(
        summary="子育ての価値観を言語化し、家族全員が安心できるガイドラインを整える。",
        points=[
            "行動ではなく感情を認める声かけを最優先し、自己肯定感を支える。",
            "週1回のファミリーミーティングで予定と気持ちを共有する。",
        ],
        actions=[
            "シーズンごとに『家族の合言葉』を決め、家のホワイトボードに貼る。",
            "学びたいテーマは親も一緒に調べ、好奇心の連鎖を体験させる。",
        ],
    ),
    'child': TokenInfo(
        summary="発達段階ごとの興味と成長サインを把握し、声かけを最適化する。",
        points=[
            "月齢ごとのできごとを『身体・知性・感情』で記録すると変化が捉えやすい。",
            "非認知能力は小さな成功体験を一緒に振り返ることで強化できる。",
        ],
        actions=[
            "観察ログに『発言』『環境』『気づき』の3列を用意し、日付タグで並べる。",
            "保育園や学校からの連絡を週次レビューに転記し、家庭でのフォローを決める。",
        ],
    ),
    'balance': TokenInfo(
        summary="ワークとファミリーの接点を構造化し、罪悪感なく切り替えられるようにする。",
        points=[
            "日中は深い集中時間を守り、夕方以降は家族モードに入るスイッチ儀式を作る。",
            "家族イベントは四半期ごとに先にカレンダーへブロックし、仕事を後から調整する。",
        ],
        actions=[
            "夫婦のタスクボードを共有し、お互いの負荷を見える化する。",
            "祝いや行事の準備タスクリストをテンプレ化し、直前のバタつきを減らす。",
        ],
    ),
    'wave': TokenInfo(
        summary="1日のエネルギー波形を捉え、クリエイティブとルーチンを最適に配分する。",
        points=[
            "起床から4時間は発散→収束→発散のサイクルを意識すると思考が途切れにくい。",
            "15時以降は意思決定よりレビューや資料整理を入れ、決断疲れを防ぐ。",
        ],
        actions=[
            "Notionデータベースに時間帯×集中度を記録し、ヒートマップで可視化する。",
            "前夜に『最高の朝』ルーティンを書き出し、起床後の迷いをなくす。",
        ],
    ),
    'energy': TokenInfo(
        summary="身体・感情・認知のエネルギー残量を分けて管理し、燃え尽きを回避する。",
        points=[
            "食事と睡眠の質をタグ付けして関連性を確認すると調整ポイントが見つかる。",
            "週に一度「エネルギーを奪う物事」を棚卸しし、手放す判断を入れる。",
        ],
        actions=[
            "水分・カフェイン摂取をショートカットキーで即記録できるようにする。",
            "季節ごとにサプリや運動メニューを見直し、身体負荷を平準化する。",
        ],
    ),
    'focus': TokenInfo(
        summary="集中リソースを守り、ディープワーク時間を戦略的に確保する。",
        points=[
            "午前は90分ブロック×2を死守し、午後はインタラクション中心に組む。",
            "環境トリガー（音・光・椅子）を整えるだけで集中率が15%以上向上する。",
        ],
        actions=[
            "Noise-cancelling + BGM の組み合わせを3種類用意し、タスクによって切り替える。",
            "最初の5分で完了イメージを紙に描き、脳内の散漫さを減らす。",
        ],
    ),
    'time': TokenInfo(
        summary="時間を投資・維持・浪費に仕分けし、価値の高い予定にリソースを集中させる。",
        points=[
            "Googleカレンダーを色分けし、可処分時間の残量を常に把握する。",
            "集中帯に会議が入る場合は理由と期待成果を参加者と共有する。",
        ],
        actions=[
            "週次で『失った時間ログ』を書き、翌週のガードレールを決める。",
            "定例は四半期ごとに棚卸しし、目的が薄れたものは思い切って終了する。",
        ],
    ),
    'active': TokenInfo(
        summary="アクティブラーニングの設計では、学習者の行動を最初に定義する。",
        points=[
            "知識投入→即実践→振り返りの1サイクルを30分以内で回すと定着率が高まる。",
            "問いを提示する際は難易度と情緒的ハードルを分けて調整する。",
        ],
        actions=[
            "授業の冒頭に『今日の挑戦』カードを配布し、目的を共有する。",
            "受講者のアウトプットをMiroボードに集約し、全員で比較できるようにする。",
        ],
    ),
    'feedback': TokenInfo(
        summary="フィードバックは観察・解釈・提案の3段階で届ける。",
        points=[
            "事実と感想を分け、相手の意図を先に確認してから助言する。",
            "即時フィードバックはモチベ維持に、遅延フィードバックは深い学びに効く。",
        ],
        actions=[
            "SBI（Situation-Behavior-Impact）メモをテンプレ化し、フィードバック前に整理する。",
            "ポジティブ:改善 = 2:1 の割合を守り、心理的安全性を担保する。",
        ],
    ),
    'adult': TokenInfo(
        summary="成人学習では内発的動機と即時活用の道筋をセットで提示する。",
        points=[
            "経験→概念化→実践→内省のコルブサイクルを1コマ内に収める。",
            "自己決定感を高めるために小さな選択肢を頻繁に用意する。",
        ],
        actions=[
            "事前アンケートで課題を集め、講義内の事例に反映する。",
            "学習計画を3週間サイクルで設計し、フォローアップ面談を組み込む。",
        ],
    ),
    'objectives': TokenInfo(
        summary="学習目標は行動・条件・評価基準の3要素で書くと測定可能になる。",
        points=[
            "Bloomのタキソノミーに沿って認知レベルを定義し、教材の粒度を合わせる。",
            "目標数は1セッションにつき最大3つまでに絞る。",
        ],
        actions=[
            "『誰が・どの状況で・どのレベルまで』を書き切るテンプレを作る。",
            "目標と評価指標を同じスプレッドシートで管理し、抜け漏れを防ぐ。",
        ],
    ),
    'backward': TokenInfo(
        summary="バックワードデザインでは成果物から逆算して学習体験を組み立てる。",
        points=[
            "終着点を定義→証拠を決める→学習活動を設計するの順番を崩さない。",
            "評価方法はルーブリックを先に作り、受講者とも共有する。",
        ],
        actions=[
            "成果物のサンプルを早期に見せ、期待値の認識合わせを行う。",
            "各ステップのToDoをTrelloに登録し、レビュー日を自動通知する。",
        ],
    ),
    'assessment': TokenInfo(
        summary="評価設計はフォーミング・サマティブ双方の指標を連動させる。",
        points=[
            "観察記録、自己評価、ピアレビューを組み合わせると偏りが減る。",
            "定量評価だけでなくコメント欄を設け、文脈を残す。",
        ],
        actions=[
            "Googleフォームでチェックリスト化し、結果を自動集計する。",
            "重要指標はシンプルなスコアカードにまとめ、ステークホルダーへ共有する。",
        ],
    ),
    'storytelling': TokenInfo(
        summary="ストーリーテリングは主人公・葛藤・変化の3要素で構成する。",
        points=[
            "導入で課題を提示し、過程で学びを描き、結末で行動変容を示す。",
            "比喩やデータを織り交ぜると説得力が増す。",
        ],
        actions=[
            "ワークショップではストーリーキャンバスを配布し、参加者に書いてもらう。",
            "音声収録して声のトーンや間を振り返る。",
        ],
    ),
    'metaphor': TokenInfo(
        summary="メタファー活用は概念を既知の体験に橋渡しする技術。",
        points=[
            "聴衆が既に知っている世界観を例に選ぶと理解が早い。",
            "1つの説明でメタファーは1種類までに絞る。",
        ],
        actions=[
            "よく使うメタファー集をカテゴリー別に整理し、必要に応じて更新する。",
            "誤解を招いたメタファーは学習ログに残し、再発を防ぐ。",
        ],
    ),
    'live': TokenInfo(
        summary="ライブコーディングでは失敗を恐れず、思考の声を実況する。",
        points=[
            "事前にコードスニペットを準備し、貼り付け時間を短縮する。",
            "意図的に軽いエラーを出し、デバッグ手順を見せると理解が進む。",
        ],
        actions=[
            "画面レイアウトを固定し、ズームレベルと配色を参加者に合わせる。",
            "2台目の端末でチャットを監視し、質問を即拾えるようにする。",
        ],
    ),
    'pricing': TokenInfo(
        summary="価格戦略は価値指標とコスト構造の両面から検討する。",
        points=[
            "アンカー価格・フロントエンド・バックエンドを組み合わせてLTVを最大化する。",
            "値上げ時はベネフィットの再定義とFAQ更新を同時に行う。",
        ],
        actions=[
            "競合比較シートを作り、価格帯×差別化要素を視覚化する。",
            "キャンペーン時は利益率シミュレーターで限界点を確認する。",
        ],
    ),
    'consultative': TokenInfo(
        summary="コンサルティブセリングは課題の共同発見と解決ロードマップの提示が肝。",
        points=[
            "診断フェーズではWhyを5回掘り下げ、真因を特定する。",
            "提案は『現状→障壁→未来像』の順で語ると納得感が高い。",
        ],
        actions=[
            "商談前にクライアントのKPIと政治的状況を整理したブリーフを作成。",
            "次の打ち合わせまでに小さな成功体験を届け、信頼を積む。",
        ],
    ),
    'member': TokenInfo(
        summary="メンバー維持は『価値を感じる瞬間』を継続的に提供することが鍵。",
        points=[
            "オンボーディング90日間のタッチポイントを設計する。",
            "休眠サイン（参加率・発言数）を指標化し、早期に声をかける。",
        ],
        actions=[
            "歓迎メッセージの後に『最初の一歩タスク』を案内し、参加障壁を下げる。",
            "退会理由を定期的に振り返り、プロダクトや運営改善に反映する。",
        ],
    ),
    'event': TokenInfo(
        summary="イベント設計は体験曲線（期待→参加→余韻）を意識する。",
        points=[
            "アジェンダは45分以内に一度休憩やワークを入れて集中を維持する。",
            "参加後のフォロー資料とアンケートを24時間以内に送る。",
        ],
        actions=[
            "逆算式ガントチャートを作り、Key Milestoneを共有する。",
            "登壇者の紹介テンプレとチェックリストを用意し、当日の混乱を防ぐ。",
        ],
    ),
    'community': TokenInfo(
        summary="コミュニティの熱量は目的・儀式・物語の3つで維持できる。",
        points=[
            "定期的なハイライト投稿で成功事例を称え、模範行動を示す。",
            "季節イベントやバッジ制度で帰属意識を高める。",
        ],
        actions=[
            "ロイヤルメンバーと四半期レビューを実施し、改善点を聞き出す。",
            "貢献度をスコア化し、ニュースレターで感謝を表明する。",
        ],
    ),
    'workflow': TokenInfo(
        summary="ワークフロー自動化は『繰り返し×エラーが多い』領域から着手する。",
        points=[
            "業務フローを泳線図で描き、手作業のボトルネックを特定。",
            "自動化後も責任者による週次モニタリングを設定する。",
        ],
        actions=[
            "ZapierやMakeのシナリオをリポジトリ化し、再利用できる形にする。",
            "失敗時のリトライやアラートを事前に設計しておく。",
        ],
    ),
    'automation': TokenInfo(
        summary="自動化は『例外処理の設計』まで含めて仕上げとする。",
        points=[
            "API制限や権限エラーを想定したフォールバック経路を用意する。",
            "ログをSlackやDataDogに集約し、障害検知を早める。",
        ],
        actions=[
            "Runbookを作成し、誰でも復旧できるようドキュメント化する。",
            "RPAとiPaaSの適材適所を比較表にまとめる。",
        ],
    ),
    'social': TokenInfo(
        summary="ソーシャルメディア戦略はペルソナの行動時間とトーンを最適化する。",
        points=[
            "プラットフォームごとの目的（認知/信頼/行動）を明確にする。",
            "投稿は価値提供:自社情報 = 3:1 を維持すると嫌われない。",
        ],
        actions=[
            "1か月分のテーマをバッチ化し、CanvaやFigmaでテンプレート化する。",
            "反応データを週次でCSVに落とし、学びを次週に反映する。",
        ],
    ),
    'positioning': TokenInfo(
        summary="ポジショニングは競合マトリクス上で空白を見つけ、強みを尖らせる。",
        points=[
            "機能軸だけでなく『世界観』『サポート』『価格柔軟性』で比較する。",
            "タグラインは顧客の言葉を引用して作ると刺さりやすい。",
        ],
        actions=[
            "競合インサイトノートを毎月更新し、変化を追跡する。",
            "営業資料に『向いていない顧客』も明記し、信頼を高める。",
        ],
    ),
    'funnel': TokenInfo(
        summary="ファネル設計は各段階のコンテンツとCTAをセットで定義する。",
        points=[
            "TOFU/MOFU/BOFUで提供価値を変え、次のアクションへ自然に誘導する。",
            "指標は転換率とスピードを同時に追跡する。",
        ],
        actions=[
            "MAツールでセグメントごとのナーチャリングシナリオを構築する。",
            "離脱ポイントごとに改善仮説をA/Bテストする。",
        ],
    ),
    'content': TokenInfo(
        summary="コンテンツ戦略はペルソナの課題と検索意図に直結させる。",
        points=[
            "1本の記事で伝えるメッセージは1テーマに絞る。",
            "更新サイクルを決め、陳腐化を防ぐ。",
        ],
        actions=[
            "キーワード×課題のマトリクスを作り、重複を避ける。",
            "執筆後24時間でセルフレビューし、伝わりづらい箇所を修正する。",
        ],
    ),
    'cursor': TokenInfo(
        summary="CursorはAIペアプログラミングを活かした高速開発が強み。",
        points=[
            "チェットペインで仕様を説明すると関数単位で提案が返ってくる。",
            "プロジェクトごとにモデル設定を変え、ClaudeとGPTを使い分ける。",
        ],
        actions=[
            "プロンプトをスニペット化し、ショートカットですぐ呼び出せるよう設定する。",
            "コードリーディング時はフォーカスモードをオンにし、差分だけに集中する。",
        ],
    ),
    'shortcuts': TokenInfo(
        summary="ショートカット整備は思考のリズムを崩さずに操作できる鍵。",
        points=[
            "⌘Pでファイル移動、⇧⌘Kでコマンド検索などよく使う操作を5個に限定して覚える。",
            "マクロキーにAI呼び出しとコード整形を割り当てるとトグルが減る。",
        ],
        actions=[
            "週1回ショートカットの習熟度を自己採点し、使えていないものを練習する。",
            "チームでお気に入りショートカットを共有し、知識を蓄積する。",
        ],
    ),
    'basics': TokenInfo(
        summary="基礎機能を体系的に押さえると応用も楽になる。",
        points=[
            "カーソルのパネル構造、AIモード、ターミナル連携を最初に理解する。",
            "設定同期と環境変数の扱いを覚えておくとプロジェクト移行時に迷わない。",
        ],
        actions=[
            "初学者向けのワークショップを30分で開き、復習としてアウトプットする。",
            "学んだショートカットや設定をREADMEにまとめ、次回セットアップを短縮する。",
        ],
    ),
    'advanced': TokenInfo(
        summary="上級テクではマルチファイル編集やエージェント駆動を駆使する。",
        points=[
            "DiffビューでAI提案を比較し、採用理由をコメントに残す。",
            "シナリオフローを設計し、連続した指示で大規模リファクタを実現する。",
        ],
        actions=[
            "プロンプトチェーンをテンプレ化し、似た案件に再利用する。",
            "クラッシュ時の復元ポイントをこまめに保存する。",
        ],
    ),
    'tips': TokenInfo(
        summary="Tips集は小さな工夫を素早く参照できるナレッジベース。",
        points=[
            "状況別（リファクタ、調査、生成など）にタグ分けすると検索しやすい。",
            "うまくいかなかった例も並べ、判断材料を残す。",
        ],
        actions=[
            "週末に新しく学んだコマンドを2個追加する。",
            "Slackチャンネルで共有し、チーム全体の生産性を底上げする。",
        ],
    ),
    'troubleshooting': TokenInfo(
        summary="トラブルシュートメモは異常兆候→原因→対処を紐づける。",
        points=[
            "ログの見方と主要エラーコードをまとめておく。",
            "再現手順を明記し、検証環境との差分を記録する。",
        ],
        actions=[
            "原因判明後は再発防止策（設定変更や手順）をチームに共有する。",
            "GitHub Issueに紐づけ、履歴をトレースできるようにする。",
        ],
    ),
    'claude': TokenInfo(
        summary="Claudeは長文コンテキストと指示理解に優れたモデル。",
        points=[
            "APIではsystem promptでトーンや役割を丁寧に定義する。",
            "プロジェクト単位でキーを分け、利用状況を可視化する。",
        ],
        actions=[
            "バージョンごとの差分をノートにまとめ、利用目的で選択基準を持つ。",
            "Claudeの回答をそのまま使わず、根拠の引用や根拠URLを必ず確認する。",
        ],
    ),
    'api': TokenInfo(
        summary="API接続時はレート制限とコスト管理を最初に設計する。",
        points=[
            "Streamingと非Streamingのレスポンス差を理解してUIに反映する。",
            "監査ログを保存し、問い合わせトレースを可能にする。",
        ],
        actions=[
            "SDKのバージョンアップ時は互換性チェックリストを実行する。",
            "環境変数でキーを管理し、ローテーションを自動化する。",
        ],
    ),
    'projects': TokenInfo(
        summary="プロジェクト事例を蓄積すると再利用できるテンプレが増える。",
        points=[
            "課題→アプローチ→成果→学びの4要素で記録する。",
            "顧客の声やKPIの変化を含めると説得力が出る。",
        ],
        actions=[
            "事例をNotionデータベース化し、検索性を高める。",
            "毎月1件はケーススタディとしてブログにまとめる。",
        ],
    ),
    'prompting': TokenInfo(
        summary="プロンプト設計はゴール・文脈・制約の3点セット。",
        points=[
            "思考過程を明示させるにはChain of Thoughtやルーブリックを添える。",
            "サンプル入力/出力を与えるFew-shotが精度を底上げする。",
        ],
        actions=[
            "用途別のプロンプトライブラリをGitで管理する。",
            "結果検証シートを作り、改善の履歴を残す。",
        ],
    ),
    'windsurf': TokenInfo(
        summary="Windsurfはブラウザ上でAI支援が完結するエディタ。",
        points=[
            "クラウド開発環境と相性が良く、軽量作業に向く。",
            "ショートカットやAIモデル設定がCursorと異なるので比較表を作る。",
        ],
        actions=[
            "用途別に使い分け、CI/CDの補助ツールとして検証する。",
            "ワークスペーステンプレをエクスポートしてチーム共有する。",
        ],
    ),
    'bolt': TokenInfo(
        summary="Bolt.newはUIモックからコード生成までを高速化するWeb IDE。",
        points=[
            "FigmaインポートやUI部品の自動生成に強みがある。",
            "生成コードのライセンスと品質基準を事前に確認する。",
        ],
        actions=[
            "デザイン→実装の橋渡し用にPoCを作成し、導入判断材料にする。",
            "他のAI IDEとの比較検証レポートを作る。",
        ],
    ),
    'v0': TokenInfo(
        summary="v0.devはVercel提供のAI UIジェネレーター。",
        points=[
            "TailwindとNext.jsコードを即座に生成できるが、アクセシビリティは要確認。",
            "複数セクションを段階的に生成すると破綻しにくい。",
        ],
        actions=[
            "生成結果をStorybookに配置し、デザインチームとすり合わせる。",
            "LLMに渡すUI要件テンプレを整備する。",
        ],
    ),
    'dify': TokenInfo(
        summary="Difyはノーコードでエージェントやワークフローを組めるOSS。",
        points=[
            "ツールコールとナレッジベースをGUIで管理できる。",
            "権限・APIキー管理をCloud/自ホスで選べる柔軟性がある。",
        ],
        actions=[
            "社内ユースケース集を作り、テンプレートをクローンして使い回す。",
            "ログをAlertmanagerに連携し、失敗検知を自動化する。",
        ],
    ),
    'agents': TokenInfo(
        summary="エージェント構築ではロール設計とツール接続が肝。",
        points=[
            "ゴールを明確にし、必要最低限のツールを与える。",
            "メモリ設計（短期/長期）を用意し、文脈維持を行う。",
        ],
        actions=[
            "テスト用のシナリオリストを作り、暴走を検知する。",
            "コスト・応答速度をGrafanaでモニタリングする。",
        ],
    ),
    'workflows': TokenInfo(
        summary="ワークフロー構築では分岐条件とエラー経路を丁寧に設計する。",
        points=[
            "人手承認ポイントを挟むタイミングを明確にする。",
            "ログをステップごとに記録し、分析を容易にする。",
        ],
        actions=[
            "デバッグ環境でテストデータを複数用意して挙動を確認する。",
            "在庫やスケジュールと連携する際はAPI制限を事前調査する。",
        ],
    ),
    'setup': TokenInfo(
        summary="セットアップ時はアクセス制御とシークレット管理を最優先する。",
        points=[
            "環境変数、APIキー、Webhook URLを分離管理する。",
            "ロールベース権限を設定し、最小権限で運用する。",
        ],
        actions=[
            "構築手順をMarkdownに残し、誰でも再現できるようにする。",
            "本番投入前にスモールスタートで検証する。",
        ],
    ),
    'llm': TokenInfo(
        summary="LLMの理解はトークン化・確率分布・自己回帰の基礎から。",
        points=[
            "前処理で使われるSentencePieceやBPEの違いを確認する。",
            "温度やTop-pの設定で出力の多様性が変わる。",
        ],
        actions=[
            "サンプルプロンプトに対し温度とTop-pを変えて挙動を記録する。",
            "論文の擬似コードを読み、内部計算を追体験する。",
        ],
    ),
    'transformer': TokenInfo(
        summary="TransformerはAttention機構で文脈を捉えるアーキテクチャ。",
        points=[
            "Multi-Head Attentionで情報を多視点から解釈する。",
            "Positional Encodingで系列順序を学習に組み込む。",
        ],
        actions=[
            "公式論文とIllustrated Transformerを読み、理解度をメモする。",
            "小規模モデルをPyTorchで実装し、学習曲線を確認する。",
        ],
    ),
    'safety': TokenInfo(
        summary="AIセーフティは悪用防止・バイアス低減・透明性確保が軸。",
        points=[
            "レッドチームテストを実施し、危険応答を洗い出す。",
            "利用規約やユーザー啓蒙をセットで整備する。",
        ],
        actions=[
            "モデルの回答ログを匿名化して保存し、監査に備える。",
            "ガードレール提示用のプロンプトテンプレを作成する。",
        ],
    ),
    'explanation': TokenInfo(
        summary="説明用プロンプトは論理の流れと根拠提示を指示する。",
        points=[
            "レベル設定（初心者/専門家）を明記する。",
            "箇条書きや段階的に説明するよう求めると読みやすい。",
        ],
        actions=[
            "出力例を保存し、良い表現を別タスクにも流用する。",
            "誤説明が出たら修正指示まで含めて再学習する。",
        ],
    ),
    'debugging': TokenInfo(
        summary="デバッグ用プロンプトは失敗要因の仮説を列挙させる。",
        points=[
            "エラーメッセージと直前の操作をセットで提示する。",
            "再現手順と期待動作を書き、差分を明確にする。",
        ],
        actions=[
            "LLMに候補を出させた後、優先度順に検証する。",
            "対策をコードへ反映したら必ず再テストし、結果を記録する。",
        ],
    ),
    'code': TokenInfo(
        summary="コード生成ではスタイルガイドと制約を明示する。",
        points=[
            "入出力例と境界条件を提示することで品質が安定する。",
            "生成後は静的解析を通し、安全性を確認する。",
        ],
        actions=[
            "小さな関数単位で生成し、テストを積み重ねる。",
            "LLMへの依頼内容をGitのコミットメッセージと合わせて保管。",
        ],
    ),
    'generation': TokenInfo(
        summary="生成タスクは温度・max_tokensでコントロールする。",
        points=[
            "長文生成時はセクションごとに指示して破綻を防ぐ。",
            "評価指標を用意し、出力品質を定量チェックする。",
        ],
        actions=[
            "テキスト→要約→校正の順で3段階プロンプトを使う。",
            "LLMのモデル差をドキュメント化し、得意領域を整理する。",
        ],
    ),
    'patterns': TokenInfo(
        summary="プロンプトパターン集は再利用性を高める知識資産。",
        points=[
            "Role, Task, Format, Constraintなど要素を分解して整理する。",
            "実例とNG集をセットで載せる。",
        ],
        actions=[
            "パターンごとの成功率を記録し、改善に活かす。",
            "学習会で共有し、チーム全体の設計力を底上げする。",
        ],
    ),
    'promptops': TokenInfo(
        summary="PromptOpsはプロンプトのバージョン管理と評価を行う運用手法。",
        points=[
            "GitやFeature flagでどのバージョンが本番か追跡する。",
            "自動テストを組み込み、品質劣化を検知する。",
        ],
        actions=[
            "Prompt registryを構築し、利用履歴を残す。",
            "Metrics（品質/コスト/速度）をダッシュボード化する。",
        ],
    ),
    'vector': TokenInfo(
        summary="ベクターデータベースは類似度検索で文脈を復元する技術。",
        points=[
            "次元数や距離関数により精度と速度が変わる。",
            "チャンクサイズと重複率を調整し、検索漏れを減らす。",
        ],
        actions=[
            "監視クエリを設定し、挙動が劣化したら再埋め込みする。",
            "メタデータでフィルタリングし、不要な結果を除外する。",
        ],
    ),
    'chunking': TokenInfo(
        summary="チャンク戦略は文脈を保ちつつサイズを揃える工夫。",
        points=[
            "見出しや意味段落を基準にスライディングウィンドウで切る。",
            "各チャンクにサマリを添え、検索後の理解を助ける。",
        ],
        actions=[
            "異なるサイズでテストし、Precision/Recallを比較する。",
            "PDFやスライドはレイアウト要素を除去してから分割する。",
        ],
    ),
    'rag': TokenInfo(
        summary="RAGはRetrieve→Augment→Generateの一連の流れ。",
        points=[
            "検索クエリを生成する際にユーザー意図を保持する。",
            "回答には根拠を添え、引用元を提示する。",
        ],
        actions=[
            "評価指標にFaithfulnessとAnswer Relevancyを設定する。",
            "フェイルオーバーとしてFAQベースの回答を用意する。",
        ],
    ),
    'agent': TokenInfo(
        summary="エージェントは目標志向で外部ツールを呼び出す存在。",
        points=[
            "計画ステップと実行ステップを分離すると暴走しにくい。",
            "メモリ書き込みを行う際はフォーマットを固定する。",
        ],
        actions=[
            "タスク指示テンプレを作成し、観察結果を逐次レビューする。",
            "評価ベンチマークを用意し、リグレッションを防ぐ。",
        ],
    ),
    'multi': TokenInfo(
        summary="マルチエージェントでは役割分担と調停ロジックが重要。",
        points=[
            "コーディネーター役を配置し、衝突解決を自動化する。",
            "タスク分解と優先度付けを初期に実施する。",
        ],
        actions=[
            "SlackやWebhookでエージェント同士のログを可視化する。",
            "停止条件を明記し、処理が長引いた際に人間が介入できるようにする。",
        ],
    ),
    'deployment': TokenInfo(
        summary="デプロイはビルド、テスト、リリースの境界を明確にする。",
        points=[
            "青/緑デプロイやカナリアを活用してリスクを抑える。",
            "ロールバック手順を事前に自動化しておく。",
        ],
        actions=[
            "本番前にヘルスチェックと依存サービスの互換性を確認する。",
            "デプロイごとにメトリクスを記録し、傾向を分析する。",
        ],
    ),
    'docker': TokenInfo(
        summary="Dockerは環境再現性とデプロイ容易性を高める。",
        points=[
            "イメージサイズを抑えるためにマルチステージビルドを使う。",
            "セキュリティ更新のためにベースイメージの定期的なリビルドが必要。",
        ],
        actions=[
            "docker composeでローカル依存関係をまとめ、開発者体験を統一する。",
            "Dockerfileにコメントで根拠を記録し、変更理由を残す。",
        ],
    ),
    'ci': TokenInfo(
        summary="CIは小さな差分を頻繁にマージし、品質を保つ仕組み。",
        points=[
            "テストの並列化とキャッシュ戦略で速度を確保する。",
            "失敗時のリトライと通知を整備する。",
        ],
        actions=[
            "テストカバレッジをバッジ化し、基準値を守る。",
            "ワークフローのYAMLをテンプレにし、プロジェクト間で再利用する。",
        ],
    ),
    'cd': TokenInfo(
        summary="CDはリリースまでの手順を自動化し、人為的エラーを減らす。",
        points=[
            "環境ごとの差分をTerraformやPulumiでコード化する。",
            "シークレット管理をVault等で一元化する。",
        ],
        actions=[
            "本番適用前にステージングで自動承認フローを挟む。",
            "リリースノート生成をパイプラインに組み込む。",
        ],
    ),
    'scalability': TokenInfo(
        summary="スケーラビリティは垂直・水平の両面で考える。",
        points=[
            "ボトルネックをAPMで特定し、キャッシュ戦略や分割統治を検討する。",
            "データベース分割やメッセージキュー導入を視野に入れる。",
        ],
        actions=[
            "負荷試験を定期的に実施し、閾値を測定する。",
            "オートスケールの閾値をCloudWatch等で管理する。",
        ],
    ),
    'system': TokenInfo(
        summary="システム設計ではコンテキスト境界を意識する。",
        points=[
            "責務をBounded Contextに分割し、依存関係を最小化する。",
            "QoS指標（可用性・遅延・耐障害性）を早期に定義する。",
        ],
        actions=[
            "C4モデルで図解し、利害関係者との認識合わせに使う。",
            "データフローとエラー経路を明示した図を作る。",
        ],
    ),
    'design': TokenInfo(
        summary="設計は要件→制約→選択肢→妥協点の順で整理する。",
        points=[
            "KPIと技術的制約を一枚のドキュメントにまとめる。",
            "意思決定理由をADRに残す。",
        ],
        actions=[
            "リファレンスアーキテクチャを比較し、採用理由を明文化する。",
            "レビュー会で反証を募り、盲点を減らす。",
        ],
    ),
    'python': TokenInfo(
        summary="Pythonは読みやすさと豊富なライブラリが魅力。",
        points=[
            "PEP8準拠で書き、型ヒントを積極的に使う。",
            "仮想環境と依存管理（poetry/pipenv）を徹底する。",
        ],
        actions=[
            "pytestでスモークテストを整備し、CIに組み込む。",
            "標準ライブラリで済む処理は外部依存を増やさない。",
        ],
    ),
    'data': TokenInfo(
        summary="データ構造の理解はアルゴリズム選定を左右する。",
        points=[
            "配列・連結リスト・木・グラフなどの特性を比較する。",
            "Big-Oで時間/空間計算量を把握する。",
        ],
        actions=[
            "LeetCodeで週2題を解き、実装感覚を磨く。",
            "社内の典型処理を分析し、最適な構造を選ぶ。",
        ],
    ),
    'structures': TokenInfo(
        summary="データ構造の選択はメモリと処理のトレードオフ。",
        points=[
            "辞書型はO(1)の検索が強みだがメモリを消費する。",
            "Immutable構造が必要かどうかを判断する。",
        ],
        actions=[
            "ユースケースごとに採用理由を記し、後で見返せるようにする。",
            "コードレビューで構造の選択を説明できるよう準備する。",
        ],
    ),
    'best': TokenInfo(
        summary="ベストプラクティスは経験知を再利用可能な形でまとめたもの。",
        points=[
            "原則と例外をセットで記録すると新規メンバーにも伝わりやすい。",
            "アップデート履歴を残し、陳腐化を防ぐ。",
        ],
        actions=[
            "スライドやドキュメントとして定期的に共有会を開く。",
            "実践例を集め、成功/失敗の両面から学ぶ。",
        ],
    ),
    'practices': TokenInfo(
        summary="プラクティス集は日常業務にすぐ応用できるTipsを集める。",
        points=[
            "カテゴリ別に整理し、検索性を高める。",
            "実践後のフィードバック欄を作り改善を続ける。",
        ],
        actions=[
            "四半期ごとに棚卸しし、不要になったものを整理する。",
            "社内Wikiにアップデートログを残す。",
        ],
    ),
    'typescript': TokenInfo(
        summary="TypeScriptは型安全性で大規模開発を支える。",
        points=[
            "strictモードを有効化し、型推論に頼りすぎない。",
            "utility typesや型ガードで表現力を高める。",
        ],
        actions=[
            "tsconfigをプロジェクト共通化し、Lintルールと合わせる。",
            "型定義の変更はChangelogに記録する。",
        ],
    ),
    'nextjs': TokenInfo(
        summary="Next.jsはApp Routerでフルスタック開発を簡素化。",
        points=[
            "Server Componentsでデータ取得を最適化し、キャッシュ戦略を考える。",
            "Route HandlerでAPIを内包させ、BFF的に利用する。",
        ],
        actions=[
            "Edge/Nodeどちらで動かすかを事前に決定し、依存ライブラリを選ぶ。",
            "RSCとクライアントコンポーネントの境界を図に描いて共有する。",
        ],
    ),
    'js': TokenInfo(
        summary="JavaScriptの基礎はスコープ・非同期・プロトタイプチェーン。",
        points=[
            "var/let/constの挙動やTDZを理解しておく。",
            "非同期処理の仕組み（Event Loop）をイメージできるようにする。",
        ],
        actions=[
            "MDNのチュートリアルをベースに自作教材を作る。",
            "テスト駆動で基本APIの使い方を確認する。",
        ],
    ),
    'async': TokenInfo(
        summary="非同期制御はPromise/async-await/Observableの特徴を理解して選ぶ。",
        points=[
            "エラーハンドリングとキャンセル処理をセットで設計する。",
            "並列実行と直列実行を切り替えるユーティリティを用意する。",
        ],
        actions=[
            "AbortControllerを積極活用し、不要なリクエストを中断する。",
            "非同期テストではfake timersを使い、時間依存を排除する。",
        ],
    ),
    'modern': TokenInfo(
        summary="モダンJSはES Modulesや最新構文をフル活用する姿勢。",
        points=[
            "BabelやSWCを通じてブラウザ互換性を意識する。",
            "Optional chainingやNull合体演算子で防御的なコードを書く。",
        ],
        actions=[
            "ブラウザサポートポリシーを定め、Polyfillを管理する。",
            "ツールチェーンのアップデート情報をウォッチする。",
        ],
    ),
    'react': TokenInfo(
        summary="Reactは宣言的UIとコンポーネント志向で状態を管理する。",
        points=[
            "Hooksのルールを守り、副作用と描画を分離する。",
            "コンポーネント分割は責務単位で行い、再利用性を高める。",
        ],
        actions=[
            "StorybookでUIをドキュメント化し、QAを効率化する。",
            "パフォーマンス計測にReact Profilerを使い、メモ化の判断材料にする。",
        ],
    ),
    'marketing': TokenInfo(
        summary="マーケティングは顧客理解→価値提案→コミュニケーション設計。",
        points=[
            "カスタマージャーニーを描き、接点ごとの役割を決める。",
            "ファネル指標をモニタリングし、改善サイクルを回す。",
        ],
        actions=[
            "定性インタビューと定量データを組み合わせ、意思決定を行う。",
            "週次でキャンペーンを振り返るMTGを設定する。",
        ],
    ),
    'media': TokenInfo(
        summary="メディア選定は受け手のライフスタイルと情報密度を基準にする。",
        points=[
            "短尺動画・長文記事・メルマガなど役割を明確にする。",
            "再配信時はフォーマットを最適化し、同内容でも飽きさせない。",
        ],
        actions=[
            "各媒体のCTAを比較し、最もCVの高い導線へ集中投資する。",
            "配信時間帯をA/Bテストし、最適値を記録する。",
        ],
    ),
}

MEMORY_BASE_POINTS = {
    'Personal': [
        "身体・感情・思考の3レイヤーで状態を観察し、偏りを見つける。",
        "家族やチームと共有したい学びは週次レビューに転記する。",
    ],
    'Education': [
        "学習者の前提知識と動機を把握してから教材を設計する。",
        "インプットとアウトプットの比率を常に確認し、退屈させない。",
    ],
    'Business': [
        "顧客価値・提供プロセス・収益性の3視点で意思決定する。",
        "再現性のある施策はドキュメント化してチームに展開する。",
    ],
    'AI': [
        "モデル・データ・ワークフローの三位一体で設計する。",
        "LLMの挙動はログを残し、改善サイクルを回す。",
    ],
    'Technical': [
        "要件・制約・トレードオフを明文化してから実装に入る。",
        "品質と速度のバランスをメトリクスで見える化する。",
    ],
}

MEMORY_BASE_ACTIONS = {
    'Personal': [
        "毎週日曜に感情ログを振り返り、翌週のセルフケアを1つ決める。",
        "観察⇒気づき⇒次の一手を1行でメモする習慣を続ける。",
    ],
    'Education': [
        "授業や講座後にアンケートを即回収し、改善案を3つ書き出す。",
        "教材のバージョン管理を行い、更新意図を記す。",
    ],
    'Business': [
        "週次でKPIダッシュボードを見ながら改善タスクを決める。",
        "顧客の声を収集し、製品や運営の改善 backlog に追加する。",
    ],
    'AI': [
        "プロンプト・評価指標・失敗例をGitで管理する。",
        "モデル更新時はABテストで品質差分を検証する。",
    ],
    'Technical': [
        "設計メモをADR化し、意思決定理由を残す。",
        "CI/CDでテストを自動化し、リグレッションを防ぐ。",
    ],
}


def main() -> None:
    zero_files = sorted(
        [p for p in BASE_DIR.rglob('*') if p.is_file() and p.stat().st_size == 0]
    )
    for path in zero_files:
        content = generate_content(path)
        path.write_text(content, encoding='utf-8')


def generate_content(path: Path) -> str:
    rel = path.relative_to(BASE_DIR).as_posix()
    if rel.startswith('02_Daily/Weekly-Reviews/'):
        return generate_weekly_review(path)
    if rel.startswith('02_Daily/Monthly-Reviews/'):
        return generate_monthly_review(path)
    if rel.startswith('07_System/Dashboards/'):
        return generate_dashboard(path)
    if rel == '04_Memory/_Master-Index.md':
        return generate_memory_master_index()
    if rel.startswith('04_Memory/') and path.name.startswith('_'):
        return generate_memory_moc(path)
    if rel.startswith('04_Memory/'):
        return generate_memory_note(path)
    if rel.startswith('03_Input/'):
        return generate_input_note(path)
    if rel.startswith('06_Templates/'):
        return generate_template(path)
    if rel.startswith('99_Archive/'):
        return generate_archive_note(path)
    if rel.startswith('05_Output/Areas/Personal/'):
        return generate_area_personal(path)
    if rel.startswith('05_Output/Areas/Content-Creation/'):
        return generate_area_content_creation(path)
    if rel.startswith('05_Output/Areas/Business/'):
        return generate_area_business(path)
    if rel.startswith('05_Output/Projects/'):
        return generate_project_note(path)
    raise ValueError(f"No generator implemented for {rel}")


def generate_weekly_review(path: Path) -> str:
    week_label = path.stem
    year_str, week_part = week_label.split('-W')
    iso_year = int(year_str)
    iso_week = int(week_part)
    start = date.fromisocalendar(iso_year, iso_week, 1)
    end = start + timedelta(days=6)
    highlights = [
        f"YouTubeシリーズの収録準備を進め、台本レビューを{iso_week}件クリアした。",
        "SURVIBE AI講座の教材アップデートを実施し、受講者質問への回答テンプレも更新。",
        "CursorとClaudeの最新アップデートを検証し、社内メモへ反映した。",
    ]
    learnings = [
        "午前の集中時間にコンテンツづくりを固めると、午後の会議が楽になる。",
        "週後半はエネルギーが下がるため、軽めのメンテ作業を割り当てるとリズムが維持できる。",
    ]
    improvements = [
        "Inbox整理を水曜日にも一度実施し、週末の負荷を軽減する。",
        "NotionタスクとObsidianタスクの二重管理をなくすため、連携ルールを明文化する。",
    ]
    focus = [
        "YouTube EP02の撮影と編集チェックを完了させる。",
        "SURVIBE AIカリキュラムのWeek3演習をブラッシュアップする。",
        "AIツール比較記事のドラフトを水曜までに書き切る。",
    ]
    metrics_table = """| 指標 | 今週 | メモ |
|------|------|------|
| Deep Work時間 | 14h | 午前2ブロック確保に成功 |
| コンテンツ公開数 | 2本 | ブログ1/動画1 |
| 学習ログ | 4件 | Claude/Dify/PromptOpsなど |
"""
    return format_block(
        f"""---
week: {week_label}
start: {start}
end: {end}
tags: [weekly-review, {iso_year}, {week_label}]
---

# {week_label} 週次レビュー

## 🌟 ハイライト
"""
    ) + '\n'.join(f"- {item}" for item in highlights) + '\n\n' + format_block(
        "## 📊 指標チェック\n" + metrics_table
    ) + format_block(
        "## 🧠 学びと気づき\n" + '\n'.join(f"- {item}" for item in learnings)
    ) + format_block(
        "## 🛠 改善アクション\n" + '\n'.join(f"- [ ] {item}" for item in improvements)
    ) + format_block(
        "## 🎯 来週のフォーカス\n" + '\n'.join(f"{idx}. {item}" for idx, item in enumerate(focus, 1))
    ) + format_block(
        "## 🙌 感謝メモ\n- チームメンバーがリリースノートのレビューを即日対応してくれた。\n- コミュニティからCursor活用の質問が届き、改善ヒントを得られた。"
    )


def generate_monthly_review(path: Path) -> str:
    ym = path.stem  # e.g. 2025-01
    year, month = map(int, ym.split('-'))
    start = date(year, month, 1)
    if month == 12:
        end = date(year + 1, 1, 1) - timedelta(days=1)
    else:
        end = date(year, month + 1, 1) - timedelta(days=1)
    outcomes = [
        "YouTubeチャンネル登録者が月次目標を105%で達成。",
        "SURVIBE AI講座の募集着地が定員に到達し、キャンセル待ちを整理。",
        "AIプロンプト集の第2版を公開し、社内の問い合わせが20%減。",
    ]
    metrics = """| 指標 | 今月 | 先月比 |
|------|------|-------|
| コンテンツ公開数 | 8本 | +2 |
| 売上(万円) | 180 | +15 |
| 学習時間 | 22h | +4 |
"""
    lessons = [
        "App Router移行に伴うデプロイ体制を早めに整える必要がある。",
        "ニュースレターの開封率が高い金曜朝に合わせて配信すると効果が良い。",
    ]
    next_focus = [
        "SURVIBE AI Week4の最終課題を改善し、評価基準をアップデート。",
        "Cursor vs Copilotの記事を深掘りし、リード獲得につなげる。",
        "ヘルスデータの可視化を自動化し、エネルギー管理の精度を上げる。",
    ]
    return format_block(
        f"""---
month: {ym}
start: {start}
end: {end}
tags: [monthly-review, {year}, {ym}]
---

# {ym} 月次レビュー

## ✅ 今月の成果
"""
    ) + '\n'.join(f"- {item}" for item in outcomes) + '\n\n' + format_block(
        "## 📈 主要指標\n" + metrics
    ) + format_block(
        "## 🧠 学び\n" + '\n'.join(f"- {item}" for item in lessons)
    ) + format_block(
        "## ⚙️ 改善タスク\n- [ ] 財務レポートの自動生成を整備\n- [ ] コミュニティイベントの運営シートを刷新"
    ) + format_block(
        "## 🎯 来月のフォーカス\n" + '\n'.join(f"{idx}. {item}" for idx, item in enumerate(next_focus, 1))
    ) + format_block(
        "## 🙏 グッドニュース\n- クライアントから継続案件の相談が2件届いた。\n- 新しい学習仲間がコミュニティに参加し、議論が活性化した。"
    )


def generate_memory_master_index() -> str:
    return format_block(
        """# 🧠 Second Brain Master Index

このインデックスは、04_Memory配下の主要ドメインを俯瞰するためのハブです。各カテゴリーのMOCと代表的なノートへ素早くアクセスできます。

## 📂 カテゴリー一覧
- [[AI/_AI-MOC]] — ツール/テクニック/コンセプト
- [[Business/_Business-MOC]] — Sales, Marketing, Operations
- [[Education/_Education-MOC]] — 学習設計と教授法
- [[Personal/_Personal-MOC]] — 健康・子育て・生産性
- [[Technical/Architecture/design-patterns]] など技術系ノート

## 🔁 更新ルール
- 月末のレビューで各MOCを更新
- 新しいノートを追加したら必ず関連MOCからリンク
- 3か月参照していないノートはArchive候補としてタグ付け

## 🧭 ナビゲーションメモ
- `#ai` や `#business` などタグ検索で横断的に探す
- Dataviewクエリで最近更新したノートを確認
- リンク切れがあればこのファイルにメモしておく
"""
    )


def generate_memory_moc(path: Path) -> str:
    parts = path.relative_to(BASE_DIR).as_posix().split('/')
    category = parts[1]
    title = {
        'AI': '🤖 AI MOC',
        'Business': '💼 Business MOC',
        'Personal': '🌱 Personal MOC',
        'Education': '📚 Education MOC',
    }.get(category, f"{category} MOC")
    sections = {
        'AI': [
            ("Tools", ["[[AI/Tools/Cursor/cursor-basics]]", "[[AI/Tools/Claude/claude-api-guide]]", "[[AI/Tools/Dify/dify-workflows]]"]),
            ("Techniques", ["[[AI/Techniques/Prompting/prompt-engineering-basics]]", "[[AI/Techniques/RAG/rag-architecture]]", "[[AI/Techniques/Agent-Development/multi-agent-systems]]"]),
            ("Concepts", ["[[AI/Concepts/llm-fundamentals]]", "[[AI/Concepts/transformer-architecture]]", "[[AI/Concepts/ai-safety]]"]),
        ],
        'Business': [
            ("Sales", ["[[Business/Sales/pricing-strategy]]", "[[Business/Sales/consultative-selling]]"]),
            ("Marketing", ["[[Business/Marketing/content-marketing-strategy]]", "[[Business/Marketing/social-media-strategy]]"]),
            ("Community & Ops", ["[[Business/Community-Building/member-retention]]", "[[Business/Operations/workflow-automation]]"]),
        ],
        'Personal': [
            ("Health", ["[[Personal/Health/stress-management]]", "[[Personal/Health/exercise-routines]]"]),
            ("Parenting", ["[[Personal/Parenting/child-development]]", "[[Personal/Parenting/balance-work-family]]"]),
            ("Productivity", ["[[Personal/Productivity/focus-techniques]]", "[[Personal/Productivity/time-management]]"]),
        ],
        'Education': [
            ("Pedagogy", ["[[Education/Pedagogy/active-learning]]", "[[Education/Pedagogy/feedback-methods]]"]),
            ("Curriculum Design", ["[[Education/Curriculum-Design/backward-design]]", "[[Education/Curriculum-Design/assessment-design]]"]),
            ("Teaching Techniques", ["[[Education/Teaching-Techniques/storytelling]]", "[[Education/Teaching-Techniques/live-coding]]"]),
        ],
    }
    body = format_block(f"# {title}\n") + "## 🔗 リンク集\n" + '\n'.join(
        f"### {section}\n" + '\n'.join(f"- {link}" for link in links)
        for section, links in sections.get(category, [])
    )
    body += "\n" + format_block(
        "## 📝 メモ\n- 月次レビューで必ず最新化する。\n- 関連タグ: #" + category.lower()
    )
    return body


def generate_memory_note(path: Path) -> str:
    rel = path.relative_to(BASE_DIR).as_posix()
    parts = rel.split('/')
    category = parts[1]
    slug = Path(rel).stem
    title = slug_to_title(slug)
    tokens = slug_tokens(slug)
    infos = [TOKEN_INFO[t] for t in tokens if t in TOKEN_INFO]
    summary = f"{title}に関する知見を整理する。"
    if infos:
        summary += " " + " ".join(info.summary for info in infos)
    else:
        summary += " 背景・重要ポイント・行動指針を短くまとめる。"
    points = MEMORY_BASE_POINTS.get(category, ["観察→気づき→改善を1セットで記録する。"])
    actions = MEMORY_BASE_ACTIONS.get(category, ["TODO化して週次で進捗確認する。"])
    for info in infos:
        points.extend(info.points)
        actions.extend(info.actions)
    # deduplicate while preserving order
    def dedup(seq: List[str]) -> List[str]:
        seen = set()
        result = []
        for item in seq:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result

    points = dedup(points)[:6]
    actions = dedup(actions)[:6]
    if not points:
        points = [f"{title}に関する基礎概念と注意点を整理する。"]
    if not actions:
        actions = ["週次レビューで関連タスクを1件以上進める。"]
    note = format_block(
        f"# {title}\n\n## 概要\n{summary}\n"
    )
    note += format_block(
        "## 重要ポイント\n" + '\n'.join(f"- {item}" for item in points)
    )
    note += format_block(
        "## 実践アクション\n" + '\n'.join(f"- [ ] {item}" for item in actions)
    )
    note += format_block(
        "## メモ\n- 更新日: " + str(date.today()) + "\n- 参照タグ: #" + category.lower()
    )
    return note
def generate_dashboard(path: Path) -> str:
    name = path.stem
    if 'HOME' in name or '🏠' in name:
        return format_block(
            """# 🏠 HOME Dashboard

**今日**:: `=date(today)`  
**週番号**:: `=this.week`  
**エネルギー**:: ☀️☀️☀️☀️☀️

## 🎯 今日のTop3
- [ ] ディープワーク: コンテンツ制作
- [ ] SURVIBE AI講座の仕込み
- [ ] 家族/メンテ作業

## ✅ 今日のタスク
```dataview
TASK
FROM "02_Daily"
WHERE !completed AND file.day = date(today)
SORT priority DESC
```

## 📚 最近の学び
```dataview
LIST file.link + " – " + choice(summary, summary, "メモなし")
FROM "04_Memory"
WHERE file.mtime >= date(today) - dur(2 days)
LIMIT 6
```

## 💧 エネルギーチェック
- 睡眠 : [ ] 7h以上
- 運動 : [ ] 有酸素または筋トレ
- 栄養 : [ ] 朝食/昼食/夕食
"""
        )
    if 'Weekly' in name or '📊' in name:
        return format_block(
            """# 📊 Weekly Dashboard

## 🗓 今週の視点
- 重点テーマ: Cursor動画 / SURVIBE演習 / プロンプト改善
- リスク: スケジュール過密、体力低下

## 📥 Inbox
```dataview
TABLE file.ctime as 追加日, length(file.tasks) as Tasks
FROM "01_Inbox"
SORT file.ctime DESC
LIMIT 15
```

## 🚀 プロジェクト状況
```dataview
TABLE progress, status
FROM "05_Output/Projects/@Active"
SORT file.name
```

## 🧠 学びログ（7日）
```dataview
LIST
FROM "04_Memory"
WHERE file.mtime >= date(today) - dur(7 days)
LIMIT 10
```
"""
        )
    if 'Analytics' in name or '📈' in name:
        return format_block(
            """# 📈 Analytics Dashboard

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
"""
        )
    if 'Projects' in name or '🎯' in name:
        return format_block(
            """# 🎯 Projects Dashboard

## アクティブ案件
```dataview
TABLE status, priority, due
FROM "05_Output/Projects/@Active"
SORT priority ASC
```

## ブロッカー
- SURVIBE AI: Week3課題の演習環境
- YouTube: EP02の撮影スタジオ確保
- 企業研修: 契約書レビュー待ち

## 次アクション
1. SURVIBE教材ドラフト共有
2. YouTube撮影日程FIX
3. 企業研修キックオフ資料送付
"""
        )
    if 'Active' in name or '🔥' in name:
        return format_block(
            """# 🔥 Active Focus Dashboard

## 集中テーマ
- Cursor上級ガイド完成
- SURVIBE Week2の演習改善
- AIツール比較記事の検証

## タイムブロック
| 時間帯 | フォーカス | 備考 |
|--------|----------|------|
| 07:00-09:00 | Script執筆 | 連続90分 |
| 10:00-12:00 | 録画/収録 | Noise対策 |
| 14:00-16:00 | ミーティング | まとめて実施 |
| 20:00-21:00 | 学習 | LLM論文 |

## ガードレール
- Slack/メールは1日3回に制限。
- 毎晩エネルギー指標を3段階で記録。
- 家族イベントは最優先で予定化。
"""
        )
    raise ValueError(f"Unknown dashboard template for {name}")


def generate_input_note(path: Path) -> str:
    name = path.stem
    if name == 'this-week-focus':
        return format_block(
            """# 今週のフォーカス

## 🎯 フラッグシップテーマ
- Cursor上級ガイドの台本確定
- SURVIBE AI Week3演習の磨き込み
- ブログ『AIツール比較』のドラフト作成

## 🗓 スプリント計画
| 日 | 午前 | 午後 | 夜 |
|----|------|------|----|
| Mon | Script執筆 | 収録準備 | 軽い学習 |
| Tue | SURVIBE演習 | クライアントMTG | 編集チェック |
| Wed | ブログ執筆 | 収録 | 家族時間 |
| Thu | 編集 | SURVIBE QA | 余白 |
| Fri | 公開作業 | 事務処理 | 週次レビュー |

## ✅ 成功条件
- 主要コンテンツを1本リリース
- SURVIBE教材の差分をGitに反映
- Inbox 10件以下を維持
"""
        )
    if name == 'this-month-goals':
        return format_block(
            """# 今月のゴール

## 🎯 成果目標
- YouTube登録者 +300人
- SURVIBE AI講座の募集を完売
- ブログ記事4本公開

## 📊 指標
| カテゴリ | 目標 | 備考 |
|----------|------|------|
| コンテンツ | 8本 | 長文4/ショート4 |
| 売上 | 180万円 | 企業研修+講座 |
| 学習 | 20時間 | 新技術インプット |

## 🛠 施策
- 週2回のライブ配信でリード獲得
- LinkedIn記事で企業研修事例を発信
- 夜間に学習時間を確保しPromptOpsを習得
"""
        )
    if name == 'hot-topic-claude-sonnet4':
        return format_block(
            """# Hot Topic: Claude Sonnet 4

## 検証ポイント
- 長文コード生成の精度向上を確認
- APIレスポンス速度とコスト試算
- Cursorとの組み合わせでのワークフロー最適化

## 調査ToDo
- [ ] SDKサンプルを動かし、トークン使用量を記録
- [ ] 既存プロンプトを移植し、差分を比較
- [ ] 懸念点と改善案をブログ草稿にまとめる

## 所感メモ
Sonnet 4は指示理解が鋭く、長文編集にも強い。Fine-grainedなChain of Thoughtを促すと安定する。"""
        )
    if name == 'hot-topic-cursor-update':
        return format_block(
            """# Hot Topic: Cursor Update

## 変更点追跡
- マルチファイルDiffのUI刷新
- Claude統合のモデル選択UI
- 新しいTeam Billing機能

## チェックリスト
- [ ] デフォルトモデル設定を確認
- [ ] スニペット/テンプレの互換性をテスト
- [ ] チームメンバーへの共有資料を作成

## 影響評価
- ワークスペース設定をテンプレ化するとオンボーディングが短縮できる。
- 料金体系が変わるため、顧客提案資料を更新する。
"""
        )
    if name == 'reference-ai-tools-comparison':
        return format_block(
            """# AIツール比較リファレンス

| ツール | 強み | 弱み | 代表用途 |
|--------|------|------|----------|
| Cursor | IDE連携とAIペアプロ | 大規模PJで負荷増 | コーディング、レビュー |
| Claude | 長文・指示理解◎ | 画像入出力は限定的 | 仕様整理、ドラフト |
| Dify | ノーコードでエージェント | サーバ管理が必要 | PoC、社内Bot |
| Windsurf | ブラウザ完結 | エコシステムは少ない | 軽量コーディング |

## 選定観点
- セキュリティ: APIキー管理 / ログ暗号化
- UX: 学習コスト / 共同編集
- コスト: 席数・従量課金・上限制御

## 次のアクション
- [ ] 4ツールで同じ課題を解かせ、所要時間と品質を比較
- [ ] クライアント資料に載せる比較チャートを作成
"""
        )
    raise ValueError(f"Unknown input note template for {name}")


def generate_template(path: Path) -> str:
    rel = path.relative_to(BASE_DIR / '06_Templates').as_posix()
    templates: Dict[str, str] = {
        'Projects/プロジェクト振り返りテンプレート.md': format_block(
            """# プロジェクト振り返りテンプレート

## 🗓 プロジェクト情報
- 期間: {{start}} ~ {{end}}
- チーム: {{members}}
- 成果物: {{deliverables}}

## ✅ 目標と結果
- 目標: 
- 結果: 
- ギャップ: 

## 🌟 良かったこと
1. 
2. 
3. 

## ⚠️ 課題
- 課題/影響/次アクションの順に記入

## 🛠 改善アイデア
- [ ] 
- [ ] 

## 📚 学び
- 技術:
- プロセス:
- コミュニケーション:
"""
        ),
        'Projects/コースカリキュラムテンプレート.md': format_block(
            """# コースカリキュラムテンプレート

## 🎯 コース概要
- タイトル: {{course_name}}
- 受講対象: {{persona}}
- 期間: {{duration}}
- 成果: {{outcome}}

## 🧭 モジュール構成
| 週 | テーマ | 目標 | 宿題 |
|----|--------|------|------|
| Week1 | | | |
| Week2 | | | |
| Week3 | | | |

## 📚 教材
- スライド: 
- ワークシート: 
- 参考資料: 

## 🔎 評価方法
- 形成評価: 
- 最終評価: 

## 🧠 メモ
- リスク: 
- サポート体制: 
"""
        ),
        'Projects/セミナー企画テンプレート.md': format_block(
            """# セミナー企画テンプレート

## 🗓 開催情報
- タイトル:
- 日時:
- 形式: オンライン/オフライン
- 参加想定人数:

## 🎯 目的
- 期待する変化:
- KPI:

## 📋 アジェンダ
| 時間 | 内容 | 担当 | メモ |
|------|------|------|------|
| 00:00 | | | |

## 💡 コンテンツポイント
- 

## 🧰 準備物
- スライド: 
- デモ: 
- 連絡テンプレ: 

## ✅ ToDo
- [ ] 集客素材作成
- [ ] 参加者リスト管理
- [ ] リマインドメール送信
"""
        ),
        'Projects/プロジェクト計画テンプレート.md': format_block(
            """# プロジェクト計画テンプレート

## 📌 情報
- プロジェクト名: 
- オーナー: 
- ステータス: planning/active/paused

## 🎯 目的とKPI
- 目的: 
- KPI: 

## 🗺 スコープ
- In Scope:
- Out of Scope:

## 🧩 タスクブレークダウン
| No | タスク | 担当 | 期日 | 状況 |
|----|--------|------|------|------|

## 🛠 リスク管理
- リスク: 
- 影響/対策:

## 📝 コミュニケーション
- 定例: 
- レポート方法: 

## ✅ 次の一歩
- [ ] 
- [ ] 
"""
        ),
        'Projects/クライアント提案テンプレート.md': format_block(
            """# クライアント提案テンプレート

## 🧾 基本情報
- クライアント: 
- 提案日: 
- 担当: 

## 🎯 課題整理
- 現状: 
- 理想状態: 
- ギャップ: 

## 💡 ソリューション
- 概要: 
- 体制: 
- スケジュール: 

## 💰 料金
| 項目 | 金額 | 備考 |
|------|------|------|

## ✅ 成功条件
- 

## 📎 添付資料
- 
"""
        ),
        'Content/ブログアウトラインテンプレート.md': format_block(
            """# ブログアウトラインテンプレート

## タイトル案

## ねらい/読者
- 読者:
- 課題:
- ゴール:

## アウトライン
1. 導入
2. 本文セクション1
3. 本文セクション2
4. まとめ/CTA

## リサーチメモ
- 参考URL:
- 引用データ:

## CTA案
- 
"""
        ),
        'Content/ブログ記事テンプレート.md': format_block(
            """# {{title}}

## 導入
- 読者の課題
- 本記事で得られる価値

## セクション1 — {{section1}}
本文

## セクション2 — {{section2}}
本文

## セクション3 — {{section3}}
本文

## まとめ
- 要点整理
- 次のアクション

## CTA
- 
"""
        ),
        'Content/SNS投稿テンプレート.md': format_block(
            """# SNS投稿テンプレート

## プラットフォーム
- Twitter / Threads / LinkedIn など

## 投稿本文
1. フック（140字以内）
2. 本文ポイント（箇条書き）
3. CTA（リンク/質問）

## ハッシュタグ
- 

## 画像/添付
- 

## 配信メモ
- 予定日時:
- 投稿後の反応: 
"""
        ),
        'Content/Xスレッドテンプレート.md': format_block(
            """# Xスレッドテンプレート

## テーマ
- 

## スレッド構成
1. フック
2. 背景
3. ポイント1
4. ポイント2
5. ポイント3
6. まとめ/CTA

## メモ
- 共有したいデータ/リンク
- 補足画像
"""
        ),
        'Content/YouTubeスクリプトテンプレート.md': format_block(
            """# YouTubeスクリプトテンプレート

## 基本情報
- タイトル: 
- 想定視聴者: 
- 目標: 登録 / リード / 教育

## 構成
1. Hook (0:00-0:20)
2. オープニング (0:20-0:45)
3. 本編パート1
4. 本編パート2
5. デモ/事例
6. まとめ & CTA

## 台本メモ
- B-roll案: 
- テロップ: 
- 注意事項: 
"""
        ),
        'Daily/デイリーTODOテンプレート.md': format_block(
            """# {{date:YYYY-MM-DD}} TODO

## 🌞 朝の準備
- [ ] エネルギーレベル記録
- [ ] 今日のTop3確認

## 🔨 作業
- [ ] Task1
- [ ] Task2
- [ ] Task3

## 🤝 連絡
- [ ] メール
- [ ] DM

## 🌙 ふりかえり
- 良かったこと:
- 改善ポイント:
"""
        ),
        'Daily/月次レビューテンプレート.md': format_block(
            """# {{date:YYYY-MM}} 月次レビュー

## ✅ 成果
- 

## 📊 指標
| KPI | 目標 | 実績 | コメント |
|-----|------|------|-----------|

## 🧠 学び
- 

## ⚙️ 改善
- [ ] 

## 🎯 来月のフォーカス
1. 
2. 
3. 
"""
        ),
        'Daily/週次レビューテンプレート.md': format_block(
            """# {{date:YYYY}}-W{{week}} 週次レビュー

## 🌟 ハイライト
- 

## 📥 Inbox状況
- 件数: 
- 特記事項: 

## 🧠 学び/気づき
- 

## 🛠 改善アクション
- [ ] 
- [ ] 

## 🎯 来週のTop3
1. 
2. 
3. 
"""
        ),
        'Meeting/ブレインストーミングセッションテンプレート.md': format_block(
            """# ブレインストーミングノート

## テーマ

## ルール
- 否定しない
- 量を出す
- アイデアの結合/発展歓迎

## 参加者
- 

## アイデアログ
- 

## 収束ステップ
- Top3候補:
- 次のアクション:
"""
        ),
        'Meeting/会議ノートテンプレート.md': format_block(
            """# 会議ノート — {{title}}

## 基本情報
- 日時: 
- 参加者: 
- 目的: 

## アジェンダ
1. 
2. 
3. 

## 議事録
- トピック:
  - 決定:
  - メモ:

## アクションアイテム
- [ ] 誰 / 何 / 期日

## 次回
- 日時候補:
- 準備物:
"""
        ),
        'Meeting/クライアント会議テンプレート.md': format_block(
            """# クライアント会議メモ

## 基本情報
- クライアント: 
- ミーティング目的: 
- ステータス: 

## 議題
1. 
2. 

## 要点
- 

## 決定事項
- 

## 宿題
- [ ] 

## フォローアップ
- メール送信日: 
- 添付資料: 
"""
        ),
        'Meeting/1on1ノートテンプレート.md': format_block(
            """# 1on1ノート — {{name}}

## 近況
- 勝ち/感謝
- 課題

## トピック
- キャリア
- スキル
- サポート

## アクション
- [ ] 
- [ ] 

## フィードバック
- ポジティブ:
- 改善:
"""
        ),
        'Knowledge/概念ノートテンプレート.md': format_block(
            """# {{concept}}

## 定義

## 重要ポイント
- 

## 例
- 

## 関連リンク
- 

## メモ
- 
"""
        ),
        'Knowledge/MOCテンプレート.md': format_block(
            """# {{title}} MOC

## サマリー

## セクション
- ### 
  - [[リンク1]]
  - [[リンク2]]

## アクション
- [ ] 次回更新日: {{date}}
"""
        ),
        'Knowledge/ツールレビューテンプレート.md': format_block(
            """# {{tool}} レビュー

## 基本情報
- カテゴリ:
- プラン:
- 導入目的:

## 良い点
- 

## 課題
- 

## 導入フロー
1. 
2. 
3. 

## 結論
- 
"""
        ),
        'Knowledge/テクニックガイドテンプレート.md': format_block(
            """# {{technique}} ガイド

## 概要

## 手順
1. 
2. 
3. 

## 注意点
- 

## 参考
- 
"""
        ),
        'Knowledge/学習ノートテンプレート.md': format_block(
            """# 学習ノート — {{topic}}

## 目的

## インプットログ
- 内容 / 日付 / 所感

## アウトプット
- 

## 次のステップ
- [ ] 
"""
        ),
    }
    if rel in templates:
        return templates[rel]
    raise ValueError(f"Unknown template for {rel}")


def generate_archive_note(path: Path) -> str:
    rel = path.relative_to(BASE_DIR / '99_Archive').as_posix()
    name = Path(rel).stem
    if rel == '_archive-workflow.md':
        return format_block(
            """# アーカイブ運用ワークフロー

## 目的
- アクティブな情報と履歴資料を切り分ける
- 後日検索できるよう最小限のメタデータを残す

## 手順
1. 月末レビューで `done` タグのノートを抽出
2. 学習価値が低ければ `99_Archive/年/` へ移動
3. Frontmatterに `archived: true` と移動日を記録
4. 重要ノートは要約を `04_Memory` にリンク

## 命名ルール
- `YYYY-MM-DD-カテゴリ.md`
- 音声/画像は `asset` フォルダにまとめ、同名ノートから参照

## メモ
- 1年経過後に更なる圧縮/削除を検討
- 機微情報は暗号化または削除ルールを別途管理
"""
        )
    if 'meeting-notes' in name:
        return format_block(
            """# 2025-01-14 Meeting Notes

## 概要
- クライアント: Studio Polaris
- テーマ: 2月ウェビナーの構成確認
- 参加: 営業2名 / 技術1名 / ファシリ1名

## 議題メモ
- オープニングを3分→5分に拡張して成果事例を追加
- 資料デモはライブではなく録画を使用する
- アンケートフォームに商談希望チェックを追加

## アクション
- [ ] 1/18までに最新版スライド共有（担当: Tech）
- [ ] 登壇者プロフィールの確認（担当: Client）
- [ ] リハーサル日程調整（担当: PM）
"""
        )
    if 'youtube-idea' in name:
        return format_block(
            """# 2025-01-13 YouTube アイデア

## コンセプト
- タイトル案: 「AIエディタCursorで1時間アプリ構築」
- ペルソナ: ノーコードからコードに挑戦したいクリエイター
- 期待成果: 新規視聴者獲得+メルマガ登録

## 構成メモ
1. Hook: Before/Afterのスピード比較
2. デモ: Cursor + ClaudeでTodoアプリ構築
3. Tips: よくある失敗例
4. CTA: 無料テンプレDL

## 次のステップ
- [ ] シナリオ初稿作成
- [ ] 画面キャプチャ撮影
- [ ] サムネイル案出し
"""
        )
    if name == 'memo-002':
        return format_block(
            """# メモ 002 — アイデア走り書き

## キーワード
- マルチエージェント
- Cursor + Claude連携
- 企業研修コンテンツ

## ラフノート
- エージェント3体で役割分担し、クライアント課題を解決するデモを作る
- Cursorのホワイトボード機能を使ったライブQA企画
- NOTE記事「AIで議事録→要約→アクション化」

## 次の一手
- [ ] 需要ヒアリング
- [ ] 技術検証
- [ ] 収益化パターン整理
"""
        )
    if 'voice-note' in name:
        return format_block(
            """# 音声メモ 2025-01-13

## トリガー
- 移動中に浮かんだ講座改善アイデア

## 書き起こしメモ
- 受講生が迷う箇所をチャットボットが即案内する仕組み
- ワーク提出→AIフィードバック→メンター最終コメントの3段階
- 収録時の声のテンポを一定に保つためのリハーサル方法

## アクション
- [ ] Botのシナリオ素案を作成
- [ ] リハ用スクリプトを10分単位で整備
"""
        )
    if 'ai-tool-idea' in name:
        return format_block(
            """# 2025-01-13 AIツール アイデア

## 背景
- クライアント向けにCursor/Claude/Difyの使い分け資料を作りたい

## アイデア
- チェックリスト式診断 → おすすめワークフローを提示
- コーディング/ドキュメント/ブレストの3カテゴリで比較
- 料金早見表 + 学習コスト評価

## 必要リサーチ
- 各ツールの最新価格
- 事例ヒアリング: 企業3社
- 既存ブログとの重複確認
"""
        )
    raise ValueError(f"Unknown archive note for {rel}")


def generate_area_personal(path: Path) -> str:
    rel = path.relative_to(BASE_DIR / '05_Output/Areas/Personal').as_posix()
    notes: Dict[str, str] = {
        'Health/exercise-log.md': format_block(
            """# エクササイズ記録

## 目的
- 週3回のトレーニングを習慣化し、体脂肪率18%を維持する。

## 週間プラン
| 曜日 | 種目 | 強度 | メモ |
|------|------|------|------|
| Mon | HIIT 20分 | 高 | 心拍150 |
| Wed | 筋トレ上半身 | 中 | 45分 |
| Fri | 5kmジョグ | 中 | 30分 |

## ケアメモ
- 起床後ストレッチ5分
- 就寝前のフォームローラー

## 振り返り
- 今週の改善点:
- 次週トライ: 
"""
        ),
        'Health/energy-tracking.md': format_block(
            """# エネルギートラッキング

## 今日の指標
- 睡眠: __h / 質 __
- 食事: ☐朝 ☐昼 ☐夜
- 水分: __L

## 体調メモ
- 体温/心拍:
- 気分:

## 観察
- トリガーとなった出来事:
- 改善アクション:

## 週次サマリー
- エネルギー平均:
- シグナル:
"""
        ),
        'Family/kids-milestones.md': format_block(
            """# 子どものマイルストーン

## プロフィール
- 名前: 
- 年齢: 
- 好きなこと: 

## 最近できたこと
- 

## 面白かった発言/行動
- 

## サポートしたいこと
- 

## 記録
| 日付 | 出来事 | 親の気づき |
|------|--------|-------------|
"""
        ),
        'Family/@TODO/family-trip-planning.md': format_block(
            """# TODO: 家族旅行計画

## 行き先候補
- 

## 日程
- 第一候補: 
- 予備日: 

## 予約タスク
- [ ] 交通手段
- [ ] 宿泊
- [ ] アクティビティ

## パッキングリスト
- 子ども用品:
- ガジェット:
- 共有書類:

## 予算
- 概算: 円
"""
        ),
        'Family/family-goals.md': format_block(
            """# ファミリーゴール

## 年間テーマ
- 

## Q1 目標
- 

## 家族イベント
- 月1回の特別な時間を記録

## 家族会議メモ
- 議題:
- 決定事項:
- 宿題:
"""
        ),
        'Self-Development/learning-goals-2025.md': format_block(
            """# 2025 学習ゴール

## 目標
- PromptOps運用を習得し、案件に適用
- システムデザイン力を磨き、研修に組み込む

## ロードマップ
| 月 | テーマ | 成果物 |
|----|--------|--------|
| 1-2月 | PromptOps | ケーススタディ |
| 3-4月 | System Design | 模擬面接対策 |

## 評価指標
- 学習時間: 20h/月
- 成果アウトプット: ブログ/動画

## サポートリソース
- 書籍/講座:
- メンター/コミュニティ:
"""
        ),
        'Self-Development/@TODO/learn-system-design.md': format_block(
            """# TODO: システムデザインを学ぶ

## 学習ステップ
- [ ] Grokking System Design 復習
- [ ] C4/ADRで手を動かす
- [ ] 模擬面接で説明練習

## インプット
- 書籍/記事: 
- 動画: 

## アウトプット
- ブログ/メモ: 
- 社内共有: 

## メモ
- 苦手ポイント:
- 対策:
"""
        ),
        'Self-Development/reading-list.md': format_block(
            """# 読書リスト

| 書名 | 著者 | ステータス | メモ |
|------|------|------------|------|
| | | 未読 | |

## リーディング計画
- 月2冊を目標にする
- 1冊につきアウトプットを1本書く

## 気づき
- 
"""
        ),
    }
    if rel in notes:
        return notes[rel]
    raise ValueError(f"Unknown personal area note for {rel}")


def generate_area_content_creation(path: Path) -> str:
    rel = path.relative_to(BASE_DIR / '05_Output/Areas/Content-Creation').as_posix()
    notes: Dict[str, str] = {
        'Blog-Writing/00-content-strategy.md': format_block(
            """# ブログコンテンツ戦略

## 目的
- AI/LLM領域の専門性を示し、案件相談とリスト獲得を両立する。

## ペルソナ
- IT企業の研修担当
- 自走したい個人クリエイター

## カテゴリ
- プロダクティビティ
- AIツール比較
- ケーススタディ

## KPI
- 月4本公開
- CTA遷移率5%以上
"""
        ),
        'Blog-Writing/@TODO/idea-cursor-vs-copilot.md': format_block(
            """# TODO: Cursor vs Copilot 記事

## 仮タイトル
- 「CursorとCopilotをどこで使い分けるか？」

## 骨子
1. 評価基準（価格/モデル/操作）
2. 具体的ワークフロー比較
3. チーム導入のポイント

## リサーチ
- 料金と利用制限
- ユーザー事例

## CTA
- ダウンロード資料 or ワークショップ案内
"""
        ),
        'Blog-Writing/@Doing/draft-ai-agent-guide.md': format_block(
            """# Draft: AI Agent Guide

## ステータス
- 章立て確定 / 事例追記中

## メモ
- エージェントの分類: シングル / マルチ / 自律
- 成功事例インタビューを引用予定

## 次タスク
- [ ] Dify実装キャプチャ撮影
- [ ] 失敗例セクションの原稿
- [ ] まとめイラスト案
"""
        ),
        'Blog-Writing/Templates/qiita-template.md': format_block(
            """# Qiita 記事テンプレ

## タイトル

## 背景
- 何に困っていたか

## 解決策
- コード/設定

## まとめ
- 学び
- 次の展開

## ハッシュタグ
- #ai #cursor など
"""
        ),
        'Blog-Writing/Templates/note-template.md': format_block(
            """# note 記事テンプレ

## イントロ
- 読者の感情に寄り添うストーリー

## 本文構成
1. 課題
2. 解決策/How to
3. 実例
4. 行動提案

## CTA
- サービス紹介 or コミュニティ招待
"""
        ),
        'Blog-Writing/@Completed/Qiita/2025/cursor-tips-2025.md': format_block(
            """# Cursor Tips 2025 — 公開メモ

## 公開情報
- URL: 
- 公開日: 2025-01-10
- 反応: LGTM __件 / コメント __件

## コンテンツ要約
- 新UIとエージェント活用術を紹介

## 改善メモ
- 次回は動画も添付する
- 画像の文字量を減らす
"""
        ),
        'Social-Media/X-Twitter/content-calendar.md': format_block(
            """# X/Twitter コンテンツカレンダー

| 日付 | テーマ | 形式 | CTA | 状況 |
|------|--------|------|-----|------|
| 1/15 | Cursorショートカット | スレッド | ブログ誘導 | draft |
| 1/18 | Claude APIログ | 単発 | YouTube誘導 | idea |

## 投稿ルール
- 週3本
- 1本はコミュニティ紹介
"""
        ),
        'Social-Media/X-Twitter/@TODO/thread-cursor-tips.md': format_block(
            """# TODO: スレッド Cursor Tips

## 構成案
1. Hook: 「Cursorだけでここまでできる」
2. ショートカット紹介
3. AI指示テンプレ
4. まとめ + CTA

## 素材
- GIFキャプチャ
- 呼び出しコマンド

## タスク
- [ ] スクリプト作成
- [ ] キャプチャ
- [ ] 投稿予約
"""
        ),
        'YouTube-Channel/00-channel-strategy.md': format_block(
            """# YouTube チャンネル戦略

## 目的
- AI×実務の実例で信頼構築
- SURVIBE講座や企業研修の導線

## コンテンツ柱
1. Cursor Tips
2. プロジェクトVlog
3. ミニ講座

## KPI
- 登録者 +300/月
- コメント10件/動画

## 運用ルール
- 週1本 + ショート
- 台本→撮影→編集→公開のリードタイム7日
"""
        ),
        'YouTube-Channel/@TODO/idea-ai-agents-explained.md': format_block(
            """# TODO: AI Agents Explained

## 企画概要
- マルチエージェントをわかりやすく紹介

## 章立て
1. エージェントとは
2. 代表的な構成
3. デモ（Dify）
4. 応用例

## 必要素材
- フローチャート
- 画面キャプチャ
"""
        ),
        'YouTube-Channel/@TODO/idea-cursor-shortcuts.md': format_block(
            """# TODO: Cursor Shortcuts Video

## 目的
- 視聴者の定着率向上

## コンテンツ
- ベスト10ショートカット
- ワークフロー紹介

## アクション
- [ ] ショートカット表を更新
- [ ] 撮影台本作成
"""
        ),
        'YouTube-Channel/@Doing/cursor-advanced-guide/script.md': format_block(
            """# Script — Cursor Advanced Guide

## 進行状況
- Hook/Section1完成
- Section2 (Automation)執筆中

## リマインド
- デモ時にAPIキーを伏せる
- 収録は土曜午前
"""
        ),
        'YouTube-Channel/@Doing/cursor-advanced-guide/notes.md': format_block(
            """# Notes — Cursor Advanced Guide

## 取材メモ
- Beta UIの差分
- Claude連携Tips

## TODO
- [ ] B-rollリスト作成
- [ ] サムネ文字決定
"""
        ),
        'YouTube-Channel/02-analytics.md': format_block(
            """# YouTube Analytics

| 指標 | 今週 | 先週比 |
|------|------|--------|
| 登録者 | 1,230 | +45 |
| 視聴時間 | 210h | +20 |
| クリック率 | 5.1% | -0.2 |

## メモ
- EP01のRetention 60%◎
- 新サムネABテスト実施予定
"""
        ),
        'YouTube-Channel/@Completed/2025/01-January/cursor-intro-video.md': format_block(
            """# Completed: Cursor Intro Video

## 公開情報
- 公開日: 2025-01-05
- URL: 
- 成果: 再生2,300 / コメント28

## 反省
- 導入が長い → 次回は30秒以内
- 字幕フォントが小さい

## 再利用
- ショート動画化予定
- メルマガで台本を配布
"""
        ),
        'YouTube-Channel/01-content-calendar.md': format_block(
            """# YouTube コンテンツカレンダー

| 週 | タイトル | 状況 | 備考 |
|----|----------|------|------|
| W02 | Cursor上級者向け | script | 収録 1/18 |
| W03 | Claude API解説 | idea | 

## メモ
- 旬のアップデートを即反映
- コラボ企画候補: ○○さん
"""
        ),
    }
    if rel in notes:
        return notes[rel]
    raise ValueError(f"Unknown content-creation note for {rel}")


def generate_area_business(path: Path) -> str:
    rel = path.relative_to(BASE_DIR / '05_Output/Areas/Business').as_posix()
    notes: Dict[str, str] = {
        'RIDE-ON-AI/@TODO/next-event-idea.md': format_block(
            """# TODO: 次回イベント企画

## テーマ案
- 「AIエージェントでナレッジ共有を高速化」

## 想定参加者
- コミュニティメンバー20名

## アジェンダ
1. 最新トレンド共有
2. ハンズオン
3. 交流

## タスク
- [ ] 会場/Zoom調整
- [ ] 集客記事
- [ ] スピーカー招致
"""
        ),
        'RIDE-ON-AI/Member-Engagement/engagement-tactics.md': format_block(
            """# エンゲージメント施策

## 目的
- 月間アクティブ率60%維持

## 施策一覧
- ウィークリーハイライト投稿
- メンター制度
- AMAセッション

## 指標
- 投稿数
- コメント数
- Slack参加率
"""
        ),
        'RIDE-ON-AI/Member-Engagement/member-journeys.md': format_block(
            """# メンバージャーニー

## フェーズ
1. Awareness
2. Onboarding
3. Growth
4. Advocate

## 接点
- ウェルカムメール
- Onboarding Call
- 月次1on1

## 改善メモ
- Onboarding資料を動画化
- 参加動機を定期的にヒアリング
"""
        ),
        'RIDE-ON-AI/Partnerships/partnership-strategy.md': format_block(
            """# パートナー戦略

## 目的
- 共同イベントと研修パッケージ拡充

## ターゲット
- AIベンダー
- コワーキング

## アクション
- [ ] 候補企業リスト
- [ ] 提案資料
- [ ] 共同LP
"""
        ),
        'RIDE-ON-AI/00-community-strategy.md': format_block(
            """# コミュニティ戦略

## Vision
- AI活用の実践知を共有し合う場を作る

## KPI
- 活動人数200
- イベント参加率40%

## プログラム
- 月次イベント
- ミニワークショップ
- メンター制度
"""
        ),
        'RIDE-ON-AI/Events/event-planning.md': format_block(
            """# イベント計画

## 開催候補
- 2/20 オンライン

## タイムライン
- 4週前: 告知
- 2週前: リマインド
- 当日: 配信

## ToDo
- [ ] スピーカー決定
- [ ] 資料テンプレ共有
- [ ] 収録テスト
"""
        ),
        'Corporate-Training/Training-Packages/cursor-training-package.md': format_block(
            """# Cursor Training Package

## 概要
- 2日集中 / 12名まで
- カリキュラム: 基礎→実践

## 料金
- 80万円〜

## モジュール
1. セットアップ
2. AI補完ワークフロー
3. チーム運用

## 付帯
- テンプレ集
- 2週間QA
"""
        ),
        'Corporate-Training/Training-Packages/ai-basics-package.md': format_block(
            """# AI Basics Package

## 対象
- 非エンジニア向け

## 目的
- LLM活用の基礎理解と社内共有

## カリキュラム
- AI概論
- Prompt設計
- 業務への応用

## KPI
- 満足度4.5/5
- 活用アイデア10件
"""
        ),
        'Corporate-Training/Training-Packages/custom-package-template.md': format_block(
            """# カスタム研修テンプレ

- 背景:
- 目的:
- 期間/回数:
- 成果物:
- 見積:
"""
        ),
        'Corporate-Training/00-service-overview.md': format_block(
            """# 企業研修サービス概要

## 提供メニュー
- ワークショップ
- 定期コンサル
- コンテンツ制作

## 価格帯
- 60万円〜

## 差別化
- 現場のAIワークフローを共創
- 伴走サポート
"""
        ),
        'Corporate-Training/@TODO/prospect-xyz-corp.md': format_block(
            """# TODO: Prospect XYZ Corp

## 状況
- 問い合わせ済み / 2月提案

## ニーズ
- 営業DX / 社内ナレッジ刷新

## タスク
- [ ] ヒアリング日程決め
- [ ] 提案骨子作成
- [ ] 見積草案
"""
        ),
        'Corporate-Training/Marketing/sales-materials.md': format_block(
            """# セールス資料管理

## 必須資料
- 会社紹介
- 研修メニュー一覧
- 事例スライド

## TODO
- [ ] 価格表アップデート
- [ ] 2024事例追記
"""
        ),
        'Corporate-Training/Client-List/clients-database.md': format_block(
            """# クライアントDB

| 企業 | 担当 | プラン | ステータス |
|------|------|-------|-----------|
| | | | |

## メモ
- NDA状況
- 継続契約タイミング
"""
        ),
        'Survibe-AI-Baib-Coding-School/Curriculum/core-curriculum.md': format_block(
            """# Core Curriculum

## モジュール
1. Cursor
2. Promptエンジニアリング
3. Dify
4. 最終課題

## 改訂メモ
- Week3演習を刷新する
"""
        ),
        'Survibe-AI-Baib-Coding-School/@TODO/marketing-campaign-q2.md': format_block(
            """# TODO: Q2 マーケキャンペーン

## 目標
- リード100件

## 施策
- ウェビナー
- メルマガシリーズ
- コラボ記事

## タスク
- [ ] ペルソナ整理
- [ ] LP更新
"""
        ),
        'Survibe-AI-Baib-Coding-School/@TODO/new-curriculum-dev.md': format_block(
            """# TODO: 新カリキュラム開発

## 目的
- 企業研修向けモジュール追加

## ステップ
- [ ] 要件ヒアリング
- [ ] シラバス案
- [ ] プロトタイプ
"""
        ),
        'Survibe-AI-Baib-Coding-School/Operations/workflows.md': format_block(
            """# Operations Workflow

## 主なプロセス
- 受講申込〜請求
- 講師アサイン
- 受講サポート

## 自動化候補
- メールテンプレ送信
- 受講状況ダッシュボード
"""
        ),
        'Survibe-AI-Baib-Coding-School/Operations/tools-systems.md': format_block(
            """# 業務ツール一覧

| カテゴリ | ツール | 用途 |
|----------|--------|------|
| CRM | HubSpot | 営業管理 |
| LMS | Teachable | コンテンツ配信 |

## TODO
- [ ] API連携整理
"""
        ),
        'Survibe-AI-Baib-Coding-School/Marketing/marketing-strategy.md': format_block(
            """# マーケティング戦略

## ペルソナ
- 企業研修担当
- キャリアチェンジ希望者

## チャネル
- メルマガ
- コミュニティ
- YouTube

## KPI
- リード/月 120
- CVR 8%
"""
        ),
        'Survibe-AI-Baib-Coding-School/00-business-model.md': format_block(
            """# ビジネスモデル

## 収益源
- 受講料
- 企業研修
- コンテンツ販売

## コスト
- 講師
- プラットフォーム
- マーケ

## 成功要因
- 実務に寄り添う教材
- コミュニティサポート
"""
        ),
        'Survibe-AI-Baib-Coding-School/Student-Management/alumni-network.md': format_block(
            """# 卒業生ネットワーク

## 現状
- Slackコミュニティ 120名

## 施策
- 毎月オンラインMeetup
- 就職サポートチャンネル

## TODO
- [ ] メンター制度ローンチ
"""
        ),
        'Survibe-AI-Baib-Coding-School/Student-Management/onboarding-process.md': format_block(
            """# オンボーディングプロセス

## ステップ
1. 申込確認
2. オリエン動画送付
3. 初回1on1

## チェックリスト
- [ ] Slack招待
- [ ] LMSアカウント
- [ ] 教材セット送付
"""
        ),
        'Survibe-AI-Baib-Coding-School/Student-Management/support-system.md': format_block(
            """# サポート体制

## 連絡手段
- Slack質問ch
- 週次オフィスアワー

## SLA
- 平日24h以内返信

## 改善案
- ナレッジベース化
- AIボット導入
"""
        ),
        'Survibe-AI-Baib-Coding-School/01-vision-mission.md': format_block(
            """# Vision / Mission

## Vision
- 実務で使えるAIスキルを誰もが持てる社会

## Mission
- 体験型カリキュラムで実践力を育てる

## バリュー
- Hands-on
- Community
- Transparency
"""
        ),
    }
    if rel in notes:
        return notes[rel]
    raise ValueError(f"Unknown business area note for {rel}")


def generate_project_note(path: Path) -> str:
    rel = path.relative_to(BASE_DIR / '05_Output/Projects').as_posix()
    notes: Dict[str, str] = {
        '@Active/SURVIBE-AI-Dec2025/00-project-overview.md': format_block(
            """# SURVIBE AI Dec 2025 — Overview

## 目的
- 第5期12月コホートを成功させる

## スコープ
- 4週間カリキュラム
- 受講生40名
- メンター3名配置

## KPI
- 満足度4.6/5
- 卒業率95%

## 現状
- カリキュラム60%完成
- 登壇者調整中
"""
        ),
        '@Active/SURVIBE-AI-Dec2025/01-planning/requirements.md': format_block(
            """# 要件定義

## 受講者像
- 業務でAIを使い始めたエンジニア

## 成果
- 最終発表資料+実装

## 制約
- 平日夜のみ
- オンライン

## メモ
- LMSログイン体験を改善
"""
        ),
        '@Active/SURVIBE-AI-Dec2025/01-planning/stakeholders.md': format_block(
            """# ステークホルダー

| 役割 | 名前 | メモ |
|------|------|------|
| プロデューサー | | |
| メンター | | |
| クライアント | | |

## コミュニケーション
- 週次MTG
- Slackチャンネル
"""
        ),
        '@Active/SURVIBE-AI-Dec2025/01-planning/timeline.md': format_block(
            """# タイムライン

| 週 | マイルストーン |
|----|---------------|
| W-6 | 募集開始 |
| W-4 | カリキュラムFIX |
| W0 | 開講 |
| W4 | Demo Day |

## リスク
- 登壇者調整
- プロダクトアップデート
"""
        ),
        '@Active/SURVIBE-AI-Dec2025/02-curriculum/week1-cursor-basics.md': format_block(
            """# Week1 — Cursor Basics

## 目標
- Cursorの環境構築と基本操作を習得

## セッション
1. オリエン + IDE設定
2. AI補完の活用
3. ハンズオン演習

## 宿題
- プロジェクト作成
- AIログを記録

## 改善メモ
- 動画教材を追加
"""
        ),
        '@Active/SURVIBE-AI-Dec2025/02-curriculum/week2-dify-agents.md': format_block(
            """# Week2 — Dify Agents

## 目標
- Difyでエージェントを構築し、ワークフロー化する

## 内容
- GUIでのFlow作成
- API連携
- トラブルシュート

## 宿題
- 自社の業務を題材にBotを作る
"""
        ),
        '@Active/SURVIBE-AI-Dec2025/02-curriculum/week3-prompting.md': format_block(
            """# Week3 — Prompting

## 目標
- プロンプト設計と評価を実践

## セクション
- Prompt基礎
- Few-shot＋評価
- PromptOps

## 宿題
- 3パターンのプロンプト比較
"""
        ),
        '@Active/SURVIBE-AI-Dec2025/02-curriculum/week4-final-project.md': format_block(
            """# Week4 — Final Project

## 目標
- 個人/チームでAIプロダクトを仕上げる

## プロセス
- アイデア相談
- 開発サポート
- Demo Day

## 評価
- 価値 / 実装 / プレゼン
"""
        ),
        '@Active/SURVIBE-AI-Dec2025/05-review-feedback/student-feedback.md': format_block(
            """# 受講生フィードバック

| 質問 | 平均 | コメント |
|------|------|----------|
| 全体満足度 | | |
| カリキュラム難易度 | | |

## メモ
- 
"""
        ),
        '@Active/SURVIBE-AI-Dec2025/05-review-feedback/improvements.md': format_block(
            """# 改善点

## 優先度A
- Week2資料のアップデート

## 優先度B
- AMA時間延長

## アクション
- [ ] カリキュラム会議
"""
        ),
        '@Active/Corporate-Training-ABC-Corp/00-client-brief.md': format_block(
            """# Client Brief — ABC Corp

## 背景
- カスタマーサクセス部向けAI研修

## 目標
- 問い合わせ対応の効率化

## 参加者
- 25名 / オンライン

## 期待成果
- マクロ＋LLM活用シナリオ
"""
        ),
        '@Active/YouTube-Cursor-Series/00-series-plan.md': format_block(
            """# YouTube Cursor Series Plan

## エピソード
- EP01: Intro
- EP02: Basic Features
- EP03: Advanced Tips
- EP04: Real-world Demo

## スケジュール
- 週1公開

## KPI
- 再生数10k/本
"""
        ),
        '@Active/YouTube-Cursor-Series/01-scripts/ep01-intro-to-cursor.md': format_block(
            """# Script EP01 — Intro to Cursor

## 目的
- Cursorの魅力を短時間で伝える

## 構成
1. Hook
2. IDE比較
3. デモ
4. CTA

## メモ
- 収録日: 
"""
        ),
        '@Active/YouTube-Cursor-Series/01-scripts/ep02-basic-features.md': format_block(
            """# Script EP02 — Basic Features

## トピック
- AIチャット
- Diffビュー
- ターミナル連携

## TODO
- [ ] デモ用レポ作成
"""
        ),
        '@Active/YouTube-Cursor-Series/01-scripts/ep03-advanced-tips.md': format_block(
            """# Script EP03 — Advanced Tips

## ハイライト
- プロンプトチェーン
- 自動リファクタ

## メモ
- 成功パターンの比較表を挿入
"""
        ),
        '@Active/YouTube-Cursor-Series/01-scripts/ep04-real-world-demo.md': format_block(
            """# Script EP04 — Real-world Demo

## 内容
- Todoアプリをゼロから構築

## セクション
1. セットアップ
2. 機能追加
3. テスト

## 留意点
- 画面切替のタイミング
"""
        ),
        '@Active/YouTube-Cursor-Series/03-editing/ep01-edit-notes.md': format_block(
            """# Editing Notes — EP01

## 編集チェック
- BGM音量 -5db
- 字幕フォント14pt

## 修正
- 0:45 カット
- 2:10 テロップ追加
"""
        ),
        '@Active/YouTube-Cursor-Series/04-published/ep01-analytics.md': format_block(
            """# EP01 Analytics

## 公開日
- 2025-01-07

## 数値
- 再生: 5,400
- CTR: 6.2%
- Retention: 58%

## 学び
- サムネ成功
- CTA位置を前倒ししたい
"""
        ),
        '@Planning/new-course-idea.md': format_block(
            """# 新コースアイデア

## コンセプト
- 「AIオペレーション実践講座」

## 受講者
- 事業会社のDX担当

## 草案
- 4週間 / ケーススタディ中心

## 次ステップ
- [ ] 競合調査
- [ ] サーベイ
"""
        ),
        '@Planning/youtube-series-prompting.md': format_block(
            """# YouTube Prompting Series

## 目的
- Prompt設計ノウハウを体系化

## エピソード案
- プロンプト基礎
- Few-shot
- 評価と改善

## タスク
- [ ] 台本構成
- [ ] サムネ案
"""
        ),
    }
    if rel in notes:
        return notes[rel]
    raise ValueError(f"Unknown project note for {rel}")
if __name__ == '__main__':
    main()
