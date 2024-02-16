
def only_long_words(func):
    
    def wrapper(text):
        result = []
        for word in text.split():
            if len(word) > 2:
                result.append(word)
            else:
                print(f"слово {word} не считаем")
        # print('текст в итоге:', ' '.join(result))
        return func(' '.join(result))
    return wrapper
        
@only_long_words
def count_words(text):

    return len(text.split())


lyrics = "все без тебя не так, лечу к тебе я словно комета, и даже под дулом пистолета я найду тебя"
print(count_words(lyrics))
