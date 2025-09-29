def password_check(string):
    ligit_punct = ['!', '@', '#', '$', '%', '&', '(', ')', '-', '_', '[', ']', '{', '}', ';', "'", ':', '"', ',', '.',
                   '/', '<', '>', '?']
    for each in string:
        if ord(each) >= 65 and ord(each) <= 90:
            is_capital = True
            break
        else:
            is_capital = False

    for each in string:
        if ord(each) >= 97 and ord(each) <= 122:
            is_low_case = True
            break
        else:
            is_low_case = False

    for each in string:
        if ord(each) >= 48 and ord(each) <= 57:
            is_digit = True
            break
        else:
            is_digit = False

    for each in string:
        if each in ligit_punct:
            is_punct = True
            break
        else:
            is_punct = False

    for each in string:
        if not each in ligit_punct:
            if not (ord(each) >= 97 and ord(each) <= 122):
                if not (ord(each) >= 65 and ord(each) <= 90):
                    if not(ord(each) >= 48 and ord(each) <= 57):
                        is_illigit = False
                        break
                    else:
                        is_illigit = True
                else:
                    is_illigit = True
            else:
                is_illigit = True
        else:
            is_illigit = True
    return is_capital and is_low_case and is_digit and is_punct and is_illigit and len(string)>=8

print(password_check("tHIs1sag00d.p4ssw0rd."))
print(password_check("3@t7ENZ((T"))
print(password_check("2.shOrt"))
print(password_check("all.l0wer.case"))
print(password_check("inv4l1d CH4R4CTERS~"))
