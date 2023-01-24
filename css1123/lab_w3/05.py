# Remove all digits from the input string. 
# 
# If there are no digits left, print None. 
# 
# Otherwise, print the digits in a comma-separated sequence.
digits = list('0123456789')
x = input()
for c in x:
    if c in digits:
        digits.remove(c)
if len(digits) == 0:
    print('None')
else:
    print(','.join(digits))