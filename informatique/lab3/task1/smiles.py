import re

# 368791
# eyes - 1; nose - 3; mouth - 3
def smilesCount(filename):
    pattern = re.compile(r';<{[|]')
    file = open(filename).read()
    return len(pattern.findall(file))
for i in range(1, 5+1):
    testFile = 'test' + str(i)
    print('Ответ на тест №'+ str(i)+ ' =', smilesCount(testFile))


