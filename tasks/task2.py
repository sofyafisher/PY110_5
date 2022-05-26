def wave(str_):
    wave_list = []
    word_list = list(str_)
    for index in range(len(word_list)):
        word_list[index] = word_list[index].upper()
        wave_list.append("".join(word_list))
        word_list = [x.lower() for x in word_list]
    return wave_list