import os
string1 = '''Everything is half here,
like the marble head
of the Roman emperor
and the lean torso
of his favorite.
The way the funnel cloud
which doesn't seem
to touch ground does—
flips a few cars, a semi—
we learn to...
'''
try:
    BASE_PATH = 'aa'
    os.mkdir(BASE_PATH)
    for i in range(1,4):
        os.mkdir(f'{BASE_PATH}/bb{i}')
        for j in range(1,4):
            os.mkdir(f'{BASE_PATH}/bb{i}/cc{j}')
            for filename in ('dd1.txt', 'dd2.txt', 'dd3.txt'):
                with open(f'{BASE_PATH}/bb{i}/cc{j}/{filename}', 'w') as f:
                    f.write(string1)
except FileExistsError:
    print("FileAlreadyExist")