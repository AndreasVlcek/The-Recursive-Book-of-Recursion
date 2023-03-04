def shortestWithBaseCase(makeRecursiveCall):
	print('shortestWithBaseCase(%s) called.' %makeRecursiveCall)
	if not makeRecursiveCall:
		# BASE CASE
		print('Returning from base case.')
		return
	else:
		# RECURSICE CASE
		shortestWithBaseCase(False)
		print('Returning from recursive case.')
		return

print('Calling shortestWithBaseCase(False):')
shortestWithBaseCase(False)
print()
print('Calling shortestWithBaseCase(True):')
shortestWithBaseCase(True)