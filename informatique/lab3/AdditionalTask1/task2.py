import re

# 368791 % 6 = 1

def deleteRepeats(file):
    fileread = file.read()
    res = re.sub(r'\b([^\W\d_]+)(\s+\1)+\b', r'\1', re.sub(r'\W+', ' ', fileread).strip(), flags=re.I)
    return res


for i in range(1,6):
    file = open('test' + str(i))
    print('Ответ на тест №'+ str(i)+ ' =', deleteRepeats(file))