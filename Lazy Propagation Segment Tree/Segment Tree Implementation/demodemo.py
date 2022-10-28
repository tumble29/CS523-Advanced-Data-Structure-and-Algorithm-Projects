import time
import random
from math import ceil, log2

    

MIN_VALUE=-10
MAX_VALUE=10
MAX = 20
UPDATES=10

def randomArray(): #return a random array 
    a=[random.randint( MIN_VALUE, MAX_VALUE) for i in range(MAX)]
    return a
#Tree Functions
def randomUpdate(): #Return a list of [update type, starting index, ending index, random value]
    utype=random.randint(0,1)
    ss=random.randint(0,MAX-1)
    se=random.randint(ss,MAX-1)
    if (utype):
       new_value=random.randint( MIN_VALUE, MAX_VALUE)
       return [utype,ss,se,new_value]
    return [utype, ss,se]
def randomQuery(): #Return a list of [starting index, ending index]
    ss=random.randint(0,MAX)
    se=random.randint(ss,MAX)
    return [ss,se]

st = [0] * MAX

def getMid(s, e):
    return s + (e - s) // 2

def getSumUtil(st, ss, se, qs, qe, si):

    if (qs <= ss and qe >= se):
        return st[si]
    if (se < qs or ss > qe):
        return 0
    mid = getMid(ss, se)

    return getSumUtil(st, ss, mid, qs, qe, 2 * si + 1) + getSumUtil(st, mid + 1, se, qs, qe, 2 * si + 2)

def updateValueUtil(st, ss, se, i, diff, si):

    if (i < ss or i > se):
        return
    st[si] = st[si] + diff

    if (se != ss):
        mid = getMid(ss, se)
        updateValueUtil(st, ss, mid, i,
                        diff, 2 * si + 1)
        updateValueUtil(st, mid + 1, se, i,
                        diff, 2 * si + 2)
        
def updateValue(arr, st, n, i, new_val):

    if (i < 0 or i > n - 1):
        print("Input khong hop le", end="")
        return
    diff = new_val - arr[i]
    arr[i] = new_val
    updateValueUtil(st, 0, n - 1, i, diff, 0)

def updateRangeOfValue(arr,st,n,ss,se,new_val):
    while(ss<=se):
        updateValue(arr,st,n,ss,new_val)
        ss=ss+1


def getSum(st, n, qs, qe):

    if (qs < 0 or qe > n - 1 or qs > qe):
        print("Input khong hop le", end="")
        return -1

    return getSumUtil(st, 0, n - 1, qs, qe, 0)

def constructSTUtil(arr, ss, se, st, si):

    if (ss == se):
        st[si] = arr[ss]
        return arr[ss]
    mid = getMid(ss, se)
    st[si] = constructSTUtil(arr, ss, mid, st, si * 2 + 1) + constructSTUtil(arr, mid + 1, se, st, si * 2 + 2)
    return st[si]



def constructST(arr, n):

    x = (int)(ceil(log2(n)))
    max_size = 2 * (int)(2 ** x) - 1
    st = [0] * max_size
    constructSTUtil(arr, 0, n - 1, st, 0)
    return st

#Lazy Propagation Segment Tree Functions


def _updateRangeUtil(tree,lazy, si, ss, se, us, ue, diff):

    if (lazy[si] != 0):
        tree[si] += (se - ss + 1) * lazy[si]
        if (ss != se):
            lazy[si * 2 + 1] += lazy[si]
            lazy[si * 2 + 2] += lazy[si]
        lazy[si] = 0
    if (ss > se or ss > ue or se < us):
        return
    if (ss >= us and se <= ue):
        tree[si] += (se - ss + 1) * diff
        if (ss != se):
            lazy[si * 2 + 1] += diff
            lazy[si * 2 + 2] += diff
        return
    mid = (ss + se) // 2
    _updateRangeUtil(tree,lazy,si * 2 + 1, ss,
                    mid, us, ue, diff)
    _updateRangeUtil(tree,lazy,si * 2 + 2, mid + 1,
                    se, us, ue, diff)
    tree[si] = tree[si * 2 + 1] + tree[si * 2 + 2]

def _updateRange(tree, lazy, n, us, ue, diff):
    _updateRangeUtil(tree,lazy, 0, 0, n - 1, us, ue, diff)

def _getSumUtil(tree,lazy, ss, se, qs, qe, si):

    if (lazy[si] != 0):
        tree[si] += (se - ss + 1) * lazy[si]
        if (ss != se):
            lazy[si * 2 + 1] += lazy[si]
            lazy[si * 2 + 2] += lazy[si]
        lazy[si] = 0
    if (ss > se or ss > qe or se < qs):
        return 0
    if (ss >= qs and se <= qe):
        return tree[si]
    mid = (ss + se) // 2
    return (_getSumUtil(tree,lazy, ss, mid, qs, qe, 2 * si + 1) +
            _getSumUtil(tree, lazy,mid + 1, se, qs, qe, 2 * si + 2))

def _getSum(tree, lazy, n, qs, qe):
    if (qs < 0 or qe > n - 1 or qs > qe):
        print("Input khong hop le")
        return -1
    return _getSumUtil(tree,lazy, 0, n - 1, qs, qe, 0);

            

def updateST(arr,st,updates):
    for i in updates: 
        if i[0]==0:
            print(getSum(st,len(arr),i[1],i[2]))
        else:
            updateRangeOfValue(arr,st,len(arr),i[1],i[2],i[3])

def updateLST(arr, lst,lazy, updates):
    for i in updates:
        if i[0]==0:
            print(_getSum(lst,lazy,len(arr),i[1],i[2]))
        else:
            _updateRange(lst,lazy,len(arr),i[1],i[2],i[3])

arr = randomArray()
st = constructST(arr, len(arr)) 
lst=st
lazy=[0]*len(lst)
updates =[] #List of random updates to the tree
queries=[]  #List of random queries to the tree
for i in range(UPDATES):
    updates.append(randomUpdate())

print("Tinh thoi gian de cap nhat cac phan tu cua ST")
start = time.time()
updateST(arr,st,updates)
end = time.time()
print("Da cap nhat xong ST trong vong "+ str(end-start)+" giay")



print("Tinh thoi gian de cap nhat cac phan tu cua LPST")
start = time.time()
updateLST(arr,lst,lazy,updates)
end = time.time()
print("Da cap nhat xong LPST trong vong "+ str(end-start)+" giay")
print("END")


    #print("Ket qua: ",
    #      getSum(st, n, 1, 3))
    #updateValue(arr, st, n, 1, 10)
    #print("Ket qua sau khi update: ",
    #      getSum(st, n, 1, 3), end="")
