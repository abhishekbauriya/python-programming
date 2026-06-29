"""
=====================================================================
 VARIABLES — LEVEL 3: INTERMEDIATE+  (fully explained, no functions)
=====================================================================
Deeper tools: string formatting, escape characters, compact ways to
build lists/dicts (comprehensions), clever unpacking, and number bases.

NEW IDEA: a "comprehension" is a one-line way to build a list/dict/set.
It contains the word 'for', but read it as "make X for each item".
You'll learn full loops later; for now just follow the pattern.

Labels: WHAT / SYNTAX / PARAMS / RETURNS / WHY / WHEN / MISTAKE
Run it:   python variables_3_intermediate_plus.py
=====================================================================
"""

print("LEVEL 3 — INTERMEDIATE+\n")


# ════════════════════════════════════════════════════════════════
# EXAMPLE 1 — str.format() : older way to insert values
# ════════════════════════════════════════════════════════════════
# WHAT   : .format() fills { } placeholders in a string with values.
# SYNTAX : "text {} text".format(value)
# PARAMS : the values that fill the { } slots, left to right.
# RETURNS: a new string.
# WHY    : You'll see it in older code; f-strings are usually nicer now.
# WHEN   : Reading old code, or when an f-string is awkward.

print("{} is {}".format("Anna", 28))   # { } slots filled in order
# OUTPUT: Anna is 28


# ════════════════════════════════════════════════════════════════
# EXAMPLE 2 — format() with positions
# ════════════════════════════════════════════════════════════════
# WHAT   : Number the { } slots to reuse/reorder values.
# SYNTAX : "{0} {1} {0}".format(a, b)
# WHY    : Reuse a value without repeating it.
# WHEN   : When the same value appears more than once.

print("{0}-{1}-{0}".format("a", "b"))   # 0=a, 1=b -> a-b-a
# OUTPUT: a-b-a


# ════════════════════════════════════════════════════════════════
# EXAMPLE 3 — f-strings can do math inside { }
# ════════════════════════════════════════════════════════════════
# WHAT   : You can put an expression (not just a variable) inside { }.
# SYNTAX : f"{expression}"
# WHY    : Compute and display in one step.
# WHEN   : Quick inline calculations in output.

print(f"{2 + 3}")          # the math runs -> 5
print(f"sum is {10 * 4}")  # -> sum is 40
# OUTPUT:
# 5
# sum is 40


# ════════════════════════════════════════════════════════════════
# EXAMPLE 4 — f-string !r (show the "developer" form)
# ════════════════════════════════════════════════════════════════
# WHAT   : !r shows a value the way repr() would (with quotes, escapes).
# SYNTAX : f"{value!r}"
# WHY    : Reveals hidden characters and shows quotes around text.
# WHEN   : Debugging — to SEE exactly what a value is.

city = "Paris"
print(f"{city!r}")    # shows the quotes -> 'Paris'
# OUTPUT: 'Paris'


# ════════════════════════════════════════════════════════════════
# EXAMPLE 5 — Multi-line strings (triple quotes)
# ════════════════════════════════════════════════════════════════
# WHAT   : Triple quotes let a string span several lines.
# SYNTAX : """line one
#          line two"""
# WHY    : For long text, messages, or blocks.
# WHEN   : Multi-line content.

poem = """roses are red
violets are blue"""
print(poem)
# OUTPUT:
# roses are red
# violets are blue


# ════════════════════════════════════════════════════════════════
# EXAMPLE 6 — Escape characters (\n and \t)
# ════════════════════════════════════════════════════════════════
# WHAT   : Special codes inside strings: \n = new line, \t = tab.
# SYNTAX : "a\nb"   "a\tb"
# WHY    : To add line breaks or tab spacing inside one string.
# WHEN   : Formatting output without multiple print() calls.

print("line1\nline2")   # \n starts a new line
print("col1\tcol2")     # \t inserts a tab gap
# OUTPUT:
# line1
# line2
# col1    col2


# ════════════════════════════════════════════════════════════════
# EXAMPLE 7 — Escaping a backslash (\\)
# ════════════════════════════════════════════════════════════════
# WHAT   : \\ prints a single backslash.
# SYNTAX : "C:\\path"
# WHY    : A single \ starts an escape code, so you double it for a real one.
# WHEN   : File paths, regex, etc.

