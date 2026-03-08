from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob

app = FastAPI()

class SentimentRequest(BaseModel):
    sentences: list[str]

def classify_sentiment(text: str) -> str:
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0.1:
        return "happy"
    elif polarity < -0.1:
        return "sad"
    else:
        return "neutral"

@app.post("/sentiment")
def sentiment_analysis(request: SentimentRequest):
    results = []
    for sentence in request.sentences:
        sentiment = classify_sentiment(sentence)
        results.append({"sentence": sentence, "sentiment": sentiment})
    return {"results": results}