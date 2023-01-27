"""
Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string. 

Examples: end_other('Hiabc', 'abc') → True end_other('AbC', 'HiaBc') → True end_other('abc', 'abXabc') → True

"""
def end_other(str1,str2):
 if(str1.lower().endswith(str2.lower()) or str2.lower().endswith(str1.lower())):
  return True
 else:
  return False

print(end_other('Hiabc','abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))