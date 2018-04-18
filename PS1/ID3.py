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

    #checkTrivialCases(examples)

    best,bestname,entropies=findbest(examples)
    tree=treeform(bestname,best,examples)
    return tree


def treeform(bestname,best,examples):
    node=Node()
    node.label=bestname
    node.mode=MODE(examples)
    if len(examples)!=1 and examples[0].items()[0][0]!='Class':
        for i in range(0,len(examples)):
            node.attvals.append(examples[i].get(bestname))
        for i in range(0,len(set(node.attvals))):
            attributeexamples=attexamples(bestname,best,list(set(node.attvals))[i],examples)
            for j in range(0,len(attributeexamples)):
                attributeexamples[j].pop(bestname,None)
            #print(attributeexamples,len(attributeexamples))
            #print len(attributeexamples[0].items()),attributeexamples[0].items()

            if len(attributeexamples[0].items())==1:
                newnode=Node()
                newnode.classification=attributeexamples[0].get('Class')
                node.children.update({list(set(node.attvals))[i]:newnode})
            else:
                #print(attributeexamples)
                best1,bestname1,entropies1=findbest(attributeexamples)
                node.children.update({list(set(node.attvals))[i]:treeform(bestname1,best1,attributeexamples)})
    else:
        node.classification=examples[0].get('Class')
    return node

def MODE(examples):
    a,b=classcount(examples)
    ii=b.index(max(b))
    return a[ii]

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
    return attex

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
            ax=returnmaxclass(x,y)
            entropies.append(entropy(ax,sum(y)))
        entrope=sum(entropies)
        allentropies.append(entrope)
    bestsplit=max(allentropies)
    ind=allentropies.index(bestsplit)
    return(ind,examples[0].items()[ind][0],allentropies)


def checkTrivialCases(examples):
    UClassList, UCCounts = classcount(examples)
    index = max(UCCounts).index()
    mode = UClassList[index]
    done = false
    for i in range (0, len(examples)):
      examples[i].pop("Class")
    for i in range (0, len(examples)):
      if done == true:
        break
      check = examples[i]
      for j in range( (i + 1), len(examples) ):
        if check != examples[j]:
          done = true;
          break
    if done == false:
      return mode


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
  if len(node.children) > 0:
    attname = node.label
    attvalue = example.get(attname)
    if node.children.get(attvalue)==None:
        return node.mode
    return evaluate(node.children.get(attvalue), example)
  else:
    return node.classification
