"""
=====================================================================
 VARIABLES — LEVEL 4: ADVANCED  (fully explained, no functions)
=====================================================================
The deeper truth: a variable is a NAME that POINTS TO an object stored
in memory. This level explains identity, copying, mutability traps,
and special number/typing tools. Read slowly — these "gotchas" trip up
even experienced programmers.

Labels: WHAT / SYNTAX / PARAMS / RETURNS / WHY / WHEN / MISTAKE
Run it:   python variables_4_advanced.py
=====================================================================
"""
import copy                       # gives us copy.deepcopy (Example 7)
from decimal import Decimal       # exact decimal numbers (Example 29)
from fractions import Fraction    # exact fractions (Example 30)
from typing import Final          # a "constant" type hint (Example 40)

print("LEVEL 4 — ADVANCED\n")


# ════════════════════════════════════════════════════════════════
# EXAMPLE 1 — A variable is a NAME pointing to an object
# ════════════════════════════════════════════════════════════════
# WHAT   : The value lives in memory; the variable is just a label for it.
# WHY    : This mental model explains every "gotcha" in this file.
# WHEN   : Keep it in mind whenever two names might share one object.

x = [1, 2]         # the LIST lives in memory; 'x' is a label pointing to it
print(x)           # -> [1, 2]
# OUTPUT: [1, 2]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 2 — id() : the object's unique identity number
# ════════════════════════════════════════════════════════════════
# WHAT   : id() returns a unique number identifying an object while the
#          program runs (think of it as the object's "address").
# SYNTAX : id(value)
# RETURNS: an integer (the exact number varies each run — don't rely on it).
# WHY    : To check whether two names point to the SAME object.
# WHEN   : Debugging sharing/aliasing issues.

a = [1, 2]
print(type(id(a)).__name__)   # id() gives an int -> int
# OUTPUT: int


# ════════════════════════════════════════════════════════════════
# EXAMPLE 3 — 'is' (same object) vs '==' (same value)
# ════════════════════════════════════════════════════════════════
# WHAT   : '==' compares VALUES; 'is' compares IDENTITY (same object).
# SYNTAX : a == b   /   a is b
# RETURNS: True or False.
# WHY    : Two different objects can hold equal values.
# WHEN   : Use == for values; use 'is' only for None (and identity checks).

a = [1, 2]
b = [1, 2]                 # a SEPARATE list with equal contents
print(a == b)              # equal values?  -> True
print(a is b)              # same object?   -> False
# OUTPUT:
# True
# False


# ════════════════════════════════════════════════════════════════
# EXAMPLE 4 — Assignment does NOT copy (aliasing)
# ════════════════════════════════════════════════════════════════
# WHAT   : 'y = x' makes y point to the SAME object as x (no copy!).
# WHY    : This surprises beginners and causes "spooky" bugs.
# WHEN   : Any time you assign a list/dict/set to another name.
# MISTAKE: Thinking 'y = x' copies the data. It does not.

x = [1, 2, 3]
y = x                      # y is just another label for the SAME list
print(x is y)              # same object -> True
# OUTPUT: True


# ════════════════════════════════════════════════════════════════
# EXAMPLE 5 — Proof of aliasing (change one, both change)
# ════════════════════════════════════════════════════════════════
# WHAT   : Because x and y share one list, editing via y shows in x.
# WHY    : Demonstrates the consequence of Example 4.
# WHEN   : Watch for this when passing lists around.

x = [1, 2, 3]
y = x
y.append(4)                # we change it through 'y'
print(x)                   # but 'x' shows the change too -> [1, 2, 3, 4]
# OUTPUT: [1, 2, 3, 4]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 6 — .copy() makes an INDEPENDENT copy
# ════════════════════════════════════════════════════════════════
# WHAT   : .copy() creates a separate list you can change safely.
# SYNTAX : new = old.copy()
# WHY    : To avoid the aliasing trap when you need a real copy.
# WHEN   : When edits to the copy must not affect the original.

