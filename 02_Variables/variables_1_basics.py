"""
=====================================================================
 VARIABLES — LEVEL 1: BASICS  (fully explained, no functions)
=====================================================================
This file teaches the BASICS of Python variables. Every example is
explained in detail using these labels:

    WHAT    -> what the example is about (plain English)
    SYNTAX  -> the general pattern / shape of the code
    PARAMS  -> what goes inside a function's ( )  (only when relevant)
    WHY     -> why this is useful
    WHEN    -> when you would use it
    MISTAKE -> a common beginner error to avoid (when relevant)

Then the CODE follows, with a comment on EVERY line, and the OUTPUT
you will see when you run the file.

Run it:   python variables_1_basics.py
=====================================================================
"""

print("LEVEL 1 — BASICS\n")


# ════════════════════════════════════════════════════════════════
# EXAMPLE 1 — Creating a variable (text / string)
# ════════════════════════════════════════════════════════════════
# WHAT   : A variable is a NAME that stores a value so you can reuse it.
# SYNTAX : variable_name = value
# WHY    : So you write a value once and reuse it by its name anywhere.
# WHEN   : Any time you need to remember a piece of information.
# MISTAKE: Text MUST be in quotes. Without quotes Python thinks it's
#          another variable name and you get a NameError.

name = "Alice"     # create a variable called 'name'; '=' STORES the value on
#                    the right into the name on the left. The quotes "" mean
#                    the value is TEXT (called a "string", or 'str').
print(name)        # print() shows the value of 'name' on the screen.
# OUTPUT: Alice


# ════════════════════════════════════════════════════════════════
# EXAMPLE 2 — The print() function explained
# ════════════════════════════════════════════════════════════════
# WHAT   : print() displays things on the screen (the console).
# SYNTAX : print(value1, value2, ...)
# PARAMS : one or more values, separated by commas. print() also has
#          optional 'sep' (what goes between values) and 'end' (what
#          goes at the end) — shown below.
# WHY    : It's how you SEE what your program is doing.
# WHEN   : Constantly — to check values and show results.

print("Hello", "world")            # two values; a comma puts a SPACE between them
print("A", "B", "C", sep="-")      # 'sep' changes the separator -> A-B-C
print("no newline", end=" ")       # 'end' replaces the line break with a space
print("same line")                 # so this prints on the SAME line
# OUTPUT:
# Hello world
# A-B-C
# no newline same line


# ════════════════════════════════════════════════════════════════
# EXAMPLE 3 — Whole numbers (int)
# ════════════════════════════════════════════════════════════════
# WHAT   : An 'int' is a whole number (no decimal point).
# SYNTAX : variable_name = 42
# WHY    : For counting, ages, quantities — anything without a fraction.
# WHEN   : Whenever you need exact whole numbers.

age = 25           # 'age' stores the whole number 25 (NO quotes -> it's a number)
print(age)         # show it
# OUTPUT: 25


# ════════════════════════════════════════════════════════════════
# EXAMPLE 4 — Decimal numbers (float)
# ════════════════════════════════════════════════════════════════
# WHAT   : A 'float' is a number WITH a decimal point.
# SYNTAX : variable_name = 3.5
# WHY    : For measurements, prices, averages — anything with fractions.
# WHEN   : Whenever a value can have a decimal part.

height = 5.9       # the dot makes this a float (a decimal number)
print(height)      # show it
# OUTPUT: 5.9


# ════════════════════════════════════════════════════════════════
# EXAMPLE 5 — True / False values (bool)
# ════════════════════════════════════════════════════════════════
# WHAT   : A 'bool' holds only True or False.
# SYNTAX : variable_name = True   (or False)
# WHY    : To remember yes/no, on/off, done/not-done states.
# WHEN   : For any value that is one of two opposites.
# MISTAKE: Do NOT put quotes around True/False. "True" (with quotes) is
#          TEXT, not a boolean.

is_student = True  # stores the boolean True (capital T, no quotes)
print(is_student)  # show it
# OUTPUT: True


