import string

def are_anagrams(text_one, text_two):
    # remove punctuation
    text_one = [letter.lower for letter in text_one if letter in string.ascii_lowercase]
    text_two = [letter.lower for letter in text_two if letter in string.ascii_lowercase]
    if len(text_one) != len(text_two):
        return False

    for l1, l2 in zip(sorted(text_one), sorted(text_two)):
        if l1 != l2:
            return False
    else:
        return True
