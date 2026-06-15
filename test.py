import random

questions = [
   #1 原理・研究法・歴史
    {
        "field": "A領域",
        "category": "1 原理・研究法・歴史",
        "question": "形式科学と経験科学という二分法に基づくと、心理学はどちらに属するか？",
        "answer": ["経験科学"],
        
    },

     {
        "field": "A領域",
        "category": "1 原理・研究法・歴史",
        "question": "日本の図書館で広く用いられている日本十数分類法において、心理学が属する類は、哲学、歴史、社会科学、自然科学のうちどれか。",
        "answer": ["哲学"]  
    },

     {
        "field": "A領域",
        "category": "1 原理・研究法・歴史",
        "question": "「心理学の過去は長いが歴史は短い」と表現して、心を研究しようとしての古くからの取り組みと、自然科学の影響を受けつつ学問として成立した心理学とを区別する視点を提供したドイツの心理学者は誰か。",
        "answer": ["エビングハウス"]
    },

    {
        "field": "A領域",
        "category": "1 原理・研究法・歴史",
        "question": "個性記述的な精神科学がめざすのは理解であることに対して、法則定立的な自然科学としての心理学がめざすのは何であると考えられているか。",
        "answer": ["説明"]
    },

    {
        "field": "A領域",
        "category": "1 原理・研究法・歴史",
        "question": "心理学でしばしば用いられる、法律定立的な立場から、一般的な法則から導かれた仮説について実証的に検証する研究手法をなんと呼ぶか。",
        "answer": ["仮説演繹法"]
    },

     {
        "field": "A領域",
        "category": "1 原理・研究法・歴史",
        "question": "インタビューを書き起こしたもののように、少なくともそのままでは量として集計しての分析ができないデータについて論じて示唆を得る研究を、量的研究に対してなんと呼ぶか、",
        "answer": ["質的研究"] 
    },

    {
         "field": "A領域",
         "category": "1 原理・研究法・歴史",
         "question": "ヒトを含む生物がある機能を持つ理由への問いに対する答え方の次元が整理された、ティンバーゲン（Tinbergen,N)の「4つのなぜ」は、至近要員、突極要因、発達要員ともう一つは何か。",
         "answer": ["系統進化要員", "系統発生"]
  },

  {
         "field": "A領域",
         "category": "1 原理・研究法・歴史",
         "question": "心理学の実証研究を、実験的研究と相観的研究徒に分ける場合、変数に対する何の有無を基準として分けるか。",
         "answer": ["操作"]
  },

   {
         "field": "A領域",
         "category": "1 原理・研究法・歴史",
         "question": "分析モデルの観点からは、壮観的研究は共分散構造モデルに対応するのに対して、実験的研究はどのようなモデルに対応すると考えられるか。",
         "answer": ["因果モデル"]
  },
#010
   {
         "field": "A領域",
         "category": "1 原理・研究法・歴史",
         "question": "実験的研究において、実験者が直接に操作を加える変数をなんと呼ぶか。",
         "answer": ["独立変数"]
  },

]

# クイズの問題をシャッフルしてみましょう。
random.shuffle(questions)

# クイズの問題を10問選んでみましょう。
selected_questions = random.sample(
    questions,
    min(10, len(questions))
)

# ↓最後に、クイズを実行するコードを書いてみましょう。
score = 0

for i, q in enumerate(selected_questions, start=1):
    print(f"\n問題 {i} / {len(selected_questions)}")
    print("\n================")
    print(q["field"])
    print(q["category"])
    print("================")

    print("問題：" + q["question"])

    user_answer = input("答え：")

    if user_answer in q["answer"]:
      print("正解！")
      score += 1
    else:
      print("不正解...")
      print("正解は", "、".join(q["answer"]), "です")

print("\n================")
print("結果")
print(score, "問正解 /", len(selected_questions), "問中")
print("================")