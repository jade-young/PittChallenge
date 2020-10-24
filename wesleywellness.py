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
import random
import time

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
            'happy', 'amused', 'excited', 'glad', 'delighted', 'pleased', 'charmed', 'grateful', 'optimistic',
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


    def follow_up_emotion(self):
        emotion_patterns = []  # categories that have more than 3 tallies
        # for categories in self.emotions.emotion_dict.keys():
        # if category counter > 3 then append category to listx

    def follow_up_happy(self):
        happy_response_list = ["That's great! Enjoy the day!",
                               "Good to hear! Hope you have a nice day!"]
        #               other responses
        print(random.choice(happy_response_list))

    def follow_up_sad(self):
        sad_response_list = ["Sorry to hear that. Maybe treat yourself today.",
                             "I'm sorry to hear that. Remember though, it's okay to feel this way sometimes."]
        #               other responses
        print(random.choice(sad_response_list))

    def follow_up_tired(self):
        sad_response_list = ["Sorry to hear that. Maybe take some time for yourself to rest."]
        #               other responses
        print(random.choice(sad_response_list))

    def follow_up_stressed(self):
        sad_response_list = ["Sorry to hear that. Maybe take some time for yourself to rest.",
                             "I'm sorry to hear that. But keep in mind that better days will always be ahead"]
        #               other responses
        print(random.choice(sad_response_list))
        breathing_ans = input("Would you like to do a breathing exercise? ")
        if (breathing_ans.lower() == "yes") or (breathing_ans.lower() == "sure") or (breathing_ans.lower() == "ok"):
            self.breathing_exercise()
        else:
            print("No worries. Feel free to request a breathing exercise at anytime.")


    def breathing_exercise(self):
        def hold_1():
            print("...")
            time.sleep(1)

        def single_round(i):
            if i==1:
                print("Lets begin our breathing exercise.")
                time.sleep(1)

            print("First, breathe in quietly for 4 seconds")
            time.sleep(1)
            hold_1()
            hold_1()
            hold_1()
            hold_1()
            print("Hold the breath for 7 seconds")
            time.sleep(1)
            hold_1()
            hold_1()
            hold_1()
            hold_1()
            hold_1()
            hold_1()
            hold_1()
            print("Now slowly exhale for 8 seconds")
            time.sleep(1)
            hold_1()
            hold_1()
            hold_1()
            hold_1()
            hold_1()
            hold_1()
            hold_1()
            hold_1()
            if i == 1:
                print("Excellent, let's repeat two more times")
            elif i == 2:
                print("Great, let's repeat one more time.")
            elif i == 3:
                print("Great job. Feel free to request a breathing exercise at any time.")

        for i in [1, 2, 3]:
            single_round(i)


def main():
    wes = InteractionLog()
    data = wes.get_data()
    wes.log_data(data)
    wes.interpret(data)


if __name__ == '__main__':
    main()
