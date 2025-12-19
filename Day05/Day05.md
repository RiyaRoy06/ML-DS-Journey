h1 tag # Explanation of the why the set/dict is faster than list:
A list checks elements one by one. This is called linear search. Time Complexity: O(n). For 1 million elements, it may need to check all elements <br>
On the otherhand, set and dictionary use a hash table. A hash function maps the element directly to a memory location. Time Complexity: O(1) <br>
So we can say that set and dictionary are faster because they use hash tables, allowing element lookup in O(1) time, while lists require O(n) time for searching. <br>