print("C:\\Users\\me")   # each \\ is one backslash -> C:\Users\me
# OUTPUT: C:\Users\me


# ════════════════════════════════════════════════════════════════
# EXAMPLE 8 — Raw strings (r"...")
# ════════════════════════════════════════════════════════════════
# WHAT   : An r-string ignores escape codes (treats \ literally).
# SYNTAX : r"text\with\backslashes"
# WHY    : Avoid doubling every backslash.
# WHEN   : Windows paths, regular expressions.

print(r"C:\new\test")   # \n is NOT a new line here -> C:\new\test
# OUTPUT: C:\new\test


# ════════════════════════════════════════════════════════════════
# EXAMPLE 9 — zfill() : pad a number-string with zeros
# ════════════════════════════════════════════════════════════════
# WHAT   : .zfill() adds leading zeros to reach a width.
# SYNTAX : text.zfill(width)
# PARAMS : width -> total length you want.
# RETURNS: a new zero-padded string.
# WHY    : Fixed-width IDs, times, etc.
# WHEN   : "007", "0042", clock digits.

print("42".zfill(5))    # pad to 5 chars -> 00042
print("7".zfill(3))     # -> 007
# OUTPUT:
# 00042
# 007


# ════════════════════════════════════════════════════════════════
# EXAMPLE 10 — center / ljust / rjust
# ════════════════════════════════════════════════════════════════
# WHAT   : Align text within a given width, optionally with a fill char.
# SYNTAX : text.center(width, fill)  /  .ljust(...)  /  .rjust(...)
# RETURNS: a new padded string.
# WHY    : Neat columns and banners.
# WHEN   : Simple text layout.

print("hi".center(6, "-"))   # -> --hi--
print("hi".ljust(6, "."))    # -> hi....
print("hi".rjust(6, "."))    # -> ....hi
# OUTPUT:
# --hi--
# hi....
# ....hi


# ════════════════════════════════════════════════════════════════
# EXAMPLE 11 — LIST COMPREHENSION (build a list in one line)
# ════════════════════════════════════════════════════════════════
# WHAT   : A short way to build a list by transforming each item.
# SYNTAX : [expression for item in iterable]
# READ AS: "make <expression> for each <item> in <iterable>".
# RETURNS: a new list.
# WHY    : Cleaner/faster than building a list step by step.
# WHEN   : Transforming a sequence into a new list.

squares = [x * x for x in range(5)]   # x*x for x = 0,1,2,3,4
print(squares)                        # -> [0, 1, 4, 9, 16]
# OUTPUT: [0, 1, 4, 9, 16]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 12 — List comprehension with a filter (if)
# ════════════════════════════════════════════════════════════════
# WHAT   : Keep only items that pass a condition.
# SYNTAX : [item for item in iterable if condition]
# WHY    : Transform AND filter in one line.
# WHEN   : "Give me only the items where ...".

evens = [n for n in range(10) if n % 2 == 0]   # keep even numbers
print(evens)                                   # -> [0, 2, 4, 6, 8]
# OUTPUT: [0, 2, 4, 6, 8]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 13 — Comprehension over text
# ════════════════════════════════════════════════════════════════
# WHAT   : Loop a comprehension over the characters of a string.
# WHY    : Quick transformations of each character.
# WHEN   : Building lists from text.

caps = [c.upper() for c in "abc"]   # uppercase each character
print(caps)                         # -> ['A', 'B', 'C']
# OUTPUT: ['A', 'B', 'C']


# ════════════════════════════════════════════════════════════════
# EXAMPLE 14 — DICT COMPREHENSION
# ════════════════════════════════════════════════════════════════
# WHAT   : Build a dictionary in one line.
# SYNTAX : {key_expr: value_expr for item in iterable}
# RETURNS: a new dict.
# WHY    : Quickly create lookup tables.
# WHEN   : Mapping each item to a computed value.

squares_map = {n: n * n for n in range(4)}   # 0->0, 1->1, 2->4, 3->9
print(squares_map)                           # -> {0: 0, 1: 1, 2: 4, 3: 9}
# OUTPUT: {0: 0, 1: 1, 2: 4, 3: 9}