original = [1, 2, 3]
clone = original.copy()    # a brand-new, separate list
clone.append(99)
print(original)            # unchanged -> [1, 2, 3]
print(clone)               # changed   -> [1, 2, 3, 99]
# OUTPUT:
# [1, 2, 3]
# [1, 2, 3, 99]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 7 — SHALLOW copy trap (inner lists are still shared)
# ════════════════════════════════════════════════════════════════
# WHAT   : .copy() copies the OUTER list, but inner lists are still shared.
# WHY    : The classic deep-vs-shallow surprise.
# WHEN   : Copying lists that contain other lists/dicts.
# FIX    : Use copy.deepcopy (next example).

nested = [[1, 2], [3, 4]]
shallow = nested.copy()    # outer list copied; inner lists are SHARED
shallow[0].append(99)      # change an inner list
print(nested)              # the original's inner list changed too! -> [[1, 2, 99], [3, 4]]
# OUTPUT: [[1, 2, 99], [3, 4]]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 8 — copy.deepcopy() copies everything
# ════════════════════════════════════════════════════════════════
# WHAT   : deepcopy() copies the outer AND all inner objects.
# SYNTAX : copy.deepcopy(value)
# RETURNS: a fully independent copy.
# WHY    : To safely copy nested data.
# WHEN   : Copying lists-of-lists, dicts-of-dicts, etc.

nested = [[1, 2], [3, 4]]
deep = copy.deepcopy(nested)   # everything copied, nothing shared
deep[0].append(99)
print(nested)                  # untouched -> [[1, 2], [3, 4]]
print(deep)                    # changed   -> [[1, 2, 99], [3, 4]]
# OUTPUT:
# [[1, 2], [3, 4]]
# [[1, 2, 99], [3, 4]]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 9 — Small integers are cached
# ════════════════════════════════════════════════════════════════
# WHAT   : Python reuses one object for small integers, so equal small
#          ints share identity.
# WHY    : An implementation detail — interesting, not something to rely on.
# WHEN   : Just so 'is' results on numbers don't confuse you.

m = 5
n = 5
print(m is n)        # same cached object -> True (CPython detail)
# OUTPUT: True


# ════════════════════════════════════════════════════════════════
# EXAMPLE 10 — None is a single shared object
# ════════════════════════════════════════════════════════════════
# WHAT   : There is only ONE None in all of Python.
# SYNTAX : value is None
# WHY    : That's why we always test None with 'is', never ==.
# WHEN   : Checking "is this unset?".

v = None
print(v is None)     # -> True
# OUTPUT: True


# ════════════════════════════════════════════════════════════════
# EXAMPLE 11 — bool is a kind of int (True == 1, False == 0)
# ════════════════════════════════════════════════════════════════
# WHAT   : Booleans ARE integers under the hood.
# WHY    : So True + True == 2; sometimes handy for counting.
# WHEN   : Good to know so it never confuses you.

print(True == 1)     # -> True
print(True + True)   # 1 + 1 -> 2
# OUTPUT:
# True
# 2


# ════════════════════════════════════════════════════════════════
# EXAMPLE 12 — isinstance(True, int) is True
# ════════════════════════════════════════════════════════════════
# WHAT   : Because bool is a subtype of int, this is True.
# SYNTAX : isinstance(value, type)
# RETURNS: True/False.
# WHY    : A subtle point when type-checking.
# WHEN   : Be careful if you must separate bool from int.

print(isinstance(True, int))     # -> True
print(isinstance(True, bool))    # -> True (it's specifically a bool)
# OUTPUT:
# True
# True


# ════════════════════════════════════════════════════════════════
# EXAMPLE 13 — Immutable values: changing makes a NEW object
# ════════════════════════════════════════════════════════════════
# WHAT   : Numbers/strings/tuples can't change; "changing" makes a new one.
# WHY    : The variable just points to a new object; the old is untouched.
# WHEN   : Understanding why numbers/strings are "safe" to share.

num = 1000
id_before = id(num)
num = num + 1            # this creates a NEW integer object
print(id(num) == id_before)   # different object now -> False
# OUTPUT: False


# ════════════════════════════════════════════════════════════════
# EXAMPLE 14 — Strings are immutable
# ════════════════════════════════════════════════════════════════
# WHAT   : You cannot change one character of a string in place.
# WHY    : Strings are immutable; you build a NEW string instead.
# WHEN   : Editing text.
# MISTAKE: text[0] = "b" causes a TypeError.

