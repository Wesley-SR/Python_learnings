class Tokenizer:
    """Tokenize text"""
    def __init__(self, text):
        print('Start Tokenizer.__init__()')
        self.tokens = text.split()
        print('End Tokenizer.__init__()')


class WordCounter(Tokenizer):
    """Count words in text"""
    def __init__(self, text, name_class):
        print('Start WordCounter.__init__()')
        super().__init__(text)
        self.word_count = len(self.tokens)
        self.name_class = name_class
        print('End WordCounter.__init__()')


class Vocabulary(Tokenizer):
    """Find unique words in text"""
    def __init__(self, text, class_age):
        print('Start init Vocabulary.__init__()')
        super().__init__(text)
        self.vocab = set(self.tokens)
        self.class_age = class_age
        print('End init Vocabulary.__init__()')


class TextDescriber(WordCounter):
    """Describe text with multiple metrics"""
    def __init__(self, text, name_class):
        print('Start init TextDescriber.__init__()')
        super().__init__(text, name_class)


        print('End init TextDescriber.__init__()')
    def print_all():
        print("Name class: {}".format(self.name_class))
        print("Class_age: {}".format(self.class_age))


td = TextDescriber('row row row your boat', 'Nome_classe')
print('--------')
print(td.tokens)
# print(td.vocab)
print(td.word_count)