# ════════════════════════════════════════════════════════════════
# EXAMPLE 15 — SET COMPREHENSION
# ════════════════════════════════════════════════════════════════
# WHAT   : Build a set (unique results) in one line.
# SYNTAX : {expression for item in iterable}
# RETURNS: a new set.
# WHY    : Unique computed values.
# WHEN   : When you want uniqueness automatically.

lengths = {len(word) for word in ["a", "bb", "cc"]}   # lengths: 1,2,2 -> unique
print(lengths)                                        # -> {1, 2}
# OUTPUT: {1, 2}


# ════════════════════════════════════════════════════════════════
# EXAMPLE 16 — range() explained
# ════════════════════════════════════════════════════════════════
# WHAT   : range() produces a sequence of numbers (lazily).
# SYNTAX : range(stop)  /  range(start, stop)  /  range(start, stop, step)
# PARAMS : start (default 0), stop (NOT included), step (default 1).
# RETURNS: a range object (wrap in list() to see the numbers).
# WHY    : To generate number sequences.
# WHEN   : Counting, comprehensions, repeating things.

print(list(range(5)))         # 0..4        -> [0, 1, 2, 3, 4]
print(list(range(2, 6)))      # 2..5        -> [2, 3, 4, 5]
print(list(range(0, 10, 2)))  # 0..8 step 2 -> [0, 2, 4, 6, 8]
# OUTPUT:
# [0, 1, 2, 3, 4]
# [2, 3, 4, 5]
# [0, 2, 4, 6, 8]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 17 — enumerate() : pair items with their position
# ════════════════════════════════════════════════════════════════
# WHAT   : enumerate() gives (index, item) pairs.
# SYNTAX : enumerate(iterable, start=0)
# PARAMS : start -> the first index number (optional).
# RETURNS: pairs you can turn into a list to see.
# WHY    : To know WHERE each item is.
# WHEN   : Numbering items.

pairs = list(enumerate(["a", "b", "c"]))   # add positions
print(pairs)                               # -> [(0,'a'),(1,'b'),(2,'c')]
print(list(enumerate(["a", "b"], start=1)))  # start at 1 -> [(1,'a'),(2,'b')]
# OUTPUT:
# [(0, 'a'), (1, 'b'), (2, 'c')]
# [(1, 'a'), (2, 'b')]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 18 — zip() : pair up two lists
# ════════════════════════════════════════════════════════════════
# WHAT   : zip() matches items from lists by position.
# SYNTAX : zip(list_a, list_b)
# RETURNS: pairs (turn into a list to see them).
# WHY    : To combine related lists.
# WHEN   : Two lists that line up (names + scores, etc.).

names = ["x", "y"]
nums = [1, 2]
print(list(zip(names, nums)))   # -> [('x', 1), ('y', 2)]
# OUTPUT: [('x', 1), ('y', 2)]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 19 — Build a dict from two lists with zip()
# ════════════════════════════════════════════════════════════════
# WHAT   : zip() + dict() turns two lists into key->value pairs.
# SYNTAX : dict(zip(keys, values))
# RETURNS: a new dict.
# WHY    : Quick way to pair keys with values.
# WHEN   : You have separate key and value lists.

keys = ["a", "b"]
values = [10, 20]
print(dict(zip(keys, values)))   # -> {'a': 10, 'b': 20}
# OUTPUT: {'a': 10, 'b': 20}


# ════════════════════════════════════════════════════════════════
# EXAMPLE 20 — Extended unpacking with *
# ════════════════════════════════════════════════════════════════
# WHAT   : * captures "the rest" of a sequence into a list.
# SYNTAX : first, *rest = sequence
# WHY    : Split off the first (or last) item cleanly.
# WHEN   : Separating a head from a tail.

first, *rest = [1, 2, 3, 4]
print(first)   # -> 1
print(rest)    # -> [2, 3, 4]
# OUTPUT:
# 1
# [2, 3, 4]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 21 — Unpacking first, middle, last
# ════════════════════════════════════════════════════════════════
# WHAT   : * can sit in the middle to grab everything between ends.
# SYNTAX : a, *middle, b = sequence
# WHY    : Grab the ends and bundle the middle.
# WHEN   : First and last matter; middle is "the rest".

a, *middle, b = [1, 2, 3, 4, 5]
print(a, middle, b)   # -> 1 [2, 3, 4] 5
# OUTPUT: 1 [2, 3, 4] 5


