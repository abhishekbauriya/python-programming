"""
variables.py
============

A comprehensive guide to Python variables for beginners.
This file covers all types of variables, their usage, and best practices.

Author: Abhishek
Date: 2026
"""

# =============================================================================
# SECTION 1: BASIC VARIABLE DECLARATION
# =============================================================================

# What is a Variable?
# -------------------
# A variable is like a CONTAINER that stores data.
# Think of it as a labeled box where you put something to use later.

# SYNTAX: variable_name = value
# DESCRIPTION: Creates a variable and assigns a value to it
# PARAMETERS: 
#   - variable_name: Any valid name you choose (follows naming rules)
#   - value: The data you want to store
# RETURN VALUE: None (but variable is now accessible)

# Example 1: Creating a simple variable
name = "Alice"  # Creates a variable 'name' containing the string "Alice"

# Example 2: Creating a number variable
age = 25  # Creates a variable 'age' containing the integer 25

# WHY USE IT: To store and reuse data throughout your program
# WHEN TO USE IT: Whenever you need to remember or track information

# COMMON MISTAKES TO AVOID:
# ❌ name = "Alice" (correct)
# ❌ Name = "Alice" (different variable - Python is case-sensitive!)
# ❌ 1name = "Alice" (ERROR - can't start with a number)
# ❌ my-name = "Alice" (ERROR - can't use hyphens, use underscores)
# ✅ my_name = "Alice" (correct - use underscores for multiple words)



# =============================================================================
# SECTION 2: DATA TYPES IN PYTHON
# =============================================================================

# Python automatically detects the type of data you're storing
# This is called "Dynamic Typing"

# -------------------------------------------------------------------------
# 2.1 INTEGER (int) - Whole numbers without decimals
# -------------------------------------------------------------------------
# SYNTAX: variable_name = integer_value
# DESCRIPTION: Stores whole numbers (positive, negative, or zero)
# PARAMETERS: Any whole number
# RETURN VALUE: None

student_count = 100          # Positive integer
temperature_below_zero = -15 # Negative integer  
zero_value = 0               # Zero is also an integer

# WHY USE IT: For counting, indexing, or any whole number value
# WHEN TO USE IT: When you don't need decimal precision

# HOW TO CHECK TYPE:
print(type(student_count))   # Output: <class 'int'>

# COMMON MISTAKES TO AVOID:
# ❌ student_count = "100"  (This is a STRING, not integer!)
# ✅ student_count = 100    (This is an integer)


# -------------------------------------------------------------------------
# 2.2 FLOAT (float) - Numbers with decimal points
# -------------------------------------------------------------------------
# SYNTAX: variable_name = float_value
# DESCRIPTION: Stores numbers with decimal points for precision
# PARAMETERS: Any number with decimal point or using scientific notation
# RETURN VALUE: None

pi = 3.14159                 # Standard decimal
price = 19.99                # Currency example
weight = 72.5                # Weight example
scientific = 2.5e4           # Scientific notation (25000.0)

# WHY USE IT: When you need decimal precision
# WHEN TO USE IT: For measurements, prices, percentages, calculations

# HOW TO CHECK TYPE:
print(type(pi))              # Output: <class 'float'>

# COMMON MISTAKES TO AVOID:
# ❌ price = 19,99  (ERROR - comma is not a decimal point in Python)
# ✅ price = 19.99  (Correct - use dot for decimal)


# -------------------------------------------------------------------------
# 2.3 STRING (str) - Text data
# -------------------------------------------------------------------------
# SYNTAX: variable_name = "text" OR variable_name = 'text'
# DESCRIPTION: Stores text, characters, or any sequence of characters
# PARAMETERS: Any text enclosed in single (''), double (""), or triple quotes
# RETURN VALUE: None

greeting = "Hello, World!"           # Double quotes
single_quote = 'Python is fun'       # Single quotes (same as double)
multi_line = """This is
a multi-line
string"""                            # Triple quotes for multiple lines

# String with quotes inside
quote = 'She said, "Python is amazing!"'

