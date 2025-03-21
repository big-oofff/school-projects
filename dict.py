def mapAB(dict1):
    if "a" in dict1 and "b"in dict1:
        dict1["ab"] = dict1["a"] + dict1["b"]
    return dict1


def topping1(dict1):
    if "ice cream" in dict1:
        dict1["ice cream"] = "cherry"
    dict1["bread"] = "butter"
    return dict1

def topping3(dict1):
    if "potato" in dict1:
        dict1["fries"] = dict1["potato"]
    if "salad" in dict1:
        dict1["spinach"] = dict1["salad"]
    return dict1


def mapAB2(dict1):
    if "a" in dict1 and "b" in dict1:
        del dict1["a"]
        del dict1["b"]
    return dict1

def mapAB3(dict1):
    if "a" in dict1 and "b" not in dict1:
        dict1["b"] = dict1["a"]
    if "b" in dict1 and "a" not in dict1:
        dict1["a"] = dict1["b"]
    return dict1

def mapAB4(dict1):
    if len(dict1["a"]) > len(dict1["b"]):
        dict1["c"] = dict1["a"]
    elif len(dict1["a"]) < len(dict1["b"]):
        dict1["c"] = dict1["b"]
    else:
        dict1["a"] = ""
        dict1["b"] = ""
    return dict1

def word0(array):
    d = dict()
    for ele in array:
        if ele not in d:
            d[ele] = 0
    return d


def wordlen(array):
    d = dict()
    for ele in array:
        if ele not in d:
            d[ele] = len(ele)
    return d

def pairs(array):
    d = dict()
    for ele in array:
        if ele[0] not in d:
            d[ele[0]] = ele[-1]
    return d



def firstChar(array):
    d = dict()
    for ele in array:
        if ele[0] not in d:
            d[ele[0]] = ele
        else:
            d[ele[0]] += ele
    return d

def word_append(array):
    d = {}
    result = ""
    for word in array:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
        if d[word] % 2 == 0:
            result += word
    return result

def word_multiple(array):
    d = {}
    result = {}
    for word in array:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    for word, count in d.items():
        result[word] = count >= 2
    return result



    

    


