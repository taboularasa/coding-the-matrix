# Collection of functions for converting lists and dictionaries

# Input: a dictionary dct and a list keylist consisting of the keys of dct
# Output: the list L such that L[i] is the value associated in dct with keylist[i]
# Example: dict2list({'a':'A', 'b':'B', 'c':'C'},['b','c','a']) should equal ['B','C','A']
# Complete the procedure definition by replacing [ ... ] with a one-line list comprehension
def dict2list(dct, keylist): return [dct[k] for k in keylist]

# Input: a list L and a list keylist of the same length
# Output: the dictionary that maps keylist[i] to L[i] for i=0,1,...len(L)-1
# Example: list2dict(['A','B','C'],['a','b','c']) should equal {'a':'A', 'b':'B', 'c':'C'}
# Complete the procedure definition by replacing { ... } with a one-line dictionary comprehension
def list2dict(L, keylist): return {keylist[i]: L[i] for i in range(len(L))}

# Input: a list L
# Output: a dictionary that, for i = 0, 1, 2, . . . , len(L) − 1, maps i to L[i]
def listrange2dict(L): return {i: L[i] for i in range(len(L)) }