text = "cat"
# text[0] = "b"        # would ERROR -> kept as a comment
new_text = "b" + text[1:]   # build a new string: "b" + "at"
print(new_text)             # -> bat
# OUTPUT: bat


# ════════════════════════════════════════════════════════════════
# EXAMPLE 15 — A tuple is fixed, but a list INSIDE it can change
# ════════════════════════════════════════════════════════════════
# WHAT   : You can't replace the tuple's items, but a mutable item
#          (like a list) inside it can still be changed.
# WHY    : Immutability is about the tuple's own slots, not what they point to.
# WHEN   : Subtle — good to be aware of.

combo = (1, [2, 3])     # a tuple holding a number and a LIST
combo[1].append(4)      # we change the inner list (allowed)
print(combo)            # -> (1, [2, 3, 4])
# OUTPUT: (1, [2, 3, 4])


# ════════════════════════════════════════════════════════════════
# EXAMPLE 16 — List-multiply trap ([[0]*3]*3 shares rows)
# ════════════════════════════════════════════════════════════════
# WHAT   : Multiplying a list of lists repeats the SAME inner list.
# WHY    : All "rows" are the one object, so changing one changes all.
# WHEN   : Avoid this when building grids.
# FIX    : Use a comprehension (next example).

rows = [[0] * 3] * 3    # three references to ONE inner list
rows[0][0] = 1          # change "one" row...
print(rows)             # ...and ALL rows change -> [[1,0,0],[1,0,0],[1,0,0]]
# OUTPUT: [[1, 0, 0], [1, 0, 0], [1, 0, 0]]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 17 — The fix: a comprehension makes separate rows
# ════════════════════════════════════════════════════════════════
# WHAT   : A comprehension builds a NEW inner list each time.
# SYNTAX : [[0] * 3 for _ in range(3)]   ('_' = a value we ignore)
# WHY    : Each row is independent now.
# WHEN   : Always build grids this way.

good = [[0] * 3 for _ in range(3)]   # 3 separate inner lists
good[0][0] = 1                       # change only the first row
print(good)                          # -> [[1,0,0],[0,0,0],[0,0,0]]
# OUTPUT: [[1, 0, 0], [0, 0, 0], [0, 0, 0]]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 18 — += on a list changes it IN PLACE (same object)
# ════════════════════════════════════════════════════════════════
# WHAT   : For lists, += adds items to the existing list (same id).
# WHY    : It mutates rather than creating a new list.
# WHEN   : Know this when a list is shared by two names.

lst = [1, 2]
before = id(lst)
lst += [3]                       # mutates the SAME list
print(id(lst) == before)         # same object -> True
print(lst)                       # -> [1, 2, 3]
# OUTPUT:
# True
# [1, 2, 3]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 19 — list = list + [..] makes a NEW object
# ════════════════════════════════════════════════════════════════
# WHAT   : Using + and = creates a brand-new list (different id).
# WHY    : Contrast with += (Example 18).
# WHEN   : When you specifically want a fresh list.

lst = [1, 2]
before = id(lst)
lst = lst + [3]                  # builds a NEW list, rebinds 'lst'
print(id(lst) == before)         # different object -> False
# OUTPUT: False


# ════════════════════════════════════════════════════════════════
# EXAMPLE 20 — Chained assignment shares a mutable object
# ════════════════════════════════════════════════════════════════
# WHAT   : 'p = q = []' makes BOTH names point to the SAME new list.
# WHY    : Combines aliasing (Ex 4) with chained assignment.
# WHEN   : Be careful initialising several lists at once.
# MISTAKE: People expect two separate lists; they get one shared list.

p = q = []        # ONE list, two labels
p.append(1)       # change via 'p'
print(q)          # 'q' sees it too -> [1]
# OUTPUT: [1]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 21 — Star-unpack the "rest"
# ════════════════════════════════════════════════════════════════
# WHAT   : * collects leftover items into a list.
# SYNTAX : head, *tail = sequence
# WHY    : Split a head from the rest cleanly.
# WHEN   : Processing "first item + remaining".