# ════════════════════════════════════════════════════════════════
# EXAMPLE 22 — Nested unpacking
# ════════════════════════════════════════════════════════════════
# WHAT   : Unpack values that are themselves grouped.
# SYNTAX : (a, (b, c)) = (1, (2, 3))
# WHY    : Pull apart structured data in one step.
# WHEN   : Tuples inside tuples.

name, (width, height) = ("image", (1920, 1080))
print(name, width, height)   # -> image 1920 1080
# OUTPUT: image 1920 1080


# ════════════════════════════════════════════════════════════════
# EXAMPLE 23 — Merging dicts with {**a, **b}
# ════════════════════════════════════════════════════════════════
# WHAT   : Combine two dicts into a new one.
# SYNTAX : {**dict_a, **dict_b}
# RETURNS: a new merged dict (later keys win on clashes).
# WHY    : To layer defaults + overrides.
# WHEN   : Combining settings.

defaults = {"color": "black", "size": "M"}
chosen = {"color": "red"}
print({**defaults, **chosen})   # 'color' overridden -> {'color':'red','size':'M'}
# OUTPUT: {'color': 'red', 'size': 'M'}


# ════════════════════════════════════════════════════════════════
# EXAMPLE 24 — copy() a list (independent copy)
# ════════════════════════════════════════════════════════════════
# WHAT   : .copy() makes a separate list you can change safely.
# SYNTAX : new = old.copy()
# RETURNS: a new list with the same items.
# WHY    : Editing a copy must not affect the original.
# WHEN   : When you need to keep the original intact.
# MISTAKE: new = old does NOT copy (both names share one list!) — see Level 4.

original = [1, 2, 3]
clone = original.copy()
clone.append(99)
print(original)   # unchanged -> [1, 2, 3]
print(clone)      # changed   -> [1, 2, 3, 99]
# OUTPUT:
# [1, 2, 3]
# [1, 2, 3, 99]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 25 — Conditional expression (one-line choice)
# ════════════════════════════════════════════════════════════════
# WHAT   : Pick one of two values based on a condition, in one line.
# SYNTAX : value_if_true if condition else value_if_false
# RETURNS: one of the two values.
# WHY    : Short way to choose a value (a mini if/else for variables).
# WHEN   : Assigning a value that depends on a condition.

age = 20
status = "adult" if age >= 18 else "minor"   # condition picks the value
print(status)                                # -> adult
# OUTPUT: adult


# ════════════════════════════════════════════════════════════════
# EXAMPLE 26 — Walrus operator := (assign AND use at once)
# ════════════════════════════════════════════════════════════════
# WHAT   : := stores a value in a variable AND gives the value back,
#          all in the same spot.
# SYNTAX : (variable := expression)
# WHY    : Compute once, reuse immediately (avoids repeating work).
# WHEN   : Advanced; handy in comprehensions/conditions. Optional for beginners.

print((total := 3 + 4))   # stores 7 in 'total' AND prints it -> 7
print(total)              # 'total' now exists -> 7
# OUTPUT:
# 7
# 7


# ════════════════════════════════════════════════════════════════
# EXAMPLE 27 — Number formatting: percentage
# ════════════════════════════════════════════════════════════════
# WHAT   : Show a decimal as a percentage.
# SYNTAX : f"{value:.0%}"  (0 decimals)  /  :.1% (1 decimal)
# WHY    : 0.25 reads better as 25%.
# WHEN   : Displaying ratios/rates.

print(f"{0.25:.0%}")    # -> 25%
print(f"{0.1234:.1%}")  # -> 12.3%
# OUTPUT:
# 25%
# 12.3%


# ════════════════════════════════════════════════════════════════
# EXAMPLE 28 — Number bases inside an f-string
# ════════════════════════════════════════════════════════════════
# WHAT   : Show a number in binary (b), hex (x), or octal (o).
# SYNTAX : f"{number:b}"  /  :x  /  :o
# WHY    : Useful in low-level/computer contexts.
# WHEN   : Bit flags, colors, addresses.

print(f"{255:b}")   # binary -> 11111111
print(f"{255:x}")   # hex    -> ff
print(f"{8:o}")     # octal  -> 10
# OUTPUT:
# 11111111
# ff
# 10