# ════════════════════════════════════════════════════════════════
# EXAMPLE 6 — "Nothing" (None)
# ════════════════════════════════════════════════════════════════
# WHAT   : 'None' is a special value meaning "no value yet" / "empty".
# SYNTAX : variable_name = None
# WHY    : To create a variable now and fill in a real value later.
# WHEN   : When something is unknown or not set yet.

middle_name = None # 'middle_name' exists but holds "nothing" for now
print(middle_name) # show it
# OUTPUT: None


# ════════════════════════════════════════════════════════════════
# EXAMPLE 7 — Comments
# ════════════════════════════════════════════════════════════════
# WHAT   : A comment is a note for humans; Python ignores it.
# SYNTAX : # everything after a hash sign is a comment
# WHY    : To explain your code so you (and others) understand it later.
# WHEN   : Whenever code isn't obvious.

# This whole line is a comment and does nothing when the program runs.
score = 10         # a comment can also sit at the END of a line of code
print(score)       # only the code runs; the comments are skipped
# OUTPUT: 10


# ════════════════════════════════════════════════════════════════
# EXAMPLE 8 — Reassigning a variable (changing its value)
# ════════════════════════════════════════════════════════════════
# WHAT   : You can give a variable a new value any time. The new value
#          REPLACES the old one.
# SYNTAX : variable_name = new_value
# WHY    : Values change as your program runs (scores, counters, etc.).
# WHEN   : Whenever the stored value needs to update.

level = 1          # 'level' starts at 1
print(level)       # -> 1
level = 2          # now 'level' is 2; the old 1 is gone forever
print(level)       # -> 2
# OUTPUT:
# 1
# 2


# ════════════════════════════════════════════════════════════════
# EXAMPLE 9 — Using a variable in a calculation
# ════════════════════════════════════════════════════════════════
# WHAT   : Variables can be used in maths just like the values inside them.
# SYNTAX : new_variable = variable + something
# WHY    : To build new values from existing ones.
# WHEN   : Any calculation that depends on a stored value.
# NOTE   : The RIGHT side is worked out FIRST, then stored on the left.

age = 26           # store 26
next_year = age + 1  # 26 + 1 = 27 is calculated, THEN stored in 'next_year'
print(next_year)   # -> 27
# OUTPUT: 27


# ════════════════════════════════════════════════════════════════
# EXAMPLE 10 — Variable naming RULES
# ════════════════════════════════════════════════════════════════
# WHAT   : Names must follow rules or Python gives an error.
# RULES  : - start with a letter or underscore _
#          - then letters, numbers, or underscores only
#          - NO spaces, NO dashes, NO symbols (! ? @ #)
#          - cannot be a Python keyword (like 'for', 'if', 'class')
# WHY    : These rules let Python tell names apart from other code.
# WHEN   : Every time you name something.

user_name = "Bob"  # letters + underscore           -> OK
score2 = 100       # a number is fine (not at start) -> OK
_secret = True     # starting with underscore        -> OK
print(user_name, score2, _secret)
# OUTPUT: Bob 100 True
# MISTAKE (these would ERROR, shown as comments so the file still runs):
#   2nd = 1        # starts with a number  -> SyntaxError
#   my-name = 1    # has a dash            -> SyntaxError
#   my name = 1    # has a space           -> SyntaxError


# ════════════════════════════════════════════════════════════════
# EXAMPLE 11 — Variable naming CONVENTION (snake_case)
# ════════════════════════════════════════════════════════════════
# WHAT   : A convention is an agreed STYLE (not a rule). Python uses
#          "snake_case": all lowercase, words joined by underscores.
# SYNTAX : first_name, total_price, is_active
# WHY    : Consistent names make code easy to read for everyone.
# WHEN   : For all normal variable names.

first_name = "Anna"        # readable: lowercase words joined by _
total_price = 19.99        # another snake_case example
print(first_name, total_price)
# OUTPUT: Anna 19.99