head, *tail = [10, 20, 30, 40]
print(head)   # -> 10
print(tail)   # -> [20, 30, 40]
# OUTPUT:
# 10
# [20, 30, 40]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 22 — Star in the middle
# ════════════════════════════════════════════════════════════════
# WHAT   : * can capture the middle while you name the ends.
# SYNTAX : first, *middle, last = sequence
# WHY    : Grab both ends, bundle the middle.
# WHEN   : First/last matter; middle is "everything else".

start, *mid, end = "abcdef"
print(start, end)   # -> a f
print(mid)          # -> ['b', 'c', 'd', 'e']
# OUTPUT:
# a f
# ['b', 'c', 'd', 'e']


# ════════════════════════════════════════════════════════════════
# EXAMPLE 23 — Star-unpack INTO a function call: print(*list)
# ════════════════════════════════════════════════════════════════
# WHAT   : * spreads a list's items as separate arguments.
# SYNTAX : print(*my_list)
# WHY    : Pass each item individually instead of the whole list.
# WHEN   : Printing items spaced out, passing args.

items = [1, 2, 3]
print(items)     # the list itself -> [1, 2, 3]
print(*items)    # spread into separate args -> 1 2 3
# OUTPUT:
# [1, 2, 3]
# 1 2 3


# ════════════════════════════════════════════════════════════════
# EXAMPLE 24 — Double-star ** unpacks a dict into format()
# ════════════════════════════════════════════════════════════════
# WHAT   : ** spreads a dict as named values.
# SYNTAX : "{key}".format(**my_dict)
# WHY    : Fill named placeholders straight from a dict.
# WHEN   : Templating from a dict of values.

values = {"a": 1, "b": 2}
print("{a}+{b}".format(**values))   # -> 1+2
# OUTPUT: 1+2


# ════════════════════════════════════════════════════════════════
# EXAMPLE 25 — Dict comprehension with a condition
# ════════════════════════════════════════════════════════════════
# WHAT   : Build a dict only for items that pass a test.
# SYNTAX : {k: v for item in iterable if condition}
# WHY    : Create a filtered lookup table in one line.
# WHEN   : Selecting a subset.

even_squares = {n: n * n for n in range(6) if n % 2 == 0}
print(even_squares)   # -> {0: 0, 2: 4, 4: 16}
# OUTPUT: {0: 0, 2: 4, 4: 16}


# ════════════════════════════════════════════════════════════════
# EXAMPLE 26 — Nested comprehension (flatten a grid)
# ════════════════════════════════════════════════════════════════
# WHAT   : Two 'for' parts flatten a list-of-lists into one list.
# SYNTAX : [value for row in grid for value in row]
# READ AS: "for each row, for each value in that row, take value".
# WHY    : Common way to flatten nested data.
# WHEN   : Turning a 2D structure into 1D.

grid = [[1, 2], [3, 4]]
flat = [value for row in grid for value in row]
print(flat)   # -> [1, 2, 3, 4]
# OUTPUT: [1, 2, 3, 4]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 27 — Walrus := inside a comprehension
# ════════════════════════════════════════════════════════════════
# WHAT   : Compute a value once, store it, and reuse it in the same line.
# SYNTAX : [stored for item in iterable if (stored := expr) > x]
# WHY    : Avoids computing the same thing twice.
# WHEN   : Advanced; optional. Shown so you recognise it.

data = [1, 2, 3, 4]
result = [y for n in data if (y := n * n) > 4]   # y = n*n, keep if y > 4
print(result)                                    # squares > 4 -> [9, 16]
# OUTPUT: [9, 16]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 28 — Self-documenting f-string {x=}
# ════════════════════════════════════════════════════════════════
# WHAT   : f"{name=}" prints both the variable name and its value.
# SYNTAX : f"{variable=}"
# WHY    : Fast debugging — see name and value at once.
# WHEN   : While developing/checking values.

ratio = 0.75
print(f"{ratio=}")   # -> ratio=0.75
# OUTPUT: ratio=0.75


