from node import Node
import math

def ID3(examples, default):
    classes=[]
    for i in range(0,len(examples)):
        classes.append(examples[i].items()[len(examples[i].items())-1])
    uniqueclass=[]
    uniqueclasscount=[]
    for i in range(0, len(set(classes))):
        counter=0
        for j in range(0, len(classes)):
            if  list(set(classes))[i] == list(classes)[j]:
                counter=counter+1
        uniqueclass.append(list(set(classes))[i][1])
        uniqueclasscount.append(counter)
    IG=0
    #II=uniqueclasscount.index(max(uniqueclasscount))
    temp=max(uniqueclasscount)/float(len(examples))
    temp2=1-temp
    print(temp, temp2)
    hprior=-1*temp*math.log(temp,2)-1*temp2*math.log(temp2,2)
        #IG=IG-1*temp*math.log(temp,2)
        #print(list(uniqueclasscount)[i])
    print("H Prior is equal to", hprior)
    #print(uniqueclass)
    #print(uniqueclasscount)
    #for i in range(0, len(examples[0].items())):
        #print(examples[1].items()[i][1])
        #print(set(examples[1].items()))

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



def findbest(node, examples):
    x=0
    for i in range(0,len(set(new_words))):
        x=x+1
    IG0=x
    print(IG0)
    for i in range(0, len(examples[0].items())):
        if IG1>IG0:
            x=x+1

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
