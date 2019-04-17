#USING LSA
## Alternative Method using stopwords
from sumy.summarizers.lsa import LsaSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer 
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
summarizer_lsa2 = LsaSummarizer()
summarizer_lsa2 = LsaSummarizer(Stemmer("english"))
summarizer_lsa2.stop_words = get_stop_words("english")

file = "plain_text.txt" #name of the plain-text file
parser = PlaintextParser.from_file(file, Tokenizer("english"))
for sentence in summarizer_lsa2(parser.document,2):
    print(sentence)
