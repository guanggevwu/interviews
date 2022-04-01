#flatten
def flatten_a_level(x):
    newx = []
    for i in x:
        for j in i:
            newx.append(j)
    return newx
x = [[[[1]]],[[[2]]]]
while type(x[0]) is list:
    x = flatten_a_level(x)