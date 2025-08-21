import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
class Processor:
    def __init__(self,data:[]):
        self.data = data
        self.words = []

    def rarest_word(self):
        word_quantity={}
        for i in self.words:
            if i not in word_quantity:
                word_quantity[i] = 1
            else:
                word_quantity[i] += 1
        for i in word_quantity:
            if word_quantity[i] == 1:
                return i

    def weapons_detected(self):
        weapon_list = self._weapon_list()
        for word in self.words:
            if word in weapon_list:
                return word
        return ""

    def _weapon_list(self):
        with open("C:/Users/user1/PycharmProjects/PythonProject/Malicious-text/data/weapon_list.txt","r") as weapons:
            return weapons.read().splitlines()

    def sentiment(self,data):
        score = SentimentIntensityAnalyzer().polarity_scores(data)
        max_sentiment = None
        for i in score:
            if max_sentiment == None:
                max_sentiment = i
            elif score[i] > score[max_sentiment]:
                max_sentiment = i
        return max_sentiment

    def manager(self):
        for item in self.data:
            self.words = item['Text'].split()
            item["rarest_word"] = self.rarest_word()
            item["sentiment"] = self.sentiment(item['Text'])
            item["weapons_detected"] = self.weapons_detected()
        return self.data



