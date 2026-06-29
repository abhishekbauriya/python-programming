"""
=====================================================================
 51 MINI PROJECTS — MASTER FILE  (all 8 groups in one file)
=====================================================================
Every beginner mini-project for Python VARIABLES, combined into ONE
runnable file. No functions (def) are used anywhere.

Each project explains:
  OBJECTIVE / DESCRIPTION / CONCEPTS / WHAT / WHY / WHEN / HOW /
  SYNTAX / PARAMETERS  -- plus a comment on every line, the OUTPUT,
  and a "TRY THIS" tweak.

GROUPS (51 projects total):
  A Basics ............. projects 1-5
  B Numbers & Math ..... projects 6-12
  C Strings ............ projects 13-19
  D Booleans & Logic ... projects 20-25
  E Lists .............. projects 26-32
  F Dictionaries ....... projects 33-38
  G Tuples & Sets ...... projects 39-44
  H Mixed Capstones .... projects 45-51

HOW TO RUN:
  python variables_mini_projects_all.py
=====================================================================
"""

print("=" * 60)
print("  51 MINI PROJECTS — running all groups A through H")
print("=" * 60)


print("GROUP A — BASICS\n")


# ──────────────────────────────────────────────────────────────
# PROJECT 1 — Personal Greeting                          ⭐ basic
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Greet a person by name and age.
# DESCRIPTION : Stores a name and age in variables and prints a friendly
#               message built with an f-string.
# CONCEPTS    : variables, strings, integers, f-strings, print()
# WHAT  : An f-string drops variables straight into text.
# WHY   : Cleaner than gluing pieces together with + and str().
# WHEN  : Whenever you build a message from variables.
# HOW   : Put 'f' before the quotes and {variable} where you want a value.
# SYNTAX: f"text {variable} text"
print("PROJECT 1 — Personal Greeting")
name = "Alex"                              # the person's name (text / str)
age = 25                                   # the person's age (whole number / int)
print(f"Hi {name}, you are {age} years old!")   # build + show the greeting
# OUTPUT: Hi Alex, you are 25 years old!
# TRY THIS: change name and age, or add their city to the sentence.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 2 — Age Next Year                              ⭐ basic
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Work out how old someone will be next year.
# DESCRIPTION : Takes an age, adds 1, and shows the result.
# CONCEPTS    : variables, integers, arithmetic (+), f-strings
# WHAT  : Using a variable in a calculation.
# WHY   : To make new values from existing ones.
# WHEN  : Any time a result depends on a stored value.
# HOW   : The right side is calculated first, then stored on the left.
print("PROJECT 2 — Age Next Year")
age = 25                                   # current age
next_year = age + 1                        # 25 + 1 = 26 is worked out, then stored
print(f"Next year you will be {next_year}")
# OUTPUT: Next year you will be 26
# TRY THIS: print how old they'll be in 10 years (age + 10).
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 3 — Rectangle Area & Perimeter                 ⭐ basic
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Calculate the area and perimeter of a rectangle.
# DESCRIPTION : Uses width and height to compute two results.
# CONCEPTS    : variables, arithmetic (* and +), f-strings
# WHAT  : Multiplication (*) and addition (+) on number variables.
# WHY   : Geometry/measurement formulas use them constantly.
# WHEN  : Any size/area calculation.
# HOW   : area = width × height ; perimeter = 2 × (width + height).
print("PROJECT 3 — Rectangle Area & Perimeter")
width = 5                                  # the rectangle's width
height = 3                                 # the rectangle's height
area = width * height                      # 5 * 3 = 15
perimeter = 2 * (width + height)           # 2 * (5 + 3) = 16  (brackets first!)
print(f"Area = {area}, Perimeter = {perimeter}")
# OUTPUT: Area = 15, Perimeter = 16
# TRY THIS: change width/height; what happens if both are 4 (a square)?
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 4 — Swap Two Values                            ⭐ basic
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Make two variables trade their values.
# DESCRIPTION : Swaps two drinks between two cups using Python's
#               one-line swap trick.
# CONCEPTS    : variables, multiple assignment, swapping
# WHAT  : Swapping with  a, b = b, a
# WHY   : Reorders values with no temporary variable needed.
# WHEN  : Sorting by hand, rearranging data.
# HOW   : The right side is built first, then unpacked into the left.
print("PROJECT 4 — Swap Two Values")
cup1 = "tea"                               # what's in cup 1
cup2 = "coffee"                            # what's in cup 2
print(f"Before: cup1={cup1}, cup2={cup2}")
cup1, cup2 = cup2, cup1                    # swap the two values in one line
print(f"After : cup1={cup1}, cup2={cup2}")
# OUTPUT:
# Before: cup1=tea, cup2=coffee
# After : cup1=coffee, cup2=tea
# TRY THIS: swap three variables in a cycle: a, b, c = c, a, b
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 5 — Simple Total                               ⭐ basic
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Add up three prices and show the total.
# DESCRIPTION : Stores three prices and adds them together.
# CONCEPTS    : variables, floats, arithmetic (+), number formatting
# WHAT  : f"{value:.2f}" shows a number with 2 decimal places.
# WHY   : Money should always show two decimals (e.g. 7.50, not 7.5).
# WHEN  : Displaying prices/money.
# HOW   : Put :.2f after the variable inside the { } of an f-string.
# SYNTAX: f"{number:.2f}"
print("PROJECT 5 — Simple Total")
item1 = 2.50                               # price of item 1
item2 = 3.00                               # price of item 2
item3 = 1.25                               # price of item 3
total = item1 + item2 + item3              # add all three prices
print(f"Total: ${total:.2f}")             # show with 2 decimal places
# OUTPUT: Total: $6.75
# TRY THIS: add a fourth item and include it in the total.
print()

print("Group A complete — 5 basic projects done!")


print("GROUP B — NUMBERS & MATH\n")