# ════════════════════════════════════════════════════════════════
# EXAMPLE 29 — Decimal : exact decimal numbers (great for money)
# ════════════════════════════════════════════════════════════════
# WHAT   : float maths can be slightly wrong (0.1 + 0.2 != 0.3 exactly).
#          Decimal is exact.
# SYNTAX : Decimal("0.1")   (pass numbers as TEXT for exactness)
# RETURNS: a Decimal value.
# WHY    : Money must be exact to the cent.
# WHEN   : Currency, billing, finance.

print(0.1 + 0.2)                          # float -> 0.30000000000000004 (not exact!)
print(Decimal("0.1") + Decimal("0.2"))    # Decimal -> 0.3 (exact)
# OUTPUT:
# 0.30000000000000004
# 0.3


# ════════════════════════════════════════════════════════════════
# EXAMPLE 30 — Fraction : exact fractions
# ════════════════════════════════════════════════════════════════
# WHAT   : Fraction keeps exact fractions (no decimal error).
# SYNTAX : Fraction(numerator, denominator)
# RETURNS: a Fraction, automatically simplified.
# WHY    : Exact ratio maths.
# WHEN   : When you need precise fractions.

print(Fraction(1, 3) + Fraction(1, 6))    # 1/3 + 1/6 -> 1/2 (simplified)
# OUTPUT: 1/2


# ════════════════════════════════════════════════════════════════
# EXAMPLE 31 — complex numbers
# ════════════════════════════════════════════════════════════════
# WHAT   : A complex number has a real and an imaginary (j) part.
# SYNTAX : complex(real, imag)   or   3 + 4j
# WHY    : Used in advanced math/engineering (rare in everyday code).
# WHEN   : Signal processing, geometry. abs() gives its magnitude.

c = complex(3, 4)        # 3 + 4j
print(abs(c))            # magnitude (like a distance) -> 5.0
# OUTPUT: 5.0


# ════════════════════════════════════════════════════════════════
# EXAMPLE 32 — hash() : a fingerprint for immutable values
# ════════════════════════════════════════════════════════════════
# WHAT   : hash() turns a value into a number used by sets/dicts.
# SYNTAX : hash(value)   (value must be immutable: number, str, tuple)
# RETURNS: an integer fingerprint; equal values share the same hash.
# WHY    : It's how dicts/sets find things fast.
# WHEN   : Understanding why keys must be immutable.
# MISTAKE: hash([1,2]) errors — lists are mutable, so they're unhashable.

print(hash((1, 2)) == hash((1, 2)))   # equal tuples -> same hash -> True
# OUTPUT: True


# ════════════════════════════════════════════════════════════════
# EXAMPLE 33 — frozenset as a dictionary key
# ════════════════════════════════════════════════════════════════
# WHAT   : A frozenset is immutable, so it can be a dict key.
# SYNTAX : my_dict[frozenset({...})] = value
# WHY    : To key data by a SET of values.
# WHEN   : Grouping by a set (e.g. a set of permissions -> a role name).

roles = {frozenset({"read", "write"}): "editor"}
print(roles[frozenset({"read", "write"})])   # -> editor
# OUTPUT: editor


# ════════════════════════════════════════════════════════════════
# EXAMPLE 34 — Symmetric difference ^ on sets
# ════════════════════════════════════════════════════════════════
# WHAT   : ^ keeps items in exactly ONE of the two sets (not both).
# SYNTAX : set_a ^ set_b
# RETURNS: a new set.
# WHY    : "What's different between these two groups?".
# WHEN   : Comparing two sets.

print({1, 2, 3} ^ {2, 3, 4})   # 1 only in first, 4 only in second -> {1, 4}
# OUTPUT: {1, 4}


# ════════════════════════════════════════════════════════════════
# EXAMPLE 35 — Merge dicts with the | operator (Python 3.9+)
# ════════════════════════════════════════════════════════════════
# WHAT   : | combines two dicts into a new one (right side wins).
# SYNTAX : dict_a | dict_b
# RETURNS: a new merged dict.
# WHY    : Cleaner than {**a, **b} on modern Python.
# WHEN   : Combining settings/dicts.

print({"a": 1} | {"b": 2})           # -> {'a': 1, 'b': 2}
print({"a": 1} | {"a": 9, "b": 2})   # right side wins -> {'a': 9, 'b': 2}
# OUTPUT:
# {'a': 1, 'b': 2}
# {'a': 9, 'b': 2}


