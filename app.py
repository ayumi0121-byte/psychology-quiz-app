import random

from flask import Flask, request

app = Flask(__name__)

questions = [
    {
        "field": "A領域",
        "category": "1 原理・研究法・歴史",
        "question": "形式科学と経験科学という二分法に基づくと、心理学はどちらに属するか？",
        "answer": ["経験科学"]
    },
    {
        "field": "A領域",
        "category": "1 原理・研究法・歴史",
        "question": "実験的研究において、実験者が直接に操作を加える変数をなんと呼ぶか。",
        "answer": ["独立変数"]
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

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "GET":
        question = random.choice(questions)

    else:
        question_text = request.form.get("question")

        if question_text is None:
            question = random.choice(questions)
        else:
            question = next(
                q for q in questions
                if q["question"] == question_text
            )

        user_answer = request.form.get("answer", "")

        if user_answer in question["answer"]:
            result = "⭕ 正解！"
        else:
            result = f"❌ 不正解！ 正解は {'、'.join(question['answer'])}"

    return f"""
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>

    <body>
        <h1>心理学検定アプリ</h1>

        <p>{question["field"]}</p>
        <p>{question["category"]}</p>

        <h2>{question["question"]}</h2>

       <form method="POST">
    <input type="hidden" name="question" value="{question['question']}">
    <input type="text" name="answer" placeholder="答えを入力">
    <button type="submit">回答する</button>
</form>

<h3>{result}</h3>

<form method="GET">
    <button type="submit">次の問題</button>
</form>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)