# ════════════════════════════════════════════════════════════════
# EXAMPLE 12 — Names are case-sensitive
# ════════════════════════════════════════════════════════════════
# WHAT   : Capital and lowercase letters are DIFFERENT to Python.
# WHY    : 'age', 'Age', and 'AGE' are three separate variables.
# WHEN   : Be consistent so you don't accidentally make a new variable.
# MISTAKE: Typing 'Name' when you meant 'name' creates/uses a DIFFERENT
#          variable (or causes a NameError).

city = "Paris"     # lowercase 'city'
City = "London"    # capital 'City' is a completely separate variable
print(city)        # -> Paris
print(City)        # -> London
# OUTPUT:
# Paris
# London


# ════════════════════════════════════════════════════════════════
# EXAMPLE 13 — Single vs double quotes for text
# ════════════════════════════════════════════════════════════════
# WHAT   : Strings can use 'single' or "double" quotes — both work.
# SYNTAX : 'text'  or  "text"
# WHY    : Pick whichever avoids clashing with quotes inside the text.
# WHEN   : Use double quotes if the text contains an apostrophe, etc.

a = 'hello'        # single quotes
b = "world"        # double quotes
c = "it's nice"    # double quotes let us include the ' apostrophe easily
print(a, b, c)
# OUTPUT: hello world it's nice


# ════════════════════════════════════════════════════════════════
# EXAMPLE 14 — Joining text with + (concatenation)
# ════════════════════════════════════════════════════════════════
# WHAT   : The + symbol GLUES two strings together.
# SYNTAX : "text1" + "text2"
# WHY    : To build a bigger piece of text from smaller ones.
# WHEN   : Combining words/labels into one string.
# MISTAKE: + does not add a space automatically — add " " yourself.

first = "John"
last = "Smith"
full = first + " " + last   # glue first, a space, and last together
print(full)                 # -> John Smith
# OUTPUT: John Smith


# ════════════════════════════════════════════════════════════════
# EXAMPLE 15 — Repeating text with *
# ════════════════════════════════════════════════════════════════
# WHAT   : The * symbol REPEATS a string a number of times.
# SYNTAX : "text" * number
# WHY    : Quick way to make repeated patterns or separators.
# WHEN   : Drawing lines, repeating characters, etc.

line = "-" * 10    # repeat "-" ten times
print(line)        # -> ----------
print("ha" * 3)    # -> hahaha
# OUTPUT:
# ----------
# hahaha


# ════════════════════════════════════════════════════════════════
# EXAMPLE 16 — f-strings (the best way to build text from variables)
# ════════════════════════════════════════════════════════════════
# WHAT   : An f-string lets you drop variables directly inside text.
# SYNTAX : f"some text {variable} more text"
# WHY    : Much cleaner than gluing pieces with + and str().
# WHEN   : Almost always, when mixing variables into messages.
# MISTAKE: Forgetting the 'f' -> "{name}" prints literally, not the value.

name = "Alice"
age = 26
message = f"{name} is {age} years old"  # {name} and {age} are replaced by values
print(message)                          # -> Alice is 26 years old
# OUTPUT: Alice is 26 years old


# ════════════════════════════════════════════════════════════════
# EXAMPLE 17 — type() : check what KIND of value something is
# ════════════════════════════════════════════════════════════════
# WHAT   : type() tells you a value's type (int, str, float, bool...).
# SYNTAX : type(value)
# PARAMS : value -> the thing you want to inspect.
# RETURNS: the type object, e.g. <class 'int'>.
# WHY    : To understand or debug what you're working with.
# WHEN   : When a value behaves unexpectedly, check its type.
# NOTE   : .__name__ gives the short clean name ('int' instead of <class 'int'>).

print(type(25).__name__)      # -> int
print(type("hi").__name__)    # -> str
print(type(3.5).__name__)     # -> float
print(type(True).__name__)    # -> bool
# OUTPUT:
# int
# str
# float
# bool


# ════════════════════════════════════════════════════════════════
# EXAMPLE 18 — int() : convert a value into a whole number
# ════════════════════════════════════════════════════════════════
# WHAT   : int() turns text or a decimal into a whole number.
# SYNTAX : int(value)
# PARAMS : value -> a number, or numeric text like "42".
# RETURNS: a whole number (int).
# WHY    : Numbers often arrive as TEXT and you need to do maths.
# WHEN   : Converting input/text before calculating.
# MISTAKE: int("3.5") errors. Convert through float: int(float("3.5")).