# ──────────────────────────────────────────────────────────────
# PROJECT 6 — Tip Calculator                             ⭐ basic
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Work out a tip and the new total.
# DESCRIPTION : Takes a bill and a tip percentage, returns tip + total.
# CONCEPTS    : floats, percentages, arithmetic, number formatting
# WHAT  : Percentage maths:  part = whole * percent / 100.
# WHY   : Percentages appear everywhere (tips, tax, discounts).
# WHEN  : Any "X% of a number" calculation.
# HOW   : Multiply by the percent, then divide by 100.
print("PROJECT 6 — Tip Calculator")
bill = 50.00                               # the bill amount
tip_percent = 15                           # tip as a percentage
tip = bill * tip_percent / 100             # 50 * 15 / 100 = 7.5
total = bill + tip                         # bill plus tip
print(f"Tip: ${tip:.2f}, Total: ${total:.2f}")
# OUTPUT: Tip: $7.50, Total: $57.50
# TRY THIS: change the tip to 20 percent.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 7 — BMI Calculator                            ⭐⭐ easy
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Calculate Body Mass Index.
# DESCRIPTION : Uses weight and height in a formula.
# CONCEPTS    : floats, arithmetic, brackets, rounding in f-strings
# WHAT  : Order of operations — brackets ( ) are calculated first.
# WHY   : Without brackets the maths would be wrong.
# WHEN  : Any multi-step formula.
# HOW   : weight / (height * height).
print("PROJECT 7 — BMI Calculator")
weight_kg = 68                             # weight in kilograms
height_m = 1.70                            # height in metres
bmi = weight_kg / (height_m * height_m)    # divide weight by height-squared
print(f"BMI = {bmi:.1f}")                  # one decimal place is enough
# OUTPUT: BMI = 23.5
# TRY THIS: change the weight and see how the BMI moves.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 8 — Simple Interest                           ⭐⭐ easy
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Work out interest earned and the final total.
# DESCRIPTION : Uses principal, rate, and years.
# CONCEPTS    : variables, arithmetic, percentages
# WHAT  : A formula combining several variables.
# WHY   : Shows how variables feed into one result.
# WHEN  : Finance / growth calculations.
# HOW   : interest = principal * rate * years / 100.
print("PROJECT 8 — Simple Interest")
principal = 1000                           # starting money
rate = 5                                   # yearly interest rate (%)
years = 2                                  # number of years
interest = principal * rate * years / 100  # 1000 * 5 * 2 / 100 = 100
total = principal + interest               # money you end up with
print(f"Interest: {interest}, Total: {total}")
# OUTPUT: Interest: 100.0, Total: 1100.0
# TRY THIS: change years to 5.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 9 — Temperature Converter                     ⭐⭐ easy
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Convert Celsius to Fahrenheit and Kelvin.
# DESCRIPTION : One input, two converted outputs.
# CONCEPTS    : floats, arithmetic, order of operations
# WHAT  : * and / happen before + (normal maths order).
# WHY   : So the conversion formula gives the right answer.
# WHEN  : Unit conversions.
# HOW   : F = C * 9/5 + 32 ; K = C + 273.15.
print("PROJECT 9 — Temperature Converter")
celsius = 30                               # temperature in Celsius
fahrenheit = celsius * 9 / 5 + 32          # convert to Fahrenheit
kelvin = celsius + 273.15                  # convert to Kelvin
print(f"{celsius}C = {fahrenheit}F = {kelvin}K")
# OUTPUT: 30C = 86.0F = 303.15K
# TRY THIS: convert 0 and 100 degrees Celsius.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 10 — Discount Price                           ⭐⭐ easy
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Apply a discount and show the sale price.
# DESCRIPTION : Reduces a price by a percentage.
# CONCEPTS    : floats, percentages, subtraction
# WHAT  : Subtracting a percentage of a value from that value.
# WHY   : Sales and discounts are everyday maths.
# WHEN  : Pricing, offers.
# HOW   : saving = price * discount / 100 ; sale = price - saving.
print("PROJECT 10 — Discount Price")
price = 80.00                              # original price
discount_percent = 25                      # discount as a percentage
saving = price * discount_percent / 100    # 80 * 25 / 100 = 20
sale_price = price - saving                # 80 - 20 = 60
print(f"You save ${saving:.2f}. Pay ${sale_price:.2f}")
# OUTPUT: You save $20.00. Pay $60.00
# TRY THIS: change the discount to 10 percent.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 11 — Average of Three Numbers                 ⭐⭐ easy
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Find the average of three test scores.
# DESCRIPTION : Adds three numbers and divides by how many there are.
# CONCEPTS    : arithmetic, brackets, division
# WHAT  : average = (sum of values) / (count of values).
# WHY   : Averages summarise data in one number.
# WHEN  : Scores, prices, measurements.
# HOW   : Wrap the addition in brackets so it happens before dividing.
print("PROJECT 11 — Average of Three Numbers")
score1 = 80                                # first score
score2 = 95                                # second score
score3 = 70                                # third score
average = (score1 + score2 + score3) / 3   # brackets add first, then divide
print(f"Average score: {average:.1f}")
# OUTPUT: Average score: 81.7
# TRY THIS: add a fourth score and divide by 4.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 12 — Percentage Calculator                    ⭐⭐ easy
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Work out what percent you scored on a test.
# DESCRIPTION : Turns "marks out of total" into a percentage.
# CONCEPTS    : division, percentages, number formatting
# WHAT  : percentage = part / whole * 100.
# WHY   : Converts a fraction into an easy-to-read percent.
# WHEN  : Grades, progress bars, stats.
# HOW   : Divide your marks by the total, then multiply by 100.
print("PROJECT 12 — Percentage Calculator")
marks = 42                                 # marks you got
total_marks = 50                           # total possible marks
percent = marks / total_marks * 100        # 42 / 50 * 100 = 84.0
print(f"You scored {percent:.0f}%")        # :.0f shows no decimals
# OUTPUT: You scored 84%
# TRY THIS: change marks to 50 (a perfect score).
print()

print("Group B complete — 7 number projects done!")


print("GROUP C — STRINGS\n")


