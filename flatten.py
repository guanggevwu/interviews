'''flatten'''

def flatten_a_level(x):
    newx = []
    for i in x:
        if type(i) is list:
            for j in i:
                newx.append(j)
        else:
            newx.append(i)
    return newx
x = [1,[2],'ad', [[5]]]
while True:
    mark = 0
    for i in x:
        if type(i) is list:
            x = flatten_a_level(x)
            mark = 1
            break
    if not mark:
        print(x)
        break