# WHY USE IT: To store and manipulate text
# WHEN TO USE IT: For names, messages, addresses, any text data

# HOW TO CHECK TYPE:
print(type(greeting))        # Output: <class 'str'>

# COMMON MISTAKES TO AVOID:
# ❌ text = "Hello"     (correct)
# ❌ text = Hello       (ERROR - without quotes, Python thinks it's a variable)
# ❌ text = "It's"      (ERROR - mismatched quotes)
# ✅ text = 'It\'s'     (Correct - escaped quote)
# ✅ text = "It's"      (Correct - different quote types)


# -------------------------------------------------------------------------
# 2.4 BOOLEAN (bool) - True or False values
# -------------------------------------------------------------------------
# SYNTAX: variable_name = True OR variable_name = False
# DESCRIPTION: Stores logical values - only True or False
# PARAMETERS: Must be exactly True or False (capitalized!)
# RETURN VALUE: None

is_student = True            # User is a student
has_paid = False             # User hasn't paid
is_adult = age >= 18         # Boolean expression (evaluates to True/False)

# WHY USE IT: For conditions, flags, and decision-making
# WHEN TO USE IT: When you need yes/no, on/off, true/false values

# HOW TO CHECK TYPE:
print(type(is_student))      # Output: <class 'bool'>

# COMMON MISTAKES TO AVOID:
# ❌ is_student = true    (ERROR - must be capitalized)
# ❌ is_student = "True"  (This is a STRING, not boolean!)
# ✅ is_student = True    (Correct - boolean True)


# -------------------------------------------------------------------------
# 2.5 NONE (NoneType) - Represents absence of value
# -------------------------------------------------------------------------
# SYNTAX: variable_name = None
# DESCRIPTION: Represents "nothing" or "no value"
# PARAMETERS: None (literally)
# RETURN VALUE: None

middle_name = None           # User has no middle name
result = None                # Will be calculated later
error_message = None         # No error yet

# WHY USE IT: To indicate a variable exists but has no meaningful value
# WHEN TO USE IT: As a placeholder, initial value, or to indicate "empty"

# HOW TO CHECK TYPE:
print(type(middle_name))     # Output: <class 'NoneType'>

# COMMON MISTAKES TO AVOID:
# ❌ result = none      (ERROR - must be capitalized)
# ❌ result = "None"    (This is a STRING, not None!)
# ✅ result = None      (Correct)


# -------------------------------------------------------------------------
# 2.6 LIST (list) - Ordered, mutable collection
# -------------------------------------------------------------------------
# SYNTAX: variable_name = [item1, item2, item3, ...]
# DESCRIPTION: Stores multiple values in an ordered sequence
# PARAMETERS: Comma-separated values inside square brackets
# RETURN VALUE: None

fruits = ["apple", "banana", "cherry"]     # List of strings
numbers = [1, 2, 3, 4, 5]                  # List of integers
mixed = ["hello", 42, True, 3.14]          # Mixed types (allowed but not recommended)
empty_list = []                            # Empty list

# WHY USE IT: To store multiple related items
# WHEN TO USE IT: When you have a collection of items that may change

# HOW TO CHECK TYPE:
print(type(fruits))          # Output: <class 'list'>

# ACCESSING ITEMS (indexing starts at 0!):
first_fruit = fruits[0]      # "apple" (first item)
last_fruit = fruits[-1]      # "cherry" (last item using negative index)

# COMMON MISTAKES TO AVOID:
# ❌ fruits = "apple", "banana"  (This creates a TUPLE, not list!)
# ❌ third = fruits[3]           (ERROR - only 3 items, max index is 2)
# ✅ fruits = ["apple", "banana", "cherry"]  (Correct)


# -------------------------------------------------------------------------
# 2.7 TUPLE (tuple) - Ordered, IMMUTABLE collection
# -------------------------------------------------------------------------
# SYNTAX: variable_name = (item1, item2, item3, ...)
# DESCRIPTION: Like a list, but CANNOT be changed after creation
# PARAMETERS: Comma-separated values inside parentheses
# RETURN VALUE: None

