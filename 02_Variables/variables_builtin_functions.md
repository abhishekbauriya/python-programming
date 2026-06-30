<div align="center">

# 🐍 Python Built-in Functions
### The Complete Beginner's Guide — all **71**, explained from zero

*No prior knowledge needed · No functions (`def`) used · Everyday examples only*

🟢 Beginner &nbsp;·&nbsp; 🟡 Intermediate &nbsp;·&nbsp; 🔴 Advanced

</div>

---

> 🧰 **Built-in functions** are ready-made tools that come with Python. You don't
> install or build them — you just type their name followed by `()`, like
> `print("hi")` or `len("cat")`. This guide explains all **71** of them, gently.

<br>

<table>
<tr>
<td>📘 <b>71</b><br>functions</td>
<td>🔰 <b>Beginner</b><br>friendly</td>
<td>🧪 <b>5 examples</b><br>per function</td>
<td>🛠️ <b>Mini project</b><br>per function</td>
<td>🚫 <b>No <code>def</code></b><br>anywhere</td>
</tr>
</table>

<br>

### 🚀 Start Here (the 15 you'll use most as a beginner)

New to Python? Don't read all 71 at once. Learn these first — they cover almost
everything you'll do early on:

> [`print`](#print) · [`input`](#input) · [`len`](#len) · [`type`](#type) · [`int`](#int) · [`float`](#float) · [`str`](#str) · [`bool`](#bool) · [`list`](#list) · [`dict`](#dict) · [`range`](#range) · [`sum`](#sum) · [`max`](#max) · [`min`](#min) · [`sorted`](#sorted)

<br>

### 🗺️ How each function is laid out (in reading order)

| # | Marker | Section | What it gives you |
|:--:|:--:|:--|:--|
| 1 | 🎯 | **Objective** | One-line summary — is this the tool you need? |
| 2 | 📋 | **Quick Facts** | Returns · Category · Related, at a glance |
| 3 | 📖 | **Description** | Plain-English meaning |
| 4 | 🏷️ | **Concepts** | Ideas it builds on |
| 5 | 🧭 | **What · Why · When · How** | The full picture, fast |
| 6 | ⌨️ | **Syntax** | The exact pattern to type |
| 7 | 🎛️ | **Parameters** | What goes inside the `()` |
| 8 | ↩️ | **Return Value** | What you get back |
| 9 | 🔍 | **Line-by-Line** | Every line of an example, explained |
| 10 | ▶️ | **Output** | What prints, and why |
| 11 | ⚙️ | **Internal Working** | What Python does behind the scenes |
| 12 | ⚠️ | **Common Mistakes** | Traps to avoid |
| 13 | 💡 | **Hint** | A memory tip |
| 14 | 📚 | **5 Examples** | Five quick ones *(click to expand)* |
| 15 | 🛠️ | **Mini Project** | A tiny real program + a challenge *(click to expand)* |
| 16 | 🔗 | **See Also** | Related functions to explore next |

> ▶️ **To run any example:** save it in a file like `test.py` and run
> `python test.py`, or type it line by line at the Python prompt.

<br>

## 📋 Table of Contents

<table>
<tr><td><b>A–B</b></td><td>

[`abs`](#abs) · [`aiter`](#aiter) · [`all`](#all) · [`anext`](#anext) · [`any`](#any) · [`ascii`](#ascii) · [`bin`](#bin) · [`bool`](#bool) · [`breakpoint`](#breakpoint) · [`bytearray`](#bytearray) · [`bytes`](#bytes)

</td></tr>
<tr><td><b>C–D</b></td><td>

[`callable`](#callable) · [`chr`](#chr) · [`classmethod`](#classmethod) · [`compile`](#compile) · [`complex`](#complex) · [`delattr`](#delattr) · [`dict`](#dict) · [`dir`](#dir) · [`divmod`](#divmod)

</td></tr>
<tr><td><b>E–F</b></td><td>

[`enumerate`](#enumerate) · [`eval`](#eval) · [`exec`](#exec) · [`filter`](#filter) · [`float`](#float) · [`format`](#format) · [`frozenset`](#frozenset)

</td></tr>
<tr><td><b>G–H</b></td><td>

[`getattr`](#getattr) · [`globals`](#globals) · [`hasattr`](#hasattr) · [`hash`](#hash) · [`help`](#help) · [`hex`](#hex)

</td></tr>
<tr><td><b>I</b></td><td>

[`id`](#id) · [`input`](#input) · [`int`](#int) · [`isinstance`](#isinstance) · [`issubclass`](#issubclass) · [`iter`](#iter)

</td></tr>
<tr><td><b>L–N</b></td><td>

[`len`](#len) · [`list`](#list) · [`locals`](#locals) · [`map`](#map) · [`max`](#max) · [`memoryview`](#memoryview) · [`min`](#min) · [`next`](#next)

</td></tr>
<tr><td><b>O–R</b></td><td>

[`object`](#object) · [`oct`](#oct) · [`open`](#open) · [`ord`](#ord) · [`pow`](#pow) · [`print`](#print) · [`property`](#property) · [`range`](#range) · [`repr`](#repr) · [`reversed`](#reversed) · [`round`](#round)

</td></tr>
<tr><td><b>S</b></td><td>

[`set`](#set) · [`setattr`](#setattr) · [`slice`](#slice) · [`sorted`](#sorted) · [`staticmethod`](#staticmethod) · [`str`](#str) · [`sum`](#sum) · [`super`](#super)

</td></tr>
<tr><td><b>T–Z</b></td><td>

[`tuple`](#tuple) · [`type`](#type) · [`vars`](#vars) · [`zip`](#zip) · [`__import__`](#__import__)

</td></tr>
</table>

---

<a id="abs"></a>
## 🔢 `abs()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Get the size of a number, ignoring whether it's positive or negative.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A number, always ≥ 0 | Numbers | `round()` · `pow()` · `min()` · `max()` |

📖 **Description** — `abs()` gives the *absolute value* of a number: how far it is from zero. The answer is always zero or positive.

🏷️ **Concepts** — `numbers` · `positive / negative` · `return values`

🧭 **What · Why · When · How**
- **What** — removes the minus sign (`-7` → `7`).
- **Why** — sometimes you care about *size/distance*, not direction.
- **When** — when a result must not be negative (like a difference).
- **How** — put a number in the brackets: `abs(number)`.

⌨️ **Syntax**
```python
abs(number)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `number` | the number to measure (int, float, or complex) | ✅ Yes |

↩️ **Return Value** — a number (int or float), always ≥ 0.

🔍 **Line-by-Line Explanation**
```python
x = -7           # store the negative number -7
result = abs(x)  # remove the sign, so result becomes 7
print(result)    # show the result on screen
```
> • `x = -7` — save `-7` into `x`
> • `result = abs(x)` — turns `-7` into `7`
> • `print(result)` — displays `7`

▶️ **Output & Output Explanation**
```text
7
```
`-7` is 7 steps away from zero, so the answer is `7`.

⚙️ **Internal Working** — Python checks the sign. If negative, it returns the positive version; if already zero or positive, it returns it unchanged.

⚠️ **Common Mistakes & Errors**
> `abs("5")` → **TypeError**. It needs a number, not text. Convert first: `abs(int("5"))`.

💡 **Hint**
> Think **"distance from zero"** — distances are never negative.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(abs(-3))       # 3   -> minus sign removed
print(abs(3))        # 3   -> already positive, unchanged
print(abs(-2.5))     # 2.5 -> works on decimals too
print(abs(0))        # 0   -> zero stays zero
print(abs(10 - 15))  # 5   -> 10-15 is -5, abs makes it 5
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Temperature Difference</b></summary>

```python
morning = 12                       # morning temperature
night = 5                          # night temperature
difference = abs(morning - night)  # always-positive difference
print(f"The temperature changed by {difference} degrees")
```
**Output:** `The temperature changed by 7 degrees`
Even if night were warmer, `abs()` keeps the difference positive.

✏️ **Your turn:** swap the two numbers (`morning = 5`, `night = 12`) and confirm the answer is still `7`.
</details>

🔗 **See Also** — `round()` · `pow()` · `min()` · `max()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="aiter"></a>
## ⚡ `aiter()` &nbsp;<sub>🔴 Advanced</sub>

> 🎯 **Objective —** Get an *async iterator* from an async collection. *(Beginners can safely skip this one.)*

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| An async iterator | Async (advanced) | `iter()` · `anext()` · `next()` |

📖 **Description** — `aiter()` is the async (asynchronous) version of `iter()`. It's used only in advanced "async" programs, where code can wait for slow things without freezing. You'll almost never need it as a beginner.

🏷️ **Concepts** — `async programming` · `iterators` *(advanced)*

🧭 **What · Why · When · How**
- **What** — returns an async iterator for an async iterable.
- **Why** — so async code can step through items one at a time.
- **When** — only inside advanced `async` programs.
- **How** — `aiter(async_iterable)`, inside async code.

⌨️ **Syntax**
```python
aiter(async_iterable)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `async_iterable` | an object built for async iteration | ✅ Yes |

↩️ **Return Value** — an async iterator object.

🔍 **Line-by-Line Explanation**
```python
# Conceptual — only works inside an 'async' program:
# it = aiter(some_async_source)   # get an async iterator
# value = await anext(it)         # await the next item (see anext)
```
> • The idea: get an async iterator, then `await` items from it.

▶️ **Output & Output Explanation** — no simple beginner output; it's only meaningful inside async programs.

⚙️ **Internal Working** — it calls the object's special `__aiter__` method, which hands back an async iterator.

⚠️ **Common Mistakes & Errors**
> Using `aiter()` on a normal list → **TypeError** (lists aren't *async*; use `iter()`).

💡 **Hint**
> If you don't know what `async` means yet, you don't need `aiter()` yet.

<details>
<summary>📚 <b>5 Examples</b> (all conceptual)</summary>

```python
# 1. it = aiter(async_source)     # get an async iterator
# 2. # used with: await anext(it)
# 3. # the normal-code version is: iter(my_list)
# 4. # aiter(my_list) would ERROR (list is not async)
# 5. # you'll meet this only after learning 'async def'
```
</details>

<details>
<summary>🛠️ <b>Mini Project</b></summary>

*Not beginner-appropriate — `aiter()` requires async programming. Use `iter()` for everyday code instead.*
</details>

🔗 **See Also** — `iter()` · `anext()` · `next()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="all"></a>
## ✅ `all()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Check whether *every* item in a group is true.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| `True` or `False` | Logic | `any()` · `bool()` · `filter()` |

📖 **Description** — `all()` returns `True` only if *every* item in a collection is "truthy". If even one item is false, it returns `False`.

🏷️ **Concepts** — `booleans (True/False)` · `lists` · `truthiness`

🧭 **What · Why · When · How**
- **What** — answers: "Are they **all** true?"
- **Why** — to check many conditions at once.
- **When** — when something must be true for *all* items.
- **How** — `all(my_list)`.

⌨️ **Syntax**
```python
all(iterable)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `iterable` | a list/tuple/etc. of values to check | ✅ Yes |

↩️ **Return Value** — `True` or `False`.

🔍 **Line-by-Line Explanation**
```python
checks = [True, True, False]  # three True/False values
result = all(checks)          # True only if EVERY item is True
print(result)                 # one is False -> prints False
```
> • a list containing a `False`
> • `all()` sees the `False` → `False`
> • prints `False`

▶️ **Output & Output Explanation**
```text
False
```
One value is `False`, so not every item is true → `False`.

⚙️ **Internal Working** — Python checks items one by one; the moment it finds a false one it stops and returns `False`. If none are false, it returns `True`.

⚠️ **Common Mistakes & Errors**
> `all([])` on an **empty** list returns `True` (there are no false items) — this can surprise you.

💡 **Hint**
> Read it as **"all of them?"** — needs *everything* true.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(all([True, True, True]))   # True  -> every item is True
print(all([True, False, True]))  # False -> one item is False
print(all([1, 2, 3]))            # True  -> all non-zero are truthy
print(all([1, 0, 3]))            # False -> 0 counts as false
print(all([]))                   # True  -> empty: nothing is false
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Did Everyone Pass?</b></summary>

```python
scores = [55, 72, 90, 48]                          # four test scores
all_passed = all(score >= 50 for score in scores)  # True only if every score >= 50
print(f"Everyone passed: {all_passed}")
```
**Output:** `Everyone passed: False`
One score (48) is below 50, so not all passed.

✏️ **Your turn:** change the `48` to `80` and re-run — now everyone passes (`True`).
</details>

🔗 **See Also** — `any()` · `bool()` · `filter()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="anext"></a>
## ⚡ `anext()` &nbsp;<sub>🔴 Advanced</sub>

> 🎯 **Objective —** Get the *next* item from an async iterator. *(Beginners can safely skip.)*

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| An awaitable (next item) | Async (advanced) | `next()` · `aiter()` · `iter()` |

📖 **Description** — `anext()` is the async version of `next()`. Like `aiter()`, it's only for advanced "async" programs and isn't needed by beginners.

🏷️ **Concepts** — `async programming` · `iterators` *(advanced)*

🧭 **What · Why · When · How**
- **What** — fetches the next item from an async iterator (you must `await` it).
- **Why** — so async code can pull items one at a time.
- **When** — only inside advanced `async` programs.
- **How** — `await anext(async_iterator)`.

⌨️ **Syntax**
```python
anext(async_iterator)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `async_iterator` | an async iterator (from `aiter()`) | ✅ Yes |
| `default` | a value to return if it's exhausted | ⬜ Optional |

↩️ **Return Value** — an awaitable that gives the next item.

🔍 **Line-by-Line Explanation**
```python
# Conceptual — works inside an 'async' program:
# it = aiter(async_source)   # get an async iterator
# value = await anext(it)    # await the next item from it
```
> • Pair `anext()` with `aiter()` inside async code.

▶️ **Output & Output Explanation** — no simple beginner output; only meaningful in async programs.

⚙️ **Internal Working** — it calls the iterator's special `__anext__` method, returning an "awaitable" for the next value.

⚠️ **Common Mistakes & Errors**
> Using `anext()` on a normal iterator → **TypeError**. Use `next()` for ordinary code.

💡 **Hint**
> It's just **"async next"**. If `async` is new to you, use `next()`.

<details>
<summary>📚 <b>5 Examples</b> (conceptual)</summary>

```python
# 1. value = await anext(it)       # get the next async item
# 2. # the normal-code version is: next(my_iterator)
# 3. # anext(my_list_iterator) would ERROR (not async)
# 4. # used together with aiter()
# 5. # appears only after you learn 'async def'
```
</details>

<details>
<summary>🛠️ <b>Mini Project</b></summary>

*Not beginner-appropriate — needs async programming. Use `next()` for everyday code.*
</details>

🔗 **See Also** — `next()` · `aiter()` · `iter()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="any"></a>
## ✅ `any()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Check whether *at least one* item in a group is true.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| `True` or `False` | Logic | `all()` · `bool()` · `filter()` |

📖 **Description** — `any()` returns `True` if *any* single item is truthy. It returns `False` only if *every* item is false.

🏷️ **Concepts** — `booleans` · `lists` · `truthiness`

🧭 **What · Why · When · How**
- **What** — answers: "Is **at least one** true?"
- **Why** — to check if something is true *somewhere* in a group.
- **When** — when just one match is enough.
- **How** — `any(my_list)`.

⌨️ **Syntax**
```python
any(iterable)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `iterable` | a list/tuple/etc. of values to check | ✅ Yes |

↩️ **Return Value** — `True` or `False`.

🔍 **Line-by-Line Explanation**
```python
checks = [False, False, True]  # one True at the end
result = any(checks)           # True if AT LEAST ONE item is True
print(result)                  # there is one True -> prints True
```
> • a list with a single `True`
> • `any()` finds it → `True`
> • prints `True`

▶️ **Output & Output Explanation**
```text
True
```
One item is `True`, and `any()` needs only one → `True`.

⚙️ **Internal Working** — Python checks items one by one; the moment it finds a true one it stops and returns `True`. If none are true, it returns `False`.

⚠️ **Common Mistakes & Errors**
> `any([])` returns `False`. Also: don't confuse `any` (at least one) with `all` (every one).

💡 **Hint**
> Read it as **"any of them?"** — needs *just one* true.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(any([False, False, True]))  # True  -> one item is True
print(any([False, False]))        # False -> none are True
print(any([0, 0, 5]))             # True  -> 5 is truthy
print(any([0, 0, 0]))             # False -> all zeros are falsy
print(any([]))                    # False -> empty: nothing true
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Did Anyone Pass?</b></summary>

```python
scores = [40, 35, 60, 20]                              # four scores
someone_passed = any(score >= 50 for score in scores)  # True if any score >= 50
print(f"Someone passed: {someone_passed}")
```
**Output:** `Someone passed: True`
One score (60) is 50 or higher, so `any()` returns `True`.

✏️ **Your turn:** change all scores to be below 50 and watch the answer become `False`.
</details>

🔗 **See Also** — `all()` · `bool()` · `filter()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="ascii"></a>
## 🔤 `ascii()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Show a value with any "unusual" characters written as safe codes.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A string (text) | Text | `repr()` · `ord()` · `chr()` · `str()` |

📖 **Description** — `ascii()` returns a printable version of a value where characters outside basic English (like `é`, `π`, emojis) appear as escape codes (e.g. `\xe9`).

🏷️ **Concepts** — `strings` · `characters` · `escape codes`

🧭 **What · Why · When · How**
- **What** — turns "fancy" characters into plain codes.
- **Why** — to safely *see* exactly what characters are in some text.
- **When** — when checking text that may contain accents or symbols.
- **How** — `ascii(value)`.

⌨️ **Syntax**
```python
ascii(object)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `object` | any value you want to inspect | ✅ Yes |

↩️ **Return Value** — a string, with quotes shown around text.

🔍 **Line-by-Line Explanation**
```python
word = "café"        # text containing the accented letter é
safe = ascii(word)   # turn é into its escape code \xe9
print(safe)          # show the safe version
```
> • store text with an accent
> • `ascii()` replaces `é` with `\xe9`
> • prints `'caf\xe9'`

▶️ **Output & Output Explanation**
```text
'caf\xe9'
```
Plain letters stay; `é` becomes `\xe9`. The quotes show it's text.

⚙️ **Internal Working** — works like `repr()` but replaces every non-ASCII character with a `\x`, `\u`, or `\U` escape code.

⚠️ **Common Mistakes & Errors**
> Expecting it to *remove* accents — it doesn't; it shows them as codes.

💡 **Hint**
> "ascii" = the basic A–Z set; anything else gets a code.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(ascii("hello"))    # 'hello'       -> plain text, unchanged
print(ascii("café"))     # 'caf\xe9'     -> é becomes a code
print(ascii("π"))        # '\u03c0'      -> the pi symbol as a code
print(ascii(123))        # 123           -> numbers shown plainly
print(ascii(["a", "é"])) # ['a', '\xe9'] -> works inside lists too
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Reveal Hidden Characters</b></summary>

```python
name = "Renée"                  # a name with an accented letter
print(f"Normal: {name}")        # shows the name as usual
print(f"Safe:   {ascii(name)}") # shows the accent as an escape code
```
**Output:**
```text
Normal: Renée
Safe:   'Ren\xe9e'
```
`ascii()` reveals that the `é` is really the code `\xe9`.

✏️ **Your turn:** try your own name, or a word with an emoji, and see the codes.
</details>

🔗 **See Also** — `repr()` · `ord()` · `chr()` · `str()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="bin"></a>
## 🔢 `bin()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Show a whole number in *binary* (base-2: only 0s and 1s).

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A string starting with `0b` | Numbers | `hex()` · `oct()` · `int()` · `format()` |

📖 **Description** — `bin()` converts a whole number into its binary text form, starting with `0b` to mark it as binary.

🏷️ **Concepts** — `numbers` · `binary (base-2)` · `strings`

🧭 **What · Why · When · How**
- **What** — turns `5` into `'0b101'`.
- **Why** — computers store numbers in binary; this lets you see it.
- **When** — learning how numbers work, or low-level number tasks.
- **How** — `bin(whole_number)`.

⌨️ **Syntax**
```python
bin(integer)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `integer` | a whole number (no decimals) | ✅ Yes |

↩️ **Return Value** — a string starting with `0b`.

🔍 **Line-by-Line Explanation**
```python
number = 5            # the whole number five
binary = bin(number)  # convert to binary text: '0b101'
print(binary)         # show the binary form
```
> • store `5`
> • `bin()` gives `'0b101'` (5 = 4 + 1)
> • prints `0b101`

▶️ **Output & Output Explanation**
```text
0b101
```
`101` in binary means 4 + 0 + 1 = 5.

⚙️ **Internal Working** — Python repeatedly divides the number by 2, collecting remainders, then writes them as 0s and 1s with a `0b` prefix.

⚠️ **Common Mistakes & Errors**
> `bin(3.5)` → **TypeError**. It needs a *whole* number, not a decimal.

💡 **Hint**
> The `0b` at the start just means "this is binary".

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(bin(2))    # 0b10       -> 2
print(bin(10))   # 0b1010     -> 8 + 2 = 10
print(bin(0))    # 0b0        -> zero
print(bin(255))  # 0b11111111 -> all ones (255)
print(bin(1))    # 0b1        -> one
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Number in Binary</b></summary>

```python
age = 9                                   # any whole number
print(f"{age} in binary is {bin(age)}")   # show its binary form
```
**Output:** `9 in binary is 0b1001`
`1001` in binary is 8 + 0 + 0 + 1 = 9.

✏️ **Your turn:** print the binary of `4`, `8`, and `16` — notice the pattern of zeros.
</details>

🔗 **See Also** — `hex()` · `oct()` · `int()` · `format()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="bool"></a>
## 🔘 `bool()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Turn any value into `True` or `False`.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| `True` or `False` | Logic | `int()` · `all()` · `any()` |

📖 **Description** — `bool()` decides whether a value is "truthy" (`True`) or "falsy" (`False`). Empty things and zero are `False`; everything else is `True`.

🏷️ **Concepts** — `booleans` · `truthiness` · `type conversion`

🧭 **What · Why · When · How**
- **What** — converts a value to `True` or `False`.
- **Why** — to check if something is "empty" or "has something in it".
- **When** — when testing whether a value counts as true.
- **How** — `bool(value)`.

⌨️ **Syntax**
```python
bool(value)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `value` | any value to test (defaults to `False` if left empty) | ⬜ Optional |

↩️ **Return Value** — `True` or `False`.

🔍 **Line-by-Line Explanation**
```python
name = ""              # an empty piece of text
has_name = bool(name)  # empty text is falsy -> False
print(has_name)        # show the result
```
> • `name` is empty text
> • `bool("")` is `False`
> • prints `False`

▶️ **Output & Output Explanation**
```text
False
```
The text is empty, and empty text counts as `False`.

⚙️ **Internal Working** — Python asks the value if it's "empty/zero". `0`, `0.0`, `""`, `[]`, `{}`, `None` are `False`; everything else is `True`.

⚠️ **Common Mistakes & Errors**
> `bool("False")` is **True**! Any *non-empty* text is truthy — even the word "False".

💡 **Hint**
> Empty or zero → `False`. Anything with "stuff" in it → `True`.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(bool(0))      # False -> zero is falsy
print(bool(7))      # True  -> any non-zero number is truthy
print(bool(""))     # False -> empty text is falsy
print(bool("hi"))   # True  -> non-empty text is truthy
print(bool([]))     # False -> empty list is falsy
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Is the Cart Empty?</b></summary>

```python
cart = []                 # an empty shopping cart (a list)
has_items = bool(cart)    # empty list -> False
print(f"Cart has items: {has_items}")
```
**Output:** `Cart has items: False`
The list is empty, so `bool()` returns `False`. Add an item and it becomes `True`.

✏️ **Your turn:** put one item in the cart (e.g. `["apple"]`) and re-run.
</details>

🔗 **See Also** — `int()` · `all()` · `any()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="breakpoint"></a>
## 🐞 `breakpoint()` &nbsp;<sub>🔴 Advanced</sub>

> 🎯 **Objective —** Pause a running program so you can inspect it (debugging). *(Advanced — beginners can skip.)*

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| Nothing (`None`) | Debugging (advanced) | `help()` · `dir()` · `print()` |

📖 **Description** — `breakpoint()` stops your program at that line and opens Python's debugger, letting you look at variables step by step. As a beginner, using `print()` to check values is simpler.

🏷️ **Concepts** — `debugging` · `pausing code` *(advanced)*

🧭 **What · Why · When · How**
- **What** — pauses the program and opens an interactive debugger.
- **Why** — to inspect what's happening when something goes wrong.
- **When** — debugging tricky bugs (a later skill).
- **How** — write `breakpoint()` on its own line.

⌨️ **Syntax**
```python
breakpoint()
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| *(none)* | takes no arguments in normal use | — |

↩️ **Return Value** — nothing (`None`); it pauses execution instead.

🔍 **Line-by-Line Explanation**
```python
x = 10
# breakpoint()   # if you remove the '#', the program pauses here
print(x)         # you'd inspect x in the debugger, then continue
```
> • when reached, `breakpoint()` opens a debugger prompt
> • you can type variable names to inspect them, then continue

▶️ **Output & Output Explanation** — no normal output; it opens an interactive debugger prompt (`(Pdb)`).

⚙️ **Internal Working** — it calls `sys.breakpointhook()`, which by default starts Python's built-in debugger, `pdb`.

⚠️ **Common Mistakes & Errors**
> Leaving `breakpoint()` in code you share — it will pause for anyone who runs it. Remove it when done.

💡 **Hint**
> As a beginner, prefer `print()` to peek at values. Save `breakpoint()` for later.

<details>
<summary>📚 <b>5 Examples</b> (conceptual)</summary>

```python
# 1. breakpoint()            # pause here and open the debugger
# 2. # at the (Pdb) prompt, type a variable name to see its value
# 3. # type 'c' (continue) to resume the program
# 4. # type 'q' (quit) to stop
# 5. # beginners can use print() instead for now
```
</details>

<details>
<summary>🛠️ <b>Mini Project</b></summary>

*Not beginner-appropriate — `breakpoint()` opens an interactive debugger. Use `print()` to inspect values for now.*
</details>

🔗 **See Also** — `help()` · `dir()` · `print()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="bytearray"></a>
## 🧱 `bytearray()` &nbsp;<sub>🟡 Intermediate</sub>

> 🎯 **Objective —** Make a *changeable* sequence of bytes (small numbers 0–255).

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A bytearray | Binary data | `bytes()` · `memoryview()` · `list()` |

📖 **Description** — A `bytearray` is like a list of small numbers (0–255), often used to represent raw data. Unlike `bytes`, it **can be changed** after you make it.

🏷️ **Concepts** — `bytes` · `raw data` · `mutable (changeable)`

🧭 **What · Why · When · How**
- **What** — builds an editable block of bytes.
- **Why** — when you need to *modify* raw data byte by byte.
- **When** — working with files, images, or network data (later topics).
- **How** — `bytearray(source)`.

⌨️ **Syntax**
```python
bytearray(source)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `source` | bytes like `b"abc"`, a list of 0–255, or a count | ⬜ Optional |

↩️ **Return Value** — a `bytearray` object (editable).

🔍 **Line-by-Line Explanation**
```python
data = bytearray(b"abc")  # make an editable copy of the bytes a, b, c
print(data)               # show it -> bytearray(b'abc')
print(list(data))         # the numbers behind the letters -> [97, 98, 99]
```
> • `bytearray(b"abc")` builds editable bytes
> • printing shows `bytearray(b'abc')`
> • each letter has a number (a=97, b=98, c=99)

▶️ **Output & Output Explanation**
```text
bytearray(b'abc')
[97, 98, 99]
```
The letters `a`, `b`, `c` are stored as the numbers `97`, `98`, `99`.

⚙️ **Internal Working** — Python keeps a resizable array of bytes in memory; because it's mutable, you can change individual positions.

⚠️ **Common Mistakes & Errors**
> Putting a number above 255 in it → **ValueError**. Each byte must be 0–255.

💡 **Hint**
> Think "a list of small numbers (0–255) that you can edit".

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(bytearray(b"hi"))       # bytearray(b'hi')
print(bytearray(3))           # bytearray(b'\x00\x00\x00') -> 3 zero bytes
print(list(bytearray(b"AB"))) # [65, 66]
ba = bytearray(b"cat"); ba[0] = 98; print(ba)  # bytearray(b'bat') -> editable!
print(bytearray([72, 73]))    # bytearray(b'HI')
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Editable Bytes</b></summary>

```python
data = bytearray(b"cat")   # start with the bytes for "cat"
data[0] = ord("b")         # change the first byte to 'b' (ord('b') is 98)
print(data.decode())       # turn it back into text
```
**Output:** `bat`
We changed the first byte, so "cat" became "bat" — possible only because bytearray is editable.

✏️ **Your turn:** change the last byte to `ord("p")` and see the result.
</details>

🔗 **See Also** — `bytes()` · `memoryview()` · `list()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="bytes"></a>
## 🔒 `bytes()` &nbsp;<sub>🟡 Intermediate</sub>

> 🎯 **Objective —** Make a *fixed* (unchangeable) sequence of bytes.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A bytes object | Binary data | `bytearray()` · `str()` · `ord()` |

📖 **Description** — `bytes` is like `bytearray` but **cannot be changed** once made. It's how Python represents raw data (e.g. the contents of a file) that shouldn't be edited in place.

🏷️ **Concepts** — `bytes` · `raw data` · `immutable (fixed)`

🧭 **What · Why · When · How**
- **What** — builds a fixed block of bytes.
- **Why** — to safely hold raw data that shouldn't change.
- **When** — files, networks, encoding text (later topics).
- **How** — `bytes(source)` or write `b"..."`.

⌨️ **Syntax**
```python
bytes(source)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `source` | text + encoding, a list of 0–255, or a count | ⬜ Optional |

↩️ **Return Value** — a `bytes` object (fixed).

🔍 **Line-by-Line Explanation**
```python
data = bytes("hi", "utf-8")  # turn the text "hi" into bytes
print(data)                  # show it -> b'hi'
print(data.decode("utf-8"))  # turn bytes back into text -> hi
```
> • `bytes("hi", "utf-8")` encodes the text as bytes
> • printing shows `b'hi'` (the `b` means "bytes")
> • `.decode()` turns it back into the text `hi`

▶️ **Output & Output Explanation**
```text
b'hi'
hi
```
The `b'...'` form shows raw bytes; decoding turns them back into readable text.

⚙️ **Internal Working** — Python stores a read-only array of bytes. Any "change" actually makes a new bytes object.

⚠️ **Common Mistakes & Errors**
> `bytes("hi")` without an encoding → **TypeError**. Add one: `bytes("hi", "utf-8")`.

💡 **Hint**
> The `b` before quotes (`b"hi"`) is the quick way to write bytes.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(bytes("hi", "utf-8"))  # b'hi'
print(b"abc")                # b'abc'  -> the shortcut form
print(bytes([72, 73]))       # b'HI'   -> from numbers
print(bytes(3))              # b'\x00\x00\x00' -> 3 zero bytes
print(b"hi".decode("utf-8")) # hi      -> bytes back to text
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Text to Bytes and Back</b></summary>

```python
message = "Hello"                  # some text
raw = message.encode("utf-8")      # text -> bytes
print(f"As bytes: {raw}")
print(f"Back to text: {raw.decode('utf-8')}")
```
**Output:**
```text
As bytes: b'Hello'
Back to text: Hello
```
Text becomes bytes for storage/sending, then decodes back to text.

✏️ **Your turn:** try a message with a space or an emoji and watch the bytes.
</details>

🔗 **See Also** — `bytearray()` · `str()` · `ord()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

# C – D

<a id="callable"></a>
## 📞 `callable()` &nbsp;<sub>🟡 Intermediate</sub>

> 🎯 **Objective —** Check whether something can be "called" (used with `()`).

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| `True` or `False` | Inspection | `type()` · `hasattr()` · `isinstance()` |

📖 **Description** — `callable()` tells you if an object can be used like a function — that is, whether you can put `()` after it to run it.

🏷️ **Concepts** — `functions` · `calling with ()` · `booleans`

🧭 **What · Why · When · How**
- **What** — answers: "Can I put `()` after this?"
- **Why** — to avoid the error of calling something that isn't callable.
- **When** — when you're unsure if a value is a function/tool.
- **How** — `callable(thing)`.

⌨️ **Syntax**
```python
callable(object)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `object` | the thing to test | ✅ Yes |

↩️ **Return Value** — `True` (can be called) or `False` (cannot).

🔍 **Line-by-Line Explanation**
```python
print(callable(print))  # print is a function -> True
print(callable(5))      # 5 is just a number -> False
```
> • `print` is a function, so adding `()` works → `True`
> • `5` is a number; `5()` would error → `False`

▶️ **Output & Output Explanation**
```text
True
False
```
Functions are callable; plain values like numbers are not.

⚙️ **Internal Working** — Python checks if the object has a special `__call__` method. Functions and types have it; numbers and strings don't.

⚠️ **Common Mistakes & Errors**
> Calling a non-callable, like `5()`, gives a **TypeError**. Use `callable()` first if unsure.

💡 **Hint**
> "callable" = "can I add `()` to run it?"

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(callable(print))  # True  -> a function
print(callable(len))    # True  -> a function
print(callable(list))   # True  -> a type can be called to build a list
print(callable("hi"))   # False -> text is not callable
print(callable(5))      # False -> a number is not callable
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Safe to Call?</b></summary>

```python
thing = len                       # try changing this to 5 or "hi"
if callable(thing):               # only call it if it's callable
    print("Yes, you can call it")
else:
    print("No, that can't be called")
```
**Output:** `Yes, you can call it`
`len` is a function, so it's callable.

✏️ **Your turn:** set `thing = 42` and re-run — the message flips.
</details>

🔗 **See Also** — `type()` · `hasattr()` · `isinstance()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="chr"></a>
## 🔡 `chr()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Turn a number into the character it represents.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A single-character string | Text | `ord()` · `ascii()` · `str()` |

📖 **Description** — Every character has a number (its Unicode "code point"). `chr()` takes a number and gives back the matching character.

🏷️ **Concepts** — `characters` · `Unicode numbers` · `strings`

🧭 **What · Why · When · How**
- **What** — number → character (e.g. `65` → `'A'`).
- **Why** — to build characters from their codes.
- **When** — simple ciphers, generating letters, learning text encoding.
- **How** — `chr(number)`.

⌨️ **Syntax**
```python
chr(number)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `number` | a whole number (a Unicode code point) | ✅ Yes |

↩️ **Return Value** — a string of exactly one character.

🔍 **Line-by-Line Explanation**
```python
code = 65         # the number 65
letter = chr(code)  # 65 maps to the character 'A'
print(letter)     # show the character
```
> • store `65`
> • `chr(65)` gives `'A'`
> • prints `A`

▶️ **Output & Output Explanation**
```text
A
```
The code `65` stands for the capital letter `A`.

⚙️ **Internal Working** — Python looks up the number in the Unicode table and returns the character stored at that position.

⚠️ **Common Mistakes & Errors**
> `chr("65")` → **TypeError**. It needs a number, not text. (`chr()` is the opposite of `ord()`.)

💡 **Hint**
> `chr` = "character from a number". Its partner `ord` goes the other way.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(chr(65))    # A   -> capital A
print(chr(97))    # a   -> small a
print(chr(48))    # 0   -> the digit zero (as text)
print(chr(8364))  # €   -> the euro sign
print(chr(126))   # ~   -> the tilde symbol
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Build a Word From Codes</b></summary>

```python
word = chr(72) + chr(73)   # 72 -> H, 73 -> I
print(f"The secret word is: {word}")
```
**Output:** `The secret word is: HI`
Each number becomes a letter, and `+` joins them into a word.

✏️ **Your turn:** spell your initials using `chr()` (e.g. `A` is 65, `B` is 66 …).
</details>

🔗 **See Also** — `ord()` · `ascii()` · `str()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="classmethod"></a>
## 🏛️ `classmethod()` &nbsp;<sub>🔴 Advanced</sub>

> 🎯 **Objective —** Mark a function inside a class as belonging to the *class itself*. *(Needs classes — beginners can skip.)*

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A class method | Classes (advanced) | `staticmethod()` · `property()` · `super()` |

📖 **Description** — `classmethod()` is used *inside classes* (usually as the `@classmethod` decorator). Since classes use `def`, this is beyond beginner scope — you'll learn it after functions and classes.

🏷️ **Concepts** — `classes` · `methods` *(advanced)*

🧭 **What · Why · When · How**
- **What** — turns a method into one tied to the class, not a single object.
- **Why** — to make helper "builder" methods on a class.
- **When** — only when writing classes (a later topic).
- **How** — written as `@classmethod` above a method (needs `def`).

⌨️ **Syntax**
```python
# Used as a decorator inside a class (needs def + class):
# @classmethod
# def make(cls): ...
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `function` | the method to convert | ✅ Yes |

↩️ **Return Value** — a class-method object.

🔍 **Line-by-Line Explanation**
```python
# Conceptual — requires a class (which uses def):
# class Dog:
#     @classmethod
#     def species(cls):
#         return "Canine"
```
> • The idea: `species` belongs to the whole `Dog` class, not one dog.

▶️ **Output & Output Explanation** — no simple beginner output; it only makes sense inside a class.

⚙️ **Internal Working** — it wraps the function so that, when called, Python passes the *class* (as `cls`) instead of an instance.

⚠️ **Common Mistakes & Errors**
> Trying to use it outside a class. It only has meaning *inside* a `class` block.

💡 **Hint**
> Skip this until you've learned `def` and `class`. Then it'll click.

<details>
<summary>📚 <b>5 Examples</b> (conceptual — need a class)</summary>

```python
# 1. @classmethod above a method makes it a class method
# 2. it receives 'cls' (the class) automatically
# 3. often used to build objects in different ways
# 4. partner concepts: staticmethod, property
# 5. you'll use it after learning classes
```
</details>

<details>
<summary>🛠️ <b>Mini Project</b></summary>

*Not beginner-appropriate — needs classes (`def`/`class`). Revisit this after the classes chapter.*
</details>

🔗 **See Also** — `staticmethod()` · `property()` · `super()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="compile"></a>
## 🧩 `compile()` &nbsp;<sub>🔴 Advanced</sub>

> 🎯 **Objective —** Turn a string of Python code into something Python can run later. *(Advanced — beginners can skip.)*

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A code object | Advanced | `eval()` · `exec()` |

📖 **Description** — `compile()` prepares Python *code written as text* so it can be run by `eval()` or `exec()`. It's an advanced, rarely-needed tool, and beginners won't use it.

🏷️ **Concepts** — `code as text` · `running code` *(advanced)*

🧭 **What · Why · When · How**
- **What** — converts code-in-a-string into a runnable "code object".
- **Why** — to run code that is built or loaded as text.
- **When** — advanced tools only; almost never as a beginner.
- **How** — `compile(source, filename, mode)`.

⌨️ **Syntax**
```python
compile(source, filename, mode)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `source` | the code, as text | ✅ Yes |
| `filename` | a name for error messages (any text) | ✅ Yes |
| `mode` | `"eval"`, `"exec"`, or `"single"` | ✅ Yes |

↩️ **Return Value** — a code object (you then run it with `eval`/`exec`).

🔍 **Line-by-Line Explanation**
```python
code = compile("2 + 3", "<demo>", "eval")  # prepare the expression 2 + 3
print(eval(code))                          # run it -> 5
```
> • `compile(...)` turns the text `"2 + 3"` into runnable code
> • `eval(code)` runs it and gives `5`

▶️ **Output & Output Explanation**
```text
5
```
The text `"2 + 3"` was compiled, then run, producing `5`.

⚙️ **Internal Working** — Python parses the text into an internal tree and turns it into bytecode (the low-level instructions Python actually runs).

⚠️ **Common Mistakes & Errors**
> Wrong `mode` (e.g. using `"eval"` for a statement like `x = 5`) → **SyntaxError**. Use `"exec"` for statements.

💡 **Hint**
> You almost never need this. For normal code, just write it directly.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(eval(compile("10 * 2", "<x>", "eval")))   # 20
print(eval(compile("5 > 3", "<x>", "eval")))     # True
print(eval(compile("len('hi')", "<x>", "eval"))) # 2
exec(compile("print('run!')", "<x>", "exec"))    # run! (a statement)
print(eval(compile("3 ** 2", "<x>", "eval")))    # 9
```
</details>

<details>
<summary>🛠️ <b>Mini Project</b></summary>

*Not recommended for beginners — `compile()` (and `eval`/`exec`) can be unsafe with untrusted text. Write normal code instead.*
</details>

🔗 **See Also** — `eval()` · `exec()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="complex"></a>
## 🔢 `complex()` &nbsp;<sub>🟡 Intermediate</sub>

> 🎯 **Objective —** Build a *complex number* (a number with a real and an imaginary part).

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A complex number | Numbers | `abs()` · `float()` · `int()` |

📖 **Description** — `complex()` makes a complex number, written like `3+4j`. The `j` marks the "imaginary" part. These appear in advanced math and engineering — rare in everyday code, but good to recognise.

🏷️ **Concepts** — `numbers` · `real & imaginary parts`

🧭 **What · Why · When · How**
- **What** — creates a number with two parts: real and imaginary.
- **Why** — some math (geometry, signals) needs them.
- **When** — advanced math; rarely in everyday programs.
- **How** — `complex(real, imaginary)`.

⌨️ **Syntax**
```python
complex(real, imaginary)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `real` | the real part (a number) | ⬜ Optional (default 0) |
| `imaginary` | the imaginary part (a number) | ⬜ Optional (default 0) |

↩️ **Return Value** — a complex number, shown like `(3+4j)`.

🔍 **Line-by-Line Explanation**
```python
c = complex(3, 4)   # real part 3, imaginary part 4
print(c)            # show it -> (3+4j)
print(abs(c))       # its size (distance from zero) -> 5.0
```
> • build `3 + 4j`
> • printing shows `(3+4j)`
> • `abs()` gives its magnitude, `5.0`

▶️ **Output & Output Explanation**
```text
(3+4j)
5.0
```
`complex(3, 4)` is `3+4j`; its distance from zero is `5.0` (like the 3-4-5 triangle).

⚙️ **Internal Working** — Python stores the two parts separately (`.real` and `.imag`) and knows the math rules for combining complex numbers.

⚠️ **Common Mistakes & Errors**
> Writing the imaginary unit as `i` (math style). In Python it's `j` — e.g. `3+4j`.

💡 **Hint**
> The `j` means "imaginary". You can read `.real` and `.imag` to get each part.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(complex(3, 4))    # (3+4j)
print(complex(5))       # (5+0j)  -> only a real part
print(complex(0, 1))    # 1j      -> purely imaginary
print((3 + 4j).real)    # 3.0     -> the real part
print((3 + 4j).imag)    # 4.0     -> the imaginary part
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Distance From Zero</b></summary>

```python
point = complex(6, 8)             # treat (6, 8) as a complex number
distance = abs(point)             # abs gives its distance from zero
print(f"Distance from zero: {distance}")
```
**Output:** `Distance from zero: 10.0`
For `6+8j`, the magnitude is 10 (a 6-8-10 right triangle).

✏️ **Your turn:** try `complex(3, 4)` — the distance should be `5.0`.
</details>

🔗 **See Also** — `abs()` · `float()` · `int()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="delattr"></a>
## 🗑️ `delattr()` &nbsp;<sub>🟡 Intermediate</sub>

> 🎯 **Objective —** Remove a named piece of data (an *attribute*) from an object.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| Nothing (`None`) | Objects | `setattr()` · `getattr()` · `hasattr()` |

📖 **Description** — Objects can hold named values called *attributes* (like `person.age`). `delattr()` removes one of them by name.

🏷️ **Concepts** — `objects` · `attributes` · `removing data`

🧭 **What · Why · When · How**
- **What** — deletes an attribute from an object.
- **Why** — to remove data you no longer need on an object.
- **When** — when cleaning up object data (somewhat advanced).
- **How** — `delattr(object, "attribute_name")`.

⌨️ **Syntax**
```python
delattr(object, "attribute_name")
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `object` | the object to change | ✅ Yes |
| `attribute_name` | the attribute's name, as text | ✅ Yes |

↩️ **Return Value** — nothing (`None`); it just removes the attribute.

🔍 **Line-by-Line Explanation**
```python
import types                                    # lets us make a simple object
person = types.SimpleNamespace(name="Sam", age=30)  # an object with two attributes
delattr(person, "age")                          # remove the 'age' attribute
print(person)                                   # 'age' is gone
```
> • make an object holding `name` and `age`
> • `delattr(person, "age")` removes `age`
> • printing shows only `name` remains

▶️ **Output & Output Explanation**
```text
namespace(name='Sam')
```
The `age` attribute was deleted, so only `name` is left.

⚙️ **Internal Working** — Python calls the object's `__delattr__`, which removes the name from the object's internal storage.

⚠️ **Common Mistakes & Errors**
> `delattr(person, "missing")` when the attribute doesn't exist → **AttributeError**.

💡 **Hint**
> `delattr(obj, "x")` is the same as writing `del obj.x`.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
import types
p = types.SimpleNamespace(a=1, b=2, c=3)
delattr(p, "b")            # remove attribute b
print(p)                   # namespace(a=1, c=3)
print(hasattr(p, "b"))     # False -> b is gone
# del p.a  # the same idea, written with 'del'
print(hasattr(p, "a"))     # True  -> a still exists
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Forget a Detail</b></summary>

```python
import types
profile = types.SimpleNamespace(name="Lily", city="Rome", age=22)
delattr(profile, "age")     # the person prefers not to store age
print(profile)
```
**Output:** `namespace(name='Lily', city='Rome')`
The `age` attribute is removed from the profile.

✏️ **Your turn:** also remove `city`, then print the profile.
</details>

🔗 **See Also** — `setattr()` · `getattr()` · `hasattr()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="dict"></a>
## 📔 `dict()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Build a *dictionary* — data stored as key → value pairs.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A dictionary | Collections | `list()` · `set()` · `zip()` |

📖 **Description** — `dict()` creates a dictionary: a collection where each value has a labelled *key*, so you look things up by name instead of position.

🏷️ **Concepts** — `dictionaries` · `keys & values` · `collections`

🧭 **What · Why · When · How**
- **What** — makes a key → value lookup table.
- **Why** — to label data (e.g. `"name"` → `"Maya"`).
- **When** — whenever data has named fields.
- **How** — `dict(key=value, ...)` or `dict(list_of_pairs)`.

⌨️ **Syntax**
```python
dict(key1=value1, key2=value2)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `**kwargs` / pairs | key=value pairs, or a list of `(key, value)` pairs | ⬜ Optional (empty = `{}`) |

↩️ **Return Value** — a dictionary.

🔍 **Line-by-Line Explanation**
```python
person = dict(name="Maya", age=24)  # build a dict with two key=value pairs
print(person)                       # show the dictionary
print(person["name"])               # look up the value for key 'name'
```
> • create a dict with keys `name` and `age`
> • printing shows `{'name': 'Maya', 'age': 24}`
> • `person["name"]` fetches `'Maya'`

▶️ **Output & Output Explanation**
```text
{'name': 'Maya', 'age': 24}
Maya
```
The dict holds two pairs; `person["name"]` returns the value `Maya`.

⚙️ **Internal Working** — Python stores the pairs in a fast lookup structure (a hash table), so finding a value by its key is very quick.

⚠️ **Common Mistakes & Errors**
> `dict("name", "Maya")` → **TypeError**. Use `dict(name="Maya")` or `{"name": "Maya"}`.

💡 **Hint**
> The empty `{}` makes an empty dict; `dict()` does the same.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(dict(a=1, b=2))                 # {'a': 1, 'b': 2}
print(dict())                         # {} -> empty dict
print(dict([("x", 1), ("y", 2)]))     # {'x': 1, 'y': 2} -> from pairs
print(dict(zip(["p", "q"], [10, 20])))# {'p': 10, 'q': 20} -> from two lists
print({"name": "Sam"})                # {'name': 'Sam'} -> the {} shortcut
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Build a Contact</b></summary>

```python
contact = dict(name="Lily", phone="555-0102", city="Rome")  # three fields
print(f"Name : {contact['name']}")
print(f"Phone: {contact['phone']}")
print(f"City : {contact['city']}")
```
**Output:**
```text
Name : Lily
Phone: 555-0102
City : Rome
```
Each value is fetched by its key name.

✏️ **Your turn:** add an `email` field and print it too.
</details>

🔗 **See Also** — `list()` · `set()` · `zip()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="dir"></a>
## 🔎 `dir()` &nbsp;<sub>🟡 Intermediate</sub>

> 🎯 **Objective —** List everything you can do with a value (its methods and attributes).

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A list of names | Inspection | `help()` · `type()` · `vars()` |

📖 **Description** — `dir()` returns a list of the names (methods and attributes) available on an object. It's a quick way to discover what a value can do.

🏷️ **Concepts** — `objects` · `methods` · `exploration`

🧭 **What · Why · When · How**
- **What** — lists the names belonging to an object.
- **Why** — to explore what you can do with something.
- **When** — when learning a new type or debugging.
- **How** — `dir(thing)`.

⌨️ **Syntax**
```python
dir(object)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `object` | the value to inspect | ⬜ Optional |

↩️ **Return Value** — a list of names (strings), sorted alphabetically.

🔍 **Line-by-Line Explanation**
```python
names = dir("hello")            # list everything a string can do
print(type(names).__name__)     # it's a list -> list
print("upper" in names)         # is the .upper() method there? -> True
```
> • `dir("hello")` gives all string methods/attributes
> • the result is a `list`
> • `"upper" in names` confirms `.upper()` exists → `True`

▶️ **Output & Output Explanation**
```text
list
True
```
`dir()` returns a list; checking `"upper"` shows the string has an `.upper()` method.

⚙️ **Internal Working** — Python gathers the names defined on the object and its type, sorts them, and returns them as a list.

⚠️ **Common Mistakes & Errors**
> Expecting plain values — the list includes many `__dunder__` names (like `__len__`). Those are internal; ignore them at first.

💡 **Hint**
> To see only the "normal" methods, skip names starting with `_`.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(type(dir("hi")).__name__)             # list
print("append" in dir([]))                  # True  -> lists have .append()
print("keys" in dir({}))                    # True  -> dicts have .keys()
print("upper" in dir("text"))               # True  -> strings have .upper()
print([m for m in dir("hi") if not m.startswith("_")][:3])  # first 3 normal methods
```
</details>

<details>
<summary>🛠️ <b>Mini Project — What Can a List Do?</b></summary>

```python
list_methods = [m for m in dir([]) if not m.startswith("_")]  # skip internal names
print("A list can:")
print(", ".join(list_methods))
```
**Output (shortened):** `A list can: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort`
These are the actions you can perform on a list.

✏️ **Your turn:** change `[]` to `""` to see what a string can do instead.
</details>

🔗 **See Also** — `help()` · `type()` · `vars()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="divmod"></a>
## ➗ `divmod()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Get the *quotient* and *remainder* of a division at the same time.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A tuple `(quotient, remainder)` | Numbers | `round()` · `pow()` · `abs()` |

📖 **Description** — `divmod(a, b)` divides `a` by `b` and gives back both the whole-number result and what's left over, as a pair.

🏷️ **Concepts** — `division` · `remainder` · `tuples`

🧭 **What · Why · When · How**
- **What** — returns `(a // b, a % b)` together.
- **Why** — get both answers in one step (no double calculation).
- **When** — splitting into groups, converting units (seconds → minutes).
- **How** — `divmod(a, b)`.

⌨️ **Syntax**
```python
divmod(a, b)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `a` | the number being divided | ✅ Yes |
| `b` | the number to divide by | ✅ Yes |

↩️ **Return Value** — a tuple: `(quotient, remainder)`.

🔍 **Line-by-Line Explanation**
```python
result = divmod(17, 5)   # divide 17 by 5: 3 whole times, 2 left over
print(result)            # show the pair -> (3, 2)
quotient, remainder = result  # unpack the pair into two variables
print(quotient, remainder)    # -> 3 2
```
> • `divmod(17, 5)` gives `(3, 2)`
> • unpacking splits it into `quotient` and `remainder`
> • prints `3 2`

▶️ **Output & Output Explanation**
```text
(3, 2)
3 2
```
5 fits into 17 three whole times (`3`) with `2` left over.

⚙️ **Internal Working** — Python computes the floor division `a // b` and the remainder `a % b`, then returns them together as a tuple.

⚠️ **Common Mistakes & Errors**
> `divmod(10, 0)` → **ZeroDivisionError**. You can't divide by zero.

💡 **Hint**
> It's `//` and `%` combined into one neat result.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(divmod(17, 5))   # (3, 2)
print(divmod(20, 4))   # (5, 0)  -> divides evenly
print(divmod(7, 2))    # (3, 1)
print(divmod(10, 3))   # (3, 1)
print(divmod(9, 2))    # (4, 1)
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Seconds to Minutes</b></summary>

```python
total_seconds = 130                              # any number of seconds
minutes, seconds = divmod(total_seconds, 60)     # 60 seconds in a minute
print(f"{total_seconds} seconds = {minutes} min {seconds} sec")
```
**Output:** `130 seconds = 2 min 10 sec`
60 goes into 130 twice (`2` minutes) with `10` seconds left over.

✏️ **Your turn:** change `total_seconds` to `200` and check the result.
</details>

🔗 **See Also** — `round()` · `pow()` · `abs()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

# E – F

<a id="enumerate"></a>
## 🔢 `enumerate()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Number the items of a list, pairing each with its position.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| Pairs of `(index, item)` | Collections | `zip()` · `range()` · `list()` |

📖 **Description** — `enumerate()` walks through a list and gives you each item **together with its position number** (starting at 0 by default).

🏷️ **Concepts** — `lists` · `position/index` · `pairs (tuples)`

🧭 **What · Why · When · How**
- **What** — turns items into `(index, item)` pairs.
- **Why** — so you know *where* each item is, not just what it is.
- **When** — numbering items, making ranked/labelled lists.
- **How** — `enumerate(my_list)`.

⌨️ **Syntax**
```python
enumerate(iterable, start=0)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `iterable` | the list/tuple/etc. to number | ✅ Yes |
| `start` | the first index number | ⬜ Optional (default 0) |

↩️ **Return Value** — an enumerate object of `(index, item)` pairs (wrap in `list()` to see).

🔍 **Line-by-Line Explanation**
```python
fruits = ["apple", "banana"]      # a list of two items
pairs = list(enumerate(fruits))   # pair each with its position
print(pairs)                      # show the pairs
```
> • a list of fruits
> • `enumerate()` adds positions: 0 for apple, 1 for banana
> • prints `[(0, 'apple'), (1, 'banana')]`

▶️ **Output & Output Explanation**
```text
[(0, 'apple'), (1, 'banana')]
```
Each item is paired with its index: apple is at `0`, banana at `1`.

⚙️ **Internal Working** — `enumerate` keeps a running counter and yields `(counter, item)` for each item, increasing the counter by 1 each time.

⚠️ **Common Mistakes & Errors**
> Forgetting positions start at 0. Use `start=1` if you want human-style numbering.

💡 **Hint**
> "enumerate" = "number them". Add `start=1` for "1, 2, 3…".

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(list(enumerate(["a", "b", "c"])))           # [(0,'a'), (1,'b'), (2,'c')]
print(list(enumerate(["x", "y"], start=1)))       # [(1,'x'), (2,'y')]
print(list(enumerate("hi")))                      # [(0,'h'), (1,'i')]
print(dict(enumerate(["red", "green"])))          # {0: 'red', 1: 'green'}
print(list(enumerate([])))                        # [] -> empty list, no pairs
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Numbered Menu</b></summary>

```python
menu = ["Coffee", "Tea", "Juice"]                        # the items
lines = [f"{n}. {item}" for n, item in enumerate(menu, start=1)]  # number them
print("\n".join(lines))                                  # show one per line
```
**Output:**
```text
1. Coffee
2. Tea
3. Juice
```
`enumerate(..., start=1)` gives human-friendly numbers 1, 2, 3.

✏️ **Your turn:** add "Water" to the menu and re-run.
</details>

🔗 **See Also** — `zip()` · `range()` · `list()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="eval"></a>
## ⚠️ `eval()` &nbsp;<sub>🔴 Advanced</sub>

> 🎯 **Objective —** Run a small piece of Python code stored as text. *(Advanced & risky — beginners can skip.)*

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| The result of the code | Advanced | `exec()` · `compile()` · `int()` |

📖 **Description** — `eval()` takes a string containing a Python *expression* and runs it, returning the result. It's powerful but **dangerous** with untrusted text, so beginners should avoid it.

🏷️ **Concepts** — `code as text` · `expressions` *(advanced)*

🧭 **What · Why · When · How**
- **What** — runs an expression that's written as text.
- **Why** — occasionally, to evaluate code built at runtime.
- **When** — rarely, and only with text *you* control.
- **How** — `eval("expression")`.

⌨️ **Syntax**
```python
eval(expression)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `expression` | Python code as text (an expression) | ✅ Yes |

↩️ **Return Value** — whatever the expression produces.

🔍 **Line-by-Line Explanation**
```python
text = "2 + 3"     # an expression written as text
result = eval(text)  # run it as if you typed 2 + 3
print(result)      # show the result -> 5
```
> • the text `"2 + 3"` is just a string
> • `eval()` runs it as real code → `5`
> • prints `5`

▶️ **Output & Output Explanation**
```text
5
```
`eval("2 + 3")` runs the expression and returns `5`.

⚙️ **Internal Working** — Python compiles the text into a small expression and runs it, returning the value it produces.

⚠️ **Common Mistakes & Errors**
> **Never** `eval()` text from a user or the internet — it can run harmful code. This is its biggest danger.

💡 **Hint**
> To turn `"5"` into the number `5`, use `int("5")` — not `eval()`. Safer and clearer.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(eval("2 + 3"))         # 5
print(eval("10 * 4"))        # 40
print(eval("len('hello')"))  # 5
print(eval("5 > 3"))         # True
print(eval("[1, 2, 3]"))     # [1, 2, 3]
```
</details>

<details>
<summary>🛠️ <b>Mini Project</b></summary>

*Not recommended for beginners — `eval()` can run dangerous code. To convert text to numbers, use `int()` or `float()` instead.*
</details>

🔗 **See Also** — `exec()` · `compile()` · `int()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="exec"></a>
## ⚠️ `exec()` &nbsp;<sub>🔴 Advanced</sub>

> 🎯 **Objective —** Run one or more *statements* of Python code stored as text. *(Advanced & risky — beginners can skip.)*

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| Nothing (`None`) | Advanced | `eval()` · `compile()` |

📖 **Description** — `exec()` is like `eval()` but runs full *statements* (such as assignments or loops) written as text. It returns nothing and, like `eval()`, is **unsafe** with untrusted text. Beginners should avoid it.

🏷️ **Concepts** — `code as text` · `statements` *(advanced)*

🧭 **What · Why · When · How**
- **What** — runs statement(s) written as text.
- **Why** — rarely, to run code built at runtime.
- **When** — advanced tools only; not for beginners.
- **How** — `exec("code")`.

⌨️ **Syntax**
```python
exec(code)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `code` | Python statement(s) as text | ✅ Yes |

↩️ **Return Value** — always `None` (it runs code; it doesn't give a value back).

🔍 **Line-by-Line Explanation**
```python
store = {}                  # a place to keep results
exec("x = 5 * 2", store)    # run the statement; x is created inside 'store'
print(store["x"])           # read the value that was created -> 10
```
> • `exec()` runs the assignment `x = 5 * 2`
> • the new variable `x` lands in the `store` dictionary
> • we read it back: `10`

▶️ **Output & Output Explanation**
```text
10
```
The statement created `x = 10`, which we then read from `store`.

⚙️ **Internal Working** — Python compiles the text in `"exec"` mode and runs it, applying any changes (like new variables) to the given namespace.

⚠️ **Common Mistakes & Errors**
> Same big danger as `eval()`: **never** run text from untrusted sources.

💡 **Hint**
> If you're tempted to use `exec()`, there's almost always a simpler, safer way.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
exec("print('hello')")               # hello
exec("for i in range(3): print(i)")  # 0 1 2 (each on its own line)
ns = {}; exec("y = 3 + 4", ns); print(ns["y"])   # 7
exec("a = [1, 2]; print(a)")         # [1, 2]
exec("print(2 ** 5)")                # 32
```
</details>

<details>
<summary>🛠️ <b>Mini Project</b></summary>

*Not recommended for beginners — `exec()` runs arbitrary code and can be unsafe. Write normal statements directly instead.*
</details>

🔗 **See Also** — `eval()` · `compile()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="filter"></a>
## 🧹 `filter()` &nbsp;<sub>🟡 Intermediate</sub>

> 🎯 **Objective —** Keep only the items of a list that pass a test.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A filter object (of kept items) | Collections | `map()` · `all()` · `any()` |

📖 **Description** — `filter()` goes through a collection and keeps only the items that match a test. With `None` as the test, it keeps items that are "truthy" (not empty/zero).

🏷️ **Concepts** — `lists` · `keeping/removing items` · `truthiness`

🧭 **What · Why · When · How**
- **What** — picks out items that pass a check.
- **Why** — to clean or narrow a list.
- **When** — removing blanks, keeping matches.
- **How** — `filter(test, items)`. Use `None` to drop falsy values.

⌨️ **Syntax**
```python
filter(test, iterable)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `test` | a check to apply (or `None` to keep truthy items) | ✅ Yes |
| `iterable` | the items to filter | ✅ Yes |

↩️ **Return Value** — a filter object (wrap in `list()` to see the kept items).

🔍 **Line-by-Line Explanation**
```python
values = [0, 1, 2, 0, 3]        # some numbers, including zeros
kept = list(filter(None, values))  # None keeps only "truthy" items (drops 0)
print(kept)                     # show what's left
```
> • zeros are "falsy", everything else is "truthy"
> • `filter(None, ...)` removes the zeros
> • prints `[1, 2, 3]`

▶️ **Output & Output Explanation**
```text
[1, 2, 3]
```
The zeros were dropped because they count as "false"; the rest were kept.

⚙️ **Internal Working** — `filter` checks each item against the test and yields only the ones that pass, one at a time (lazily).

⚠️ **Common Mistakes & Errors**
> Forgetting `list()` — `print(filter(None, x))` shows a filter object, not the items. Wrap it in `list()`.

💡 **Hint**
> `filter(None, items)` is a handy way to drop blanks, zeros, and empties.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(list(filter(None, [0, 1, 2, 0, 3])))        # [1, 2, 3]  -> drops zeros
print(list(filter(None, ["", "hi", "", "yo"])))   # ['hi', 'yo'] -> drops blanks
print(list(filter(str.isdigit, ["1","a","2"])))   # ['1', '2'] -> keeps digits
print(list(filter(str.isalpha, "a1b2c3")))        # ['a','b','c'] -> keeps letters
print(list(filter(None, [True, False, True])))    # [True, True] -> drops False
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Remove Empty Names</b></summary>

```python
names = ["Ann", "", "Ben", "", "Cara"]   # a list with empty entries
real_names = list(filter(None, names))    # keep only the non-empty names
print(real_names)
```
**Output:** `['Ann', 'Ben', 'Cara']`
`filter(None, ...)` drops the empty strings, leaving real names.

✏️ **Your turn:** add `"   "` (spaces) — does it get removed? (It won't; spaces are truthy!)
</details>

🔗 **See Also** — `map()` · `all()` · `any()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="float"></a>
## 🔢 `float()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Turn a value into a decimal number.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A decimal number (float) | Numbers | `int()` · `str()` · `round()` |

📖 **Description** — `float()` converts text or a whole number into a *decimal* number (one that can have a fractional part, like `3.5`).

🏷️ **Concepts** — `numbers` · `decimals` · `type conversion`

🧭 **What · Why · When · How**
- **What** — makes a decimal number from text or an int.
- **Why** — prices, measurements, and averages often need decimals.
- **When** — converting input like `"2.5"` before doing decimal math.
- **How** — `float(value)`.

⌨️ **Syntax**
```python
float(value)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `value` | a number or numeric text like `"2.5"` | ⬜ Optional (empty = `0.0`) |

↩️ **Return Value** — a decimal number (float).

🔍 **Line-by-Line Explanation**
```python
text = "2.5"          # a number written as text
price = float(text)   # convert the text into the decimal 2.5
print(price + 1)      # now decimal math works -> 3.5
```
> • `"2.5"` is text, not a number
> • `float("2.5")` makes it the number `2.5`
> • adding works → `3.5`

▶️ **Output & Output Explanation**
```text
3.5
```
The text became the number `2.5`, and `2.5 + 1` is `3.5`.

⚙️ **Internal Working** — Python reads the characters and builds a floating-point number (a decimal stored in a special binary format).

⚠️ **Common Mistakes & Errors**
> `float("two")` → **ValueError**. The text must look like a number, e.g. `"2"` or `"2.5"`.

💡 **Hint**
> `float` is for decimals; `int` is for whole numbers.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(float("3.5"))    # 3.5
print(float(5))        # 5.0  -> whole number becomes a decimal
print(float("10"))     # 10.0
print(float("  2.0 ")) # 2.0  -> spaces around are ignored
print(float(7) / 2)    # 3.5  -> decimal division
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Average Price</b></summary>

```python
prices_text = ["1.50", "2.25", "3.00"]                 # prices as text
prices = [float(p) for p in prices_text]               # turn each into a decimal
average = sum(prices) / len(prices)                    # work out the average
print(f"Average price: {average:.2f}")
```
**Output:** `Average price: 2.25`
Each text price becomes a decimal, then we average them.

✏️ **Your turn:** add `"4.00"` to the list and re-run.
</details>

🔗 **See Also** — `int()` · `str()` · `round()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="format"></a>
## 🎨 `format()` &nbsp;<sub>🟡 Intermediate</sub>

> 🎯 **Objective —** Turn a value into nicely-formatted text (decimals, padding, percentages…).

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A formatted string | Text | `str()` · `round()` · `f-strings` |

📖 **Description** — `format()` converts a value into text using a "format spec" — a short code that controls decimals, width, commas, percentages, and number bases.

🏷️ **Concepts** — `strings` · `formatting` · `numbers`

🧭 **What · Why · When · How**
- **What** — formats a value as text following rules you give.
- **Why** — to display numbers cleanly (money, percentages, columns).
- **When** — preparing output for people to read.
- **How** — `format(value, "spec")`. (f-strings use the same specs.)

⌨️ **Syntax**
```python
format(value, "spec")
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `value` | the value to format | ✅ Yes |
| `spec` | the format code (e.g. `".2f"`, `","`, `"x"`) | ⬜ Optional |

↩️ **Return Value** — a formatted string.

🔍 **Line-by-Line Explanation**
```python
pi = 3.14159                  # a long decimal
nice = format(pi, ".2f")      # keep 2 decimal places
print(nice)                   # show the tidy number
```
> • `".2f"` means "2 digits after the decimal point"
> • `format(pi, ".2f")` gives the text `"3.14"`
> • prints `3.14`

▶️ **Output & Output Explanation**
```text
3.14
```
The format spec `".2f"` rounded the display to two decimal places.

⚙️ **Internal Working** — Python calls the value's `__format__` method with your spec, which builds the final text accordingly.

⚠️ **Common Mistakes & Errors**
> Using a number spec on text (e.g. `format("hi", ".2f")`) → **ValueError**. Specs must match the value's type.

💡 **Hint**
> The same specs work inside f-strings: `f"{pi:.2f}"` equals `format(pi, ".2f")`.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(format(3.14159, ".2f"))  # 3.14      -> 2 decimals
print(format(1000000, ","))    # 1,000,000 -> thousands separators
print(format(0.25, ".0%"))     # 25%       -> percentage
print(format(255, "x"))        # ff        -> hexadecimal
print(format(42, ">6"))        # '    42'  -> right-aligned in width 6
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Price Tag</b></summary>

```python
price = 1234.5                          # a price
tag = format(price, ",.2f")             # commas AND 2 decimals
print(f"Price: ${tag}")
```
**Output:** `Price: $1,234.50`
`",.2f"` adds a thousands comma and keeps two decimal places.

✏️ **Your turn:** format `0.4` as a percentage with `".1%"`.
</details>

🔗 **See Also** — `str()` · `round()` · `f-strings`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="frozenset"></a>
## 🧊 `frozenset()` &nbsp;<sub>🟡 Intermediate</sub>

> 🎯 **Objective —** Make a *fixed* set of unique items (one that can't be changed).

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A frozenset | Collections | `set()` · `dict()` · `tuple()` |

📖 **Description** — A `frozenset` is like a `set` (unique items, no duplicates) but **unchangeable**. Because it's fixed, it can be used as a dictionary key or placed inside another set.

🏷️ **Concepts** — `sets` · `unique items` · `immutable (fixed)`

🧭 **What · Why · When · How**
- **What** — builds a set you can't add to or remove from.
- **Why** — when you need a set that's safe and usable as a key.
- **When** — fixed groups of unique values.
- **How** — `frozenset(items)`.

⌨️ **Syntax**
```python
frozenset(iterable)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `iterable` | items to put in the set | ⬜ Optional (empty = empty frozenset) |

↩️ **Return Value** — a frozenset of the unique items.

🔍 **Line-by-Line Explanation**
```python
fs = frozenset([1, 2, 2, 3])  # duplicates removed, and now fixed
print(fs)                     # show it -> frozenset({1, 2, 3})
print(2 in fs)                # check membership -> True
```
> • the duplicate `2` is dropped (sets keep unique items)
> • the result is fixed (can't be changed)
> • `2 in fs` confirms membership → `True`

▶️ **Output & Output Explanation**
```text
frozenset({1, 2, 3})
True
```
The duplicate was removed; the frozenset holds `1, 2, 3` and you can test membership.

⚙️ **Internal Working** — like a `set`, it stores items in a hash table for fast lookups, but it locks them so nothing can be added or removed.

⚠️ **Common Mistakes & Errors**
> `fs.add(4)` → **AttributeError**. A frozenset can't be changed. Use a normal `set` if you need to add items.

💡 **Hint**
> "frozen" = fixed. Use it when you need a set that won't change (e.g. a dict key).

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(frozenset([1, 2, 2, 3]))     # frozenset({1, 2, 3})
print(frozenset("hello"))          # frozenset({'h','e','l','o'}) -> unique letters
print(len(frozenset([1, 1, 1])))   # 1 -> only one unique item
print(frozenset([1, 2]) & frozenset([2, 3]))  # frozenset({2}) -> shared item
print(3 in frozenset([1, 2, 3]))   # True
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Fixed Tag Set</b></summary>

```python
tags = frozenset(["python", "beginner", "python"])  # duplicates removed, fixed
print(f"Unique tags: {sorted(tags)}")
print(f"Has 'python': {'python' in tags}")
```
**Output:**
```text
Unique tags: ['beginner', 'python']
Has 'python': True
```
The repeated "python" appears once, and the set is safely unchangeable.

✏️ **Your turn:** try `tags.add("new")` — you'll see it errors, because a frozenset is fixed.
</details>

🔗 **See Also** — `set()` · `dict()` · `tuple()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

# G – H

<a id="getattr"></a>
## 📤 `getattr()` &nbsp;<sub>🟡 Intermediate</sub>

> 🎯 **Objective —** Read a named piece of data (an *attribute*) from an object, safely.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| The attribute's value (or a default) | Objects | `setattr()` · `hasattr()` · `delattr()` |

📖 **Description** — Objects can hold named values (attributes), like `person.name`. `getattr()` reads one *by its name as text*, and can give a fallback if it's missing.

🏷️ **Concepts** — `objects` · `attributes` · `safe access`

🧭 **What · Why · When · How**
- **What** — gets `object.attribute` using the name as text.
- **Why** — handy when the attribute name is in a variable, or might not exist.
- **When** — reading object data without risking a crash.
- **How** — `getattr(object, "name", default)`.

⌨️ **Syntax**
```python
getattr(object, "attribute_name", default)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `object` | the object to read from | ✅ Yes |
| `attribute_name` | the attribute's name, as text | ✅ Yes |
| `default` | value to return if the attribute is missing | ⬜ Optional |

↩️ **Return Value** — the attribute's value, or the default if it's missing.

🔍 **Line-by-Line Explanation**
```python
import types
person = types.SimpleNamespace(name="Sam", age=30)  # an object with two attributes
print(getattr(person, "name"))            # read the 'name' attribute -> Sam
print(getattr(person, "email", "none"))   # 'email' is missing -> use the default
```
> • make an object with `name` and `age`
> • `getattr(person, "name")` returns `"Sam"`
> • `getattr(person, "email", "none")` returns the default `"none"`

▶️ **Output & Output Explanation**
```text
Sam
none
```
`name` exists so its value comes back; `email` is missing so the default is used.

⚙️ **Internal Working** — Python looks up the name in the object's storage; if not found and a default was given, it returns that instead of erroring.

⚠️ **Common Mistakes & Errors**
> `getattr(person, "missing")` with **no default** → **AttributeError**. Always pass a default if the attribute might not exist.

💡 **Hint**
> `getattr(obj, "x")` is the same as `obj.x` — but it won't crash if you add a default.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
import types
p = types.SimpleNamespace(color="red", size="M")
print(getattr(p, "color"))            # red
print(getattr(p, "size"))             # M
print(getattr(p, "price", 0))         # 0   -> missing, default used
print(getattr(p, "color", "blue"))    # red -> exists, default ignored
print(hasattr(p, "color"))            # True
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Read a Setting Safely</b></summary>

```python
import types
settings = types.SimpleNamespace(volume=70)     # only 'volume' is set
volume = getattr(settings, "volume", 50)         # exists -> 70
language = getattr(settings, "language", "English")  # missing -> default
print(f"Volume: {volume}, Language: {language}")
```
**Output:** `Volume: 70, Language: English`
`volume` is read directly; `language` falls back to the default.

✏️ **Your turn:** add `language="Spanish"` to the object and re-run.
</details>

🔗 **See Also** — `setattr()` · `hasattr()` · `delattr()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="globals"></a>
## 🌍 `globals()` &nbsp;<sub>🔴 Advanced</sub>

> 🎯 **Objective —** Get a dictionary of all the global (file-level) variables. *(Advanced — rarely needed.)*

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A dictionary of globals | Inspection (advanced) | `locals()` · `vars()` · `dir()` |

📖 **Description** — `globals()` returns a dictionary of every variable defined at the top level of your file. It's an advanced inspection tool you'll rarely use as a beginner.

🏷️ **Concepts** — `variables` · `scope` · `dictionaries` *(advanced)*

🧭 **What · Why · When · How**
- **What** — shows all top-level (global) variables as a dict.
- **Why** — advanced inspection or debugging.
- **When** — rarely; almost never for beginners.
- **How** — `globals()`.

⌨️ **Syntax**
```python
globals()
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| *(none)* | takes no arguments | — |

↩️ **Return Value** — a dictionary mapping names to their values.

🔍 **Line-by-Line Explanation**
```python
greeting = "hello"               # a global variable
print("greeting" in globals())   # is it in the globals dict? -> True
print(globals()["greeting"])     # read its value through globals -> hello
```
> • define a global variable `greeting`
> • `globals()` contains it → `True`
> • we can read it via the dictionary → `hello`

▶️ **Output & Output Explanation**
```text
True
hello
```
The variable `greeting` appears in the globals dictionary, and we read its value from there.

⚙️ **Internal Working** — Python keeps your module's top-level names in a dictionary; `globals()` simply hands you that dictionary.

⚠️ **Common Mistakes & Errors**
> Editing `globals()` to create variables is confusing and error-prone. Just assign variables normally.

💡 **Hint**
> You'll almost never need this. Normal variables are simpler and clearer.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
x = 10
print("x" in globals())              # True
print(globals()["x"])                # 10
print(type(globals()).__name__)      # dict
print("__name__" in globals())       # True -> a built-in global
print("not_defined" in globals())    # False
```
</details>

<details>
<summary>🛠️ <b>Mini Project</b></summary>

*Not beginner-appropriate — `globals()` is an advanced inspection tool. Use normal variables for everyday code.*
</details>

🔗 **See Also** — `locals()` · `vars()` · `dir()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="hasattr"></a>
## ❓ `hasattr()` &nbsp;<sub>🟡 Intermediate</sub>

> 🎯 **Objective —** Check whether an object has a particular attribute.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| `True` or `False` | Objects | `getattr()` · `setattr()` · `delattr()` |

📖 **Description** — `hasattr()` tells you whether an object has a named attribute, returning `True` or `False`. It's a safe way to check before reading.

🏷️ **Concepts** — `objects` · `attributes` · `booleans`

🧭 **What · Why · When · How**
- **What** — answers: "Does this object have attribute X?"
- **Why** — to avoid an AttributeError before reading.
- **When** — checking optional attributes.
- **How** — `hasattr(object, "name")`.

⌨️ **Syntax**
```python
hasattr(object, "attribute_name")
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `object` | the object to check | ✅ Yes |
| `attribute_name` | the attribute name, as text | ✅ Yes |

↩️ **Return Value** — `True` (it has it) or `False` (it doesn't).

🔍 **Line-by-Line Explanation**
```python
import types
person = types.SimpleNamespace(name="Sam")   # object with one attribute
print(hasattr(person, "name"))    # has 'name'?  -> True
print(hasattr(person, "age"))     # has 'age'?   -> False
```
> • object has `name` but not `age`
> • `hasattr(person, "name")` → `True`
> • `hasattr(person, "age")` → `False`

▶️ **Output & Output Explanation**
```text
True
False
```
The object has a `name` attribute but not an `age` attribute.

⚙️ **Internal Working** — it tries `getattr()`; if that succeeds it returns `True`, if it raises an error it returns `False`.

⚠️ **Common Mistakes & Errors**
> Passing the name *without quotes*: `hasattr(person, name)` → looks for a variable `name`. Use `"name"` (text).

💡 **Hint**
> Use `hasattr()` to check, then `getattr()` to read — a safe pair.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
import types
p = types.SimpleNamespace(x=1, y=2)
print(hasattr(p, "x"))       # True
print(hasattr(p, "z"))       # False
print(hasattr("hello", "upper"))  # True  -> strings have .upper()
print(hasattr([], "append"))      # True  -> lists have .append()
print(hasattr(5, "append"))       # False -> numbers don't
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Check Before Reading</b></summary>

```python
import types
user = types.SimpleNamespace(name="Lily")    # no 'email' attribute
if hasattr(user, "email"):                    # only read it if it exists
    print(user.email)
else:
    print("No email on file")
```
**Output:** `No email on file`
Because `email` isn't there, the safe check avoids a crash.

✏️ **Your turn:** add `email="lily@mail.com"` to the object and re-run.
</details>

🔗 **See Also** — `getattr()` · `setattr()` · `delattr()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="hash"></a>
## #️⃣ `hash()` &nbsp;<sub>🟡 Intermediate</sub>

> 🎯 **Objective —** Get a number "fingerprint" for a fixed value.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| An integer (the hash) | Inspection | `id()` · `dict()` · `set()` |

📖 **Description** — `hash()` turns a fixed (immutable) value into a number. Equal values always give the same hash. This is how sets and dictionaries find things quickly.

🏷️ **Concepts** — `hashing` · `immutable values` · `dicts & sets`

🧭 **What · Why · When · How**
- **What** — makes a number fingerprint for a value.
- **Why** — it's what lets dicts/sets look things up fast.
- **When** — mostly behind the scenes; rarely called directly.
- **How** — `hash(value)` — value must be immutable.

⌨️ **Syntax**
```python
hash(value)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `value` | an immutable value (number, string, tuple…) | ✅ Yes |

↩️ **Return Value** — an integer (the hash). Equal values share the same hash.

🔍 **Line-by-Line Explanation**
```python
print(hash(42))                    # a number's hash is itself -> 42
print(hash("hi") == hash("hi"))    # equal values -> equal hashes -> True
```
> • for small integers, the hash equals the number
> • two equal strings always hash to the same number → `True`

▶️ **Output & Output Explanation**
```text
42
True
```
`hash(42)` is `42`; equal strings always produce equal hashes.

⚙️ **Internal Working** — Python runs a formula over the value to produce a number. Equal values always yield the same number (that's the key rule).

⚠️ **Common Mistakes & Errors**
> `hash([1, 2])` → **TypeError**: lists are mutable, so they're *unhashable*. Use a tuple `(1, 2)` instead.

💡 **Hint**
> Only fixed (immutable) things are hashable: numbers, strings, tuples — not lists or dicts.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(hash(42))                       # 42
print(hash("hi") == hash("hi"))       # True  -> equal values, equal hash
print(hash((1, 2)) == hash((1, 2)))   # True  -> tuples are hashable
print(type(hash("x")).__name__)       # int
# print(hash([1, 2]))                 # ERROR -> lists are unhashable
print(hash(True))                     # 1     -> True behaves like 1
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Same Value, Same Fingerprint</b></summary>

```python
a = "password"
b = "password"
print(f"Hashes match: {hash(a) == hash(b)}")   # equal text -> equal hash
```
**Output:** `Hashes match: True`
Identical values always hash the same — that's why dicts can find keys reliably.

✏️ **Your turn:** change `b` to `"Password"` (capital P) and see the hashes differ.
</details>

🔗 **See Also** — `id()` · `dict()` · `set()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="help"></a>
## 🆘 `help()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Show Python's built-in documentation for anything.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| Nothing (prints docs) | Learning | `dir()` · `type()` · `print()` |

📖 **Description** — `help()` prints the official explanation of a function, type, or method right in your console. It's one of the best tools for learning Python on your own.

🏷️ **Concepts** — `documentation` · `self-learning`

🧭 **What · Why · When · How**
- **What** — prints built-in documentation.
- **Why** — to learn what something does without leaving Python.
- **When** — any time you meet an unfamiliar function.
- **How** — `help(thing)`.

⌨️ **Syntax**
```python
help(object)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `object` | the thing to explain (a function, type, etc.) | ⬜ Optional |

↩️ **Return Value** — nothing (`None`); it *prints* the documentation.

🔍 **Line-by-Line Explanation**
```python
help(len)   # print the documentation for the len() function
```
> • `help(len)` prints what `len` does and how to use it

▶️ **Output & Output Explanation**
```text
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.
```
It prints a short explanation of `len`, including what it does.

⚙️ **Internal Working** — Python reads the object's built-in documentation (its "docstring") and prints it in a readable layout.

⚠️ **Common Mistakes & Errors**
> `help(len())` calls `len()` first (which errors). Pass the function itself: `help(len)` — no `()`.

💡 **Hint**
> Pass the *name* without `()`: `help(print)`, `help(str)`, `help(list)`.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
help(len)        # docs for len()
help(print)      # docs for print()
help(str)        # docs for the str type (lots of methods)
help(abs)        # docs for abs()
help("hello".upper)  # docs for the .upper() string method
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Learn a New Function</b></summary>

```python
help(round)   # read the docs for round() to learn how it works
```
**Output (shortened):**
```text
Help on built-in function round in module builtins:

round(number, ndigits=None)
    Round a number to a given precision in decimal digits.
```
Now you know `round()` takes a number and an optional number of digits.

✏️ **Your turn:** run `help(sorted)` and read how its `reverse` option works.
</details>

🔗 **See Also** — `dir()` · `type()` · `print()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="hex"></a>
## 🔢 `hex()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Show a whole number in *hexadecimal* (base-16).

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A string starting with `0x` | Numbers | `bin()` · `oct()` · `int()` · `format()` |

📖 **Description** — `hex()` converts a whole number into base-16 text (digits 0–9 and letters a–f), starting with `0x`. Hex is common for colours and computer addresses.

🏷️ **Concepts** — `numbers` · `hexadecimal (base-16)` · `strings`

🧭 **What · Why · When · How**
- **What** — turns `255` into `'0xff'`.
- **Why** — hex is a compact way to show byte values (00–ff).
- **When** — colours, low-level number work.
- **How** — `hex(whole_number)`.

⌨️ **Syntax**
```python
hex(integer)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `integer` | a whole number | ✅ Yes |

↩️ **Return Value** — a string starting with `0x`.

🔍 **Line-by-Line Explanation**
```python
number = 255          # the whole number 255
h = hex(number)       # convert to hex text: '0xff'
print(h)              # show the hex form
```
> • store `255`
> • `hex(255)` gives `'0xff'` (f = 15, so ff = 255)
> • prints `0xff`

▶️ **Output & Output Explanation**
```text
0xff
```
In hex, `ff` equals 255. The `0x` marks it as hexadecimal.

⚙️ **Internal Working** — Python repeatedly divides by 16, mapping each remainder to a hex digit (10→a, 11→b … 15→f), with a `0x` prefix.

⚠️ **Common Mistakes & Errors**
> `hex(3.5)` → **TypeError**. It needs a *whole* number, not a decimal.

💡 **Hint**
> Hex digits go 0–9 then a–f. The `0x` just means "this is hex".

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(hex(255))   # 0xff
print(hex(16))    # 0x10
print(hex(10))    # 0xa
print(hex(0))     # 0x0
print(hex(4096))  # 0x1000
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Colour Value in Hex</b></summary>

```python
red = 255                                  # a colour channel value (0-255)
print(f"Red {red} in hex is {hex(red)}")   # show it in hex
```
**Output:** `Red 255 in hex is 0xff`
Web colours use hex; pure red is `ff` for the red channel.

✏️ **Your turn:** print the hex of `128` (half brightness).
</details>

🔗 **See Also** — `bin()` · `oct()` · `int()` · `format()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

# I

<a id="id"></a>
## 🆔 `id()` &nbsp;<sub>🟡 Intermediate</sub>

> 🎯 **Objective —** Get a unique identity number for an object (its place in memory).

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| An integer (the identity) | Inspection | `is` · `hash()` · `type()` |

📖 **Description** — `id()` returns a number that uniquely identifies an object while the program runs — like its "address". Two names pointing to the *same* object share the same `id`.

🏷️ **Concepts** — `objects` · `identity` · `memory`

🧭 **What · Why · When · How**
- **What** — gives an object's unique identity number.
- **Why** — to check if two names point to the *same* object.
- **When** — understanding sharing/aliasing of lists and dicts.
- **How** — `id(value)`.

⌨️ **Syntax**
```python
id(object)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `object` | the object to identify | ✅ Yes |

↩️ **Return Value** — an integer (different each run; don't rely on the exact value).

🔍 **Line-by-Line Explanation**
```python
x = [1, 2]      # a list
y = x           # y points to the SAME list (not a copy)
print(id(x) == id(y))  # same object -> True
```
> • `x` and `y` are two names for one list
> • their `id()` values match → `True`

▶️ **Output & Output Explanation**
```text
True
```
Because `y = x` doesn't copy, both names share one object, so their ids match.

⚙️ **Internal Working** — in CPython, `id()` returns the object's memory address as a number.

⚠️ **Common Mistakes & Errors**
> Comparing exact `id` numbers between runs — they change every time. Compare ids *within one run*, or use `is`.

💡 **Hint**
> `a is b` is a friendlier way of asking `id(a) == id(b)`.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
a = [1, 2]; b = a
print(id(a) == id(b))   # True  -> same object
c = [1, 2]
print(id(a) == id(c))   # False -> equal values, different objects
print(type(id(a)).__name__)  # int
print(a is b)           # True  -> the friendly version
print(a is c)           # False
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Copy or Same?</b></summary>

```python
original = [1, 2, 3]
alias = original              # NOT a copy -> same object
copy_of = original.copy()     # a real, separate copy
print(f"alias is same object: {id(alias) == id(original)}")
print(f"copy is same object:  {id(copy_of) == id(original)}")
```
**Output:**
```text
alias is same object: True
copy is same object:  False
```
`alias` shares the object; `.copy()` makes a brand-new one.

✏️ **Your turn:** change `alias` with `alias.append(4)` and print `original` — it changes too!
</details>

🔗 **See Also** — `is` · `hash()` · `type()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="input"></a>
## ⌨️ `input()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Ask the person running the program to type something.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A string (what they typed) | Input/Output | `print()` · `int()` · `float()` |

📖 **Description** — `input()` pauses the program, shows an optional message, waits for the user to type and press Enter, then gives back what they typed **as text**.

🏷️ **Concepts** — `user input` · `strings` · `interaction`

🧭 **What · Why · When · How**
- **What** — reads a line the user types.
- **Why** — to make interactive programs.
- **When** — quizzes, calculators, anything that asks the user.
- **How** — `input("prompt message")`.

⌨️ **Syntax**
```python
input("prompt")
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `prompt` | a message to show before typing | ⬜ Optional |

↩️ **Return Value** — always a **string** (even if they type numbers).

🔍 **Line-by-Line Explanation**
```python
name = input("What is your name? ")  # show the message, wait for typing
print(f"Hello, {name}!")             # greet them using what they typed
```
> • `input(...)` shows the prompt and waits
> • whatever they type is stored in `name` (as text)
> • we greet them with an f-string

▶️ **Output & Output Explanation**
```text
What is your name? Alice      <- the user typed "Alice"
Hello, Alice!
```
The program waits, the user types `Alice`, and it greets them.

⚙️ **Internal Working** — Python reads one line from the keyboard (standard input) up to the Enter key, and returns it as text (without the newline).

⚠️ **Common Mistakes & Errors**
> `input()` always gives **text**. To do math, convert: `age = int(input("Age? "))`. Forgetting this is the #1 beginner bug.

💡 **Hint**
> Numbers from `input()` are text. Wrap them in `int()` or `float()` before calculating.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
# (these wait for you to type, then continue)
name = input("Name: ")              # returns text
age = int(input("Age: "))           # convert text to a whole number
height = float(input("Height: "))   # convert text to a decimal
color = input()                     # no prompt is fine
print(name, age, height, color)
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Simple Greeter</b></summary>

```python
name = input("What's your name? ")          # ask for a name
age = int(input("How old are you? "))       # ask for age, convert to number
print(f"Hi {name}! Next year you'll be {age + 1}.")
```
**Example run:**
```text
What's your name? Sam
How old are you? 20
Hi Sam! Next year you'll be 21.
```
We convert the age with `int()` so `age + 1` does real math.

✏️ **Your turn:** also ask for their city and include it in the message.
</details>

🔗 **See Also** — `print()` · `int()` · `float()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="int"></a>
## 🔢 `int()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Turn a value into a whole number.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A whole number (int) | Numbers | `float()` · `str()` · `round()` |

📖 **Description** — `int()` converts text or a decimal into a *whole* number. For decimals it chops off the fractional part (it doesn't round).

🏷️ **Concepts** — `numbers` · `whole numbers` · `type conversion`

🧭 **What · Why · When · How**
- **What** — makes a whole number from text or a decimal.
- **Why** — numbers often arrive as text (e.g. from `input()`).
- **When** — before doing whole-number math.
- **How** — `int(value)`.

⌨️ **Syntax**
```python
int(value, base)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `value` | a number or numeric text like `"42"` | ⬜ Optional (empty = `0`) |
| `base` | the number base of the text (e.g. 2, 16) | ⬜ Optional (default 10) |

↩️ **Return Value** — a whole number (int).

🔍 **Line-by-Line Explanation**
```python
text = "7"           # a number written as text
number = int(text)   # convert "7" into the whole number 7
print(number + 3)    # now math works -> 10
print(int(3.9))      # a decimal is CHOPPED, not rounded -> 3
```
> • `"7"` is text; `int("7")` makes it `7`
> • `7 + 3` is `10`
> • `int(3.9)` drops the `.9` → `3`

▶️ **Output & Output Explanation**
```text
10
3
```
Text `"7"` became `7` (so `+3` gives `10`); `int(3.9)` chops to `3`.

⚙️ **Internal Working** — for text, Python reads the digits in the given base and builds an integer; for a float, it discards the part after the decimal point.

⚠️ **Common Mistakes & Errors**
> `int("3.5")` → **ValueError** (it's not a whole-number string). Convert through float: `int(float("3.5"))`.

💡 **Hint**
> `int()` chops toward zero; use `round()` if you actually want rounding.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(int("5"))         # 5
print(int(3.9))         # 3    -> chopped, not rounded
print(int("ff", 16))    # 255  -> read as hexadecimal
print(int("1010", 2))   # 10   -> read as binary
print(int("  42  "))    # 42   -> spaces around are ignored
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Add Two Typed Numbers</b></summary>

```python
a_text = "15"                      # numbers arriving as text
b_text = "27"
total = int(a_text) + int(b_text)  # convert both, then add
print(f"{a_text} + {b_text} = {total}")
```
**Output:** `15 + 27 = 42`
Without `int()`, `"15" + "27"` would join into `"1527"` instead of adding.

✏️ **Your turn:** remove the `int()` calls and see the difference!
</details>

🔗 **See Also** — `float()` · `str()` · `round()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="isinstance"></a>
## 🧬 `isinstance()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Check whether a value is of a particular type.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| `True` or `False` | Inspection | `type()` · `issubclass()` · `bool()` |

📖 **Description** — `isinstance()` checks if a value is of a given type (like `int`, `str`, `list`). It can check several types at once.

🏷️ **Concepts** — `types` · `checking` · `booleans`

🧭 **What · Why · When · How**
- **What** — answers: "Is this value a(n) X?"
- **Why** — to handle values differently based on their type.
- **When** — validating input, branching on type.
- **How** — `isinstance(value, type)`.

⌨️ **Syntax**
```python
isinstance(value, type)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `value` | the value to check | ✅ Yes |
| `type` | a type, or a tuple of types | ✅ Yes |

↩️ **Return Value** — `True` or `False`.

🔍 **Line-by-Line Explanation**
```python
x = 5                          # a whole number
print(isinstance(x, int))      # is x an int? -> True
print(isinstance(x, str))      # is x a str?  -> False
```
> • `x` is `5`, a whole number
> • it *is* an `int` → `True`
> • it is *not* a `str` → `False`

▶️ **Output & Output Explanation**
```text
True
False
```
`5` is an integer, so it's an `int` but not a `str`.

⚙️ **Internal Working** — Python checks whether the value's type matches (or is a subtype of) the type(s) you gave.

⚠️ **Common Mistakes & Errors**
> Quoting the type: `isinstance(x, "int")` → **TypeError**. Use the type itself: `int` (no quotes).

💡 **Hint**
> Prefer `isinstance(x, int)` over `type(x) == int` — it's the recommended way.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(isinstance(5, int))            # True
print(isinstance("hi", str))         # True
print(isinstance(5, str))            # False
print(isinstance(5, (int, float)))   # True -> matches if it's ANY of these
print(isinstance([1, 2], list))      # True
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Number or Text?</b></summary>

```python
value = 42                                  # try changing to "hello"
if isinstance(value, (int, float)):         # is it a number?
    print(f"{value} is a number")
else:
    print(f"{value} is not a number")
```
**Output:** `42 is a number`
`isinstance(value, (int, float))` is `True` for both whole and decimal numbers.

✏️ **Your turn:** set `value = "hello"` and re-run.
</details>

🔗 **See Also** — `type()` · `issubclass()` · `bool()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="issubclass"></a>
## 🧬 `issubclass()` &nbsp;<sub>🟡 Intermediate</sub>

> 🎯 **Objective —** Check whether one type is a "child" of another type.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| `True` or `False` | Inspection | `isinstance()` · `type()` |

📖 **Description** — `issubclass()` checks whether one *type* is built from (a subclass of) another type. For example, `bool` is a kind of `int`.

🏷️ **Concepts** — `types` · `inheritance` · `booleans`

🧭 **What · Why · When · How**
- **What** — answers: "Is type A based on type B?"
- **Why** — to understand type relationships.
- **When** — advanced type checks (more useful once you learn classes).
- **How** — `issubclass(type_a, type_b)`.

⌨️ **Syntax**
```python
issubclass(class_a, class_b)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `class_a` | the type you're testing | ✅ Yes |
| `class_b` | the type (or tuple of types) to test against | ✅ Yes |

↩️ **Return Value** — `True` or `False`.

🔍 **Line-by-Line Explanation**
```python
print(issubclass(bool, int))   # is bool a kind of int? -> True
print(issubclass(int, str))    # is int a kind of str?  -> False
```
> • `bool` is built on `int`, so → `True`
> • `int` has nothing to do with `str`, so → `False`

▶️ **Output & Output Explanation**
```text
True
False
```
`bool` is a subclass of `int` (True/False act like 1/0); `int` is not a subclass of `str`.

⚙️ **Internal Working** — Python walks the type's "family tree" (its base classes) to see if the other type appears in it.

⚠️ **Common Mistakes & Errors**
> Passing *values* instead of *types*: `issubclass(5, int)` → **TypeError**. Use types: `issubclass(bool, int)`. (For values, use `isinstance`.)

💡 **Hint**
> `issubclass` compares *types*; `isinstance` checks a *value* against a type.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(issubclass(bool, int))      # True
print(issubclass(int, object))    # True  -> everything is based on 'object'
print(issubclass(int, str))       # False
print(issubclass(str, object))    # True
print(issubclass(bool, (int, str)))  # True -> matches int
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Is True a Number?</b></summary>

```python
print(f"bool is a kind of int: {issubclass(bool, int)}")   # True
print(f"So True + True works: {True + True}")               # 2
```
**Output:**
```text
bool is a kind of int: True
So True + True works: 2
```
Because `bool` is built on `int`, `True` and `False` behave like `1` and `0`.

✏️ **Your turn:** check `issubclass(float, int)` — is a float a kind of int? (No!)
</details>

🔗 **See Also** — `isinstance()` · `type()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="iter"></a>
## 🔁 `iter()` &nbsp;<sub>🟡 Intermediate</sub>

> 🎯 **Objective —** Get an *iterator* — something that hands out items one at a time.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| An iterator | Collections | `next()` · `enumerate()` · `list()` |

📖 **Description** — `iter()` turns a collection (like a list) into an *iterator*: an object you can pull items from one by one using `next()`. Loops use this behind the scenes.

🏷️ **Concepts** — `iterators` · `one-at-a-time access`

🧭 **What · Why · When · How**
- **What** — creates an iterator from a collection.
- **Why** — to step through items manually, one at a time.
- **When** — advanced control over looping (loops do this automatically).
- **How** — `iter(collection)`, then `next(...)`.

⌨️ **Syntax**
```python
iter(iterable)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `iterable` | a list/tuple/string/etc. | ✅ Yes |

↩️ **Return Value** — an iterator object.

🔍 **Line-by-Line Explanation**
```python
numbers = [10, 20, 30]    # a list
it = iter(numbers)        # turn it into an iterator
print(next(it))           # pull the first item -> 10
print(next(it))           # pull the next item  -> 20
```
> • `iter(numbers)` makes an iterator
> • `next(it)` gives the first item, `10`
> • the next `next(it)` gives `20`

▶️ **Output & Output Explanation**
```text
10
20
```
Each `next()` hands out the following item from the iterator.

⚙️ **Internal Working** — `iter()` calls the object's `__iter__` method to produce an iterator that remembers its position between `next()` calls.

⚠️ **Common Mistakes & Errors**
> Calling `next()` past the end → **StopIteration**. (Normal `for` loops handle this for you.)

💡 **Hint**
> You rarely call `iter()` yourself — `for item in list:` does it automatically.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
it = iter([1, 2, 3])
print(next(it))             # 1
print(next(it))             # 2
print(list(iter("abc")))    # ['a', 'b', 'c'] -> each character
print(next(iter([99])))     # 99 -> first item of a one-item list
print(type(iter([])).__name__)  # list_iterator
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Serve One at a Time</b></summary>

```python
queue = iter(["Ann", "Ben", "Cara"])   # a line of people as an iterator
print(f"Now serving: {next(queue)}")    # Ann
print(f"Now serving: {next(queue)}")    # Ben
print(f"Now serving: {next(queue)}")    # Cara
```
**Output:**
```text
Now serving: Ann
Now serving: Ben
Now serving: Cara
```
Each `next()` serves the next person in line.

✏️ **Your turn:** add a 4th `next(queue)` — you'll get a StopIteration error (the line is empty).
</details>

🔗 **See Also** — `next()` · `enumerate()` · `list()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

# L – N

<a id="len"></a>
## 📏 `len()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Count how many items are inside something.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A whole number (the count) | Collections | `sum()` · `max()` · `range()` |

📖 **Description** — `len()` returns how many items are in a value — characters in text, items in a list, or pairs in a dictionary.

🏷️ **Concepts** — `length/size` · `collections` · `strings`

🧭 **What · Why · When · How**
- **What** — counts items.
- **Why** — to know how big something is.
- **When** — validating lengths, loops, "how many?" questions.
- **How** — `len(thing)`.

⌨️ **Syntax**
```python
len(object)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `object` | text, list, dict, set, tuple, etc. | ✅ Yes |

↩️ **Return Value** — a whole number (the count).

🔍 **Line-by-Line Explanation**
```python
word = "banana"     # a piece of text
count = len(word)   # count its characters
print(count)        # show the count -> 6
```
> • `"banana"` has 6 letters
> • `len(word)` returns `6`
> • prints `6`

▶️ **Output & Output Explanation**
```text
6
```
The word `banana` has six characters.

⚙️ **Internal Working** — Python asks the object for its length via its `__len__` method and returns that number.

⚠️ **Common Mistakes & Errors**
> `len(42)` → **TypeError**. Numbers have no length. Use it on text/lists/etc.

💡 **Hint**
> Spaces count too: `len("a b")` is `3`.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(len("banana"))       # 6  -> characters
print(len([1, 2, 3]))      # 3  -> list items
print(len({"a": 1}))       # 1  -> dict pairs
print(len(""))             # 0  -> empty text
print(len((1, 2, 3, 4)))   # 4  -> tuple items
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Password Length Check</b></summary>

```python
password = "secret12"                  # the password to check
print(f"Length: {len(password)}")
print(f"Long enough: {len(password) >= 8}")   # needs 8+ characters
```
**Output:**
```text
Length: 8
Long enough: True
```
`len()` measures the password, and we compare it to the minimum.

✏️ **Your turn:** change the password to `"abc"` and re-run.
</details>

🔗 **See Also** — `sum()` · `max()` · `range()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="list"></a>
## 📝 `list()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Make a list (an ordered, changeable collection) from other items.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A list | Collections | `tuple()` · `set()` · `dict()` |

📖 **Description** — `list()` builds a list. You can start empty, or turn another collection (text, range, tuple, set) into a list.

🏷️ **Concepts** — `lists` · `collections` · `type conversion`

🧭 **What · Why · When · How**
- **What** — creates a list, optionally from existing items.
- **Why** — lists are ordered and changeable, the everyday workhorse collection.
- **When** — gathering items you'll add to, sort, or index.
- **How** — `list()` or `list(something)`.

⌨️ **Syntax**
```python
list(iterable)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `iterable` | items to turn into a list | ⬜ Optional (empty = `[]`) |

↩️ **Return Value** — a list.

🔍 **Line-by-Line Explanation**
```python
letters = list("abc")   # turn the text into a list of characters
print(letters)          # show the list
```
> • `"abc"` is text
> • `list("abc")` splits it into `['a', 'b', 'c']`
> • prints the list

▶️ **Output & Output Explanation**
```text
['a', 'b', 'c']
```
The text became a list with one character per item.

⚙️ **Internal Working** — Python walks through the given iterable and collects each item into a new list, in order.

⚠️ **Common Mistakes & Errors**
> `list(5)` → **TypeError**: a number isn't iterable. Use `[5]` to make a one-item list.

💡 **Hint**
> `[]` and `list()` both make an empty list; `[]` is shorter.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(list("abc"))        # ['a', 'b', 'c']
print(list((1, 2, 3)))    # [1, 2, 3]   -> tuple to list
print(list(range(3)))     # [0, 1, 2]   -> range to list
print(list())             # []          -> empty list
print(list({3, 1, 2}))    # [1, 2, 3]   -> set to list (order may vary)
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Unique, Sorted Letters</b></summary>

```python
word = "mississippi"            # a word with repeats
unique = list(set(word))        # set drops duplicates, list makes it a list
print(sorted(unique))           # sort the unique letters
```
**Output:** `['i', 'm', 'p', 's']`
`set()` removes duplicate letters; `list()` and `sorted()` tidy them up.

✏️ **Your turn:** try the word `"banana"`.
</details>

🔗 **See Also** — `tuple()` · `set()` · `dict()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="locals"></a>
## 🏠 `locals()` &nbsp;<sub>🔴 Advanced</sub>

> 🎯 **Objective —** Get a dictionary of the local variables in the current spot. *(Advanced — rarely needed.)*

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A dictionary of local variables | Inspection (advanced) | `globals()` · `vars()` · `dir()` |

📖 **Description** — `locals()` returns a dictionary of the variables visible in the current local area. At the top level of a file it's similar to `globals()`. It's an advanced tool beginners rarely need.

🏷️ **Concepts** — `variables` · `scope` · `dictionaries` *(advanced)*

🧭 **What · Why · When · How**
- **What** — shows local variables as a dict.
- **Why** — advanced inspection/debugging.
- **When** — rarely; not for beginners.
- **How** — `locals()`.

⌨️ **Syntax**
```python
locals()
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| *(none)* | takes no arguments | — |

↩️ **Return Value** — a dictionary of local names and their values.

🔍 **Line-by-Line Explanation**
```python
city = "Rome"                  # a local variable
print("city" in locals())      # is it among the locals? -> True
print(type(locals()).__name__) # it's a dict -> dict
```
> • define `city`
> • `locals()` includes it → `True`
> • the result is a `dict`

▶️ **Output & Output Explanation**
```text
True
dict
```
`city` appears in the locals dictionary, which is a `dict`.

⚙️ **Internal Working** — Python exposes the current local namespace as a dictionary. (Editing it doesn't reliably create real variables.)

⚠️ **Common Mistakes & Errors**
> Trying to *create* variables by editing `locals()` — it often won't work. Assign variables normally.

💡 **Hint**
> Like `globals()`, you'll almost never need this as a beginner.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
a = 1
print("a" in locals())            # True
print(type(locals()).__name__)    # dict
b = "hi"
print("b" in locals())            # True
print("missing" in locals())      # False
```
</details>

<details>
<summary>🛠️ <b>Mini Project</b></summary>

*Not beginner-appropriate — `locals()` is an advanced inspection tool. Use normal variables instead.*
</details>

🔗 **See Also** — `globals()` · `vars()` · `dir()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="map"></a>
## 🔁 `map()` &nbsp;<sub>🟡 Intermediate</sub>

> 🎯 **Objective —** Apply the same action to every item in a list.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A map object (transformed items) | Collections | `filter()` · `list()` · comprehensions |

📖 **Description** — `map()` takes a function and a collection, and runs that function on **every** item, giving back the transformed items. You can use built-in functions like `str`, `int`, or `str.upper` — no need to write your own.

🏷️ **Concepts** — `lists` · `transforming items` · `functions as tools`

🧭 **What · Why · When · How**
- **What** — applies a function to each item.
- **Why** — to transform a whole list at once.
- **When** — converting types, uppercasing, measuring lengths, etc.
- **How** — `map(function, items)` — use a built-in function as the tool.

⌨️ **Syntax**
```python
map(function, iterable)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `function` | the action to apply (e.g. `str`, `int`, `str.upper`) | ✅ Yes |
| `iterable` | the items to transform | ✅ Yes |

↩️ **Return Value** — a map object (wrap in `list()` to see the results).

🔍 **Line-by-Line Explanation**
```python
texts = ["1", "2", "3"]            # numbers stored as text
numbers = list(map(int, texts))    # turn each text into a real number
print(numbers)                     # show the result
```
> • each item is text like `"1"`
> • `map(int, texts)` runs `int()` on every item
> • prints `[1, 2, 3]`

▶️ **Output & Output Explanation**
```text
[1, 2, 3]
```
`int` was applied to every item, turning each text into a number.

⚙️ **Internal Working** — `map` pairs the function with each item and yields the results one at a time (lazily), which is why you wrap it in `list()`.

⚠️ **Common Mistakes & Errors**
> Forgetting `list()` — `print(map(...))` shows a map object, not the values. Wrap it in `list()`.

💡 **Hint**
> Pass the function **without** `()`: `map(str.upper, words)`, not `map(str.upper(), words)`.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(list(map(str, [1, 2, 3])))          # ['1', '2', '3'] -> numbers to text
print(list(map(int, ["4", "5"])))         # [4, 5]          -> text to numbers
print(list(map(str.upper, ["a", "b"])))   # ['A', 'B']      -> uppercase each
print(list(map(len, ["hi", "hello"])))    # [2, 5]          -> length of each
print(list(map(abs, [-1, -2, 3])))        # [1, 2, 3]       -> abs of each
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Convert Prices to Numbers</b></summary>

```python
price_texts = ["1.50", "2.25", "3.00"]              # prices as text
prices = list(map(float, price_texts))               # turn each into a decimal
print(f"Prices: {prices}")
print(f"Total: {sum(prices):.2f}")
```
**Output:**
```text
Prices: [1.5, 2.25, 3.0]
Total: 6.75
```
`map(float, ...)` converts every price at once, then `sum()` adds them.

✏️ **Your turn:** use `map(str.title, ["ann", "ben"])` to capitalise names.
</details>

🔗 **See Also** — `filter()` · `list()` · comprehensions

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="max"></a>
## ⬆️ `max()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Find the largest value.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| The largest item | Numbers/Collections | `min()` · `sorted()` · `sum()` |

📖 **Description** — `max()` returns the biggest value — either from several arguments or from a list. With text, "biggest" means latest alphabetically.

🏷️ **Concepts** — `comparison` · `largest` · `collections`

🧭 **What · Why · When · How**
- **What** — picks the largest value.
- **Why** — to find a top score, highest price, etc.
- **When** — any "what's the biggest?" question.
- **How** — `max(a, b, c)` or `max(my_list)`.

⌨️ **Syntax**
```python
max(iterable)        # or:  max(a, b, c, ...)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `iterable` / values | a list, or several values | ✅ Yes |
| `key`, `default` | advanced options | ⬜ Optional |

↩️ **Return Value** — the largest item.

🔍 **Line-by-Line Explanation**
```python
scores = [70, 95, 82]     # a list of scores
top = max(scores)         # find the biggest
print(top)                # show it -> 95
```
> • a list of three scores
> • `max(scores)` finds `95`
> • prints `95`

▶️ **Output & Output Explanation**
```text
95
```
`95` is the largest number in the list.

⚙️ **Internal Working** — Python scans the items, keeping track of the biggest seen so far, and returns it at the end.

⚠️ **Common Mistakes & Errors**
> `max([])` on an empty list → **ValueError**. Pass `default=...` or check it's not empty first.

💡 **Hint**
> Works on text too: `max("apple", "banana")` is `"banana"` (later alphabetically).

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(max(3, 7, 2))              # 7
print(max([10, 40, 20]))         # 40
print(max("apple", "banana"))    # banana  -> later alphabetically
print(max([1.5, 2.5, 0.5]))      # 2.5
print(max([5], default=0))       # 5
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Highest Score</b></summary>

```python
scores = [55, 91, 72, 88]                 # everyone's scores
print(f"Highest score: {max(scores)}")    # find the top one
print(f"Range: {max(scores) - min(scores)}")  # biggest minus smallest
```
**Output:**
```text
Highest score: 91
Range: 36
```
`max()` finds the top score; with `min()` we also get the spread.

✏️ **Your turn:** add a score of `99` and re-run.
</details>

🔗 **See Also** — `min()` · `sorted()` · `sum()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="memoryview"></a>
## 🧠 `memoryview()` &nbsp;<sub>🔴 Advanced</sub>

> 🎯 **Objective —** Look at raw bytes without copying them. *(Advanced — beginners can skip.)*

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A memoryview object | Binary data (advanced) | `bytes()` · `bytearray()` |

📖 **Description** — `memoryview()` lets you read (and sometimes edit) the bytes of data like `bytes` or `bytearray` *without making a copy*. It's a performance tool for large data — beyond beginner needs.

🏷️ **Concepts** — `bytes` · `memory` · `no-copy access` *(advanced)*

🧭 **What · Why · When · How**
- **What** — a "window" onto another object's bytes.
- **Why** — to work with big data efficiently (no copying).
- **When** — advanced performance work; rarely as a beginner.
- **How** — `memoryview(bytes_like)`.

⌨️ **Syntax**
```python
memoryview(bytes_object)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `bytes_object` | a `bytes` or `bytearray` | ✅ Yes |

↩️ **Return Value** — a memoryview object.

🔍 **Line-by-Line Explanation**
```python
data = b"abc"            # some bytes
view = memoryview(data)  # a window onto those bytes (no copy)
print(view[0])           # the first byte's number -> 97
```
> • `memoryview(data)` looks at the bytes directly
> • `view[0]` reads the first byte as a number (`a` = 97)

▶️ **Output & Output Explanation**
```text
97
```
The first byte is the letter `a`, whose number is `97`.

⚙️ **Internal Working** — it shares the original object's memory and provides indexed access without copying the data.

⚠️ **Common Mistakes & Errors**
> Expecting characters — indexing a memoryview gives the byte *numbers* (e.g. `97`), not letters.

💡 **Hint**
> You won't need this as a beginner. It's a tool for large, performance-critical data.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
mv = memoryview(b"abc")
print(mv[0])              # 97  -> byte value of 'a'
print(mv[1])              # 98  -> 'b'
print(bytes(mv))          # b'abc' -> back to bytes
print(len(mv))            # 3
print(list(mv))           # [97, 98, 99]
```
</details>

<details>
<summary>🛠️ <b>Mini Project</b></summary>

*Not beginner-appropriate — `memoryview()` is a performance tool for large binary data. Use `bytes`/`bytearray` directly for everyday tasks.*
</details>

🔗 **See Also** — `bytes()` · `bytearray()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="min"></a>
## ⬇️ `min()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Find the smallest value.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| The smallest item | Numbers/Collections | `max()` · `sorted()` · `sum()` |

📖 **Description** — `min()` returns the smallest value — from several arguments or from a list. With text, "smallest" means earliest alphabetically.

🏷️ **Concepts** — `comparison` · `smallest` · `collections`

🧭 **What · Why · When · How**
- **What** — picks the smallest value.
- **Why** — to find a lowest price, minimum score, etc.
- **When** — any "what's the smallest?" question.
- **How** — `min(a, b, c)` or `min(my_list)`.

⌨️ **Syntax**
```python
min(iterable)        # or:  min(a, b, c, ...)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `iterable` / values | a list, or several values | ✅ Yes |
| `key`, `default` | advanced options | ⬜ Optional |

↩️ **Return Value** — the smallest item.

🔍 **Line-by-Line Explanation**
```python
prices = [4.99, 1.50, 3.25]   # a list of prices
cheapest = min(prices)        # find the smallest
print(cheapest)               # show it -> 1.5
```
> • a list of three prices
> • `min(prices)` finds `1.5`
> • prints `1.5`

▶️ **Output & Output Explanation**
```text
1.5
```
`1.5` is the smallest price in the list.

⚙️ **Internal Working** — Python scans the items, keeping the smallest seen so far, and returns it.

⚠️ **Common Mistakes & Errors**
> `min([])` on an empty list → **ValueError**. Pass `default=...` or check first.

💡 **Hint**
> `min` and `max` are mirror images — same rules, opposite ends.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(min(3, 7, 2))              # 2
print(min([10, 40, 20]))         # 10
print(min("apple", "banana"))    # apple  -> earlier alphabetically
print(min([1.5, 2.5, 0.5]))      # 0.5
print(min([], default=0))        # 0      -> safe on empty
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Cheapest Item</b></summary>

```python
prices = [4.99, 1.50, 3.25, 0.99]              # prices in a cart
print(f"Cheapest: ${min(prices):.2f}")          # smallest price
print(f"Most expensive: ${max(prices):.2f}")    # largest price
```
**Output:**
```text
Cheapest: $0.99
Most expensive: $4.99
```
`min()` and `max()` find the extremes of the price list.

✏️ **Your turn:** add a price of `0.50` and re-run.
</details>

🔗 **See Also** — `max()` · `sorted()` · `sum()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="next"></a>
## ⏭️ `next()` &nbsp;<sub>🟡 Intermediate</sub>

> 🎯 **Objective —** Get the next item from an iterator, one at a time.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| The next item (or a default) | Collections | `iter()` · `enumerate()` |

📖 **Description** — `next()` pulls the following item from an iterator (made by `iter()`). You can give a default to return when there's nothing left, instead of an error.

🏷️ **Concepts** — `iterators` · `one-at-a-time access`

🧭 **What · Why · When · How**
- **What** — fetches the next item from an iterator.
- **Why** — to step through items manually.
- **When** — advanced looping control (loops use it automatically).
- **How** — `next(iterator, default)`.

⌨️ **Syntax**
```python
next(iterator, default)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `iterator` | an iterator (from `iter()`) | ✅ Yes |
| `default` | value to return when it's empty | ⬜ Optional |

↩️ **Return Value** — the next item, or the default if there are none left.

🔍 **Line-by-Line Explanation**
```python
it = iter([10, 20])     # make an iterator from a list
print(next(it))         # first item -> 10
print(next(it))         # next item  -> 20
print(next(it, "end"))  # nothing left -> the default "end"
```
> • `iter([10, 20])` makes an iterator
> • two `next()` calls give `10` then `20`
> • the third `next()` has nothing left, so returns `"end"`

▶️ **Output & Output Explanation**
```text
10
20
end
```
After both items are served, the default `"end"` prevents an error.

⚙️ **Internal Working** — `next()` calls the iterator's `__next__` method, which returns the next value or signals it's finished (`StopIteration`).

⚠️ **Common Mistakes & Errors**
> `next()` past the end with **no default** → **StopIteration** error. Pass a default to be safe.

💡 **Hint**
> Always pair `next()` with `iter()`, and add a default to avoid surprises.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
it = iter([1, 2, 3])
print(next(it))            # 1
print(next(it))            # 2
print(next(it))            # 3
print(next(it, "done"))    # done -> empty, default used
print(next(iter("hi")))    # h    -> first character
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Take the First Item</b></summary>

```python
winners = iter(["Gold", "Silver", "Bronze"])   # an iterator of medals
print(f"1st place: {next(winners)}")            # Gold
print(f"2nd place: {next(winners)}")            # Silver
```
**Output:**
```text
1st place: Gold
2nd place: Silver
```
Each `next()` hands out the next medal in order.

✏️ **Your turn:** add a line to get `next(winners)` for Bronze.
</details>

🔗 **See Also** — `iter()` · `enumerate()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

# O – R

<a id="object"></a>
## 🧊 `object()` &nbsp;<sub>🔴 Advanced</sub>

> 🎯 **Objective —** Create the simplest, most basic object Python has. *(Advanced — rarely used directly.)*

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A plain object | Objects (advanced) | `type()` · `id()` · `isinstance()` |

📖 **Description** — `object()` makes a featureless object. Every value in Python is ultimately built on `object`. You rarely create one directly; it's more of a foundation concept.

🏷️ **Concepts** — `objects` · `the base of everything` *(advanced)*

🧭 **What · Why · When · How**
- **What** — creates a bare object with no data of its own.
- **Why** — it's the root that all other types are built on.
- **When** — rarely; occasionally as a unique placeholder marker.
- **How** — `object()`.

⌨️ **Syntax**
```python
object()
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| *(none)* | takes no arguments | — |

↩️ **Return Value** — a new, plain object.

🔍 **Line-by-Line Explanation**
```python
thing = object()              # make a bare object
print(type(thing).__name__)   # its type is 'object'
```
> • `object()` builds a featureless object
> • its type is literally `object`

▶️ **Output & Output Explanation**
```text
object
```
The created value's type is `object`, the base of all Python types.

⚙️ **Internal Working** — it allocates the most basic instance Python has, with just the universal behaviour every object shares.

⚠️ **Common Mistakes & Errors**
> You can't add attributes to a plain `object()` (e.g. `o.x = 1` errors). Use a class or `types.SimpleNamespace` for that.

💡 **Hint**
> As a beginner, you'll almost never call `object()` directly. Just know everything is "an object".

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
o = object()
print(type(o).__name__)          # object
print(isinstance(o, object))     # True
print(isinstance(5, object))     # True -> numbers are objects too
print(isinstance("hi", object))  # True -> so are strings
print(type(object).__name__)     # type -> object itself is a type
```
</details>

<details>
<summary>🛠️ <b>Mini Project</b></summary>

*Not beginner-appropriate — `object()` is a foundational concept, not something you build with directly. Just remember: in Python, everything is an object.*
</details>

🔗 **See Also** — `type()` · `id()` · `isinstance()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="oct"></a>
## 🔢 `oct()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Show a whole number in *octal* (base-8).

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A string starting with `0o` | Numbers | `bin()` · `hex()` · `int()` |

📖 **Description** — `oct()` converts a whole number into base-8 text (digits 0–7), starting with `0o`. Octal is less common than binary or hex, but works the same way.

🏷️ **Concepts** — `numbers` · `octal (base-8)` · `strings`

🧭 **What · Why · When · How**
- **What** — turns `8` into `'0o10'`.
- **Why** — octal appears in some older systems and file permissions.
- **When** — low-level number work; learning number bases.
- **How** — `oct(whole_number)`.

⌨️ **Syntax**
```python
oct(integer)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `integer` | a whole number | ✅ Yes |

↩️ **Return Value** — a string starting with `0o`.

🔍 **Line-by-Line Explanation**
```python
number = 8           # the whole number eight
o = oct(number)      # convert to octal text: '0o10'
print(o)             # show the octal form
```
> • store `8`
> • `oct(8)` gives `'0o10'` (in base-8, 10 means eight)
> • prints `0o10`

▶️ **Output & Output Explanation**
```text
0o10
```
In octal, `10` means 8. The `0o` marks it as octal.

⚙️ **Internal Working** — Python repeatedly divides by 8, collecting remainders (0–7), with a `0o` prefix.

⚠️ **Common Mistakes & Errors**
> `oct(3.5)` → **TypeError**. It needs a whole number.

💡 **Hint**
> Octal digits go 0–7 only. The `0o` means "this is octal".

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(oct(8))     # 0o10
print(oct(64))    # 0o100
print(oct(10))    # 0o12
print(oct(0))     # 0o0
print(oct(255))   # 0o377
```
</details>

<details>
<summary>🛠️ <b>Mini Project — One Number, Three Bases</b></summary>

```python
n = 42                                  # any whole number
print(f"{n} in binary:  {bin(n)}")
print(f"{n} in octal:   {oct(n)}")
print(f"{n} in hex:     {hex(n)}")
```
**Output:**
```text
42 in binary:  0b101010
42 in octal:   0o52
42 in hex:     0x2a
```
The same number `42`, shown in three different bases.

✏️ **Your turn:** try the number `100`.
</details>

🔗 **See Also** — `bin()` · `hex()` · `int()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="open"></a>
## 📂 `open()` &nbsp;<sub>🟡 Intermediate</sub>

> 🎯 **Objective —** Open a file so you can read from it or write to it.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A file object | Files | `print()` · `str()` · `input()` |

📖 **Description** — `open()` connects your program to a file on disk. You give it a filename and a mode (`"r"` read, `"w"` write, `"a"` add), then read or write text. Use it inside a `with` block so the file closes automatically.

🏷️ **Concepts** — `files` · `reading & writing` · `with-blocks`

🧭 **What · Why · When · How**
- **What** — opens a file for reading or writing.
- **Why** — to save data, or load data back later.
- **When** — saving results, reading text files.
- **How** — `with open("name.txt", "mode") as f:`.

⌨️ **Syntax**
```python
open(filename, mode)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `filename` | the file's name/path, as text | ✅ Yes |
| `mode` | `"r"` read, `"w"` write, `"a"` append | ⬜ Optional (default `"r"`) |

↩️ **Return Value** — a file object you can read from or write to.

🔍 **Line-by-Line Explanation**
```python
with open("notes.txt", "w") as f:  # open (create) the file for writing
    f.write("Hello!")              # write some text into it
with open("notes.txt", "r") as f:  # open the same file for reading
    print(f.read())                # read and print its contents
```
> • the first `with` opens the file for **writing** and saves "Hello!"
> • the second opens it for **reading** and prints what's inside
> • the `with` block closes the file automatically each time

▶️ **Output & Output Explanation**
```text
Hello!
```
We wrote "Hello!" to the file, then read it back and printed it.

⚙️ **Internal Working** — `open()` asks the operating system for access to the file and returns a file object that buffers reads/writes. `with` ensures it's closed afterwards.

⚠️ **Common Mistakes & Errors**
> Opening a missing file in read mode → **FileNotFoundError**. Also: mode `"w"` **erases** the file first — use `"a"` to add instead.

💡 **Hint**
> Always use `with open(...) as f:` — it closes the file for you, even if an error happens.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
# write text (creates/overwrites the file)
with open("a.txt", "w") as f: f.write("line 1\n")
# append text (adds to the end)
with open("a.txt", "a") as f: f.write("line 2\n")
# read the whole file
with open("a.txt", "r") as f: print(f.read())
# read line by line into a list
with open("a.txt", "r") as f: print(f.readlines())
# default mode is read
with open("a.txt") as f: print(len(f.read()))
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Save and Load a Note</b></summary>

```python
note = "Buy milk and eggs"                 # the text to save
with open("shopping.txt", "w") as f:       # open for writing
    f.write(note)                          # save the note
with open("shopping.txt", "r") as f:       # open for reading
    loaded = f.read()                      # load it back
print(f"Saved note says: {loaded}")
```
**Output:** `Saved note says: Buy milk and eggs`
The note is written to a file, then read back into the program.

✏️ **Your turn:** change the mode of the first `open` to `"a"` and run twice — the note repeats.
</details>

🔗 **See Also** — `print()` · `str()` · `input()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="ord"></a>
## 🔡 `ord()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Turn a single character into its number (the opposite of `chr()`).

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A whole number (code point) | Text | `chr()` · `ascii()` · `str()` |

📖 **Description** — `ord()` takes one character and gives back its Unicode number (its "code point"). It's the reverse of `chr()`.

🏷️ **Concepts** — `characters` · `Unicode numbers` · `text`

🧭 **What · Why · When · How**
- **What** — character → number (e.g. `'A'` → `65`).
- **Why** — to compare characters or do simple ciphers.
- **When** — text encoding, puzzles, sorting by code.
- **How** — `ord(character)`.

⌨️ **Syntax**
```python
ord(character)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `character` | a string of exactly one character | ✅ Yes |

↩️ **Return Value** — a whole number (the Unicode code point).

🔍 **Line-by-Line Explanation**
```python
letter = "A"        # a single character
code = ord(letter)  # find its number
print(code)         # show it -> 65
```
> • `"A"` is one character
> • `ord("A")` gives `65`
> • prints `65`

▶️ **Output & Output Explanation**
```text
65
```
The capital letter `A` has the code number `65`.

⚙️ **Internal Working** — Python looks up the character in the Unicode table and returns its position number.

⚠️ **Common Mistakes & Errors**
> `ord("AB")` → **TypeError**. It needs exactly **one** character, not a word.

💡 **Hint**
> `ord` and `chr` are partners: `chr(ord("A"))` gives back `"A"`.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(ord("A"))    # 65
print(ord("a"))    # 97
print(ord("0"))    # 48  -> the character zero
print(ord("€"))    # 8364
print(chr(ord("Z")))  # Z -> round trip back to the character
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Letter to Number</b></summary>

```python
letter = "C"                                  # a letter
position = ord(letter) - ord("A") + 1          # A=1, B=2, C=3 ...
print(f"{letter} is letter number {position} of the alphabet")
```
**Output:** `C is letter number 3 of the alphabet`
Subtracting `ord("A")` turns letters into 1-based positions.

✏️ **Your turn:** try the letter `"Z"` — it should be number 26.
</details>

🔗 **See Also** — `chr()` · `ascii()` · `str()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="pow"></a>
## 🔢 `pow()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Raise a number to a power (and optionally take a remainder).

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A number | Numbers | `abs()` · `round()` · `divmod()` |

📖 **Description** — `pow(a, b)` calculates `a` to the power of `b` — the same as `a ** b`. With a third argument, `pow(a, b, c)` also takes the remainder mod `c`.

🏷️ **Concepts** — `numbers` · `powers/exponents`

🧭 **What · Why · When · How**
- **What** — computes `a` raised to the power `b`.
- **Why** — squares, cubes, growth, areas, volumes.
- **When** — any exponent calculation.
- **How** — `pow(base, exponent)`.

⌨️ **Syntax**
```python
pow(base, exponent, modulus)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `base` | the number to raise | ✅ Yes |
| `exponent` | the power to raise it to | ✅ Yes |
| `modulus` | take the remainder mod this | ⬜ Optional |

↩️ **Return Value** — a number (the result).

🔍 **Line-by-Line Explanation**
```python
result = pow(2, 3)   # 2 to the power of 3 = 2 * 2 * 2
print(result)        # show it -> 8
```
> • `pow(2, 3)` multiplies 2 by itself 3 times
> • that's `8`
> • prints `8`

▶️ **Output & Output Explanation**
```text
8
```
`2 ** 3` is `2 × 2 × 2 = 8`.

⚙️ **Internal Working** — Python multiplies the base by itself `exponent` times (using a fast method). With a modulus, it efficiently computes the remainder too.

⚠️ **Common Mistakes & Errors**
> Confusing `pow(2, 3)` (power → 8) with `2 * 3` (multiply → 6). Power is repeated multiplication.

💡 **Hint**
> `pow(a, b)` is the same as `a ** b` — pick whichever reads clearer.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(pow(2, 3))     # 8     -> 2*2*2
print(pow(5, 2))     # 25    -> 5 squared
print(pow(2, 10))    # 1024
print(pow(9, 0))     # 1     -> anything to the power 0 is 1
print(pow(2, 3, 5))  # 3     -> 8 mod 5 (the remainder)
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Area of a Square</b></summary>

```python
side = 6                          # length of one side
area = pow(side, 2)               # side squared = area of a square
print(f"A square with side {side} has area {area}")
```
**Output:** `A square with side 6 has area 36`
A square's area is its side raised to the power 2.

✏️ **Your turn:** compute the *volume* of a cube with `pow(side, 3)`.
</details>

🔗 **See Also** — `abs()` · `round()` · `divmod()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="print"></a>
## 🖨️ `print()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Show text or values on the screen.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| Nothing (`None`) | Input/Output | `input()` · `str()` · `format()` |

📖 **Description** — `print()` displays whatever you give it in the console. It's the very first function most people learn and the main way to *see* what your program is doing.

🏷️ **Concepts** — `output` · `strings` · `display`

🧭 **What · Why · When · How**
- **What** — prints values to the screen.
- **Why** — to see results and messages.
- **When** — constantly — checking values, showing output.
- **How** — `print(value1, value2, ...)`.

⌨️ **Syntax**
```python
print(*values, sep=" ", end="\n")
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `values` | one or more things to show | ⬜ Optional (empty = blank line) |
| `sep` | what to put between values (default a space) | ⬜ Optional |
| `end` | what to put at the end (default a newline) | ⬜ Optional |

↩️ **Return Value** — nothing (`None`); it just displays.

🔍 **Line-by-Line Explanation**
```python
print("Hello", "world")        # two values -> a space goes between them
print("A", "B", "C", sep="-")  # change the separator to a dash
print("no newline", end=" ")   # end with a space instead of a line break
print("same line")             # so this continues on the same line
```
> • commas put a space between values
> • `sep="-"` changes that separator
> • `end=" "` replaces the line break, so the next print joins on

▶️ **Output & Output Explanation**
```text
Hello world
A-B-C
no newline same line
```
Default spacing, then a dash separator, then two prints joined on one line.

⚙️ **Internal Working** — `print()` turns each value into text (using `str()`), joins them with `sep`, adds `end`, and sends it to the screen (standard output).

⚠️ **Common Mistakes & Errors**
> `print "hi"` (Python 2 style) → **SyntaxError**. In Python 3 you must use brackets: `print("hi")`.

💡 **Hint**
> Use an f-string for clean messages: `print(f"Score: {score}")`.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print("Hello")                  # Hello
print("x =", 5)                 # x = 5
print(1, 2, 3, sep=", ")        # 1, 2, 3
print("Loading", end="...")     # Loading... (no line break)
print()                         # (prints a blank line)
```
</details>

<details>
<summary>🛠️ <b>Mini Project — A Tiny Receipt</b></summary>

```python
item = "Coffee"
price = 3.5
print("=" * 20)                          # a line of 20 equals signs
print(f"{item:<10}${price:.2f}")          # name left-aligned, price with 2 decimals
print("=" * 20)
```
**Output:**
```text
====================
Coffee    $3.50
====================
```
`print()` plus f-string formatting makes a neat little receipt.

✏️ **Your turn:** add a second item line for "Cake" at 4.50.
</details>

🔗 **See Also** — `input()` · `str()` · `format()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="property"></a>
## 🏛️ `property()` &nbsp;<sub>🔴 Advanced</sub>

> 🎯 **Objective —** Make a method act like a simple attribute, inside a class. *(Needs classes — beginners can skip.)*

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A property object | Classes (advanced) | `classmethod()` · `staticmethod()` · `getattr()` |

📖 **Description** — `property()` is used *inside classes* (usually as the `@property` decorator) to let a method be accessed like a plain attribute. Because classes use `def`, this is beyond beginner scope.

🏷️ **Concepts** — `classes` · `attributes` · `methods` *(advanced)*

🧭 **What · Why · When · How**
- **What** — turns a method into a read-like attribute.
- **Why** — to compute a value on access while looking like a simple field.
- **When** — only when writing classes (a later topic).
- **How** — written as `@property` above a method (needs `def`).

⌨️ **Syntax**
```python
# Used as a decorator inside a class (needs def + class):
# @property
# def area(self): ...
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `fget` | the method that gets the value | ✅ Yes |
| `fset`, `fdel`, `doc` | optional setter/deleter/docs | ⬜ Optional |

↩️ **Return Value** — a property object.

🔍 **Line-by-Line Explanation**
```python
# Conceptual — requires a class (which uses def):
# class Circle:
#     @property
#     def area(self):
#         return 3.14159 * self.radius ** 2
```
> • The idea: read `circle.area` like a field, but it's computed by a method.

▶️ **Output & Output Explanation** — no simple beginner output; it only makes sense inside a class.

⚙️ **Internal Working** — it wraps getter/setter functions so that reading or writing the attribute quietly calls those functions.

⚠️ **Common Mistakes & Errors**
> Trying to use it outside a class — it only has meaning *inside* a `class` block.

💡 **Hint**
> Skip until you've learned `def` and `class`. Then properties will make sense.

<details>
<summary>📚 <b>5 Examples</b> (conceptual — need a class)</summary>

```python
# 1. @property turns a method into a read-like attribute
# 2. you then access it as obj.name (no parentheses)
# 3. great for computed values (like area from radius)
# 4. partners: classmethod, staticmethod
# 5. you'll use it after learning classes
```
</details>

<details>
<summary>🛠️ <b>Mini Project</b></summary>

*Not beginner-appropriate — needs classes (`def`/`class`). Revisit after the classes chapter.*
</details>

🔗 **See Also** — `classmethod()` · `staticmethod()` · `getattr()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="range"></a>
## 🔢 `range()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Create a sequence of numbers (great for counting and loops).

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A range of numbers | Numbers/Collections | `list()` · `enumerate()` · `len()` |

📖 **Description** — `range()` produces a sequence of numbers without storing them all at once. You set a start, a stop (not included), and an optional step.

🏷️ **Concepts** — `numbers` · `sequences` · `counting`

🧭 **What · Why · When · How**
- **What** — makes a number sequence like 0, 1, 2, 3…
- **Why** — to count or repeat a set number of times.
- **When** — loops, generating numbers, comprehensions.
- **How** — `range(stop)` or `range(start, stop, step)`.

⌨️ **Syntax**
```python
range(start, stop, step)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `start` | first number | ⬜ Optional (default 0) |
| `stop` | one past the last number (NOT included) | ✅ Yes |
| `step` | how much to count by | ⬜ Optional (default 1) |

↩️ **Return Value** — a range object (wrap in `list()` to see the numbers).

🔍 **Line-by-Line Explanation**
```python
numbers = range(5)        # the sequence 0, 1, 2, 3, 4
print(list(numbers))      # turn it into a list to see it
```
> • `range(5)` means 0 up to (but not including) 5
> • `list(...)` shows `[0, 1, 2, 3, 4]`

▶️ **Output & Output Explanation**
```text
[0, 1, 2, 3, 4]
```
`range(5)` gives five numbers starting at 0; `5` itself is **not** included.

⚙️ **Internal Working** — `range` stores only the start, stop, and step, and computes each number on demand — so even `range(1000000)` uses almost no memory.

⚠️ **Common Mistakes & Errors**
> The `stop` is **excluded**: `range(1, 5)` gives `1, 2, 3, 4` (not 5). For 1–5, use `range(1, 6)`.

💡 **Hint**
> Think "up to, but not including, stop". Wrap in `list()` to see the numbers.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(list(range(5)))         # [0, 1, 2, 3, 4]
print(list(range(2, 6)))      # [2, 3, 4, 5]
print(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]  -> step of 2
print(list(range(5, 0, -1)))  # [5, 4, 3, 2, 1]  -> counting down
print(len(range(100)))        # 100              -> how many numbers
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Countdown List</b></summary>

```python
countdown = list(range(5, 0, -1))     # 5 down to 1
print(f"Countdown: {countdown}")
print("Blast off!")
```
**Output:**
```text
Countdown: [5, 4, 3, 2, 1]
Blast off!
```
A negative step makes `range()` count backwards.

✏️ **Your turn:** make a list of even numbers from 0 to 20 with `range(0, 21, 2)`.
</details>

🔗 **See Also** — `list()` · `enumerate()` · `len()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="repr"></a>
## 🔍 `repr()` &nbsp;<sub>🟡 Intermediate</sub>

> 🎯 **Objective —** Get the "developer" version of a value (shows quotes and hidden details).

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A string (the repr) | Text/Inspection | `str()` · `ascii()` · `print()` |

📖 **Description** — `repr()` returns a precise, unambiguous text version of a value — often the exact way you'd type it in code. Strings come back **with quotes**, which helps you spot hidden spaces or characters.

🏷️ **Concepts** — `strings` · `debugging` · `representation`

🧭 **What · Why · When · How**
- **What** — gives the developer-friendly text form of a value.
- **Why** — to see exactly what a value is (quotes, escapes, etc.).
- **When** — debugging, especially with tricky strings.
- **How** — `repr(value)`.

⌨️ **Syntax**
```python
repr(object)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `object` | the value to represent | ✅ Yes |

↩️ **Return Value** — a string (often the code form of the value).

🔍 **Line-by-Line Explanation**
```python
text = "hi"           # a piece of text
print(str(text))      # str() -> the friendly form -> hi
print(repr(text))     # repr() -> the developer form -> 'hi'
```
> • `str("hi")` shows `hi` (for people)
> • `repr("hi")` shows `'hi'` (with quotes, for developers)

▶️ **Output & Output Explanation**
```text
hi
'hi'
```
`str()` is the clean form; `repr()` adds quotes so you can see it's text.

⚙️ **Internal Working** — Python calls the value's `__repr__` method, which returns its precise, often code-like representation.

⚠️ **Common Mistakes & Errors**
> Confusing `str()` (for humans) with `repr()` (for developers). For text, `repr()` shows the quotes.

💡 **Hint**
> Use `repr()` when a string looks "off" — it reveals hidden spaces, newlines, etc.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(repr("hi"))        # 'hi'      -> shows the quotes
print(repr(42))          # 42        -> numbers look the same
print(repr([1, 2]))      # [1, 2]
print(repr("a\nb"))      # 'a\nb'    -> reveals the hidden newline
print(repr("  spaced ")) # '  spaced ' -> reveals the spaces
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Spot the Hidden Spaces</b></summary>

```python
user_input = "  hello  "                    # text with sneaky spaces
print(f"Looks like: {user_input}")           # hard to see the spaces
print(f"Really is:  {repr(user_input)}")     # repr reveals them
```
**Output:**
```text
Looks like:   hello  
Really is:  '  hello  '
```
`repr()` shows the quotes, making the leading/trailing spaces visible.

✏️ **Your turn:** try `repr("line1\nline2")` to see the newline revealed.
</details>

🔗 **See Also** — `str()` · `ascii()` · `print()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="reversed"></a>
## 🔄 `reversed()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Go through a sequence backwards.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A reversed iterator | Collections | `sorted()` · `list()` · slicing `[::-1]` |

📖 **Description** — `reversed()` gives back the items of a list, tuple, or string in reverse order. Wrap it in `list()` (or `"".join()` for text) to see the result.

🏷️ **Concepts** — `lists` · `order` · `reversing`

🧭 **What · Why · When · How**
- **What** — reverses the order of items.
- **Why** — to process things last-to-first.
- **When** — countdowns, undo order, reversing text.
- **How** — `reversed(sequence)`.

⌨️ **Syntax**
```python
reversed(sequence)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `sequence` | a list, tuple, string, or range | ✅ Yes |

↩️ **Return Value** — a reversed iterator (wrap in `list()` to see it).

🔍 **Line-by-Line Explanation**
```python
nums = [1, 2, 3]            # a list
backwards = list(reversed(nums))  # reverse it into a new list
print(backwards)           # show the reversed list
```
> • `reversed(nums)` walks the list back-to-front
> • `list(...)` collects it as `[3, 2, 1]`
> • the original `nums` is unchanged

▶️ **Output & Output Explanation**
```text
[3, 2, 1]
```
The list's items come out in reverse order.

⚙️ **Internal Working** — it returns an iterator that yields items from the end toward the start, without changing the original.

⚠️ **Common Mistakes & Errors**
> Forgetting `list()` — `print(reversed(x))` shows an iterator object, not the items.

💡 **Hint**
> For a quick reversed *copy*, slicing also works: `[1,2,3][::-1]`.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(list(reversed([1, 2, 3])))     # [3, 2, 1]
print(list(reversed("abc")))         # ['c', 'b', 'a']
print("".join(reversed("hello")))    # olleh -> reversed text
print(list(reversed(range(5))))      # [4, 3, 2, 1, 0]
print(list(reversed((10, 20, 30))))  # [30, 20, 10]
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Is It a Palindrome?</b></summary>

```python
word = "level"                                  # try "hello" too
backwards = "".join(reversed(word))             # reverse the word
print(f"'{word}' reversed is '{backwards}'")
print(f"Palindrome: {word == backwards}")       # same forwards and backwards?
```
**Output:**
```text
'level' reversed is 'level'
Palindrome: True
```
A palindrome reads the same forwards and backwards.

✏️ **Your turn:** test the word `"hello"` — is it a palindrome?
</details>

🔗 **See Also** — `sorted()` · `list()` · slicing `[::-1]`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="round"></a>
## 🔢 `round()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Round a number to a chosen number of decimal places.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A rounded number | Numbers | `int()` · `format()` · `divmod()` |

📖 **Description** — `round()` rounds a number. With one argument it rounds to a whole number; with two, it keeps that many decimal places.

🏷️ **Concepts** — `numbers` · `rounding` · `decimals`

🧭 **What · Why · When · How**
- **What** — rounds a number to a given precision.
- **Why** — to tidy long decimals for display.
- **When** — money, averages, measurements.
- **How** — `round(number, decimals)`.

⌨️ **Syntax**
```python
round(number, decimals)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `number` | the number to round | ✅ Yes |
| `decimals` | how many decimal places to keep | ⬜ Optional (default 0) |

↩️ **Return Value** — the rounded number.

🔍 **Line-by-Line Explanation**
```python
value = 3.14159          # a long decimal
rounded = round(value, 2)  # keep 2 decimal places
print(rounded)           # show it -> 3.14
```
> • `round(3.14159, 2)` keeps two decimals
> • that's `3.14`
> • prints `3.14`

▶️ **Output & Output Explanation**
```text
3.14
```
Keeping two decimal places turns `3.14159` into `3.14`.

⚙️ **Internal Working** — Python rounds to the nearest value at the requested precision. On exact halves it rounds to the *even* neighbour ("banker's rounding").

⚠️ **Common Mistakes & Errors**
> Surprise: `round(2.5)` is `2`, not `3`! On exact `.5` values Python rounds to the nearest **even** number (`round(0.5)` → 0, `round(1.5)` → 2, `round(3.5)` → 4). This avoids bias over many numbers.

💡 **Hint**
> For display only, an f-string is often clearer: `f"{value:.2f}"`.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(round(3.14159, 2))   # 3.14
print(round(2.7))          # 3     -> nearest whole number
print(round(1234, -2))     # 1200  -> nearest hundred
print(round(2.5))          # 2     -> banker's rounding (to even)
print(round(3.5))          # 4     -> rounds up to even
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Split the Bill</b></summary>

```python
bill = 100.0                          # total bill
people = 3                            # how many split it
each = round(bill / people, 2)        # per person, to the cent
print(f"Each person pays: ${each}")
```
**Output:** `Each person pays: $33.33`
`round(..., 2)` keeps the result to two decimal places (cents).

✏️ **Your turn:** change `people` to `4` and re-run.
</details>

🔗 **See Also** — `int()` · `format()` · `divmod()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

# S

<a id="set"></a>
## 🎯 `set()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Make a collection of *unique* items (no duplicates).

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A set | Collections | `list()` · `frozenset()` · `dict()` |

📖 **Description** — `set()` builds a set: an unordered collection where every item is unique. Adding a duplicate has no effect. Sets are great for removing repeats and comparing groups.

🏷️ **Concepts** — `sets` · `unique items` · `collections`

🧭 **What · Why · When · How**
- **What** — makes a collection of unique values.
- **Why** — to drop duplicates or do group math (union, overlap).
- **When** — de-duplicating, membership checks, comparisons.
- **How** — `set(items)` or `{1, 2, 3}`.

⌨️ **Syntax**
```python
set(iterable)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `iterable` | items to put in the set | ⬜ Optional (empty = empty set) |

↩️ **Return Value** — a set of the unique items.

🔍 **Line-by-Line Explanation**
```python
nums = [1, 2, 2, 3, 3, 3]   # a list with duplicates
unique = set(nums)          # turn it into a set (duplicates dropped)
print(unique)               # show the unique values
```
> • the list has repeated 2s and 3s
> • `set(nums)` keeps each value once
> • prints `{1, 2, 3}`

▶️ **Output & Output Explanation**
```text
{1, 2, 3}
```
The duplicates are removed, leaving one of each value.

⚙️ **Internal Working** — a set stores items in a hash table, which automatically prevents duplicates and makes membership checks fast.

⚠️ **Common Mistakes & Errors**
> `{}` makes an empty **dict**, not a set! For an empty set, use `set()`.

💡 **Hint**
> Sets have no order, so don't rely on the items printing in a fixed sequence.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(set([1, 2, 2, 3]))      # {1, 2, 3}
print(set("hello"))           # {'h','e','l','o'} -> unique letters
print({1, 2} | {2, 3})        # {1, 2, 3}  -> union (all)
print({1, 2, 3} & {2, 3, 4})  # {2, 3}     -> intersection (shared)
print(len(set([1, 1, 1])))    # 1          -> one unique item
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Count Unique Visitors</b></summary>

```python
visits = ["Ann", "Ben", "Ann", "Cara", "Ben", "Ann"]  # log with repeats
unique_visitors = set(visits)                           # drop repeats
print(f"Total visits: {len(visits)}")
print(f"Unique visitors: {len(unique_visitors)}")
```
**Output:**
```text
Total visits: 6
Unique visitors: 3
```
The log has 6 visits, but only 3 different people.

✏️ **Your turn:** print the sorted unique names with `sorted(unique_visitors)`.
</details>

🔗 **See Also** — `list()` · `frozenset()` · `dict()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="setattr"></a>
## 📥 `setattr()` &nbsp;<sub>🟡 Intermediate</sub>

> 🎯 **Objective —** Set (or add) a named piece of data on an object.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| Nothing (`None`) | Objects | `getattr()` · `hasattr()` · `delattr()` |

📖 **Description** — `setattr()` puts a value on an object under a given name. If the attribute exists it's updated; if not, it's created. The name is given as text.

🏷️ **Concepts** — `objects` · `attributes` · `setting data`

🧭 **What · Why · When · How**
- **What** — sets `object.attribute = value` using the name as text.
- **Why** — handy when the attribute name is decided at runtime.
- **When** — building or updating object data dynamically.
- **How** — `setattr(object, "name", value)`.

⌨️ **Syntax**
```python
setattr(object, "attribute_name", value)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `object` | the object to change | ✅ Yes |
| `attribute_name` | the attribute name, as text | ✅ Yes |
| `value` | what to store | ✅ Yes |

↩️ **Return Value** — nothing (`None`); it changes the object in place.

🔍 **Line-by-Line Explanation**
```python
import types
person = types.SimpleNamespace(name="Sam")  # an object with one attribute
setattr(person, "age", 30)                   # add a new attribute 'age'
print(person)                                # now it has name AND age
```
> • start with an object that has `name`
> • `setattr(person, "age", 30)` adds `age`
> • printing shows both attributes

▶️ **Output & Output Explanation**
```text
namespace(name='Sam', age=30)
```
The `age` attribute was created and set to `30`.

⚙️ **Internal Working** — Python calls the object's `__setattr__`, storing the name/value pair in the object's internal data.

⚠️ **Common Mistakes & Errors**
> `setattr(person, age, 30)` without quotes around `age` → looks for a variable `age`. Use `"age"` (text).

💡 **Hint**
> `setattr(obj, "x", 5)` is the same as writing `obj.x = 5`.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
import types
p = types.SimpleNamespace()
setattr(p, "name", "Lily")     # add name
setattr(p, "age", 22)          # add age
print(p)                       # namespace(name='Lily', age=22)
setattr(p, "age", 23)          # update age
print(getattr(p, "age"))       # 23
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Build a Profile Step by Step</b></summary>

```python
import types
profile = types.SimpleNamespace()         # start empty
setattr(profile, "name", "Maya")          # add fields one by one
setattr(profile, "city", "Lisbon")
print(f"{profile.name} lives in {profile.city}")
```
**Output:** `Maya lives in Lisbon`
We added each field with `setattr`, then read them back.

✏️ **Your turn:** add an `age` field with `setattr` and print it.
</details>

🔗 **See Also** — `getattr()` · `hasattr()` · `delattr()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="slice"></a>
## ✂️ `slice()` &nbsp;<sub>🟡 Intermediate</sub>

> 🎯 **Objective —** Make a reusable "cut" you can apply to lists or text.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A slice object | Collections | `range()` · `list()` · `reversed()` |

📖 **Description** — `slice()` builds a slice object describing *start*, *stop*, and *step*. You usually slice with `[1:4]`, but `slice()` lets you save that "cut" in a variable and reuse it.

🏷️ **Concepts** — `slicing` · `start/stop/step` · `sequences`

🧭 **What · Why · When · How**
- **What** — creates a reusable slice (a saved `[start:stop:step]`).
- **Why** — to apply the same cut to several sequences.
- **When** — when a particular slice is used repeatedly.
- **How** — `slice(start, stop, step)`, then `sequence[my_slice]`.

⌨️ **Syntax**
```python
slice(start, stop, step)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `start` | first index | ⬜ Optional |
| `stop` | one past the last index | ✅ Yes |
| `step` | step size | ⬜ Optional |

↩️ **Return Value** — a slice object you can use inside `[ ]`.

🔍 **Line-by-Line Explanation**
```python
middle = slice(1, 4)     # a saved cut: positions 1, 2, 3
print("hello"[middle])   # apply it to text -> ell
print([10,20,30,40,50][middle])  # apply the SAME cut to a list
```
> • `slice(1, 4)` saves the cut "from 1 up to 4"
> • `"hello"[middle]` gives `"ell"`
> • the same `middle` works on a list too

▶️ **Output & Output Explanation**
```text
ell
[20, 30, 40]
```
The same slice picks positions 1–3 from both the text and the list.

⚙️ **Internal Working** — `sequence[1:4]` is actually shorthand for `sequence[slice(1, 4)]`; `slice()` just lets you name and reuse that object.

⚠️ **Common Mistakes & Errors**
> Like normal slicing, `stop` is **excluded**: `slice(1, 4)` covers positions 1, 2, 3 — not 4.

💡 **Hint**
> For one-off cuts, just use `[1:4]`. Use `slice()` only when you reuse the same cut.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
s = slice(0, 3)
print("python"[s])              # pyt
print([1, 2, 3, 4, 5][s])       # [1, 2, 3]
print("abcdef"[slice(0, 6, 2)]) # ace  -> every 2nd character
print("hello"[slice(2, None)])  # llo  -> from 2 to the end
print("hello"[slice(None, 2)])  # he   -> from start to 2
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Reusable First-Three Cut</b></summary>

```python
first_three = slice(0, 3)                  # a reusable cut for "first 3"
print("Code:", "ABCDEFG"[first_three])      # ABC
print("List:", [9, 8, 7, 6, 5][first_three])# [9, 8, 7]
```
**Output:**
```text
Code: ABC
List: [9, 8, 7]
```
One saved slice grabs the first three items from any sequence.

✏️ **Your turn:** make a `last_two = slice(-2, None)` and apply it to a word.
</details>

🔗 **See Also** — `range()` · `list()` · `reversed()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="sorted"></a>
## 🔃 `sorted()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Get a new, sorted version of a collection.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A new sorted list | Collections | `reversed()` · `min()` · `max()` |

📖 **Description** — `sorted()` returns a **new** list with the items in order (smallest to largest, or A–Z). The original is left unchanged. Add `reverse=True` for descending order.

🏷️ **Concepts** — `sorting` · `order` · `lists`

🧭 **What · Why · When · How**
- **What** — produces a sorted copy of items.
- **Why** — to arrange data in order.
- **When** — rankings, alphabetical lists, tidy output.
- **How** — `sorted(items)` or `sorted(items, reverse=True)`.

⌨️ **Syntax**
```python
sorted(iterable, reverse=False)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `iterable` | the items to sort | ✅ Yes |
| `reverse` | `True` for largest-first | ⬜ Optional (default `False`) |
| `key` | a rule to sort by (advanced) | ⬜ Optional |

↩️ **Return Value** — a new sorted list.

🔍 **Line-by-Line Explanation**
```python
nums = [3, 1, 2]          # an unsorted list
ordered = sorted(nums)    # make a sorted COPY
print(ordered)            # the sorted version
print(nums)               # original is UNCHANGED
```
> • `sorted(nums)` returns a new list `[1, 2, 3]`
> • the original `nums` stays `[3, 1, 2]`

▶️ **Output & Output Explanation**
```text
[1, 2, 3]
[3, 1, 2]
```
`sorted()` gives a sorted copy; the original list is untouched.

⚙️ **Internal Working** — Python uses an efficient sorting method (Timsort) to order the items into a brand-new list.

⚠️ **Common Mistakes & Errors**
> `sorted([1, "a"])` → **TypeError**: you can't compare numbers and text. Sort items of the same type.

💡 **Hint**
> `sorted()` returns a new list; `list.sort()` changes the list in place. Use `sorted()` to keep the original.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(sorted([3, 1, 2]))               # [1, 2, 3]
print(sorted([3, 1, 2], reverse=True)) # [3, 2, 1]
print(sorted(["banana", "apple"]))     # ['apple', 'banana']
print(sorted("dcba"))                  # ['a', 'b', 'c', 'd']
print(sorted([3, 1, 2])[0])            # 1 -> the smallest
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Leaderboard</b></summary>

```python
scores = [55, 91, 72, 88, 64]                  # everyone's scores
ranked = sorted(scores, reverse=True)          # highest first
print(f"Ranked: {ranked}")
print(f"Winner scored: {ranked[0]}")
```
**Output:**
```text
Ranked: [91, 88, 72, 64, 55]
Winner scored: 91
```
`reverse=True` ranks high-to-low; the first item is the top score.

✏️ **Your turn:** sort the names `["Cara", "Ann", "Ben"]` alphabetically.
</details>

🔗 **See Also** — `reversed()` · `min()` · `max()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="staticmethod"></a>
## 🏛️ `staticmethod()` &nbsp;<sub>🔴 Advanced</sub>

> 🎯 **Objective —** Mark a function inside a class as a plain helper (no `self`). *(Needs classes — beginners can skip.)*

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A static method | Classes (advanced) | `classmethod()` · `property()` · `super()` |

📖 **Description** — `staticmethod()` is used *inside classes* (usually as `@staticmethod`) to make a method that doesn't need the object (`self`) — just a regular helper that lives in the class. Because classes use `def`, this is beyond beginner scope.

🏷️ **Concepts** — `classes` · `methods` *(advanced)*

🧭 **What · Why · When · How**
- **What** — turns a method into a plain function inside a class.
- **Why** — to group a helper with a class without needing the object.
- **When** — only when writing classes (a later topic).
- **How** — written as `@staticmethod` above a method (needs `def`).

⌨️ **Syntax**
```python
# Used as a decorator inside a class (needs def + class):
# @staticmethod
# def add(a, b): ...
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `function` | the method to convert | ✅ Yes |

↩️ **Return Value** — a static-method object.

🔍 **Line-by-Line Explanation**
```python
# Conceptual — requires a class (which uses def):
# class Math:
#     @staticmethod
#     def add(a, b):
#         return a + b
```
> • The idea: `add` is grouped with `Math` but needs no object.

▶️ **Output & Output Explanation** — no simple beginner output; it only makes sense inside a class.

⚙️ **Internal Working** — it wraps the function so Python does *not* pass the object (`self`) when it's called.

⚠️ **Common Mistakes & Errors**
> Trying to use it outside a class — it only has meaning *inside* a `class` block.

💡 **Hint**
> Skip until you've learned `def` and `class`.

<details>
<summary>📚 <b>5 Examples</b> (conceptual — need a class)</summary>

```python
# 1. @staticmethod makes a method that ignores 'self'
# 2. it behaves like a normal function inside the class
# 3. used for helpers related to the class
# 4. partners: classmethod, property
# 5. you'll use it after learning classes
```
</details>

<details>
<summary>🛠️ <b>Mini Project</b></summary>

*Not beginner-appropriate — needs classes (`def`/`class`). Revisit after the classes chapter.*
</details>

🔗 **See Also** — `classmethod()` · `property()` · `super()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="str"></a>
## 🔤 `str()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Turn any value into text.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A string (text) | Text | `int()` · `float()` · `repr()` |

📖 **Description** — `str()` converts any value into a string (text). It's essential when you want to join a number with words using `+`.

🏷️ **Concepts** — `strings` · `type conversion` · `text`

🧭 **What · Why · When · How**
- **What** — makes text from any value.
- **Why** — you can only glue text to text with `+`; numbers must become text first.
- **When** — building messages, saving values as text.
- **How** — `str(value)`.

⌨️ **Syntax**
```python
str(value)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `value` | any value to turn into text | ⬜ Optional (empty = `""`) |

↩️ **Return Value** — a string (text).

🔍 **Line-by-Line Explanation**
```python
age = 30                       # a number
message = "Age: " + str(age)   # turn 30 into "30" so + works
print(message)                 # show the joined text
```
> • `"Age: " + 30` would error (text + number)
> • `str(30)` makes `"30"`, so the `+` works
> • prints `Age: 30`

▶️ **Output & Output Explanation**
```text
Age: 30
```
The number `30` became the text `"30"`, then joined onto `"Age: "`.

⚙️ **Internal Working** — Python calls the value's `__str__` method, which returns its human-friendly text form.

⚠️ **Common Mistakes & Errors**
> `"Total: " + 5` → **TypeError**. Convert the number: `"Total: " + str(5)` (or use an f-string).

💡 **Hint**
> f-strings convert for you: `f"Age: {age}"` needs no `str()`.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(str(42))          # '42'
print(str(3.5))         # '3.5'
print(str([1, 2]))      # '[1, 2]'
print(str(True))        # 'True'
print("Score: " + str(95))  # Score: 95
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Build a Label</b></summary>

```python
product = "Apple"
price = 2
label = product + " costs $" + str(price)   # join text and a number
print(label)
```
**Output:** `Apple costs $2`
`str(price)` turns the number into text so it can join with `+`.

✏️ **Your turn:** rewrite the label using an f-string (no `str()` needed).
</details>

🔗 **See Also** — `int()` · `float()` · `repr()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="sum"></a>
## ➕ `sum()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Add up all the numbers in a list.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| The total (a number) | Numbers/Collections | `len()` · `max()` · `min()` |

📖 **Description** — `sum()` adds together all the numbers in a collection and returns the total. You can also give a starting value.

🏷️ **Concepts** — `numbers` · `totals` · `collections`

🧭 **What · Why · When · How**
- **What** — adds all numbers in a list.
- **Why** — totals and averages.
- **When** — bills, scores, any running total.
- **How** — `sum(my_list)`.

⌨️ **Syntax**
```python
sum(iterable, start=0)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `iterable` | the numbers to add | ✅ Yes |
| `start` | a value to start the total from | ⬜ Optional (default 0) |

↩️ **Return Value** — the total (a number).

🔍 **Line-by-Line Explanation**
```python
scores = [10, 20, 30]   # three numbers
total = sum(scores)     # add them all up
print(total)            # show the total -> 60
```
> • `sum([10, 20, 30])` adds them
> • the total is `60`
> • prints `60`

▶️ **Output & Output Explanation**
```text
60
```
`10 + 20 + 30` equals `60`.

⚙️ **Internal Working** — Python starts from `start` (default 0) and adds each item to a running total, returning it at the end.

⚠️ **Common Mistakes & Errors**
> `sum(["1", "2"])` → **TypeError**: it adds *numbers*, not text. Convert first (e.g. with `map(int, ...)`).

💡 **Hint**
> Average = `sum(list) / len(list)`.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(sum([1, 2, 3]))          # 6
print(sum([1.5, 2.5]))         # 4.0
print(sum(range(1, 6)))        # 15  -> 1+2+3+4+5
print(sum([1, 2, 3], 100))     # 106 -> starts the total at 100
print(sum([10, 20]) / 2)       # 15.0 -> average of two numbers
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Class Average</b></summary>

```python
scores = [70, 85, 90, 65]                 # the class scores
total = sum(scores)                        # add them all
average = total / len(scores)              # divide by how many
print(f"Total: {total}, Average: {average:.1f}")
```
**Output:** `Total: 310, Average: 77.5`
`sum()` totals the scores; dividing by `len()` gives the average.

✏️ **Your turn:** add a 5th score of `95` and re-run.
</details>

🔗 **See Also** — `len()` · `max()` · `min()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="super"></a>
## 🏛️ `super()` &nbsp;<sub>🔴 Advanced</sub>

> 🎯 **Objective —** Call a method from a "parent" class. *(Needs classes — beginners can skip.)*

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A proxy to the parent class | Classes (advanced) | `classmethod()` · `staticmethod()` · `property()` |

📖 **Description** — `super()` is used *inside classes* to call methods of a parent class (the class a new class is built on). Because classes use `def`, this is beyond beginner scope — you'll meet it after the classes chapter.

🏷️ **Concepts** — `classes` · `inheritance` *(advanced)*

🧭 **What · Why · When · How**
- **What** — accesses the parent class's version of a method.
- **Why** — to build on (extend) a parent class.
- **When** — only when writing classes that inherit from others.
- **How** — `super().method()` inside a class (needs `def`).

⌨️ **Syntax**
```python
# Used inside a class (needs def + class):
# super().__init__()
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| *(usually none)* | modern usage takes no arguments | — |

↩️ **Return Value** — a special object that forwards calls to the parent class.

🔍 **Line-by-Line Explanation**
```python
# Conceptual — requires classes (which use def):
# class Animal: ...
# class Dog(Animal):
#     def __init__(self):
#         super().__init__()   # run the parent's setup too
```
> • The idea: `super()` lets a child class reuse its parent's behaviour.

▶️ **Output & Output Explanation** — no simple beginner output; it only makes sense inside classes.

⚙️ **Internal Working** — it finds the next class in the inheritance chain and forwards your method call to it.

⚠️ **Common Mistakes & Errors**
> Using it outside a class — it only has meaning *inside* a `class` that inherits from another.

💡 **Hint**
> Skip until you've learned `def`, `class`, and inheritance.

<details>
<summary>📚 <b>5 Examples</b> (conceptual — need classes)</summary>

```python
# 1. super() calls the parent class's method
# 2. common in __init__ to run the parent's setup
# 3. used when one class is built on another
# 4. partners: classmethod, staticmethod, property
# 5. you'll use it after learning inheritance
```
</details>

<details>
<summary>🛠️ <b>Mini Project</b></summary>

*Not beginner-appropriate — needs classes and inheritance (`def`/`class`). Revisit after the classes chapter.*
</details>

🔗 **See Also** — `classmethod()` · `staticmethod()` · `property()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

# T – Z

<a id="tuple"></a>
## 📦 `tuple()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Make a *tuple* — a fixed (unchangeable) ordered collection.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A tuple | Collections | `list()` · `set()` · `zip()` |

📖 **Description** — `tuple()` builds a tuple: like a list but **unchangeable**. Once made, its items can't be added to or replaced — which makes it safe for data that shouldn't change.

🏷️ **Concepts** — `tuples` · `fixed collections` · `immutability`

🧭 **What · Why · When · How**
- **What** — makes an ordered, unchangeable collection.
- **Why** — for fixed groups (coordinates, RGB colours) that shouldn't change.
- **When** — when data must stay constant, or as a dict key.
- **How** — `tuple(items)` or `(1, 2, 3)`.

⌨️ **Syntax**
```python
tuple(iterable)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `iterable` | items to put in the tuple | ⬜ Optional (empty = `()`) |

↩️ **Return Value** — a tuple of the items.

🔍 **Line-by-Line Explanation**
```python
point = tuple([10, 20])   # build a tuple from a list
print(point)              # show it -> (10, 20)
print(point[0])           # read an item by position -> 10
```
> • `tuple([10, 20])` makes `(10, 20)`
> • printing shows `(10, 20)`
> • `point[0]` reads the first item, `10`

▶️ **Output & Output Explanation**
```text
(10, 20)
10
```
The list became a fixed tuple; you can still read items by position.

⚙️ **Internal Working** — Python stores the items in a fixed-size, read-only structure, which is slightly lighter than a list.

⚠️ **Common Mistakes & Errors**
> A one-item tuple needs a comma: `(5,)` is a tuple, but `(5)` is just the number `5`.

💡 **Hint**
> Use a tuple for "this shouldn't change"; use a list when you'll edit it.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(tuple([1, 2, 3]))   # (1, 2, 3)
print(tuple("abc"))       # ('a', 'b', 'c')
print(tuple())            # ()        -> empty tuple
print(tuple(range(3)))    # (0, 1, 2)
print((5,))               # (5,)      -> one-item tuple (note the comma)
```
</details>

<details>
<summary>🛠️ <b>Mini Project — A Fixed Coordinate</b></summary>

```python
location = tuple([40, 70])              # a fixed (x, y) point
x, y = location                         # unpack it into two variables
print(f"x = {x}, y = {y}")
# location[0] = 99  # this would ERROR -> tuples can't change
```
**Output:** `x = 40, y = 70`
The coordinate is safely fixed, and we unpack it into `x` and `y`.

✏️ **Your turn:** make an RGB colour tuple like `(255, 0, 0)` and unpack it into `r, g, b`.
</details>

🔗 **See Also** — `list()` · `set()` · `zip()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="type"></a>
## 🏷️ `type()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Find out what kind of value something is.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| The value's type | Inspection | `isinstance()` · `dir()` · `id()` |

📖 **Description** — `type()` tells you a value's type (like `int`, `str`, `list`). It's one of the most useful tools for understanding and debugging your data. *(It can also build classes — an advanced use beginners can ignore.)*

🏷️ **Concepts** — `types` · `inspection`

🧭 **What · Why · When · How**
- **What** — reports a value's type.
- **Why** — to understand or debug what you're working with.
- **When** — when a value behaves unexpectedly.
- **How** — `type(value)`.

⌨️ **Syntax**
```python
type(value)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `value` | the value to inspect | ✅ Yes |

↩️ **Return Value** — the value's type (e.g. `<class 'int'>`).

🔍 **Line-by-Line Explanation**
```python
x = 5                       # a whole number
print(type(x))              # show its type -> <class 'int'>
print(type(x).__name__)     # just the short name -> int
```
> • `type(5)` is `<class 'int'>`
> • `.__name__` gives the clean name `int`

▶️ **Output & Output Explanation**
```text
<class 'int'>
int
```
`type()` shows the full type; `.__name__` gives the short, tidy name.

⚙️ **Internal Working** — every object stores a link to its type; `type()` simply returns that link.

⚠️ **Common Mistakes & Errors**
> For *checking* a type, prefer `isinstance(x, int)` over `type(x) == int` — it's the recommended way and also handles subtypes.

💡 **Hint**
> Add `.__name__` for a clean printout: `type(x).__name__` gives `int`, not `<class 'int'>`.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(type(5).__name__)        # int
print(type("hi").__name__)     # str
print(type(3.5).__name__)      # float
print(type([1, 2]).__name__)   # list
print(type(True).__name__)     # bool
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Identify a Value</b></summary>

```python
value = 3.14                                   # try "hi", [1,2], or True
print(f"The value {value} is of type {type(value).__name__}")
```
**Output:** `The value 3.14 is of type float`
`type(value).__name__` cleanly reports the kind of value.

✏️ **Your turn:** set `value = [1, 2, 3]` and re-run.
</details>

🔗 **See Also** — `isinstance()` · `dir()` · `id()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="vars"></a>
## 📒 `vars()` &nbsp;<sub>🟡 Intermediate</sub>

> 🎯 **Objective —** See an object's attributes as a dictionary.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| A dictionary of attributes | Inspection | `dir()` · `getattr()` · `locals()` |

📖 **Description** — `vars(object)` returns the object's attributes as a `name → value` dictionary. With no argument, it acts like `locals()`. It's handy for quickly seeing what data an object holds.

🏷️ **Concepts** — `objects` · `attributes` · `dictionaries`

🧭 **What · Why · When · How**
- **What** — shows an object's stored attributes as a dict.
- **Why** — to inspect an object's data at a glance.
- **When** — debugging, printing an object's contents.
- **How** — `vars(object)`.

⌨️ **Syntax**
```python
vars(object)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `object` | the object to inspect | ⬜ Optional |

↩️ **Return Value** — a dictionary of the object's attributes.

🔍 **Line-by-Line Explanation**
```python
import types
person = types.SimpleNamespace(name="Sam", age=30)  # object with 2 attributes
print(vars(person))     # see its attributes as a dict
```
> • the object has `name` and `age`
> • `vars(person)` shows them as a dictionary

▶️ **Output & Output Explanation**
```text
{'name': 'Sam', 'age': 30}
```
The object's attributes are shown as `name → value` pairs.

⚙️ **Internal Working** — it returns the object's `__dict__`, the dictionary where its attributes are actually stored.

⚠️ **Common Mistakes & Errors**
> `vars(5)` → **TypeError**: simple values like numbers don't have an attribute dictionary.

💡 **Hint**
> `vars(obj)` is a quick way to *print everything* an object is storing.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
import types
p = types.SimpleNamespace(x=1, y=2)
print(vars(p))                 # {'x': 1, 'y': 2}
print(list(vars(p).keys()))    # ['x', 'y']
print(vars(p)["x"])            # 1
print(type(vars(p)).__name__)  # dict
q = types.SimpleNamespace()
print(vars(q))                 # {} -> no attributes yet
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Print a Whole Profile</b></summary>

```python
import types
profile = types.SimpleNamespace(name="Maya", city="Lisbon", age=24)
for field, value in vars(profile).items():   # go through each attribute
    print(f"{field}: {value}")
```
**Output:**
```text
name: Maya
city: Lisbon
age: 24
```
`vars()` turns the object into a dict so we can print every field.

✏️ **Your turn:** add an `email` attribute and re-run — it appears automatically.
</details>

🔗 **See Also** — `dir()` · `getattr()` · `locals()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="zip"></a>
## 🤐 `zip()` &nbsp;<sub>🟢 Beginner</sub>

> 🎯 **Objective —** Pair up items from two (or more) lists, position by position.

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| Pairs of items | Collections | `enumerate()` · `dict()` · `map()` |

📖 **Description** — `zip()` takes two or more lists and joins their items into pairs, matching by position. It's perfect when two lists "line up" — like names and scores.

🏷️ **Concepts** — `lists` · `pairing` · `tuples`

🧭 **What · Why · When · How**
- **What** — combines lists into matched pairs.
- **Why** — to work with related lists together.
- **When** — names + values, keys + values, columns of data.
- **How** — `zip(list_a, list_b)`.

⌨️ **Syntax**
```python
zip(iterable_a, iterable_b, ...)
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `iterables` | two or more lists/tuples/etc. to pair | ✅ Yes |

↩️ **Return Value** — a zip object of pairs (wrap in `list()` or `dict()` to see).

🔍 **Line-by-Line Explanation**
```python
names = ["Ann", "Ben"]          # one list
scores = [90, 85]               # a matching list
paired = list(zip(names, scores))  # pair them by position
print(paired)                   # show the pairs
```
> • two lists that line up
> • `zip(names, scores)` pairs Ann↔90 and Ben↔85
> • prints `[('Ann', 90), ('Ben', 85)]`

▶️ **Output & Output Explanation**
```text
[('Ann', 90), ('Ben', 85)]
```
Each name is paired with the score at the same position.

⚙️ **Internal Working** — `zip` walks all lists at once, grabbing one item from each per step, and stops when the **shortest** list runs out.

⚠️ **Common Mistakes & Errors**
> If the lists are different lengths, `zip` stops at the **shorter** one (extra items are dropped). Make sure they match.

💡 **Hint**
> `dict(zip(keys, values))` is a quick way to build a dictionary from two lists.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
print(list(zip(["a", "b"], [1, 2])))        # [('a', 1), ('b', 2)]
print(dict(zip(["x", "y"], [10, 20])))      # {'x': 10, 'y': 20}
print(list(zip([1, 2, 3], ["a", "b", "c"])))# [(1,'a'), (2,'b'), (3,'c')]
print(list(zip([1, 2, 3], ["a"])))          # [(1, 'a')] -> stops at shortest
print(list(zip("ab", "12")))                # [('a','1'), ('b','2')]
```
</details>

<details>
<summary>🛠️ <b>Mini Project — Name and Score Report</b></summary>

```python
names = ["Ann", "Ben", "Cara"]                       # two lists that line up
scores = [88, 72, 95]
lines = [f"{name}: {score}" for name, score in zip(names, scores)]
print("\n".join(lines))
```
**Output:**
```text
Ann: 88
Ben: 72
Cara: 95
```
`zip()` pairs each name with its score so we can print them together.

✏️ **Your turn:** add `"Dan"` and a 4th score, then re-run.
</details>

🔗 **See Also** — `enumerate()` · `dict()` · `map()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<a id="__import__"></a>
## 📦 `__import__()` &nbsp;<sub>🔴 Advanced</sub>

> 🎯 **Objective —** Load a module by its name given as text. *(Advanced — use the `import` statement instead.)*

📋 **Quick Facts**

| ↩️ Returns | 🏷️ Category | 🔗 Related |
|:--|:--|:--|
| The imported module | Advanced | `import` statement · `dir()` · `help()` |

📖 **Description** — `__import__()` is the low-level function behind the normal `import` statement. You'll almost never call it directly — the friendly `import math` does the same thing more clearly.

🏷️ **Concepts** — `modules` · `importing` *(advanced)*

🧭 **What · Why · When · How**
- **What** — loads a module whose name is in a string.
- **Why** — rarely, when the module name is only known at runtime.
- **When** — advanced tools; almost never as a beginner.
- **How** — `__import__("module_name")`.

⌨️ **Syntax**
```python
__import__("module_name")
```

🎛️ **Parameters**

| Parameter | What it is | Required? |
|:--|:--|:--|
| `name` | the module's name, as text | ✅ Yes |

↩️ **Return Value** — the imported module object.

🔍 **Line-by-Line Explanation**
```python
math = __import__("math")  # load the 'math' module by name
print(math.sqrt(16))       # use it -> 4.0
```
> • `__import__("math")` loads the math module
> • `math.sqrt(16)` works just like after a normal import → `4.0`

▶️ **Output & Output Explanation**
```text
4.0
```
The math module loaded, and `sqrt(16)` gave `4.0`.

⚙️ **Internal Working** — it finds the module, runs it once if needed, caches it, and returns the module object. The `import` statement calls this for you.

⚠️ **Common Mistakes & Errors**
> Using `__import__()` instead of `import` makes code harder to read. For everyday use, just write `import math`.

💡 **Hint**
> Prefer the normal statement: `import math` — clearer and what everyone expects.

<details>
<summary>📚 <b>5 Examples</b></summary>

```python
m = __import__("math")
print(m.pi)                 # 3.141592653589793
print(m.sqrt(25))           # 5.0
r = __import__("random")
print(type(r).__name__)     # module
# the normal, preferred way is simply:  import math
print(__import__("math").floor(3.7))  # 3
```
</details>

<details>
<summary>🛠️ <b>Mini Project</b></summary>

*Not recommended for beginners — use the clear `import` statement (e.g. `import math`) instead of `__import__()`.*
</details>

🔗 **See Also** — `import` statement · `dir()` · `help()`

<p align="right"><a href="#-table-of-contents">⬆ Back to top</a></p>

---

<div align="center">

# 🎉 That's all 71 built-in functions!

</div>

> 🏁 **You made it!** You now have a beginner-friendly reference for every one of
> Python's 71 built-in functions. Bookmark the ones you use most, and revisit the
> 🔴 advanced ones after you learn `def`, classes, and async.

<br>

## 📇 Quick Reference Cheat-Sheet

A one-line reminder of each function, grouped by what it's for.
🟢 Beginner · 🟡 Intermediate · 🔴 Advanced

### 🔢 Numbers
| Function | One-liner | Level |
|:--|:--|:--:|
| `abs()` | size of a number (drops the sign) | 🟢 |
| `bin()` | number → binary text (`0b…`) | 🟢 |
| `oct()` | number → octal text (`0o…`) | 🟢 |
| `hex()` | number → hex text (`0x…`) | 🟢 |
| `int()` | make a whole number | 🟢 |
| `float()` | make a decimal number | 🟢 |
| `complex()` | make a complex number (`3+4j`) | 🟡 |
| `pow()` | raise to a power | 🟢 |
| `round()` | round a number | 🟢 |
| `divmod()` | quotient **and** remainder | 🟢 |

### 🔤 Text
| Function | One-liner | Level |
|:--|:--|:--:|
| `str()` | turn anything into text | 🟢 |
| `chr()` | number → character | 🟢 |
| `ord()` | character → number | 🟢 |
| `ascii()` | text with non-English chars as codes | 🟢 |
| `repr()` | developer form of a value | 🟡 |
| `format()` | format a value as text | 🟡 |

### ✅ Logic / True-False
| Function | One-liner | Level |
|:--|:--|:--:|
| `bool()` | turn a value into True/False | 🟢 |
| `all()` | are **all** items true? | 🟢 |
| `any()` | is **any** item true? | 🟢 |

### 📦 Collections
| Function | One-liner | Level |
|:--|:--|:--:|
| `list()` | make a list (changeable) | 🟢 |
| `tuple()` | make a tuple (fixed) | 🟢 |
| `set()` | make a set (unique items) | 🟢 |
| `frozenset()` | make a fixed set | 🟡 |
| `dict()` | make a dictionary (key→value) | 🟢 |
| `len()` | count items | 🟢 |
| `sum()` | add up numbers | 🟢 |
| `min()` | smallest item | 🟢 |
| `max()` | largest item | 🟢 |
| `sorted()` | sorted copy | 🟢 |
| `reversed()` | go backwards | 🟢 |
| `range()` | sequence of numbers | 🟢 |
| `enumerate()` | pair items with positions | 🟢 |
| `zip()` | pair up two lists | 🟢 |
| `map()` | apply a function to each item | 🟡 |
| `filter()` | keep items that pass a test | 🟡 |
| `slice()` | a reusable cut | 🟡 |
| `iter()` | make an iterator | 🟡 |
| `next()` | get the next item | 🟡 |

### 🖥️ Input / Output / Files
| Function | One-liner | Level |
|:--|:--|:--:|
| `print()` | show things on screen | 🟢 |
| `input()` | read what the user types | 🟢 |
| `open()` | open a file to read/write | 🟡 |

### 🔎 Inspection / Learning
| Function | One-liner | Level |
|:--|:--|:--:|
| `type()` | what kind of value is it? | 🟢 |
| `isinstance()` | is it of this type? | 🟢 |
| `issubclass()` | is this type built on that one? | 🟡 |
| `help()` | show built-in documentation | 🟢 |
| `dir()` | list what a value can do | 🟡 |
| `id()` | unique identity number | 🟡 |
| `hash()` | number fingerprint | 🟡 |
| `callable()` | can it be called with `()`? | 🟡 |
| `repr()` | precise developer text | 🟡 |
| `vars()` | object's attributes as a dict | 🟡 |

### 🧩 Objects / Attributes
| Function | One-liner | Level |
|:--|:--|:--:|
| `getattr()` | read an attribute by name | 🟡 |
| `setattr()` | set an attribute by name | 🟡 |
| `hasattr()` | does it have this attribute? | 🟡 |
| `delattr()` | remove an attribute | 🟡 |
| `object()` | the base object of everything | 🔴 |

### 🔴 Advanced (revisit later)
| Function | One-liner | Why later |
|:--|:--|:--|
| `classmethod()` | method tied to a class | needs classes |
| `staticmethod()` | plain helper in a class | needs classes |
| `property()` | method that acts like an attribute | needs classes |
| `super()` | call a parent class's method | needs classes |
| `aiter()` | async iterator | needs async |
| `anext()` | async next item | needs async |
| `eval()` | run an expression from text | risky |
| `exec()` | run statements from text | risky |
| `compile()` | prepare code from text | risky |
| `globals()` | dict of global variables | advanced |
| `locals()` | dict of local variables | advanced |
| `memoryview()` | no-copy view of bytes | advanced |
| `breakpoint()` | open the debugger | debugging |
| `bytes()` | fixed raw bytes | binary data |
| `bytearray()` | editable raw bytes | binary data |
| `__import__()` | load a module by name | use `import` |

<br>

<div align="center">

**Happy coding! 🐍**
*Start with the 🟢 functions, practise the mini-projects, and grow from there.*

</div>