# Pitt Challenge
# Project - Intelligient Assistant for General Health
# Jade Young & Devon Smyth

import random
import time


class Symptoms:
    def __init__(self):
        self.symptoms_dict = {'cough': ['cough','coughing'],
                              'headache': ['headache','pounding','head'],
                              'fever': ['fever','temperature'],
                              'nose': ['stuffy','runny','sneeze','sinus'],
                              'throat':['throat', 'itch '],
                              'stomach':['stomach','bug'],
                              'back':['back'],
                              'knee':['knee','knees']
                              }
        self.symptoms_list = ['cough','coughing','headache','pounding','head','fever','temperature',
                              'stuffy','runny','sneeze','sinus','throat','stomach','bug','back','knee','knees'
                              ]
        self.cough = 0
        self.headache = 0
        self.fever = 0
        self.nose = 0
        self.throat = 0
        self.stomach = 0
        self.back = 0
        self.knee = 0
        # lists for category counters
        self.cough_list = []
        self.headache_list = []
        self.fever_list = []
        self.nose_list = []
        self.throat_list = []
        self.stomach_list = []
        self.back_list = []
        self.knee_list = []


class Emotions:
    def __init__(self):
        self.emotions_dict = {'sad': ['sad', 'depressed', 'upset', 'desperate', 'angry', 'disgusted', 'frustrated',
                  'jealous','betrayed', 'abused', 'rejected'], 'stressed': ['stressed', 'panic', 'uncomfortable', 'unsure','stuck','desperate','frozen','hurt'], 
                  'happy': ['happy', 'great', 'amused', 'excited', 'glad','delighted','pleased','charmed',
                    'grateful','optimistic','content','joyful','loving','loved','secure','strong','brave',
                    'prepared','relaxed','comforted', 'good'],
            'tired': ['bored', 'depressed', 'drained', 'tired','dejected', 'dull', 'fatigued', 'burn', 'burned', 'burnt'],
            'energized': ['strong', 'strengthened', 'motivated', 'focused', 'invigorated', 'determined', 'energized',
                        'inspired']
        }

        self.emotions_list = ['strong', 'strengthened', 'motivated', 'focused', 'invigorated', 'determined', 'energized', 'inspired',
            'great', 'bored', 'depressed', 'drained', 'tired','dejected', 'dull', 'fatigued', 'burn', 'burned', 'burnt',
            'happy', 'great', 'amused', 'excited', 'glad', 'delighted', 'pleased', 'charmed', 'grateful', 'optimistic',
            'content', 'joyful', 'loving', 'loved', 'secure', 'strong', 'brave', 'prepared', 'relaxed', 'comforted',
            'stressed', 'panic', 'uncomfortable', 'unsure','stuck','desperate','frozen','hurt','sad', 'depressed',
            'upset', 'desperate', 'angry', 'disgusted', 'frustrated', 'jealous','betrayed', 'abused', 'rejected', 'good'
            ]
        # counters for the categories
        self.sad = 0
        self.stressed = 0
        self.happy = 0
        self.tired = 0
        self.energized = 0
        # list for each of the counters
        self.sad_list = []
        self.stressed_list = []
        self.happy_list = []
        self.tired_list = []
        self.energized_list = []