# ──────────────────────────────────────────────────────────────
# PROJECT 13 — Initials Maker                            ⭐ basic
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Turn a first and last name into initials (e.g. "A.B.").
# DESCRIPTION : Takes the first letter of each name.
# CONCEPTS    : strings, indexing [0], .upper(), f-strings
# WHAT  : text[0] gets the first character (positions start at 0).
# WHY   : To read a specific character.
# WHEN  : Initials, first letters, codes.
# HOW   : Take [0] of each name, uppercase it, and join with dots.
# SYNTAX: text[0]   and   text.upper()
print("PROJECT 13 — Initials Maker")
first = "ada"                              # first name
last = "lovelace"                          # last name
initials = first[0].upper() + "." + last[0].upper() + "."   # 'A' + '.' + 'L' + '.'
print(f"Initials: {initials}")
# OUTPUT: Initials: A.L.
# TRY THIS: add a middle name and include its initial.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 14 — Username Generator                       ⭐⭐ easy
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Build a username from a name and a number.
# DESCRIPTION : Lowercases the name and sticks a number on the end.
# CONCEPTS    : strings, .lower(), str(), concatenation
# WHAT  : .lower() makes text lowercase; str() turns a number into text.
# WHY   : Usernames are usually lowercase; you can't + a number onto text.
# WHEN  : Making IDs, handles, slugs.
# HOW   : name.lower() + str(number).
# SYNTAX: text.lower()   and   str(value)
print("PROJECT 14 — Username Generator")
name = "Alex"                              # the person's name
lucky_number = 7                           # a number to append
username = name.lower() + str(lucky_number)  # "alex" + "7" -> "alex7"
print(f"Username: {username}")
# OUTPUT: Username: alex7
# TRY THIS: add the first 3 letters of a city: + city[:3].lower()
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 15 — Character Counter                        ⭐⭐ easy
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Count the characters in a piece of text.
# DESCRIPTION : Uses len() to measure a string's length.
# CONCEPTS    : strings, len()
# WHAT  : len(text) counts how many characters are in the text.
# WHY   : To measure length (limits, validation, stats).
# WHEN  : Password length, tweet length, etc.
# HOW   : Pass the string to len().
# SYNTAX: len(value)   ->   returns a whole number
print("PROJECT 15 — Character Counter")
message = "hello world"                    # the text to measure
length = len(message)                      # counts ALL characters incl. the space
print(f'"{message}" has {length} characters')
# OUTPUT: "hello world" has 11 characters
# TRY THIS: count a message with no spaces, then with spaces.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 16 — Word Counter                             ⭐⭐ easy
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Count how many words are in a sentence.
# DESCRIPTION : Splits the sentence on spaces, then counts the pieces.
# CONCEPTS    : strings, .split(), len()
# WHAT  : .split() breaks text into a LIST of words; len() counts them.
# WHY   : Words are separated by spaces, so splitting gives a word list.
# WHEN  : Word counts, text stats.
# HOW   : sentence.split() then len() of the result.
# SYNTAX: text.split()   ->   returns a list of pieces
print("PROJECT 16 — Word Counter")
sentence = "learn python step by step"     # the sentence to count
words = sentence.split()                   # -> ['learn','python','step','by','step']
word_count = len(words)                     # count the items in the list
print(f"Word count: {word_count}")
# OUTPUT: Word count: 5
# TRY THIS: print the list 'words' to see the split pieces.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 17 — Reverse Text                             ⭐⭐ easy
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Reverse a word (useful for palindrome checks).
# DESCRIPTION : Uses slicing with a step of -1 to flip the text.
# CONCEPTS    : strings, slicing [::-1]
# WHAT  : text[::-1] returns the text backwards.
# WHY   : A quick, no-tools way to reverse a string.
# WHEN  : Palindromes, puzzles, formatting.
# HOW   : Use a slice with step -1.
# SYNTAX: text[::-1]
print("PROJECT 17 — Reverse Text")
word = "python"                            # the word to reverse
reversed_word = word[::-1]                 # step -1 walks the text backwards
print(f"{word} reversed is {reversed_word}")
# OUTPUT: python reversed is nohtyp
# TRY THIS: check if "level" reversed equals "level" (a palindrome!).
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 18 — Vowel Counter                            ⭐⭐ easy
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Count the vowels in a word.
# DESCRIPTION : Counts each vowel and adds the counts together.
# CONCEPTS    : strings, .count(), arithmetic
# WHAT  : text.count("a") counts how many times "a" appears.
# WHY   : To measure specific characters.
# WHEN  : Text analysis, puzzles.
# HOW   : Add up the counts of a, e, i, o, u.
# SYNTAX: text.count(substring)   ->   a whole number
print("PROJECT 18 — Vowel Counter")
word = "education"                          # the word to analyse
vowels = (word.count("a") + word.count("e") + word.count("i")
          + word.count("o") + word.count("u"))   # add each vowel's count
print(f'"{word}" has {vowels} vowels')
# OUTPUT: "education" has 5 vowels
# TRY THIS: count vowels in your own name (lowercase it first with .lower()).
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 19 — Mad Libs Story                           ⭐⭐ easy
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Fill a story template with fun words.
# DESCRIPTION : Drops several word-variables into one sentence.
# CONCEPTS    : strings, f-strings, multiple variables
# WHAT  : One f-string can insert MANY variables at once.
# WHY   : To build longer text from several pieces.
# WHEN  : Templates, messages, reports.
# HOW   : Put each {variable} where you want it in the text.
print("PROJECT 19 — Mad Libs Story")
adjective = "tiny"                          # a describing word
animal = "dragon"                           # an animal
action = "sneezed"                          # a past-tense action
story = f"A {adjective} {animal} {action} and the whole town laughed."
print(story)
# OUTPUT: A tiny dragon sneezed and the whole town laughed.
# TRY THIS: change the three words to make your own silly story.
print()

print("Group C complete — 7 string projects done!")


print("GROUP D — BOOLEANS & LOGIC\n")