text_number = "7"             # this is TEXT, even though it looks numeric
real_number = int(text_number)  # convert "7" -> 7
print(real_number + 3)        # now maths works -> 10
print(int(3.9))               # a decimal is CUT OFF (not rounded) -> 3
# OUTPUT:
# 10
# 3


# ════════════════════════════════════════════════════════════════
# EXAMPLE 19 — str() : convert a value into text
# ════════════════════════════════════════════════════════════════
# WHAT   : str() turns any value into a string (text).
# SYNTAX : str(value)
# PARAMS : value -> any value.
# RETURNS: text (str).
# WHY    : You can only glue text to text with +; numbers must become text first.
# WHEN   : Building a message with + (or just use an f-string instead).
# MISTAKE: "Age: " + 30 errors. Use "Age: " + str(30).

age = 30
print("Age: " + str(age))     # convert 30 -> "30" so + works
# OUTPUT: Age: 30


# ════════════════════════════════════════════════════════════════
# EXAMPLE 20 — float() : convert a value into a decimal number
# ════════════════════════════════════════════════════════════════
# WHAT   : float() turns text or a whole number into a decimal.
# SYNTAX : float(value)
# PARAMS : value -> a number or numeric text like "2.5".
# RETURNS: a decimal number (float).
# WHY    : When you need decimals (prices, measurements, averages).
# WHEN   : Converting text like "2.5" before doing decimal maths.

price = float("2.5")          # convert text "2.5" -> 2.5
print(price + 1)              # -> 3.5
# OUTPUT: 3.5


# ════════════════════════════════════════════════════════════════
# EXAMPLE 21 — bool() : convert a value into True or False
# ════════════════════════════════════════════════════════════════
# WHAT   : bool() turns a value into True/False using "truthiness".
# SYNTAX : bool(value)
# PARAMS : value -> any value.
# RETURNS: True or False.
# RULE   : 0, 0.0, "", [], {}, None are FALSE. Everything else is TRUE.
# WHY    : To check if something is "empty" or "present".
# MISTAKE: bool("False") is TRUE! Any non-empty text counts as True.

print(bool(0))        # 0 is falsy        -> False
print(bool(7))        # any other number  -> True
print(bool(""))       # empty text        -> False
print(bool("False"))  # non-empty text    -> True  (surprising!)
# OUTPUT:
# False
# True
# False
# True


# ════════════════════════════════════════════════════════════════
# EXAMPLE 22 — Arithmetic operators (+  -  *  /)
# ════════════════════════════════════════════════════════════════
# WHAT   : The basic maths symbols.
# SYNTAX : a + b   a - b   a * b   a / b
# WHY    : To do calculations.
# WHEN   : Any maths.
# NOTE   : / ALWAYS gives a decimal (float), even for 8 / 4.

a = 8
b = 5
print(a + b)   # addition       -> 13
print(a - b)   # subtraction    -> 3
print(a * b)   # multiplication -> 40
print(a / b)   # division       -> 1.6  (a float!)
# OUTPUT:
# 13
# 3
# 40
# 1.6


# ════════════════════════════════════════════════════════════════
# EXAMPLE 23 — More operators (//  %  **)
# ════════════════════════════════════════════════════════════════
# WHAT   : Floor division, remainder, and power.
# SYNTAX : a // b   a % b   a ** b
# WHY    : // = whole part of a division; % = the leftover; ** = powers.
# WHEN   : // and % for splitting/grouping; ** for squares, cubes, etc.
# MISTAKE: Don't confuse / (1.6) with // (1) — they are different.