# ════════════════════════════════════════════════════════════════
# EXAMPLE 36 — Unpack a tuple returned by divmod()
# ════════════════════════════════════════════════════════════════
# WHAT   : Functions can return a tuple; unpack it into variables.
# SYNTAX : a, b = divmod(x, y)
# WHY    : Read both results clearly.
# WHEN   : Any function that returns a pair.

quotient, remainder = divmod(17, 5)
print(quotient, remainder)   # -> 3 2
# OUTPUT: 3 2


# ════════════════════════════════════════════════════════════════
# EXAMPLE 37 — enumerate() with a custom start
# ════════════════════════════════════════════════════════════════
# WHAT   : enumerate() can begin numbering at any value.
# SYNTAX : enumerate(iterable, start=1)
# WHY    : Human-friendly numbering (1, 2, 3 instead of 0, 1, 2).
# WHEN   : Numbered lists for people.

print(list(enumerate(["a", "b"], start=1)))   # -> [(1, 'a'), (2, 'b')]
# OUTPUT: [(1, 'a'), (2, 'b')]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 38 — zip(strict=True) catches length mismatches
# ════════════════════════════════════════════════════════════════
# WHAT   : With strict=True, zip errors if the lists differ in length.
# SYNTAX : zip(a, b, strict=True)
# WHY    : Silent truncation hides bugs; strict makes them loud.
# WHEN   : When the lists SHOULD be the same length.

print(list(zip([1, 2], [3, 4], strict=True)))   # equal lengths -> [(1, 3), (2, 4)]
# OUTPUT: [(1, 3), (2, 4)]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 39 — Type hint with a generic type
# ════════════════════════════════════════════════════════════════
# WHAT   : Annotate that a variable should be a list of ints.
# SYNTAX : name: list[int] = [...]
# WHY    : Documents intent; editors/tools can check it. It does NOT enforce.
# WHEN   : Larger projects; optional for beginners.

prices: list[int] = [10, 20, 30]   # the hint says "a list of ints"
print(prices)                      # the hint doesn't change the value
# OUTPUT: [10, 20, 30]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 40 — A constant marked with typing.Final
# ════════════════════════════════════════════════════════════════
# WHAT   : Final is a hint meaning "don't reassign this".
# SYNTAX : NAME: Final = value
# WHY    : Stronger signal than ALL_CAPS; tools can warn on reassignment.
# WHEN   : Real constants in bigger projects.

MAX_USERS: Final = 100   # a hint: treat as a constant
print(MAX_USERS)         # -> 100
# OUTPUT: 100


# ════════════════════════════════════════════════════════════════
# EXAMPLE 41 — Scope (concept): module-level variables are "global"
# ════════════════════════════════════════════════════════════════
# WHAT   : Variables made at the top level of a file are "global" — usable
#          anywhere in the file. A separate "local" scope exists only
#          INSIDE functions (which you'll learn next chapter).
# WHY    : Scope decides WHERE a variable can be seen/used.
# WHEN   : You'll work with local vs global once you learn functions.

GLOBAL_GREETING = "hello"   # a global (module-level) variable
print(GLOBAL_GREETING)      # usable here and anywhere else in this file
# OUTPUT: hello


# ════════════════════════════════════════════════════════════════
# EXAMPLE 42 — A string is iterable -> list of characters
# ════════════════════════════════════════════════════════════════
# WHAT   : You can loop over a string's characters; list() collects them.
# SYNTAX : list(text)
# RETURNS: a list of single-character strings.
# WHY    : To work with characters individually.
# WHEN   : Processing text char by char.

print(list("abc"))   # -> ['a', 'b', 'c']
# OUTPUT: ['a', 'b', 'c']


# ════════════════════════════════════════════════════════════════
# EXAMPLE 43 — Build a word from numbers with chr() + join
# ════════════════════════════════════════════════════════════════
# WHAT   : Turn character codes into letters and join them.
# SYNTAX : "".join(chr(code) for code in codes)
# WHY    : Combines chr(), a comprehension, and join().
# WHEN   : Encoding/decoding, building strings from data.