coordinates = (10.5, 20.3)               # Tuple of floats
rgb_color = (255, 128, 0)                # RGB color values
single_item_tuple = (42,)                # Note: comma needed for single item!
empty_tuple = ()                         # Empty tuple

# WHY USE IT: For data that should NEVER change (constants, fixed data)
# WHEN TO USE IT: For coordinates, configurations, data that must stay constant

# HOW TO CHECK TYPE:
print(type(coordinates))     # Output: <class 'tuple'>

# COMMON MISTAKES TO AVOID:
# ❌ single = (42)       (This is just 42 in parentheses, NOT a tuple!)
# ✅ single = (42,)      (Correct - comma makes it a tuple)


# -------------------------------------------------------------------------
# 2.8 DICTIONARY (dict) - Key-value pairs
# -------------------------------------------------------------------------
# SYNTAX: variable_name = {key1: value1, key2: value2, ...}
# DESCRIPTION: Stores data as key-value pairs for easy lookup
# PARAMETERS: Key-value pairs inside curly braces, separated by colons
# RETURN VALUE: None

person = {
    "name": "Alice",                # Key: "name", Value: "Alice"
    "age": 25,                      # Key: "age", Value: 25
    "is_student": True              # Key: "is_student", Value: True
}

# WHY USE IT: To store related information with meaningful labels
# WHEN TO USE IT: For structured data, configurations, records

# HOW TO CHECK TYPE:
print(type(person))         # Output: <class 'dict'>

# ACCESSING VALUES:
person_name = person["name"]        # "Alice"
person_age = person.get("age")      # 25 (safer method)

# COMMON MISTAKES TO AVOID:
# ❌ person = {name: "Alice"}      (ERROR - keys must be quoted if strings!)
# ❌ person = {"name": "Alice", "name": "Bob"}  (Duplicate keys!)
# ✅ person = {"name": "Alice", "age": 25}  (Correct)


# -------------------------------------------------------------------------
# 2.9 SET (set) - Unordered collection of UNIQUE items
# -------------------------------------------------------------------------
# SYNTAX: variable_name = {item1, item2, item3, ...}
# DESCRIPTION: Stores unique values only (duplicates removed automatically)
# PARAMETERS: Comma-separated values inside curly braces
# RETURN VALUE: None

unique_numbers = {1, 2, 3, 4, 5}             # Set of numbers
with_duplicates = {1, 2, 2, 3, 3, 3}         # Becomes {1, 2, 3}
empty_set = set()                             # Empty set (NOT {} - that's dict!)

# WHY USE IT: To ensure uniqueness or for set operations (union, intersection)
# WHEN TO USE IT: When you need unique values or mathematical set operations

# HOW TO CHECK TYPE:
print(type(unique_numbers))   # Output: <class 'set'>

# COMMON MISTAKES TO AVOID:
# ❌ empty = {}          (This creates an EMPTY DICTIONARY, not set!)
# ✅ empty = set()       (Correct way to create empty set)



# =============================================================================
# SECTION 3: VARIABLE NAMING RULES AND CONVENTIONS
# =============================================================================

# RULES (MUST follow - otherwise ERROR):
# ---------------------------------------
# 1. Can only contain letters, numbers, and underscores
# 2. CANNOT start with a number
# 3. CANNOT use Python keywords (if, else, for, while, etc.)
# 4. Case-sensitive (name, Name, NAME are different variables)

# CONVENTIONS (SHOULD follow - for readability):
# -----------------------------------------------
# 1. Use lowercase letters for variable names
# 2. Use underscores to separate words (snake_case)
# 3. Use descriptive names (not single letters except in loops)
# 4. Avoid using 'l', 'O', 'I' as single-letter names (confusing with numbers)

# VALID NAMES:
user_name = "Alice"         # ✅ snake_case (recommended)
userName = "Alice"          # ✅ camelCase (acceptable but not Pythonic)
_user = "Alice"             # ✅ Leading underscore (convention: "private")
user2 = "Alice"             # ✅ Number in middle/end is fine

