#USING LSA
#Based on term frequency techniques with singular value decomposition to summarize texts.
from sumy.parsers.plaintext import PlaintextParser #We're choosing a plaintext parser here, other parsers available for HTML etc.
from sumy.nlp.tokenizers import Tokenizer 
from sumy.summarizers.lsa import LsaSummarizer

file = "plain_text.txt" #name of the plain-text file
parser = PlaintextParser.from_file(file, Tokenizer("english"))
summarizer_lsa = LsaSummarizer()
summary_2 =summarizer_lsa(parser.document,2)
for sentence in summary_2:
    print(sentence)
