import string
from collections import Counter
import matplotlib.pyplot as plt

def clean_text(text):
    # Convert the text to lowercase for case-insensitive matching
    lower_case_text = text.lower()
    # Remove punctuations
    cleaned_text = lower_case_text.translate(str.maketrans('', '', string.punctuation))
    return cleaned_text

def tokenize_and_remove_stopwords(cleaned_text, stop_words):
    # Tokenization (Splitting text into a list of words)
    tokenized_text = cleaned_text.split()
    # Removing stop words from the tokenized words list
    final_words = [word for word in tokenized_text if word not in stop_words]
    return final_words

def emotion_analysis(final_words, emotions_file):
    emotion_list = []
    with open(emotions_file, 'r') as file:
        for line in file:
            clear_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
            word, emotion = clear_line.split(':')
            # Checking for emotions in the final words
            if word in final_words:
                emotion_list.append(emotion)
    return emotion_list

def sentiment_analysis(text, positive_words, negative_words):

    # Count the number of positive and negative words
    positive_count = sum(1 for word in text if word in positive_words)
    negative_count = sum(1 for word in text if word in negative_words)

    # Determine sentiment based on the word counts
    if positive_count > negative_count:
        sentiment = 'Positive'
    elif positive_count < negative_count:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return sentiment


def plot_emotion_graph(emotion_list):
    count_emotions = Counter(emotion_list)

    # Plotting the emotions on the graph
    fig, ax1 = plt.subplots()
    ax1.bar(count_emotions.keys(), count_emotions.values())
    fig.autofmt_xdate()

    # Save the plot to the static folder
    plot_image = 'static/emotion_graph.png'
    plt.savefig(plot_image)
    plt.close()  # Close the plot to prevent it from being displayed in the console

    return plot_image


def stop_words() :
    words=["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                      "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
                      "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
                      "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
                      "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
                      "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
                      "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
                      "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
                      "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
                      "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    return words


