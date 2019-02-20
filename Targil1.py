
import heapq
from functools import reduce

##-------------------------------Question 1-------------------------------#
def upper_half(matrix):
    return [y[x::] for x,y in enumerate(matrix,0)]
    pass

##-------------------------------Question 2-------------------------------#
def encrypt(string, key = 1):
    afterEncrypt = ""
    cut1 = 0
    cut2 = 1

    for i in range(len(string)):
        charToConvert = string[cut1:cut2] #slicing the string eachtime 1 letter until the end
        charASCII = (ord(charToConvert) + key) #get the ASCII code of each letter before checking bir ot small

        if 122 < charASCII: #check of the letter is big or small
            charToAdd = chr(ord(charToConvert) - 26 + key)
        else:
            charToAdd = chr(ord(charToConvert) + key)

        afterEncrypt += charToAdd #add the letter after encryption to the new string
        cut1 += 1
        cut2 += 1
        pass
    return afterEncrypt
    pass

##-------------------------------Question 3-------------------------------#
def sum_digits1(n): #with regular arithmetic expressions
    nAfterSum = 0
    while n > 0:
        nAfterSum += n % 10
        n = n//10
        pass
    return nAfterSum
    pass

def sum_digits2(n): #with convartion to string and manipulating with slicing
    nAfterSum = 0
    nAsStr = str(n) #convert to a string
    for i in range(len(nAsStr)): #run on the string length
        nAfterSum += int(nAsStr[i:i+1]) #each time slice the string and comvert it using int function, than sum it to nAfterSum
        pass
    return nAfterSum
    pass

##-------------------------------Question 4-------------------------------#
def reducefunc(x, y):
    updatedList = [] #updated list to return, made from all the elements in the 2 lists
    for i in range(len(x)):
        updatedList.append(x[i]) #add all the elements from the first list to the new one
        pass

    for j in range(len(y)):
        updatedList.append(y[j]) #add all the elements from the second list to the new one
        pass

    return updatedList #return the new list
    pass

def flatten(alist):
    return reduce(reducefunc , alist) #reduce takes the first 2 pairs(in that case 2 lists) and a function to work on both, and than return a elemnt(in that case a list),
                                      #after that, takes the element that was returned with the 3rd and so on
    pass

##-------------------------------Question 5-------------------------------#
def dijkstra(graph,weights,source):

    INFINITY = 1000000
    heap=[]
    routDict=dict()

    for i in (graph):
        routDict[i]=INFINITY
        pass

    routDict[source]=0
    i=source

    while(i in (graph)):
        nodes=graph[i]
        if (nodes==[]):
            break
        for j in (nodes):
            tupple=(i,j)
            if (tupple in (weights)):
                distance=weights[tupple]
            if (distance+routDict[i]<routDict[j]):
                routDict[j]=distance+routDict[i]
            heapq.heappush(heap,(distance+routDict[i],j))
        next=heapq.heappop(heap)
        i=next[1]

    for i in (routDict):
        if (routDict[i]==INFINITY):
            routDict[i]="infinity"
    return (routDict)
    pass

#############################################################################################
#############################################################################################
#############################################################################################
# Start Tests

#1st Question
def test_upper_half():
    assert (upper_half([]) == [])
    assert (upper_half([[1,2,3,4],[5,6,7,8],[7,8,9,10],[11,12,13,14]]) == [[1,2,3,4],[6,7,8],[9,10],[14]])
    assert (upper_half([[1,2,3,4] , [5,6,7,8]]) == [[1,2,3,4],[6,7,8]])
    assert (upper_half([[1, 2, 3, 4, 5], [6, 7, 8, 9, "spam"] , [11, 12, 13 ,14, 15], [16, "stam", 18, 19, 20]]) == [[1, 2, 3, 4, 5], [7, 8, 9, "spam"], [13, 14 ,15] , [19, 20]])
    pass

#2nd Question
def test_encrypt():
    assert (encrypt("spam") == "tqbn")
    assert (encrypt("spam", 3) == "vsdp")
    assert (encrypt("soft", 5) == "xtky")
    assert (encrypt("zyzz", 7) == "gfgg")
    pass

#3rd Question
def test_sum_digits1():
    assert (sum_digits1(1492) == 16)
    assert (sum_digits1(784) == 19)
    assert (sum_digits1(67342) == 22)
    assert (sum_digits1(968634) == 36)
    pass

def test_sum_digits2():
    assert (sum_digits2(1492) == 16)
    assert (sum_digits2(784) == 19)
    assert (sum_digits2(67342) == 22)
    assert (sum_digits2(968634) == 36)
    pass

#4th Question
def test_flatten():
    assert (flatten([[1, 2, 3], ['foo', 'bar'], [], [[1, 2], [3]]]) == [1, 2, 3,'foo','bar',[1, 2], [3]])
    assert (flatten([[1, 2], ['foo', 'ba', ['r']], [], [[1, 2], [3]]]) == [1, 2, 'foo', 'ba', ['r'] , [1, 2], [3]])
    pass

#5th Question
def test_dijkstra():
    graph = {'a': ['b', 'c'], 'b': ['d'], 'c': [], 'd': ['c', 'e'], 'e': [], 'f': ['e']}
    weights = {('a', 'b'): 2, ('a', 'c'): 10, ('b', 'd'): 3, ('d', 'c'): 1, ('d', 'e'): 12, ('f', 'e'): 0}

    assert dijkstra(graph, weights, 'a') == ({'a': 0, 'b': 2, 'c': 6, 'd': 5, 'e': 17, 'f': 'infinity'})
    assert dijkstra(graph, weights, 'b') == ({'a': 'infinity', 'b': 0, 'c': 4, 'd': 3, 'e': 15, 'f': 'infinity'})
    assert dijkstra(graph, weights, 'f') == ({'a': 'infinity', 'b': 'infinity', 'c': 'infinity', 'd': 'infinity', 'e': 0, 'f': 0})
    pass


test_upper_half()
test_encrypt()
test_sum_digits1()
test_sum_digits2()
test_flatten()
test_dijkstra()







