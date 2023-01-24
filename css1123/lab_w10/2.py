import shutil
import os
with open('super_dd.txt', 'a') as fn:
    try:
        for i in os.listdir('aa'):
            for j in os.listdir('aa/'+i):
                for k  in os.listdir('aa/'+i+'/'+j):
                    with open('aa/'+i+'/'+j+'/'+k, 'r') as f:
                        fn.write(f.read())
        # fn.close()
        # shutil.move('super_dd.txt', 'aa')
    except FileNotFoundError:
        print('File not found!')