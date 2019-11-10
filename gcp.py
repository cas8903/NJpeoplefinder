"""
gcp.py
Used for communicating with Google's language processing API
"""

from google.cloud import language
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:\\Users\\Connor\\PycharmProjects\\Subreddit_Analitics-9c6cd7fe0223.json"


def gather_sentiment(text):
    client = language.Client()
    document = client.document_from_text(text)

    """
    Queries sentiment and sentiment magnitude. The sentiment is scored between -1 and +1, and the sentiment magnitude is
    unbounded, from 0 onward. Sentiment is the emotion, and the magnitude is the strength of that emotion.
    """
    sent_analysis = document.analyze_sentiment()
    dir(sent_analysis)
    sentiment = sent_analysis.sentiment

    """
    Entity analysis. Returns a list on entities from the given string. Each on of the entities contains data about its
    name, type, and other metadata that google calculates
    """
    ent_analysis = document.analyze_entities()
    dir(ent_analysis)
    entities = ent_analysis.entities

    return sentiment.score, sentiment.magnitude


def main():
    gather_sentiment("This is a sample statement.")


if __name__ == "__main__":
    main()