# ──────────────────────────────────────────────────────────────
# PROJECT 20 — Even or Odd                              ⭐⭐ easy
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Decide whether a number is even or odd.
# DESCRIPTION : Uses the remainder operator to test divisibility by 2.
# CONCEPTS    : modulo (%), comparison (==), conditional expression
# WHAT  : n % 2 gives the remainder when dividing by 2 (0 = even).
# WHY   : The remainder tells you if a number divides evenly.
# WHEN  : Grouping, alternating, divisibility checks.
# HOW   : (n % 2 == 0) is True for even numbers.
# SYNTAX: value_if_true if condition else value_if_false
print("PROJECT 20 — Even or Odd")
number = 7                                 # the number to test
is_even = (number % 2 == 0)                # remainder 0 -> even -> True/False
label = "even" if is_even else "odd"       # pick a word based on the boolean
print(f"{number} is {label}")
# OUTPUT: 7 is odd
# TRY THIS: change number to 10.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 21 — Leap Year Check                          ⭐⭐⭐ tricky
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Decide whether a year is a leap year.
# DESCRIPTION : Applies the real leap-year rule using logic operators.
# CONCEPTS    : modulo (%), and/or, brackets, booleans
# WHAT  : Combine conditions with 'and' / 'or'.
# WHY   : The rule has multiple parts that must combine correctly.
# WHEN  : Date logic, rules with several conditions.
# HOW   : Leap if divisible by 4 AND (not by 100, OR by 400).
print("PROJECT 21 — Leap Year Check")
year = 2024                                # the year to test
is_leap = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
print(f"{year} leap year? {is_leap}")
# OUTPUT: 2024 leap year? True
# TRY THIS: test 1900 (False) and 2000 (True) — they show why the rule is tricky.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 22 — Voting Eligibility                       ⭐⭐ easy
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Decide if a person can vote (age 18+ AND a citizen).
# DESCRIPTION : Combines two conditions with 'and'.
# CONCEPTS    : comparison (>=), boolean variable, and
# WHAT  : 'and' is True only when BOTH sides are True.
# WHY   : Eligibility often needs several conditions met together.
# WHEN  : Access checks, rules.
# HOW   : (age >= 18) and is_citizen.
print("PROJECT 22 — Voting Eligibility")
age = 20                                   # the person's age
is_citizen = True                          # are they a citizen?
can_vote = (age >= 18) and is_citizen      # both must be True
print(f"Can vote? {can_vote}")
# OUTPUT: Can vote? True
# TRY THIS: set age to 16, or is_citizen to False.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 23 — Password Length Check                    ⭐⭐ easy
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Check if a password is long enough.
# DESCRIPTION : Compares the password length to a minimum.
# CONCEPTS    : len(), comparison (>=), conditional expression
# WHAT  : len(password) >= 8 gives True if it's 8+ characters.
# WHY   : A simple validation rule.
# WHEN  : Form validation, security checks.
# HOW   : Compare len(password) to the minimum length.
print("PROJECT 23 — Password Length Check")
password = "secret12"                      # the password to check
min_length = 8                             # the required minimum length
strong_enough = len(password) >= min_length  # True if long enough
result = "OK" if strong_enough else "too short"
print(f"Password length {len(password)} -> {result}")
# OUTPUT: Password length 8 -> OK
# TRY THIS: change the password to "abc".
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 24 — Grade to Letter                          ⭐⭐⭐ tricky
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Convert a score into a letter grade.
# DESCRIPTION : Picks A/B/C/F using a chained conditional expression.
# CONCEPTS    : comparisons, chained conditional expression
# WHAT  : x if c1 else y if c2 else z  (a one-line if/elif/else).
# WHY   : Maps a number into named categories.
# WHEN  : Grading, banding, tiers.
# HOW   : Check highest threshold first, then work downwards.
print("PROJECT 24 — Grade to Letter")
score = 76                                 # the test score
grade = ("A" if score >= 90 else          # 90+ -> A
         "B" if score >= 80 else          # 80-89 -> B
         "C" if score >= 70 else          # 70-79 -> C
         "F")                             # below 70 -> F
print(f"Score {score} -> Grade {grade}")
# OUTPUT: Score 76 -> Grade C
# TRY THIS: change score to 95, 85, 60.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 25 — Bigger of Two Numbers                    ⭐⭐ easy
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Find the larger of two numbers (two ways).
# DESCRIPTION : Uses both a conditional expression and the max() function.
# CONCEPTS    : comparison (>), conditional expression, max()
# WHAT  : max(a, b) returns the bigger value directly.
# WHY   : Two ways to do the same thing — pick the clearest.
# WHEN  : Comparisons, picking extremes.
# HOW   : a if a > b else b   OR   max(a, b).
# SYNTAX: max(value1, value2)   ->   the largest value
print("PROJECT 25 — Bigger of Two Numbers")
a = 14                                     # first number
b = 9                                      # second number
bigger = a if a > b else b                 # pick the larger with logic
print(f"Bigger (logic): {bigger}")
print(f"Bigger (max):   {max(a, b)}")      # the built-in shortcut
# OUTPUT:
# Bigger (logic): 14
# Bigger (max):   14
# TRY THIS: swap the values so b is larger.
print()

print("Group D complete — 6 boolean/logic projects done!")


print("GROUP E — LISTS\n")


