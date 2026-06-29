"""
=====================================================================
 VARIABLES — LEVEL 2: INTERMEDIATE  (fully explained, no functions)
=====================================================================
Now we store MANY values in one variable: lists, tuples, dicts, sets.
Same teaching labels as Level 1:

    WHAT / SYNTAX / PARAMS / RETURNS / WHY / WHEN / MISTAKE

Every line is commented, and the OUTPUT is shown.
Run it:   python variables_2_intermediate.py
=====================================================================
"""

print("LEVEL 2 — INTERMEDIATE\n")


# ════════════════════════════════════════════════════════════════
# EXAMPLE 1 — Creating a list
# ════════════════════════════════════════════════════════════════
# WHAT   : A list stores MANY values in order, in one variable.
# SYNTAX : my_list = [value1, value2, value3]
# WHY    : To keep a group of related items together.
# WHEN   : Any time you have a collection (names, numbers, etc.).
# MISTAKE: Use square brackets [ ] for lists (curly { } make a dict/set).

fruits = ["apple", "banana", "cherry"]   # 3 strings inside [ ] -> a list
print(fruits)                            # show the whole list
# OUTPUT: ['apple', 'banana', 'cherry']


# ════════════════════════════════════════════════════════════════
# EXAMPLE 2 — Getting an item by position (indexing)
# ════════════════════════════════════════════════════════════════
# WHAT   : Read one item from a list by its position number.
# SYNTAX : my_list[position]
# WHY    : To use a specific item.
# WHEN   : Whenever you need one element.
# MISTAKE: Counting starts at 0, so the FIRST item is my_list[0].

fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # position 0 = the first item  -> apple
print(fruits[1])   # position 1 = the second item -> banana
# OUTPUT:
# apple
# banana


# ════════════════════════════════════════════════════════════════
# EXAMPLE 3 — Negative indexing (counting from the end)
# ════════════════════════════════════════════════════════════════
# WHAT   : Negative positions count backwards from the end.
# SYNTAX : my_list[-1]   (the last item)
# WHY    : Easy way to reach the end without knowing the length.
# WHEN   : Getting the last (or second-to-last) item.

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])  # -1 = last item        -> cherry
print(fruits[-2])  # -2 = second from last -> banana
# OUTPUT:
# cherry
# banana


# ════════════════════════════════════════════════════════════════
# EXAMPLE 4 — Slicing a list (getting several items)
# ════════════════════════════════════════════════════════════════
# WHAT   : Take a section of a list.
# SYNTAX : my_list[start:stop]   (stop is NOT included)
# RETURNS: a NEW list with the chosen items.
# WHY    : To work with part of a list.
# WHEN   : Getting the first N items, a middle section, etc.

nums = [10, 20, 30, 40, 50]
print(nums[1:4])   # positions 1,2,3 -> [20, 30, 40]
print(nums[:2])    # from start to 2 -> [10, 20]
print(nums[3:])    # from 3 to end   -> [40, 50]
# OUTPUT:
# [20, 30, 40]
# [10, 20]
# [40, 50]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 5 — append() : add an item to the end
# ════════════════════════════════════════════════════════════════
# WHAT   : .append() adds one item to the end of a list.
# SYNTAX : my_list.append(item)
# PARAMS : item -> the value to add.
# RETURNS: nothing (it changes the list in place).
# WHY    : To grow a list as you go.
# WHEN   : Building up a list one item at a time.

fruits = ["apple", "banana"]
fruits.append("cherry")   # add "cherry" to the end
print(fruits)             # -> ['apple', 'banana', 'cherry']
# OUTPUT: ['apple', 'banana', 'cherry']


# ════════════════════════════════════════════════════════════════
# EXAMPLE 6 — insert() : add an item at a position
# ════════════════════════════════════════════════════════════════
# WHAT   : .insert() puts an item at a chosen position.
# SYNTAX : my_list.insert(position, item)
# PARAMS : position -> where to put it; item -> the value.
# RETURNS: nothing (changes the list in place).
# WHY    : When order matters and you need it somewhere specific.
# WHEN   : Adding to the front or middle.

fruits = ["apple", "cherry"]
fruits.insert(1, "banana")   # put "banana" at position 1
print(fruits)                # -> ['apple', 'banana', 'cherry']
# OUTPUT: ['apple', 'banana', 'cherry']


