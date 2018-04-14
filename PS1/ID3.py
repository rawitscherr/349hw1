from node import Node
import math

def ID3(examples, default):

    entropies=[]
    for i in range(0, len(examples[0].items())-1):# i is number of attributes in each example
        attributeValues = []
        attributeClass = []
        for j in range (0, len(examples)):     # j is number of examples
                                                       # examples[1].items()[i][1] = value of attribute i
            attributename=examples[1].items()[i][0] #= name of attribute i
            attributeValues.append(examples[j].items()[i][1])
            attributeClass.append(examples[j].items()[len(examples[j].items()) - 1][1])
        #print(attributename,attributeValues,'class', attributeClass)
    one,two=classcount(examples)
    #print(one,two)
    three=returnmaxclass(one,two)
    #print(three)
    #print(max(two), sum(two))
    a=entropy(max(two),sum(two))
    #print(a)


            #x=max(uniqueclasscount)
            #y=sum(uniqueclasscount)-x


#      Takes in an array of examples, and returns a tree (an instance of Node)
#      trained on the examples.  Each example is a dictionary of attribute:value pairs,
#      and the target class variable is a special attribute with the name "Class".
#      Any missing attributes are denoted with a value of "?"

    if examples == None:
        return default
    elif examples.count('Class' in examples[0]) == len(examples) or 'a':
        return default
    else:
        infogain=0

        print( examples.items())
        tree= Node()
        tree.label=tree
        return default


def classcount(examples):
    classes = []
    numExamples = len(examples)
    for i in range(0, numExamples):
        classes.append(examples[i].items()[len(examples[i].items())-1])

    uniqueclass = []        # set of unique classifications
    uniqueclasscount = []   # list containing counts of corresponding classifications in uniqueclass list
                            # used for caluclating MODE(classes)

    numUniqueClasses = len(set(classes))

    for i in range(0, numUniqueClasses):
        counter = 0
        for j in range(0, numExamples):
            if  list(set(classes))[i] == list(classes)[j]:
                counter = counter+1
        uniqueclass.append(list(set(classes))[i][1])
        uniqueclasscount.append(counter)
    return uniqueclass, uniqueclasscount

def findbest(node, examples):
    x=0
    for i in range(0,len(set(new_words))):
        x=x+1
    IG0=x
    print(IG0)
    for i in range(0, len(examples[0].items())):
        if IG1>IG0:
            x=x+1

def entropy(x,y):
    temp1 = float(x/float(y))
    temp2 = float(1 - temp1)
    if temp2 == 0:
      hprior = temp1 * math.log(temp1,2)
    else:
        hprior = temp1 * math.log(temp1,2) + temp2 * math.log(temp2, 2)
        #hprior=math.log(temp1,2)
    return hprior

def returnmaxclass(uniqueclass, uniqueclasscount):
    x=uniqueclasscount.index(max(uniqueclasscount))
    maxclass=uniqueclass[x]
    return maxclass




def prune(node, examples):
  '''
  Takes in a trained tree and a validation set of examples.  Prunes nodes in order
  to improve accuracy on the validation data; the precise pruning strategy is up to you.
  '''

def test(node, examples):
  '''
  Takes in a trained tree and a test set of examples.  Returns the accuracy (fraction
  of examples the tree classifies correctly).
  '''


def evaluate(node, example):
  '''
  Takes in a tree and one example.  Returns the Class value that the tree
  assigns to the example.
  '''
