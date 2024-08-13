"""Executing this module initiates the application of emotion prediction
to be executed over the Flask channel and deployed on
localhost:8000."""

from flask import Flask, render_template, request
from emotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_analyzer():
    """This endpoint receives text from the HTML interface and
    runs emotion detection over it using the emotion_detector
    function. The output returned shows the expression's
    score for the provided text."""
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    keys = list(response.keys())
    if response.get("dominant_emotion") is None:
        return "Invalid text! Please try again"

    return (f"For the given statement, the system response is {keys[0]}: {response[keys[0]]}, "
            f"{keys[1]}: {response[keys[1]]}, {keys[2]}: {response[keys[2]]}, "
            f"{keys[3]}: {response[keys[3]]} and {keys[4]}: {response[keys[4]]}. "
            f"The dominant emotion is {response['dominant_emotion']}")

@app.route("/")
def render_index_page():
    """Render the main application page."""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
