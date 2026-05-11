import sys

args = sys.argv

if (len(args) == 1):
	sys.exit()

try:
	assert len(args) <= 2, "more than one argument is provided"
	value = args[1]
	if value[0] == '-':
		value = value.lstrip('-')
	assert value.isdigit(), "argument is not an integer"
except AssertionError as e:
	print(f"AssertionError: {e}")
	sys.exit()

if int(value) % 2 > 0:
	print("I'm Odd.")
else:
	print("I'm Even.")