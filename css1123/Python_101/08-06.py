TtoK = {"a":"2", "b":"22", "c":"222","d":"3" ,"e":"33" ,"f":"333", "g":"4", "h":"44", "i":"444", "j":"5", "k":"55", "l":"555", "m":"6", "n":"66", "o":"666", "p":"7", "q":"77", "r":"777", "s":"7777", "t":"8", "u":"88", "v":"888", "w":"9", "x":"99", "y":"999", "z":"9999", " ":"0"}
KtoT = {value: key for key, value in TtoK.items()}

def text2keys(text):
    question = ''
    for i in text.lower():
        if i in TtoK:
            question += TtoK[i] + ' '
    return question.strip()

def keys2text(keys):
    question = ''
    for i in keys.split():
        question += keys[i] + ' '
    return question.strip()

# exec(input().strip())
# print(text2keys("I am busy."))
# print(keys2text("444 0 2 6 0 22 88 7777 999"))