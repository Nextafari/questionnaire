import random
import string


def random_id():
    random_number = str(random.randint(0, 150))
    word = string.ascii_lowercase + random_number
    word_length = 4
    random_word = "".join(random.choice(word) for i in range(word_length))
    return random_word


# random_id()
