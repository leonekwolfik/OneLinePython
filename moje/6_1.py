text = 'uriis'
anagram = 'wirus'


def my_is_anagram(*words):
    assert len(words) == 2
    return all(w in words[1] for w in words[0]) and len(words[0]) == len(words[1])  # don't work

    # for w in words[0]:
    #     if w not in words[1]:
    #         return False
    #
    # return True


# print(my_is_anagram(text, anagram))

is_anagram = lambda x1, x2: sorted(x1) == sorted(x2)

print(is_anagram("urwis", "wirus"))
print(is_anagram("uriis", "wirus"))
print(is_anagram("urwisu", "wiruus"))
print(is_anagram("urwis", "jeden"))


def my_is_anagram2(w1, w2):
    def _get_histogram(_word: str) -> dict:
        _histogram = dict()
        for _c in _word:
            if _c not in _histogram.items():
                _histogram.update({_c: 1})
            else:
                _histogram[_c] += 1
        return _histogram

    hist1 = _get_histogram(w1)
    hist2 = _get_histogram(w2)
    print(hist1, '\n', hist2)
    return hist2 == hist1


print(my_is_anagram2("urwis", "wirus"))
print(my_is_anagram2("uriis", "wirus"))
print(my_is_anagram2("urwisu", "wiruus"))
print(my_is_anagram2("urwis", "jeden"))