# ════════════════════════════════════════════════════════════════
# EXAMPLE 7 — remove() : delete an item by value
# ════════════════════════════════════════════════════════════════
# WHAT   : .remove() deletes the first matching value.
# SYNTAX : my_list.remove(value)
# PARAMS : value -> the item to remove.
# RETURNS: nothing (changes the list in place).
# WHY    : To take an item out by what it is.
# WHEN   : Removing a known value.
# MISTAKE: Removing a value that isn't there causes an error.

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")   # delete "banana"
print(fruits)             # -> ['apple', 'cherry']
# OUTPUT: ['apple', 'cherry']


# ════════════════════════════════════════════════════════════════
# EXAMPLE 8 — pop() : remove by position and get it back
# ════════════════════════════════════════════════════════════════
# WHAT   : .pop() removes an item by position AND returns it.
# SYNTAX : my_list.pop(position)   (position is optional; default last)
# PARAMS : position -> which item (optional).
# RETURNS: the removed item.
# WHY    : When you want to use the item you remove.
# WHEN   : Taking the last item off, processing a "stack".

nums = [10, 20, 30]
last = nums.pop()    # remove and return the LAST item (30)
print(last)          # -> 30
print(nums)          # -> [10, 20]
# OUTPUT:
# 30
# [10, 20]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 9 — Changing an item
# ════════════════════════════════════════════════════════════════
# WHAT   : Replace an item by assigning to its position.
# SYNTAX : my_list[position] = new_value
# WHY    : Lists are CHANGEABLE — you can edit them in place.
# WHEN   : Updating a value.

fruits = ["apple", "banana", "cherry"]
fruits[0] = "mango"    # replace the item at position 0
print(fruits)          # -> ['mango', 'banana', 'cherry']
# OUTPUT: ['mango', 'banana', 'cherry']


# ════════════════════════════════════════════════════════════════
# EXAMPLE 10 — len() on a list
# ════════════════════════════════════════════════════════════════
# WHAT   : len() counts how many items are in the list.
# SYNTAX : len(my_list)
# RETURNS: a whole number.
# WHY    : To know the size.
# WHEN   : Loops, checks, "how many?" questions.

fruits = ["apple", "banana", "cherry"]
print(len(fruits))   # -> 3
# OUTPUT: 3


# ════════════════════════════════════════════════════════════════
# EXAMPLE 11 — A list can hold mixed types
# ════════════════════════════════════════════════════════════════
# WHAT   : Items in a list can be different types.
# WHY    : Flexible, but usually keep one type for clarity.
# WHEN   : Occasionally useful (e.g. a row of mixed data).

mixed = ["text", 42, 3.5, True]   # str, int, float, bool together
print(mixed)
# OUTPUT: ['text', 42, 3.5, True]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 12 — 'in' : is a value inside the list?
# ════════════════════════════════════════════════════════════════
# WHAT   : 'in' checks membership (True/False).
# SYNTAX : value in my_list
# RETURNS: True or False.
# WHY    : To test whether something is present.
# WHEN   : Before using/adding an item.

fruits = ["apple", "banana"]
print("apple" in fruits)    # -> True
print("grape" in fruits)    # -> False
# OUTPUT:
# True
# False


# ════════════════════════════════════════════════════════════════
# EXAMPLE 13 — sorted() vs .sort()
# ════════════════════════════════════════════════════════════════
# WHAT   : Both order a list, but differently.
# SYNTAX : sorted(my_list)  -> returns a NEW sorted list
#          my_list.sort()   -> sorts the list IN PLACE, returns nothing
# WHY    : sorted() keeps the original; .sort() changes it.
# WHEN   : Use sorted() when you still need the original order.
# MISTAKE: x = my_list.sort() gives None (sort returns nothing).

nums = [3, 1, 2]
print(sorted(nums))   # NEW sorted list -> [1, 2, 3]
print(nums)           # original UNCHANGED -> [3, 1, 2]
nums.sort()           # now sort IN PLACE
print(nums)           # original changed -> [1, 2, 3]
# OUTPUT:
# [1, 2, 3]
# [3, 1, 2]
# [1, 2, 3]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 14 — reverse() : flip the order in place
# ════════════════════════════════════════════════════════════════
# WHAT   : .reverse() reverses the list in place.
# SYNTAX : my_list.reverse()
# RETURNS: nothing (changes the list in place).
# WHY    : To flip the order of items.
# WHEN   : Reversing data; or use [::-1] for a new reversed list.

