print('Code in a loop:')
i = 0
while i < 5:
	print(i, "Hello, world!")
	i = i + 1
	
print('Code in a loop:')
def hello(i = 0):
	print(i, 'Hello, world!')
	i = i + 1
	if i < 5:
		hello(i) # RECURSIVE CASE
	else:
		return # BASE CASE

hello()
	