# INVALID NAMES (will cause ERROR):
# 2nd_user = "Alice"        # ❌ Starts with number
# user-name = "Alice"       # ❌ Contains hyphen
# class = "Alice"           # ❌ Uses Python keyword
# user name = "Alice"       # ❌ Contains space

# GOOD vs BAD naming examples:
x = "John"                  # ❌ Bad - What does 'x' mean?
user_first_name = "John"    # ✅ Good - Descriptive

a = 100                     # ❌ Bad - Unclear
total_score = 100           # ✅ Good - Clear purpose

temp = 98.6                 # ⚠️ Okay for short scripts
body_temperature = 98.6     # ✅ Better - More specific



# =============================================================================
# SECTION 4: VARIABLE ASSIGNMENT TECHNIQUES
# =============================================================================


# -------------------------------------------------------------------------
# 4.1 Multiple Assignment (same value to multiple variables)
# -------------------------------------------------------------------------
# SYNTAX: var1 = var2 = var3 = value
# DESCRIPTION: Assigns the same value to multiple variables at once
# PARAMETERS: Multiple variable names, one value
# RETURN VALUE: None

x = y = z = 0               # All three variables get value 0
print(x, y, z)               # Output: 0 0 0

# WHY USE IT: To initialize multiple variables to the same starting value
# WHEN TO USE IT: When setting up default values or resetting counters


# -------------------------------------------------------------------------
# 4.2 Multiple Assignment (different values)
# -------------------------------------------------------------------------
# SYNTAX: var1, var2, var3 = value1, value2, value3
# DESCRIPTION: Assigns different values to multiple variables in one line
# PARAMETERS: Equal number of variables and values
# RETURN VALUE: None

first_name, last_name, age = "Alice", "Smith", 25
print(first_name)            # Output: Alice
print(last_name)             # Output: Smith
print(age)                   # Output: 25

# WHY USE IT: Cleaner code when assigning related values
# WHEN TO USE IT: When unpacking values from a function or collection

# COMMON MISTAKES TO AVOID:
# ❌ a, b = 1, 2, 3       (ERROR - 3 values for 2 variables)
# ❌ a, b, c = 1, 2        (ERROR - 2 values for 3 variables)
# ✅ a, b, c = 1, 2, 3     (Correct - equal counts)


# -------------------------------------------------------------------------
# 4.3 Swapping Variables (Python's special way)
# -------------------------------------------------------------------------
# SYNTAX: var1, var2 = var2, var1
# DESCRIPTION: Swaps values between two variables without temp variable
# PARAMETERS: Two variables to swap
# RETURN VALUE: None

a = 10
b = 20
print(f"Before: a={a}, b={b}")  # Output: Before: a=10, b=20

a, b = b, a                          # Swap!
print(f"After: a={a}, b={b}")    # Output: After: a=20, b=10

# WHY USE IT: Python's elegant way to swap - no need for temp variable
# WHEN TO USE IT: Whenever you need to swap two values

# Other languages need:
# temp = a
# a = b
# b = temp
# Python does it in one line!



# =============================================================================
# SECTION 5: TYPE CONVERSION (Type Casting)
# =============================================================================

# Sometimes you need to change one type to another
# SYNTAX: new_variable = target_type(original_value)


# -------------------------------------------------------------------------
# 5.1 Converting TO Integer
# -------------------------------------------------------------------------
# SYNTAX: int(value)
# DESCRIPTION: Converts value to integer (truncates decimals)
# PARAMETERS: Number, string number, or boolean
# RETURN VALUE: Integer

string_num = "42"
converted_to_int = int(string_num)     # "42" → 42
print(type(converted_to_int))          # <class 'int'>

float_to_int = int(3.99)               # 3.99 → 3 (truncates, doesn't round!)
bool_to_int = int(True)                # True → 1
bool_false_to_int = int(False)         # False → 0

# COMMON MISTAKES TO AVOID:
# ❌ int("hello")     (ERROR - can't convert text to number)
# ❌ int("3.14")      (ERROR - can't directly convert float string)
# ✅ int(float("3.14"))  (Correct - convert to float first)


