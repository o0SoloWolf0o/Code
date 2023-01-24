# 1. Initialize a sum and a count to zero.
# 2. Get the first input.
# 3. While the input is not 'q', add the input to the sum and increment the count.
# 4. If the input is 'q', print the average of the sum and count.
# 5. If the input is not 'q', but the count is still zero, print 'No Data'.
s = 0
n = 0
x = input()
while x != 'q':
    s += float(x)
    n += 1
    x = input()
if n == 0:
    print('No Data')
else:
    avg = s/n
    print(round(avg, 2))
