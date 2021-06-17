from . import models

import datetime as dt


def save_history(raw, num):
    """
    save latest 6 conversion
    revrite the oldest one
    """
    if models.History.objects.all().count() > 6:
        tmp = models.History.objects.latest()
    else:
        tmp = models.History()

    tmp.from_num = raw
    tmp.to_num = num
    tmp.time = dt.datetime.now()
    tmp.save()


def check_num(num):
    """
    check, is num an arabic or a roman
    return None, if no one
    """
    all_models = models.Numbers.objects.all()
    roman = [x.roman for x in all_models]
    arabic = [str(x) for x in range(10)]

    num = list(num)

    if set(num).issubset(roman):
        return "R"

    elif set(num).issubset(arabic):
        return "A"

    else:
        return None


def to_roman(num):
    """
    convert number from arabic to roman
    return string of roman numbres
    """
    num = int(num)

    all_models = models.Numbers.objects.all()
    nums = {x.arabic: x.roman for x in all_models}
    keys = list(nums.keys())
    keys.sort(reverse=True)  # can be important!

    numStr = ""

    if num // 1000 > 3:
        numStr += "M*" + str(num // 1000) + "+"
        num -= (num // 1000) * 1000

    for x in range(len(keys)):
        amount = num // int(keys[x])

        if amount > 3 and int(keys[x]) != 1000:
            numStr += nums[keys[x]] + nums[keys[x - 1]]
            num = num - (int(keys[x - 1]) - int(keys[x]))

        else:
            for j in range(amount):
                numStr += nums[keys[x]]
            num = num - amount * int(keys[x])

    return numStr


def to_arabic(num):
    """
    convert number from roman to arabic
    return integer
    """
    all_models = models.Numbers.objects.all()
    nums = {str(x.roman): x.arabic for x in all_models}

    num = list(num)
    calc = []
    res = 0

    # convert roman to arabic
    for x in num:
        calc.append(int(nums[x]))

    # calculate with the rules of roman number position
    for x in range(len(calc) - 1):
        if calc[x] < calc[x + 1]:
            calc[x] = calc[x] * (-1)

    return sum(calc)