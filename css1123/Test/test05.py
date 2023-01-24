input_str = input()
output = ""
for i in input_str:
    if i == "(":
        output += "["
    elif i == "[":
        output += "("
    elif i == ")":
        output += "]"
    elif i == "]":
        output += ")"
    else:
        output += i
print(output)