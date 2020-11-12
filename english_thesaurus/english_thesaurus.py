import json
from difflib import get_close_matches


class EnglishThesaurus:
    def load_data(self):
        self.data = json.load(open("english_thesaurus/data.json"))

    def translate(self, w):
        if w in self.data:
            return self.data[w]
        elif w.title() in self.data:
            return self.data[w.title()]
        elif w.upper() in self.data:  # in case user enters words like USA or NATO
            return self.data[w.upper()]

        closest_matches = get_close_matches(w, self.data.keys())
        if len(closest_matches) > 0:
            yn = input("Did you mean '{}'? [y/n]: ".format(closest_matches[0])).lower()
            if yn == "y":
                return self.data[closest_matches[0]]
            else:
                return "The word '{}' doesn't exist.".format(w)
        else:
            return "The word '{}' doesn't exist.".format(w)

    def interface(self):
        self.load_data()
        word = input("Enter word: ").lower()
        output = self.translate(word)
        if type(output) == list:
            for item in output:
                print(item)
        else:
            print(output)