# ──────────────────────────────────────────────────────────────
# PROJECT 26 — Scores Summary (min, max, average)       ⭐⭐ easy
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Summarise a list of scores.
# DESCRIPTION : Finds the lowest, highest, and average score.
# CONCEPTS    : lists, min(), max(), sum(), len()
# WHAT  : min/max/sum/len each take the whole list and return one result.
# WHY   : Quick statistics without writing loops.
# WHEN  : Any time you summarise a list of numbers.
# HOW   : average = sum(list) / len(list).
# SYNTAX: min(list) / max(list) / sum(list) / len(list)
print("PROJECT 26 — Scores Summary")
scores = [70, 85, 90, 65, 95]              # a list of numbers
lowest = min(scores)                       # smallest value
highest = max(scores)                      # largest value
average = sum(scores) / len(scores)        # total divided by how many
print(f"Low={lowest}, High={highest}, Avg={average:.1f}")
# OUTPUT: Low=65, High=95, Avg=81.0
# TRY THIS: add another score to the list and re-run.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 27 — To-Do List Manager                       ⭐⭐ easy
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Add and complete tasks in a list.
# DESCRIPTION : Adds a task with append(), finishes one with remove().
# CONCEPTS    : lists, .append(), .remove(), len()
# WHAT  : .append(x) adds to the end; .remove(x) deletes by value.
# WHY   : Lists are changeable, so they're perfect for to-do items.
# WHEN  : Any growing/shrinking collection.
# HOW   : append to add, remove to delete.
# SYNTAX: list.append(item)   /   list.remove(item)
print("PROJECT 27 — To-Do List Manager")
todo = ["wash dishes", "buy milk"]         # starting tasks
todo.append("call mom")                    # add a new task to the end
todo.remove("buy milk")                    # mark "buy milk" as done (remove it)
print(f"Tasks left ({len(todo)}): {todo}")
# OUTPUT: Tasks left (2): ['wash dishes', 'call mom']
# TRY THIS: append two more tasks, then remove one.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 28 — Shopping Cart Total                      ⭐⭐ easy
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Add up the prices in a cart.
# DESCRIPTION : Sums a list of prices and counts the items.
# CONCEPTS    : lists, sum(), len(), number formatting
# WHAT  : sum() adds all numbers in a list.
# WHY   : Totals are the most common list operation.
# WHEN  : Carts, bills, any running total.
# HOW   : total = sum(prices).
print("PROJECT 28 — Shopping Cart Total")
prices = [4.99, 1.50, 3.25, 0.99]          # prices of items in the cart
total = sum(prices)                        # add them all up
item_count = len(prices)                   # how many items
print(f"{item_count} items, total ${total:.2f}")
# OUTPUT: 4 items, total $10.73
# TRY THIS: add an expensive item and watch the total change.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 29 — Remove Duplicates                        ⭐⭐ easy
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Get the unique values from a list.
# DESCRIPTION : Converts the list to a set (drops repeats), then back.
# CONCEPTS    : lists, set(), sorted()
# WHAT  : set() keeps only unique items; sorted() orders them.
# WHY   : Sets automatically remove duplicates.
# WHEN  : Cleaning messy data with repeats.
# HOW   : sorted(set(my_list)).
# SYNTAX: set(iterable)   /   sorted(iterable)
print("PROJECT 29 — Remove Duplicates")
votes = ["red", "blue", "red", "green", "blue", "red"]
unique = sorted(set(votes))                # unique colours, alphabetical
print(f"Unique choices: {unique}")
# OUTPUT: Unique choices: ['blue', 'green', 'red']
# TRY THIS: count how many unique choices there are with len(set(votes)).
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 30 — Top 3 Scores                             ⭐⭐⭐ tricky
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Find the three highest scores.
# DESCRIPTION : Sorts the scores high-to-low and slices the first three.
# CONCEPTS    : lists, sorted(reverse=True), slicing [:3]
# WHAT  : sorted(list, reverse=True) orders biggest-first; [:3] takes 3.
# WHY   : Ranking and "top N" are everyday tasks.
# WHEN  : Leaderboards, highlights.
# HOW   : Sort descending, then slice the first N.
# SYNTAX: sorted(list, reverse=True)   /   list[:3]
print("PROJECT 30 — Top 3 Scores")
scores = [55, 91, 72, 88, 64, 99]          # all scores
ranked = sorted(scores, reverse=True)      # biggest first
top3 = ranked[:3]                          # take the first three
print(f"Top 3: {top3}")
# OUTPUT: Top 3: [99, 91, 88]
# TRY THIS: get the BOTTOM 3 with sorted(scores)[:3].
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 31 — Second Largest Number                    ⭐⭐⭐ tricky
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Find the second biggest unique number.
# DESCRIPTION : Removes duplicates, sorts, then picks the 2nd from the end.
# CONCEPTS    : set(), sorted(), negative indexing [-2]
# WHAT  : [-2] is the second-to-last item.
# WHY   : "Second highest" is a classic interview-style task.
# WHEN  : Rankings where you skip the top one.
# HOW   : sorted(set(list))[-2].
print("PROJECT 31 — Second Largest Number")
nums = [10, 50, 50, 30, 40]                # note the duplicate 50
unique_sorted = sorted(set(nums))          # unique + ascending -> [10,30,40,50]
second_largest = unique_sorted[-2]         # second from the end -> 40
print(f"Second largest: {second_largest}")
# OUTPUT: Second largest: 40
# TRY THIS: get the largest with [-1] and the smallest with [0].
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 32 — Squares List (comprehension)             ⭐⭐⭐ tricky
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Build a list of squares of 1..5.
# DESCRIPTION : Uses a list comprehension to transform numbers.
# CONCEPTS    : lists, comprehension, range()
# WHAT  : [x*x for x in range(1,6)] builds a list by transforming each item.
# WHY   : A compact, readable way to make a new list.
# WHEN  : Transforming one list into another.
# HOW   : [expression for item in iterable].
# SYNTAX: [expr for item in iterable]
print("PROJECT 32 — Squares List")
squares = [x * x for x in range(1, 6)]     # 1,4,9,16,25
print(f"Squares 1-5: {squares}")
# OUTPUT: Squares 1-5: [1, 4, 9, 16, 25]
# TRY THIS: build a list of even numbers: [n for n in range(10) if n % 2 == 0]
print()

print("Group E complete — 7 list projects done!")


print("GROUP F — DICTIONARIES\n")