nums = [1, 2, 3]
nums.reverse()    # flip it in place
print(nums)       # -> [3, 2, 1]
print([1, 2, 3][::-1])   # slicing makes a NEW reversed list -> [3, 2, 1]
# OUTPUT:
# [3, 2, 1]
# [3, 2, 1]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 15 — Creating a tuple
# ════════════════════════════════════════════════════════════════
# WHAT   : A tuple is like a list but UNCHANGEABLE (fixed).
# SYNTAX : my_tuple = (value1, value2)
# WHY    : For data that should never change (safer).
# WHEN   : Fixed pairs/records like coordinates, RGB colours.
# MISTAKE: A single-item tuple needs a comma: (5,) not (5).

point = (10, 20)     # two values in ( ) -> a tuple
print(point)         # -> (10, 20)
one = (5,)           # the comma makes it a tuple, not just the number 5
print(type(one).__name__)   # -> tuple
# OUTPUT:
# (10, 20)
# tuple


# ════════════════════════════════════════════════════════════════
# EXAMPLE 16 — Tuple indexing
# ════════════════════════════════════════════════════════════════
# WHAT   : Read a tuple item by position (same as lists).
# SYNTAX : my_tuple[position]
# WHY    : To use a specific value.
# WHEN   : Accessing parts of a fixed record.

point = (10, 20)
print(point[0])   # -> 10
print(point[1])   # -> 20
# OUTPUT:
# 10
# 20


# ════════════════════════════════════════════════════════════════
# EXAMPLE 17 — Tuple unpacking (split into variables)
# ════════════════════════════════════════════════════════════════
# WHAT   : Spread a tuple's values into separate variables.
# SYNTAX : a, b = my_tuple
# WHY    : Cleaner than point[0], point[1] everywhere.
# WHEN   : Reading the parts of a pair/record into named variables.

point = (10, 20)
x, y = point        # x gets 10, y gets 20
print(x, y)         # -> 10 20
# OUTPUT: 10 20


# ════════════════════════════════════════════════════════════════
# EXAMPLE 18 — Tuples are immutable (cannot change)
# ════════════════════════════════════════════════════════════════
# WHAT   : You cannot change a tuple after creating it.
# WHY    : Safety — fixed data can't be edited by accident.
# WHEN   : Knowing the difference from lists.
# MISTAKE: point[0] = 99 on a tuple causes a TypeError.

point = (10, 20)
# point[0] = 99   # <-- this line would ERROR, so it's a comment
print("tuples cannot be changed; lists can")
# OUTPUT: tuples cannot be changed; lists can


# ════════════════════════════════════════════════════════════════
# EXAMPLE 19 — Creating a dictionary
# ════════════════════════════════════════════════════════════════
# WHAT   : A dict stores KEY -> VALUE pairs (a labelled lookup table).
# SYNTAX : my_dict = {"key": value, "key2": value2}
# WHY    : To label data so you fetch it by name, not position.
# WHEN   : Records with named fields (a person, a config, etc.).

person = {"name": "Lily", "age": 22}   # 'name' and 'age' are keys
print(person)
# OUTPUT: {'name': 'Lily', 'age': 22}


# ════════════════════════════════════════════════════════════════
# EXAMPLE 20 — Reading a value by its key
# ════════════════════════════════════════════════════════════════
# WHAT   : Use the key in [ ] to get its value.
# SYNTAX : my_dict["key"]
# WHY    : To fetch a specific labelled value.
# WHEN   : Reading a field.
# MISTAKE: Asking for a missing key with [ ] causes a KeyError (see Ex 21).

person = {"name": "Lily", "age": 22}
print(person["name"])   # -> Lily
print(person["age"])    # -> 22
# OUTPUT:
# Lily
# 22


# ════════════════════════════════════════════════════════════════
# EXAMPLE 21 — .get() : safe lookup with a default
# ════════════════════════════════════════════════════════════════
# WHAT   : .get() reads a key but won't crash if it's missing.
# SYNTAX : my_dict.get("key", default)
# PARAMS : key -> what to look up; default -> value if key is missing.
# RETURNS: the value, or the default.
# WHY    : Avoids KeyError crashes for optional fields.
# WHEN   : When a key might not exist.

