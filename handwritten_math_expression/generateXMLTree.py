def verifyRecRelationship(rec_a, rec_b):
    w1_a,h1_a,w2_a,h2_a = rec_a
    w1_b,h1_b,w2_b,h2_b = rec_b
    heighta = h2_a - h1_a
    heightb = h2_b - h1_b
    #b is 'div'
    if(h2_a <= h1_b and w2_a <= w2_b and w1_a >= w1_b):
        return 'up'
    #a is root
    elif(h1_b < h1_a and w1_b > w2_a and heightb <= heighta/3 * 2):
        return 'power'
    else:
        return 'parallel'
 
def convertLabelIntoExpressionStr(labels,position):
    id = 0
    if('-' in labels):
        index_m = [ind for ind, j in enumerate(labels) if j == "-"]
        for i in index_m:
            if(verifyRecRelationship(position[i-1],position[i]) == 'up'):
                labels[i] = '/'
                id = i
    for x in range(len(labels)-1):
        if(verifyRecRelationship(position[x],position[x+1]) == 'power'):
            labels.insert(x+1,'^')
    if(id != 0):
        labels.insert(0,'(')
        labels.insert(id+1,')')
        labels.insert(i+3,'(')
        labels.append(')')
    str1 = ''
    for label in labels:
        str1 = str1 + label
    return str1

labels= ['5','6','-','8']
positions= [[67, 24, 146, 160],[203, 29, 265, 149],[22, 182, 321, 205],[134, 226, 205, 365]]
return_str = convertLabelIntoExpressionStr(labels,positions)
print(return_str)
