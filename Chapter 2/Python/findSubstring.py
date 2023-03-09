def findSubstringIterative(needle, haystack):
	i = 0
	while i < len(haystack):
		if haystack[i:i + len(needle)] == needle:
			return i # Needle found.
		i = i + 1
	return - 1 # Needle not found.

def findSubstringRecursive(needle, haystack, i=0):
	if i >= len(haystack):
		return -1 # BASE CASE (Needle not found.)
	
	if haystack[i:i + len(needle)] == needle:
		return i # BASE CASE (Needle found.)
	else:
		# RECURSIVE CASE
		return findSubstringRecursive(needle, haystack, i + 1)	

print(findSubstringIterative('cat', 'my cat Zophie'))
print(findSubstringRecursive('cat', 'my cat Zophie'))