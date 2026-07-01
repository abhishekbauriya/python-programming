"""
 ██████╗ ██████╗ ███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ ███████╗
██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝
██║   ██║██████╔╝█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝███████╗
██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗╚════██║
╚██████╔╝██║     ███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║███████║
 ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝

Python Operators — A Beginner's Guide (with explanations)
=========================================================

This file teaches you EVERY Python operator, step by step. It is the
companion to variables.py — same explained-and-commented style, so your
repo reads as one consistent beginner series.

Read the comments (lines starting with #) — they explain EVERY line:
what it does, why you use it, when to use it, and mistakes to avoid.

WHAT IS THIS FILE?
------------------
This single file teaches you EVERY Python operator, step by step.
It is split into 4 levels, each with 50 examples:

    LEVEL 1  ->  BASICS          (examples  1–50)   Arithmetic, comparison, assignment
    LEVEL 2  ->  INTERMEDIATE    (examples 51–100)  Logical, membership, identity, augmented
    LEVEL 3  ->  INTERMEDIATE+   (examples 101–150) Bitwise, precedence, ternary, walrus
    LEVEL 4  ->  ADVANCED        (examples 151–200) Operator overloading, @, unpacking, operator module

Then there are 5 MINI-PROJECTS that use operators for real, tiny programs.

HOW TO RUN THIS FILE
--------------------
Open a terminal in the same folder and type:

    python operators.py

Everything below will print to your screen in order.

TIP: Read the comments (the green text starting with #). Comments are notes
for humans — Python completely ignores them when it runs the code.
"""

# ─────────────────────────────────────────────────────────────────────────────
# 🧒 ABSOLUTE-BEGINNER PRIMER  (read this once, then you'll understand everything)
# ─────────────────────────────────────────────────────────────────────────────
#
# Before operators, here are the 4 tiny building blocks used in every example.
#
# 1) A COMMENT starts with '#'. Python ignores it. It's just a note to yourself.
#        # this whole line is ignored by Python
#
# 2) A VARIABLE is a labelled box that stores a value. You create it with '='.
#        age = 25          # 'age' is the box, 25 is the value inside it
#    The '=' here is the ASSIGNMENT operator (your very first operator!).
#
# 3) print(...) shows something on the screen so you can SEE the result.
#        print(age)        # shows: 25
#
# 4) "def" — you asked WHY we use "def", so here is the honest answer:
#        "def" stands for DEFINE. It creates a reusable named block of code
#        called a FUNCTION. Think of a function as a recipe you write once and
#        can "cook" (call) many times without rewriting the steps.
#
#        # Without def, you'd repeat the same lines everywhere.
#        # WITH def, you write the steps once and reuse them.
#
#        def greet():          # define a recipe named 'greet'
#            print("Hello!")   # the step inside the recipe (indented = inside)
#
#        greet()               # "cook" the recipe -> prints: Hello!
#        greet()               # cook it again      -> prints: Hello!
#
#    In the BASICS and INTERMEDIATE levels we mostly avoid 'def' to keep things
#    simple. We only introduce it later (and in the mini-projects) once you're
#    comfortable — and every time we use it, we'll remind you what it means.
#
# 5) INDENTATION (the spaces at the start of a line) tells Python what is
#    "inside" something. Lines indented under 'def' are inside that function.
#    Use 4 spaces. This matters in Python — it is not just for looks!
#
# Okay — you now know enough to understand the entire file. Let's go. 🚀


# A tiny helper so the printed output has clear, pretty section titles.
# (This uses 'def' — remember: it just defines a reusable recipe.)
def title(text):
    """Print a nice section title. 'text' is the heading to show."""
    line = "═" * 70          # make a line of 70 '═' characters
    print("\n" + line)       # \n = a blank line before, for spacing
    print(f"  {text}")       # f"..." lets us drop variables inside text
    print(line)


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  LEVEL 1 — BASICS  (Examples 1–50)                                         ║
# ║  Arithmetic • Comparison • Assignment                                      ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# WHAT ARE OPERATORS?
#   An OPERATOR is a symbol that performs an action on values.
#   The values it works on are called OPERANDS.
#       3   +   4
#       ^   ^   ^
#    operand op operand
#
# We start with the operators you already know from a calculator.

title("LEVEL 1 — BASICS: Arithmetic Operators")

# ── The '+' operator (ADDITION) ──────────────────────────────────────────────
# SYNTAX:        a + b
# DESCRIPTION:   Adds two numbers together.
# PARAMETERS:    a, b -> the two numbers (operands) on each side.
# RETURN VALUE:  Their sum (a number).
# WHEN TO USE:   Any time you need a total.
print("Example 1  | 3 + 4 =", 3 + 4)          # -> 7

# '+' also JOINS (concatenates) two strings. Same symbol, different job,
# depending on the TYPE of the operands (numbers add, text joins).
print("Example 2  | 'Py' + 'thon' =", "Py" + "thon")   # -> Python
# COMMON MISTAKE: You CANNOT mix text and number with '+'.
#   "age " + 25  -> ERROR. Fix it by converting: "age " + str(25)
print("Example 3  | 'age ' + str(25) =", "age " + str(25))

# ── The '-' operator (SUBTRACTION) ───────────────────────────────────────────
# SYNTAX: a - b   RETURNS: the difference.
print("Example 4  | 10 - 3 =", 10 - 3)        # -> 7
# '-' can also be UNARY (used with a single operand) to make a number negative.
print("Example 5  | -5 (negative five) =", -5)
print("Example 6  | -(3 + 2) =", -(3 + 2))    # -> -5

# ── The '*' operator (MULTIPLICATION) ────────────────────────────────────────
# SYNTAX: a * b   RETURNS: the product.
print("Example 7  | 6 * 7 =", 6 * 7)          # -> 42
# '*' with a string REPEATS it. "ab" * 3 -> "ababab"
print("Example 8  | 'ha' * 3 =", "ha" * 3)    # -> hahaha
print("Example 9  | '-' * 10 =", "-" * 10)    # a quick way to draw a line

# ── The '/' operator (TRUE DIVISION) ─────────────────────────────────────────
# SYNTAX: a / b   RETURNS: a FLOAT (a number with a decimal point), ALWAYS.
print("Example 10 | 7 / 2 =", 7 / 2)          # -> 3.5
print("Example 11 | 8 / 2 =", 8 / 2)          # -> 4.0  (note: 4.0, not 4)
# COMMON MISTAKE: Dividing by zero crashes the program.
#   5 / 0  -> ZeroDivisionError. Always make sure the divisor isn't 0.

