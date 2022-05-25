def wave(str_):
    wave_list = []
    for index, value in enumerate(str_):
        word = str_.replace(str_[index], str_[index].upper())
        wave_list.append(word)
    return wave_list