# ──────────────────────────────────────────────────────────────
# PROJECT 33 — Profile Card                             ⭐⭐ easy
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Store and display a person's details.
# DESCRIPTION : Keeps labelled values in a dictionary and prints them.
# CONCEPTS    : dicts, key access [ ], f-strings
# WHAT  : A dict stores values under named keys; my_dict["key"] reads one.
# WHY   : Labels are clearer than remembering positions (like in a list).
# WHEN  : Records with named fields (a person, a product, etc.).
# HOW   : Create with { "key": value }, read with [ "key" ].
# SYNTAX: my_dict["key"]
print("PROJECT 33 — Profile Card")
person = {"name": "Maya", "age": 24, "city": "Lisbon"}   # 3 labelled fields
print(f"Name: {person['name']}")           # read the 'name' value
print(f"Age : {person['age']}")            # read the 'age' value
print(f"City: {person['city']}")           # read the 'city' value
# OUTPUT:
# Name: Maya
# Age : 24
# City: Lisbon
# TRY THIS: add a "hobby" key and print it.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 34 — Word Frequency Counter                   ⭐⭐⭐ tricky
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Count how many times each word appears.
# DESCRIPTION : Builds a dict of word -> count using a comprehension.
# CONCEPTS    : strings .split(), set(), .count(), dict comprehension
# WHAT  : {w: words.count(w) for w in set(words)} maps each unique word
#         to how many times it appears.
# WHY   : Counting is a core data task.
# WHEN  : Text analysis, tallies.
# HOW   : split into words, then count each unique word.
print("PROJECT 34 — Word Frequency Counter")
text = "red blue red green blue red"        # the text to analyse
words = text.split()                        # -> ['red','blue','red','green','blue','red']
counts = {w: words.count(w) for w in set(words)}   # unique word -> its count
print(f"Counts: {counts}")
# OUTPUT: Counts: {'red': 3, 'blue': 2, 'green': 1}   (order may vary)
# TRY THIS: find the most common word with max(counts, key=counts.get).
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 35 — Phone Book Lookup                        ⭐⭐ easy
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Look up a phone number safely.
# DESCRIPTION : Uses .get() so a missing name doesn't crash.
# CONCEPTS    : dicts, .get() with a default
# WHAT  : .get(key, default) returns the value or a fallback.
# WHY   : Reading a missing key with [ ] would crash (KeyError).
# WHEN  : When a key might not exist.
# HOW   : phonebook.get(name, "not found").
# SYNTAX: my_dict.get("key", default)
print("PROJECT 35 — Phone Book Lookup")
phonebook = {"Alice": "555-1234", "Bob": "555-9876"}
search = "Carol"                            # a name that's NOT in the book
number = phonebook.get(search, "not found") # safe lookup with a fallback
print(f"{search}: {number}")
# OUTPUT: Carol: not found
# TRY THIS: search for "Alice" instead.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 36 — Inventory Update                         ⭐⭐ easy
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Add stock and add a new product.
# DESCRIPTION : Updates an existing value and adds a new key.
# CONCEPTS    : dicts, updating values, adding keys, += 
# WHAT  : Assigning to a key updates it (or creates it if new).
# WHY   : Inventories change all the time.
# WHEN  : Counters, stock, scores stored by name.
# HOW   : inventory["apples"] += 5 ; inventory["pears"] = 10.
print("PROJECT 36 — Inventory Update")
inventory = {"apples": 12, "bananas": 8}    # current stock
inventory["apples"] += 5                    # restock apples: 12 + 5 = 17
inventory["pears"] = 10                      # add a brand-new product
print(f"Inventory: {inventory}")
# OUTPUT: Inventory: {'apples': 17, 'bananas': 8, 'pears': 10}
# TRY THIS: sell 3 bananas with inventory["bananas"] -= 3.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 37 — Simple Settings (config)                 ⭐⭐ easy
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Read settings with safe defaults.
# DESCRIPTION : Uses .get() to fall back when a setting is missing.
# CONCEPTS    : dicts, .get() with defaults, booleans
# WHAT  : .get() lets you provide a default for optional settings.
# WHY   : Programs need sensible defaults when a setting isn't given.
# WHEN  : Configuration, options, preferences.
# HOW   : settings.get("dark_mode", False).
print("PROJECT 37 — Simple Settings")
settings = {"volume": 70, "dark_mode": True}   # the user's chosen settings
volume = settings.get("volume", 50)             # present -> 70
language = settings.get("language", "English")  # missing -> default "English"
print(f"Volume={volume}, Language={language}, Dark={settings.get('dark_mode')}")
# OUTPUT: Volume=70, Language=English, Dark=True
# TRY THIS: remove "volume" from the dict; the default 50 kicks in.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 38 — Menu Price Lookup & Bill                 ⭐⭐⭐ tricky
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Look up item prices and total an order.
# DESCRIPTION : Uses a menu dict to price an order, then sums it.
# CONCEPTS    : dicts, key access, sum(), comprehension
# WHAT  : menu[item] gets a price; a comprehension prices the whole order.
# WHY   : Looking up values by name is what dicts are best at.
# WHEN  : Pricing, mapping names to values.
# HOW   : sum(menu[item] for item in order).
print("PROJECT 38 — Menu Price Lookup & Bill")
menu = {"coffee": 3.0, "cake": 4.5, "tea": 2.5}   # item -> price
order = ["coffee", "cake", "coffee"]               # what the customer ordered
bill = sum(menu[item] for item in order)           # add up each item's price
print(f"Order: {order}")
print(f"Bill: ${bill:.2f}")
# OUTPUT:
# Order: ['coffee', 'cake', 'coffee']
# Bill: $10.50
# TRY THIS: add "tea" to the order and re-run.
print()

print("Group F complete — 6 dictionary projects done!")


print("GROUP G — TUPLES & SETS\n")


