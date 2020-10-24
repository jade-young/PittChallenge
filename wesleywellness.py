# pitt challenge
# Project - Intelligient Assistant for General Health
# mom can we get webmd? we have webmd at home webmd at home: WesleyWellness

# waits for greeting "Good morning, Wesley!"
# introduction
# how are you feeling today?
# starts interaction
"""
Wesley sorts the response into groups
follow up on previously identified patterns (how far back?)
if user only reports symptoms, for example, Wesley inquires about emotions
engage appropriately with emotion
    ex. stressed: "would you like to do a breathing exercise?"
"""
# logs interaction


class Emotions:
    def __init__(self):
        self.emotions_dict = {'sad': ['sad', 'depressed', 'upset', 'desperate', 'angry', 'disgusted', 'frustrated',
                  'jealous','betrayed', 'abused', 'rejected'], 'stressed': ['stressed', 'panic', 'uncomfortable', 'unsure','stuck','desperate','frozen','hurt'], 
                  'happy': ['happy', 'great', 'amused', 'excited', 'glad','delighted','pleased','charmed',
                    'grateful','optimistic','content','joyful','loving','loved','secure','strong','brave',
                    'prepared','relaxed','comforted'],
            'tired': ['bored', 'depressed', 'drained', 'tired','dejected', 'dull', 'fatigued', 'burn', 'burned', 'burnt'],
            'energized': ['strong', 'strengthened', 'motivated', 'focused', 'invigorated', 'determined', 'energized',
                        'inspired']
        }

        self.emotions_list = ['strong', 'strengthened', 'motivated', 'focused', 'invigorated', 'determined', 'energized', 'inspired',
            'great', 'bored', 'depressed', 'drained', 'tired','dejected', 'dull', 'fatigued', 'burn', 'burned', 'burnt',
            'happy', 'great', 'amused', 'excited', 'glad', 'delighted', 'pleased', 'charmed', 'grateful', 'optimistic',
            'content', 'joyful', 'loving', 'loved', 'secure', 'strong', 'brave', 'prepared', 'relaxed', 'comforted',
            'stressed', 'panic', 'uncomfortable', 'unsure','stuck','desperate','frozen','hurt','sad', 'depressed',
            'upset', 'desperate', 'angry', 'disgusted', 'frustrated', 'jealous','betrayed', 'abused', 'rejected'
            ]
        # counters for the categories
        self.sad = 0
        self.stressed = 0
        self.happy = 0
        self.tired = 0
        self.energized = 0


class InteractionLog:
    # tracks interaction data

    def __init__(self):
        self.user_name = "Devon"
        self.emotions = Emotions()
        self.reported_emotions = []
        self.symptoms = {}
        self.interaction_number = 0

    def get_data(self):
        print("Good Morning, Devon!")
        general_answer = input("How are you feeling today? ")
        word_list = general_answer.split()
        print(word_list)
        return word_list

    def log_data(self, new_data):
        # write to text file

        return True

    def interpret(self, data):
        for word in data:
            for emotion in self.emotions.emotions_list:
                if word.lower() == emotion.lower():
                    # add to reported_emotions
                    self.reported_emotions.append(word.lower())
        print(self.reported_emotions)
        for word in self.reported_emotions:
            """for key in self.emotions.emotions_dict.keys():
                for emotion in self.emotions.emotions_dict[key]:
                    if word == emotion:
                        self.emotions.key += 1"""
            for emotion in self.emotions.emotions_dict['sad']:
                if word == emotion:
                    self.emotions.sad = self.emotions.sad + 1
                    continue
            for emotion in self.emotions.emotions_dict['stressed']:
                if word == emotion:
                    self.emotions.stressed = self.emotions.stressed + 1
                    continue
            for emotion in self.emotions.emotions_dict['happy']:
                if word == emotion:
                    self.emotions.happy = self.emotions.happy + 1
                    continue
            for emotion in self.emotions.emotions_dict['tired']:
                if word == emotion:
                    self.emotions.tired = self.emotions.tired + 1
                    continue
            for emotion in self.emotions.emotions_dict['energized']:
                if word == emotion:
                    self.emotions.energized += self.emotions.energized + 1
        print("tallies for each category")
        print("happy:", self.emotions.happy)
        print("sad:", self.emotions.sad)
        print("stressed:", self.emotions.stressed)
        print("tired:", self.emotions.tired)
        print("energized:", self.emotions.energized)
        self.follow_up()

    def follow_up(self):
        # find categories with most tallies (over time)
        patterns = []  # categories that have more than 3 tallies
        """for categories in self.emotions.emotions_dict.keys():
            # if category counter > 3 then append category to list
            if self.emotions.emotions_dict.categories > 3:
                patterns.append(categories)"""
        if self.emotions.sad > 1:
            patterns.append('sad')
        if self.emotions.stressed > 1:
            patterns.append('stressed')
        if self.emotions.happy > 1:
            patterns.append('happy')
        if self.emotions.tired > 1:
            patterns.append('tired')
        if self.emotions.energized > 1:
            patterns.append('energized')
        print(patterns)

        # find category with the most tallies (max) (single day)


def main():
    wes = InteractionLog()
    data = wes.get_data()
    # wes.log_data(data)
    wes.interpret(data)


if __name__ == '__main__':
    main()
