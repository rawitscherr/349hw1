from node import Node
import math

def ID3(examples, default):
#      Takes in an array of examples, and returns a tree (an instance of Node)
#      trained on the examples.  Each example is a dictionary of attribute:value pairs,
#      and the target class variable is a special attribute with the name "Class".
#      Any missing attributes are denoted with a value of "?"
    print(examples)
    if examples == None:
        return default
    elif 1 == len(examples[0].items()): #need to check for no nontrivial splits
        default=examples[0].items()[0][1]
        print default
        return default
    else:
        findbest(examples)
        best,bestname,entropies=findbest(examples)
        #print(best,entropies)
        tree= Node()
        tree.label=best
        attvals=[]
        for i in range(0,len(examples)):
            attvals.append(examples[i].items()[best][1])
        for i in range(0,len(set(attvals))):
            tree.children.update({list(set(attvals))[i]:best})
            #tree.children.update({'a':1})
        print(tree.children)
        for i in range(0,len(tree.children.items())):
            ates=attexamples(bestname,best,list(set(attvals))[i],examples)
            #print(ates)
            for j in range(0,len(ates)):
                ates[j].pop(bestname,None)
            #ID3(ates,default)
            #print(ates)
            ID3(ates,default)
        #print(prop)
        return tree



    #for i in range(0, len(examples[0].items())-1):# i is number of attributes in each example
        #attributeValues = []
        #attributeClass = []
        #for j in range (0, len(examples)):     # j is number of examples
                                                       # examples[1].items()[i][1] = value of attribute i
            #attributename=examples[1].items()[i][0] #= name of attribute i
            #attributeValues.append(examples[j].items()[i][1])
            #attributeClass.append(examples[j].items()[len(examples[j].items()) - 1][1])
        #print(attributename,attributeValues,'class', attributeClass)
    #one,two=classcount(examples)
    #print(one,two)
    #three=returnmaxclass(one,two)
    #print(three)
    #print(max(two), sum(two))
    #a=entropy(max(two),sum(two))
    #print(a)

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

def attexamples(attributename,attributeindex,value,examples):
    attex=[]
    for i in range(0,len(examples)):
        if value==examples[i].items()[attributeindex][1] and examples[i].items()[attributeindex][0]== attributename:
            attex.append(examples[i])
        #print(i,examples[i])
    return attex

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
    maxclassnum=uniqueclasscount[x]
    return maxclassnum

def findbest(examples):
    allentropies=[]
    for i in range(0,len(examples[0].items())-1):
        attvalues=[]
        attnum=i
        for j in range(0,len(examples)):
            attvalues.append(examples[j].items()[i][1])
            uniqueatt=list(set(attvalues))
            entropies=[]
        for j in range(0,len(uniqueatt)):
            ex=attexamples(examples[0].items()[attnum][0],attnum,uniqueatt[j],examples)
            x,y=classcount(ex)
            #print(ex,x,y)
            ax=returnmaxclass(x,y)
            #print(ax, sum(y))
            entropies.append(entropy(ax,sum(y)))
            #print(entropies)
        entrope=sum(entropies)
        allentropies.append(entrope)
    #print(allentropies)
    bestsplit=max(allentropies)
    ind=allentropies.index(bestsplit)
    return(ind,examples[0].items()[ind][0],allentropies)
    #return(ind,allentropies)

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
  if len(tree.children == 0):
    return tree.classification
  for i in range(0,len(tree.children)):
    for j in range(0,len(example.items())):
      if tree.children[i].label == example.items()[j]: ## reformat, this wont work as is
        evaluate(tree.children[i],example)
  return tree.classification

