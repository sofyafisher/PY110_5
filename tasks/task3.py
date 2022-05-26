def wave_inf(str_):
    wave_list = []
    word_list = list(str_)
    word_path = list(range(len(list(str_)))) + \
                list(range(len(list(str_))))[::-1][1:]
    while True:
        for index in word_path:
            word_list[index] = word_list[index].upper()
            wave_list.append("".join(word_list))
            word_list = [x.lower() for x in word_list]
            yield wave_list[index]