person = {"name": "Lily"}
print(person.get("age", "unknown"))   # 'age' missing -> default "unknown"
# OUTPUT: unknown


# ════════════════════════════════════════════════════════════════
# EXAMPLE 22 — Adding and updating dictionary values
# ════════════════════════════════════════════════════════════════
# WHAT   : Assign to a key to add it (new) or update it (existing).
# SYNTAX : my_dict["key"] = value
# WHY    : To build or change records.
# WHEN   : Filling in or editing fields.

person = {"name": "Lily"}
person["age"] = 22       # key didn't exist -> ADDS it
person["name"] = "Lila"  # key existed      -> UPDATES it
print(person)            # -> {'name': 'Lila', 'age': 22}
# OUTPUT: {'name': 'Lila', 'age': 22}


# ════════════════════════════════════════════════════════════════
# EXAMPLE 23 — Removing a key
# ════════════════════════════════════════════════════════════════
# WHAT   : Delete a key/value pair.
# SYNTAX : del my_dict["key"]   OR   my_dict.pop("key")
# WHY    : To remove a field you no longer need.
# WHEN   : Cleaning up data.

person = {"name": "Lily", "age": 22, "city": "Rome"}
del person["city"]        # remove the 'city' pair
print(person)             # -> {'name': 'Lily', 'age': 22}
removed = person.pop("age")   # remove 'age' AND get its value
print(removed, person)        # -> 22 {'name': 'Lily'}
# OUTPUT:
# {'name': 'Lily', 'age': 22}
# 22 {'name': 'Lily'}


# ════════════════════════════════════════════════════════════════
# EXAMPLE 24 — keys(), values(), items()
# ════════════════════════════════════════════════════════════════
# WHAT   : Get all keys, all values, or all key-value pairs.
# SYNTAX : my_dict.keys()  /  my_dict.values()  /  my_dict.items()
# RETURNS: special view objects (wrap in list() to see them clearly).
# WHY    : To look at everything in the dict.
# WHEN   : Inspecting or processing all entries.

person = {"name": "Lily", "age": 22}
print(list(person.keys()))     # -> ['name', 'age']
print(list(person.values()))   # -> ['Lily', 22]
print(list(person.items()))    # -> [('name', 'Lily'), ('age', 22)]
# OUTPUT:
# ['name', 'age']
# ['Lily', 22]
# [('name', 'Lily'), ('age', 22)]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 25 — Checking if a key exists ('in')
# ════════════════════════════════════════════════════════════════
# WHAT   : 'in' on a dict checks for a KEY (not a value).
# SYNTAX : "key" in my_dict
# RETURNS: True or False.
# WHY    : To safely check before reading a key.
# WHEN   : Avoiding KeyError.

person = {"name": "Lily", "age": 22}
print("name" in person)    # is there a 'name' key? -> True
print("email" in person)   # is there an 'email' key? -> False
# OUTPUT:
# True
# False


# ════════════════════════════════════════════════════════════════
# EXAMPLE 26 — Creating a set
# ════════════════════════════════════════════════════════════════
# WHAT   : A set holds only UNIQUE values, in no particular order.
# SYNTAX : my_set = {value1, value2}
# WHY    : To remove duplicates or do "membership" math.
# WHEN   : Unique collections, comparing groups.
# MISTAKE: {} makes an empty DICT, not a set. Use set() for an empty set.

colors = {"red", "green", "red", "blue"}   # the duplicate "red" is dropped
print(len(colors))   # 3 unique colors -> 3
# OUTPUT: 3


# ════════════════════════════════════════════════════════════════
# EXAMPLE 27 — Using a set to remove duplicates from a list
# ════════════════════════════════════════════════════════════════
# WHAT   : Convert a list to a set to drop repeats.
# SYNTAX : set(my_list)
# RETURNS: a set of the unique items.
# WHY    : Quick de-duplication.
# WHEN   : Cleaning data with repeats.

