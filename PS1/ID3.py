from node import Node
import math

def ID3(examples, default):
  '''
  Takes in an array of examples, and returns a tree (an instance of Node)
  trained on the examples.  Each example is a dictionary of attribute:value pairs,
  and the target class variable is a special attribute with the name "Class".
  Any missing attributes are denoted with a value of "?"
  '''
  if examples == None:
      return default
      #checkTrivialCases(examples)
  bestname,bestentropy=findbest(examples)
  tree=treeform(bestname,examples)
  return tree

def classcount(examples):
    classes = []
    for i in range(0, len(examples)):
        classes.append(examples[i].get('Class'))
    uniqueclass = list(set(classes))        # set of unique classifications
    uniqueclasscount = []   # list containing counts of corresponding classifications in uniqueclass list
    for i in range(0, len(uniqueclass)):
        uniqueclasscount.append(classes.count(uniqueclass[i]))
    return uniqueclass, uniqueclasscount

def MODE(examples):
    a,b=classcount(examples)
    ii=b.index(max(b))
    return a[ii]

def attexamples(attributename,attributevalue,examples):
    attributeexamples=[]
    for i in range(0,len(examples)):
        if attributevalue==examples[i].get(attributename):
            attributeexamples.append(examples[i])
    return attributeexamples

def entropy(x,y):
    temp1 = float(x/float(y))
    temp2 = float(1 - temp1)
    if temp2 == 0:
      hprior = temp1 * math.log(temp1,2)
    else:
        hprior = temp1 * math.log(temp1,2) + temp2 * math.log(temp2, 2)
    return hprior

def returnmaxclass(uniqueclass, uniqueclasscount):
    x=uniqueclasscount.index(max(uniqueclasscount))
    maxclassnum=uniqueclasscount[x]
    return maxclassnum

def findbest(examples):
    allentropies=[]
    attributelist=[]
    for i in range(0,len(examples[0].items())):
        if examples[0].items()[i][0]!='Class':
            attributelist.append(examples[0].items()[i][0])
    for i in range(0,len(attributelist)):
        attvalues=[]
        for j in range(0,len(examples)):
            attvalues.append(examples[j].get(attributelist[i]))
        uniqueattributes=list(set(attvalues))
        entropies=[]
        for j in range(0,len(uniqueattributes)):
            attributeexamples=attexamples(attributelist[i],uniqueattributes[j],examples)
            uniqueclass,uniqueclasscount=classcount(attributeexamples)
            maxclass=returnmaxclass(uniqueclass,uniqueclasscount)
            entropies.append(entropy(maxclass,sum(uniqueclasscount)))
        entrope=sum(entropies)
        allentropies.append(entrope)
    for i in range(0,len(attributelist)):
        atts=[]
        for j in range(0,len(examples)):
            atts.append(examples[j].get(attributelist[i]))
        if len(set(atts))==1:
            allentropies[i]=allentropies[i]-5
    bestsplit=max(allentropies)
    ind=allentropies.index(bestsplit)
    return(attributelist[ind],max(allentropies))

def treeform(bestname,examples):
    node=Node()
    node.label=bestname
    node.classification=MODE(examples)
    allclasses=[]
    for i in range(0,len(examples)):
        allclasses.append(examples[i].get('Class'))
    x,y=findbest(examples)
    #print x,y
    if len(examples)!=1 and len(set(allclasses))!=1 and y>-2:
        #print 'pass'
        for i in range(0,len(examples)):
            node.attvals.append(examples[i].get(bestname))
        for i in range(0,len(set(node.attvals))):
            attributeexamples=attexamples(bestname,list(set(node.attvals))[i],examples)
            bestname1,bestentropy=findbest(attributeexamples)
            node.children.update({list(set(node.attvals))[i]:treeform(bestname1,attributeexamples)})
    else:
        node.classification=examples[0].get('Class')
    return node

def prune(node, examples):
  '''
  Takes in a trained tree and a validation set of examples.  Prunes nodes in order
  to improve accuracy on the validation data; the precise pruning strategy is up to you.
  '''
  baseAccuracy = test(node, examples)
  newTree = pruneTree(node)
  newAccuracy = test(newTree, examples)
  if newAccuracy >= baseAccuracy:
    return prune(newTree, examples)
  else:
    return node


def pruneTree(node):
  numchildren = len(node.children)
  if numchildren == 0:
    return node
  for i in range(0, numchildren):
    numGrandChildren = len(node.children.items()[i][1].children)
    if numGrandChildren == 0:
      node.children.pop(node.children.items()[i][0])
      return node
    else: 
      pruneTree(node.children.items()[i][1])
  

def test(node, examples):
  '''
  Takes in a trained tree and a test set of examples.  Returns the accuracy (fraction
  of examples the tree classifies correctly).
  '''
  total = len(examples)
  correct = 0
  for i in range (0, len(examples)):
    #print(examples[i])
    c = traverse(node, examples[i])
    if c == examples[i].get("Class"):
      correct = correct + 1
    #else:
        #print examples[i],c,examples[i].get("Class")
  return float(correct)/total


def traverse(node, example):
  '''
  Helper function for test
  '''
  if len(node.children.items()) == 0:
    return node.classification
  else:
    attsplit = node.label
    attvalue = example.get(attsplit)
    #print attvalue,node.children
    if node.children.get(attvalue)==None:
        return node.classification
    return traverse(node.children.get(attvalue), example)

def evaluate(node, example):
  '''
  Takes in a tree and one example.  Returns the Class value that the tree
  assigns to the example.
  '''
  if len(node.children) > 0:
      attname = node.label
      attvalue = example.get(attname)
      if node.children.get(attvalue)==None:
          return node.classification
      return evaluate(node.children.get(attvalue), example)
  else:
      return node.classification