# ──────────────────────────────────────────────────────────────
# PROJECT 39 — Distance Between Two Points              ⭐⭐⭐ tricky
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Measure the straight-line distance between two points.
# DESCRIPTION : Uses (x, y) tuples and the distance formula.
# CONCEPTS    : tuples, unpacking, arithmetic, power (** 0.5 = square root)
# WHAT  : ** 0.5 raises to the power one-half, which is a square root.
# WHY   : The distance formula needs a square root.
# WHEN  : Geometry, maps, games.
# HOW   : distance = ((x2-x1)**2 + (y2-y1)**2) ** 0.5.
print("PROJECT 39 — Distance Between Two Points")
point_a = (0, 0)                           # first point as an (x, y) tuple
point_b = (3, 4)                           # second point
x1, y1 = point_a                           # unpack the first point
x2, y2 = point_b                           # unpack the second point
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5   # the distance formula
print(f"Distance: {distance}")
# OUTPUT: Distance: 5.0
# TRY THIS: change point_b to (6, 8); the distance should be 10.0.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 40 — RGB to Hex Colour                        ⭐⭐⭐ tricky
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Turn an (R, G, B) colour into a hex code like #ff8800.
# DESCRIPTION : Formats each colour number as 2-digit hex.
# CONCEPTS    : tuples, unpacking, f-string format spec :02x
# WHAT  : :02x formats a number as 2-digit lowercase hexadecimal.
# WHY   : Web colours use hex (00-ff per channel).
# WHEN  : Colours, low-level number display.
# HOW   : f"#{r:02x}{g:02x}{b:02x}".
# SYNTAX: f"{number:02x}"   (0 = pad with zeros, 2 = width, x = hex)
print("PROJECT 40 — RGB to Hex Colour")
rgb = (255, 136, 0)                         # an (R, G, B) colour: orange
r, g, b = rgb                               # unpack the three channels
hex_color = f"#{r:02x}{g:02x}{b:02x}"       # format each as 2-digit hex
print(f"RGB {rgb} -> {hex_color}")
# OUTPUT: RGB (255, 136, 0) -> #ff8800
# TRY THIS: try (0, 0, 0) for black and (255, 255, 255) for white.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 41 — Common Friends                           ⭐⭐ easy
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Find friends two people share.
# DESCRIPTION : Uses set intersection (&) to find common items.
# CONCEPTS    : sets, intersection (&)
# WHAT  : set_a & set_b keeps only items present in BOTH sets.
# WHY   : "What do these two have in common?" is a set operation.
# WHEN  : Comparing groups, matching, recommendations.
# HOW   : Convert each friend list to a set, then use &.
# SYNTAX: set_a & set_b
print("PROJECT 41 — Common Friends")
alice_friends = {"Bob", "Carol", "Dan", "Eve"}
bob_friends = {"Alice", "Carol", "Eve", "Frank"}
shared = alice_friends & bob_friends        # friends in both sets
print(f"Common friends: {shared}")
# OUTPUT: Common friends: {'Carol', 'Eve'}   (order may vary)
# TRY THIS: use | to see ALL friends across both people.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 42 — Unique Tags                              ⭐⭐ easy
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Get the unique tags from a list that has repeats.
# DESCRIPTION : Converts a tag list into a set to drop duplicates.
# CONCEPTS    : sets, len(), sorted()
# WHAT  : set() removes duplicates automatically.
# WHY   : Tags often repeat; you want each one once.
# WHEN  : Tags, categories, labels.
# HOW   : set(tags), then sorted() to display nicely.
print("PROJECT 42 — Unique Tags")
tags = ["python", "code", "python", "beginner", "code", "python"]
unique_tags = set(tags)                     # drop the repeats
print(f"{len(unique_tags)} unique tags: {sorted(unique_tags)}")
# OUTPUT: 3 unique tags: ['beginner', 'code', 'python']
# TRY THIS: add more repeated tags; the unique count stays correct.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 43 — Midpoint of Two Points                   ⭐⭐ easy
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Find the point exactly between two points.
# DESCRIPTION : Averages the x's and the y's.
# CONCEPTS    : tuples, unpacking, arithmetic, building a tuple
# WHAT  : The midpoint is the average of the two x's and two y's.
# WHY   : Shows how to compute and RETURN a new tuple.
# WHEN  : Geometry, layout, animation.
# HOW   : midpoint = ((x1+x2)/2, (y1+y2)/2).
print("PROJECT 43 — Midpoint of Two Points")
p1 = (2, 4)                                 # first point
p2 = (6, 10)                                # second point
x1, y1 = p1                                 # unpack first
x2, y2 = p2                                 # unpack second
midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)   # average each coordinate
print(f"Midpoint of {p1} and {p2} is {midpoint}")
# OUTPUT: Midpoint of (2, 4) and (6, 10) is (4.0, 7.0)
# TRY THIS: find the midpoint of (0, 0) and (10, 10).
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 44 — Hobby Comparison (set operations)        ⭐⭐⭐ tricky
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Compare two people's hobbies in several ways.
# DESCRIPTION : Uses union, intersection, and difference together.
# CONCEPTS    : sets, union (|), intersection (&), difference (-)
# WHAT  : | = all, & = shared, - = only in the first.
# WHY   : Three quick answers from the same two sets.
# WHEN  : Comparing any two groups.
# HOW   : a | b, a & b, a - b.
print("PROJECT 44 — Hobby Comparison")
sam = {"reading", "chess", "cycling"}       # Sam's hobbies
lee = {"chess", "cooking", "cycling"}       # Lee's hobbies
print(f"All hobbies   : {sorted(sam | lee)}")   # union: everything
print(f"Shared hobbies: {sorted(sam & lee)}")   # intersection: both
print(f"Only Sam's    : {sorted(sam - lee)}")   # difference: Sam not Lee
# OUTPUT:
# All hobbies   : ['chess', 'cooking', 'cycling', 'reading']
# Shared hobbies: ['chess', 'cycling']
# Only Sam's    : ['reading']
# TRY THIS: print "Only Lee's" with (lee - sam).
print()

print("Group G complete — 6 tuple/set projects done!")


print("GROUP H — MIXED CAPSTONES\n")


# ──────────────────────────────────────────────────────────────
# PROJECT 45 — Receipt Generator                        ⭐⭐⭐ tricky
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Print a shop receipt with a subtotal, tax, and total.
# DESCRIPTION : Stores each item's price and quantity, then totals them.
# CONCEPTS    : dicts, tuples as values, sum(), comprehension, "\n".join
# WHAT  : Each value is a (price, quantity) tuple; we sum price*qty.
# WHY   : Combines several tools into one realistic task.
# WHEN  : Carts, billing, summaries.
# HOW   : subtotal = sum(price*qty for (price, qty) in cart.values()).
print("PROJECT 45 — Receipt Generator")
cart = {                                    # item -> (price, quantity)
    "Apple":  (0.50, 6),
    "Bread":  (2.00, 2),
    "Milk":   (1.20, 3),
}
# Build one text line per item (name, qty, and line total), joined by newlines:
lines = "\n".join(f"  {name:<6} {qty} x {price:.2f} = {price*qty:.2f}"
                  for name, (price, qty) in cart.items())
subtotal = sum(price * qty for (price, qty) in cart.values())   # add line totals
tax = subtotal * 0.10                        # 10% tax
total = subtotal + tax                       # final amount
print(lines)                                 # the itemised lines
print(f"  Subtotal = {subtotal:.2f}")
print(f"  Tax(10%) = {tax:.2f}")
print(f"  TOTAL    = {total:.2f}")
# OUTPUT:
#   Apple  6 x 0.50 = 3.00
#   Bread  2 x 2.00 = 4.00
#   Milk   3 x 1.20 = 3.60
#   Subtotal = 10.60
#   Tax(10%) = 1.06
#   TOTAL    = 11.66
# TRY THIS: add a new item to the cart dict.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 46 — Student Report Card                      ⭐⭐⭐ tricky
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Show subject scores, the average, and a letter grade.
# DESCRIPTION : Uses a dict of subject->score, then computes a grade.
# CONCEPTS    : dicts, sum()/len() average, chained conditional expression
# WHAT  : average = sum(scores)/len(scores); grade chosen from the average.
# WHY   : Brings dict data and number logic together.
# WHEN  : Reports, summaries, dashboards.
# HOW   : Compute the average, then map it to a letter.
print("PROJECT 46 — Student Report Card")
grades = {"Math": 88, "Science": 76, "English": 92}   # subject -> score
average = sum(grades.values()) / len(grades)          # average score
letter = ("A" if average >= 90 else                   # pick a grade
          "B" if average >= 80 else
          "C" if average >= 70 else "F")