word = "".join(chr(code) for code in [72, 73])   # 72->H, 73->I
print(word)                                       # -> HI
# OUTPUT: HI


# ════════════════════════════════════════════════════════════════
# EXAMPLE 44 — Navigating nested data (list -> dict -> list)
# ════════════════════════════════════════════════════════════════
# WHAT   : Reach a deep value by chaining [ ] step by step.
# SYNTAX : data[index]["key"][index]
# WHY    : Real-world data is layered.
# WHEN   : Reading JSON-like structures.

records = [{"tags": ["x", "y"]}, {"tags": ["z"]}]
print(records[0]["tags"][1])   # record 0 -> tags -> position 1 -> y
# OUTPUT: y


# ════════════════════════════════════════════════════════════════
# EXAMPLE 45 — Nested conditional expression (one-line A/B/C)
# ════════════════════════════════════════════════════════════════
# WHAT   : Chain conditional expressions for several choices.
# SYNTAX : x if c1 else y if c2 else z
# WHY    : A compact "if/elif/else" for picking a value.
# WHEN   : Mapping a number to a category.

grade = 85
letter = "A" if grade >= 90 else "B" if grade >= 80 else "C"
print(letter)   # 85 -> "B"
# OUTPUT: B


# ════════════════════════════════════════════════════════════════
# EXAMPLE 46 — all() and any()
# ════════════════════════════════════════════════════════════════
# WHAT   : all() -> True if EVERY item is true. any() -> True if AT LEAST one is.
# SYNTAX : all(iterable)  /  any(iterable)
# RETURNS: True or False.
# WHY    : Summarise many True/False values at once.
# WHEN   : "Did everything pass?" / "Did anything fail?".

checks = [True, True, False]
print(all(checks))   # all true? -> False
print(any(checks))   # any true? -> True
# OUTPUT:
# False
# True


# ════════════════════════════════════════════════════════════════
# EXAMPLE 47 — Sorting by putting the sort-key FIRST (no key= needed)
# ════════════════════════════════════════════════════════════════
# WHAT   : Python sorts tuples by their FIRST item automatically.
# SYNTAX : sorted(list_of_tuples)
# WHY    : A no-extra-tools way to sort records by a chosen field.
# WHEN   : When you can arrange data as (sort_value, ...).

items = [(3, "b"), (1, "a"), (2, "c")]   # (priority, name)
print(sorted(items))                      # sorts by priority -> [(1,'a'),(2,'c'),(3,'b')]
# OUTPUT: [(1, 'a'), (2, 'c'), (3, 'b')]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 48 — De-duplicate AND sort in one expression
# ════════════════════════════════════════════════════════════════
# WHAT   : set() removes duplicates; sorted() orders them.
# SYNTAX : sorted(set(my_list))
# RETURNS: a clean, ordered, duplicate-free list.
# WHY    : Common data-cleaning combo.
# WHEN   : Tidying messy lists.

seq = [3, 1, 2, 3, 1]
print(sorted(set(seq)))   # unique + sorted -> [1, 2, 3]
# OUTPUT: [1, 2, 3]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 49 — Unpack a record tuple and use it
# ════════════════════════════════════════════════════════════════
# WHAT   : Tuples make great fixed records; unpack them when used.
# SYNTAX : a, b, c = my_tuple
# WHY    : Clear names beat point[0], point[1], point[2].
# WHEN   : Coordinates, fixed groups.

point3d = (1, 2, 3)
px, py, pz = point3d
print(px + py + pz)   # -> 6
# OUTPUT: 6


# ════════════════════════════════════════════════════════════════
# EXAMPLE 50 — Capstone: build a report from nested data
# ════════════════════════════════════════════════════════════════
# WHAT   : Combine dict access, sum(), max(), and an f-string.
# WHY    : Shows the advanced tools working together.
# WHEN   : Producing a calculated summary from structured data.

team = {"name": "Falcons", "scores": [10, 25, 15]}
print(f"{team['name']} total={sum(team['scores'])} best={max(team['scores'])}")
# OUTPUT: Falcons total=50 best=25


print("\nLevel 4 complete! 50 advanced concepts, every line explained.")
print("You now understand variables deeply. Next stop: functions (def)!")