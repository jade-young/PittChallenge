class Emotions:
    def __init__(self):
        self.emotions_dict = {'sad': ['sad', 'depressed', 'upset', 'desperate', 'angry', 'disgusted', 'frustrated',
                  'jealous','betrayed', 'abused', 'rejected'], 'stressed': ['stressed', 'panic', 'uncomfortable', 'unsure','stuck','desperate','frozen','hurt'],
                  'happy': ['happy', 'great', 'amused', 'excited', 'glad','delighted','pleased','charmed',
                    'grateful','optimistic','content','joyful','loving','loved','secure','strong','brave',
                    'prepared','relaxed','comforted'],
            'tired': ['bored', 'depressed', 'drained', 'tired','dejected', 'dull', 'fatigued', 'burn', 'burned', 'burnt'],
            'energized': ['strong', 'strengthened', 'motivated', 'focused', 'invigorated', 'determined', 'energized',
                        'inspired', 'great']
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
