from flask import Flask, render_template, request
from main import clean_text, tokenize_and_remove_stopwords, emotion_analysis, sentiment_analysis, plot_emotion_graph, stop_words
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def analyze_text():
    if request.method == 'POST':
        text = request.form['text']

        cleaned_text = clean_text(text)
        stop_words_list = stop_words()
        final_words = tokenize_and_remove_stopwords(cleaned_text, stop_words_list)

        emotions_file = 'emotions.txt'
        emotion_list = emotion_analysis(final_words, emotions_file)

        positive_words = [
            'happy', 'joyful', 'excellent', 'wonderful', 'fantastic', 'amazing', 'outstanding',
            'great', 'superb', 'awesome', 'delightful', 'pleased', 'terrific', 'splendid',
            'love', 'good', 'beautiful', 'brilliant', 'charming', 'exciting',
            'positive', 'vibrant', 'uplifting', 'admirable', 'refreshing', 'praiseworthy'
        ]

        negative_words = [
            'sad', 'angry', 'poor', 'awful', 'terrible', 'bad', 'dismal', 'dreadful',
            'unpleasant', 'annoying', 'frustrated', 'miserable', 'gloomy',
            'inferior', 'hate', 'dislike', 'ugly', 'boring', 'disappointing',
            'negative', 'disturbing', 'irritating', 'depressing', 'horrifying', 'displeasing'
        ]

        sentiment = sentiment_analysis(final_words, positive_words, negative_words)
        plot_image = plot_emotion_graph(emotion_list)

        return render_template('index.html', text=text, sentiment=sentiment, plot_image=plot_image)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

application = app
