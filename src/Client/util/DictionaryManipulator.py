class DictionaryManipulator:

    def __init__(self):
        self.__dict = {}
        with open("../en_US.dic", 'r') as content_file:
            for line in content_file.readlines():
                words = line.split("/")
                if len(words) > 1:
                    self.__dict[words[0].lower()] = words[1].replace("\n", "")
                else:
                    self.__dict[line.replace("\n", "")] = None

    def words_exist(self, word):
        return word in self.__dict.keys()

    def add_word_into_dictionary(self, word, speech=None):
        if word:
            self.__dict[word] = speech