print(17 // 5)   # floor division: how many WHOLE 5s fit in 17 -> 3
print(17 % 5)    # modulo: the remainder left over           -> 2
print(2 ** 3)    # power: 2 to the power of 3                 -> 8
# OUTPUT:
# 3
# 2
# 8


# ════════════════════════════════════════════════════════════════
# EXAMPLE 24 — Augmented assignment (+=  -=  *=)
# ════════════════════════════════════════════════════════════════
# WHAT   : A shortcut to update a variable using its own value.
# SYNTAX : variable += value   (means: variable = variable + value)
# WHY    : Shorter and clearer than repeating the variable name.
# WHEN   : Counters, running totals, scores.

count = 10
count += 1     # same as count = count + 1   -> 11
print(count)
lives = 3
lives -= 1     # same as lives = lives - 1    -> 2
print(lives)
points = 5
points *= 2    # same as points = points * 2  -> 10
print(points)
# OUTPUT:
# 11
# 2
# 10


# ════════════════════════════════════════════════════════════════
# EXAMPLE 25 — len() : count items / characters
# ════════════════════════════════════════════════════════════════
# WHAT   : len() tells you how many items are inside something.
# SYNTAX : len(value)
# PARAMS : value -> text, a list, a dict, a set, etc.
# RETURNS: a whole number (the count).
# WHY    : To measure the size/length of data.
# WHEN   : Checking how long a word is, or how big a list is.

word = "banana"
print(len(word))     # count the 6 characters -> 6
# OUTPUT: 6


# ════════════════════════════════════════════════════════════════
# EXAMPLE 26 — Comparison operators (==  !=  >  <  >=  <=)
# ════════════════════════════════════════════════════════════════
# WHAT   : Comparisons ask a question and answer True or False.
# SYNTAX : a == b   a != b   a > b   a < b   a >= b   a <= b
# WHY    : To compare values and make decisions.
# WHEN   : Any time you ask "is this bigger / equal / different?".
# MISTAKE: ONE = stores a value (x = 5). TWO == compares (x == 5).
#          Mixing them up is the most common beginner error.

print(5 == 5)    # are they EQUAL?            -> True
print(5 != 3)    # are they NOT equal?        -> True
print(5 > 3)     # greater than?              -> True
print(5 < 3)     # less than?                 -> False
print(5 >= 5)    # greater than OR equal?     -> True
# OUTPUT:
# True
# True
# True
# False
# True


# ════════════════════════════════════════════════════════════════
# EXAMPLE 27 — Multiple assignment (several variables at once)
# ════════════════════════════════════════════════════════════════
# WHAT   : Create several variables on ONE line.
# SYNTAX : name1, name2, name3 = value1, value2, value3
# WHY    : Shorter and tidy when values belong together.
# WHEN   : Setting up a few related variables at once.
# MISTAKE: The number of names must equal the number of values.

x, y, z = 1, 2, 3   # x=1, y=2, z=3 — matched left-to-right
print(x, y, z)      # -> 1 2 3
# OUTPUT: 1 2 3


# ════════════════════════════════════════════════════════════════
# EXAMPLE 28 — Giving several variables the SAME value
# ════════════════════════════════════════════════════════════════
# WHAT   : Set many variables to one starting value.
# SYNTAX : a = b = c = value
# WHY    : Quick way to initialise counters/flags to the same start.
# WHEN   : Starting several totals at 0, for example.

a = b = c = 0       # all three start at 0
print(a, b, c)      # -> 0 0 0
# OUTPUT: 0 0 0


# ════════════════════════════════════════════════════════════════
# EXAMPLE 29 — Swapping two variables
# ════════════════════════════════════════════════════════════════
# WHAT   : Make two variables trade their values.
# SYNTAX : a, b = b, a
# WHY    : A clean Python trick — no temporary variable needed.
# WHEN   : Reordering values, sorting by hand, etc.

left = "L"
right = "R"
left, right = right, left   # both values swap in one step
print(left, right)          # -> R L
# OUTPUT: R L


# ════════════════════════════════════════════════════════════════
# EXAMPLE 30 — f-string number formatting (decimals)
# ════════════════════════════════════════════════════════════════
# WHAT   : Control how a number looks inside an f-string.
# SYNTAX : f"{number:.2f}"   ->  2 digits after the decimal point
# WHY    : To show clean, tidy numbers (money, percentages, etc.).
# WHEN   : Displaying numbers to people.

pi = 3.14159
print(f"{pi:.2f}")     # keep 2 decimal places -> 3.14
print(f"{pi:.0f}")     # keep 0 decimal places -> 3
# OUTPUT:
# 3.14
# 3


# ════════════════════════════════════════════════════════════════
# EXAMPLE 31 — Lowercase and UPPERCASE text
# ════════════════════════════════════════════════════════════════
# WHAT   : .lower() and .upper() change a string's letter case.
# SYNTAX : text.lower()   /   text.upper()
# PARAMS : none.
# RETURNS: a NEW string (the original is unchanged — strings can't change).
# WHY    : To standardise text (e.g. compare ignoring case).
# WHEN   : Cleaning user input, comparisons, formatting.

print("HELLO".lower())   # -> hello
print("hello".upper())   # -> HELLO
# OUTPUT:
# hello
# HELLO


# ════════════════════════════════════════════════════════════════
# EXAMPLE 32 — Removing spaces with strip()
# ════════════════════════════════════════════════════════════════
# WHAT   : .strip() removes spaces (and line breaks) from BOTH ends.
# SYNTAX : text.strip()
# PARAMS : none (by default removes whitespace).
# RETURNS: a new, trimmed string.
# WHY    : Stray spaces cause sneaky bugs and ugly output.
# WHEN   : Cleaning text, especially typed/imported input.

messy = "   hi   "
print(messy.strip())     # spaces at both ends removed -> "hi"
print(f"[{messy.strip()}]")   # brackets prove the spaces are gone -> [hi]
# OUTPUT:
# hi
# [hi]


# ════════════════════════════════════════════════════════════════
# EXAMPLE 33 — Picking one character (indexing)
# ════════════════════════════════════════════════════════════════
# WHAT   : Get a single character from text by its position.
# SYNTAX : text[position]
# WHY    : To read a specific character.
# WHEN   : Checking the first/last letter, etc.
# MISTAKE: Counting starts at 0, so the FIRST character is text[0].

word = "python"
print(word[0])    # first character  -> p
print(word[1])    # second character -> y
print(word[-1])   # -1 means the LAST character -> n
# OUTPUT:
# p
# y
# n


# ════════════════════════════════════════════════════════════════
# EXAMPLE 34 — Taking a slice (a piece of text)
# ════════════════════════════════════════════════════════════════
# WHAT   : Get several characters at once.
# SYNTAX : text[start:stop]   (stop is NOT included)
# WHY    : To grab part of a string.
# WHEN   : Extracting prefixes, sections, etc.
# MISTAKE: The 'stop' index is excluded: [0:3] gives positions 0,1,2.

word = "python"
print(word[0:3])   # characters 0,1,2 -> pyt
print(word[2:])    # from 2 to the end -> thon
print(word[:2])    # from start to 2   -> py
# OUTPUT:
# pyt
# thon
# py


# ════════════════════════════════════════════════════════════════
# EXAMPLE 35 — A boolean from a comparison stored in a variable
# ════════════════════════════════════════════════════════════════
# WHAT   : A comparison produces True/False, which you can store.
# SYNTAX : result = a > b
# WHY    : To remember the answer to a question for later use.
# WHEN   : Saving a yes/no result.

temperature = 30
is_hot = temperature > 25   # the comparison gives True; store it in 'is_hot'
print(is_hot)               # -> True
# OUTPUT: True


# ════════════════════════════════════════════════════════════════
# EXAMPLE 36 — Mixing text and numbers in an f-string (no str() needed)
# ════════════════════════════════════════════════════════════════
# WHAT   : f-strings automatically turn numbers into text for you.
# SYNTAX : f"text {number} text"
# WHY    : Cleaner than using + and str() everywhere.
# WHEN   : Almost always when displaying numbers with words.

score = 95
print(f"Your score is {score} points")   # number slots in automatically
# OUTPUT: Your score is 95 points


# ════════════════════════════════════════════════════════════════
# EXAMPLE 37 — Constants (values that should not change)
# ════════════════════════════════════════════════════════════════
# WHAT   : Python has no "locked" values, but the CONVENTION is to write
#          fixed values in ALL_CAPITALS to mean "don't change me".
# SYNTAX : MAX_SPEED = 120
# WHY    : Signals to other people that this value is meant to stay fixed.
# WHEN   : For settings, limits, and fixed numbers like PI.

PI = 3.14159        # a constant (ALL_CAPS by convention)
MAX_USERS = 100     # another constant
print(PI, MAX_USERS)
# OUTPUT: 3.14159 100


# ════════════════════════════════════════════════════════════════
# EXAMPLE 38 — Using a constant in a calculation
# ════════════════════════════════════════════════════════════════
# WHAT   : Constants are used just like any other variable.
# WHY    : Define a value once, reuse it everywhere (easy to update).
# WHEN   : Repeated fixed values (tax rate, PI, limits).

PI = 3.14159
radius = 5
area = PI * radius * radius   # area of a circle = PI x r x r
print(area)                   # -> 78.53975
# OUTPUT: 78.53975


# ════════════════════════════════════════════════════════════════
# EXAMPLE 39 — Negative numbers and order of operations
# ════════════════════════════════════════════════════════════════
# WHAT   : Python follows normal maths order: ( ) first, then * and /,
#          then + and - (just like school).
# SYNTAX : use ( ) to force the order you want.
# WHY    : So calculations come out the way you intend.
# WHEN   : Any multi-step calculation.

result1 = 2 + 3 * 4      # * happens before + -> 2 + 12 = 14
result2 = (2 + 3) * 4    # ( ) forces + first -> 5 * 4 = 20
print(result1, result2)  # -> 14 20
# OUTPUT: 14 20


# ════════════════════════════════════════════════════════════════
# EXAMPLE 40 — Booleans behave like numbers (True is 1, False is 0)
# ════════════════════════════════════════════════════════════════
# WHAT   : In Python, True equals 1 and False equals 0.
# WHY    : Sometimes handy (e.g. counting True values by adding them).
# WHEN   : Rarely needed early on, but good to know so it doesn't confuse you.

print(True + True)    # 1 + 1 -> 2
print(False + 5)      # 0 + 5 -> 5
# OUTPUT:
# 2
# 5


# ════════════════════════════════════════════════════════════════
# EXAMPLE 41 — Checking if text contains something ('in')
# ════════════════════════════════════════════════════════════════
# WHAT   : The 'in' keyword checks if one thing is inside another.
# SYNTAX : small in big   ->  True or False
# WHY    : To search for a character/word inside text.
# WHEN   : Simple "does it contain?" checks.

sentence = "I love python"
print("python" in sentence)   # is "python" inside? -> True
print("java" in sentence)     # is "java" inside?   -> False
# OUTPUT:
# True
# False


# ════════════════════════════════════════════════════════════════
# EXAMPLE 42 — Combining text variables and f-strings
# ════════════════════════════════════════════════════════════════
# WHAT   : Put several variables into one sentence.
# WHY    : To produce a readable, complete message.
# WHEN   : Building output lines, reports, greetings.

first = "Maya"
city = "Lisbon"
age = 24
print(f"{first} is {age} and lives in {city}")
# OUTPUT: Maya is 24 and lives in Lisbon


# ════════════════════════════════════════════════════════════════
# EXAMPLE 43 — round() : round a number
# ════════════════════════════════════════════════════════════════
# WHAT   : round() rounds a number to a chosen number of decimals.
# SYNTAX : round(number, decimals)
# PARAMS : number -> the value; decimals -> how many places (optional).
# RETURNS: the rounded number.
# WHY    : To tidy up long decimals for display.
# WHEN   : Showing prices, averages, measurements.

print(round(3.14159, 2))   # keep 2 decimals -> 3.14
print(round(2.7))          # no decimals -> nearest whole number -> 3
# OUTPUT:
# 3.14
# 3


# ════════════════════════════════════════════════════════════════
# EXAMPLE 44 — abs() : the size of a number (no minus sign)
# ════════════════════════════════════════════════════════════════
# WHAT   : abs() gives a number's distance from zero (drops the sign).
# SYNTAX : abs(number)
# PARAMS : number -> any number.
# RETURNS: the number without a minus sign.
# WHY    : When you care about size, not direction.
# WHEN   : Differences, distances.

print(abs(-8))    # -> 8
print(abs(8))     # -> 8 (already positive)
# OUTPUT:
# 8
# 8


# ════════════════════════════════════════════════════════════════
# EXAMPLE 45 — Converting between types in one calculation
# ════════════════════════════════════════════════════════════════
# WHAT   : Real programs often convert text to numbers, calculate, then
#          convert back to text for display.
# WHY    : Data arrives as text but maths needs numbers.
# WHEN   : Whenever you read values as text (input, files).

quantity_text = "3"            # text
price_text = "2.50"            # text
quantity = int(quantity_text)  # text -> whole number
price = float(price_text)      # text -> decimal number
total = quantity * price       # do the maths -> 7.5
print("Total: $" + str(total)) # number -> text to glue with +
# OUTPUT: Total: $7.5


# ════════════════════════════════════════════════════════════════
# EXAMPLE 46 — A variable can change TYPE when reassigned
# ════════════════════════════════════════════════════════════════
# WHAT   : A variable isn't locked to one type; reassigning can change it.
# WHY    : Python is flexible — the type follows the current value.
# WHEN   : Good to understand; avoid doing it confusingly in real code.

thing = 10           # right now 'thing' is an int
print(type(thing).__name__)   # -> int
thing = "now text"   # reassigned to a string; type changes
print(type(thing).__name__)   # -> str
# OUTPUT:
# int
# str


# ════════════════════════════════════════════════════════════════
# EXAMPLE 47 — Booleans from combining conditions (and / or / not)
# ════════════════════════════════════════════════════════════════
# WHAT   : Combine True/False values with and, or, not.
# SYNTAX : a and b   |   a or b   |   not a
# WHY    : To check more than one condition at once.
# WHEN   : "Is it both X AND Y?", "Is it X OR Y?".
# RULES  : and -> True only if BOTH are True.
#          or  -> True if AT LEAST one is True.
#          not -> flips True<->False.

age = 20
has_ticket = True
print(age >= 18 and has_ticket)   # both True? -> True
print(age < 13 or has_ticket)     # at least one True? -> True
print(not has_ticket)             # flip it -> False
# OUTPUT:
# True
# True
# False


# ════════════════════════════════════════════════════════════════
# EXAMPLE 48 — Chained comparison (is a value in a range?)
# ════════════════════════════════════════════════════════════════
# WHAT   : Python lets you chain comparisons naturally.
# SYNTAX : low < value < high
# WHY    : Reads like maths: "is value between low and high?".
# WHEN   : Range checks.

n = 5
print(1 < n < 10)    # is n between 1 and 10? -> True
print(1 < 20 < 10)   # 20 is not < 10         -> False
# OUTPUT:
# True
# False


# ════════════════════════════════════════════════════════════════
# EXAMPLE 49 — A tiny, complete mini-summary using variables
# ════════════════════════════════════════════════════════════════
# WHAT   : Bring several basics together into one useful result.
# WHY    : This is what real code looks like — variables working together.
# WHEN   : Always! Programs are many small steps combined.

name = "Alex"
age = 28
favorite = "blue"
summary = f"{name} is {age} years old and likes {favorite}"
print(summary)
# OUTPUT: Alex is 28 years old and likes blue


# ════════════════════════════════════════════════════════════════
# EXAMPLE 50 — Putting numbers and text together cleanly
# ════════════════════════════════════════════════════════════════
# WHAT   : A final example mixing maths, formatting, and text.
# WHY    : Shows how the pieces fit into one readable output line.
# WHEN   : Producing a final report/answer.

price = 19.99
quantity = 3
total = price * quantity                 # maths -> 59.97
print(f"{quantity} items x ${price} = ${total:.2f}")   # formatted to 2 decimals
# OUTPUT: 3 items x $19.99 = $59.97


print("\nLevel 1 complete! You learned 50 BASIC variable concepts,")
print("with every line explained. Next: variables_2_intermediate.py")