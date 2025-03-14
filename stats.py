def str2wordcount(rawtext):
    text_list = rawtext.split()
    word_count = len(text_list)
    return word_count

def str2charcount(rawtext):
    loweredstr = rawtext.lower()
    alphcount = {}
    for char in loweredstr:
        alphcount[char] = 0
    for char in loweredstr:
        alphcount[char] += 1
    return alphcount

def sort_on(dict):
    return dict["num"]

def sortdict(chardict):
    dictlist = []
    for i in chardict:
        dictlist.append({"name":i,"num":chardict[i]})

    dictlist.sort(reverse=True, key=sort_on)
    return dictlist


