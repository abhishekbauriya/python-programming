<div align="center">

# 🐍 Python Built-in Function
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
