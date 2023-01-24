timer = {}
number_of_song = input('Number of songs: ')
for i in range(number_of_song):
    name_song, artist, type_song, time = input().split(',')
    m,s = [int(x) for x in time.split(':')]
    if type_song not in timer:
        timer[type_song] = 0
    timer[type_song] += m*60 + s
y = [(t,g) for g,t in timer.items()]
y.sort()
for t,g in y[-3:][::-1]:
    m = str(t//60)
    s = '0' + str(t%60)[-2:]
    print(g,'-->'+m+':'+s)