# ════════════════════════════════════════════════════════════════
# EXAMPLE 29 — bin(), hex(), oct() functions
# ════════════════════════════════════════════════════════════════
# WHAT   : Convert a number to a based-string WITH a prefix.
# SYNTAX : bin(n) -> '0b...'  /  hex(n) -> '0x...'  /  oct(n) -> '0o...'
# RETURNS: a string with a prefix showing the base.
# WHY    : Quick base conversions.
# WHEN   : Same low-level contexts as above.

print(bin(5))     # -> 0b101
print(hex(255))   # -> 0xff
print(oct(8))     # -> 0o10
# OUTPUT:
# 0b101
# 0xff
# 0o10


# ════════════════════════════════════════════════════════════════
# EXAMPLE 30 — chr() and ord()
# ════════════════════════════════════════════════════════════════
# WHAT   : chr(number) -> character;  ord(character) -> number.
# SYNTAX : chr(65) / ord("A")
# RETURNS: a character / a number (a Unicode code point).
# WHY    : Convert between characters and their code numbers.
# WHEN   : Encoding, simple ciphers, char math.

print(chr(65))    # number 65 -> letter A
print(ord("A"))   # letter A  -> number 65
# OUTPUT:
# A
# 65


# ════════════════════════════════════════════════════════════════
# EXAMPLE 31 — round() to negative places
# ════════════════════════════════════════════════════════════════
# WHAT   : round() with a NEGATIVE number rounds to tens/hundreds.
# SYNTAX : round(number, -2)  -> nearest hundred
# WHY    : To round big numbers to a coarse level.
# WHEN   : Estimates, approximate totals.

print(round(1234, -2))   # nearest hundred -> 1200
print(round(1750, -3))   # nearest thousand -> 2000
# OUTPUT:
# 1200
# 2000


# ════════════════════════════════════════════════════════════════
# EXAMPLE 32 — divmod() : quotient AND remainder together
# ════════════════════════════════════════════════════════════════
# WHAT   : divmod(a, b) returns (a // b, a % b) as a pair.
# SYNTAX : divmod(a, b)
# RETURNS: a tuple (quotient, remainder).
# WHY    : Get both results in one call.
# WHEN   : Converting units (seconds -> minutes, etc.).

quotient, remainder = divmod(17, 5)   # 17 // 5 = 3, 17 % 5 = 2
print(quotient, remainder)            # -> 3 2
# OUTPUT: 3 2


# ════════════════════════════════════════════════════════════════
# EXAMPLE 33 — Truthiness (what counts as True/False)
# ════════════════════════════════════════════════════════════════
# WHAT   : Empty things are "falsy"; non-empty things are "truthy".
# RULE   : "", [], {}, set(), 0, 0.0, None are FALSE. Others are TRUE.
# WHY    : Lets you check "is this empty?" simply.
# WHEN   : Checking for empty values.

print(bool(""))      # empty text -> False
print(bool([]))      # empty list -> False
print(bool("x"))     # non-empty  -> True
print(bool([0]))     # a list with an item -> True (it's not empty!)
# OUTPUT:
# False
# False
# True
# True


# ════════════════════════════════════════════════════════════════
# EXAMPLE 34 — Checking for None with 'is'
# ════════════════════════════════════════════════════════════════
# WHAT   : Compare to None using 'is', not ==.
# SYNTAX : value is None
# WHY    : None is a single special object; 'is' is the correct, clear test.
# WHEN   : Checking "has this been set?".

value = None
print(value is None)       # -> True
value = "set"
print(value is None)       # -> False
# OUTPUT:
# True
# False


# ════════════════════════════════════════════════════════════════
# EXAMPLE 35 — Reading nested data
# ════════════════════════════════════════════════════════════════
# WHAT   : Reach into layered dicts/lists step by step.
# SYNTAX : data["a"]["b"]  or  data["a"][0]
# WHY    : Real data is often nested.
# WHEN   : Config, JSON-like structures.

config = {"db": {"host": "local", "port": 5432}}
print(config["db"]["host"])   # -> local
print(config["db"]["port"])   # -> 5432
# OUTPUT:
# local
# 5432


# ════════════════════════════════════════════════════════════════
# EXAMPLE 36 — A tuple as a dictionary key
# ════════════════════════════════════════════════════════════════
# WHAT   : Tuples (being unchangeable) can be dict keys; lists cannot.
# SYNTAX : my_dict[(x, y)] = value
# WHY    : To key data by a COMBINATION of values.
# WHEN   : Grids, coordinates, composite keys.

