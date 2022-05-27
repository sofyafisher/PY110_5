def modify(str_):
    new_str_ = ''
    if len(str_) % 2 == 0:
        k = int(len(str_) / 2) - 1
        new_str_ = str_[k::-1] + str_[(k + 1):][::-1]
    elif len(str_) % 2 != 0:
        k = int(len(str_) // 2) + 1
        new_str_ = str_[(k - 2)::-1] + str_[k - 1] + str_[k:][::-1]
    return new_str_
