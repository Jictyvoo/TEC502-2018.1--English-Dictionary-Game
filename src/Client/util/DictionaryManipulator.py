class DictionaryManipulator:

    def __init__(self):
        self.__dict = {}
        with open("./en_US.dic", 'r') as content_file:
            count = 0
            for line in content_file.readlines():
                words = line.split("/")
                if len(words) > 1:
                    self.__dict[words[0].lower()] = count  # words[1].replace("\n", "")
                else:
                    self.__dict[line.replace("\n", "")] = count  # None
                count += 1

    def words_exist(self, word):
        return word in self.__dict.keys()

    def add_word_into_dictionary(self, word, speech=None):
        if word:
            self.__dict[word] = speech