# -------------------------------------------------------------------------
# 5.2 Converting TO Float
# -------------------------------------------------------------------------
# SYNTAX: float(value)
# DESCRIPTION: Converts value to float (adds .0 if needed)
# PARAMETERS: Number, string number, or boolean
# RETURN VALUE: Float

int_to_float = float(42)               # 42 → 42.0
string_to_float = float("3.14")        # "3.14" → 3.14
bool_to_float = float(True)            # True → 1.0


# -------------------------------------------------------------------------
# 5.3 Converting TO String
# -------------------------------------------------------------------------
# SYNTAX: str(value)
# DESCRIPTION: Converts any value to its string representation
# PARAMETERS: Any Python object
# RETURN VALUE: String

num_to_string = str(42)                # 42 → "42"
float_to_string = str(3.14)            # 3.14 → "3.14"
bool_to_string = str(True)             # True → "True"
list_to_string = str([1, 2, 3])        # [1, 2, 3] → "[1, 2, 3]"

# WHY USE IT: For concatenating numbers with strings
# WHEN TO USE IT: When building messages with numbers

# Example - building a message:
age = 25
message = "I am " + str(age) + " years old"  # Must convert to string!
print(message)  # Output: I am 25 years old

# Better alternative (f-strings):
message = f"I am {age} years old"  # Automatically converts!
print(message)  # Output: I am 25 years old



# =============================================================================
# SECTION 6: CHECKING VARIABLE TYPES
# =============================================================================

# SYNTAX: type(variable)
# DESCRIPTION: Returns the type of a variable
# PARAMETERS: Any Python object
# RETURN VALUE: Type object (e.g., <class 'int'>)

my_var = 42
print(type(my_var))            # Output: <class 'int'>

# SYNTAX: isinstance(variable, type)
# DESCRIPTION: Checks if variable is of specified type (returns True/False)
# PARAMETERS: Variable to check, type to check against
# RETURN VALUE: Boolean (True or False)

print(isinstance(my_var, int))     # Output: True
print(isinstance(my_var, str))     # Output: False
print(isinstance(my_var, (int, float)))  # Output: True (either int OR float)

# WHY USE isinstance instead of type():
# - isinstance handles inheritance better
# - Can check against multiple types at once
# - More Pythonic and recommended



# =============================================================================
# SECTION 7: CONSTANTS (Variables that shouldn't change)
# =============================================================================

# Python doesn't have true constants, but we use CONVENTION:
# All uppercase letters with underscores between words

MAX_SCORE = 100                  # Maximum possible score
PI = 3.14159265359               # Value of Pi
MAX_RETRIES = 3                  # Maximum login attempts
DEFAULT_LANGUAGE = "en"          # Default language setting
API_URL = "https://api.example.com"  # API endpoint

# WHY USE IT: To indicate values that should NEVER be changed in the code
# WHEN TO USE IT: For configuration values, limits, fixed values

# COMMON MISTAKES TO AVOID:
# ❌ MAX_SCORE = 100; MAX_SCORE = 200  (Don't change constants!)
# ❌ max_score = 100          (Looks like a regular variable)
# ✅ MAX_SCORE = 100          (Clearly indicates it's a constant)

# NOTE: Python won't stop you from changing these, but other programmers
# will be confused if you do. It's a CONVENTION, not a rule.


# =============================================================================
# SECTION 8: SPECIAL VARIABLES AND CONVENTIONS
# =============================================================================

# -------------------------------------------------------------------------
# 8.1 Private Variables (by convention)
# -------------------------------------------------------------------------
# Leading underscore indicates "private" - don't use outside the class/module

_internal_data = "Don't access this directly"   # Convention: private
__very_private = "Even more private"            # Name mangling in classes

# -------------------------------------------------------------------------
# 8.2 Dunder Variables (Double Underscore)
# -------------------------------------------------------------------------
# Python uses these for special purposes - don't create your own!

__name__ = "__main__"    # Module name (set automatically)
__doc__ = "Docstring"    # Module documentation

