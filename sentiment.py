import time
import pandas as pd
from nltk.tokenize import sent_tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def labeling_Sentiment(df1):
    analyzer = SentimentIntensityAnalyzer()
    Positive = []
    Negative = []
    Netural = []
    positive = 0
    negative = 0
    netural = 0
    paragraph = []
    for i in df1.text:
        paragraph.append(str(i))
        sentence = sent_tokenize(str(i))
        for j in sentence:

            score = analyzer.polarity_scores(str(j))
            max_key = max(score, key=score.get)
            if max_key == 'neg':
                negative = negative + 1
            elif max_key == 'neu':
                netural = netural + 1
            elif max_key == 'pos':
                positive = positive + 1
        Positive.append(positive)
        Negative.append(negative)
        Netural.append(netural)
        positive = 0
        negative = 0
        netural = 0

    data = [paragraph, Positive, Negative, Netural]
    df1 = pd.DataFrame(data, index=['text', 'Positive', 'Negative', 'Neutral'])
    tdf = df1.T
    dfs = tdf
    df1 = pd.DataFrame(dfs)
    return df1


start = time.process_time()
df = pd.read_excel('usa.xlsx', engine='openpyxl')
print(df)


def main():
    dfc = labeling_Sentiment(df)
    data = [df['title'], df['author'], df['country'], df['text'], dfc['Positive'], dfc['Negative'], dfc['Neutral']]
    ds = pd.DataFrame(data, index=['title', 'Author', 'Country', 'Text', 'Positive', 'Negative', 'Neutral'])
    ds1 = ds.T
    ds1.to_excel("Ebeded.xlsx", header=True)


if __name__ == "__main__":
    main()

print(time.process_time() - start)
