def count_letters(text):
    dict_letters = {}
    text = text.lower()
    for _letter in text:
        if _letter.isalpha():
            if _letter in dict_letters.keys():
                dict_letters[_letter] += 1
            else:
                dict_letters[_letter] = 1
    return dict_letters


def calculate_frequency(dict_letters, number):
    _dict_frequency = {}
    for _letter in dict_letters.keys():
        _dict_frequency[_letter] = dict_letters[_letter] / number
    return _dict_frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
dict_count = count_letters(main_str)
count = 0
for letter in main_str:
    if letter.isalpha():
        count += 1
dict_frequency = calculate_frequency(dict_count, count)
for letter in dict_frequency.keys():
    print(f"{letter}:{dict_frequency[letter]: .2f}")