class InteractionLog:
    # tracks interaction data

    def __init__(self):
        self.user_name = "Devon"
        self.emotions = Emotions()
        self.symptoms = Symptoms()
        self.reported_emotions = []
        self.reported_symptoms = []
        self.streak = [0, 0, 0, 0, 0]
        self.symptom_streak = [0, 0, 0, 0, 0, 0, 0, 0]
        self.interaction_number = 0
        self.stored_data = []
        self.stored_data2 = []

    def get_data(self):
        print("Good Morning, Devon!")
        general_answer = input("How are you feeling today? ")
        word_list = general_answer.split()
        # print(word_list)
        return word_list

    def log_data(self):
        # write to text file
        
        temp_list = [self.emotions.sad_list, self.emotions.stressed_list, self.emotions.happy_list, self.emotions.tired_list, self.emotions.energized_list]
        with open('wesley_log_e.txt', 'a') as thefile:
            for counter in self.emotions.sad_list:
                thefile.write(str(counter))  # '\n'.join(counter)
            for counter in self.emotions.energized_list:
                thefile.write(str(counter))
            for counter in self.emotions.happy_list:
                thefile.write(str(counter))
            for counter in self.emotions.stressed_list:
                thefile.write(str(counter))
            for counter in self.emotions.tired_list:
                thefile.write(str(counter))
            thefile.write("\n")
        
        with open('wesley_log_s.txt', 'a') as thefile:
            for counter in self.symptoms.cough_list:
                thefile.write(str(counter))
            for counter in self.symptoms.headache_list:
                thefile.write(str(counter))
            for counter in self.symptoms.fever_list:
                thefile.write(str(counter))
            for counter in self.symptoms.nose_list:
                thefile.write(str(counter))
            for counter in self.symptoms.throat_list:
                thefile.write(str(counter))
            for counter in self.symptoms.stomach_list:
                thefile.write(str(counter))
            for counter in self.symptoms.back_list:
                thefile.write(str(counter))
            for counter in self.symptoms.knee_list:
                thefile.write(str(counter))
            thefile.write("\n")
        
        return True

    def interpret(self, data):
        for word in data:
            for emotion in self.emotions.emotions_list:
                if word.lower() == emotion.lower():
                    # add to reported_emotions
                    self.reported_emotions.append(word.lower())
            for symptom in self.symptoms.symptoms_list:
                if word.lower() == symptom.lower():
                    # add to reported symtoms
                    self.reported_symptoms.append(word.lower())

        for word in self.reported_emotions:
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
        for word in self.reported_symptoms:
            for symptom in self.symptoms.symptoms_dict['cough']:
                if word == symptom:
                    self.symptoms.cough = self.symptoms.cough + 1
                    continue
            for symptom in self.symptoms.symptoms_dict['headache']:
                if word == symptom:
                    self.symptoms.headache = self.symptoms.headache + 1
                    continue
            for symptom in self.symptoms.symptoms_dict['fever']:
                if word == symptom:
                    self.symptoms.fever = self.symptoms.fever + 1
                    continue
            for symptom in self.symptoms.symptoms_dict['nose']:
                if word == symptom:
                    self.symptoms.nose = self.symptoms.nose + 1
                    continue
            for symptom in self.symptoms.symptoms_dict['throat']:
                if word == symptom:
                    self.symptoms.throat = self.symptoms.throat + 1
                    continue
            for symptom in self.symptoms.symptoms_dict['stomach']:
                if word == symptom:
                    self.symptoms.stomach = self.symptoms.stomach + 1
                    continue
            for symptom in self.symptoms.symptoms_dict['back']:
                if word == symptom:
                    self.symptoms.back = self.symptoms.back + 1
                    continue
            for symptom in self.symptoms.symptoms_dict['knee']:
                if word == symptom:
                    self.symptoms.knee = self.symptoms.knee + 1

        # append each counter to categories list
        self.emotions.sad_list.append(self.emotions.sad)
        self.emotions.stressed_list.append(self.emotions.stressed)
        self.emotions.happy_list.append(self.emotions.happy)
        self.emotions.tired_list.append(self.emotions.tired)
        self.emotions.energized_list.append(self.emotions.energized)

        self.symptoms.cough_list.append(self.symptoms.cough)
        self.symptoms.headache_list.append(self.symptoms.headache)
        self.symptoms.fever_list.append(self.symptoms.fever)
        self.symptoms.nose_list.append(self.symptoms.nose)
        self.symptoms.throat_list.append(self.symptoms.throat)
        self.symptoms.stomach_list.append(self.symptoms.stomach)
        self.symptoms.back_list.append(self.symptoms.back)
        self.symptoms.knee_list.append(self.symptoms.knee)

        """print("tallies for each category")
        print("happy:", self.emotions.happy)
        print("sad:", self.emotions.sad)
        print("stressed:", self.emotions.stressed)
        print("tired:", self.emotions.tired)
        print("energized:", self.emotions.energized)"""
        # self.follow_up()

    def follow_up(self):
        # emotion of the day
        index = 0
        max = 0
        max_category = -1
        for number in self.stored_data[-1]:
            if number > max:
                max = number
                max_category = index
            index += 1

        if max_category == 0:
            self.follow_up_sad()
        if max_category == 1:
            self.follow_up_energized()
        if max_category == 2:
            self.follow_up_happy()
        if max_category == 3:
            self.follow_up_stressed()
        if max_category == 4:
            self.follow_up_tired()

        self.recognize_streak()
    
    def recognize_streak(self):
        # recognize patterns in each emotion/symptom over past few days
        if len(self.stored_data) < 3:
            return
        for category in [0, 1, 2, 3, 4]:
            if self.stored_data[-1][category]>=1:
                if self.stored_data[-2][category] >= 1:
                    if self.stored_data[-3][category] >= 1:
                        self.streak[category]+=1

        for category in [0, 1, 2, 3, 4, 5, 6, 7]:
            if self.stored_data2[-1][category]>=1:
                if self.stored_data2[-2][category] >= 1:
                    if self.stored_data2[-3][category] >= 1:
                        self.symptom_streak[category] += 1 # add variable self.symptom_streak

        # make user aware of noticed emotional trends
        if self.streak[0] == 1:
            print("Ive noticed you've been down the past few days.")
        if self.streak[3] == 1:
            print("Ive noticed you've been stressed the past few days.")
        if self.streak[4] == 1:
            print("Ive noticed you've been tired the past few days.")

        # make user aware of noticed symptom patterns
        # 'cough''headache''fever''nose''throat''stomach''back''knee'
        if self.symptom_streak[0] == 1:
            print("Ive noticed you've mentioned having a cough the past few days.")
            print("I'd recommend seeking a professional's guidance if it continues to bother you.")
        if self.symptom_streak[1] == 1:
            print("Ive noticed you've mentioned having a headache the past few days.")
            print("I'd recommend seeking a professional's guidance if it continues to bother you.")
        if self.symptom_streak[2] == 1:
            print("Ive noticed you've mentioned fever-related symptoms the past few days.")
            print("I'd recommend seeking a professional's guidance if this persists over the next few days")
        if self.symptom_streak[3] == 1:
            print("Ive notice you've mentioned nose-related symptoms the past few days.")
            print("I'd recommend seeking a professional's guidance if it continues to bother you.")
        if self.symptom_streak[4] == 1:
            print("Ive noticed you've mentioned throat-related symptoms the past few days.")
            print("I'd recommend seeking a professional's guidance if it continues to bother you.")
        if self.symptom_streak[5] == 1:
            print("Ive noticed you've mentioned your stomach bothering you the past few days.")
            print("I'd recommend seeking a professional's guidance if it continues to bother you.")
        if self.symptom_streak[6] == 1:
            print("Ive noticed you've mentioned your back bothering you the past few days.")
            print("I'd recommend seeking a professional's guidance if it continues to bother you.")
        if self.symptom_streak[7] == 1:
            print("Ive noticed you've mentioned your knees bothering you the past few days.")
            print("I'd recommend seeking a professional's guidance if it continues to bother you.")

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
            if i == 1:
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
 
    def analyze(self):
        # read data from file
        with open('wesley_log_e.txt', 'r') as thefile:
            current_line = thefile.readline()
            current_line = current_line.strip()
            l1 = []
            for num in current_line.split():
                for digit in num:
                    l1.append(int(digit))
            self.stored_data.append(l1)
            current_line = thefile.readline()
            current_line = current_line.strip()
            while current_line != '':
                l1 = []
                for num in current_line.split():

                    for digit in num:
                        l1.append(int(digit))
                self.stored_data.append(l1)
                current_line = thefile.readline()
                current_line = current_line.strip()
        with open('wesley_log_s.txt', 'r') as thefile:
            current_line = thefile.readline()
            current_line = current_line.strip()
            l1 = []
            for num in current_line.split():
                for digit in num:
                    l1.append(int(digit))
            self.stored_data2.append(l1)
            current_line = thefile.readline()
            current_line = current_line.strip()
            while current_line != '':
                l1 = []
                for num in current_line.split():

                    for digit in num:
                        l1.append(int(digit))
                self.stored_data2.append(l1)
                current_line = thefile.readline()
                current_line = current_line.strip()


def main():
    wes = InteractionLog()
    data = wes.get_data()

    wes.interpret(data)
    wes.log_data()
    wes.analyze()
    wes.follow_up()


if __name__ == '__main__':
    main()
