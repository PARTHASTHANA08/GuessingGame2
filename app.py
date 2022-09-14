from flask import Flask,render_template,jsonify,request
import random

app = Flask(__name__)

answer = {
    "1" : ["avengers"],
    "2" : ["football"],
    "3" : ["india"]
    }
quizes = [
   {
      "input" : 8,
      "category":"Marvel",
      "word":"avengers"
   },
   {
      "input":8,
      "category":"Sports",
      "word":"football"
   },
   {
      "input":5,
      "category":"Country",
      "word":"india"
   }
]
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-quiz")
def get_story():
    return jsonify({
        "status": "success",
        "quiz": random.choice(quizes)
    })

@app.route("/post-answers", methods=["POST"])
def post_answers():
    story_id = request.json.get("story_id")
    values = request.json.get("values")
    answers = answer.get(story_id)
    index, score = 0, 0
    while index < len(values):
        if values[index].lower() == answers[index].lower():
            score += 1
        index += 1
    return jsonify({
        "status": "success",
        "result": f"{score} / {len(values)}"
    })

if __name__ == "__main__":
    app.run(debug=True)