nums = [1, 2, 2, 3, 3, 3]
unique = set(nums)         # duplicates removed
print(unique)              # -> {1, 2, 3}
print(sorted(unique))      # back to a sorted list -> [1, 2, 3]
# OUTPUT:
# {1, 2, 3}
# [1, 2, 3]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 28 — add() and remove() on a set
# ════════════════════════════════════════════════════════════════
# WHAT   : Sets can change: add or remove items.
# SYNTAX : my_set.add(item)  /  my_set.remove(item)
# RETURNS: nothing (changes the set in place).
# WHY    : To build/update a unique collection.
# WHEN   : Tracking seen items, tags, etc.

colors = {"red", "green"}
colors.add("blue")      # add a new color
colors.add("red")       # already there -> no duplicate added
print(len(colors))      # -> 3
# OUTPUT: 3


# ════════════════════════════════════════════════════════════════
# EXAMPLE 29 — Union | : everything in either set
# ════════════════════════════════════════════════════════════════
# WHAT   : Combine two sets (no duplicates).
# SYNTAX : set_a | set_b
# RETURNS: a new set with items from both.
# WHY    : To merge groups.
# WHEN   : "All items across both".

print({1, 2} | {2, 3})    # -> {1, 2, 3}
# OUTPUT: {1, 2, 3}


# ════════════════════════════════════════════════════════════════
# EXAMPLE 30 — Intersection & : items in BOTH sets
# ════════════════════════════════════════════════════════════════
# WHAT   : Keep only items present in both sets.
# SYNTAX : set_a & set_b
# RETURNS: a new set of the shared items.
# WHY    : To find what's common.
# WHEN   : "What do these two have in common?".

print({1, 2, 3} & {2, 3, 4})    # -> {2, 3}
# OUTPUT: {2, 3}


# ════════════════════════════════════════════════════════════════
# EXAMPLE 31 — Difference - : in the first but not the second
# ════════════════════════════════════════════════════════════════
# WHAT   : Items in set_a that are NOT in set_b.
# SYNTAX : set_a - set_b
# RETURNS: a new set.
# WHY    : To find what's missing/extra.
# WHEN   : "What's only in A?".

print({1, 2, 3} - {2})    # -> {1, 3}
# OUTPUT: {1, 3}


# ════════════════════════════════════════════════════════════════
# EXAMPLE 32 — Splitting text into a list of words
# ════════════════════════════════════════════════════════════════
# WHAT   : .split() breaks text into a list.
# SYNTAX : text.split(separator)   (separator optional; default = spaces)
# PARAMS : separator -> where to cut (optional).
# RETURNS: a list of pieces.
# WHY    : To process words or fields.
# WHEN   : Reading sentences, CSV lines, etc.

sentence = "learn python today"
words = sentence.split()   # split on spaces by default
print(words)               # -> ['learn', 'python', 'today']
print("a,b,c".split(","))  # split on commas -> ['a', 'b', 'c']
# OUTPUT:
# ['learn', 'python', 'today']
# ['a', 'b', 'c']


# ════════════════════════════════════════════════════════════════
# EXAMPLE 33 — Joining a list into text
# ════════════════════════════════════════════════════════════════
# WHAT   : .join() glues a list of strings into one string.
# SYNTAX : "separator".join(list_of_strings)
# PARAMS : the list to join (the separator is the string before .join).
# RETURNS: one combined string.
# WHY    : The opposite of split() — build text from pieces.
# WHEN   : Making CSV lines, sentences, paths.
# MISTAKE: All items must be strings (use str() on numbers first).

words = ["learn", "python", "today"]
print(" ".join(words))     # join with spaces -> learn python today
print("-".join(words))     # join with dashes -> learn-python-today
# OUTPUT:
# learn python today
# learn-python-today


# ════════════════════════════════════════════════════════════════
# EXAMPLE 34 — replace() : swap part of a string
# ════════════════════════════════════════════════════════════════
# WHAT   : .replace() returns a new string with text swapped.
# SYNTAX : text.replace(old, new)
# PARAMS : old -> text to find; new -> text to put instead.
# RETURNS: a NEW string (strings can't change in place).
# WHY    : To edit text.
# WHEN   : Fixing/cleaning strings.

text = "hello world"
print(text.replace("world", "there"))   # -> hello there
# OUTPUT: hello there


