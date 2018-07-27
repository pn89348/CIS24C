from flask import Flask, render_template, request, redirect
app = Flask(__name__)
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

def sentiment_score(text):
    '''This function inputs some text and returns the sentiment score (between -1 to 1)'''
    text = str(text)
    sentiment_analyzer = SentimentIntensityAnalyzer()
    sentiment_dict = sentiment_analyzer.polarity_scores(text)
    return str(sentiment_dict['compound'])

@app.route("/", methods=['GET', 'POST'])
def index():
        text_inputs=""
        text_outputs=""
        if request.method == 'POST':
                text_inputs=request.form["text_area"]
        print(text_inputs)
        score = sentiment_score(text_inputs)
        return render_template('index.html', text_input=text_inputs, text_output=score)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=80, debug=True)