# -------------------------------------------------------------------------
# 8.3 Throwaway Variables (Underscore only)
# -------------------------------------------------------------------------
# Use single underscore when you don't need the value

for _ in range(5):           # Just want to repeat 5 times, don't need index
    print("Hello!")

# Unpacking when you don't need all values
first, _, third = [1, 2, 3]  # Get first and third, ignore second


# =============================================================================
# SECTION 9: PRACTICAL EXAMPLES
# =============================================================================

# -------------------------------------------------------------------------
# Example 1: User Profile System
# -------------------------------------------------------------------------
print("\n--- Example 1: User Profile ---")

# Storing user information
user_profile = {
    "username": "alice_smith",
    "email": "alice@example.com",
    "age": 25,
    "is_active": True,
    "score": 0,
    "preferences": {
        "theme": "dark",
        "notifications": True
    }
}

# Accessing and using the data
print(f"Username: {user_profile['username']}")
print(f"Is Active: {user_profile['is_active']}")

# Updating a value
user_profile["score"] = 100
print(f"Updated Score: {user_profile['score']}")

# -------------------------------------------------------------------------
# Example 2: Shopping Cart
# -------------------------------------------------------------------------
print("\n--- Example 2: Shopping Cart ---")

# Cart items as list of dictionaries
cart = [
    {"name": "Python Book", "price": 39.99, "quantity": 1},
    {"name": "Laptop Stand", "price": 25.50, "quantity": 2},
]

# Calculating total
total = 0.0  # Initialize as float for currency
for item in cart:
    item_total = item["price"] * item["quantity"]
    total += item_total

print(f"Cart Total: ${total:.2f}")  # .2f formats to 2 decimal places

# -------------------------------------------------------------------------
# Example 3: Temperature Converter
# -------------------------------------------------------------------------
print("\n--- Example 3: Temperature Converter ---")

def celsius_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit.
    
    SYNTAX: fahrenheit = celsius_to_fahrenheit(celsius)
    DESCRIPTION: Converts temperature from Celsius to Fahrenheit
    PARAMETERS:
        celsius (float/int): Temperature in Celsius
    RETURN VALUE:
        float: Temperature in Fahrenheit
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Using the function
temp_c = 100
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")


# =============================================================================
# SECTION 10: COMMON MISTAKES SUMMARY
# =============================================================================

"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                     COMMON MISTAKES TO AVOID                           ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                         ║
║  1. USING UNDEFINED VARIABLES                                           ║
║     ❌ print(my_variable)    # Error: 'my_variable' is not defined      ║
║     ✅ my_variable = "value" # Define before using!                    ║
║        print(my_variable)                                            ║
║                                                                         ║
║  2. CASE SENSITIVITY ERRORS                                             ║
║     ❌ Name = "Alice"; print(name)  # Error: 'name' not defined        ║
║     ✅ name = "Alice"; print(name)  # Use consistent casing           ║
║                                                                         ║
║  3. CONFUSING = (assignment) WITH == (comparison)                       ║
║     ❌ if name = "Alice":     # Error: assignment in condition         ║
║     ✅ if name == "Alice":    # Correct: comparison                    ║
║                                                                         ║
║  4. STRING VS NUMBER CONFUSION                                           ║
║     ❌ result = "5" + 5       # Error: can't add string and int        ║
║     ✅ result = int("5") + 5  # Convert string to int first           ║
║                                                                         ║
║  5. MUTABLE DEFAULT ARGUMENTS (advanced but important)                  ║
║     ❌ def func(my_list=[]):   # Dangerous! Same list reused           ║
║     ✅ def func(my_list=None): # Safe pattern                          ║
║            my_list = my_list or []                                      ║
║                                                                         ║
║  6. SHADOWING BUILT-IN NAMES                                            ║
║     ❌ list = [1,2,3]        # Now you can't use list() function!      ║
║     ✅ my_list = [1,2,3]     # Use a different name                    ║
║                                                                         ║
║  7. FORGETTING THAT LISTS ARE MUTABLE                                   ║
║     ❌ a = [1,2,3]; b = a; b[0] = 99  # Both a and b change!          ║
║     ✅ a = [1,2,3]; b = a.copy()       # Proper copy                  ║
║                                                                         ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""