print(f"Subjects: {grades}")
print(f"Average : {average:.1f}  ->  Grade {letter}")
# OUTPUT:
# Subjects: {'Math': 88, 'Science': 76, 'English': 92}
# Average : 85.3  ->  Grade B
# TRY THIS: add a "History" subject and re-run.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 47 — Quiz Scorer                              ⭐⭐⭐ tricky
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Mark a quiz by comparing answers to the correct ones.
# DESCRIPTION : Counts matches between two lists using zip().
# CONCEPTS    : lists, zip(), sum() with a comprehension, percentages
# WHAT  : zip pairs each answer with its correct answer; we count matches.
# WHY   : Comparing two lists position-by-position is a common task.
# WHEN  : Grading, validation, matching.
# HOW   : sum(1 for a, c in zip(answers, correct) if a == c).
print("PROJECT 47 — Quiz Scorer")
correct = ["A", "B", "C", "D", "A"]          # the answer key
answers = ["A", "B", "D", "D", "C"]          # the student's answers
score = sum(1 for a, c in zip(answers, correct) if a == c)   # count matches
percent = score / len(correct) * 100         # turn into a percentage
print(f"Score: {score}/{len(correct)} ({percent:.0f}%)")
# OUTPUT: Score: 3/5 (60%)
# TRY THIS: change some answers to match and watch the score rise.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 48 — Leaderboard                              ⭐⭐⭐ tricky
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Rank players from highest to lowest score.
# DESCRIPTION : Stores (score, name) tuples, sorts them, and numbers them.
# CONCEPTS    : tuples, sorted(reverse=True), enumerate(), "\n".join
# WHAT  : Sorting tuples sorts by the FIRST item (score) automatically.
# WHY   : Putting score first means no special sort key is needed.
# WHEN  : Rankings, leaderboards, top lists.
# HOW   : sort (score, name) tuples descending, then number with enumerate.
print("PROJECT 48 — Leaderboard")
players = [(95, "Alice"), (88, "Bob"), (99, "Carol"), (88, "Dan")]  # (score, name)
ranked = sorted(players, reverse=True)       # highest score first
board = "\n".join(f"  {place}. {name} - {score}"
                  for place, (score, name) in enumerate(ranked, start=1))
print(board)
# OUTPUT:
#   1. Carol - 99
#   2. Alice - 95
#   3. Bob - 88
#   4. Dan - 88
# TRY THIS: add a new (score, name) player to the list.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 49 — Budget Tracker                           ⭐⭐⭐ tricky
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Work out money left after expenses.
# DESCRIPTION : Subtracts total expenses from income and reports status.
# CONCEPTS    : dicts, sum() of values, subtraction, conditional expression
# WHAT  : sum(expenses.values()) totals all the expense amounts.
# WHY   : Combines a dict total with a simple decision.
# WHEN  : Money, resources, capacity.
# HOW   : balance = income - total_expenses.
print("PROJECT 49 — Budget Tracker")
income = 2000                               # money coming in
expenses = {"rent": 900, "food": 400, "fun": 250}   # category -> amount
total_expenses = sum(expenses.values())     # add up all expenses
balance = income - total_expenses           # what's left
status = "surplus" if balance >= 0 else "over budget"   # decide the status
print(f"Income={income}, Expenses={total_expenses}, Balance={balance} ({status})")
# OUTPUT: Income=2000, Expenses=1550, Balance=450 (surplus)
# TRY THIS: raise an expense so the balance goes negative.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 50 — Unit Converter                           ⭐⭐ easy
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Convert kilometres into several other units at once.
# DESCRIPTION : Applies a few conversion formulas to one value.
# CONCEPTS    : floats, arithmetic, f-strings, number formatting
# WHAT  : One input value feeding several conversion formulas.
# WHY   : Shows reusing a variable in multiple calculations.
# WHEN  : Measurements, conversions.
# HOW   : multiply the value by each conversion factor.
print("PROJECT 50 — Unit Converter")
km = 5                                      # distance in kilometres
miles = km * 0.621371                       # km -> miles
meters = km * 1000                          # km -> meters
feet = km * 3280.84                         # km -> feet
print(f"{km} km = {miles:.2f} miles = {meters:.0f} m = {feet:.0f} ft")
# OUTPUT: 5 km = 3.11 miles = 5000 m = 16404 ft
# TRY THIS: change km to 10.
print()


# ──────────────────────────────────────────────────────────────
# PROJECT 51 — Contact Card Formatter                   ⭐⭐⭐ tricky
# ──────────────────────────────────────────────────────────────
# OBJECTIVE   : Turn contact details into a neat printed card.
# DESCRIPTION : Combines dict data, text alignment, and a banner.
# CONCEPTS    : dicts, f-strings, alignment (:<, :>), string repetition
# WHAT  : ":<12" left-aligns text in a width of 12 for neat columns.
# WHY   : Formatting makes output readable and professional.
# WHEN  : Cards, tables, reports.
# HOW   : Pad each label to a fixed width, wrap in a line border.
print("PROJECT 51 — Contact Card Formatter")
contact = {"name": "Maya Cruz", "email": "maya@mail.com", "phone": "555-0102"}
border = "+" + "-" * 30 + "+"               # a top/bottom border line
print(border)
print(f"| {'Name:':<8}{contact['name']:<20} |")    # label + value, padded
print(f"| {'Email:':<8}{contact['email']:<20} |")
print(f"| {'Phone:':<8}{contact['phone']:<20} |")
print(border)
# OUTPUT:
# +------------------------------+
# | Name:  Maya Cruz            |
# | Email: maya@mail.com        |
# | Phone: 555-0102             |
# +------------------------------+
# TRY THIS: add a "city" line to the card.
print()

print("Group H complete — 7 capstone projects done!")
print("\nYou finished 51 mini projects! You now understand variables by USING them.")

print("\n" + "=" * 60)
print("  ALL 51 MINI PROJECTS COMPLETE!")
print("=" * 60)

