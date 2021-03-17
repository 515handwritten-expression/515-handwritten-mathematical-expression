'''This file is used as postprocessing module after each characters is recognized by the model
Input of the module: A list of labels and a list of character positions in the original image
Output of the moduule: A string for Latex output and a string for operation
'''
#Given two rectangl positions and return the relationship
def verifyRecRelationship(rec_a, rec_b):
    w1_a,h1_a,w2_a,h2_a = rec_a
    w1_b,h1_b,w2_b,h2_b = rec_b
    #b is 'div'
    if(h2_a <= h1_b and w2_a <= w2_b and w1_a >= w1_b):
        return 'up'
    #a is root
    elif(h1_b < h1_a and w1_b > w2_a and (h2_b - h1_b) <= (h2_a - h1_a)/3 * 2):
        return 'power'
    else:
        return 'parallel'
 
#According to the positions between characters and labels return a string
def convertLabelIntoExpressionStr(labels,position):
    id = 0
    hat = 0
    labels = ['/' if a=='div' else a for a in labels]
    labels = ['*' if a=='times' else a for a in labels]
    if('-' in labels):
        index_m = [ind for ind, j in enumerate(labels) if j == "-"]
        for i in index_m:
            if(verifyRecRelationship(position[i-1],position[i]) == 'up'):
                labels[i] = '/'
                id = i
    for x in range(len(labels)-1):
        if(verifyRecRelationship(position[x],position[x+1]) == 'power'):
            hat += 1
            labels.insert(x+hat,'^')
    if(id != 0):
        labels.insert(0,'(')
        labels.insert(id+1+hat,')')
        labels.insert(i+3+hat,'(')
        labels.append(')')
    str1 = ''
    for label in labels:
        str1 = str1 + label
    return str1

#Get rid off the native symbols in the string
def removeNegativeSymbol(inputstr):
    if(inputstr[0]=='-'):
        inputstr = '0' + inputstr
    inputstr = inputstr.replace('(-','(0-')
    return inputstr


def getStringsForLatexAndTree(labels,positions):
    if(len(labels)>1):
        str_latex = convertLabelIntoExpressionStr(labels,positions)
        str_tree = str_latex
        str_tree = removeNegativeSymbol(str_tree)
    else:
        str_tree = labels[0]
        str_latex = labels[0]
    return str_latex, str_tree
