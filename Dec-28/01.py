def shorten_word(word: str = "") -> str:
    if not type(word) is str:
        return ''
    if len(word) <= 4:
        return word
    result = word[:2] + '-' + word[-2:]
    return result

def shorten(text = "") -> str:
    if not type(text) is str:
        return ''
    result = []
    for word in text.split(' '):
        result.append(shorten_word(word))
    return ' '.join(result)
def test_shorten():
    assert shorten("крокодил") == 'кр-ил'
    assert shorten("вода") == 'вода'
    assert shorten("йо") == "йо"
    assert shorten("") == ""
    assert shorten(75) == ""
    assert shorten() == ""
    assert shorten("крокодил водолаз") == "кр-ил во-аз"
    print("тест пройден")

test_shorten()