# =============================================================================
# SECTION 11: QUICK REFERENCE CHEAT SHEET
# =============================================================================

"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                      PYTHON VARIABLES CHEAT SHEET                        ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                         ║
║  DATA TYPES:                                                            ║
║  ─────────────────────────────────────────────────────────────────────  ║
║  Type        Example              Mutable?   Description               ║
║  ─────────────────────────────────────────────────────────────────────  ║
║  int         42, -10, 0           No         Whole numbers             ║
║  float       3.14, -0.5, 2.5e4    No         Decimal numbers           ║
║  str         "hello", 'world'     No         Text                      ║
║  bool        True, False          No         Logical values            ║
║  list        [1, 2, 3]            Yes        Ordered collection        ║
║  tuple       (1, 2, 3)            No         Immutable collection      ║
║  dict        {"a": 1}             Yes        Key-value pairs           ║
║  set         {1, 2, 3}            Yes        Unique values only        ║
║  NoneType    None                 No         No value                  ║
║                                                                         ║
║  NAMING RULES:                                                          ║
║  ─────────────────────────────────────────────────────────────────────  ║
║  ✅ user_name, _private, CONSTANT_NAME, num2                            ║
║  ❌ 2name, user-name, class, user name                                  ║
║                                                                         ║
║  TYPE CONVERSION:                                                        ║
║  ─────────────────────────────────────────────────────────────────────  ║
║  int(x)     → Convert to integer                                        ║
║  float(x)   → Convert to float                                          ║
║  str(x)     → Convert to string                                         ║
║  bool(x)    → Convert to boolean                                        ║
║  list(x)    → Convert to list                                           ║
║  tuple(x)   → Convert to tuple                                          ║
║  set(x)     → Convert to set                                            ║
║                                                                         ║
║  USEFUL FUNCTIONS:                                                      ║
║  ─────────────────────────────────────────────────────────────────────  ║
║  type(x)           → Get the type of x                                  ║
║  isinstance(x, t)  → Check if x is type t (returns bool)                ║
║  id(x)             → Get memory address of x                             ║
║                                                                         ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""


# =============================================================================
# SECTION 12: SELF-TEST / EXERCISES
# =============================================================================

def test_your_knowledge():
    """
    Run this function to test your understanding of Python variables.
    Each print statement shows the answer - try to predict before running!
    """
    print("\n" + "="*60)
    print("VARIABLES KNOWLEDGE TEST")
    print("="*60)
    
    # Test 1: What will this print?
    x = 5
    y = x
    x = 10
    print(f"Test 1: y = {y}")  # Answer: y = 5 (y got the value, not reference to x)
    
    # Test 2: What type is this?
    value = [1, 2, 3]
    print(f"Test 2: type = {type(value)}")  # Answer: <class 'list'>
    
    # Test 3: What happens here?
    a, b = 1, 2, 3  # This will cause an ERROR!
    # Uncommenting above line causes: ValueError: too many values to unpack
    
    # Test 4: Is this True or False?
    print(f"Test 4: isinstance(42, (int, float)) = {isinstance(42, (int, float))}")
    # Answer: True (42 is an int, which is in the tuple of types)
    
    # Test 5: What's the difference?
    list1 = [1, 2, 3]
    list2 = list1
    list2.append(4)
    print(f"Test 5: list1 = {list1}")  # Answer: [1, 2, 3, 4] (same object!)
    
    print("\n" + "="*60)


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    """
    This code only runs when you execute this file directly.
    It won't run if this file is imported as a module.
    """
    print("="*60)
    print("PYTHON VARIABLES TUTORIAL")
    print("="*60)
    print("\nThis file demonstrates all Python variable types and concepts.")
    print("Read through the comments to learn each concept.")
    print("\nRun test_your_knowledge() to test yourself!")
    print("="*60)
    
    # Uncomment the line below to run the knowledge test:
    # test_your_knowledge()