# ════════════════════════════════════════════════════════════════
# EXAMPLE 35 — find() : where is a substring?
# ════════════════════════════════════════════════════════════════
# WHAT   : .find() gives the position of text inside text.
# SYNTAX : text.find(substring)
# RETURNS: the position (or -1 if not found).
# WHY    : To locate something in a string.
# WHEN   : Searching text.

print("banana".find("n"))     # first "n" is at position 2 -> 2
print("banana".find("z"))     # not found -> -1
# OUTPUT:
# 2
# -1


# ════════════════════════════════════════════════════════════════
# EXAMPLE 36 — count() : how many times does it appear?
# ════════════════════════════════════════════════════════════════
# WHAT   : .count() counts occurrences.
# SYNTAX : text.count(substring)
# RETURNS: a whole number.
# WHY    : To measure repetition.
# WHEN   : Counting characters/words.

print("banana".count("a"))    # three "a"s -> 3
# OUTPUT: 3


# ════════════════════════════════════════════════════════════════
# EXAMPLE 37 — startswith() / endswith()
# ════════════════════════════════════════════════════════════════
# WHAT   : Check how a string begins or ends.
# SYNTAX : text.startswith(x)  /  text.endswith(x)
# RETURNS: True or False.
# WHY    : To classify text by prefix/suffix.
# WHEN   : Checking file types, URLs, etc.

print("report.pdf".endswith(".pdf"))     # -> True
print("https://x".startswith("https"))   # -> True
# OUTPUT:
# True
# True


# ════════════════════════════════════════════════════════════════
# EXAMPLE 38 — title() and capitalize()
# ════════════════════════════════════════════════════════════════
# WHAT   : Change the capitalisation of words.
# SYNTAX : text.title()  /  text.capitalize()
# RETURNS: a new string.
# WHY    : To format names/titles nicely.
# WHEN   : Display formatting.

print("hello world".title())        # each word capitalised -> Hello World
print("hello world".capitalize())   # only the first letter -> Hello world
# OUTPUT:
# Hello World
# Hello world


# ════════════════════════════════════════════════════════════════
# EXAMPLE 39 — min() and max() on a list
# ════════════════════════════════════════════════════════════════
# WHAT   : Find the smallest / largest value.
# SYNTAX : min(my_list)  /  max(my_list)
# RETURNS: the smallest / largest item.
# WHY    : To find extremes.
# WHEN   : Highest score, lowest price, etc.

scores = [50, 92, 73]
print(min(scores))   # -> 50
print(max(scores))   # -> 92
# OUTPUT:
# 50
# 92


# ════════════════════════════════════════════════════════════════
# EXAMPLE 40 — sum() on a list
# ════════════════════════════════════════════════════════════════
# WHAT   : Add up all numbers in a list.
# SYNTAX : sum(my_list)
# RETURNS: the total.
# WHY    : Totals and averages.
# WHEN   : Adding many numbers.

scores = [50, 92, 73]
total = sum(scores)              # 50 + 92 + 73
print(total)                     # -> 215
print(total / len(scores))       # average -> 71.66666...
# OUTPUT:
# 215
# 71.66666666666667


# ════════════════════════════════════════════════════════════════
# EXAMPLE 41 — sorted() with reverse
# ════════════════════════════════════════════════════════════════
# WHAT   : sorted() can order biggest-first.
# SYNTAX : sorted(my_list, reverse=True)
# PARAMS : reverse -> True for descending order.
# RETURNS: a new sorted list.
# WHY    : Ranking high-to-low.
# WHEN   : Leaderboards, top results.

print(sorted([3, 1, 2]))                  # ascending  -> [1, 2, 3]
print(sorted([3, 1, 2], reverse=True))    # descending -> [3, 2, 1]
# OUTPUT:
# [1, 2, 3]
# [3, 2, 1]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 42 — f-string alignment (padding to a width)
# ════════════════════════════════════════════════════════════════
# WHAT   : Pad a value to a fixed width for neat columns.
# SYNTAX : f"{value:>8}"  (right-align in width 8)  /  :<8 (left)  /  :^8 (center)
# WHY    : To line up output in columns.
# WHEN   : Tables, reports.

print(f"[{42:>8}]")    # right-aligned, width 8 -> [      42]
print(f"[{42:<8}]")    # left-aligned          -> [42      ]
print(f"[{42:^8}]")    # centered              -> [   42   ]
# OUTPUT:
# [      42]
# [42      ]
# [   42   ]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 43 — f-string thousands separator
# ════════════════════════════════════════════════════════════════
# WHAT   : Add commas to big numbers.
# SYNTAX : f"{number:,}"
# WHY    : Readability for large numbers.
# WHEN   : Money, counts, stats.