# ── The '//' operator (FLOOR / INTEGER DIVISION) ─────────────────────────────
# SYNTAX: a // b   RETURNS: the division result rounded DOWN to a whole number.
# WHEN TO USE: When you only care about "how many whole times it fits".
print("Example 12 | 7 // 2 =", 7 // 2)        # -> 3  (3.5 rounded down)
print("Example 13 | 17 // 5 =", 17 // 5)      # -> 3  (5 fits 3 whole times)
print("Example 14 | -7 // 2 =", -7 // 2)      # -> -4 (rounds DOWN, toward negative)

# ── The '%' operator (MODULO / REMAINDER) ────────────────────────────────────
# SYNTAX: a % b   RETURNS: what is LEFT OVER after dividing.
# WHEN TO USE: Checking even/odd, wrapping around (clock math), grouping.
print("Example 15 | 7 % 2 =", 7 % 2)          # -> 1  (7 = 3*2 + 1 leftover)
print("Example 16 | 10 % 5 =", 10 % 5)        # -> 0  (divides evenly)
print("Example 17 | 14 % 12 =", 14 % 12)      # -> 2  (like 14 o'clock = 2pm)
# The classic even/odd test: a number is EVEN when 'n % 2 == 0'.
print("Example 18 | 8 % 2 == 0 (is 8 even?) ->", 8 % 2 == 0)   # -> True

# ── The '**' operator (EXPONENT / POWER) ─────────────────────────────────────
# SYNTAX: a ** b   RETURNS: a raised to the power b.
print("Example 19 | 2 ** 3 =", 2 ** 3)        # -> 8  (2*2*2)
print("Example 20 | 5 ** 2 =", 5 ** 2)        # -> 25 (5 squared)
print("Example 21 | 9 ** 0.5 =", 9 ** 0.5)    # -> 3.0 (power 0.5 = square root)
print("Example 22 | 10 ** -1 =", 10 ** -1)    # -> 0.1 (negative power = 1/10)

# ── Combining arithmetic operators ───────────────────────────────────────────
# Python follows math order: ** first, then * / // %, then + -.
# Use () to force your own order — clearer AND safer.
print("Example 23 | 2 + 3 * 4 =", 2 + 3 * 4)          # -> 14 (3*4 first)
print("Example 24 | (2 + 3) * 4 =", (2 + 3) * 4)      # -> 20 (parentheses first)
print("Example 25 | 2 ** 3 ** 2 =", 2 ** 3 ** 2)      # -> 512 ('**' goes right-to-left: 2**(3**2))


title("LEVEL 1 — BASICS: Comparison Operators")
# ─────────────────────────────────────────────────────────────────────────────
# COMPARISON operators compare two values and ALWAYS return a BOOLEAN:
# either True or False. These are the yes/no questions of programming.
# ─────────────────────────────────────────────────────────────────────────────

# ── '==' EQUAL TO ── asks "are these the same value?" (TWO equals signs!)
# COMMON MISTAKE: using one '=' (assignment) when you mean '==' (comparison).
print("Example 26 | 5 == 5 ->", 5 == 5)       # -> True
print("Example 27 | 5 == 6 ->", 5 == 6)       # -> False
print("Example 28 | 'cat' == 'cat' ->", "cat" == "cat")   # -> True

# ── '!=' NOT EQUAL TO ── asks "are these different?"
print("Example 29 | 5 != 6 ->", 5 != 6)       # -> True
print("Example 30 | 5 != 5 ->", 5 != 5)       # -> False

# ── '>' GREATER THAN ──
print("Example 31 | 10 > 3 ->", 10 > 3)       # -> True
print("Example 32 | 3 > 10 ->", 3 > 10)       # -> False

# ── '<' LESS THAN ──
print("Example 33 | 3 < 10 ->", 3 < 10)       # -> True

# ── '>=' GREATER THAN OR EQUAL TO ──
print("Example 34 | 5 >= 5 ->", 5 >= 5)       # -> True  (equal counts)
print("Example 35 | 4 >= 5 ->", 4 >= 5)       # -> False

# ── '<=' LESS THAN OR EQUAL TO ──
print("Example 36 | 5 <= 5 ->", 5 <= 5)       # -> True
print("Example 37 | 6 <= 5 ->", 6 <= 5)       # -> False

# Comparisons work on text too (alphabetical / dictionary order).
print("Example 38 | 'apple' < 'banana' ->", "apple" < "banana")  # -> True
print("Example 39 | 'Zoo' < 'apple' ->", "Zoo" < "apple")        # -> True (capitals rank before lowercase)

# Comparing the RESULT of math is very common.
print("Example 40 | (2 + 2) == 4 ->", (2 + 2) == 4)   # -> True


title("LEVEL 1 — BASICS: Assignment (the '=' operator)")
# ─────────────────────────────────────────────────────────────────────────────
# '=' stores a value into a variable. It does NOT mean "equals" in the math
# sense — it means "put the right-hand value into the left-hand box".
# ─────────────────────────────────────────────────────────────────────────────

# ── Basic assignment ──
x = 10                                 # put 10 into a box named x
print("Example 41 | x =", x)           # -> 10

# ── Reassigning ── a variable can be given a new value any time.
x = 20                                 # the old 10 is thrown away
print("Example 42 | x is now", x)      # -> 20

# ── Using a variable to build another ──
price = 100
tax = price * 0.1                      # 10% of price
print("Example 43 | tax =", tax)       # -> 10.0

# ── Multiple assignment ── give several variables values on one line.
a, b, c = 1, 2, 3
print("Example 44 | a, b, c =", a, b, c)   # -> 1 2 3

# ── Chained assignment ── give the SAME value to many variables at once.
p = q = r = 0
print("Example 45 | p, q, r =", p, q, r)   # -> 0 0 0

# ── Swapping two variables ── Python's famous one-liner (no temp needed!).
left, right = "L", "R"
left, right = right, left              # swap in a single step
print("Example 46 | after swap:", left, right)   # -> R L

# ── Assignment stores the RESULT, computed once ──
total = 3 + 4 * 5                      # the math runs now; 'total' holds 23
print("Example 47 | total =", total)  # -> 23

# ── Booleans are just values, so you can store a comparison's result ──
is_adult = 20 >= 18
print("Example 48 | is_adult =", is_adult)   # -> True

# ── Variables remember types ── the same box can later hold different types.
value = 5
print("Example 49 | value is a number:", value)
value = "five"                         # now it holds text instead
print("Example 49 | value is now text:", value)

# ── Putting basics together ──
length, width = 8, 3
area = length * width
perimeter = 2 * (length + width)
print("Example 50 | area =", area, "| perimeter =", perimeter)   # -> 24 | 22

# ✅ You finished LEVEL 1! You can now do calculator math, ask yes/no
#    questions with comparisons, and store results in variables.


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  LEVEL 2 — INTERMEDIATE  (Examples 51–100)                                 ║
# ║  Augmented Assignment • Logical • Membership • Identity                    ║
# ╚══════════════════════════════════════════════════════════════════════════╝

title("LEVEL 2 — INTERMEDIATE: Augmented Assignment (+=, -=, ...)")
# ─────────────────────────────────────────────────────────────────────────────
# AUGMENTED assignment is a SHORTCUT: it updates a variable using its own value.
#   x += 5   is exactly the same as   x = x + 5
# WHY USE IT: shorter, clearer, and it says "change x by...".
# ─────────────────────────────────────────────────────────────────────────────

# ── '+=' add-and-store ──
score = 10
score += 5                              # same as: score = score + 5
print("Example 51 | score after += 5 ->", score)   # -> 15

# ── '-=' subtract-and-store ──
lives = 3
lives -= 1
print("Example 52 | lives after -= 1 ->", lives)   # -> 2

# ── '*=' multiply-and-store ──
money = 100
money *= 2
print("Example 53 | money after *= 2 ->", money)   # -> 200

# ── '/=' divide-and-store (result becomes a float) ──
n = 10
n /= 4
print("Example 54 | n after /= 4 ->", n)           # -> 2.5

# ── '//=' floor-divide-and-store ──
m = 17
m //= 5
print("Example 55 | m after //= 5 ->", m)          # -> 3

# ── '%=' modulo-and-store ──
r = 17
r %= 5
print("Example 56 | r after %= 5 ->", r)           # -> 2

# ── '**=' power-and-store ──
base = 2
base **= 10
print("Example 57 | base after **= 10 ->", base)   # -> 1024

# ── '+=' also works to grow text and lists ──
word = "Py"
word += "thon"                          # append text
print("Example 58 | word after += ->", word)       # -> Python

shopping = ["milk"]
shopping += ["eggs"]                    # add an item list-to-list
print("Example 59 | shopping after += ->", shopping)   # -> ['milk', 'eggs']

# ── A running total: the everyday use of '+=' ──
total = 0
for item_price in [5, 10, 15]:          # 'for' repeats once per item
    total += item_price                 # keep adding into total
print("Example 60 | running total ->", total)       # -> 30
# COMMON MISTAKE: forgetting to set total = 0 BEFORE the loop -> NameError.


title("LEVEL 2 — INTERMEDIATE: Logical Operators (and, or, not)")
# ─────────────────────────────────────────────────────────────────────────────
# LOGICAL operators combine yes/no (boolean) values.
#   and -> True only if BOTH sides are True
#   or  -> True if AT LEAST ONE side is True
#   not -> flips True<->False
# ─────────────────────────────────────────────────────────────────────────────

# ── 'and' ──
print("Example 61 | True and True ->", True and True)     # -> True
print("Example 62 | True and False ->", True and False)   # -> False
age = 25
print("Example 63 | age>18 and age<65 ->", age > 18 and age < 65)   # -> True

# ── 'or' ──
print("Example 64 | True or False ->", True or False)     # -> True
print("Example 65 | False or False ->", False or False)   # -> False
day = "Sunday"
print("Example 66 | weekend? ->", day == "Saturday" or day == "Sunday")   # -> True

# ── 'not' ──
print("Example 67 | not True ->", not True)               # -> False
is_raining = False
print("Example 68 | not is_raining ->", not is_raining)   # -> True

# ── Combining them (use () to stay clear) ──
temp = 22
print("Example 69 | nice weather? ->", (temp > 18 and temp < 30) and not is_raining)  # -> True

# ── SHORT-CIRCUIT behaviour (important & clever!) ──
# 'and' stops at the first False; 'or' stops at the first True.
# This lets you guard against errors, e.g. check something exists first.
name = ""
print("Example 70 | name and name[0] ->", name and name[0])
# Because name is "" (falsy), 'and' short-circuits and returns "" WITHOUT
# ever running name[0] — which would have crashed on empty text.

# ── Truthiness: non-booleans have a True/False "feel" ──
# Falsy values: 0, 0.0, "", [], {}, None. Everything else is truthy.
print("Example 71 | bool(0) ->", bool(0))          # -> False
print("Example 72 | bool('') ->", bool(""))        # -> False
print("Example 73 | bool('hi') ->", bool("hi"))    # -> True
print("Example 74 | bool([]) ->", bool([]))        # -> False (empty list)
print("Example 75 | bool([1]) ->", bool([1]))      # -> True

# ── 'or' for default values (a common real trick) ──
user_input = ""                          # imagine the user typed nothing
name_to_show = user_input or "Guest"     # "" is falsy, so fall back to "Guest"
print("Example 76 | name_to_show ->", name_to_show)   # -> Guest

# ── 'and'/'or' return the actual operand, not just True/False ──
print("Example 77 | 3 and 5 ->", 3 and 5)          # -> 5 (both truthy -> last one)
print("Example 78 | 0 or 9 ->", 0 or 9)            # -> 9 (0 falsy -> the other)
print("Example 79 | 'a' and 'b' ->", "a" and "b")  # -> b

# ── COMMON MISTAKE: writing math-style 'and' wrong ──
# WRONG idea: if 1 < x < 10 and > 0  (broken). Chain properly instead:
x = 5
print("Example 80 | 1 < x < 10 ->", 1 < x < 10)    # -> True (Python allows chaining!)


title("LEVEL 2 — INTERMEDIATE: Membership (in / not in)")
# ─────────────────────────────────────────────────────────────────────────────
# 'in' checks whether a value EXISTS inside a collection (list, string, etc.).
# Returns True/False. 'not in' is the opposite.
# ─────────────────────────────────────────────────────────────────────────────

fruits = ["apple", "banana", "cherry"]
print("Example 81 | 'banana' in fruits ->", "banana" in fruits)    # -> True
print("Example 82 | 'mango' in fruits ->", "mango" in fruits)      # -> False
print("Example 83 | 'mango' not in fruits ->", "mango" not in fruits)  # -> True

# ── 'in' on a string checks for a substring (part of the text) ──
sentence = "hello world"
print("Example 84 | 'world' in sentence ->", "world" in sentence)  # -> True
print("Example 85 | 'z' in sentence ->", "z" in sentence)          # -> False

# ── 'in' on a dictionary checks the KEYS ──
prices = {"pen": 5, "book": 50}
print("Example 86 | 'pen' in prices ->", "pen" in prices)          # -> True (key)
print("Example 87 | 5 in prices ->", 5 in prices)                  # -> False (5 is a value, not a key)

# ── 'in' on a range / set ──
print("Example 88 | 3 in range(5) ->", 3 in range(5))             # -> True (0,1,2,3,4)
print("Example 89 | 7 in {1, 3, 7} ->", 7 in {1, 3, 7})          # -> True

# ── Practical use: react to what's inside ──
password = "abc123"
has_digit = any(ch in "0123456789" for ch in password)  # is any char a digit?
print("Example 90 | password has a digit ->", has_digit)   # -> True


title("LEVEL 2 — INTERMEDIATE: Identity (is / is not)")
# ─────────────────────────────────────────────────────────────────────────────
# '==' asks "same VALUE?".  'is' asks "the SAME OBJECT in memory?".
# They are NOT the same question. This trips up almost every beginner.
# RULE OF THUMB: use '==' for values; use 'is' ONLY with None, True, False.
# ─────────────────────────────────────────────────────────────────────────────

a = [1, 2, 3]
b = [1, 2, 3]          # a separate list that happens to look identical
c = a                  # c is another label for the SAME list as a

print("Example 91 | a == b ->", a == b)      # -> True  (same contents)
print("Example 92 | a is b ->", a is b)      # -> False (two different objects)
print("Example 93 | a is c ->", a is c)      # -> True  (same object)

# ── The correct, idiomatic use of 'is' ──
value = None                              # None means "no value / empty"
print("Example 94 | value is None ->", value is None)          # -> True (preferred)
print("Example 95 | value is not None ->", value is not None)  # -> False

# ── COMMON MISTAKE: using 'is' to compare numbers or strings ──
# It may sometimes look like it works, but it's unreliable. Use '==' instead.
big = 1000
also_big = 1000
print("Example 96 | 1000 == 1000 ->", big == also_big)   # -> True  (correct way)
# Avoid:  big is also_big  (may be True or False depending on Python internals)

# ── Show that changing 'a' also changes 'c' (same object!) ──
a.append(4)
print("Example 97 | after a.append(4), c ->", c)   # -> [1, 2, 3, 4] (c changed too!)

# ── 'is' with booleans ──
flag = True
print("Example 98 | flag is True ->", flag is True)   # -> True

# ── Copy to get a truly separate object ──
original = [1, 2]
copy = original[:]                         # slice makes a fresh copy
print("Example 99 | original is copy ->", original is copy)   # -> False
print("Example 99 | original == copy ->", original == copy)   # -> True

# ── Recap comparison of == vs is ──
print("Example 100 | Summary: '==' compares values, 'is' compares identity.")

# ✅ You finished LEVEL 2! You can now update variables in place, combine
#    conditions, search inside collections, and tell '==' apart from 'is'.


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  LEVEL 3 — INTERMEDIATE+  (Examples 101–150)                               ║
# ║  Bitwise • Shifts • Precedence • Ternary • Walrus • Chaining               ║
# ╚══════════════════════════════════════════════════════════════════════════╝

title("LEVEL 3 — INTERMEDIATE+: Bitwise Operators")
# ─────────────────────────────────────────────────────────────────────────────
# Computers store numbers in BINARY (only 0s and 1s). Bitwise operators work on
# those individual bits. You rarely need them as a beginner, but they're great
# to understand. Helper: bin(n) shows a number's binary form.
#   5  is  0b101   (that's 4 + 0 + 1)
#   3  is  0b011   (that's 0 + 2 + 1)
# ─────────────────────────────────────────────────────────────────────────────

print("Example 101 | bin(5) ->", bin(5))     # -> 0b101
print("Example 102 | bin(3) ->", bin(3))     # -> 0b11

# ── '&' bitwise AND ── a bit is 1 only if BOTH bits are 1 ──
# 5 = 101, 3 = 011  ->  001 = 1
print("Example 103 | 5 & 3 ->", 5 & 3)       # -> 1

# ── '|' bitwise OR ── a bit is 1 if EITHER bit is 1 ──
# 5 = 101, 3 = 011  ->  111 = 7
print("Example 104 | 5 | 3 ->", 5 | 3)       # -> 7

# ── '^' bitwise XOR ── a bit is 1 if the bits are DIFFERENT ──
# 5 = 101, 3 = 011  ->  110 = 6
print("Example 105 | 5 ^ 3 ->", 5 ^ 3)       # -> 6

# ── '~' bitwise NOT ── flips every bit; result is -(n+1) ──
print("Example 106 | ~5 ->", ~5)             # -> -6

# ── '<<' LEFT SHIFT ── move bits left; each shift multiplies by 2 ──
print("Example 107 | 1 << 3 ->", 1 << 3)     # -> 8  (1 * 2 * 2 * 2)
print("Example 108 | 3 << 2 ->", 3 << 2)     # -> 12 (3 * 4)

# ── '>>' RIGHT SHIFT ── move bits right; each shift divides by 2 (floor) ──
print("Example 109 | 16 >> 2 ->", 16 >> 2)   # -> 4  (16 / 2 / 2)
print("Example 110 | 7 >> 1 ->", 7 >> 1)     # -> 3  (7 // 2)

# ── Augmented bitwise (&=, |=, ^=, <<=, >>=) ──
flags = 0b0000
flags |= 0b0001                              # turn ON the 1st bit
print("Example 111 | flags |= 1 ->", bin(flags))   # -> 0b1
flags |= 0b0100                              # turn ON the 3rd bit
print("Example 112 | flags |= 4 ->", bin(flags))   # -> 0b101
flags &= ~0b0001                             # turn OFF the 1st bit
print("Example 113 | turn off bit 1 ->", bin(flags))   # -> 0b100

# ── Bit tricks ──
print("Example 114 | is 6 even? (6 & 1 == 0) ->", 6 & 1 == 0)   # -> True (last bit 0 = even)
print("Example 115 | is 7 even? (7 & 1 == 0) ->", 7 & 1 == 0)   # -> False
x, y = 4, 9
x ^= y; y ^= x; x ^= y                       # swap without a temp using XOR
print("Example 116 | XOR swap -> x,y =", x, y)   # -> 9 4

# ── Bitwise operators ALSO work on sets (very useful!) ──
A = {1, 2, 3}
B = {2, 3, 4}
print("Example 117 | A & B (intersection) ->", A & B)   # -> {2, 3}
print("Example 118 | A | B (union) ->", A | B)          # -> {1, 2, 3, 4}
print("Example 119 | A ^ B (symmetric diff) ->", A ^ B) # -> {1, 4}
print("Example 120 | A - B (difference) ->", A - B)     # -> {1}


title("LEVEL 3 — INTERMEDIATE+: Operator Precedence")
# ─────────────────────────────────────────────────────────────────────────────
# PRECEDENCE = which operator runs first. Highest to lowest (common ones):
#   ()  ->  **  ->  unary -  ->  * / // %  ->  + -  ->  comparisons  ->
#   not  ->  and  ->  or
# GOLDEN RULE: when unsure, add parentheses. Clarity beats cleverness.
# ─────────────────────────────────────────────────────────────────────────────

print("Example 121 | 2 + 3 * 4 ->", 2 + 3 * 4)              # -> 14
print("Example 122 | (2 + 3) * 4 ->", (2 + 3) * 4)          # -> 20
print("Example 123 | 2 ** 2 ** 3 ->", 2 ** 2 ** 3)          # -> 256 (** is right-to-left)
print("Example 124 | -3 ** 2 ->", -3 ** 2)                  # -> -9 (** before unary minus!)
print("Example 125 | (-3) ** 2 ->", (-3) ** 2)              # -> 9
print("Example 126 | 10 - 4 - 3 ->", 10 - 4 - 3)            # -> 3 (- is left-to-right)
print("Example 127 | True or False and False ->", True or False and False)  # -> True (and before or)
print("Example 128 | (True or False) and False ->", (True or False) and False)  # -> False
print("Example 129 | not 5 > 3 ->", not 5 > 3)              # -> False (> before not)
print("Example 130 | 5 + 3 > 6 ->", 5 + 3 > 6)             # -> True (+ before >)


title("LEVEL 3 — INTERMEDIATE+: Ternary (Conditional Expression)")
# ─────────────────────────────────────────────────────────────────────────────
# A one-line if/else that RETURNS a value.
# SYNTAX:  value_if_true  if  condition  else  value_if_false
# WHEN TO USE: to pick between two values compactly.
# ─────────────────────────────────────────────────────────────────────────────

age = 20
status = "adult" if age >= 18 else "minor"
print("Example 131 | status ->", status)                   # -> adult

n = 7
label = "even" if n % 2 == 0 else "odd"
print("Example 132 | label ->", label)                     # -> odd

score = 55
result = "pass" if score >= 60 else "fail"
print("Example 133 | result ->", result)                   # -> fail

# ── Ternary inside an f-string ──
temp = 30
print(f"Example 134 | It is {'hot' if temp > 25 else 'mild'}")   # -> hot

# ── Pick the larger of two (though max() is clearer for real code) ──
a, b = 8, 12
bigger = a if a > b else b
print("Example 135 | bigger ->", bigger)                    # -> 12

# ── Guard against divide-by-zero with a ternary ──
count = 0
avg = (100 / count) if count != 0 else 0
print("Example 136 | safe average ->", avg)                 # -> 0

# ── COMMON MISTAKE: don't nest too many ternaries — it becomes unreadable ──
x = 5
sign = "positive" if x > 0 else "zero" if x == 0 else "negative"
print("Example 137 | sign ->", sign)                        # -> positive (readable at most 2)


title("LEVEL 3 — INTERMEDIATE+: Walrus Operator ':='")
# ─────────────────────────────────────────────────────────────────────────────
# ':=' ASSIGNS a value AND returns it, all inside a bigger expression.
# WHEN TO USE: to compute something once and reuse it in the same line.
# NOTE: it is a newer feature (Python 3.8+).
# ─────────────────────────────────────────────────────────────────────────────

# Compute len() once, use it in the condition AND the message.
data = [10, 20, 30, 40]
if (size := len(data)) > 3:
    print("Example 138 | list is big, size =", size)        # size was set by :=

# Without walrus you'd call len(data) twice or add an extra line.
# Reuse a computed value in a print:
print("Example 139 | squared =", (sq := 6 ** 2), "and sq =", sq)   # -> 36 ... 36

# Filter using a value you also want to keep:
nums = [1, 2, 3, 4, 5, 6]
evens = [y for n in nums if (y := n * 10) % 20 == 0]
print("Example 140 | evens ->", evens)                      # -> [20, 40, 60]


title("LEVEL 3 — INTERMEDIATE+: Chained Comparisons & mixing")
# ─────────────────────────────────────────────────────────────────────────────
# Python lets you chain comparisons like math: low < x < high.
# It reads naturally AND only evaluates x once.
# ─────────────────────────────────────────────────────────────────────────────

x = 5
print("Example 141 | 0 < x < 10 ->", 0 < x < 10)            # -> True
print("Example 142 | 0 < x < 3 ->", 0 < x < 3)             # -> False
print("Example 143 | 1 <= x <= 5 ->", 1 <= x <= 5)         # -> True
grade = 85
print("Example 144 | 80 <= grade < 90 (a B?) ->", 80 <= grade < 90)   # -> True

# ── Equality chaining ──
a = b = c = 7
print("Example 145 | a == b == c ->", a == b == c)          # -> True

# ── Mixing arithmetic + comparison + logical in one expression ──
hour = 14
is_afternoon = 12 <= hour < 18
print("Example 146 | is_afternoon ->", is_afternoon)        # -> True

# ── Combine membership + logical ──
role = "editor"
can_edit = role in ("admin", "editor") and role != "banned_editor"
print("Example 147 | can_edit ->", can_edit)                # -> True

# ── Ternary + walrus together ──
text = "hello"
msg = f"length {n2}" if (n2 := len(text)) > 3 else "short"
print("Example 148 | msg ->", msg)                          # -> length 5

# ── Precedence puzzle: solve it, then verify ──
print("Example 149 | 2 + 3 > 4 and 1 < 2 ->", 2 + 3 > 4 and 1 < 2)   # -> True

# ── Bitwise vs logical: '&' is bitwise, 'and' is logical — don't mix them up ──
print("Example 150 | True & False vs True and False ->", True & False, "|", True and False)  # -> False | False

# ✅ You finished LEVEL 3! Bits, precedence, ternaries, walrus, and chaining.


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  LEVEL 4 — ADVANCED  (Examples 151–200)                                    ║
# ║  Operator Overloading • @ • Unpacking * ** • operator module              ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# QUICK PRIMER for this level (two new words):
#
#   CLASS  -> a blueprint for making your own type of object. Written with the
#             'class' keyword. Example below makes a 'Money' type.
#
#   METHOD -> a function that lives INSIDE a class. It's still made with 'def'
#             (remember: def = "define a reusable block"). Methods whose names
#             start and end with double underscores, like __add__, are called
#             "DUNDER" (double-underscore) methods. Python calls them
#             automatically when you use an operator on your object.
#
# OPERATOR OVERLOADING = teaching '+', '-', '==', etc. how to work on YOUR own
# objects, by defining the matching dunder method.
#
#   Operator you type     Dunder method Python calls
#   -----------------     ----------------------------
#         a + b                a.__add__(b)
#         a - b                a.__sub__(b)
#         a * b                a.__mul__(b)
#         a == b               a.__eq__(b)
#         a < b                a.__lt__(b)
#         len(a)               a.__len__()
#         print(a)             a.__str__()

title("LEVEL 4 — ADVANCED: Operator Overloading with a Money class")

class Money:
    """A tiny custom type that stores an amount and knows how to do math."""

    # __init__ is the SETUP method: it runs when you create a Money(...).
    # 'self' means "this particular object". 'amount' is the value passed in.
    def __init__(self, amount):
        self.amount = amount            # store the value inside the object

    # __str__ controls what print() shows for this object.
    def __str__(self):
        return f"${self.amount}"

    # __add__ teaches the '+' operator. 'other' is the value on the right.
    def __add__(self, other):
        return Money(self.amount + other.amount)   # return a NEW Money

    # __sub__ teaches '-'
    def __sub__(self, other):
        return Money(self.amount - other.amount)

    # __mul__ teaches '*' (here: multiply money by a plain number)
    def __mul__(self, factor):
        return Money(self.amount * factor)

    # __eq__ teaches '==' (are two Moneys worth the same?)
    def __eq__(self, other):
        return self.amount == other.amount

    # __lt__ teaches '<' (used for sorting and comparisons)
    def __lt__(self, other):
        return self.amount < other.amount

wallet = Money(100)
gift = Money(50)

print("Example 151 | wallet ->", wallet)               # -> $100  (uses __str__)
print("Example 152 | wallet + gift ->", wallet + gift) # -> $150  (uses __add__)
print("Example 153 | wallet - gift ->", wallet - gift) # -> $50   (uses __sub__)
print("Example 154 | gift * 3 ->", gift * 3)           # -> $150  (uses __mul__)
print("Example 155 | wallet == Money(100) ->", wallet == Money(100))   # -> True (__eq__)
print("Example 156 | gift < wallet ->", gift < wallet)                 # -> True (__lt__)
print("Example 157 | sorted list ->", [str(m) for m in sorted([wallet, gift, Money(75)])])  # uses __lt__

# ── More dunder methods on a Vector (2D arrow) ──
class Vector:
    """A 2D vector (x, y) with rich operator support."""
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __repr__(self):                 # __repr__ = developer-friendly text
        return f"Vector({self.x}, {self.y})"
    def __add__(self, o):
        return Vector(self.x + o.x, self.y + o.y)
    def __sub__(self, o):
        return Vector(self.x - o.x, self.y - o.y)
    def __mul__(self, k):               # scale by a number
        return Vector(self.x * k, self.y * k)
    def __eq__(self, o):
        return self.x == o.x and self.y == o.y
    def __len__(self):                  # __len__ must return a whole number
        return int((self.x ** 2 + self.y ** 2) ** 0.5)
    def __neg__(self):                  # teaches the unary minus:  -v
        return Vector(-self.x, -self.y)

v1 = Vector(2, 3)
v2 = Vector(1, 1)
print("Example 158 | v1 + v2 ->", v1 + v2)     # -> Vector(3, 4)
print("Example 159 | v1 - v2 ->", v1 - v2)     # -> Vector(1, 2)
print("Example 160 | v1 * 3 ->", v1 * 3)       # -> Vector(6, 9)
print("Example 161 | v1 == Vector(2,3) ->", v1 == Vector(2, 3))   # -> True
print("Example 162 | len(Vector(3,4)) ->", len(Vector(3, 4)))     # -> 5
print("Example 163 | -v1 ->", -v1)             # -> Vector(-2, -3)

# ── __contains__ teaches the 'in' operator ──
class Team:
    def __init__(self, members):
        self.members = members
    def __contains__(self, name):
        return name in self.members

team = Team(["Ana", "Ben"])
print("Example 164 | 'Ana' in team ->", "Ana" in team)     # -> True (__contains__)
print("Example 165 | 'Xy' in team ->", "Xy" in team)       # -> False

# ── __getitem__ teaches square-bracket access  obj[i] ──
class Squares:
    def __getitem__(self, i):
        return i * i

sq = Squares()
print("Example 166 | Squares()[5] ->", sq[5])              # -> 25 (__getitem__)

# ── __call__ makes an object callable like a function ──
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    def __call__(self, x):
        return x * self.factor

double = Multiplier(2)
print("Example 167 | double(21) ->", double(21))          # -> 42 (__call__)

# ── COMMON MISTAKE reminder ──
print("Example 168 | If you define __eq__ but not __lt__, sorting your")
print("             | objects will fail. Define the operators you actually use.")


title("LEVEL 4 — ADVANCED: The '@' matrix-multiply operator")
# ─────────────────────────────────────────────────────────────────────────────
# '@' is the matrix-multiplication operator (dunder __matmul__). Core Python
# doesn't multiply lists with it, but libraries like NumPy do. You can also
# define it yourself. Here's a dot-product example.
# ─────────────────────────────────────────────────────────────────────────────

class Row:
    def __init__(self, values):
        self.values = values
    def __matmul__(self, other):        # teaches the '@' operator
        # dot product: multiply matching items and sum them
        return sum(a * b for a, b in zip(self.values, other.values))

r1 = Row([1, 2, 3])
r2 = Row([4, 5, 6])
print("Example 169 | r1 @ r2 (dot product) ->", r1 @ r2)   # -> 32 (1*4+2*5+3*6)


title("LEVEL 4 — ADVANCED: Unpacking operators '*' and '**'")
# ─────────────────────────────────────────────────────────────────────────────
# Here '*' and '**' are NOT math — they UNPACK collections.
#   *  spreads a list/tuple into separate items
#   ** spreads a dictionary into named (keyword) items
# ─────────────────────────────────────────────────────────────────────────────

nums = [1, 2, 3]
print("Example 170 | print(*nums) ->", end=" ")
print(*nums)                             # same as print(1, 2, 3)

# ── Merge lists with * ──
combined = [*nums, 4, 5]
print("Example 171 | [*nums, 4, 5] ->", combined)          # -> [1, 2, 3, 4, 5]

# ── Merge dictionaries with ** ──
d1 = {"a": 1}
d2 = {"b": 2}
merged = {**d1, **d2}
print("Example 172 | {**d1, **d2} ->", merged)             # -> {'a': 1, 'b': 2}

# ── * in assignment: grab "the rest" ──
first, *rest = [10, 20, 30, 40]
print("Example 173 | first, *rest ->", first, rest)        # -> 10 [20, 30, 40]
*head, last = [1, 2, 3, 4]
print("Example 174 | *head, last ->", head, last)          # -> [1, 2, 3] 4

# ── *args / **kwargs in functions: accept any number of arguments ──
def add_all(*args):                      # 'args' becomes a tuple of everything
    return sum(args)
print("Example 175 | add_all(1,2,3,4) ->", add_all(1, 2, 3, 4))   # -> 10

def describe(**kwargs):                  # 'kwargs' becomes a dict of named args
    return kwargs
print("Example 176 | describe(a=1, b=2) ->", describe(a=1, b=2))  # -> {'a': 1, 'b': 2}

# ── Unpack a list straight into a function call ──
def volume(l, w, h):
    return l * w * h
dims = [2, 3, 4]
print("Example 177 | volume(*dims) ->", volume(*dims))     # -> 24


title("LEVEL 4 — ADVANCED: The 'operator' module & functools")
# ─────────────────────────────────────────────────────────────────────────────
# Every operator has a FUNCTION twin in the built-in 'operator' module.
# Useful when you need to PASS an operator as an argument.
# ─────────────────────────────────────────────────────────────────────────────

import operator                          # 'import' loads a toolbox of functions
from functools import reduce            # reduce combines a list into one value

print("Example 178 | operator.add(3, 4) ->", operator.add(3, 4))   # -> 7 (same as 3 + 4)
print("Example 179 | operator.mul(6, 7) ->", operator.mul(6, 7))   # -> 42
print("Example 180 | operator.eq(5, 5) ->", operator.eq(5, 5))     # -> True
print("Example 181 | operator.gt(9, 2) ->", operator.gt(9, 2))     # -> True
print("Example 182 | operator.contains([1,2,3], 2) ->", operator.contains([1, 2, 3], 2))  # -> True

# ── reduce + operator.mul = multiply an entire list (a "product") ──
factorial_5 = reduce(operator.mul, [1, 2, 3, 4, 5])
print("Example 183 | 5! via reduce(mul) ->", factorial_5)          # -> 120

# ── reduce + operator.add = sum a list ──
print("Example 184 | reduce(add) ->", reduce(operator.add, [10, 20, 30]))   # -> 60

# ── itemgetter: build a "grab index/key" function to use as a sort key ──
people = [("Ana", 30), ("Ben", 25), ("Cid", 40)]
by_age = sorted(people, key=operator.itemgetter(1))   # sort by the age (index 1)
print("Example 185 | sorted by age ->", by_age)

# ── attrgetter: grab an attribute; here sort Money objects by .amount ──
monies = [Money(30), Money(10), Money(20)]
cheapest_first = sorted(monies, key=operator.attrgetter("amount"))
print("Example 186 | sorted Money ->", [str(m) for m in cheapest_first])

# ── A few more identity/verification examples to lock it in ──
print("Example 187 | operator.sub(10, 3) ->", operator.sub(10, 3))     # -> 7
print("Example 188 | operator.floordiv(17,5) ->", operator.floordiv(17, 5))  # -> 3
print("Example 189 | operator.mod(17, 5) ->", operator.mod(17, 5))     # -> 2
print("Example 190 | operator.pow(2, 8) ->", operator.pow(2, 8))       # -> 256
print("Example 191 | operator.neg(5) ->", operator.neg(5))             # -> -5
print("Example 192 | operator.and_(5, 3) ->", operator.and_(5, 3))     # -> 1 (bitwise)
print("Example 193 | operator.or_(5, 3) ->", operator.or_(5, 3))       # -> 7 (bitwise)
print("Example 194 | operator.xor(5, 3) ->", operator.xor(5, 3))       # -> 6
print("Example 195 | operator.lshift(1, 4) ->", operator.lshift(1, 4)) # -> 16
print("Example 196 | operator.rshift(16, 2) ->", operator.rshift(16, 2))   # -> 4
print("Example 197 | operator.not_(False) ->", operator.not_(False))   # -> True
print("Example 198 | operator.truth(0) ->", operator.truth(0))         # -> False
print("Example 199 | operator.concat('a','b') ->", operator.concat("a", "b"))  # -> ab
print("Example 200 | operator.getitem([9,8,7], 1) ->", operator.getitem([9, 8, 7], 1))  # -> 8

# 🎉 You finished all 200 examples across 4 levels! Now let's build things.


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🛠️  MINI-PROJECTS  — operators in tiny real programs                      ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# Each project is wrapped in a function (def) so it stays tidy and you can
# "run" it by calling it. Reminder: def = define a reusable block of steps.

title("MINI-PROJECT 1 — Simple Calculator (arithmetic operators)")

def calculator(a, b):
    """Take two numbers and show every arithmetic operator on them."""
    print(f"  a = {a}, b = {b}")
    print("  a + b  =", a + b)           # addition
    print("  a - b  =", a - b)           # subtraction
    print("  a * b  =", a * b)           # multiplication
    # Guard against divide-by-zero using a ternary (LEVEL 3 idea).
    print("  a / b  =", a / b if b != 0 else "undefined (can't divide by 0)")
    print("  a // b =", a // b if b != 0 else "undefined")
    print("  a % b  =", a % b if b != 0 else "undefined")
    print("  a ** b =", a ** b)          # power

calculator(12, 5)                        # call the function to run it


title("MINI-PROJECT 2 — Number Inspector (%, comparison, logical)")

def inspect_number(n):
    """Report facts about a number using operators."""
    is_even = n % 2 == 0                             # modulo test
    sign = "positive" if n > 0 else "zero" if n == 0 else "negative"  # ternary
    in_range = 0 <= n <= 100                         # chained comparison
    # A prime-ish quick check for small numbers (uses % and 'all')
    is_prime = n > 1 and all(n % d != 0 for d in range(2, int(n ** 0.5) + 1))
    print(f"  {n}: {'even' if is_even else 'odd'}, {sign}, "
          f"{'in 0–100' if in_range else 'out of 0–100'}, "
          f"{'prime' if is_prime else 'not prime'}")

for value in [7, 10, -4, 0, 97]:
    inspect_number(value)


title("MINI-PROJECT 3 — Temperature Converter (arithmetic)")

def convert_temp(celsius):
    """Convert Celsius to Fahrenheit and Kelvin using arithmetic operators."""
    fahrenheit = celsius * 9 / 5 + 32    # precedence: * and / before +
    kelvin = celsius + 273.15
    # Round to 2 decimals for a clean display.
    print(f"  {celsius}°C = {round(fahrenheit, 2)}°F = {round(kelvin, 2)}K")

for c in [0, 25, 37, 100, -40]:
    convert_temp(c)                      # -40 is the point where C and F meet!


title("MINI-PROJECT 4 — Permissions with Bitwise Flags (& | ^ ~ <<)")
# Each permission is a single bit. We combine them with OR and test with AND.
# This is the classic real-world reason bitwise operators exist.

READ    = 1 << 0                         # 0b001  = 1
WRITE   = 1 << 1                         # 0b010  = 2
EXECUTE = 1 << 2                         # 0b100  = 4

def show_permissions(perm):
    """Given a combined permission number, list which powers are ON."""
    print(f"  permission value {perm} (binary {bin(perm)}):")
    print("    can read?   ", bool(perm & READ))     # AND isolates the bit
    print("    can write?  ", bool(perm & WRITE))
    print("    can execute?", bool(perm & EXECUTE))

user = READ | WRITE                      # combine two permissions with OR
show_permissions(user)                   # read+write ON, execute OFF
user |= EXECUTE                          # grant execute too (augmented OR)
print("  ...granted execute...")
show_permissions(user)
user &= ~WRITE                           # revoke write (AND with inverted bit)
print("  ...revoked write...")
show_permissions(user)


title("MINI-PROJECT 5 — Grade Calculator (comparison, logical, ternary)")

def grade_for(score):
    """Turn a 0–100 score into a letter grade."""
    # First, validate the input with a chained comparison + logical 'not'.
    if not (0 <= score <= 100):
        return "invalid"
    # A chain of comparisons decides the letter.
    if score >= 90:
        return "A"
    elif score >= 80:                    # 'elif' = "else, if" (checked in order)
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

for s in [95, 82, 74, 61, 50, 150]:
    passed = grade_for(s) not in ("F", "invalid")     # membership + ternary idea
    print(f"  score {s:>3} -> grade {grade_for(s)} ({'PASS' if passed else 'FAIL'})")


title("MINI-PROJECT 6 — Vector Playground (operator overloading)")
# Reuses the Vector class from LEVEL 4 to show operators on custom objects.

def vector_demo():
    a = Vector(3, 4)
    b = Vector(1, 2)
    print("  a =", a, "| b =", b)
    print("  a + b =", a + b)            # __add__
    print("  a - b =", a - b)            # __sub__
    print("  a * 2 =", a * 2)            # __mul__
    print("  -a    =", -a)               # __neg__
    print("  |a|   =", len(a))           # __len__ (magnitude, whole number)
    print("  a == Vector(3,4)?", a == Vector(3, 4))   # __eq__

vector_demo()


# ─────────────────────────────────────────────────────────────────────────────
# 📌 CHEAT-SHEET (quick reference — scroll here any time)
# ─────────────────────────────────────────────────────────────────────────────
# ARITHMETIC : +  -  *  /  //  %  **
# COMPARISON : ==  !=  >  <  >=  <=
# ASSIGNMENT : =   +=  -=  *=  /=  //=  %=  **=   (and &= |= ^= <<= >>=)
# LOGICAL    : and  or  not
# MEMBERSHIP : in  not in
# IDENTITY   : is  is not
# BITWISE    : &  |  ^  ~  <<  >>
# SPECIAL    : :=  (walrus)   @ (matmul)   * ** (unpacking)   x if c else y (ternary)
#
# TOP BEGINNER MISTAKES TO REMEMBER:
#   1. '=' assigns, '==' compares. Mixing them is the #1 bug.
#   2. '/' always gives a float; use '//' for whole-number division.
#   3. Never divide by zero — check the divisor first.
#   4. Use '==' for values and 'is' only for None / True / False.
#   5. '&' is bitwise, 'and' is logical — they are different.
#   6. When precedence is unclear, add parentheses. Always.
# ─────────────────────────────────────────────────────────────────────────────

# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  📚 MINI REFERENCE — the built-in functions used in this file             ║
# ╚══════════════════════════════════════════════════════════════════════════╝
# Same format as variables.py: SYNTAX · DESCRIPTION · PARAMETERS · RETURNS · WHEN.
#
# print(*values, sep=" ", end="\n")
#   DESCRIPTION : Shows values on the screen.
#   PARAMETERS  : the values to show; 'sep' between them; 'end' after them.
#   RETURNS     : None (it just displays; it doesn't give back a value).
#   WHEN TO USE : any time you want to SEE a result.
#
# str(x)  /  int(x)  /  float(x)
#   DESCRIPTION : Convert a value into text / whole number / decimal number.
#   PARAMETERS  : x -> the value to convert.
#   RETURNS     : the converted value.
#   WHEN TO USE : to join a number to text ("age " + str(25)), or turn typed
#                 text like "5" into the number 5.
#
# bool(x)
#   DESCRIPTION : Convert a value to True/False using truthiness rules.
#   RETURNS     : False for 0, "", [], {}, None; True for everything else.
#   WHEN TO USE : to check if something is "empty/zero" vs "has something".
#
# bin(n)
#   DESCRIPTION : Text showing a whole number in binary (base 2).
#   PARAMETERS  : n -> a whole number.
#   RETURNS     : a string like "0b101".
#   WHEN TO USE : to SEE the bits when learning bitwise operators.
#
# len(x)
#   DESCRIPTION : How many items are in x (or __len__ for your own objects).
#   RETURNS     : a whole number (the count).
#   WHEN TO USE : to measure a list, string, dict, etc.
#
# range(stop)  /  range(start, stop)
#   DESCRIPTION : A sequence of whole numbers (start up to, but NOT including, stop).
#   RETURNS     : a range object you can loop over or test with 'in'.
#   WHEN TO USE : to repeat something a fixed number of times.
#
# sum(iterable)
#   DESCRIPTION : Adds up all numbers in a collection.
#   RETURNS     : the total.
#   WHEN TO USE : totals, averages (sum / len).
#
# sorted(iterable, key=None)
#   DESCRIPTION : Returns a NEW sorted list (uses '<', i.e. __lt__).
#   PARAMETERS  : 'key' -> optional function deciding what to sort by.
#   RETURNS     : a new sorted list (original is unchanged).
#   WHEN TO USE : to order items smallest-to-largest / A-to-Z.
#
# any(iterable)  /  all(iterable)
#   DESCRIPTION : any -> True if AT LEAST ONE item is truthy.
#                 all -> True only if EVERY item is truthy.
#   RETURNS     : True or False.
#   WHEN TO USE : checking conditions across many items at once.
#
# round(number, ndigits)
#   DESCRIPTION : Rounds a number to 'ndigits' decimal places.
#   RETURNS     : the rounded number.
#   WHEN TO USE : cleaner display of decimals (e.g. money, temperatures).
#
# zip(a, b)
#   DESCRIPTION : Pairs up items from two collections, position by position.
#   RETURNS     : an iterator of (a_item, b_item) pairs.
#   WHEN TO USE : looping over two lists together (see the dot-product example).
#
# reduce(function, iterable)   (from functools)
#   DESCRIPTION : Repeatedly combines items into ONE value using 'function'.
#   RETURNS     : the single combined result.
#   WHEN TO USE : product of a list, running combine — see examples 183–184.


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  ✍️  YOUR TURN — small practice tasks (edit, then re-run the file)         ║
# ╚══════════════════════════════════════════════════════════════════════════╝
# Try these yourself. Uncomment a line (remove the leading #) and run again.
# There are no grades — breaking things and fixing them is how you learn. 💪
#
#   1. Print the remainder when 100 is divided by 7.        (hint: %)
#   2. Is 2025 a leap year? A year is a leap year if it is divisible by 4
#      AND (not by 100, OR divisible by 400).               (hint: % and, or)
#   3. Use a ternary to print "big" if a number > 50 else "small".
#   4. Swap two variables using the one-line trick:  a, b = b, a
#   5. Combine READ and EXECUTE permissions with | and check the result with &.
#   6. Give the Vector class a __truediv__ method so you can write  v / 2.
#
# Example starting points (uncomment to try):
# print("Task 1:", 100 % 7)
# year = 2025
# print("Task 2 leap year?:", year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
# num = 73
# print("Task 3:", "big" if num > 50 else "small")


print("\n" + "═" * 70)
print("  🎓 All done! You've seen every Python operator with 200+ examples,")
print("     6 mini-projects, a mini reference, and practice tasks.")
print("     Re-run this file any time:  python operators.py")
print("═" * 70)