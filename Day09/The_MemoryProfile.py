# Goal: Compare sys.getsizeof() of a list Comprehension vs Generator Expression for 1 million numbers.

import sys
list_expression=[x for x in range(1000000)]
generator_expression=(x for x in range(1000000))
print("List Comprehension size: ",sys.getsizeof(list_expression),"bytes")
print("Generator Expression size: ",sys.getsizeof(generator_expression),"bytes")
