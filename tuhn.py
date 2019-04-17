#Import library essentials
from sumy.parsers.plaintext import PlaintextParser #We're choosing a plaintext parser here, other parsers available for HTML etc.
from sumy.nlp.tokenizers import Tokenizer 
from sumy.summarizers.luhn import LuhnSummarizer 

file = "plain_text.txt" #name of the plain-text file
parser = PlaintextParser.from_file(file, Tokenizer("english"))
summarizer_luhn = LuhnSummarizer()

summary = summarizer_luhn(parser.document,2)
for sentence in summary:
    print sentence
   