grid = {(0, 0): "start", (1, 1): "end"}
print(grid[(1, 1)])   # look up by the (1,1) key -> end
# OUTPUT: end


# ════════════════════════════════════════════════════════════════
# EXAMPLE 37 — frozenset (a set that cannot change)
# ════════════════════════════════════════════════════════════════
# WHAT   : Like a set, but fixed — so it CAN be a dict key or set member.
# SYNTAX : frozenset(iterable)
# RETURNS: a frozenset.
# WHY    : When you need an unchangeable, hashable set.
# WHEN   : Using a set of values as a key.

fs = frozenset([1, 2, 2, 3])   # duplicates removed, and now fixed
print(fs)                      # -> frozenset({1, 2, 3})
# OUTPUT: frozenset({1, 2, 3})


# ════════════════════════════════════════════════════════════════
# EXAMPLE 38 — Text <-> bytes (encode / decode)
# ════════════════════════════════════════════════════════════════
# WHAT   : Text is for humans; bytes are for files/networks.
# SYNTAX : text.encode("utf-8")  /  data.decode("utf-8")
# RETURNS: bytes / text.
# WHY    : Files and networks work in bytes.
# WHEN   : Saving/sending data (more in later chapters).

data = "hi".encode("utf-8")    # text -> bytes
print(data)                    # -> b'hi'
print(data.decode("utf-8"))    # bytes -> text -> hi
# OUTPUT:
# b'hi'
# hi


# ════════════════════════════════════════════════════════════════
# EXAMPLE 39 — Variable annotations (type hints)
# ════════════════════════════════════════════════════════════════
# WHAT   : A NOTE about the expected type. It does NOT enforce anything.
# SYNTAX : variable_name: type = value
# WHY    : Documents intent; tools/editors can warn you.
# WHEN   : Larger projects; optional for beginners.

quantity: int = 5          # ': int' is a hint saying "this should be an int"
name: str = "Sam"
print(quantity, name)      # the hints don't change the values
# OUTPUT: 5 Sam


# ════════════════════════════════════════════════════════════════
# EXAMPLE 40 — Build text by joining a comprehension
# ════════════════════════════════════════════════════════════════
# WHAT   : Turn numbers into a joined string in one line.
# SYNTAX : "sep".join(str(x) for x in iterable)
# WHY    : Make CSV-like text from numbers.
# WHEN   : Producing output lines.
# MISTAKE: join needs strings, so str() converts each number first.

csv_line = ",".join(str(n) for n in [1, 2, 3])
print(csv_line)   # -> 1,2,3
# OUTPUT: 1,2,3


# ════════════════════════════════════════════════════════════════
# EXAMPLE 41 — sum() over a comprehension (no temporary list)
# ════════════════════════════════════════════════════════════════
# WHAT   : Add up computed values directly.
# SYNTAX : sum(expression for item in iterable)
# WHY    : Efficient — no list is built first.
# WHEN   : Totals from a transformation.

print(sum(n for n in range(1, 6)))      # 1+2+3+4+5 -> 15
print(sum(n * n for n in range(1, 4)))  # 1+4+9     -> 14
# OUTPUT:
# 15
# 14


# ════════════════════════════════════════════════════════════════
# EXAMPLE 42 — Count items that match a rule
# ════════════════════════════════════════════════════════════════
# WHAT   : Use a comprehension + len() to count matches.
# SYNTAX : len([item for item in iterable if condition])
# WHY    : Quick "how many satisfy X?" answer.
# WHEN   : Counting filtered items.

data = [4, 7, 2, 9, 5]
big = len([n for n in data if n > 4])   # count numbers greater than 4
print(big)                              # 7, 9, 5 -> 3
# OUTPUT: 3


# ════════════════════════════════════════════════════════════════
# EXAMPLE 43 — Reverse a list/string with slicing [::-1]
# ════════════════════════════════════════════════════════════════
# WHAT   : A slice with step -1 returns a reversed copy.
# SYNTAX : sequence[::-1]
# RETURNS: a new reversed list/string.
# WHY    : Quick reversal without changing the original.
# WHEN   : Reversing data or text.

print([1, 2, 3][::-1])   # -> [3, 2, 1]
print("hello"[::-1])     # -> olleh
# OUTPUT:
# [3, 2, 1]
# olleh


