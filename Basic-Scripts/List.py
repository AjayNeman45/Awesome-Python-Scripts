#!/usr/bin/python
spam = ['ankit','arjun','arun']
print(spam) # output : ['ankit','arjun','arun']
spam.append('anurag')
print(spam) # append element at the last position of the array. output : ['ankit','arjun','arun','anurag']
spam.insert(1,'elliot')
print(spam) # output : ['ankit','elliot','arjun','arun,'anurag']
spam.pop(1)
print(spam) # removes the element from the array given at that position of index. output : ['ankit','arjun','arun','anurag']
spam.remove('arun')
print(spam) # output : ['ankit','elliot','arjun','anurag']
print(spam.index('anurag')) # return the index of the first matched item. output : 3
spam.reverse()
print(spam) # reverse the element of the array. output : ['anurag','arjun','elliot','ankit']
spam.clear()
print(spam) # Removes all the element the array. output : []
