import ssl
import nltk
from nltk.corpus import words

try: 
    _create_unverified_https_context = _create_unverified_https_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

def get_words():
    nltk.download('words')
    word_list = words.words()
    return word_list



if __name__ == "__main__":
    external_words = get_words()
    print(external_words)
    print (word_list)

 