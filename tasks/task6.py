def roman_to_int(str_):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
         'C': 100, 'D': 500, 'M': 1000}
    new_list_ = []
    for i in list(str_):
        for key, item in d.items():
            if i == key:
                new_list_.append(item)

    for n in range(len(new_list_) - 1):
        if new_list_[n] < new_list_[n + 1]:
            new_list_[n + 1] = -new_list_[n] + new_list_[n + 1]
            new_list_[n] = 0
    return sum(new_list_)