print(f"{1234567:,}")    # -> 1,234,567
# OUTPUT: 1,234,567


# ════════════════════════════════════════════════════════════════
# EXAMPLE 44 — Returning two values together (tuple + unpack)
# ════════════════════════════════════════════════════════════════
# WHAT   : Group related values in a tuple, then unpack them.
# WHY    : Keep things that belong together as one variable.
# WHEN   : Coordinates, dimensions, paired results.

size = (1920, 1080)    # a (width, height) pair
w, h = size            # unpack into two variables
print(w, h)            # -> 1920 1080
# OUTPUT: 1920 1080


# ════════════════════════════════════════════════════════════════
# EXAMPLE 45 — Nested list (a list inside a list)
# ════════════════════════════════════════════════════════════════
# WHAT   : Lists can contain other lists (like a grid/table).
# SYNTAX : grid[row][column]
# WHY    : To represent tables/matrices.
# WHEN   : Grids, rows of data.

grid = [[1, 2], [3, 4]]    # two rows
print(grid[0])             # first row -> [1, 2]
print(grid[1][0])          # row 1, column 0 -> 3
# OUTPUT:
# [1, 2]
# 3


# ════════════════════════════════════════════════════════════════
# EXAMPLE 46 — Nested dictionary (a dict inside a dict)
# ════════════════════════════════════════════════════════════════
# WHAT   : Dicts can contain other dicts (grouped records).
# SYNTAX : data["outer"]["inner"]
# WHY    : To represent structured, layered data.
# WHEN   : Config, JSON-like data.

data = {"user": {"name": "Sam", "age": 30}}
print(data["user"]["name"])   # dig into the inner dict -> Sam
# OUTPUT: Sam


# ════════════════════════════════════════════════════════════════
# EXAMPLE 47 — List of dictionaries (a very common shape)
# ════════════════════════════════════════════════════════════════
# WHAT   : A list where each item is a dict (like rows of records).
# SYNTAX : people[index]["key"]
# WHY    : The standard shape for lists of records.
# WHEN   : Lists of users, products, etc.

people = [{"name": "A"}, {"name": "B"}]
print(people[0]["name"])   # first record's name -> A
print(people[1]["name"])   # second record's name -> B
# OUTPUT:
# A
# B


# ════════════════════════════════════════════════════════════════
# EXAMPLE 48 — Boolean logic recap (and / or / not)
# ════════════════════════════════════════════════════════════════
# WHAT   : Combine True/False values.
# SYNTAX : a and b  |  a or b  |  not a
# WHY    : Check multiple conditions together.
# WHEN   : Decisions based on more than one thing.

age = 20
member = True
print(age >= 18 and member)   # both true -> True
print(age < 13 or member)     # at least one true -> True
print(not member)             # flip -> False
# OUTPUT:
# True
# True
# False


# ════════════════════════════════════════════════════════════════
# EXAMPLE 49 — Chained comparison (range check)
# ════════════════════════════════════════════════════════════════
# WHAT   : Check if a value is between two others, written naturally.
# SYNTAX : low < value < high
# RETURNS: True or False.
# WHY    : Reads like maths.
# WHEN   : Range checks.

n = 5
print(1 < n < 10)    # is n between 1 and 10? -> True
# OUTPUT: True


# ════════════════════════════════════════════════════════════════
# EXAMPLE 50 — Putting collections together (a small summary)
# ════════════════════════════════════════════════════════════════
# WHAT   : Combine list/dict/set tools into one useful result.
# WHY    : Real programs mix these constantly.
# WHEN   : Always.

person = {"name": "Lily", "city": "Rome"}
hobbies = ["reading", "cycling", "reading"]   # note the duplicate
unique_hobbies = set(hobbies)                 # drop the duplicate
print(f"{person['name']} from {person['city']} has {len(unique_hobbies)} unique hobbies")
# OUTPUT: Lily from Rome has 2 unique hobbies


print("\nLevel 2 complete! 50 intermediate concepts, every line explained.")
print("Next: variables_3_intermediate_plus.py")