# ════════════════════════════════════════════════════════════════
# EXAMPLE 44 — Swapping several variables at once
# ════════════════════════════════════════════════════════════════
# WHAT   : Reassign multiple variables in one line.
# SYNTAX : a, b, c = c, a, b
# WHY    : Rotate/rearrange values cleanly.
# WHEN   : Reordering data.

a, b, c = 1, 2, 3
a, b, c = c, a, b      # rotate the values
print(a, b, c)         # -> 3 1 2
# OUTPUT: 3 1 2


# ════════════════════════════════════════════════════════════════
# EXAMPLE 45 — sorted() ignoring case (key=str.lower)
# ════════════════════════════════════════════════════════════════
# WHAT   : Sort by a RULE. Here: compare lowercased text.
# SYNTAX : sorted(my_list, key=str.lower)
# PARAMS : key -> a rule that maps each item to what to compare by.
# WHY    : Default sort puts 'A' before 'a'; this ignores case.
# WHEN   : Alphabetical sorting that's case-insensitive.

words = ["banana", "Apple", "cherry"]
print(sorted(words))               # default: capitals first -> ['Apple','banana','cherry']
print(sorted(words, key=str.lower))# case-insensitive       -> ['Apple','banana','cherry']
# OUTPUT:
# ['Apple', 'banana', 'cherry']
# ['Apple', 'banana', 'cherry']


# ════════════════════════════════════════════════════════════════
# EXAMPLE 46 — Combine collections cleanly
# ════════════════════════════════════════════════════════════════
# WHAT   : Use several tools together in one expression.
# WHY    : This is everyday Python.
# WHEN   : Building summaries.

nums = [5, 3, 8, 1]
print(f"min={min(nums)} max={max(nums)} sorted={sorted(nums)}")
# OUTPUT: min=1 max=8 sorted=[1, 3, 5, 8]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 47 — Dict comprehension with a condition
# ════════════════════════════════════════════════════════════════
# WHAT   : Build a dict but only for items that pass a test.
# SYNTAX : {k: v for item in iterable if condition}
# WHY    : Create a filtered lookup table.
# WHEN   : Selecting a subset by rule.

even_squares = {n: n * n for n in range(6) if n % 2 == 0}
print(even_squares)   # only even keys -> {0: 0, 2: 4, 4: 16}
# OUTPUT: {0: 0, 2: 4, 4: 16}


# ════════════════════════════════════════════════════════════════
# EXAMPLE 48 — Nested comprehension (flatten a grid)
# ════════════════════════════════════════════════════════════════
# WHAT   : A comprehension with two 'for' parts flattens nested data.
# SYNTAX : [value for row in grid for value in row]
# READ AS: "for each row, for each value in that row".
# WHY    : Turn a list-of-lists into one flat list.
# WHEN   : Flattening grids/tables.

grid = [[1, 2], [3, 4]]
flat = [value for row in grid for value in row]
print(flat)   # -> [1, 2, 3, 4]
# OUTPUT: [1, 2, 3, 4]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 49 — Self-documenting f-string {x=}
# ════════════════════════════════════════════════════════════════
# WHAT   : f"{name=}" prints both the NAME and the VALUE.
# SYNTAX : f"{variable=}"
# WHY    : Super handy for quick debugging.
# WHEN   : Checking a variable's value while developing.

ratio = 0.75
count = 42
print(f"{ratio=}")   # -> ratio=0.75
print(f"{count=}")   # -> count=42
# OUTPUT:
# ratio=0.75
# count=42


# ════════════════════════════════════════════════════════════════
# EXAMPLE 50 — Put it together (a small report)
# ════════════════════════════════════════════════════════════════
# WHAT   : Combine comprehension, sum, and an f-string.
# WHY    : Shows the intermediate+ tools working as a team.
# WHEN   : Producing a calculated summary.

prices = [10, 25, 15, 30]
total = sum(prices)                                  # 80
expensive = [p for p in prices if p >= 20]           # [25, 30]
print(f"total={total}, expensive items={expensive}, count={len(expensive)}")
# OUTPUT: total=80, expensive items=[25, 30], count=2


print("\nLevel 3 complete! 50 intermediate+ concepts, every line explained.")
print("Next: variables_4_advanced.py")