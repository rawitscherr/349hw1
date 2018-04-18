from node import Node
import pdb
import math

def ID3(examples, default):
#      Takes in an array of examples, and returns a tree (an instance of Node)
#      trained on the examples.  Each example is a dictionary of attribute:value pairs,
#      and the target class variable is a special attribute with the name "Class".
#      Any missing attributes are denoted with a value of "?"
    if examples == None:
        return default
    elif 1 == len(examples[0].items()): #need to check for no nontrivial splits
        default=examples[0].items()[0][1]
        return default
    else:
        best,bestname,entropies=findbest(examples)
        a=Node()
        tree=treeform(a,bestname,best,examples)
        print(tree.label,tree.children[0].label,tree.children)
        return tree


def treeform(node,bestname,best,examples):
    node.label=bestname
    attvals=[]
    if len(examples)>1:
        for i in range(0,len(examples)):
            attvals.append(examples[i].get(bestname))
        for i in range(0,len(set(attvals))):
            ates=attexamples(bestname,best,list(set(attvals))[i],examples)
            for j in range(0,len(ates)):
                ates[j].pop(bestname,None)
                #print(ates,len(ates))
            if len(ates)>1:
                if len(ates[0].items())>1:
                    best,bestname,entropies=findbest(ates)
                        #pdb.set_trace()
                    node.children.update({list(set(attvals))[i]:treeform(node,bestname,best,ates)})
            else:
                node.children.update({ates[0]:Node()})
                node.children[i].classification=ates[0].get('Class')
    else:
        node.classification=examples.get('Class')
    return node


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
        if len(examples[i].items())>attributeindex:
            if value==examples[i].items()[attributeindex][1] and examples[i].items()[attributeindex][0] == attributename:
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
  total = len(examples)
  correct = 0
  for i in range (0, len(examples)):
    c = traverse(node, examples[i])
    if c == examples[i].get("Class"):
      correct = correct + 1
  return float(correct)/total


def traverse(node, example):
  '''
  Helper function for test
  '''
  if len(node.children) == 0:
    return node.classification
  else:
    attsplit = node.label
    attvalue = example.get(attsplit)
    traverse(node.children.get(attvalue), example)



def evaluate(node, example):
  '''
  Takes in a tree and one example.  Returns the Class value that the tree
  assigns to the example.
  '''
  #print(node.children)
  if len(node.children) == 0:
    return node.classification
  else:
    attname = node.label
    attvalue = example.get(attname)
    evaluate(node.children.get(attvalue), example)
