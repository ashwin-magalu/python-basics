list1 = [1, 2, 3, 4, 5, 6]
list2 = ["one", "two", "three", 'four', "five"]
list3 = ["ONE", "TWO", 'THREE', 'FOUR', 'FIVE']

zipped = list(zip(list1, list2))
print(zipped)
# [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')]
# here 6 is truncated as it don't have any pair

zipped = list(zip(list1, list2, list3))
print(zipped)
#[(1, 'one', 'ONE'), (2, 'two', 'TWO'), (3, 'three', 'THREE'), (4, 'four', 'FOUR'), (5, 'five', 'FIVE')]

unzipped = list(zip(*zipped))
print(unzipped)
#[(1, 2, 3, 4, 5), ('one', 'two', 'three', 'four', 'five'), ('ONE', 'TWO', 'THREE', 'FOUR', 'FIVE')]

for (l1, l2) in zip(list1, list2):
    print(l1)
    print(l2)
""" 
1
one
2
two
3
three
4
four
5
five
"""

items = ["Apple", "Banana", "Orange"]
counts = [3, 6, 4]
prices = [100, 40, 70]

sentences = []
for (item, count, price) in zip(items, counts, prices):
    count, price = str(count), str(price)
    sentence = "I bought "+count+" "+item+"s for Rs."+price+"/-."
    sentences.append(sentence)

print(sentences)
#['I bought 3 Apples for Rs.100/-.', 'I bought 6 Bananas for Rs.40/-.', 'I bought 4 Oranges for Rs.70/-.']
