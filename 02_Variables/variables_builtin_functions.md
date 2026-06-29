# Python Built-in Functions — Beginner-Friendly DevOps Edition

> **`python-programming` · Chapter 02 · Variables & Built-in Functions**
>
> All **71 Python built-in functions**, rewritten for people who are **new to Python**
> but know cloud/DevOps. Every function includes:
>
> **What it does (plain English) · Syntax · Parameters · What you get back ·
> 5 examples (each with output + explanation) · Common mistakes (with the fix) ·
> Real-world use case (Problem → Solution → walkthrough) · Mini-project (with full solution).**
>
> Target: **Python 3.10+**.
---


## How to read this handbook (for beginners)

Each example follows the same simple rhythm so nothing is left as a mystery:

```python
# 1. The code you run
result = abs(-5)
print(result)
```
**Output:**
```
5
```
**What happened:** `abs(-5)` removed the minus sign and gave back `5`. We stored that
in a variable called `result`, then `print()` showed it on screen.

A few terms you'll see a lot:
- **"Return / get back"** = the value a function hands back to you so you can store or print it.
- **"Iterable"** = anything you can loop over: a list `[1, 2, 3]`, a string `"abc"`, a range, etc.
- **"Argument / parameter"** = the value you put inside the `()` when calling a function.
- 🔧 = you'll use this one constantly. ⚠️ = handle with care (security-sensitive).

> Cloud snippets use AWS concepts (because you know them) but explain the Python part.
> Where they call an SDK like Boto3, that line is illustrative — swap in real
> credentials/clients to actually run it. Everything else runs as shown.

---



## Table of Contents

**A–B:** [abs](#abs) · [aiter](#aiter) · [all](#all-🔧) · [anext](#anext) · [any](#any-🔧) · [ascii](#ascii) · [bin](#bin) · [bool](#bool) · [breakpoint](#breakpoint) · [bytearray](#bytearray) · [bytes](#bytes)

**C–D:** [callable](#callable) · [chr](#chr) · [classmethod](#classmethod) · [compile](#compile) · [complex](#complex) · [delattr](#delattr) · [dict](#dict-🔧) · [dir](#dir) · [divmod](#divmod)

**E–F:** [enumerate](#enumerate-🔧) · [eval](#eval-⚠️) · [exec](#exec-⚠️) · [filter](#filter-🔧) · [float](#float) · [format](#format) · [frozenset](#frozenset)

**G–H:** [getattr](#getattr-🔧) · [globals](#globals) · [hasattr](#hasattr) · [hash](#hash) · [help](#help) · [hex](#hex)

**I:** [id](#id) · [input](#input) · [int](#int-🔧) · [isinstance](#isinstance-🔧) · [issubclass](#issubclass) · [iter](#iter)

**L–N:** [len](#len-🔧) · [list](#list-🔧) · [locals](#locals) · [map](#map-🔧) · [max](#max-🔧) · [memoryview](#memoryview) · [min](#min-🔧) · [next](#next)

**O–P:** [object](#object) · [oct](#oct) · [open](#open-🔧) · [ord](#ord) · [pow](#pow) · [print](#print-🔧) · [property](#property)

**R–S:** [range](#range-🔧) · [repr](#repr) · [reversed](#reversed) · [round](#round) · [set](#set-🔧) · [setattr](#setattr) · [slice](#slice) · [sorted](#sorted-🔧) · [staticmethod](#staticmethod) · [str](#str-🔧) · [sum](#sum-🔧) · [super](#super)

**T–Z:** [tuple](#tuple) · [type](#type-🔧) · [vars](#vars) · [zip](#zip-🔧) · [\_\_import\_\_](#__import__)

---



# A–B

## `abs()`

**What it does (plain English):** Gives you a number's distance from zero — it just removes the minus sign. `-7` becomes `7`; `7` stays `7`.

**Syntax:** `abs(x)` — read as "give me the absolute value of x".

**Parameters:**
- `x` — any number (a whole number or a decimal).

**What you get back:** A number with no minus sign.

**Examples (with solutions):**

Example 1 — a negative whole number
```python
result = abs(-7)
print(result)
```
**Output:**
```
7
```
**What happened:** The minus sign is dropped, so `-7` becomes `7`.

Example 2 — a positive number stays the same
```python
print(abs(7))
```
**Output:**
```
7
```
**What happened:** `7` is already positive, so nothing changes.

Example 3 — a decimal number
```python
print(abs(-3.5))
```
**Output:**
```
3.5
```
**What happened:** Works on decimals too; the sign is removed.

Example 4 — the difference between two numbers
```python
desired = 5
running = 8
print(abs(desired - running))
```
**Output:**
```
3
```
**What happened:** `5 - 8` is `-3`. `abs()` turns it into `3`, so we get the *size* of the gap without caring which number was bigger.

Example 5 — using it in a comparison
```python
reading = 95
baseline = 50
print(abs(reading - baseline) > 20)
```
**Output:**
```
True
```
**What happened:** `95 - 50` is `45`. `abs(45)` is `45`. Is `45 > 20`? Yes → `True`.

**Common mistakes (and the fix):**
- ❌ `abs("5")` → error, because `"5"` is text, not a number.
  ✅ Convert first: `abs(int("5"))` gives `5`.

**Real-world use case (with full solution):**

**The problem:** Auto Scaling says you should have 5 servers, but right now 2 are running. You want to know *how many* to add or remove — and the answer shouldn't depend on which number is bigger.

**The solution:**
```python
def scaling_action(desired, running):
    gap = abs(desired - running)        # how far off are we?
    if gap == 0:
        return "already correct"
    direction = "add" if desired > running else "remove"
    return f"{direction} {gap} servers"

print(scaling_action(5, 2))
print(scaling_action(2, 6))
```
**How it works, step by step:**
1. `abs(desired - running)` gives the size of the gap (always positive).
2. If the gap is `0`, we're done.
3. We separately decide *direction* by comparing the two numbers.

**Output:**
```
add 3 servers
remove 4 servers
```

**Mini-project (with solution):**

**Your task:** You have CPU readings. Anything more than 20 away from the normal value of 50 is "weird." Print the weird ones.

**Solution:**
```python
readings = [50, 95, 48, 12, 51]
baseline = 50

for r in readings:
    if abs(r - baseline) > 20:
        print(f"anomaly: {r}")
```
**Output:**
```
anomaly: 95
anomaly: 12
```
**Explanation:** For each reading we measure its distance from `50` using `abs()`. `95` is 45 away and `12` is 38 away — both over 20 — so they get flagged. The others are close to 50 and stay quiet.

---

## `aiter()`

**What it does (plain English):** Gives you an *async iterator* — a special looping helper for data that arrives over time (like pages from an API), used inside `async` code. Think of it as the "async version" of normal looping. (This is an advanced topic — skim it if you're brand new and come back later.)

**Syntax:** `aiter(async_iterable)` — "give me an async iterator for this thing I can loop over asynchronously".

**Parameters:**
- `async_iterable` — an object built to be looped over with `async for`.

**What you get back:** An async iterator you pull items from using `await anext(...)`.

**Examples (with solutions):**

Example 1 — set up something we can loop over asynchronously
```python
import asyncio

async def get_pages():          # produces "pages" one at a time
    for n in [1, 2, 3]:
        await asyncio.sleep(0)  # pretend we waited for the network
        yield f"page-{n}"
```
**Output:** *(nothing yet — this just defines the data source)*
**What happened:** `get_pages()` will hand out `page-1`, `page-2`, `page-3` one by one.

Example 2 — loop over it the normal async way
```python
async def main():
    async for page in get_pages():
        print(page)

asyncio.run(main())
```
**Output:**
```
page-1
page-2
page-3
```
**What happened:** `async for` quietly uses `aiter()` behind the scenes to walk through each page.

Example 3 — get the iterator yourself with `aiter()`
```python
async def main():
    it = aiter(get_pages())     # the async iterator
    print(await anext(it))      # pull ONE page

asyncio.run(main())
```
**Output:**
```
page-1
```
**What happened:** `aiter()` gives you the iterator; `await anext(it)` pulls the next item (here, the first page).

Example 4 — collect them all into a list
```python
async def main():
    pages = [p async for p in get_pages()]
    print(pages)

asyncio.run(main())
```
**Output:**
```
['page-1', 'page-2', 'page-3']
```
**What happened:** An "async comprehension" loops over every page and builds a list.

Example 5 — `aiter()` directly inside `async for`
```python
async def main():
    async for p in aiter(get_pages()):
        print(p)

asyncio.run(main())
```
**Output:**
```
page-1
page-2
page-3
```
**What happened:** Same result — `aiter()` is explicit here, but `async for` would have called it anyway.

**Common mistakes (and the fix):**
- ❌ Using `aiter()` in normal (non-async) code → it only works inside `async def` functions.
  ✅ Put your loop inside an `async def` and run it with `asyncio.run(...)`.
- ❌ Forgetting `await` before `anext()` → you get an unfinished task instead of the value.
  ✅ Always write `await anext(it)`.

**Real-world use case (with full solution):**

**The problem:** A cloud API returns results in pages, and you only want the **first** page without waiting to download all of them.

**The solution:**
```python
import asyncio

async def list_buckets():           # pretend cloud pager
    for name in ["logs", "backups", "media"]:
        await asyncio.sleep(0)
        yield name

async def first_bucket():
    it = aiter(list_buckets())      # async iterator
    return await anext(it, None)    # first item, or None if empty

print(asyncio.run(first_bucket()))
```
**How it works, step by step:**
1. `aiter(list_buckets())` gives an async iterator over the bucket names.
2. `await anext(it, None)` pulls just the first one (`None` is a safe fallback if there are none).
3. We never fetch pages 2 and 3 — saving time.

**Output:**
```
logs
```

**Mini-project (with solution):**

**Your task:** Read the first 2 "new log lines" from an async source.

**Solution:**
```python
import asyncio

async def tail():
    for line in ["ERROR disk full", "WARN high cpu", "INFO ok"]:
        await asyncio.sleep(0.05)
        yield line

async def main():
    it = aiter(tail())
    print(await anext(it))   # 1st line
    print(await anext(it))   # 2nd line

asyncio.run(main())
```
**Output:**
```
ERROR disk full
WARN high cpu
```
**Explanation:** `aiter()` gives the iterator; each `await anext(it)` grabs the next line. We stop after two — the third line is never read.

---

## `all()` 🔧

**What it does (plain English):** Checks a list (or any iterable) and returns `True` only if **every single item** is "truthy" (basically: not zero, not empty, not `False`). If even one item fails, you get `False`.

**Syntax:** `all(iterable)` — "are ALL of these true?"

**Parameters:**
- `iterable` — a list/collection of things to check.

**What you get back:** `True` or `False`.

**Examples (with solutions):**

Example 1 — all `True`
```python
print(all([True, True, True]))
```
**Output:**
```
True
```
**What happened:** Every item is `True`, so `all()` is `True`.

Example 2 — one item is falsy
```python
print(all([1, 2, 0, 3]))
```
**Output:**
```
False
```
**What happened:** In Python `0` counts as "false". One false item makes the whole thing `False`.

Example 3 — an empty list (surprising!)
```python
print(all([]))
```
**Output:**
```
True
```
**What happened:** With nothing to check, Python says "nothing failed" → `True`. Remember this surprise.

Example 4 — checking a condition for every number
```python
numbers = [1, 2, 3]
print(all(n > 0 for n in numbers))
```
**Output:**
```
True
```
**What happened:** `n > 0` is tested for each number. All are positive, so `all()` is `True`.

Example 5 — one number breaks the rule
```python
numbers = [1, -2, 3]
print(all(n > 0 for n in numbers))
```
**Output:**
```
False
```
**What happened:** `-2 > 0` is `False`, so not all pass → `False`.

**Common mistakes (and the fix):**
- ❌ Expecting `all([])` to be `False`. It's `True`. An empty health-check list would wrongly "pass".
  ✅ Check it's not empty first: `if checks and all(checks): ...`
- ❌ Thinking the text `"False"` is false. Any non-empty text is truthy, so `all(["False"])` is `True`.
  ✅ Convert text to real booleans before checking.

**Real-world use case (with full solution):**

**The problem:** Before promoting a release, every region's smoke test must pass. If even one fails, block the release.

**The solution:**
```python
def can_promote(results):
    if not results:                 # guard against the empty-list surprise
        return False
    return all(results.values())    # True only if every region passed

checks = {"us-east-1": True, "eu-west-1": True, "ap-south-1": False}
print(can_promote(checks))
```
**How it works, step by step:**
1. `results.values()` gives just the pass/fail flags: `True, True, False`.
2. `all(...)` is `True` only if they're *all* `True`.
3. Here `ap-south-1` failed, so we get `False` → release blocked.

**Output:**
```
False
```

**Mini-project (with solution):**

**Your task:** A deploy config must have all four required keys filled in. Print whether it's ready.

**Solution:**
```python
required = ["region", "ami", "instance_type", "subnet"]

config = {"region": "us-east-1", "ami": "ami-1",
          "instance_type": "t3.micro", "subnet": "subnet-1"}

ready = all(config.get(key) for key in required)
print("ready to deploy:", ready)
```
**Output:**
```
ready to deploy: True
```
**Explanation:** For each required key, `config.get(key)` returns its value (or `None` if missing). `all()` is `True` only when every key has a real, non-empty value. All four are present, so it's ready.

---

## `anext()`

**What it does (plain English):** Pulls the **next item** from an async iterator (the one you get from `aiter()`). It's the async version of `next()`. Used inside `async` code with `await`. (Advanced — pair it with `aiter()` above.)

**Syntax:** `await anext(async_iterator)` or `await anext(async_iterator, default)`.

**Parameters:**
- `async_iterator` — an async iterator (from `aiter()` or an async generator).
- `default` *(optional)* — what to return if there's nothing left (instead of raising an error).

**What you get back:** The next item, or your `default` if it's empty.

**Examples (with solutions):**

Example 1 — pull items one at a time
```python
import asyncio

async def gen():
    for x in ["a", "b"]:
        yield x

async def main():
    it = gen()
    print(await anext(it))     # first
    print(await anext(it))     # second

asyncio.run(main())
```
**Output:**
```
a
b
```
**What happened:** Each `await anext(it)` gives the next value in order.

Example 2 — use a default so you don't crash when empty
```python
import asyncio

async def gen():
    yield "only"

async def main():
    it = gen()
    print(await anext(it, "END"))   # gets "only"
    print(await anext(it, "END"))   # empty now -> default

asyncio.run(main())
```
**Output:**
```
only
END
```
**What happened:** After the single item is used up, the default `"END"` is returned instead of an error.

Example 3 — first item only
```python
import asyncio

async def gen():
    for n in [10, 20, 30]:
        yield n

async def main():
    print(await anext(aiter(gen()), None))

asyncio.run(main())
```
**Output:**
```
10
```
**What happened:** `aiter()` makes the iterator, `anext()` grabs just the first number.

Example 4 — wrap it in a helper
```python
import asyncio

async def gen():
    yield "x"

async def first(ait):
    return await anext(ait, None)

async def main():
    print(await first(gen()))

asyncio.run(main())
```
**Output:**
```
x
```
**What happened:** A reusable `first()` helper returns the first item or `None`.

Example 5 — loop until exhausted using the default
```python
import asyncio

async def gen():
    for n in [1, 2]:
        yield n

async def main():
    it = gen()
    while True:
        value = await anext(it, None)
        if value is None:
            break
        print(value)

asyncio.run(main())
```
**Output:**
```
1
2
```
**What happened:** We keep pulling until `anext` returns the default `None`, then stop.

**Common mistakes (and the fix):**
- ❌ Forgetting `await` → `anext(it)` alone gives an unfinished task, not the value.
  ✅ Always `await anext(it)`.
- ❌ No default on an empty iterator → raises `StopAsyncIteration`.
  ✅ Pass a default: `await anext(it, None)`.

**Real-world use case (with full solution):**

**The problem:** You have an async stream of messages and only want to "peek" at the first one safely.

**The solution:**
```python
import asyncio

async def messages():
    for m in ["deploy started", "deploy done"]:
        await asyncio.sleep(0)
        yield m

async def peek_first(stream, default=None):
    return await anext(aiter(stream), default)

print(asyncio.run(peek_first(messages())))
```
**How it works, step by step:**
1. `aiter(stream)` turns the stream into an async iterator.
2. `anext(..., default)` returns the first message, or `default` if the stream is empty.
3. We never read the rest.

**Output:**
```
deploy started
```

**Mini-project (with solution):**

**Your task:** Try attempts one by one and stop at the first success.

**Solution:**
```python
import asyncio

async def attempts():
    for ok in [False, False, True]:
        await asyncio.sleep(0)
        yield ok

async def main():
    it = attempts()
    while True:
        result = await anext(it, None)
        if result is None:
            print("gave up")
            break
        if result:
            print("succeeded")
            break

asyncio.run(main())
```
**Output:**
```
succeeded
```
**Explanation:** We pull attempt results until one is `True`. The first two are `False`, the third is `True`, so we print "succeeded" and stop.

---

## `any()` 🔧

**What it does (plain English):** The opposite spirit of `all()`. Returns `True` if **at least one** item is truthy. Only returns `False` if *everything* is falsy (or the list is empty).

**Syntax:** `any(iterable)` — "is ANY of these true?"

**Parameters:**
- `iterable` — a list/collection to check.

**What you get back:** `True` or `False`.

**Examples (with solutions):**

Example 1 — one `True` is enough
```python
print(any([False, False, True]))
```
**Output:**
```
True
```
**What happened:** As soon as one item is `True`, `any()` is `True`.

Example 2 — everything falsy
```python
print(any([0, "", None]))
```
**Output:**
```
False
```
**What happened:** `0`, empty text `""`, and `None` all count as false, so `any()` is `False`.

Example 3 — empty list
```python
print(any([]))
```
**Output:**
```
False
```
**What happened:** Nothing is true (there's nothing at all), so `False`.

Example 4 — does any number break a rule?
```python
numbers = [1, -2, 3]
print(any(n < 0 for n in numbers))
```
**Output:**
```
True
```
**What happened:** `-2 < 0` is `True`, so at least one matches → `True`.

Example 5 — search log lines for an error
```python
lines = ["all good", "error: disk full"]
print(any("error" in line for line in lines))
```
**Output:**
```
True
```
**What happened:** The second line contains `"error"`, so `any()` returns `True`.

**Common mistakes (and the fix):**
- ❌ Thinking `any([0, "", None])` means "is anything here?" It checks *truthiness*, so it's `False` even though items exist.
  ✅ To check "is the list non-empty," use `len(my_list) > 0` or just `if my_list:`.

**Real-world use case (with full solution):**

**The problem:** Page the on-call engineer if **any** dependency (database, cache, queue) is unhealthy.

**The solution:**
```python
def should_page(statuses):
    return any(healthy is False for healthy in statuses.values())

health = {"db": True, "cache": False, "queue": True}
print("page on-call:", should_page(health))
```
**How it works, step by step:**
1. `statuses.values()` gives the health flags: `True, False, True`.
2. `healthy is False` is `True` for the cache.
3. `any(...)` sees that one `True` and returns `True` → page someone.

**Output:**
```
page on-call: True
```

**Mini-project (with solution):**

**Your task:** Scan config lines and warn if any line looks like it contains a hard-coded password.

**Solution:**
```python
lines = ["region=us-east-1", "PASSWORD=hunter2", "timeout=30"]
danger_words = ["password=", "secret=", "token="]

found = any(
    any(word in line.lower() for word in danger_words)
    for line in lines
)
print("secret found:", found)
```
**Output:**
```
secret found: True
```
**Explanation:** For each line we check if any danger word appears in it (lowercased so `PASSWORD` matches `password=`). The outer `any()` is `True` because at least one line matched.

---

## `ascii()`

**What it does (plain English):** Turns any value into text, but rewrites non-English characters (like `é` or emoji) as safe escape codes such as `\xe9`. Useful when a system can only handle plain English (ASCII) characters.

**Syntax:** `ascii(object)`

**Parameters:**
- `object` — any value.

**What you get back:** A text string containing only plain ASCII characters.

**Examples (with solutions):**

Example 1 — an accented word
```python
print(ascii("café"))
```
**Output:**
```
'caf\xe9'
```
**What happened:** The `é` became the escape code `\xe9`, keeping everything ASCII-safe.

Example 2 — plain English is untouched
```python
print(ascii("hello"))
```
**Output:**
```
'hello'
```
**What happened:** Every character is already ASCII, so nothing changes (you just get quotes around it).

Example 3 — emoji
```python
print(ascii("team 🚀"))
```
**Output:**
```
'team \U0001f680'
```
**What happened:** The rocket emoji is turned into its long escape code.

Example 4 — inside a list
```python
print(ascii(["a", "ñ"]))
```
**Output:**
```
['a', '\xf1']
```
**What happened:** It escapes characters anywhere inside the value, even in a list.

Example 5 — numbers are simple
```python
print(ascii(123))
```
**Output:**
```
123
```
**What happened:** Numbers have no special characters, so you just get `123`.

**Common mistakes (and the fix):**
- ❌ Expecting `ascii("café")` to look pretty. It deliberately escapes — that's the point.
  ✅ If you want the readable version, just use the string directly or `print("café")`.

**Real-world use case (with full solution):**

**The problem:** An older log system breaks when a tag value contains emoji or accents. You want log lines that are always safe ASCII.

**The solution:**
```python
def safe_log_line(key, value):
    return f"{key}={ascii(value)}"

print(safe_log_line("team", "rockets-🚀"))
```
**How it works, step by step:**
1. `ascii(value)` converts the emoji into a safe escape code.
2. The resulting line contains only plain characters the old system can handle.

**Output:**
```
team='rockets-\U0001f680'
```

**Mini-project (with solution):**

**Your task:** Find which tags contain non-ASCII characters (often a policy violation).

**Solution:**
```python
tags = {"env": "prod", "owner": "José", "team": "core"}

for key, value in tags.items():
    if ascii(value) != f"'{value}'":   # escaped version differs => non-ASCII
        print(f"non-ASCII tag: {key} = {value}")
```
**Output:**
```
non-ASCII tag: owner = José
```
**Explanation:** If `ascii(value)` changes the text, it means there was a non-ASCII character. `"José"` changes (the `é`), so it's flagged; `"prod"` and `"core"` don't change.

---

## `bin()`

**What it does (plain English):** Shows a whole number in binary (just 0s and 1s), with a `0b` label in front. Binary is how computers store numbers; you'll see it with bit flags and network masks.

**Syntax:** `bin(x)`

**Parameters:**
- `x` — a whole number.

**What you get back:** Text like `'0b1010'` (the `0b` means "this is binary").

**Examples (with solutions):**

Example 1 — ten in binary
```python
print(bin(10))
```
**Output:**
```
0b1010
```
**What happened:** `10` in binary is `1010`. The `0b` prefix marks it as binary.

Example 2 — the number 255
```python
print(bin(255))
```
**Output:**
```
0b11111111
```
**What happened:** `255` is eight 1s in binary (a full byte).

Example 3 — zero
```python
print(bin(0))
```
**Output:**
```
0b0
```
**What happened:** Zero is just `0` in binary.

Example 4 — drop the `0b` prefix
```python
print(bin(10)[2:])
```
**Output:**
```
1010
```
**What happened:** `[2:]` means "skip the first 2 characters" (`0b`), leaving only the digits.

Example 5 — a negative number
```python
print(bin(-5))
```
**Output:**
```
-0b101
```
**What happened:** The minus sign goes in front of the binary form.

**Common mistakes (and the fix):**
- ❌ Forgetting the `0b` is part of the text — `bin(10)` is the string `'0b1010'`, not just `1010`.
  ✅ Use `bin(10)[2:]` when you want only the digits.
- ❌ `bin(3.5)` → error, because it's a decimal.
  ✅ Convert first: `bin(int(3.5))`.

**Real-world use case (with full solution):**

**The problem:** A permission value packs several on/off settings into one number, where each binary digit is one capability. You want to read which capabilities are on.

**The solution:**
```python
capabilities = ["read", "write", "delete", "admin"]
permission = 0b0011        # read + write are on

bits = bin(permission)[2:].zfill(len(capabilities))   # '0011'
bits = bits[::-1]                                      # reverse to line up positions

for i, b in enumerate(bits):
    if b == "1":
        print("enabled:", capabilities[i])
```
**How it works, step by step:**
1. `bin(permission)[2:]` gives the digits `'11'`; `.zfill(4)` pads to `'0011'`.
2. We reverse it so position 0 lines up with `read`.
3. We print each capability whose digit is `1`.

**Output:**
```
enabled: read
enabled: write
```

**Mini-project (with solution):**

**Your task:** Show how a number looks in binary, padded to 8 digits (one byte).

**Solution:**
```python
def to_byte_string(n):
    return bin(n)[2:].zfill(8)

print(to_byte_string(5))
print(to_byte_string(200))
```
**Output:**
```
00000101
11001000
```
**Explanation:** `bin(n)[2:]` gives the bare digits and `.zfill(8)` pads the front with zeros to make a tidy 8-digit byte.

---

## `bool()`

**What it does (plain English):** Converts any value into either `True` or `False` using Python's "truthiness" rules: empty things and zero are `False`; everything else is `True`.

**Syntax:** `bool(x)`

**Parameters:**
- `x` — any value (optional; with nothing, you get `False`).

**What you get back:** `True` or `False`.

**Examples (with solutions):**

Example 1 — zero is false
```python
print(bool(0))
```
**Output:**
```
False
```
**What happened:** `0` is treated as `False`.

Example 2 — empty text is false
```python
print(bool(""))
```
**Output:**
```
False
```
**What happened:** An empty string counts as `False`.

Example 3 — an empty list is false
```python
print(bool([]))
```
**Output:**
```
False
```
**What happened:** Empty containers (list, dict, set) are `False`.

Example 4 — the surprising one
```python
print(bool("False"))
```
**Output:**
```
True
```
**What happened:** This is *text* that says "False", but it's non-empty text, so Python sees it as `True`. Watch out!

Example 5 — any non-zero number is true
```python
print(bool(0.0001))
```
**Output:**
```
True
```
**What happened:** It's not zero, so it's `True`.

**Common mistakes (and the fix):**
- ❌ Trusting `bool("False")` or `bool("0")` to be `False`. Both are `True` (non-empty text).
  ✅ Parse the text yourself (see the use case below).
- ❌ Writing `if x == True:` — unnecessary. Just write `if x:`.

**Real-world use case (with full solution):**

**The problem:** A feature flag comes from an environment variable, which is always text like `"true"`, `"0"`, or `"yes"`. You need a real `True`/`False`.

**The solution:**
```python
import os

def env_flag(name, default=False):
    value = os.environ.get(name)        # the text, or None if unset
    if value is None:
        return default
    return value.strip().lower() in ("1", "true", "yes", "on")

os.environ["ENABLE_CANARY"] = "Yes"
print(env_flag("ENABLE_CANARY"))
```
**How it works, step by step:**
1. We read the variable as text.
2. If it's missing, return the default.
3. Otherwise we lowercase it and check it against a list of "yes" words.

**Output:**
```
True
```

**Mini-project (with solution):**

**Your task:** Turn a messy settings dict (mixed text values) into clean booleans.

**Solution:**
```python
truthy_words = {"1", "true", "yes", "on", "enabled"}

settings = {"tls": "on", "debug": "0", "cache": "Yes"}

clean = {}
for key, value in settings.items():
    clean[key] = str(value).strip().lower() in truthy_words

print(clean)
```
**Output:**
```
{'tls': True, 'debug': False, 'cache': True}
```
**Explanation:** Each value is lowercased and checked against the set of "yes" words. `"on"` and `"Yes"` match (→ `True`); `"0"` doesn't (→ `False`).

---

## `breakpoint()`

**What it does (plain English):** Pauses your program at that exact line and drops you into an interactive debugger, so you can look at your variables while the program is frozen. Great for figuring out *why* something is wrong.

**Syntax:** `breakpoint()`

**Parameters:** None needed for normal use.

**What you get back:** Nothing — it hands control to the debugger so you can type commands.

**Examples (with solutions):**

Example 1 — pause to inspect a value
```python
def deploy(stage):
    breakpoint()       # program pauses HERE
    return stage

deploy("prod")
```
**Output (in the debugger you type commands):**
```
(Pdb) stage
'prod'
(Pdb) c          # 'c' = continue running
```
**What happened:** Execution paused; you typed `stage` to see its value, then `c` to continue.

Example 2 — the handy debugger commands
```python
# Once paused, these are the ones you'll use most:
#   n   -> run the next line
#   p x -> print the value of x
#   c   -> continue (un-pause)
#   q   -> quit the program
```
**Output:** *(reference only)*
**What happened:** These four commands cover 90% of debugging.

Example 3 — turn ALL breakpoints off without editing code
```bash
# Run your script like this in the terminal:
PYTHONBREAKPOINT=0 python script.py
```
**Output:** *(the program runs straight through, ignoring breakpoints)*
**What happened:** The `PYTHONBREAKPOINT=0` setting disables every `breakpoint()` at once.

Example 4 — pause only when something is wrong
```python
def handle(value):
    if value < 0:
        breakpoint()       # only pauses for bad input
    return value

handle(-1)
```
**Output:** *(pauses only when value is negative)*
**What happened:** Wrapping it in an `if` makes it a conditional pause.

Example 5 — inspect a dict mid-run
```python
data = {"region": "us-east-1"}
breakpoint()
# at the prompt: p data["region"]   ->  'us-east-1'
```
**Output:**
```
(Pdb) p data["region"]
'us-east-1'
```
**What happened:** You can run small expressions at the prompt to inspect anything.

**Common mistakes (and the fix):**
- ❌ Leaving `breakpoint()` in code you commit → it freezes automated pipelines (CI) waiting for input that never comes.
  ✅ Remove it before committing, or use a linter to catch leftovers.

**Real-world use case (with full solution):**

**The problem:** A script that launches servers keeps sending wrong settings to AWS. You want to inspect the exact settings right before the API call.

**The solution:**
```python
def launch(params):
    breakpoint()                 # inspect params before anything happens
    # ec2.run_instances(**params)   # the real call (commented out for safety)
    print("would launch with:", params)

launch({"ImageId": "ami-123", "InstanceType": "t3.micro"})
```
**How it works, step by step:**
1. The program pauses *before* the cloud call.
2. At the prompt you type `p params` to confirm the AMI and instance type are correct.
3. Type `c` to continue once you're satisfied.

**Output (debugger session):**
```
(Pdb) p params
{'ImageId': 'ami-123', 'InstanceType': 't3.micro'}
(Pdb) c
would launch with: {'ImageId': 'ami-123', 'InstanceType': 't3.micro'}
```

**Mini-project (with solution):**

**Your task:** Make a debug helper that only pauses when an environment variable `DEBUG=1` is set, so it's safe to leave in dev code.

**Solution:**
```python
import os

def dbg():
    if os.environ.get("DEBUG") == "1":
        breakpoint()

def process(x):
    dbg()            # pauses ONLY if DEBUG=1
    return x * 2

print(process(5))
```
**Output (with DEBUG unset):**
```
10
```
**Explanation:** Because `DEBUG` isn't `"1"`, `dbg()` does nothing and the program runs normally. Set `DEBUG=1` in your terminal and it would pause instead.

---

## `bytearray()`

**What it does (plain English):** Makes a **changeable** sequence of raw bytes (numbers 0–255). "Bytes" are how files and network data are really stored. "Changeable" means you can edit individual bytes after creating it.

**Syntax:** `bytearray(source)`

**Parameters:**
- A length number, a list of small numbers (0–255), or a string plus an encoding like `"utf-8"`.

**What you get back:** A `bytearray` you can modify in place.

**Examples (with solutions):**

Example 1 — start with empty bytes
```python
ba = bytearray(3)
print(ba)
```
**Output:**
```
bytearray(b'\x00\x00\x00')
```
**What happened:** `bytearray(3)` made room for 3 bytes, all set to zero (`\x00`).

Example 2 — from a list of numbers
```python
ba = bytearray([72, 105])
print(ba)
```
**Output:**
```
bytearray(b'Hi')
```
**What happened:** `72` is the code for `H` and `105` is `i`, so the bytes spell "Hi".

Example 3 — from text
```python
ba = bytearray("Hi", "utf-8")
print(ba)
```
**Output:**
```
bytearray(b'Hi')
```
**What happened:** The text "Hi" was encoded into bytes using UTF-8.

Example 4 — change a byte in place (the whole point)
```python
ba = bytearray("Hi", "utf-8")
ba[0] = 74          # 74 is the code for 'J'
print(ba)
```
**Output:**
```
bytearray(b'Ji')
```
**What happened:** We replaced the first byte, turning "Hi" into "Ji". This editing is what makes `bytearray` special.

Example 5 — add more bytes
```python
ba = bytearray(b"log")
ba.extend(b"-1")
print(ba)
```
**Output:**
```
bytearray(b'log-1')
```
**What happened:** `.extend()` appended more bytes to the end.

**Common mistakes (and the fix):**
- ❌ Setting a byte outside 0–255, like `ba[0] = 300` → error.
  ✅ Keep byte values between 0 and 255.
- ❌ Expecting `ba[0]` to be a character. It's actually the *number* (e.g. `72`), not `"H"`.
  ✅ To see text, decode it: `ba.decode("utf-8")`.

**Real-world use case (with full solution):**

**The problem:** You're assembling an upload payload piece by piece (e.g. several records joined by newlines) before sending it to object storage.

**The solution:**
```python
def build_payload(records):
    buffer = bytearray()                 # empty, editable
    for record in records:
        buffer.extend(record.encode("utf-8"))   # add the record's bytes
        buffer.append(10)                        # 10 is the newline byte '\n'
    return bytes(buffer)                  # freeze it before upload

payload = build_payload(["line-a", "line-b"])
print(payload)
```
**How it works, step by step:**
1. Start with an empty `bytearray`.
2. For each record, add its bytes, then add a newline byte.
3. Convert to immutable `bytes` at the end (uploads expect finished, unchangeable data).

**Output:**
```
b'line-a\nline-b\n'
```

**Mini-project (with solution):**

**Your task:** Build a simple reversible scrambler that flips every byte using XOR. (This is a demo, **not** real encryption.)

**Solution:**
```python
def scramble(data, key):
    ba = bytearray(data)            # editable copy
    for i in range(len(ba)):
        ba[i] = ba[i] ^ key         # XOR each byte with the key
    return bytes(ba)

secret = scramble(b"hello", 42)
print("scrambled:", secret)
print("unscrambled:", scramble(secret, 42))   # XOR again to reverse
```
**Output:**
```
scrambled: b'BO\x06\x06\x05'
unscrambled: b'hello'
```
**Explanation:** XOR-ing a byte with the same key twice returns the original, so scrambling and unscrambling use the exact same function. We edit each byte in place, which is why `bytearray` is perfect here.

---

## `bytes()`

**What it does (plain English):** Makes an **unchangeable** sequence of raw bytes. Same idea as `bytearray`, but once created you can't edit it. This is the normal type for file contents, network data, and anything you hash.

**Syntax:** `bytes(source)`

**Parameters:**
- A length number, a list of small numbers (0–255), or a string plus an encoding.

**What you get back:** A `bytes` object (read-only).

**Examples (with solutions):**

Example 1 — from text using `.encode()` (most common)
```python
data = "hello".encode("utf-8")
print(data)
```
**Output:**
```
b'hello'
```
**What happened:** `.encode()` turned the text into bytes. The `b` prefix means "these are bytes."

Example 2 — using `bytes()` directly
```python
print(bytes("hi", "utf-8"))
```
**Output:**
```
b'hi'
```
**What happened:** Same as `.encode()`, just written differently.

Example 3 — from numbers
```python
print(bytes([104, 105]))
```
**Output:**
```
b'hi'
```
**What happened:** `104` and `105` are the codes for `h` and `i`.

Example 4 — turn bytes back into text
```python
data = b"hello"
print(data.decode("utf-8"))
```
**Output:**
```
hello
```
**What happened:** `.decode()` is the reverse of `.encode()` — bytes back to readable text.

Example 5 — bytes are read-only
```python
data = bytes("hi", "utf-8")
print(data)
# data[0] = 74   # this would ERROR — bytes can't be changed
```
**Output:**
```
b'hi'
```
**What happened:** Unlike `bytearray`, you can't edit `bytes`. If you need editing, use `bytearray`.

**Common mistakes (and the fix):**
- ❌ Mixing text and bytes, like `"abc" + b"def"` → error.
  ✅ Make them the same type first: `"abc".encode() + b"def"`.
- ❌ `bytes("café")` with no encoding → error on the accented character.
  ✅ Always give an encoding: `bytes("café", "utf-8")`.

**Real-world use case (with full solution):**

**The problem:** You want to verify a file/object hasn't changed by computing its checksum (a fingerprint). Hashing functions need **bytes**, not text.

**The solution:**
```python
import hashlib

def fingerprint(text):
    data = text.encode("utf-8")          # text -> bytes
    return hashlib.md5(data).hexdigest() # the checksum

print(fingerprint("config-v2"))
```
**How it works, step by step:**
1. `.encode("utf-8")` converts your text into bytes.
2. `hashlib.md5(...)` computes a fingerprint of those bytes.
3. `.hexdigest()` shows it as a readable hex string. Same input → same fingerprint, so you can detect changes.

**Output:**
```
2c5e8c... (a 32-character hex string)
```

**Mini-project (with solution):**

**Your task:** Build a storage key from a file's content, so identical content always maps to the same key.

**Solution:**
```python
import hashlib

def content_key(text):
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return f"blobs/{digest[:2]}/{digest}"

print(content_key("hello world"))
```
**Output:**
```
blobs/b9/b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9
```
**Explanation:** We encode the text to bytes, hash it with SHA-256, and build a folder-style key from the fingerprint. The same content will always produce the same key, which is how content-addressable storage works.

---

# C–D

## `callable()`

**What it does (plain English):** Tells you whether something can be "called" — meaning you can put `()` after it to run it. Functions and classes are callable; plain numbers and strings are not.

**Syntax:** `callable(object)`

**Parameters:**
- `object` — anything you want to test.

**What you get back:** `True` (you can call it) or `False`.

**Examples (with solutions):**

Example 1 — a built-in function is callable
```python
print(callable(len))
```
**Output:**
```
True
```
**What happened:** `len` is a function, so you can run it as `len(...)` → `True`.

Example 2 — a number is not callable
```python
print(callable(42))
```
**Output:**
```
False
```
**What happened:** You can't do `42()`, so it's `False`.

Example 3 — a class is callable (you call it to make an object)
```python
print(callable(str))
```
**Output:**
```
True
```
**What happened:** `str("hi")` creates a string, so the class itself is callable.

Example 4 — a small inline function (lambda)
```python
double = lambda x: x * 2
print(callable(double))
```
**Output:**
```
True
```
**What happened:** A `lambda` is just a tiny function, so it's callable.

Example 5 — a plain string is not
```python
print(callable("hello"))
```
**Output:**
```
False
```
**What happened:** `"hello"()` makes no sense, so `False`.

**Common mistakes (and the fix):**
- ❌ Thinking `callable()` checks the arguments are right. It only checks "can this be called at all," not "with these inputs."
  ✅ Use it just to guard against calling something that isn't a function.

**Real-world use case (with full solution):**

**The problem:** You have a lookup table of event handlers. Before running one, you want to be sure the value you found is actually a function (not missing or a typo).

**The solution:**
```python
def dispatch(event, handlers):
    handler = handlers.get(event["type"])     # look up the right function
    if callable(handler):                     # is it actually runnable?
        return handler(event)
    return f"no handler for {event['type']}"

handlers = {
    "s3:ObjectCreated": lambda e: f"processing {e['key']}"
}

print(dispatch({"type": "s3:ObjectCreated", "key": "file.txt"}, handlers))
print(dispatch({"type": "unknown"}, handlers))
```
**How it works, step by step:**
1. We look up a handler by the event's type.
2. `callable(handler)` checks we actually found a function.
3. If yes, we run it; if not, we return a safe message instead of crashing.

**Output:**
```
processing file.txt
no handler for unknown
```

**Mini-project (with solution):**

**Your task:** Run a list of pipeline steps. Each step might be a function to apply, or just a plain value to pass along.

**Solution:**
```python
def run_pipeline(value, steps):
    for step in steps:
        if callable(step):
            value = step(value)     # it's a function: apply it
        else:
            value = step            # it's a plain value: use it directly
    return value

result = run_pipeline(3, [lambda x: x + 1, lambda x: x * 2])
print(result)
```
**Output:**
```
8
```
**Explanation:** Start with `3`. First step adds 1 → `4`. Second step doubles → `8`. `callable()` lets the same loop handle both functions and plain values safely.

---

## `chr()`

**What it does (plain English):** Turns a number into its matching character. Every character has a number code (called a Unicode code point); `chr()` goes from the number to the character. (Its opposite is `ord()`.)

**Syntax:** `chr(number)`

**Parameters:**
- `number` — a whole number (the character's code).

**What you get back:** A single character (as text).

**Examples (with solutions):**

Example 1 — code 65 is capital A
```python
print(chr(65))
```
**Output:**
```
A
```
**What happened:** The code `65` maps to the letter `A`.

Example 2 — code 97 is lowercase a
```python
print(chr(97))
```
**Output:**
```
a
```
**What happened:** Lowercase letters start at `97`.

Example 3 — a newline character
```python
print("line1" + chr(10) + "line2")
```
**Output:**
```
line1
line2
```
**What happened:** Code `10` is the newline character (`\n`), so it splits the text onto two lines.

Example 4 — build a word from codes
```python
codes = [72, 105]
word = chr(codes[0]) + chr(codes[1])
print(word)
```
**Output:**
```
Hi
```
**What happened:** `72`→`H`, `105`→`i`, joined into "Hi".

Example 5 — an emoji has a (big) code
```python
print(chr(128640))
```
**Output:**
```
🚀
```
**What happened:** Even emoji have number codes; `128640` is the rocket.

**Common mistakes (and the fix):**
- ❌ Passing a number that's too big (above ~1.1 million) → error.
  ✅ Stick to valid code points (0 to 1,114,111).

**Real-world use case (with full solution):**

**The problem:** You want to join data fields with a separator that will never appear inside the data itself. A normal comma might appear in values, so you use a rare "unit separator" character (code 31).

**The solution:**
```python
separator = chr(31)        # the "unit separator" control character

def make_record(fields):
    return separator.join(fields)

record = make_record(["i-0a1", "running", "us-east-1"])
print(repr(record))        # repr shows the hidden separator
```
**How it works, step by step:**
1. `chr(31)` gives a character that won't show up in normal data.
2. `.join(fields)` glues the fields together with that separator.
3. `repr(...)` lets us *see* the otherwise-invisible separator (`\x1f`).

**Output:**
```
'i-0a1\x1frunning\x1fus-east-1'
```

**Mini-project (with solution):**

**Your task:** Generate spreadsheet-style column names: A, B, C … Z, then AA, AB, and so on, for naming resources.

**Solution:**
```python
def column_name(n):
    name = ""
    n = n + 1                       # make it 1-based
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        name = chr(65 + remainder) + name   # 65 is 'A'
    return name

print([column_name(i) for i in range(5)])   # first five
print(column_name(26))                       # the 27th
```
**Output:**
```
['A', 'B', 'C', 'D', 'E']
AA
```
**Explanation:** `chr(65 + remainder)` turns a number 0–25 into a letter A–Z. The loop handles "carrying over" to two letters once you pass Z, just like spreadsheet columns.

---

## `classmethod()`

**What it does (plain English):** A label (`@classmethod`) you put above a function inside a class to say "this method works with the *class itself*, not a specific object." It's most useful for making alternate ways to build an object (factory methods). (This is an object-oriented topic — fine to skim if classes are new to you.)

**Syntax:**
```python
class Thing:
    @classmethod
    def make(cls, ...):
        ...
```

**Parameters:**
- The method automatically receives `cls` (the class) as its first argument — you don't pass it yourself.

**What you get back:** A method you call on the class, like `Thing.make(...)`.

**Examples (with solutions):**

Example 1 — a factory that reads from the environment
```python
import os

class Config:
    def __init__(self, region):
        self.region = region

    @classmethod
    def from_env(cls):
        region = os.environ.get("AWS_REGION", "us-east-1")
        return cls(region)          # cls() builds a Config

os.environ["AWS_REGION"] = "eu-west-1"
print(Config.from_env().region)
```
**Output:**
```
eu-west-1
```
**What happened:** `from_env` read the env var and built a `Config` for us, no manual values needed.

Example 2 — a "default" preset
```python
class Config:
    def __init__(self, region):
        self.region = region

    @classmethod
    def default(cls):
        return cls("us-east-1")

print(Config.default().region)
```
**Output:**
```
us-east-1
```
**What happened:** `default()` is a tidy shortcut for the most common setup.

Example 3 — you call it on the class, not an object
```python
class Greeter:
    @classmethod
    def hello(cls):
        return "hi from " + cls.__name__

print(Greeter.hello())
```
**Output:**
```
hi from Greeter
```
**What happened:** `cls.__name__` is the class's name. We never created an object.

Example 4 — it knows the real subclass
```python
class Base:
    @classmethod
    def create(cls):
        return cls()

class Special(Base):
    pass

print(type(Special.create()).__name__)
```
**Output:**
```
Special
```
**What happened:** Because `cls` is the actual class used, `Special.create()` builds a `Special`, not a `Base`. This is the big advantage over a static method.

Example 5 — multiple presets side by side
```python
class Instance:
    def __init__(self, size):
        self.size = size

    @classmethod
    def small(cls):
        return cls("t3.micro")

    @classmethod
    def large(cls):
        return cls("m5.2xlarge")

print(Instance.small().size, Instance.large().size)
```
**Output:**
```
t3.micro m5.2xlarge
```
**What happened:** Two named shortcuts for building common configurations.

**Common mistakes (and the fix):**
- ❌ Naming the first parameter `self` instead of `cls`. By convention a classmethod's first parameter is `cls` (the class).
  ✅ Write `def make(cls, ...)`.
- ❌ Forgetting the `@classmethod` label — then Python treats it as a normal method that needs an object.

**Real-world use case (with full solution):**

**The problem:** You want several clean ways to build a cloud client config — from a profile name, from defaults, etc. — that all end up calling the same constructor.

**The solution:**
```python
class AwsConfig:
    def __init__(self, region, profile):
        self.region = region
        self.profile = profile

    @classmethod
    def for_profile(cls, profile):
        return cls(region="us-east-1", profile=profile)

config = AwsConfig.for_profile("prod")
print(config.region, "/", config.profile)
```
**How it works, step by step:**
1. `for_profile` is an alternate constructor.
2. It fills in a sensible default region and uses the profile you gave.
3. `cls(...)` builds the object, so it still works for subclasses.

**Output:**
```
us-east-1 / prod
```

**Mini-project (with solution):**

**Your task:** A class for EC2 launch settings with two presets, `small()` and `large()`.

**Solution:**
```python
class Launch:
    def __init__(self, instance_type, ami):
        self.instance_type = instance_type
        self.ami = ami

    @classmethod
    def small(cls):
        return cls("t3.micro", "ami-base")

    @classmethod
    def large(cls):
        return cls("m5.2xlarge", "ami-base")

print("small:", Launch.small().instance_type)
print("large:", Launch.large().instance_type)
```
**Output:**
```
small: t3.micro
large: m5.2xlarge
```
**Explanation:** Each preset returns a ready-made `Launch` object. The caller doesn't need to remember which instance type goes with which size.

---

## `compile()`

**What it does (plain English):** Takes Python code written as text and prepares ("compiles") it so it can be run later by `eval()` or `exec()`. You rarely need this directly. ⚠️ Like `eval`/`exec`, never compile code that came from an untrusted user.

**Syntax:** `compile(source, filename, mode)`

**Parameters:**
- `source` — the code, as text.
- `filename` — a label used in error messages (use `"<string>"` if you have no file).
- `mode` — `"eval"` for a single expression, or `"exec"` for full statements.

**What you get back:** A ready-to-run "code object".

**Examples (with solutions):**

Example 1 — compile then evaluate an expression
```python
code = compile("x + 1", "<expr>", "eval")
print(eval(code, {"x": 41}))
```
**Output:**
```
42
```
**What happened:** We compiled `"x + 1"` once, then ran it with `x = 41`.

Example 2 — compile a small program (statements)
```python
program = compile("for i in range(3): print(i)", "<prog>", "exec")
exec(program)
```
**Output:**
```
0
1
2
```
**What happened:** Mode `"exec"` is for multi-step code like loops.

Example 3 — reuse a compiled expression with different values
```python
code = compile("price * qty", "<e>", "eval")
print(eval(code, {"price": 10, "qty": 3}))
print(eval(code, {"price": 5, "qty": 4}))
```
**Output:**
```
30
20
```
**What happened:** Compile once, run many times with different inputs — faster than re-parsing each time.

Example 4 — wrong mode causes an error
```python
# compile("x = 5", "<e>", "eval")   # ERROR: "eval" is only for expressions
code = compile("x = 5", "<e>", "exec")  # "exec" is correct for assignment
exec(code)
print(x)
```
**Output:**
```
5
```
**What happened:** Assignments are statements, so they need `"exec"`, not `"eval"`.

Example 5 — measure length of text
```python
code = compile("len(name)", "<e>", "eval")
print(eval(code, {"name": "server-1", "len": len}))
```
**Output:**
```
8
```
**What happened:** We had to provide `len` in the variables dict because we locked down the environment.

**Common mistakes (and the fix):**
- ❌ Using `"eval"` mode for statements like `x = 1` → `SyntaxError`.
  ✅ Use `"exec"` for statements, `"eval"` for single expressions.
- ❌ ⚠️ Compiling text from a user/web request → just as dangerous as `eval`.
  ✅ Never compile untrusted input.

**Real-world use case (with full solution):**

**The problem:** Operators write simple alert rules like `"cpu > 80 and mem > 70"`. You evaluate each rule against many metric samples, so you compile each rule once for speed — while locking down what the code can access.

**The solution:**
```python
def make_rule(expression):
    code = compile(expression, "<rule>", "eval")     # compile once
    def check(metrics):
        # {"__builtins__": {}} removes access to dangerous functions
        return bool(eval(code, {"__builtins__": {}}, metrics))
    return check

high_load = make_rule("cpu > 80 and mem > 70")
print(high_load({"cpu": 92, "mem": 85}))
print(high_load({"cpu": 50, "mem": 60}))
```
**How it works, step by step:**
1. `compile(...)` turns the rule text into a reusable code object.
2. `eval(code, {"__builtins__": {}}, metrics)` runs it with the metric values, but with built-in functions removed for safety.
3. We get `True`/`False` for each set of metrics.

**Output:**
```
True
False
```
> Even with built-ins removed, only do this with rules *you* control, never random user input.

**Mini-project (with solution):**

**Your task:** Build a tiny formula evaluator that remembers (caches) compiled formulas so it doesn't recompile the same one twice.

**Solution:**
```python
class FormulaCache:
    def __init__(self):
        self.cache = {}

    def evaluate(self, expression, **variables):
        if expression not in self.cache:
            self.cache[expression] = compile(expression, "<f>", "eval")
        code = self.cache[expression]
        return eval(code, {"__builtins__": {}}, variables)

fc = FormulaCache()
print(fc.evaluate("a + b * 2", a=1, b=3))
print(fc.evaluate("a + b * 2", a=10, b=1))   # reuses the cached compile
```
**Output:**
```
7
12
```
**Explanation:** The first call compiles and stores the formula; the second call finds it already compiled and just runs it with new numbers.

---

## `complex()`

**What it does (plain English):** Creates a "complex number," which has a normal part and an "imaginary" part written with `j`. You'll almost never need these in everyday DevOps — they show up in advanced math/signal analysis. Included for completeness.

**Syntax:** `complex(real, imaginary)` or `complex("1+2j")`

**Parameters:**
- `real` — the normal part.
- `imaginary` — the coefficient of the `j` part.

**What you get back:** A `complex` number.

**Examples (with solutions):**

Example 1 — build one from two numbers
```python
print(complex(3, 4))
```
**Output:**
```
(3+4j)
```
**What happened:** `3` is the real part, `4` is the imaginary part (`4j`).

Example 2 — from text
```python
print(complex("2+5j"))
```
**Output:**
```
(2+5j)
```
**What happened:** Python parsed the text into a complex number (note: no spaces allowed).

Example 3 — just a real number
```python
print(complex(7))
```
**Output:**
```
(7+0j)
```
**What happened:** With no imaginary part given, it's `0j`.

Example 4 — the "size" of a complex number
```python
print(abs(complex(3, 4)))
```
**Output:**
```
5.0
```
**What happened:** `abs()` on a complex number gives its distance from zero, here `5.0` (a classic 3-4-5 triangle).

Example 5 — multiply two complex numbers
```python
print(complex(1, 1) * complex(1, -1))
```
**Output:**
```
(2+0j)
```
**What happened:** Complex multiplication follows math rules; the imaginary parts cancel out here.

**Common mistakes (and the fix):**
- ❌ Writing the text with spaces, like `complex("2 + 5j")` → error.
  ✅ Remove the spaces: `complex("2+5j")`.
- ❌ Using `i` instead of `j`. Python uses `j` for the imaginary unit.

**Real-world use case (with full solution):**

**The problem:** You're doing advanced analysis on latency data (a Fourier transform) to spot repeating spikes. The math library returns complex numbers, and you need their magnitudes.

**The solution:**
```python
# In real life numpy returns complex numbers from np.fft.fft(...).
# Here's the core idea with one value:
frequency_value = complex(0.6, 0.8)
magnitude = abs(frequency_value)      # how strong this frequency is
print(round(magnitude, 2))
```
**How it works, step by step:**
1. Each frequency comes back as a complex number.
2. `abs()` gives its magnitude (strength).
3. Big magnitudes point to repeating patterns in your data.

**Output:**
```
1.0
```

**Mini-project (with solution):**

**Your task:** Use a complex number to represent an (x, y) point and compute its distance from the origin.

**Solution:**
```python
def distance_from_origin(x, y):
    point = complex(x, y)
    return abs(point)

print(distance_from_origin(3, 4))
```
**Output:**
```
5.0
```
**Explanation:** A complex number `x + yj` is a neat way to store a 2D point. `abs()` then gives the straight-line distance from `(0, 0)`.

---

## `delattr()`

**What it does (plain English):** Removes an attribute (a stored value) from an object, when you only know the attribute's name as text. It's the dynamic version of writing `del obj.name`.

**Syntax:** `delattr(object, "name")`

**Parameters:**
- `object` — the object to modify.
- `name` — the attribute name, as text.

**What you get back:** Nothing — it just removes the attribute.

**Examples (with solutions):**

Example 1 — remove an attribute
```python
class Box:
    pass

b = Box()
b.debug = True
delattr(b, "debug")
print(hasattr(b, "debug"))     # is it still there?
```
**Output:**
```
False
```
**What happened:** `delattr` removed `debug`, so `hasattr` now reports `False`.

Example 2 — remove several by name
```python
class Box:
    pass

b = Box()
b.a = 1
b.b = 2
for name in ["a", "b"]:
    delattr(b, name)
print(vars(b))                 # what's left?
```
**Output:**
```
{}
```
**What happened:** We looped over names and deleted each, leaving the object empty.

Example 3 — check before deleting (safe)
```python
class Box:
    pass

b = Box()
if hasattr(b, "x"):
    delattr(b, "x")
print("done")                  # no error even though x didn't exist
```
**Output:**
```
done
```
**What happened:** We checked with `hasattr` first, avoiding an error.

Example 4 — deleting a missing attribute errors
```python
class Box:
    pass

b = Box()
# delattr(b, "missing")   # this would raise AttributeError
print("skip the risky line")
```
**Output:**
```
skip the risky line
```
**What happened:** Deleting something that isn't there raises an error — always guard with `hasattr`.

Example 5 — equivalent to `del`
```python
class Box:
    pass

b = Box()
b.temp = 5
del b.temp                     # same effect as delattr(b, "temp")
print(hasattr(b, "temp"))
```
**Output:**
```
False
```
**What happened:** `delattr(b, "temp")` and `del b.temp` do the same thing; use `delattr` when the name is in a variable.

**Common mistakes (and the fix):**
- ❌ Deleting an attribute that doesn't exist → `AttributeError`.
  ✅ Guard first: `if hasattr(obj, name): delattr(obj, name)`.

**Real-world use case (with full solution):**

**The problem:** Before logging or saving a config object, you want to strip out sensitive fields like passwords and tokens.

**The solution:**
```python
sensitive = ["password", "secret_key", "token"]

class Connection:
    pass

conn = Connection()
conn.host = "db.internal"
conn.password = "p@ss"

for field in sensitive:
    if hasattr(conn, field):
        delattr(conn, field)

print(vars(conn))      # vars() shows the object's remaining attributes
```
**How it works, step by step:**
1. We list the sensitive field names.
2. For each one, if the object has it, we delete it.
3. What's left is safe to log or save.

**Output:**
```
{'host': 'db.internal'}
```

**Mini-project (with solution):**

**Your task:** Remove any attribute whose value is `None` from a settings object (clean up "empty" fields).

**Solution:**
```python
class Settings:
    pass

s = Settings()
s.region = "us-east-1"
s.zone = None
s.replicas = 3

for name in list(vars(s)):        # list() so we can delete while looping
    if getattr(s, name) is None:
        delattr(s, name)

print(vars(s))
```
**Output:**
```
{'region': 'us-east-1', 'replicas': 3}
```
**Explanation:** `vars(s)` gives the attribute names. We check each value with `getattr`; if it's `None`, we remove it with `delattr`. We wrap the names in `list()` so we can safely delete while looping.

---

## `dict()` 🔧

**What it does (plain English):** Creates a dictionary — a collection of **key → value** pairs, like a real-world lookup table. Dictionaries are everywhere in cloud work: tags, config, JSON data, API responses.

**Syntax:** `dict(...)` (several ways shown below) or the shortcut `{}`.

**Parameters:**
- Keyword pairs, another dictionary, or a list of `(key, value)` pairs.

**What you get back:** A `dict`.

**Examples (with solutions):**

Example 1 — create with keyword pairs
```python
tags = dict(env="prod", team="sre")
print(tags)
```
**Output:**
```
{'env': 'prod', 'team': 'sre'}
```
**What happened:** Each `name=value` became a key→value pair.

Example 2 — look up a value by its key
```python
tags = {"env": "prod", "team": "sre"}
print(tags["env"])
```
**Output:**
```
prod
```
**What happened:** Square brackets `["env"]` fetch the value stored under that key.

Example 3 — safe lookup with a default
```python
tags = {"env": "prod"}
print(tags.get("owner", "unknown"))
```
**Output:**
```
unknown
```
**What happened:** `.get()` returns a fallback (`"unknown"`) instead of crashing when the key is missing.

Example 4 — build from two lists
```python
keys = ["x", "y"]
values = [10, 20]
print(dict(zip(keys, values)))
```
**Output:**
```
{'x': 10, 'y': 20}
```
**What happened:** `zip` pairs them up, and `dict` turns the pairs into a dictionary.

Example 5 — merge two dictionaries
```python
defaults = {"region": "us-east-1"}
overrides = {"region": "eu-west-1", "team": "sre"}
merged = {**defaults, **overrides}
print(merged)
```
**Output:**
```
{'region': 'eu-west-1', 'team': 'sre'}
```
**What happened:** The `{**a, **b}` trick combines both; when keys clash, the later one (`overrides`) wins.

**Common mistakes (and the fix):**
- ❌ Using `tags["owner"]` when the key might be missing → `KeyError` crash.
  ✅ Use `tags.get("owner", default)` for safe lookups.
- ❌ Confusing `{}` (empty dict) with an empty set. `{}` is always an empty dictionary.

**Real-world use case (with full solution):**

**The problem:** AWS returns tags as a list of `{"Key": ..., "Value": ...}` items, which is awkward. You want a simple `{key: value}` dictionary instead.

**The solution:**
```python
def tags_to_dict(tag_list):
    result = {}
    for tag in tag_list:
        result[tag["Key"]] = tag["Value"]
    return result

aws_tags = [
    {"Key": "env", "Value": "prod"},
    {"Key": "team", "Value": "sre"},
]
print(tags_to_dict(aws_tags))
```
**How it works, step by step:**
1. Start with an empty dictionary.
2. For each AWS tag, take its `Key` and `Value` and store them as a pair.
3. Return the clean dictionary.

**Output:**
```
{'env': 'prod', 'team': 'sre'}
```

**Mini-project (with solution):**

**Your task:** Merge default tags, stack tags, and resource tags so that later sources override earlier ones.

**Solution:**
```python
def merge_tags(*sources):
    result = {}
    for source in sources:
        result.update(source)      # update() merges, overwriting clashes
    return result

final = merge_tags(
    {"env": "prod"},
    {"team": "sre"},
    {"env": "staging"},            # this overrides env
)
print(final)
```
**Output:**
```
{'env': 'staging', 'team': 'sre'}
```
**Explanation:** `.update()` copies pairs from each source into the result. Because we apply them in order, the last `env` value (`"staging"`) wins.

---

## `dir()`

**What it does (plain English):** Lists the names of everything you can do with an object — its methods and attributes. It's like asking "what can this thing do?" Great for exploring an unfamiliar library.

**Syntax:** `dir(object)`

**Parameters:**
- `object` — anything (optional; with nothing, it lists names in your current code).

**What you get back:** An alphabetically sorted list of names (as text).

**Examples (with solutions):**

Example 1 — what can a list do?
```python
names = dir([])
print(names[-3:])      # show the last 3 for brevity
```
**Output:**
```
['pop', 'remove', 'reverse']
```
**What happened:** `dir([])` lists all list methods; we printed the last few.

Example 2 — hide the "dunder" names
```python
useful = [name for name in dir(str) if not name.startswith("_")]
print(useful[:5])
```
**Output:**
```
['capitalize', 'casefold', 'center', 'count', 'encode']
```
**What happened:** Names with underscores (like `__len__`) are internal. Filtering them out shows the methods you'd actually call.

Example 3 — check if a method exists
```python
print("upper" in dir(str))
```
**Output:**
```
True
```
**What happened:** `str` has an `upper` method, so it's in the list.

Example 4 — explore a module
```python
import os
print("getcwd" in dir(os))
```
**Output:**
```
True
```
**What happened:** `dir(os)` lists everything in the `os` module; `getcwd` is one of them.

Example 5 — find methods starting with a word
```python
describe_methods = [m for m in dir(dict) if m.startswith("set")]
print(describe_methods)
```
**Output:**
```
['setdefault']
```
**What happened:** We filtered the dict's methods to those starting with "set".

**Common mistakes (and the fix):**
- ❌ Expecting a clean list — most names are internal dunders.
  ✅ Filter them: `[n for n in dir(x) if not n.startswith("_")]`.

**Real-world use case (with full solution):**

**The problem:** You're exploring a cloud SDK client in an interactive session and want to see which "describe" operations it offers, without reading the docs.

**The solution:**
```python
class FakeEC2:                 # stand-in for a real boto3 client
    def describe_instances(self): pass
    def describe_volumes(self): pass
    def run_instances(self): pass

ec2 = FakeEC2()
describe_ops = [name for name in dir(ec2) if name.startswith("describe_")]
print(describe_ops)
```
**How it works, step by step:**
1. `dir(ec2)` lists every method on the client.
2. We keep only the ones starting with `describe_`.
3. Now we can see the read operations at a glance.

**Output:**
```
['describe_instances', 'describe_volumes']
```

**Mini-project (with solution):**

**Your task:** Print a clean list of an object's public methods (the ones you'd actually call).

**Solution:**
```python
def public_methods(obj):
    result = []
    for name in dir(obj):
        if not name.startswith("_") and callable(getattr(obj, name)):
            result.append(name)
    return result

print(public_methods(str)[:5])
```
**Output:**
```
['capitalize', 'casefold', 'center', 'count', 'encode']
```
**Explanation:** We skip underscore names (internal) and use `callable(getattr(obj, name))` to keep only methods (things you can actually call), not plain data attributes.

---

## `divmod()`

**What it does (plain English):** Does division and gives you **both** results at once: how many times one number fits into another (the quotient) and what's left over (the remainder).

**Syntax:** `divmod(a, b)`

**Parameters:**
- `a` — the number being divided.
- `b` — the number you're dividing by.

**What you get back:** A pair `(quotient, remainder)`.

**Examples (with solutions):**

Example 1 — basic
```python
print(divmod(17, 5))
```
**Output:**
```
(3, 2)
```
**What happened:** `5` fits into `17` three times (`3`), with `2` left over.

Example 2 — unpack the two results
```python
quotient, remainder = divmod(17, 5)
print("quotient:", quotient)
print("remainder:", remainder)
```
**Output:**
```
quotient: 3
remainder: 2
```
**What happened:** We split the pair into two named variables for clarity.

Example 3 — no remainder
```python
print(divmod(10, 2))
```
**Output:**
```
(5, 0)
```
**What happened:** `2` divides `10` evenly, so the remainder is `0`.

Example 4 — works with decimals
```python
print(divmod(7.5, 2))
```
**Output:**
```
(3.0, 1.5)
```
**What happened:** `2` fits into `7.5` three times with `1.5` left over.

Example 5 — convert minutes to hours and minutes
```python
hours, minutes = divmod(125, 60)
print(f"{hours}h {minutes}m")
```
**Output:**
```
2h 5m
```
**What happened:** `60` fits into `125` twice (`2` hours) with `5` minutes left.

**Common mistakes (and the fix):**
- ❌ Dividing by zero: `divmod(5, 0)` → error.
  ✅ Make sure the second number isn't zero.

**Real-world use case (with full solution):**

**The problem:** You have a size in raw bytes and want to show it to humans as KiB/MiB/GiB instead of a giant number.

**The solution:**
```python
def human_size(num_bytes):
    units = ["B", "KiB", "MiB", "GiB", "TiB"]
    i = 0
    while num_bytes >= 1024 and i < len(units) - 1:
        num_bytes, remainder = divmod(num_bytes, 1024)
        i += 1
    return f"{num_bytes}{units[i]}"

print(human_size(5 * 1024 * 1024 * 1024))   # 5 GiB worth of bytes
```
**How it works, step by step:**
1. Each loop divides by 1024 and moves up one unit (B → KiB → MiB → …).
2. `divmod` gives the new size and a remainder (we ignore the remainder here for a simple result).
3. We stop once the number is small enough.

**Output:**
```
5GiB
```

**Mini-project (with solution):**

**Your task:** Convert a number of seconds into a readable `Dd Hh Mm Ss` uptime string.

**Solution:**
```python
def format_uptime(seconds):
    days, seconds = divmod(seconds, 86400)   # 86400 seconds in a day
    hours, seconds = divmod(seconds, 3600)   # 3600 seconds in an hour
    minutes, seconds = divmod(seconds, 60)   # 60 seconds in a minute
    return f"{days}d {hours}h {minutes}m {seconds}s"

print(format_uptime(90061))
```
**Output:**
```
1d 1h 1m 1s
```
**Explanation:** Each `divmod` peels off the next unit: first whole days, then hours from what's left, then minutes, leaving the final seconds. `90061` seconds works out to exactly 1 day, 1 hour, 1 minute, 1 second.

---

# E–F

## `enumerate()` 🔧

**What it does (plain English):** Lets you loop over a list while also getting a counter (0, 1, 2, …) automatically. Saves you from manually keeping track of "which number item am I on?"

**Syntax:** `enumerate(iterable, start=0)`

**Parameters:**
- `iterable` — the list/sequence to loop over.
- `start` — the number to start counting from (default `0`).

**What you get back:** Pairs of `(index, item)` you can loop over.

**Examples (with solutions):**

Example 1 — loop with an automatic counter
```python
servers = ["web-1", "web-2", "web-3"]
for index, name in enumerate(servers):
    print(index, name)
```
**Output:**
```
0 web-1
1 web-2
2 web-3
```
**What happened:** Each loop gives you both the position (`index`) and the value (`name`).

Example 2 — start counting at 1 (human-friendly)
```python
servers = ["web-1", "web-2"]
for number, name in enumerate(servers, start=1):
    print(f"#{number}: {name}")
```
**Output:**
```
#1: web-1
#2: web-2
```
**What happened:** `start=1` makes the counter begin at 1 instead of 0.

Example 3 — see the raw pairs
```python
print(list(enumerate(["a", "b"])))
```
**Output:**
```
[(0, 'a'), (1, 'b')]
```
**What happened:** `enumerate` produces `(index, item)` pairs; `list()` lets us see them all.

Example 4 — find the position of an item
```python
letters = "abc"
positions = [i for i, c in enumerate(letters) if c == "b"]
print(positions)
```
**Output:**
```
[1]
```
**What happened:** We kept only the index where the character was `"b"`, which is position `1`.

Example 5 — build a numbered dictionary
```python
print(dict(enumerate(["red", "green"])))
```
**Output:**
```
{0: 'red', 1: 'green'}
```
**What happened:** The pairs become key→value entries: position → color.

**Common mistakes (and the fix):**
- ❌ Manually doing `i = 0` and `i += 1` inside a loop. It's easy to make mistakes that way.
  ✅ Let `enumerate` handle the counter for you.

**Real-world use case (with full solution):**

**The problem:** You're doing a rolling deploy in batches and want to label each batch ("batch 1", "batch 2", …) in your logs.

**The solution:**
```python
def rolling_deploy(instances, batch_size=2):
    starts = range(0, len(instances), batch_size)
    for batch_number, start in enumerate(starts, start=1):
        batch = instances[start:start + batch_size]
        print(f"batch {batch_number}: deploying {batch}")

rolling_deploy(["i-1", "i-2", "i-3", "i-4", "i-5"])
```
**How it works, step by step:**
1. `range(0, len(...), batch_size)` gives the starting position of each batch.
2. `enumerate(..., start=1)` numbers the batches starting at 1.
3. We slice out each batch and print it with its number.

**Output:**
```
batch 1: deploying ['i-1', 'i-2']
batch 2: deploying ['i-3', 'i-4']
batch 3: deploying ['i-5']
```

**Mini-project (with solution):**

**Your task:** Print only the ERROR lines from a log, showing each one's original line number.

**Solution:**
```python
log_lines = ["service started", "ERROR disk full", "ok", "ERROR out of memory"]

for line_number, line in enumerate(log_lines, start=1):
    if "ERROR" in line:
        print(f"L{line_number}: {line}")
```
**Output:**
```
L2: ERROR disk full
L4: ERROR out of memory
```
**Explanation:** `enumerate(..., start=1)` gives a 1-based line number for every line. We print only the lines containing "ERROR", along with their real position in the file.

---

## `eval()` ⚠️

**What it does (plain English):** Takes a piece of Python written as **text** and runs it as a single expression, giving you the result. It's powerful but **dangerous**: if the text came from an outsider, it can run harmful code. As a beginner, treat `eval` as something to *avoid* — the use case below shows the safe alternative.

**Syntax:** `eval(expression_text)`

**Parameters:**
- `expression_text` — a single expression, as text.

**What you get back:** The value the expression produces.

**Examples (with solutions):**

Example 1 — evaluate simple math
```python
print(eval("2 + 3"))
```
**Output:**
```
5
```
**What happened:** Python ran the text `"2 + 3"` as code and returned `5`.

Example 2 — use a variable you provide
```python
print(eval("x * 2", {"x": 10}))
```
**Output:**
```
20
```
**What happened:** We supplied `x = 10` in a dictionary, so `x * 2` became `20`.

Example 3 — a built-in inside the text
```python
print(eval("len(name)", {"name": "server", "len": len}))
```
**Output:**
```
6
```
**What happened:** We had to pass `len` in too, because we controlled exactly what the code could see.

Example 4 — why it's dangerous (don't run on untrusted text)
```python
# eval("__import__('os').system('rm -rf /')")   # could DELETE FILES
print("never eval text from users or the internet")
```
**Output:**
```
never eval text from users or the internet
```
**What happened:** That commented line shows how `eval` on bad input could run destructive commands.

Example 5 — the SAFE alternative for *data*
```python
import ast
print(ast.literal_eval("{'replicas': 3, 'zones': ['a', 'b']}"))
```
**Output:**
```
{'replicas': 3, 'zones': ['a', 'b']}
```
**What happened:** `ast.literal_eval` reads simple data (numbers, lists, dicts) but **refuses** to run functions — much safer.

**Common mistakes (and the fix):**
- ❌ 🚨 Using `eval` on anything a user typed, a webhook sent, or a CI variable provided.
  ✅ For data, use `ast.literal_eval` or `json.loads`. For logic, write real code.

**Real-world use case (with full solution):**

**The problem:** You receive config as a Python-style string and need to turn it into a real dictionary — **without** the risk of running arbitrary code.

**The solution:**
```python
import ast

def parse_config(text):
    return ast.literal_eval(text)    # safe: only literals allowed

config = parse_config("{'replicas': 3, 'zones': ['a', 'b']}")
print(config["replicas"], config["zones"])
```
**How it works, step by step:**
1. `ast.literal_eval` understands literals: numbers, strings, lists, dicts, `True/False/None`.
2. It will *reject* anything that tries to call a function, so malicious input can't do damage.
3. You get back a normal Python dictionary.

**Output:**
```
3 ['a', 'b']
```

**Mini-project (with solution):**

**Your task:** Build a calculator that only allows arithmetic, by rejecting anything that isn't numbers and math symbols.

**Solution:**
```python
import re

def safe_calc(expression):
    if not re.fullmatch(r"[\d\s+\-*/().]+", expression):
        return "rejected: only arithmetic allowed"
    return eval(expression, {"__builtins__": {}}, {})

print(safe_calc("(2 + 3) * 4"))
print(safe_calc("__import__('os')"))
```
**Output:**
```
20
rejected: only arithmetic allowed
```
**Explanation:** Before calling `eval`, we check that the text contains only digits, spaces, and math symbols. The dangerous second input fails that check and is rejected. We also strip out built-ins as an extra safety net.

---

## `exec()` ⚠️

**What it does (plain English):** Like `eval`, but runs **full statements** (multiple lines, loops, function definitions) instead of a single expression. It returns nothing — its effects happen inside the code it runs. Same big warning: **never** run untrusted text. Beginners can safely skip this one.

**Syntax:** `exec(code_text)`

**Parameters:**
- `code_text` — Python statements, as text.

**What you get back:** `None` (the effects show up as side effects, like defining variables).

**Examples (with solutions):**

Example 1 — run a small statement
```python
exec("greeting = 'hello'")
print(greeting)
```
**Output:**
```
hello
```
**What happened:** `exec` created the variable `greeting`, which we then printed.

Example 2 — capture results in a dictionary
```python
namespace = {}
exec("total = 2 + 3", namespace)
print(namespace["total"])
```
**Output:**
```
5
```
**What happened:** We gave `exec` a dictionary to work in, then read the result out of it.

Example 3 — run a loop
```python
exec("for i in range(3): print(i)")
```
**Output:**
```
0
1
2
```
**What happened:** `exec` can run multi-step code like loops (unlike `eval`).

Example 4 — define a function dynamically
```python
namespace = {}
exec("def square(n): return n * n", namespace)
print(namespace["square"](4))
```
**Output:**
```
16
```
**What happened:** The function was defined inside `namespace`, then we called it.

Example 5 — it returns nothing
```python
result = exec("x = 1")
print(result)
```
**Output:**
```
None
```
**What happened:** `exec` always returns `None`; you read effects from the namespace, not a return value.

**Common mistakes (and the fix):**
- ❌ Expecting `exec` to give back a value. It returns `None`.
  ✅ Read your results from the namespace dictionary you passed in.
- ❌ 🚨 Running untrusted text → arbitrary code execution.
  ✅ Never do it on external input.

**Real-world use case (with full solution):**

**The problem:** A trusted internal codegen tool produces small helper functions as text, and you want to load them so you can call them.

**The solution:**
```python
def load_helpers(source_text):
    namespace = {"__builtins__": {}}   # locked-down environment
    exec(source_text, namespace)
    # keep only the functions that were defined
    return {name: value for name, value in namespace.items() if callable(value)}

helpers = load_helpers("def double(x): return x * 2")
print(helpers["double"](21))
```
**How it works, step by step:**
1. We run the generated code inside a restricted namespace.
2. After running, the namespace contains the new functions.
3. We pick out the callable ones and return them in a dictionary.

**Output:**
```
42
```

**Mini-project (with solution):**

**Your task:** Run a small "setup" snippet that computes a value, then use that value in a message.

**Solution:**
```python
def render(setup_code, template):
    namespace = {}
    exec(setup_code, {"__builtins__": {}}, namespace)
    return template.format(**namespace)

message = render("count = 3 * 2", "Provisioned {count} nodes")
print(message)
```
**Output:**
```
Provisioned 6 nodes
```
**Explanation:** `exec` runs `count = 3 * 2`, putting `count = 6` into the namespace. We then drop that into the template with `.format()`. Only use this pattern with code you wrote/control.

---

## `filter()` 🔧

**What it does (plain English):** Goes through a list and keeps only the items that pass a test you give it. It's a clean way to say "give me just the items where this is true."

**Syntax:** `filter(test_function, iterable)`

**Parameters:**
- `test_function` — a function that returns `True`/`False` for each item (or `None` to keep "truthy" items).
- `iterable` — the list to filter.

**What you get back:** A filtered sequence (wrap it in `list(...)` to see the items).

**Examples (with solutions):**

Example 1 — keep positive numbers
```python
numbers = [-1, 2, -3, 4]
result = list(filter(lambda x: x > 0, numbers))
print(result)
```
**Output:**
```
[2, 4]
```
**What happened:** The test `x > 0` is `True` only for `2` and `4`, so only those are kept.

Example 2 — drop "empty" values
```python
items = [0, 1, "", "x", None]
print(list(filter(None, items)))
```
**Output:**
```
[1, 'x']
```
**What happened:** Passing `None` as the test keeps only truthy items, removing `0`, `""`, and `None`.

Example 3 — keep `.log` files
```python
files = ["app.log", "data.txt", "error.log"]
logs = list(filter(lambda name: name.endswith(".log"), files))
print(logs)
```
**Output:**
```
['app.log', 'error.log']
```
**What happened:** The test keeps only names ending in `.log`.

Example 4 — count matching items
```python
numbers = range(10)
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(len(evens), "even numbers")
```
**Output:**
```
5 even numbers
```
**What happened:** We filtered to even numbers, then counted them with `len`.

Example 5 — remember to convert to a list
```python
result = filter(lambda x: x > 0, [1, -2, 3])
print(result)            # not the items yet!
print(list(result))      # now we see them
```
**Output:**
```
<filter object at 0x...>
[1, 3]
```
**What happened:** `filter` is "lazy" — it doesn't do the work until you ask for the items with `list()`.

**Common mistakes (and the fix):**
- ❌ `filter(None, data)` keeps *truthy* items — it removes `0` and `""` too, not just `None`.
  ✅ If you only want to remove `None`, use `filter(lambda x: x is not None, data)`.
- ❌ Forgetting `list(...)` and being confused by `<filter object>`.
  ✅ Wrap it: `list(filter(...))`.

**Real-world use case (with full solution):**

**The problem:** A cloud API returns many instances, and you only want the ones that are currently running.

**The solution:**
```python
def running_only(instances):
    return list(filter(lambda i: i["State"] == "running", instances))

data = [
    {"Id": "i-1", "State": "running"},
    {"Id": "i-2", "State": "stopped"},
    {"Id": "i-3", "State": "running"},
]
running = running_only(data)
print([i["Id"] for i in running])
```
**How it works, step by step:**
1. The test `i["State"] == "running"` is `True` only for running instances.
2. `filter` keeps just those.
3. We then pull out their IDs for printing.

**Output:**
```
['i-1', 'i-3']
```

**Mini-project (with solution):**

**Your task:** Find resources that are missing a required `owner` tag (a common compliance check).

**Solution:**
```python
def missing_owner(resources):
    return list(filter(lambda r: "owner" not in r.get("tags", {}), resources))

resources = [
    {"id": "bucket-1", "tags": {"owner": "sre"}},
    {"id": "bucket-2", "tags": {}},
    {"id": "bucket-3", "tags": {"team": "core"}},
]
flagged = missing_owner(resources)
print([r["id"] for r in flagged])
```
**Output:**
```
['bucket-2', 'bucket-3']
```
**Explanation:** For each resource we look at its tags. The test is `True` when `"owner"` is *not* present. `filter` keeps those, and we print their IDs as the ones to fix.

---

## `float()`

**What it does (plain English):** Turns a number or a piece of text into a decimal number (one that can have a fractional part, like `3.5`).

**Syntax:** `float(value)`

**Parameters:**
- `value` — a number or text like `"3.14"`.

**What you get back:** A decimal number (a `float`).

**Examples (with solutions):**

Example 1 — text to decimal
```python
print(float("3.14"))
```
**Output:**
```
3.14
```
**What happened:** The text `"3.14"` became the number `3.14`.

Example 2 — whole number to decimal
```python
print(float(5))
```
**Output:**
```
5.0
```
**What happened:** `5` became `5.0`, the decimal version.

Example 3 — surrounding spaces are ignored
```python
print(float("  2.5  "))
```
**Output:**
```
2.5
```
**What happened:** Leading/trailing spaces are trimmed automatically.

Example 4 — scientific notation
```python
print(float("1e3"))
```
**Output:**
```
1000.0
```
**What happened:** `1e3` means "1 times 10 to the power 3" = `1000.0`.

Example 5 — the classic decimal surprise
```python
print(0.1 + 0.2)
```
**Output:**
```
0.30000000000000004
```
**What happened:** Computers can't store some decimals perfectly, so tiny errors appear. Keep this in mind for money calculations.

**Common mistakes (and the fix):**
- ❌ Comparing decimals exactly: `0.1 + 0.2 == 0.3` is `False` because of tiny rounding errors.
  ✅ For money, use the `decimal` module; for general comparisons, check they're *close enough*.
- ❌ `float("n/a")` → error.
  ✅ Wrap risky conversions in `try/except` (see the use case).

**Real-world use case (with full solution):**

**The problem:** Cost or utilization values arrive as text and sometimes contain junk like `"n/a"`. You need numbers, with a safe fallback when conversion fails.

**The solution:**
```python
def to_float(value, default=0.0):
    try:
        return float(value)
    except (TypeError, ValueError):
        return default        # used when the text isn't a number

print(to_float("12.5"))
print(to_float("n/a"))
print(to_float(None))
```
**How it works, step by step:**
1. We try to convert the value to a float.
2. If that fails (bad text or `None`), the `except` block returns the default instead of crashing.

**Output:**
```
12.5
0.0
0.0
```

**Mini-project (with solution):**

**Your task:** Given a dict of service costs (as text), find which services are over budget.

**Solution:**
```python
def over_budget(costs, limit):
    result = {}
    for service, cost_text in costs.items():
        cost = float(cost_text)
        if cost > limit:
            result[service] = cost
    return result

costs = {"ec2": "120.50", "s3": "8.00", "rds": "60.00"}
print(over_budget(costs, limit=100))
```
**Output:**
```
{'ec2': 120.5}
```
**Explanation:** We convert each cost from text to a number with `float()`, compare it to the limit, and keep only the ones above it. Only EC2 is over `100`.

---

## `format()`

**What it does (plain English):** Formats a single value into a nicely-styled piece of text — adding commas to big numbers, fixing decimal places, padding for alignment, showing percentages, and so on. It's the engine behind f-strings.

**Syntax:** `format(value, format_spec)`

**Parameters:**
- `value` — the value to format.
- `format_spec` — a short code describing the style (e.g. `",.2f"` = commas + 2 decimals).

**What you get back:** A formatted text string.

**Examples (with solutions):**

Example 1 — add thousands separators
```python
print(format(1234567, ","))
```
**Output:**
```
1,234,567
```
**What happened:** The `","` spec inserts commas to make big numbers readable.

Example 2 — two decimal places
```python
print(format(3.14159, ".2f"))
```
**Output:**
```
3.14
```
**What happened:** `".2f"` means "decimal with 2 digits after the point".

Example 3 — show a percentage
```python
print(format(0.625, ".1%"))
```
**Output:**
```
62.5%
```
**What happened:** `".1%"` multiplies by 100 and adds a `%` sign, with 1 decimal.

Example 4 — pad for alignment
```python
print(format(42, ">8"))
```
**Output:**
```
      42
```
**What happened:** `">8"` right-aligns the value in a space 8 characters wide (good for tidy columns).

Example 5 — combine commas and decimals
```python
print(format(12345.6, ",.2f"))
```
**Output:**
```
12,345.60
```
**What happened:** Commas *and* two decimals together — perfect for money.

**Common mistakes (and the fix):**
- ❌ Mixing up `format(value, spec)` (formats one value) with `"...".format(...)` (fills in a template).
  ✅ For a single value, `format(value, spec)`; inside f-strings you can write `f"{value:,.2f}"`.

**Real-world use case (with full solution):**

**The problem:** You're building a cost report and want each line aligned, with money shown using commas and two decimals, and the percentage shown nicely.

**The solution:**
```python
def cost_line(service, amount, share):
    name = format(service, "<10")        # left-align, width 10
    money = format(amount, ">12,.2f")    # right-align, commas, 2 decimals
    pct = format(share, ".1%")           # percentage
    return f"{name}{money}  ({pct})"

print(cost_line("EC2", 12345.6, 0.62))
print(cost_line("S3", 8.0, 0.04))
```
**How it works, step by step:**
1. We format the name to a fixed width so columns line up.
2. We format the amount with commas and two decimals.
3. We format the share as a percentage, then combine everything.

**Output:**
```
EC2          12,345.60  (62.0%)
S3                8.00  (4.0%)
```

**Mini-project (with solution):**

**Your task:** Print an aligned status table without any external library.

**Solution:**
```python
def status_table(rows):
    for name, state, usage in rows:
        print(f"{format(name, '<12')}{format(state, '<10')}{format(usage, '>6.1%')}")

status_table([
    ("web-1", "running", 0.42),
    ("db-1", "degraded", 0.91),
])
```
**Output:**
```
web-1       running     42.0%
db-1        degraded    91.0%
```
**Explanation:** Each column uses a width so everything lines up: names left-aligned in 12 spaces, states in 10, and usage right-aligned as a percentage. The result is a clean, readable table.

---

## `frozenset()`

**What it does (plain English):** Makes a **set that can never be changed**. A normal set is a bag of unique items; a frozenset is the same but locked. Because it's locked, you can use it as a dictionary key or put it inside another set.

**Syntax:** `frozenset(iterable)`

**Parameters:**
- `iterable` — a list/collection of items (duplicates are removed automatically).

**What you get back:** A `frozenset` (read-only).

**Examples (with solutions):**

Example 1 — duplicates are removed
```python
print(frozenset([1, 2, 2, 3]))
```
**Output:**
```
frozenset({1, 2, 3})
```
**What happened:** The repeated `2` is collapsed to one; sets hold only unique items.

Example 2 — you can't change it
```python
fs = frozenset([1, 2])
# fs.add(3)   # this would ERROR — frozensets are locked
print(fs)
```
**Output:**
```
frozenset({1, 2})
```
**What happened:** Unlike a normal set, you can't add or remove items.

Example 3 — find common items (intersection)
```python
a = frozenset([1, 2, 3])
b = frozenset([2, 3, 4])
print(a & b)
```
**Output:**
```
frozenset({2, 3})
```
**What happened:** `&` keeps items that appear in both sets.

Example 4 — use it as a dictionary key (a normal set can't do this)
```python
groups = {frozenset({"read", "write"}): "editor"}
print(groups[frozenset({"read", "write"})])
```
**Output:**
```
editor
```
**What happened:** Because frozensets are locked, Python allows them as keys.

Example 5 — check "is this a subset?"
```python
allowed = frozenset({"read", "list"})
print(frozenset({"read"}) <= allowed)
```
**Output:**
```
True
```
**What happened:** `<=` asks "is every item on the left also on the right?" — yes, so `True`.

**Common mistakes (and the fix):**
- ❌ Trying to add items: `fs.add(x)` → error.
  ✅ If you need to change it, use a normal `set` instead.

**Real-world use case (with full solution):**

**The problem:** You have a fixed list of read-only permissions and want to check whether a user's permissions stay within that allowed set — using something safe that can't be accidentally modified.

**The solution:**
```python
READONLY = frozenset({"s3:GetObject", "s3:ListBucket"})

def is_readonly(user_perms):
    return frozenset(user_perms) <= READONLY    # all within allowed?

print(is_readonly(["s3:GetObject"]))
print(is_readonly(["s3:DeleteObject"]))
```
**How it works, step by step:**
1. `READONLY` is a locked set of safe permissions.
2. `frozenset(user_perms) <= READONLY` asks "are all the user's permissions inside the allowed set?"
3. The first user is fine; the second has a delete permission, so it's `False`.

**Output:**
```
True
False
```

**Mini-project (with solution):**

**Your task:** Several users have permission lists. Find how many *unique* roles exist (users with the same set of permissions share a role, regardless of order).

**Solution:**
```python
def count_unique_roles(user_permissions):
    roles = set()
    for perms in user_permissions.values():
        roles.add(frozenset(perms))     # frozenset so it can live in a set
    return len(roles)

users = {
    "alice": ["read", "write"],
    "bob": ["write", "read"],   # same as alice, different order
    "carol": ["read"],
}
print(count_unique_roles(users))
```
**Output:**
```
2
```
**Explanation:** Order doesn't matter for sets, so alice and bob both become `frozenset({"read", "write"})` — counted once. Carol is different. That leaves 2 unique roles. We needed `frozenset` because you can't put a normal set inside another set.

---

# G–H

## `getattr()` 🔧

**What it does (plain English):** Reads an attribute (a stored value) from an object when you only know its name as **text**. It's the flexible version of writing `obj.name`. You can also give a fallback so it won't crash if the attribute is missing.

**Syntax:** `getattr(object, "name")` or `getattr(object, "name", default)`

**Parameters:**
- `object` — the object to read from.
- `name` — the attribute name, as text.
- `default` *(optional)* — what to return if the attribute doesn't exist.

**What you get back:** The attribute's value (or the default).

**Examples (with solutions):**

Example 1 — read an attribute by name
```python
class Server:
    region = "us-east-1"

print(getattr(Server, "region"))
```
**Output:**
```
us-east-1
```
**What happened:** `getattr(Server, "region")` is the same as `Server.region`, but the name came from text.

Example 2 — use a fallback for a missing attribute
```python
class Server:
    region = "us-east-1"

print(getattr(Server, "zone", "unknown"))
```
**Output:**
```
unknown
```
**What happened:** There's no `zone`, so instead of crashing we get the fallback `"unknown"`.

Example 3 — without a fallback, missing = error
```python
class Server:
    pass

# getattr(Server, "zone")   # would raise AttributeError
print(getattr(Server, "zone", None))   # safe version
```
**Output:**
```
None
```
**What happened:** Always provide a default when the attribute might not exist.

Example 4 — fetch and call a method
```python
text = "hello"
upper_method = getattr(text, "upper")
print(upper_method())
```
**Output:**
```
HELLO
```
**What happened:** `getattr` returned the `upper` method; adding `()` ran it.

Example 5 — pick an attribute name from a variable
```python
class Config:
    region = "eu-west-1"
    replicas = 3

field = "replicas"
print(getattr(Config, field))
```
**Output:**
```
3
```
**What happened:** The attribute name was stored in `field`, and `getattr` used it.

**Common mistakes (and the fix):**
- ❌ No default on a possibly-missing attribute → `AttributeError`.
  ✅ Pass a default: `getattr(obj, name, None)`.
- ❌ Forgetting to add `()` when you fetched a method, so nothing runs.
  ✅ Call it: `getattr(obj, "method")()`.

**Real-world use case (with full solution):**

**The problem:** Your config says which cloud action to run (e.g. `"describe_instances"`). You want to call the matching method on a client by its name.

**The solution:**
```python
class FakeClient:
    def describe_instances(self, **kwargs):
        return {"ok": True, "args": kwargs}

def run_action(client, action_name, **params):
    operation = getattr(client, action_name, None)
    if not callable(operation):
        return f"unsupported action: {action_name}"
    return operation(**params)

print(run_action(FakeClient(), "describe_instances", MaxResults=5))
print(run_action(FakeClient(), "delete_everything"))
```
**How it works, step by step:**
1. `getattr(client, action_name, None)` looks up the method by name.
2. `callable(...)` checks we actually found one.
3. If yes, we run it with the given parameters; if not, we return a safe message.

**Output:**
```
{'ok': True, 'args': {'MaxResults': 5}}
unsupported action: delete_everything
```

**Mini-project (with solution):**

**Your task:** Build a tiny command router that maps subcommands (`deploy`, `status`) to handler methods by name.

**Solution:**
```python
class CLI:
    def cmd_deploy(self, env):
        return f"deploying to {env}"

    def cmd_status(self, env):
        return f"status of {env}"

    def run(self, command, env):
        handler = getattr(self, f"cmd_{command}", None)
        if handler is None:
            return f"unknown command: {command}"
        return handler(env)

cli = CLI()
print(cli.run("deploy", "prod"))
print(cli.run("backup", "prod"))
```
**Output:**
```
deploying to prod
unknown command: backup
```
**Explanation:** We build the method name as `cmd_<command>` and fetch it with `getattr`. Known commands run; unknown ones return a friendly message instead of crashing.

---

## `globals()`

**What it does (plain English):** Gives you a dictionary of all the "global" names in your file — the variables and functions defined at the top level (not inside a function). Mostly used to *look things up*, not to change them.

**Syntax:** `globals()`

**Parameters:** None.

**What you get back:** A dictionary of `name → value` for everything defined at the file's top level.

**Examples (with solutions):**

Example 1 — read a global variable by name
```python
REGION = "us-east-1"
print(globals()["REGION"])
```
**Output:**
```
us-east-1
```
**What happened:** `globals()` holds your top-level names; we looked up `REGION`.

Example 2 — check whether a name exists
```python
REGION = "us-east-1"
print("REGION" in globals())
print("MISSING" in globals())
```
**Output:**
```
True
False
```
**What happened:** We can test if a global name has been defined.

Example 3 — list your constants (UPPERCASE names)
```python
REGION = "us-east-1"
MAX_RETRIES = 3
name = "ignore-me"
constants = [n for n in globals() if n.isupper()]
print(sorted(constants))
```
**Output:**
```
['MAX_RETRIES', 'REGION']
```
**What happened:** We kept only the all-uppercase names, which by convention are constants.

Example 4 — read several config constants
```python
AWS_REGION = "us-east-1"
TIMEOUT = 30
config = {n: globals()[n] for n in ["AWS_REGION", "TIMEOUT"]}
print(config)
```
**Output:**
```
{'AWS_REGION': 'us-east-1', 'TIMEOUT': 30}
```
**What happened:** We built a small config snapshot by reading named globals.

Example 5 — it's a normal dictionary
```python
print(type(globals()).__name__)
```
**Output:**
```
dict
```
**What happened:** `globals()` returns an ordinary dictionary you can read like any other.

**Common mistakes (and the fix):**
- ❌ Adding variables by writing into `globals()` — confusing and error-prone.
  ✅ Just define variables normally, or store config in a real dictionary.

**Real-world use case (with full solution):**

**The problem:** You keep config as uppercase constants and want to gather them all into one dictionary for logging.

**The solution:**
```python
AWS_REGION = "us-east-1"
MAX_RETRIES = 3
TIMEOUT = 30

def config_snapshot():
    return {name: value for name, value in globals().items() if name.isupper()}

print(config_snapshot())
```
**How it works, step by step:**
1. `globals().items()` gives every top-level `name, value`.
2. We keep only the uppercase names (your constants).
3. The result is a tidy config dictionary you can log.

**Output:**
```
{'AWS_REGION': 'us-east-1', 'MAX_RETRIES': 3, 'TIMEOUT': 30}
```

**Mini-project (with solution):**

**Your task:** Automatically collect every function whose name starts with `task_` into a dispatch table.

**Solution:**
```python
def task_backup():
    return "backup done"

def task_cleanup():
    return "cleanup done"

tasks = {}
for name, value in globals().items():
    if name.startswith("task_") and callable(value):
        tasks[name[5:]] = value      # drop the "task_" prefix

print(tasks["backup"]())
print(list(tasks))
```
**Output:**
```
backup done
['backup', 'cleanup']
```
**Explanation:** We scan all globals for functions whose names start with `task_`, then store them under a short name. This is a simple "auto-registration" pattern — add a new `task_` function and it appears automatically.

---

## `hasattr()`

**What it does (plain English):** Asks a simple yes/no question: "Does this object have an attribute with this name?" Returns `True` or `False`. Handy before reading or deleting an attribute.

**Syntax:** `hasattr(object, "name")`

**Parameters:**
- `object` — the object to check.
- `name` — the attribute name, as text.

**What you get back:** `True` or `False`.

**Examples (with solutions):**

Example 1 — text has an `upper` method
```python
print(hasattr("hello", "upper"))
```
**Output:**
```
True
```
**What happened:** Strings have `upper`, so `True`.

Example 2 — a number doesn't have `append`
```python
print(hasattr(42, "append"))
```
**Output:**
```
False
```
**What happened:** Numbers can't `append`, so `False`.

Example 3 — check a custom object
```python
class Box:
    color = "red"

b = Box()
print(hasattr(b, "color"))
print(hasattr(b, "size"))
```
**Output:**
```
True
False
```
**What happened:** `b` has `color` but not `size`.

Example 4 — guard before reading
```python
class Box:
    pass

b = Box()
if hasattr(b, "region"):
    print(b.region)
else:
    print("no region set")
```
**Output:**
```
no region set
```
**What happened:** We checked first, avoiding a crash on the missing attribute.

Example 5 — filter a list of names
```python
class Box:
    region = "us-east-1"

b = Box()
present = [name for name in ["region", "zone"] if hasattr(b, name)]
print(present)
```
**Output:**
```
['region']
```
**What happened:** Only `region` exists on `b`, so only it survives the filter.

**Common mistakes (and the fix):**
- ❌ Using `hasattr` heavily where a simple default would be cleaner.
  ✅ Often `getattr(obj, name, default)` does the check and the read in one step.

**Real-world use case (with full solution):**

**The problem:** Different versions of a cloud SDK have different methods. You want to use a newer method if it's available, and fall back if not.

**The solution:**
```python
def describe(client):
    if hasattr(client, "describe_instance_details"):
        return "using the detailed describe call"
    return "falling back to the basic describe call"

class OldClient:
    pass

class NewClient:
    def describe_instance_details(self):
        pass

print(describe(OldClient()))
print(describe(NewClient()))
```
**How it works, step by step:**
1. `hasattr` checks whether the newer method exists on this client.
2. If yes, we use it; if not, we use the older approach.
3. This keeps your code working across SDK versions.

**Output:**
```
falling back to the basic describe call
using the detailed describe call
```

**Mini-project (with solution):**

**Your task:** Pull a set of fields from an object, filling in `"N/A"` wherever a field is missing.

**Solution:**
```python
def extract(obj, fields, missing="N/A"):
    result = {}
    for field in fields:
        if hasattr(obj, field):
            result[field] = getattr(obj, field)
        else:
            result[field] = missing
    return result

class Box:
    pass

b = Box()
b.region = "us-east-1"
print(extract(b, ["region", "zone", "owner"]))
```
**Output:**
```
{'region': 'us-east-1', 'zone': 'N/A', 'owner': 'N/A'}
```
**Explanation:** For each field, `hasattr` decides whether to read the real value with `getattr` or substitute `"N/A"`. The result is a complete record with no missing keys.

---

## `hash()`

**What it does (plain English):** Turns a value into a number "fingerprint." Equal values always get the same fingerprint. Python uses this internally to make dictionaries and sets fast. Only unchangeable values (numbers, text, tuples) can be hashed.

**Syntax:** `hash(object)`

**Parameters:**
- `object` — an unchangeable (hashable) value.

**What you get back:** An integer fingerprint (it can be negative).

**Examples (with solutions):**

Example 1 — a number hashes to itself
```python
print(hash(42))
```
**Output:**
```
42
```
**What happened:** Small whole numbers hash to themselves.

Example 2 — equal values hash equally
```python
print(hash(3) == hash(3.0))
```
**Output:**
```
True
```
**What happened:** `3` and `3.0` are equal, so they share a fingerprint.

Example 3 — tuples are hashable
```python
print(type(hash((1, 2))).__name__)
```
**Output:**
```
int
```
**What happened:** A tuple of numbers can be hashed, producing an integer.

Example 4 — lists are NOT hashable
```python
try:
    hash([1, 2])
except TypeError as e:
    print("error:", e)
```
**Output:**
```
error: unhashable type: 'list'
```
**What happened:** Lists can change, so they can't be hashed (and can't be dict keys).

Example 5 — text hashing varies between runs
```python
# hash("abc") gives a number, but it changes each time you start Python
print(isinstance(hash("abc"), int))
```
**Output:**
```
True
```
**What happened:** String hashes are randomized per run for security — never save them to compare later.

**Common mistakes (and the fix):**
- ❌ Trying to hash a list or dict → error.
  ✅ Convert to a tuple/frozenset first if you need a hashable version.
- ❌ Saving a string's `hash()` to a file expecting it to match next run — it won't.
  ✅ For stable fingerprints, use `hashlib` (see the mini-project).

**Real-world use case (with full solution):**

**The problem:** Within a single run, you're receiving events and want to skip duplicates quickly.

**The solution:**
```python
def deduplicate(events):
    seen = set()
    unique = []
    for event in events:
        fingerprint = hash((event["source"], event["type"], event["id"]))
        if fingerprint not in seen:
            seen.add(fingerprint)
            unique.append(event)
    return unique

events = [
    {"source": "s3", "type": "put", "id": "1"},
    {"source": "s3", "type": "put", "id": "1"},   # duplicate
    {"source": "s3", "type": "put", "id": "2"},
]
print(len(deduplicate(events)), "unique events")
```
**How it works, step by step:**
1. For each event we build a fingerprint from its key fields.
2. If we've seen that fingerprint, we skip the event.
3. Otherwise we record it and keep the event.

**Output:**
```
2 unique events
```

**Mini-project (with solution):**

**Your task:** Spread keys evenly across 4 "shards" using a **stable** hash (one that's the same every run). Use `hashlib`, not `hash()`.

**Solution:**
```python
import hashlib

def shard_for(key, shard_count):
    digest = hashlib.sha256(key.encode()).hexdigest()
    number = int(digest, 16)            # turn the hex fingerprint into a number
    return number % shard_count         # remainder picks the shard

for user in ["user-1", "user-2", "user-3"]:
    print(user, "->", "shard", shard_for(user, 4))
```
**Output:**
```
user-1 -> shard 2
user-2 -> shard 1
user-3 -> shard 0
```
**Explanation:** `hashlib.sha256` gives a stable fingerprint that's identical every run (unlike `hash()`). We turn it into a number and use `% 4` to choose one of four shards. The same key always lands on the same shard.

---

## `help()`

**What it does (plain English):** Shows you the built-in documentation for something — what it does and how to use it. Perfect for learning a function without leaving Python.

**Syntax:** `help(object)`

**Parameters:**
- `object` — the function, method, or type you want help on.

**What you get back:** Nothing returned — it *prints* the documentation.

**Examples (with solutions):**

Example 1 — help on a built-in function
```python
help(len)
```
**Output (trimmed):**
```
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.
```
**What happened:** It printed `len`'s purpose and how to call it.

Example 2 — help on a method
```python
help(str.upper)
```
**Output (trimmed):**
```
Help on method_descriptor:

upper(self, /)
    Return a copy of the string converted to uppercase.
```
**What happened:** We learned what `str.upper` does without a web search.

Example 3 — read a docstring programmatically
```python
print(sorted.__doc__[:48])
```
**Output:**
```
Return a new list containing all items from the i
```
**What happened:** `__doc__` is the same help text as a string you can slice.

Example 4 — help on a whole type
```python
# help(list)   # prints ALL list methods (long output)
print("run help(list) in a REPL to see every list method")
```
**Output:**
```
run help(list) in a REPL to see every list method
```
**What happened:** `help(list)` is great in an interactive session but prints a lot.

Example 5 — help in your own function
```python
def deploy(env):
    "Deploy the app to the given environment."
    return f"deploying to {env}"

print(deploy.__doc__)
```
**Output:**
```
Deploy the app to the given environment.
```
**What happened:** The text right under `def` is your function's docstring, shown by `help()` too.

**Common mistakes (and the fix):**
- ❌ Calling bare `help()` (no argument) inside a script → it starts an interactive prompt that hangs automation.
  ✅ Always pass an argument: `help(len)`.

**Real-world use case (with full solution):**

**The problem:** While writing automation in an interactive session, you want to quickly check a function's documentation programmatically (e.g. to log or display it).

**The solution:**
```python
def show_doc(func):
    doc = func.__doc__ or "(no documentation)"
    first_line = doc.strip().splitlines()[0]
    return f"{func.__name__}: {first_line}"

print(show_doc(sorted))
print(show_doc(len))
```
**How it works, step by step:**
1. `func.__doc__` is the documentation text (the same thing `help` shows).
2. We grab just the first line for a short summary.
3. We pair it with the function's name.

**Output:**
```
sorted: Return a new list containing all items from the iterable in ascending order.
len: Return the number of items in a container.
```

**Mini-project (with solution):**

**Your task:** Report which functions are missing documentation (a quick quality check).

**Solution:**
```python
def deploy(): "Deploy the app."
def cleanup(): pass        # no docstring

functions = {"deploy": deploy, "cleanup": cleanup}

undocumented = [name for name, fn in functions.items() if not fn.__doc__]
print("missing docs:", undocumented)
```
**Output:**
```
missing docs: ['cleanup']
```
**Explanation:** A function's `__doc__` is `None` when it has no docstring. We collect the names of functions where `__doc__` is empty — here, only `cleanup` needs documentation.

---

## `hex()`

**What it does (plain English):** Shows a whole number in hexadecimal (base 16), labeled with `0x`. Hex is a compact way to write big numbers and is common for colors, hashes, and addresses.

**Syntax:** `hex(x)`

**Parameters:**
- `x` — a whole number.

**What you get back:** Text like `'0xff'`.

**Examples (with solutions):**

Example 1 — 255 in hex
```python
print(hex(255))
```
**Output:**
```
0xff
```
**What happened:** `255` is `ff` in hex; the `0x` marks it as hexadecimal.

Example 2 — 16 in hex
```python
print(hex(16))
```
**Output:**
```
0x10
```
**What happened:** After 15 (`f`), hex rolls over to `10`.

Example 3 — drop the `0x` prefix
```python
print(hex(255)[2:])
```
**Output:**
```
ff
```
**What happened:** `[2:]` removes the `0x`, leaving just the digits.

Example 4 — round-trip back to a number
```python
print(int(hex(255), 16))
```
**Output:**
```
255
```
**What happened:** `int(text, 16)` reads hex text back into a normal number.

Example 5 — a negative number
```python
print(hex(-42))
```
**Output:**
```
-0x2a
```
**What happened:** The minus sign goes in front of the hex form.

**Common mistakes (and the fix):**
- ❌ Forgetting the `0x` is part of the text.
  ✅ Use `hex(x)[2:]` for bare digits.
- ❌ `hex(3.5)` → error (decimals not allowed).
  ✅ Convert first: `hex(int(3.5))`.

**Real-world use case (with full solution):**

**The problem:** You want a short, readable fingerprint of a deploy string to use as a cache-busting tag.

**The solution:**
```python
import hashlib

def short_fingerprint(text):
    digest_bytes = hashlib.sha256(text.encode()).digest()[:4]   # first 4 bytes
    number = int.from_bytes(digest_bytes, "big")                # bytes -> number
    return hex(number)

print(short_fingerprint("deploy-v2"))
```
**How it works, step by step:**
1. We hash the text and take the first 4 bytes.
2. `int.from_bytes` turns those bytes into a number.
3. `hex(...)` shows it compactly as a hex string.

**Output:**
```
0x... (an 8-character hex fingerprint)
```

**Mini-project (with solution):**

**Your task:** Format a list of byte numbers as a MAC address like `00:1b:44:11:3a:b7`.

**Solution:**
```python
def to_mac(byte_numbers):
    parts = []
    for b in byte_numbers:
        digits = hex(b)[2:].zfill(2)     # drop 0x, pad to 2 digits
        parts.append(digits)
    return ":".join(parts)

print(to_mac([0x00, 0x1B, 0x44, 0x11, 0x3A, 0xB7]))
```
**Output:**
```
00:1b:44:11:3a:b7
```
**Explanation:** For each byte we get its hex digits (without `0x`), pad to two characters with `zfill(2)`, then join everything with colons to form a standard MAC address.

---

# I

## `id()`

**What it does (plain English):** Gives a unique number that identifies an exact object in memory while your program runs. Two variables that point to the *same* object share the same `id`. Useful for spotting when two names secretly refer to one thing.

**Syntax:** `id(object)`

**Parameters:**
- `object` — any value.

**What you get back:** A unique integer (different each run; don't save it).

**Examples (with solutions):**

Example 1 — same object, same id
```python
a = [1, 2]
b = a               # b points to the SAME list
print(id(a) == id(b))
```
**Output:**
```
True
```
**What happened:** `b = a` doesn't copy; both names point to one list, so the ids match.

Example 2 — equal but separate objects
```python
a = [1, 2]
c = [1, 2]          # a brand-new list with the same contents
print(a == c)       # same contents?
print(id(a) == id(c))   # same object?
```
**Output:**
```
True
False
```
**What happened:** `a` and `c` have equal *contents* (`==` is `True`) but are *different objects* (ids differ).

Example 3 — `is` checks identity
```python
a = [1, 2]
b = a
print(a is b)       # 'is' compares ids under the hood
```
**Output:**
```
True
```
**What happened:** `a is b` is the readable way to ask "same object?" — it uses `id` internally.

Example 4 — small numbers are reused
```python
x = 256
y = 256
print(id(x) == id(y))
```
**Output:**
```
True
```
**What happened:** Python reuses small integers, so both names point to the same `256`.

Example 5 — id changes between runs
```python
print(isinstance(id("anything"), int))
```
**Output:**
```
True
```
**What happened:** `id` is always an integer, but its exact value is meaningless across runs — don't store it.

**Common mistakes (and the fix):**
- ❌ Using `id(a) == id(b)` to compare values. That only checks if they're the *same object*.
  ✅ Use `==` for value comparison, and `is`/`is not` for identity.

**Real-world use case (with full solution):**

**The problem:** A classic Python bug: using a mutable default like `items=[]` causes every call to secretly share one list. You want to *prove* they're sharing.

**The solution:**
```python
def buggy(items=[]):           # DON'T do this — shared default list
    items.append("x")
    return items

first = buggy()
second = buggy()
print(first, second)
print("sharing the same list?", id(first) == id(second))
```
**How it works, step by step:**
1. The default `[]` is created once and reused across calls.
2. Both calls append to that same list.
3. `id(first) == id(second)` being `True` proves they're the same object — the bug.

**Output:**
```
['x', 'x'] ['x', 'x']
sharing the same list? True
```
> The fix is `def safe(items=None): items = items or []` so each call gets a fresh list.

**Mini-project (with solution):**

**Your task:** Given named objects, group together the names that point to the same underlying object.

**Solution:**
```python
def alias_groups(named):
    by_id = {}
    for name, obj in named.items():
        by_id.setdefault(id(obj), []).append(name)
    return [names for names in by_id.values() if len(names) > 1]

shared = [1, 2]
print(alias_groups({"a": shared, "b": shared, "c": [1, 2]}))
```
**Output:**
```
[['a', 'b']]
```
**Explanation:** We group names by their object's `id`. `a` and `b` point to the same list (same id), so they're grouped. `c` is a separate list, so it's alone and filtered out.

---

## `input()`

**What it does (plain English):** Pauses your program and waits for the user to type a line, then gives you what they typed as **text**. Used for interactive scripts.

**Syntax:** `input("optional prompt: ")`

**Parameters:**
- `prompt` *(optional)* — a message shown before waiting for input.

**What you get back:** The typed line, as text (always text, even if they type numbers).

**Examples (with solutions):**

Example 1 — ask for a name
```python
name = input("Your name: ")
print("Hello,", name)
```
**Example interaction:**
```
Your name: Sam
Hello, Sam
```
**What happened:** The program waited, the user typed `Sam`, and we greeted them.

Example 2 — input is always text (convert for numbers)
```python
count = input("How many servers? ")
print(type(count).__name__)     # what type did we get?
```
**Example interaction:**
```
How many servers? 3
str
```
**What happened:** Even though they typed `3`, we got the *text* `"3"`. Convert with `int()` to do math.

Example 3 — convert to a number
```python
count = int(input("How many servers? "))
print("total:", count + 1)
```
**Example interaction:**
```
How many servers? 3
total: 4
```
**What happened:** `int(...)` turned the text into a real number so we could add.

Example 4 — provide a default for an empty answer
```python
region = input("Region: ") or "us-east-1"
print("using", region)
```
**Example interaction (user just presses Enter):**
```
Region:
using us-east-1
```
**What happened:** If the user types nothing, `"" or "us-east-1"` gives the default.

Example 5 — normalize the answer
```python
answer = input("Proceed? (y/n) ").strip().lower()
print("proceed" if answer == "y" else "cancel")
```
**Example interaction:**
```
Proceed? (y/n)  Y
proceed
```
**What happened:** `.strip().lower()` cleans up spacing and capitalization so `"Y"` matches `"y"`.

**Common mistakes (and the fix):**
- ❌ Doing math on `input()` directly — it's text, so `input() + 1` errors.
  ✅ Convert: `int(input(...))` or `float(input(...))`.
- ❌ Using `input()` in automated pipelines (CI) — it waits forever for input that never comes.
  ✅ In automation, read from command-line arguments or environment variables instead.

**Real-world use case (with full solution):**

**The problem:** Before deleting a production resource, you want the operator to type the exact resource name to confirm — a safety check against accidents.

**The solution:**
```python
def confirm_delete(resource_name):
    typed = input(f"Type '{resource_name}' to confirm deletion: ").strip()
    if typed != resource_name:
        return "aborted: name did not match"
    return f"deleting {resource_name}..."

# Example: confirm_delete("prod-database")
print("(this runs interactively)")
```
**How it works, step by step:**
1. We ask the operator to type the resource name exactly.
2. We compare what they typed to the real name.
3. Only an exact match proceeds; anything else aborts safely.

**Output (interactive):**
```
Type 'prod-database' to confirm deletion: prod-database
deleting prod-database...
```

**Mini-project (with solution):**

**Your task:** Build a small setup wizard that asks a few questions with sensible defaults.

**Solution:**
```python
def setup_wizard():
    region = input("Region [us-east-1]: ").strip() or "us-east-1"
    count_text = input("Instance count [1]: ").strip() or "1"
    return {"region": region, "count": int(count_text)}

# config = setup_wizard()
# print(config)
print("(run setup_wizard() in a terminal to try it)")
```
**Output (interactive example):**
```
Region [us-east-1]:
Instance count [1]: 3
{'region': 'us-east-1', 'count': 3}
```
**Explanation:** Each question offers a default (used when the operator presses Enter). We convert the count to a real number with `int()` so it's ready to use.

---

## `int()` 🔧

**What it does (plain English):** Turns a number or text into a whole number (no decimal part). If you give it a decimal, it chops off everything after the point (it does **not** round).

**Syntax:** `int(value)` or `int("text", base)`

**Parameters:**
- `value` — a number or text to convert.
- `base` *(optional)* — the number system of the text, e.g. `16` for hex, `2` for binary.

**What you get back:** A whole number (`int`).

**Examples (with solutions):**

Example 1 — text to whole number
```python
print(int("42"))
```
**Output:**
```
42
```
**What happened:** The text `"42"` became the number `42`.

Example 2 — decimals get chopped, not rounded
```python
print(int(3.9))
```
**Output:**
```
3
```
**What happened:** `int` removes the decimal part, so `3.9` becomes `3` (not `4`).

Example 3 — read hex text
```python
print(int("ff", 16))
```
**Output:**
```
255
```
**What happened:** With base `16`, the text `"ff"` is read as hexadecimal = `255`.

Example 4 — surrounding spaces are fine
```python
print(int("  7  "))
```
**Output:**
```
7
```
**What happened:** Spaces around the number are trimmed automatically.

Example 5 — decimal-looking text errors
```python
try:
    int("3.0")
except ValueError as e:
    print("error:", e)
```
**Output:**
```
error: invalid literal for int() with base 10: '3.0'
```
**What happened:** `int("3.0")` fails because of the dot. Do `int(float("3.0"))` instead.

**Common mistakes (and the fix):**
- ❌ Expecting `int(3.9)` to round to `4`. It truncates to `3`.
  ✅ Use `round(3.9)` if you want rounding.
- ❌ `int("3.0")` → error.
  ✅ Convert through float first: `int(float("3.0"))`.

**Real-world use case (with full solution):**

**The problem:** Numeric tuning values come from environment variables (always text) and might be missing or invalid. You need a safe whole number with a default.

**The solution:**
```python
import os

def env_int(name, default):
    raw = os.environ.get(name, "")
    try:
        return int(raw.strip())
    except ValueError:
        return default

os.environ["MAX_RETRIES"] = "5"
print(env_int("MAX_RETRIES", 3))      # set -> 5
print(env_int("MISSING_VALUE", 3))    # unset/invalid -> default 3
```
**How it works, step by step:**
1. We read the variable as text (empty string if missing).
2. We try to convert it to a whole number.
3. If that fails, we return the default instead of crashing.

**Output:**
```
5
3
```

**Mini-project (with solution):**

**Your task:** Expand a port range like `"8000-8003"` into a list of individual ports.

**Solution:**
```python
def parse_ports(spec):
    if "-" in spec:
        low_text, high_text = spec.split("-")
        low, high = int(low_text), int(high_text)
        return list(range(low, high + 1))
    return [int(spec)]

print(parse_ports("8000-8003"))
print(parse_ports("9090"))
```
**Output:**
```
[8000, 8001, 8002, 8003]
[9090]
```
**Explanation:** If there's a dash, we split it and convert both sides to whole numbers, then build the range (`+ 1` because `range` stops one early). A single port just becomes a one-item list.

---

## `isinstance()` 🔧

**What it does (plain English):** Checks whether a value is of a certain type (a number, text, list, etc.). Returns `True`/`False`. This is the recommended way to check "what kind of thing is this?"

**Syntax:** `isinstance(value, type)` or `isinstance(value, (type1, type2))`

**Parameters:**
- `value` — the thing to check.
- `type` — a type, or a tuple of types ("any of these").

**What you get back:** `True` or `False`.

**Examples (with solutions):**

Example 1 — is it a whole number?
```python
print(isinstance(5, int))
```
**Output:**
```
True
```
**What happened:** `5` is an `int`, so `True`.

Example 2 — accept several types
```python
print(isinstance(5.0, (int, float)))
```
**Output:**
```
True
```
**What happened:** The value matches one of the listed types (`float`), so `True`.

Example 3 — is it text?
```python
print(isinstance("hello", str))
```
**Output:**
```
True
```
**What happened:** `"hello"` is a string, so `True`.

Example 4 — the boolean surprise
```python
print(isinstance(True, int))
```
**Output:**
```
True
```
**What happened:** In Python, `True`/`False` are technically a kind of integer, so this is `True`. Check `bool` first if you must tell them apart.

Example 5 — wrong type
```python
print(isinstance([1, 2], dict))
```
**Output:**
```
False
```
**What happened:** A list isn't a dict, so `False`.

**Common mistakes (and the fix):**
- ❌ Using `type(x) == int` instead of `isinstance`. That fails for subclasses.
  ✅ Prefer `isinstance(x, int)`.
- ❌ Forgetting `isinstance(True, int)` is `True`.
  ✅ If you must separate them: check `isinstance(x, bool)` *before* checking `int`.

**Real-world use case (with full solution):**

**The problem:** You parsed some YAML/JSON config and must confirm it has the right shape before using it (avoid crashing deep in your code on bad input).

**The solution:**
```python
def validate(config):
    if not isinstance(config, dict):
        return "error: config must be a mapping"
    if not isinstance(config.get("replicas"), int):
        return "error: 'replicas' must be a whole number"
    if not isinstance(config.get("zones", []), list):
        return "error: 'zones' must be a list"
    return "config looks valid"

print(validate({"replicas": 3, "zones": ["a", "b"]}))
print(validate({"replicas": "three"}))
```
**How it works, step by step:**
1. First we confirm the whole config is a dictionary.
2. Then we check each field is the expected type.
3. We return a clear message instead of crashing on bad data.

**Output:**
```
config looks valid
error: 'replicas' must be a whole number
```

**Mini-project (with solution):**

**Your task:** Flatten a nested list (lists inside lists) into a single flat list.

**Solution:**
```python
def flatten(value):
    if isinstance(value, list):
        result = []
        for item in value:
            result.extend(flatten(item))   # dig into nested lists
        return result
    return [value]                          # a plain value becomes a 1-item list

print(flatten([1, [2, [3, 4]], 5]))
```
**Output:**
```
[1, 2, 3, 4, 5]
```
**Explanation:** `isinstance(value, list)` decides whether to dig deeper (it's a list) or treat the value as a single item. The function calls itself on nested lists until everything is flattened into one level.

---

## `issubclass()`

**What it does (plain English):** Checks whether one **class** is built on top of (inherits from) another class. It's like `isinstance`, but for classes themselves rather than objects. (An object-oriented topic — skim if classes are new.)

**Syntax:** `issubclass(class, parent_class)`

**Parameters:**
- `class` — the class to check (a class, not an object).
- `parent_class` — the class (or tuple of classes) to check against.

**What you get back:** `True` or `False`.

**Examples (with solutions):**

Example 1 — bool is built on int
```python
print(issubclass(bool, int))
```
**Output:**
```
True
```
**What happened:** Booleans are a special kind of integer, so `bool` is a subclass of `int`.

Example 2 — everything is built on object
```python
print(issubclass(str, object))
```
**Output:**
```
True
```
**What happened:** In Python, all classes ultimately inherit from `object`.

Example 3 — unrelated classes
```python
print(issubclass(str, int))
```
**Output:**
```
False
```
**What happened:** `str` is not based on `int`, so `False`.

Example 4 — your own class hierarchy
```python
class Animal: pass
class Dog(Animal): pass

print(issubclass(Dog, Animal))
```
**Output:**
```
True
```
**What happened:** `Dog` is defined as `Dog(Animal)`, so it's a subclass of `Animal`.

Example 5 — passing an object errors
```python
class Animal: pass
try:
    issubclass(Animal(), Animal)   # an OBJECT, not a class
except TypeError as e:
    print("error: needs a class, not an object")
```
**Output:**
```
error: needs a class, not an object
```
**What happened:** `issubclass` needs classes. For objects, use `isinstance` instead.

**Common mistakes (and the fix):**
- ❌ Passing an object instead of a class → `TypeError`.
  ✅ Use `isinstance` for objects, `issubclass` for classes.

**Real-world use case (with full solution):**

**The problem:** You have a plugin system, and every plugin must be built on a common `BasePlugin` class. You want to reject anything that isn't before registering it.

**The solution:**
```python
class BasePlugin: pass
class S3Plugin(BasePlugin): pass
class RandomClass: pass

def register(plugin_class, registry):
    if not issubclass(plugin_class, BasePlugin):
        return f"rejected: {plugin_class.__name__} is not a BasePlugin"
    registry[plugin_class.__name__] = plugin_class
    return f"registered {plugin_class.__name__}"

registry = {}
print(register(S3Plugin, registry))
print(register(RandomClass, registry))
```
**How it works, step by step:**
1. `issubclass(plugin_class, BasePlugin)` checks the plugin is built on the right base.
2. Valid plugins get added to the registry.
3. Invalid ones are rejected with a clear message.

**Output:**
```
registered S3Plugin
rejected: RandomClass is not a BasePlugin
```

**Mini-project (with solution):**

**Your task:** Sort exception types into "retryable" vs "fatal" based on whether they inherit from a `Transient` base.

**Solution:**
```python
class Transient(Exception): pass
class Timeout(Transient): pass
class Fatal(Exception): pass

def is_retryable(exception_type):
    return issubclass(exception_type, Transient)

print("Timeout retryable?", is_retryable(Timeout))
print("Fatal retryable?", is_retryable(Fatal))
```
**Output:**
```
Timeout retryable? True
Fatal retryable? False
```
**Explanation:** `Timeout` is built on `Transient`, so it's considered retryable. `Fatal` is not, so your retry logic would give up on it. This lets you handle whole families of errors with one check.

---

## `iter()`

**What it does (plain English):** Turns something you can loop over into an "iterator" — an object that hands out items one at a time when you ask (using `next()`). It has a clever second form for reading data in chunks until a stop signal.

**Syntax:** `iter(iterable)` or `iter(callable, stop_value)`

**Parameters:**
- `iterable` — a list/sequence to step through; **or**
- `callable, stop_value` — call the function repeatedly until it returns `stop_value`.

**What you get back:** An iterator (use `next()` to pull items).

**Examples (with solutions):**

Example 1 — step through a list one item at a time
```python
it = iter([1, 2, 3])
print(next(it))
print(next(it))
```
**Output:**
```
1
2
```
**What happened:** `iter` made an iterator; each `next()` pulls the following item.

Example 2 — loop over an iterator
```python
it = iter("ab")
for char in it:
    print(char)
```
**Output:**
```
a
b
```
**What happened:** A `for` loop pulls items from the iterator until it's empty.

Example 3 — iterators get used up
```python
it = iter([10, 20])
print(list(it))    # consume everything
print(list(it))    # nothing left
```
**Output:**
```
[10, 20]
[]
```
**What happened:** Once an iterator is exhausted, it's empty — you'd need a fresh one to loop again.

Example 4 — provide a default when empty
```python
it = iter([1])
print(next(it))           # 1
print(next(it, "done"))   # empty now -> default
```
**Output:**
```
1
done
```
**What happened:** `next(it, "done")` returns the default instead of crashing when empty.

Example 5 — the two-argument chunk form
```python
import io
stream = io.BytesIO(b"abcdefgh")

chunks = []
for chunk in iter(lambda: stream.read(3), b""):
    chunks.append(chunk)
print(chunks)
```
**Output:**
```
[b'abc', b'def', b'gh']
```
**What happened:** `iter(function, stop)` calls `stream.read(3)` over and over until it returns the stop value `b""` (end of data), giving you 3-byte chunks.

**Common mistakes (and the fix):**
- ❌ Expecting to loop an iterator twice — it's single-use.
  ✅ Re-create it with `iter(...)` (or loop the original list).

**Real-world use case (with full solution):**

**The problem:** You need to process a large file or stream without loading it all into memory at once — read it in fixed-size chunks instead.

**The solution:**
```python
import io

def process_stream(read_function, chunk_size=4096):
    total_bytes = 0
    for chunk in iter(lambda: read_function(chunk_size), b""):
        total_bytes += len(chunk)        # here we just count; you could hash/scan
    return total_bytes

stream = io.BytesIO(b"x" * 10000)        # pretend large stream
print(process_stream(stream.read))
```
**How it works, step by step:**
1. `iter(lambda: read_function(chunk_size), b"")` keeps calling the reader.
2. Each call returns the next chunk; the loop ends when it returns the empty `b""`.
3. Memory stays low because we only hold one chunk at a time.

**Output:**
```
10000
```

**Mini-project (with solution):**

**Your task:** Drain a work queue until you hit a special "stop" marker (a poison pill).

**Solution:**
```python
import queue

work = queue.Queue()
for item in ["task-a", "task-b", "task-c", None]:   # None = stop marker
    work.put(item)

processed = list(iter(work.get, None))    # pull items until we get None
print(processed)
```
**Output:**
```
['task-a', 'task-b', 'task-c']
```
**Explanation:** `iter(work.get, None)` repeatedly calls `work.get` to pull tasks, stopping the moment it pulls the `None` marker. This is a clean way to consume a queue until a sentinel tells you to stop.

---

## `len()` 🔧

**What it does (plain English):** Tells you how many items are inside something — letters in a string, items in a list, keys in a dictionary.

**Syntax:** `len(thing)`

**Parameters:**
- `thing` — a string, list, tuple, dictionary, set, or range.

**What you get back:** A whole number (the count). Never negative.

**Examples (with solutions):**

Example 1 — count letters in a word
```python
print(len("hello"))
```
**Output:**
```
5
```
**What happened:** `len` counted the 5 characters in `"hello"`.

Example 2 — count items in a list
```python
servers = ["web-1", "web-2", "web-3"]
print(len(servers))
```
**Output:**
```
3
```
**What happened:** There are 3 items in the list, so `len` returns `3`.

Example 3 — count keys in a dictionary
```python
tags = {"env": "prod", "team": "sre"}
print(len(tags))
```
**Output:**
```
2
```
**What happened:** A dictionary's length is its number of keys (`env` and `team`).

Example 4 — works on a range too
```python
print(len(range(10)))
```
**Output:**
```
10
```
**What happened:** `range(10)` represents the numbers 0–9, which is 10 numbers.

Example 5 — empty things have length 0
```python
print(len([]))
print(len(""))
```
**Output:**
```
0
0
```
**What happened:** An empty list and an empty string both contain nothing, so their length is `0`.

**Common mistakes (and the fix):**
- ❌ Trying `len(42)` on a plain number → error (numbers aren't containers).
  ✅ Only use `len` on collections (strings, lists, dicts, sets, tuples, ranges).
- ❌ Writing `if len(items) == 0:` to check for "empty."
  ✅ Use the shorter, clearer `if not items:` — an empty list/string is already "falsy."

**Real-world use case (with full solution):**

**The problem:** After calling an AWS API to list instances, you expect a specific number back. If the count is wrong, you want to stop early instead of acting on bad data.

**The solution:**
```python
def assert_count(items, expected, what="resources"):
    if len(items) != expected:
        raise AssertionError(f"expected {expected} {what}, got {len(items)}")
    print(f"OK: found {len(items)} {what}")

assert_count(["i-1", "i-2"], 2)        # correct count -> OK
```
**How it works, step by step:**
1. `len(items)` counts what the API actually returned.
2. We compare it to the number we expected.
3. If they don't match, we raise an error and stop; otherwise we print an OK message.

**Output:**
```
OK: found 2 resources
```

**Mini-project (with solution):**

**Your task:** Write a "capacity guard" that refuses to launch new servers if doing so would push the fleet over a maximum size.

**Solution:**
```python
def can_launch(current_servers, requested, cap):
    if len(current_servers) + requested > cap:
        return f"DENIED: would exceed cap of {cap}"
    return "OK to launch"

print(can_launch(["i-1", "i-2"], 3, cap=4))
print(can_launch(["i-1"], 2, cap=4))
```
**Output:**
```
DENIED: would exceed cap of 4
OK to launch
```
**Explanation:** `len(current_servers)` is how many you already have. Add the number you want to launch; if the total exceeds the cap, deny it. The first call (2 + 3 = 5 > 4) is denied; the second (1 + 2 = 3 ≤ 4) is allowed.

---

## `list()` 🔧

**What it does (plain English):** Makes a list. Often used to "unpack" lazy things (like `range`, `map`, or `filter`) into a real list you can see and index.

**Syntax:** `list()` or `list(iterable)`

**Parameters:**
- `iterable` — optional; anything you can loop over (string, range, another list, etc.).

**What you get back:** A new list.

**Examples (with solutions):**

Example 1 — an empty list to start with
```python
print(list())
```
**Output:**
```
[]
```
**What happened:** With no input, `list()` gives you an empty list, ready to fill.

Example 2 — turn a string into a list of characters
```python
print(list("abc"))
```
**Output:**
```
['a', 'b', 'c']
```
**What happened:** Looping over `"abc"` gives each character, and `list` collects them.

Example 3 — turn a range into a visible list
```python
print(list(range(5)))
```
**Output:**
```
[0, 1, 2, 3, 4]
```
**What happened:** `range(5)` is lazy (it doesn't show its numbers). `list()` forces them out.

Example 4 — listing a dictionary gives its KEYS
```python
tags = {"env": "prod", "team": "sre"}
print(list(tags))
```
**Output:**
```
['env', 'team']
```
**What happened:** When you `list()` a dictionary, you get its keys (not the values).

Example 5 — copy a list (so changes don't affect the original)
```python
original = [1, 2, 3]
copy = list(original)
copy.append(4)
print(original)
print(copy)
```
**Output:**
```
[1, 2, 3]
[1, 2, 3, 4]
```
**What happened:** `list(original)` made a separate copy, so appending to `copy` left `original` untouched.

**Common mistakes (and the fix):**
- ❌ Expecting `list(my_dict)` to give the values. It gives the keys.
  ✅ Use `list(my_dict.values())` for values, or `list(my_dict.items())` for key-value pairs.
- ❌ Wrapping things in `list()` that you only loop over once (wastes memory).
  ✅ If you're just looping, you can loop the range/map directly without `list()`.

**Real-world use case (with full solution):**

**The problem:** A cloud API returns results in "pages." You want all the items gathered into one flat list you can work with.

**The solution:**
```python
def collect_all(pages, key):
    everything = []
    for page in pages:
        everything.extend(page.get(key, []))   # add this page's items
    return everything

pages = [{"Instances": ["i-1"]}, {"Instances": ["i-2", "i-3"]}]
print(collect_all(pages, "Instances"))
```
**How it works, step by step:**
1. Start with an empty list called `everything`.
2. For each page, pull out its list of items and `extend` (add them all) into `everything`.
3. Return the combined list once all pages are processed.

**Output:**
```
['i-1', 'i-2', 'i-3']
```

**Mini-project (with solution):**

**Your task:** Split a long list of items into smaller "batches" of a fixed size (useful for bulk API calls that accept only N items at a time).

**Solution:**
```python
def make_batches(items, size):
    batches = []
    for start in range(0, len(items), size):
        batches.append(items[start:start + size])
    return batches

print(make_batches([1, 2, 3, 4, 5, 6, 7], 3))
```
**Output:**
```
[[1, 2, 3], [4, 5, 6], [7]]
```
**Explanation:** `range(0, len(items), size)` gives starting positions 0, 3, 6. For each one, `items[start:start+size]` slices out up to `size` items. The last batch has just `[7]` because that's all that's left.

---

## `locals()`

**What it does (plain English):** Hands you a dictionary of the variables that currently exist inside your function (their names and values). Handy for debugging "what was set at this point?"

**Syntax:** `locals()`

**Parameters:** None.

**What you get back:** A dictionary of `{variable_name: value}` for the local scope.

**Examples (with solutions):**

Example 1 — see a function's local variables
```python
def show():
    a = 1
    b = 2
    return locals()

print(show())
```
**Output:**
```
{'a': 1, 'b': 2}
```
**What happened:** Inside `show`, two variables existed (`a` and `b`); `locals()` returned them as a dictionary.

Example 2 — just the variable names
```python
def names(x):
    y = x * 2
    return list(locals())

print(names(5))
```
**Output:**
```
['x', 'y']
```
**What happened:** `list(locals())` gives just the keys — the names of the variables in scope (`x` the parameter, `y` the new one).

Example 3 — it updates as you add variables
```python
def grow():
    snapshot = []
    a = 1
    snapshot.append(len(locals()))   # a + snapshot exist
    b = 2
    snapshot.append(len(locals()))   # now b too
    return snapshot

print(grow())
```
**Output:**
```
[2, 3]
```
**What happened:** Each call to `locals()` reflects the variables that exist at that moment, so the count grows.

Example 4 — use locals to fill a message
```python
def summary(service, status):
    return "{service} is {status}".format(**locals())

print(summary("api", "healthy"))
```
**Output:**
```
api is healthy
```
**What happened:** `**locals()` feeds the variables `service` and `status` straight into the `.format()` placeholders.

Example 5 — at the top level, locals is the global scope
```python
region = "us-east-1"
print("region" in locals())
```
**Output:**
```
True
```
**What happened:** Outside any function, `locals()` is the same as the module's globals, so `region` is in there.

**Common mistakes (and the fix):**
- ❌ Trying to *create* variables by writing into `locals()` inside a function (e.g. `locals()["x"] = 5`). Python ignores it.
  ✅ Just assign normally: `x = 5`.
- ❌ Confusing `locals()` (inside a function) with `globals()` (module-wide).
  ✅ Remember: locals = "in here, right now"; globals = "the whole file."

**Real-world use case (with full solution):**

**The problem:** A provisioning function failed, and you want your error log to include all the inputs that were in scope, without writing each one out by hand.

**The solution:**
```python
import logging
logging.basicConfig(level=logging.ERROR)

def provision(region, ami, count):
    try:
        raise RuntimeError("API rejected request")
    except Exception:
        context = {k: v for k, v in locals().items() if k != "self"}
        logging.error("provision failed with context=%s", context)

provision("us-east-1", "ami-123", 3)
```
**How it works, step by step:**
1. Inside the `except` block, `locals()` holds every local variable (`region`, `ami`, `count`).
2. We copy them into a `context` dictionary (skipping `self` if present).
3. We log that context, so the error message shows exactly what the function was working with.

**Output:**
```
ERROR:root:provision failed with context={'region': 'us-east-1', 'ami': 'ami-123', 'count': 3}
```

**Mini-project (with solution):**

**Your task:** Write a function that builds a status message using its local variables, without repeating their names.

**Solution:**
```python
def status_line(service, region, healthy):
    state = "UP" if healthy else "DOWN"
    return "{service} in {region}: {state}".format(**locals())

print(status_line("web", "eu-west-1", True))
print(status_line("db", "us-east-1", False))
```
**Output:**
```
web in eu-west-1: UP
db in us-east-1: DOWN
```
**Explanation:** We compute `state` from `healthy`, then `**locals()` passes `service`, `region`, and `state` into the template automatically — no need to write `service=service, region=region, ...`.

---

## `map()` 🔧

**What it does (plain English):** Applies the same function to every item in a list (or other iterable) and gives back the results, one per item. A clean way to "transform everything."

**Syntax:** `map(function, iterable)`

**Parameters:**
- `function` — what to do to each item (a function or `lambda`).
- `iterable` — the items to transform. (You can pass more than one iterable.)

**What you get back:** A lazy `map` object — wrap it in `list()` to see the results.

**Examples (with solutions):**

Example 1 — turn numbers into text
```python
numbers = [1, 2, 3]
print(list(map(str, numbers)))
```
**Output:**
```
['1', '2', '3']
```
**What happened:** `map` ran `str()` on each number, turning `1` into `"1"`, and so on.

Example 2 — uppercase every word
```python
words = ["web", "db"]
print(list(map(str.upper, words)))
```
**Output:**
```
['WEB', 'DB']
```
**What happened:** `str.upper` was applied to each word, capitalizing them.

Example 3 — your own transformation with lambda
```python
prices = [10, 20, 30]
with_tax = list(map(lambda p: p * 1.1, prices))
print(with_tax)
```
**Output:**
```
[11.0, 22.0, 33.0]
```
**What happened:** The `lambda` multiplies each price by 1.1; `map` applies it to all of them.

Example 4 — convert a string of digits to numbers
```python
print(list(map(int, "123")))
```
**Output:**
```
[1, 2, 3]
```
**What happened:** Looping `"123"` gives `'1'`, `'2'`, `'3'`; `int` turns each into a number.

Example 5 — combine two lists item-by-item
```python
a = [1, 2, 3]
b = [10, 20, 30]
print(list(map(lambda x, y: x + y, a, b)))
```
**Output:**
```
[11, 22, 33]
```
**What happened:** With two lists, `map` pairs them up (1&10, 2&20, 3&30) and adds each pair.

**Common mistakes (and the fix):**
- ❌ Forgetting `list()` and printing `map(...)` directly → you see something like `<map object at 0x...>`.
  ✅ Wrap it: `list(map(...))` (or loop over it).
- ❌ Reaching for `map(lambda x: ..., data)` when a list comprehension reads more clearly.
  ✅ For custom logic, `[do(x) for x in data]` is often friendlier. Use `map` mainly with existing named functions like `str` or `int`.

**Real-world use case (with full solution):**

**The problem:** Port numbers arrive as messy text — some with extra spaces, some already numbers. You need them all as clean integers.

**The solution:**
```python
def clean_ports(raw_ports):
    return list(map(lambda p: int(str(p).strip()), raw_ports))

print(clean_ports([" 80 ", "443", 8080]))
```
**How it works, step by step:**
1. For each value, `str(p)` makes sure it's text, `.strip()` removes spaces.
2. `int(...)` converts that clean text into a number.
3. `map` applies this to every item, and `list()` collects the results.

**Output:**
```
[80, 443, 8080]
```

**Mini-project (with solution):**

**Your task:** Pair each server ID with its status to make readable lines like `"i-1: running"`.

**Solution:**
```python
def status_lines(ids, states):
    return list(map(lambda server_id, state: f"{server_id}: {state}", ids, states))

print(status_lines(["i-1", "i-2"], ["running", "stopped"]))
```
**Output:**
```
['i-1: running', 'i-2: stopped']
```
**Explanation:** Because we gave `map` two lists, the `lambda` receives one item from each at the same position, letting us format them together into a single string.

---

## `max()` 🔧

**What it does (plain English):** Finds the biggest value. Either the biggest item in a list, or the biggest of several values you pass directly.

**Syntax:** `max(iterable)` or `max(a, b, c, ...)` — optionally with `key=` and `default=`.

**Parameters:**
- `iterable` (or several direct values) — what to compare.
- `key` — optional function deciding *how* to compare (e.g. by a field).
- `default` — optional value to return if the list is empty (avoids an error).

**What you get back:** The largest item.

**Examples (with solutions):**

Example 1 — biggest number in a list
```python
print(max([3, 1, 4, 1, 5]))
```
**Output:**
```
5
```
**What happened:** `max` scanned the list and returned the largest value, `5`.

Example 2 — biggest of several values
```python
print(max(10, 25, 7))
```
**Output:**
```
25
```
**What happened:** You can pass values directly instead of a list; `max` still finds the biggest.

Example 3 — longest word using key
```python
words = ["a", "bbbb", "cc"]
print(max(words, key=len))
```
**Output:**
```
bbbb
```
**What happened:** `key=len` tells `max` to compare by length, so it returns the longest word.

Example 4 — biggest by a dictionary field
```python
servers = [{"name": "a", "cpu": 30}, {"name": "b", "cpu": 90}]
busiest = max(servers, key=lambda s: s["cpu"])
print(busiest["name"])
```
**Output:**
```
b
```
**What happened:** `key=lambda s: s["cpu"]` compares by the `cpu` value, so the server with cpu 90 wins.

Example 5 — empty list without crashing
```python
print(max([], default=0))
```
**Output:**
```
0
```
**What happened:** Normally `max([])` errors, but `default=0` tells it to return `0` when there's nothing to compare.

**Common mistakes (and the fix):**
- ❌ Calling `max([])` on an empty list → `ValueError` crash.
  ✅ Pass `default=`, e.g. `max(items, default=None)`.
- ❌ Forgetting `key=` and trying to `max()` a list of dictionaries → it can't compare them.
  ✅ Tell it what to compare: `max(items, key=lambda d: d["field"])`.

**Real-world use case (with full solution):**

**The problem:** You have several machine images (AMIs) and want the **newest** one, based on its creation date.

**The solution:**
```python
def newest_image(images):
    return max(images, key=lambda img: img["CreationDate"], default=None)

amis = [
    {"Id": "ami-old", "CreationDate": "2024-01-01"},
    {"Id": "ami-new", "CreationDate": "2024-06-01"},
]
result = newest_image(amis)
print(result["Id"])
```
**How it works, step by step:**
1. `key=lambda img: img["CreationDate"]` compares images by their date text.
2. Dates in `YYYY-MM-DD` form compare correctly as text (later dates are "bigger").
3. `max` returns the image with the latest date; `default=None` guards against an empty list.

**Output:**
```
ami-new
```

**Mini-project (with solution):**

**Your task:** From a window of metric samples, report the peak value and when it happened.

**Solution:**
```python
def peak(samples):                       # samples: list of (time, value)
    return max(samples, key=lambda s: s[1], default=None)

readings = [("t1", 40), ("t2", 95), ("t3", 60)]
print(peak(readings))
```
**Output:**
```
('t2', 95)
```
**Explanation:** Each sample is a `(time, value)` pair. `key=lambda s: s[1]` compares by the value (the second item), so `max` returns the whole pair with the highest reading — telling you both the peak and its timestamp.

---

## `memoryview()`

**What it does (plain English):** Lets you look at and slice the bytes of binary data **without copying** it. Useful when data is large and you don't want to duplicate it in memory. (An advanced tool — you'll meet it rarely as a beginner.)

**Syntax:** `memoryview(bytes_like_object)`

**Parameters:**
- `bytes_like_object` — binary data such as `bytes` or `bytearray`.

**What you get back:** A `memoryview` object you can index and slice.

**Examples (with solutions):**

Example 1 — make a memoryview
```python
data = b"abcdef"
view = memoryview(data)
print(len(view))
```
**Output:**
```
6
```
**What happened:** `view` looks at the same 6 bytes as `data`, without copying them.

Example 2 — indexing gives a number, not a character
```python
view = memoryview(b"abc")
print(view[0])
```
**Output:**
```
97
```
**What happened:** Byte values are numbers; `97` is the code for the letter `a`.

Example 3 — slice a piece back into bytes
```python
view = memoryview(b"abcdef")
print(bytes(view[1:4]))
```
**Output:**
```
b'bcd'
```
**What happened:** Slicing the view picks bytes 1–3; wrapping in `bytes()` turns them back into readable bytes.

Example 4 — edit underlying data through the view
```python
data = bytearray(b"hello")
view = memoryview(data)
view[0] = 72            # 72 is the code for 'H'
print(data)
```
**Output:**
```
bytearray(b'Hello')
```
**What happened:** Because `bytearray` is changeable, editing the view changed the original data in place.

Example 5 — only the header is copied
```python
big = b"HEADER" + b"x" * 1000
view = memoryview(big)
header = bytes(view[:6])
print(header)
```
**Output:**
```
b'HEADER'
```
**What happened:** We copied just the 6-byte header out of a large buffer, leaving the rest untouched in memory.

**Common mistakes (and the fix):**
- ❌ Expecting `view[0]` to be a character like `'a'`. It's the byte's number (`97`).
  ✅ Slice and convert: `bytes(view[0:1])` gives `b'a'`.
- ❌ Trying to edit a view of plain `bytes` (which can't change).
  ✅ Use a `bytearray` if you need to modify the underlying data.

**Real-world use case (with full solution):**

**The problem:** You downloaded a large file's bytes and only need to read its small header. Copying the whole thing just to peek wastes memory.

**The solution:**
```python
def read_header(buffer, header_size=16):
    view = memoryview(buffer)
    return bytes(view[:header_size])   # copy ONLY the header

payload = b"MAGIC-HEADER----" + b"data" * 100000
print(read_header(payload))
```
**How it works, step by step:**
1. `memoryview(buffer)` wraps the big buffer without copying it.
2. `view[:header_size]` selects just the first 16 bytes.
3. `bytes(...)` copies only those 16 bytes out — the megabytes of `data` are never duplicated.

**Output:**
```
b'MAGIC-HEADER----'
```

**Mini-project (with solution):**

**Your task:** Patch (overwrite) part of a large buffer in place — for example, replacing a version string — without rebuilding the whole buffer.

**Solution:**
```python
def patch(buffer, offset, new_data):
    view = memoryview(buffer)
    view[offset:offset + len(new_data)] = new_data
    return buffer

config = bytearray(b"version=0.0.0")
patch(config, 8, b"1.2.3")
print(config)
```
**Output:**
```
bytearray(b'version=1.2.3')
```
**Explanation:** The view points at the same memory as `config`. Assigning into `view[8:13]` overwrites those bytes directly, swapping `0.0.0` for `1.2.3` without creating a new buffer.

---

## `min()` 🔧

**What it does (plain English):** Finds the smallest value — the opposite of `max()`. Works the same way, including `key=` and `default=`.

**Syntax:** `min(iterable)` or `min(a, b, c, ...)` — optionally with `key=` and `default=`.

**Parameters:**
- `iterable` (or several direct values) — what to compare.
- `key` — optional function deciding how to compare.
- `default` — optional value returned if the list is empty.

**What you get back:** The smallest item.

**Examples (with solutions):**

Example 1 — smallest number in a list
```python
print(min([3, 1, 4]))
```
**Output:**
```
1
```
**What happened:** `min` returned the lowest value in the list.

Example 2 — smallest of several values
```python
print(min(9, 4, 7))
```
**Output:**
```
4
```
**What happened:** Passing values directly works too; `4` is the smallest.

Example 3 — youngest by a field
```python
people = [{"name": "a", "age": 30}, {"name": "b", "age": 22}]
youngest = min(people, key=lambda p: p["age"])
print(youngest["name"])
```
**Output:**
```
b
```
**What happened:** `key=lambda p: p["age"]` compares by age, so the person aged 22 is chosen.

Example 4 — empty list without crashing
```python
print(min([], default="none"))
```
**Output:**
```
none
```
**What happened:** With nothing to compare, `default="none"` is returned instead of an error.

Example 5 — alphabetically first word
```python
print(min(["banana", "apple", "cherry"]))
```
**Output:**
```
apple
```
**What happened:** For strings, "smallest" means earliest alphabetically, so `apple` wins.

**Common mistakes (and the fix):**
- ❌ `min([])` on an empty list → crash.
  ✅ Add `default=`, e.g. `min(items, default=None)`.
- ❌ Mixing types like `min([1, "a"])` → error (can't compare a number to text).
  ✅ Compare items of the same type, or use a `key` that maps them to comparable values.

**Real-world use case (with full solution):**

**The problem:** You're shopping for the cheapest AWS region to run a workload and have a price for each.

**The solution:**
```python
def cheapest_region(prices):
    return min(prices.items(), key=lambda pair: pair[1])

prices = {"us-east-1": 0.012, "eu-west-1": 0.015, "ap-south-1": 0.009}
region, price = cheapest_region(prices)
print(f"{region} at ${price}")
```
**How it works, step by step:**
1. `prices.items()` gives `(region, price)` pairs.
2. `key=lambda pair: pair[1]` compares by the price (the second element).
3. `min` returns the pair with the lowest price, which we unpack into `region` and `price`.

**Output:**
```
ap-south-1 at $0.009
```

**Mini-project (with solution):**

**Your task:** Find the oldest snapshot (the one to clean up first), based on its creation date.

**Solution:**
```python
def oldest_snapshot(snapshots):
    return min(snapshots, key=lambda s: s["created"], default=None)

snaps = [
    {"id": "snap-1", "created": "2024-06-01"},
    {"id": "snap-2", "created": "2024-01-01"},
]
print(oldest_snapshot(snaps)["id"])
```
**Output:**
```
snap-2
```
**Explanation:** Comparing the `created` dates as text, the earliest date (`2024-01-01`) is the "smallest," so `min` returns `snap-2` — the oldest, and the first you'd delete.

---

## `next()`

**What it does (plain English):** Pulls the **next** item out of an iterator (something created by `iter()`, a generator, etc.). With a default, it returns that instead of crashing when there's nothing left.

**Syntax:** `next(iterator)` or `next(iterator, default)`

**Parameters:**
- `iterator` — the thing you're pulling items from.
- `default` — optional value to return when it's empty.

**What you get back:** The next item (or the default).

**Examples (with solutions):**

Example 1 — pull items one at a time
```python
it = iter([1, 2, 3])
print(next(it))
print(next(it))
```
**Output:**
```
1
2
```
**What happened:** Each `next()` hands back the following item from the iterator.

Example 2 — a default avoids crashing when empty
```python
it = iter([1])
print(next(it))            # 1
print(next(it, "done"))    # empty now
```
**Output:**
```
1
done
```
**What happened:** After the only item is used, `next(it, "done")` returns the default instead of erroring.

Example 3 — pull from a generator
```python
squares = (n * n for n in range(3))
print(next(squares))
```
**Output:**
```
0
```
**What happened:** A generator produces values on demand; `next` asks it for the first one (`0*0`).

Example 4 — find the first match and stop
```python
numbers = [1, 3, 5, 8, 9]
first_even = next((n for n in numbers if n % 2 == 0), None)
print(first_even)
```
**Output:**
```
8
```
**What happened:** The generator yields evens; `next` grabs the first one (`8`) without scanning the rest.

Example 5 — empty source returns the default
```python
print(next(iter([]), "empty"))
```
**Output:**
```
empty
```
**What happened:** There's nothing to pull, so the default `"empty"` comes back.

**Common mistakes (and the fix):**
- ❌ Calling `next()` on an exhausted iterator with no default → `StopIteration` crash.
  ✅ Always pass a default when the iterator might be empty: `next(it, None)`.
- ❌ Expecting `next` to "go back" — iterators only move forward.
  ✅ If you need to revisit items, store them in a list first.

**Real-world use case (with full solution):**

**The problem:** Out of a list of instances, you just want the **first running one** — and you don't want to keep scanning after you find it.

**The solution:**
```python
def first_running(instances):
    return next((i for i in instances if i["State"] == "running"), None)

data = [
    {"Id": "i-1", "State": "stopped"},
    {"Id": "i-2", "State": "running"},
    {"Id": "i-3", "State": "running"},
]
found = first_running(data)
print(found["Id"] if found else "none running")
```
**How it works, step by step:**
1. The generator `(i for i in instances if i["State"] == "running")` produces only running instances.
2. `next(..., None)` pulls the very first one and stops immediately.
3. If none are running, the default `None` is returned, which we handle with an `if`.

**Output:**
```
i-2
```

**Mini-project (with solution):**

**Your task:** Build a simple ID generator that hands out `res-1`, `res-2`, `res-3`, … one at a time.

**Solution:**
```python
def id_pool(prefix="res"):
    number = 0
    while True:
        number += 1
        yield f"{prefix}-{number}"

pool = id_pool()
print(next(pool))
print(next(pool))
print(next(pool))
```
**Output:**
```
res-1
res-2
res-3
```
**Explanation:** The generator counts upward forever, yielding a new ID each time. `next(pool)` asks for the next ID on demand — perfect for hand-numbering resources as you create them.

---

## `object()`

**What it does (plain English):** Creates a brand-new, blank object. Its main beginner-friendly use is as a unique "marker" (sentinel) that can't accidentally equal anything else — even `None`.

**Syntax:** `object()`

**Parameters:** None.

**What you get back:** A new, featureless object that is unique every time.

**Examples (with solutions):**

Example 1 — make a blank object
```python
marker = object()
print(type(marker))
```
**Output:**
```
<class 'object'>
```
**What happened:** `object()` created a basic object; it's the simplest thing in Python.

Example 2 — each one is unique
```python
a = object()
b = object()
print(a is b)
```
**Output:**
```
False
```
**What happened:** Every call to `object()` makes a different object, so `a` and `b` are not the same.

Example 3 — everything is an object
```python
print(isinstance("hello", object))
print(isinstance(123, object))
```
**Output:**
```
True
True
```
**What happened:** All Python values are objects, so `isinstance(..., object)` is always `True`.

Example 4 — a unique "missing" marker
```python
MISSING = object()
value = MISSING
print(value is MISSING)
```
**Output:**
```
True
```
**What happened:** We use one specific `object()` as a flag and check identity with `is`.

Example 5 — you can't attach attributes to a plain object
```python
o = object()
try:
    o.name = "x"
except AttributeError as e:
    print("error:", e)
```
**Output:**
```
error: 'object' object has no attribute 'name'
```
**What happened:** A bare `object()` has no storage for attributes, so assigning one fails. (Custom classes can store attributes.)

**Common mistakes (and the fix):**
- ❌ Using `None` to mean "no value given" when `None` might be a real, valid value.
  ✅ Use a private `object()` sentinel so you can tell "not provided" apart from "provided as None."
- ❌ Trying `o.x = 1` on a plain object → error.
  ✅ If you need to store data, make a small class instead.

**Real-world use case (with full solution):**

**The problem:** A function should be able to tell the difference between "the caller didn't pass a value" and "the caller passed `None` on purpose."

**The solution:**
```python
NOT_GIVEN = object()                 # unique private marker

def update_setting(value=NOT_GIVEN):
    if value is NOT_GIVEN:
        return "no change requested"
    return f"set to {value!r}"        # value might legitimately be None

print(update_setting())              # nothing passed
print(update_setting(None))          # None passed on purpose
print(update_setting("prod"))
```
**How it works, step by step:**
1. The default is our unique `NOT_GIVEN` marker, which no caller can accidentally supply.
2. If `value` is still that marker, the caller passed nothing.
3. Otherwise they passed something — even `None` counts as a real choice.

**Output:**
```
no change requested
set to None
set to 'prod'
```

**Mini-project (with solution):**

**Your task:** Build a tiny cache where storing `None` is valid and clearly different from "key not found."

**Solution:**
```python
MISS = object()

class Cache:
    def __init__(self):
        self._store = {}
    def get(self, key):
        value = self._store.get(key, MISS)
        return "MISS" if value is MISS else value
    def set(self, key, value):
        self._store[key] = value

cache = Cache()
cache.set("a", None)
print(cache.get("a"))     # stored None
print(cache.get("b"))     # never stored
```
**Output:**
```
None
MISS
```
**Explanation:** We use the unique `MISS` marker as the "not found" signal. Because a real stored `None` can never equal `MISS`, the cache correctly reports `None` for key `a` and `MISS` for the missing key `b`.

---

## `oct()`

**What it does (plain English):** Converts a whole number into its **octal** (base-8) text form, starting with `0o`. Most useful for Unix file permissions, which are written in octal (like `755`).

**Syntax:** `oct(number)`

**Parameters:**
- `number` — a whole number (integer).

**What you get back:** A string like `'0o755'`.

**Examples (with solutions):**

Example 1 — convert a number to octal
```python
print(oct(8))
```
**Output:**
```
0o10
```
**What happened:** In base-8, the number 8 is written as `10`. The `0o` prefix marks it as octal.

Example 2 — a permission value
```python
print(oct(493))
```
**Output:**
```
0o755
```
**What happened:** The decimal number 493 is `755` in octal — the classic "owner full, others read+execute" permission.

Example 3 — octal literals are already base-8
```python
print(oct(0o644))
```
**Output:**
```
0o644
```
**What happened:** `0o644` is written in octal in the code; `oct()` shows it back in the same form.

Example 4 — get just the digits (no prefix)
```python
print(oct(64)[2:])
```
**Output:**
```
100
```
**What happened:** `oct(64)` is `'0o100'`; slicing `[2:]` drops the `0o` to leave `100`.

Example 5 — round-trip back to a number
```python
text = oct(64)         # '0o100'
print(int(text, 8))    # read it back as base-8
```
**Output:**
```
64
```
**What happened:** `int(text, 8)` parses the octal text back into the original number `64`.

**Common mistakes (and the fix):**
- ❌ Writing a permission as the decimal `755` when you mean octal — they're different numbers!
  ✅ Use the `0o` prefix in code: `0o755`. To display a mode, use `oct(mode)`.
- ❌ Forgetting the `0o` is part of the string when you only want the digits.
  ✅ Slice it off: `oct(x)[2:]`.

**Real-world use case (with full solution):**

**The problem:** You're auditing files on a server and want to print each file's permission in the familiar octal form (e.g. `0o600` for a secret key).

**The solution:**
```python
import stat

def perm_octal(mode_bits):
    # keep only the permission part of the mode, then show it in octal
    return oct(stat.S_IMODE(mode_bits))

# Example: a file created with mode 0o600 (owner read/write only)
print(perm_octal(0o100600))
```
**How it works, step by step:**
1. A file's full "mode" includes type bits plus permission bits.
2. `stat.S_IMODE(...)` keeps only the permission bits.
3. `oct(...)` turns those into readable octal like `0o600`.

**Output:**
```
0o600
```

**Mini-project (with solution):**

**Your task:** Turn human-friendly permission words (`rwx`, `r-x`, `r--`) into the octal number you'd pass to `chmod`.

**Solution:**
```python
def to_octal(owner, group, other):
    value = {"r": 4, "w": 2, "x": 1, "-": 0}
    def triad(letters):
        return sum(value[ch] for ch in letters)
    mode = triad(owner) * 64 + triad(group) * 8 + triad(other)
    return oct(mode)

print(to_octal("rwx", "r-x", "r--"))
```
**Output:**
```
0o754
```
**Explanation:** Each permission letter has a value (r=4, w=2, x=1). We add them per group, then combine the three groups (owner ×64, group ×8, other ×1) into a single number and show it as octal — here `rwx r-x r--` becomes `0o754`.

---

## `open()` 🔧

**What it does (plain English):** Opens a file so you can read from it or write to it. Almost always used with `with`, which automatically closes the file when you're done.

**Syntax:** `open(path, mode="r", encoding=None)`

**Parameters:**
- `path` — the file's name/location.
- `mode` — `"r"` read, `"w"` write (overwrites!), `"a"` append, add `"b"` for binary.
- `encoding` — text encoding; use `"utf-8"` to be safe and consistent.

**What you get back:** A file object (use it inside a `with` block).

**Examples (with solutions):**

Example 1 — write text to a file
```python
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("hello")
print("done writing")
```
**Output:**
```
done writing
```
**What happened:** `"w"` mode created (or overwrote) `demo.txt` and wrote `hello`. The `with` block closed the file automatically.

Example 2 — read the whole file back
```python
with open("demo.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)
```
**Output:**
```
hello
```
**What happened:** `"r"` mode (the default) read the entire file into `content`.

Example 3 — append without erasing
```python
with open("demo.txt", "a", encoding="utf-8") as f:
    f.write(" world")

with open("demo.txt", encoding="utf-8") as f:
    print(f.read())
```
**Output:**
```
hello world
```
**What happened:** `"a"` added to the end instead of overwriting, so the file now reads `hello world`.

Example 4 — read line by line
```python
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("line1\nline2\n")

with open("demo.txt", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```
**Output:**
```
line1
line2
```
**What happened:** Looping a file yields one line at a time; `.strip()` removes the trailing newline.

Example 5 — "w" overwrites everything (be careful!)
```python
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("fresh start")

with open("demo.txt", encoding="utf-8") as f:
    print(f.read())
```
**Output:**
```
fresh start
```
**What happened:** Opening with `"w"` again wiped the previous contents before writing.

**Common mistakes (and the fix):**
- ❌ Forgetting `with`, then never closing the file (leaks resources).
  ✅ Always use `with open(...) as f:` — it closes for you.
- ❌ Using `"w"` when you meant `"a"`, accidentally erasing the file.
  ✅ Use `"a"` to add to a file; reserve `"w"` for "start fresh."
- ❌ Relying on the default encoding (varies by computer).
  ✅ Pass `encoding="utf-8"` so it behaves the same everywhere.

**Real-world use case (with full solution):**

**The problem:** You need to save a generated config file, but you don't want a crash mid-write to leave a half-written, corrupt file behind.

**The solution:**
```python
import json, os, tempfile

def write_atomic(path, text):
    folder = os.path.dirname(path) or "."
    fd, temp_path = tempfile.mkstemp(dir=folder)
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(temp_path, path)        # swap into place in one step

write_atomic("config.json", json.dumps({"replicas": 3}))
with open("config.json", encoding="utf-8") as f:
    print(f.read())
```
**How it works, step by step:**
1. We write to a **temporary** file first.
2. If writing succeeds, `os.replace` swaps it into the real name in a single, safe step.
3. If a crash happened mid-write, the real config file is never touched — no corruption.

**Output:**
```
{"replicas": 3}
```

**Mini-project (with solution):**

**Your task:** Write a simple size-based log rotator: append a line to a log, but if the log grows past a size limit, rename it to `.1` and start fresh.

**Solution:**
```python
import os

def log_line(path, message, max_bytes=50):
    if os.path.exists(path) and os.path.getsize(path) > max_bytes:
        os.replace(path, path + ".1")          # rotate
    with open(path, "a", encoding="utf-8") as f:
        f.write(message + "\n")

for i in range(5):
    log_line("app.log", f"event number {i}")

with open("app.log", encoding="utf-8") as f:
    print("current log:\n" + f.read().strip())
```
**Output:**
```
current log:
event number 4
```
**Explanation:** Each call appends a line. Once the file passes the size limit, it gets renamed to `app.log.1` and a new `app.log` begins — so the current log here only shows the most recent entries (older ones rolled into `app.log.1`).

---

## `ord()`

**What it does (plain English):** Gives you the number (Unicode code point) behind a single character. It's the opposite of `chr()`, which turns a number back into a character.

**Syntax:** `ord(character)`

**Parameters:**
- `character` — a string of exactly one character.

**What you get back:** A whole number (the character's code).

**Examples (with solutions):**

Example 1 — the code for a capital letter
```python
print(ord("A"))
```
**Output:**
```
65
```
**What happened:** The character `A` has Unicode code `65`.

Example 2 — lowercase is different
```python
print(ord("a"))
```
**Output:**
```
97
```
**What happened:** `a` is `97` — lowercase letters have different codes than uppercase.

Example 3 — ord and chr are opposites
```python
print(chr(ord("Z")))
```
**Output:**
```
Z
```
**What happened:** `ord("Z")` gives `90`, and `chr(90)` turns it right back into `Z`.

Example 4 — codes for each character in a word
```python
print([ord(ch) for ch in "Hi"])
```
**Output:**
```
[72, 105]
```
**What happened:** We looped over `"Hi"` and got the code for each letter.

Example 5 — even special characters have codes
```python
print(ord("\n"))
```
**Output:**
```
10
```
**What happened:** The newline character `\n` has code `10`.

**Common mistakes (and the fix):**
- ❌ Passing more than one character, like `ord("ab")` → error.
  ✅ `ord` takes exactly one character; loop if you need codes for many.
- ❌ Mixing up `ord` and `chr`. 
  ✅ Remember: `ord` = character → number; `chr` = number → character.

**Real-world use case (with full solution):**

**The problem:** You want a quick, lightweight numeric "fingerprint" of a short string (for example, to spread cache keys around) without pulling in a hashing library.

**The solution:**
```python
def simple_checksum(text):
    return sum(ord(ch) for ch in text) % 1000

print(simple_checksum("deploy-v2"))
print(simple_checksum("deploy-v3"))
```
**How it works, step by step:**
1. `ord(ch)` turns each character into its number.
2. `sum(...)` adds all those numbers together.
3. `% 1000` keeps the result in a small range (0–999), giving a compact fingerprint.

**Output:**
```
3
4
```

**Mini-project (with solution):**

**Your task:** Check whether a character is an uppercase ASCII letter (A–Z) using its code number.

**Solution:**
```python
def is_upper_letter(ch):
    return ord("A") <= ord(ch) <= ord("Z")

print(is_upper_letter("M"))
print(is_upper_letter("m"))
print(is_upper_letter("5"))
```
**Output:**
```
True
False
False
```
**Explanation:** Uppercase letters have codes from `ord("A")` (65) to `ord("Z")` (90). We check whether the character's code falls in that range. `M` does; lowercase `m` (109) and the digit `5` (53) do not.

---

## `pow()`

**What it does (plain English):** Raises a number to a power — `pow(2, 3)` means 2 to the power of 3. It does the same thing as the `**` operator.

**Syntax:** `pow(base, exponent)` or `pow(base, exponent, modulus)`

**Parameters:**
- `base` — the number being multiplied.
- `exponent` — how many times.
- `modulus` — optional; if given, returns `(base ** exponent) % modulus` efficiently.

**What you get back:** The resulting number.

**Examples (with solutions):**

Example 1 — basic power
```python
print(pow(2, 3))
```
**Output:**
```
8
```
**What happened:** 2 × 2 × 2 = 8.

Example 2 — same as the ** operator
```python
print(pow(5, 2))
print(5 ** 2)
```
**Output:**
```
25
25
```
**What happened:** `pow(5, 2)` and `5 ** 2` both mean "5 squared."

Example 3 — power of zero is 1
```python
print(pow(10, 0))
```
**Output:**
```
1
```
**What happened:** Any number to the power of 0 is 1.

Example 4 — negative exponent gives a fraction
```python
print(pow(2, -1))
```
**Output:**
```
0.5
```
**What happened:** 2 to the power of -1 means 1 ÷ 2 = 0.5.

Example 5 — the three-argument form (modulus)
```python
print(pow(2, 10, 1000))
```
**Output:**
```
24
```
**What happened:** 2 to the power 10 is 1024; `% 1000` leaves `24`. The 3-arg form does this efficiently.

**Common mistakes (and the fix):**
- ❌ Expecting the 3-argument form to work with decimals — it needs whole numbers.
  ✅ Use whole numbers for `pow(base, exp, mod)`.
- ❌ Confusing `pow(2, 3)` (= 8) with `2 * 3` (= 6).
  ✅ `pow` is repeated multiplication (powers), not a single multiply.

**Real-world use case (with full solution):**

**The problem:** When a network call fails, you want to wait longer before each retry (1s, 2s, 4s, 8s…), but never longer than a sensible cap.

**The solution:**
```python
def backoff_delay(attempt, base=2, cap=60):
    return min(pow(base, attempt), cap)

delays = [backoff_delay(a) for a in range(8)]
print(delays)
```
**How it works, step by step:**
1. `pow(2, attempt)` doubles the wait each time: 1, 2, 4, 8, …
2. `min(..., cap)` makes sure the wait never exceeds 60 seconds.
3. We build a list of delays, one per retry attempt.

**Output:**
```
[1, 2, 4, 8, 16, 32, 60, 60]
```

**Mini-project (with solution):**

**Your task:** Print a small "powers of two" reference table (handy for sizing memory or capacity), from 2⁰ up to 2¹⁰.

**Solution:**
```python
def powers_of_two(up_to=10):
    for exp in range(up_to + 1):
        print(f"2^{exp} = {pow(2, exp)}")

powers_of_two(4)   # keeping it short for the demo
```
**Output:**
```
2^0 = 1
2^1 = 2
2^2 = 4
2^3 = 8
2^4 = 16
```
**Explanation:** For each exponent from 0 to 4, `pow(2, exp)` computes 2 raised to that power, and we print a labeled line. (Call `powers_of_two(10)` for the full table up to 1024.)

---

## `print()` 🔧

**What it does (plain English):** Shows text or values on the screen (standard output). The first function almost everyone learns — and your main way to see what your program is doing.

**Syntax:** `print(*things, sep=" ", end="\n", flush=False)`

**Parameters:**
- `*things` — one or more values to display.
- `sep` — what goes *between* multiple values (default a space).
- `end` — what goes at the *end* (default a newline).
- `flush` — set `True` to force output to appear immediately.

**What you get back:** Nothing (`None`) — it just displays.

**Examples (with solutions):**

Example 1 — print several values
```python
print("a", "b", "c")
```
**Output:**
```
a b c
```
**What happened:** By default, `print` puts a space between the values and a newline at the end.

Example 2 — change the separator
```python
print("2024", "06", "01", sep="-")
```
**Output:**
```
2024-06-01
```
**What happened:** `sep="-"` joined the values with dashes instead of spaces.

Example 3 — stay on the same line
```python
print("Loading", end="")
print("...done")
```
**Output:**
```
Loading...done
```
**What happened:** `end=""` removed the newline after `"Loading"`, so the next print continued on the same line.

Example 4 — print a number and text together
```python
count = 3
print("Provisioned", count, "servers")
```
**Output:**
```
Provisioned 3 servers
```
**What happened:** `print` happily mixes text and numbers, separating them with spaces.

Example 5 — f-strings give you full control
```python
name, cpu = "web-1", 87.5
print(f"{name}: {cpu}% CPU")
```
**Output:**
```
web-1: 87.5% CPU
```
**What happened:** An f-string (`f"..."`) lets you drop variables right into the text with `{}`.

**Common mistakes (and the fix):**
- ❌ Relying on `print` for real application logs (no timestamps, levels, or structure).
  ✅ For real systems, use the `logging` module; keep `print` for quick checks and tools.
- ❌ In containers, logs sometimes appear late or vanish on crash (output is buffered).
  ✅ Use `print(..., flush=True)` or run Python with `-u` / `PYTHONUNBUFFERED=1`.

**Real-world use case (with full solution):**

**The problem:** Your script's *data* should go to standard output (so it can be piped to another command), but *status messages* should go to standard error (so they don't pollute the data).

**The solution:**
```python
import sys

def emit(records):
    for r in records:
        print(r, flush=True)                               # data -> stdout
    print(f"processed {len(records)} records", file=sys.stderr)  # status -> stderr

emit(["i-1", "i-2"])
```
**How it works, step by step:**
1. Each record is printed normally, which goes to standard output (the "data" channel).
2. The summary uses `file=sys.stderr`, sending it to the separate "messages" channel.
3. In a shell, you could now do `script.py > data.txt` and still see the status message.

**Output:**
```
i-1
i-2
processed 2 records
```
*(The first two lines are stdout; the last line is stderr — they just both show here in the console.)*

**Mini-project (with solution):**

**Your task:** Write a tiny structured logger that prints each event as a JSON line (the format log platforms love to ingest).

**Solution:**
```python
import json

def log(level, message, **fields):
    entry = {"level": level, "message": message}
    entry.update(fields)
    print(json.dumps(entry), flush=True)

log("INFO", "deploy started", env="prod", version="1.2.3")
log("ERROR", "disk full", host="web-1")
```
**Output:**
```
{"level": "INFO", "message": "deploy started", "env": "prod", "version": "1.2.3"}
{"level": "ERROR", "message": "disk full", "host": "web-1"}
```
**Explanation:** We build a dictionary from the level, message, and any extra `fields`, then `json.dumps` turns it into a JSON string that `print` writes as one line. `flush=True` makes sure it shows up right away, even inside a container.

---

## `property()`

**What it does (plain English):** Lets a class have a "smart attribute" — something you access like a normal field (`obj.cpu`), but that secretly runs your code to compute it or to check a value before storing it. Usually written with the `@property` decorator.

**Syntax:** `@property` above a method (the getter), plus optional `@name.setter`.

**Parameters:** (when used as a decorator) none directly — you decorate getter/setter methods.

**What you get back:** An attribute that looks normal but runs your logic.

**Examples (with solutions):**

Example 1 — a computed (read-only) attribute
```python
class Disk:
    def __init__(self, used_gb, total_gb):
        self.used_gb = used_gb
        self.total_gb = total_gb

    @property
    def percent_used(self):
        return round(self.used_gb / self.total_gb * 100, 1)

d = Disk(used_gb=75, total_gb=100)
print(d.percent_used)
```
**Output:**
```
75.0
```
**What happened:** `percent_used` looks like a field but is calculated on the fly from the other two values. Note: no parentheses — you access it like `d.percent_used`, not `d.percent_used()`.

Example 2 — validate on assignment with a setter
```python
class Server:
    def __init__(self, cpu):
        self.cpu = cpu                  # this triggers the setter below

    @property
    def cpu(self):
        return self._cpu

    @cpu.setter
    def cpu(self, value):
        if value < 0:
            raise ValueError("cpu must be >= 0")
        self._cpu = value

s = Server(2)
print(s.cpu)
```
**Output:**
```
2
```
**What happened:** Setting `cpu` runs the setter, which checks the value before storing it in `_cpu`.

Example 3 — the setter blocks bad values
```python
s = Server(2)
try:
    s.cpu = -5
except ValueError as e:
    print("rejected:", e)
```
**Output:**
```
rejected: cpu must be >= 0
```
**What happened:** Assigning `-5` triggered the setter's check, which raised an error instead of storing a bad value.

Example 4 — access looks like a plain field
```python
s = Server(4)
s.cpu = 8        # runs the setter
print(s.cpu)     # runs the getter
```
**Output:**
```
8
```
**What happened:** From the outside it feels like a normal attribute, even though getter/setter code runs behind the scenes.

Example 5 — properties can combine other fields
```python
class Endpoint:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    @property
    def url(self):
        return f"https://{self.host}:{self.port}"

e = Endpoint("api.internal", 8443)
print(e.url)
```
**Output:**
```
https://api.internal:8443
```
**What happened:** `url` is built from `host` and `port` whenever you read it.

**Common mistakes (and the fix):**
- ❌ Storing the value under the same name as the property (e.g. property `cpu` saving to `self.cpu`) → infinite loop.
  ✅ Use a different backing name like `self._cpu`.
- ❌ Calling a property like a method: `d.percent_used()`.
  ✅ Access it without parentheses: `d.percent_used`.

**Real-world use case (with full solution):**

**The problem:** Building a cloud SDK client is expensive, and you don't want to create it until it's actually needed — then reuse the same one.

**The solution:**
```python
class AwsService:
    def __init__(self, region):
        self.region = region
        self._client = None

    @property
    def client(self):
        if self._client is None:
            print(f"(creating client for {self.region})")   # happens once
            self._client = {"region": self.region}           # stand-in for boto3.client(...)
        return self._client

svc = AwsService("us-east-1")
print(svc.client)     # first access -> creates it
print(svc.client)     # second access -> reuses it
```
**How it works, step by step:**
1. We start with `_client = None` (not built yet).
2. The first time you read `svc.client`, the getter builds the client and stores it.
3. Every later read finds it already built and returns the same one — so the "creating" message prints only once.

**Output:**
```
(creating client for us-east-1)
{'region': 'us-east-1'}
{'region': 'us-east-1'}
```

**Mini-project (with solution):**

**Your task:** Make a `Scaling` config where `replicas` must stay between 0 and 100; bad values are rejected automatically.

**Solution:**
```python
class Scaling:
    def __init__(self, replicas):
        self.replicas = replicas

    @property
    def replicas(self):
        return self._replicas

    @replicas.setter
    def replicas(self, value):
        if not (0 <= value <= 100):
            raise ValueError("replicas must be between 0 and 100")
        self._replicas = value

cfg = Scaling(3)
cfg.replicas = 10
print(cfg.replicas)

try:
    cfg.replicas = 999
except ValueError as e:
    print("rejected:", e)
```
**Output:**
```
10
rejected: replicas must be between 0 and 100
```
**Explanation:** Every assignment to `replicas` runs the setter, which enforces the 0–100 range. Valid values are stored in `_replicas`; invalid ones raise an error — so the object can never hold a bad value.

---

## `range()` 🔧

**What it does (plain English):** Produces a sequence of numbers, most often to drive a loop a set number of times. It's memory-light: it generates numbers as needed instead of storing them all.

**Syntax:** `range(stop)` or `range(start, stop)` or `range(start, stop, step)`

**Parameters:**
- `start` — first number (default 0).
- `stop` — stops **before** this number (not included).
- `step` — how much to jump each time (default 1; can be negative).

**What you get back:** A `range` object — loop over it, or wrap in `list()` to see the numbers.

**Examples (with solutions):**

Example 1 — count from 0
```python
print(list(range(5)))
```
**Output:**
```
[0, 1, 2, 3, 4]
```
**What happened:** `range(5)` gives 0 up to (but not including) 5.

Example 2 — loop a fixed number of times
```python
for i in range(3):
    print("attempt", i)
```
**Output:**
```
attempt 0
attempt 1
attempt 2
```
**What happened:** The loop ran 3 times, with `i` taking values 0, 1, 2.

Example 3 — choose a start and stop
```python
print(list(range(2, 6)))
```
**Output:**
```
[2, 3, 4, 5]
```
**What happened:** Starting at 2 and stopping before 6 gives 2, 3, 4, 5.

Example 4 — step by 2
```python
print(list(range(0, 10, 2)))
```
**Output:**
```
[0, 2, 4, 6, 8]
```
**What happened:** A step of 2 jumps every other number.

Example 5 — count backwards
```python
print(list(range(5, 0, -1)))
```
**Output:**
```
[5, 4, 3, 2, 1]
```
**What happened:** A negative step counts down (stopping before 0).

**Common mistakes (and the fix):**
- ❌ Expecting `range(1, 5)` to include 5. The stop value is excluded.
  ✅ If you need 1–5 inclusive, use `range(1, 6)`.
- ❌ Printing `range(5)` directly and being confused by `range(0, 5)`.
  ✅ Wrap it in `list()` to *see* the numbers; loop over it to *use* them.

**Real-world use case (with full solution):**

**The problem:** A network operation sometimes fails. You want to retry it a fixed number of times, waiting longer between attempts, and give up after the last try.

**The solution:**
```python
import time

def with_retries(action, attempts=3):
    for attempt in range(attempts):
        try:
            return action()
        except Exception as e:
            print(f"attempt {attempt} failed: {e}")
            if attempt == attempts - 1:
                raise                      # last try -> give up
            time.sleep(0)                  # would be 2 ** attempt in real code

print(with_retries(lambda: "success"))
```
**How it works, step by step:**
1. `range(attempts)` gives us attempt numbers 0, 1, 2.
2. We try the action; if it works, we return the result immediately.
3. On failure, we check if this was the last attempt (`attempts - 1`) and either give up or wait and loop again.

**Output:**
```
success
```

**Mini-project (with solution):**

**Your task:** Generate `(offset, limit)` pairs to page through a large dataset in chunks of a fixed size.

**Solution:**
```python
def pages(total, page_size):
    return [(offset, page_size) for offset in range(0, total, page_size)]

print(pages(25, 10))
```
**Output:**
```
[(0, 10), (10, 10), (20, 10)]
```
**Explanation:** `range(0, 25, 10)` produces the starting offsets 0, 10, 20. We pair each with the page size to get the windows your API would request — the last page (offset 20) simply returns the remaining 5 items.

---

## `repr()`

**What it does (plain English):** Gives a precise, "developer's-eye" text version of a value — one that shows quotes and hidden characters. Great for debugging, because it reveals things a normal `print` hides (like a sneaky trailing space).

**Syntax:** `repr(value)`

**Parameters:**
- `value` — any value.

**What you get back:** A string representation aimed at developers.

**Examples (with solutions):**

Example 1 — repr shows the quotes
```python
print(repr("hello"))
```
**Output:**
```
'hello'
```
**What happened:** Unlike `print("hello")`, `repr` shows the surrounding quotes, making it clear this is a string.

Example 2 — it reveals hidden characters
```python
print(repr("hi\n"))
```
**Output:**
```
'hi\n'
```
**What happened:** The newline shows up as a visible `\n` instead of an actual line break — very useful for spotting hidden characters.

Example 3 — spot a sneaky trailing space
```python
value = "us-east-1 "
print(repr(value))
```
**Output:**
```
'us-east-1 '
```
**What happened:** That trailing space (a common bug source) is now visible inside the quotes.

Example 4 — repr of a list
```python
print(repr([1, "a", True]))
```
**Output:**
```
[1, 'a', True]
```
**What happened:** Each element is shown in its developer form (note the quotes around `'a'`).

Example 5 — the !r shortcut in f-strings
```python
name = "web-1"
print(f"server={name!r}")
```
**Output:**
```
server='web-1'
```
**What happened:** `{name!r}` applies `repr` inside an f-string, showing the quoted form.

**Common mistakes (and the fix):**
- ❌ Expecting `repr` to look "pretty" for end users. It's for developers, not display.
  ✅ Use `str()` (or plain `print`) for user-facing text; use `repr` for debugging.
- ❌ Assuming `print(x)` and `print(repr(x))` look the same. They often differ for strings.
  ✅ When debugging mysterious values, reach for `repr` to see exactly what's there.

**Real-world use case (with full solution):**

**The problem:** A config value "looks right" but a comparison keeps failing. You suspect an invisible character (space, tab, or carriage return) is hiding in it.

**The solution:**
```python
import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

def log_value(name, value):
    logging.debug("%s=%r", name, value)   # %r uses repr

log_value("REGION", "us-east-1\r")         # note the hidden carriage return
```
**How it works, step by step:**
1. `%r` in the log format applies `repr` to the value.
2. `repr` turns invisible characters into visible escapes like `\r`.
3. The log line now clearly shows the stray character that was breaking your comparison.

**Output:**
```
REGION='us-east-1\r'
```

**Mini-project (with solution):**

**Your task:** Give a small class a helpful `__repr__` so it prints usefully in logs and the debugger.

**Solution:**
```python
class Endpoint:
    def __init__(self, host, port):
        self.host = host
        self.port = port
    def __repr__(self):
        return f"Endpoint(host={self.host!r}, port={self.port})"

e = Endpoint("db.internal", 5432)
print(repr(e))
print([e, e])      # repr is also used inside lists
```
**Output:**
```
Endpoint(host='db.internal', port=5432)
[Endpoint(host='db.internal', port=5432), Endpoint(host='db.internal', port=5432)]
```
**Explanation:** Defining `__repr__` controls how your object appears in debugging contexts (and inside lists). A good `repr` shows the key fields, so logs and the debugger tell you exactly what the object holds.

---

## `reversed()`

**What it does (plain English):** Gives you the items of a sequence in reverse order (last to first), as something you can loop over.

**Syntax:** `reversed(sequence)`

**Parameters:**
- `sequence` — a list, tuple, string, or range (something with a known length and order).

**What you get back:** A reverse iterator — wrap in `list()` (or join, for strings) to see it.

**Examples (with solutions):**

Example 1 — reverse a list
```python
print(list(reversed([1, 2, 3])))
```
**Output:**
```
[3, 2, 1]
```
**What happened:** `reversed` walked the list from the end to the start.

Example 2 — reverse a string
```python
print("".join(reversed("abc")))
```
**Output:**
```
cba
```
**What happened:** `reversed` gave the characters back-to-front; `"".join(...)` glued them back into a string.

Example 3 — reverse a range
```python
print(list(reversed(range(4))))
```
**Output:**
```
[3, 2, 1, 0]
```
**What happened:** The numbers 0–3 came back in reverse order.

Example 4 — loop directly over the reverse
```python
for step in reversed(["a", "b", "c"]):
    print(step)
```
**Output:**
```
c
b
a
```
**What happened:** You can loop over `reversed(...)` without converting to a list first.

Example 5 — the original is unchanged
```python
items = [1, 2, 3]
backwards = list(reversed(items))
print(backwards)
print(items)
```
**Output:**
```
[3, 2, 1]
[1, 2, 3]
```
**What happened:** `reversed` doesn't modify the original; it just gives you a reversed view.

**Common mistakes (and the fix):**
- ❌ Trying `reversed(some_set)` — sets have no order, so this errors.
  ✅ Convert to a list first if you have an unordered collection: `reversed(list(my_set))`.
- ❌ Forgetting it returns an iterator (single-use), not a list.
  ✅ Wrap in `list()` if you need to look at it more than once.

**Real-world use case (with full solution):**

**The problem:** A deployment applied several steps in order. Something failed, so now you must **undo** them — and undo has to happen in the reverse order they were applied.

**The solution:**
```python
def rollback(applied_steps):
    for step in reversed(applied_steps):
        print(f"reverting: {step}")

rollback(["create-security-group", "create-instance", "attach-volume"])
```
**How it works, step by step:**
1. The steps were applied first-to-last.
2. `reversed(...)` walks them last-to-first.
3. We undo each one in that reverse order — so the volume detaches before the instance is removed, and so on.

**Output:**
```
reverting: attach-volume
reverting: create-instance
reverting: create-security-group
```

**Mini-project (with solution):**

**Your task:** Build a simple "undo" system: given a history of actions and matching undo-actions, run the undos in reverse.

**Solution:**
```python
def undo_all(history, undo_actions):
    for action in reversed(history):
        undo_actions[action]()

log = []
undo_all(
    ["open-file", "write-data"],
    {
        "open-file": lambda: log.append("closed file"),
        "write-data": lambda: log.append("erased data"),
    },
)
print(log)
```
**Output:**
```
['erased data', 'closed file']
```
**Explanation:** Actions happened as open → write. To undo safely we reverse that, so we erase the data first, then close the file. `reversed(history)` gives us that order, and we call each matching undo function.

---

## `round()`

**What it does (plain English):** Rounds a number to a chosen number of decimal places (or to a whole number if you don't say). Good for tidying up display values.

**Syntax:** `round(number)` or `round(number, decimal_places)`

**Parameters:**
- `number` — the value to round.
- `decimal_places` — optional; how many digits after the dot to keep.

**What you get back:** The rounded number.

**Examples (with solutions):**

Example 1 — round to a whole number
```python
print(round(3.7))
```
**Output:**
```
4
```
**What happened:** With no decimal places given, `round` returns the nearest whole number.

Example 2 — round to 2 decimal places
```python
print(round(3.14159, 2))
```
**Output:**
```
3.14
```
**What happened:** Keeping 2 decimals gives `3.14`.

Example 3 — the "round half to even" surprise
```python
print(round(2.5))
print(round(3.5))
```
**Output:**
```
2
4
```
**What happened:** Python rounds exact halves to the nearest **even** number, so `2.5` → `2` (not 3) and `3.5` → `4`. This surprises many beginners.

Example 4 — round a percentage for display
```python
ratio = 0.6789
print(round(ratio * 100, 1))
```
**Output:**
```
67.9
```
**What happened:** We turned a ratio into a percentage and kept one decimal place.

Example 5 — negative places round to tens/hundreds
```python
print(round(1234, -2))
```
**Output:**
```
1200
```
**What happened:** A negative count rounds to the left of the dot — here, to the nearest hundred.

**Common mistakes (and the fix):**
- ❌ Expecting `round(2.5)` to give 3. Python's "round half to even" gives 2.
  ✅ Know the rule, or use the `decimal` module if you need traditional rounding.
- ❌ Using floats (and `round`) for money — tiny errors creep in (e.g. `round(2.675, 2)` is `2.67`).
  ✅ For currency, use `decimal.Decimal`, which is exact.

**Real-world use case (with full solution):**

**The problem:** You're displaying a billing total to a person. Floating-point math can produce ugly or slightly-wrong values, and money must be exact to the cent.

**The solution:**
```python
from decimal import Decimal, ROUND_HALF_UP

def format_money(amount_text):
    amount = Decimal(amount_text)
    cents = amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return f"${cents}"

print(format_money("12.675"))
print(format_money("8"))
```
**How it works, step by step:**
1. `Decimal(amount_text)` reads the amount exactly (no float errors).
2. `quantize(Decimal("0.01"), ...)` rounds to two decimal places using normal "round half up."
3. We format it with a dollar sign — correct to the cent.

**Output:**
```
$12.68
$8.00
```

**Mini-project (with solution):**

**Your task:** Round a batch of utilization ratios (like `0.123`) into one-decimal percentages for a dashboard.

**Solution:**
```python
def to_percentages(ratios):
    return [round(r * 100, 1) for r in ratios]

print(to_percentages([0.123, 0.999, 0.5]))
```
**Output:**
```
[12.3, 99.9, 50.0]
```
**Explanation:** For each ratio we multiply by 100 to get a percentage, then `round(..., 1)` keeps a single decimal place — clean values ready to show on a dashboard.

---

## `set()` 🔧

**What it does (plain English):** Makes a **set** — a collection of unique items with no duplicates and no fixed order. Sets are brilliant for "what's different between these two groups?" questions.

**Syntax:** `set()` or `set(iterable)`

**Parameters:**
- `iterable` — optional; items to put in the set (duplicates are dropped).

**What you get back:** A set of unique items.

**Examples (with solutions):**

Example 1 — duplicates disappear
```python
print(set([1, 2, 2, 3, 3, 3]))
```
**Output:**
```
{1, 2, 3}
```
**What happened:** A set keeps only one of each value, so the repeats are removed.

Example 2 — unique characters in a word
```python
print(set("banana"))
```
**Output:**
```
{'a', 'b', 'n'}
```
**What happened:** The set has each distinct letter once. (Order may look different — sets aren't ordered.)

Example 3 — items in both sets (intersection)
```python
print({1, 2, 3} & {2, 3, 4})
```
**Output:**
```
{2, 3}
```
**What happened:** The `&` operator keeps only items present in *both* sets.

Example 4 — items in either set (union)
```python
print({1, 2} | {2, 3})
```
**Output:**
```
{1, 2, 3}
```
**What happened:** The `|` operator combines both sets, still without duplicates.

Example 5 — items in the first but not the second (difference)
```python
print({1, 2, 3} - {2})
```
**Output:**
```
{1, 3}
```
**What happened:** The `-` operator removes anything that's in the second set.

**Common mistakes (and the fix):**
- ❌ Writing `{}` to make an empty set — that's actually an empty **dictionary**!
  ✅ Use `set()` for an empty set.
- ❌ Relying on the order of items in a set. There isn't one.
  ✅ If you need order, sort it: `sorted(my_set)`.

**Real-world use case (with full solution):**

**The problem:** You have a list of servers you *want* (declared) and a list that *actually exist*. You need to know which to create and which to delete — the heart of "infrastructure as code."

**The solution:**
```python
def reconcile(declared, actual):
    declared, actual = set(declared), set(actual)
    return {
        "create": sorted(declared - actual),   # wanted but missing
        "delete": sorted(actual - declared),    # exist but not wanted
        "keep":   sorted(declared & actual),    # in both
    }

result = reconcile(["web-1", "web-2", "web-3"], ["web-2", "web-3", "web-9"])
print(result)
```
**How it works, step by step:**
1. `declared - actual` = things you want that don't exist yet → **create**.
2. `actual - declared` = things that exist but you no longer want → **delete**.
3. `declared & actual` = things in both → **keep**. We `sorted(...)` each for tidy, predictable output.

**Output:**
```
{'create': ['web-1'], 'delete': ['web-9'], 'keep': ['web-2', 'web-3']}
```

**Mini-project (with solution):**

**Your task:** Show which IAM permissions were **added** and **removed** between an old policy and a new one.

**Solution:**
```python
def policy_diff(old, new):
    old, new = set(old), set(new)
    return {
        "added":   sorted(new - old),
        "removed": sorted(old - new),
    }

print(policy_diff(
    ["s3:GetObject", "s3:ListBucket"],
    ["s3:GetObject", "s3:PutObject"],
))
```
**Output:**
```
{'added': ['s3:PutObject'], 'removed': ['s3:ListBucket']}
```
**Explanation:** Turning each policy into a set lets us subtract them. `new - old` finds permissions that are new (added); `old - new` finds permissions that disappeared (removed). A clean, instant diff.

---

## `setattr()`

**What it does (plain English):** Sets an attribute on an object **by its name as a string**. It's the dynamic version of writing `obj.name = value` — handy when the attribute name is decided at runtime.

**Syntax:** `setattr(object, name, value)`

**Parameters:**
- `object` — the object to modify.
- `name` — the attribute name, as a string.
- `value` — what to store.

**What you get back:** Nothing (`None`) — it changes the object in place.

**Examples (with solutions):**

Example 1 — set an attribute by name
```python
class Box:
    pass

b = Box()
setattr(b, "color", "red")
print(b.color)
```
**Output:**
```
red
```
**What happened:** `setattr(b, "color", "red")` is the same as writing `b.color = "red"`.

Example 2 — the name can come from a variable
```python
b = Box()
field = "size"
setattr(b, field, "large")
print(b.size)
```
**Output:**
```
large
```
**What happened:** The attribute name lived in a variable; `setattr` used its value (`"size"`) as the name.

Example 3 — set many attributes from a dictionary
```python
b = Box()
for key, value in {"cpu": 4, "mem": 16}.items():
    setattr(b, key, value)
print(b.cpu, b.mem)
```
**Output:**
```
4 16
```
**What happened:** We looped over a dictionary and created one attribute per key/value pair.

Example 4 — overwrite an existing attribute
```python
b = Box()
b.region = "us-east-1"
setattr(b, "region", "eu-west-1")
print(b.region)
```
**Output:**
```
eu-west-1
```
**What happened:** `setattr` updated the existing `region` to a new value.

Example 5 — pairs nicely with getattr
```python
b = Box()
setattr(b, "status", "running")
print(getattr(b, "status"))
```
**Output:**
```
running
```
**What happened:** `setattr` writes by name; `getattr` reads by name — a matched pair.

**Common mistakes (and the fix):**
- ❌ Building attribute names from untrusted input — you could overwrite important things.
  ✅ Only use names you control, or check them against an allowed list first.
- ❌ Reaching for `setattr` when a plain dictionary would be simpler.
  ✅ If you just need name→value storage, a `dict` is often clearer than attributes.

**Real-world use case (with full solution):**

**The problem:** You parsed a config file into a dictionary, but the rest of your code expects a config **object** with attributes like `cfg.region`.

**The solution:**
```python
class Config:
    def __init__(self, data):
        for key, value in data.items():
            setattr(self, key, value)

cfg = Config({"region": "us-east-1", "replicas": 3, "tls": True})
print(cfg.region)
print(cfg.replicas)
print(cfg.tls)
```
**How it works, step by step:**
1. The constructor receives the parsed dictionary.
2. It loops over each key/value pair.
3. `setattr(self, key, value)` turns each pair into an attribute, so `data["region"]` becomes `cfg.region`.

**Output:**
```
us-east-1
3
True
```

**Mini-project (with solution):**

**Your task:** Load environment variables that start with `APP_` onto a settings object (e.g. `APP_REGION` becomes `settings.region`).

**Solution:**
```python
import os

class Settings:
    pass

def load_env(prefix="APP_"):
    settings = Settings()
    for key, value in os.environ.items():
        if key.startswith(prefix):
            attr_name = key[len(prefix):].lower()
            setattr(settings, attr_name, value)
    return settings

os.environ["APP_REGION"] = "eu-west-1"
os.environ["APP_TIER"] = "gold"
s = load_env()
print(s.region, s.tier)
```
**Output:**
```
eu-west-1 gold
```
**Explanation:** For each `APP_*` variable, we strip the `APP_` prefix, lowercase the rest to make a clean attribute name, and use `setattr` to attach it. Now your settings live as friendly attributes like `s.region`.

---

## `slice()`

**What it does (plain English):** Creates a reusable "slice" (a `start:stop:step` pattern) that you can name and apply to sequences. You already use slicing as `mylist[1:4]`; `slice()` lets you save that pattern in a variable.

**Syntax:** `slice(stop)` or `slice(start, stop)` or `slice(start, stop, step)`

**Parameters:**
- `start`, `stop`, `step` — the same pieces you'd write in `a[start:stop:step]` (any can be `None`).

**What you get back:** A `slice` object you can use inside `[]`.

**Examples (with solutions):**

Example 1 — a named slice
```python
first_three = slice(0, 3)
print([10, 20, 30, 40, 50][first_three])
```
**Output:**
```
[10, 20, 30]
```
**What happened:** `slice(0, 3)` means "positions 0,1,2"; using it in `[]` grabs the first three items.

Example 2 — it's the same as the colon form
```python
data = [10, 20, 30, 40, 50]
print(data[slice(1, 4)])
print(data[1:4])
```
**Output:**
```
[20, 30, 40]
[20, 30, 40]
```
**What happened:** `data[slice(1, 4)]` and `data[1:4]` do exactly the same thing.

Example 3 — a step slice (every other)
```python
every_other = slice(None, None, 2)
print(list(range(10))[every_other])
```
**Output:**
```
[0, 2, 4, 6, 8]
```
**What happened:** `slice(None, None, 2)` is like `[::2]` — take every second item.

Example 4 — slice a string
```python
print("hello world"[slice(0, 5)])
```
**Output:**
```
hello
```
**What happened:** Slicing works on strings too; this grabs the first 5 characters.

Example 5 — the last few items
```python
last_two = slice(-2, None)
print([1, 2, 3, 4, 5][last_two])
```
**Output:**
```
[4, 5]
```
**What happened:** `slice(-2, None)` is like `[-2:]` — the final two items.

**Common mistakes (and the fix):**
- ❌ Thinking slicing crashes on out-of-range bounds. It doesn't — it just clamps.
  ✅ `[1, 2, 3][slice(0, 99)]` safely returns the whole list.
- ❌ Writing the same `[a:b:c]` numbers over and over.
  ✅ Name them once with `slice(...)` to document what each region means.

**Real-world use case (with full solution):**

**The problem:** You're parsing a fixed-width log format where each field always sits at the same column positions. Naming those regions makes the parser readable.

**The solution:**
```python
TIMESTAMP = slice(0, 19)
LEVEL     = slice(20, 25)
MESSAGE   = slice(26, None)

line = "2024-06-01T12:00:00 ERROR disk full on /var"
print("time:   ", line[TIMESTAMP])
print("level:  ", line[LEVEL].strip())
print("message:", line[MESSAGE])
```
**How it works, step by step:**
1. We give each column range a clear name with `slice(...)`.
2. Applying a named slice to the line extracts that field.
3. The code reads like the format spec itself — far clearer than scattered `line[0:19]` numbers.

**Output:**
```
time:    2024-06-01T12:00:00
level:   ERROR
message: disk full on /var
```

**Mini-project (with solution):**

**Your task:** Parse a fixed-width inventory line into named fields (id, type, availability zone).

**Solution:**
```python
COLUMNS = {
    "id":   slice(0, 6),
    "type": slice(6, 16),
    "az":   slice(16, 26),
}

def parse(line):
    return {name: line[where].strip() for name, where in COLUMNS.items()}

print(parse("i-001 t3.micro   us-east-1a"))
```
**Output:**
```
{'id': 'i-001', 'type': 't3.micro', 'az': 'us-east-1a'}
```
**Explanation:** We map each field name to the column range it occupies. The parser loops over those named slices, pulls each region out of the line, and `.strip()`s the padding — turning a rigid fixed-width row into a friendly dictionary.

---

## `sorted()` 🔧

**What it does (plain English):** Returns a **new** sorted list from any collection. It doesn't change the original. You can sort by a custom rule with `key=` and reverse the order with `reverse=True`.

**Syntax:** `sorted(iterable, key=None, reverse=False)`

**Parameters:**
- `iterable` — what to sort.
- `key` — optional function deciding *how* to compare items.
- `reverse` — `True` for descending (largest first).

**What you get back:** A new sorted list.

**Examples (with solutions):**

Example 1 — sort numbers
```python
print(sorted([3, 1, 2]))
```
**Output:**
```
[1, 2, 3]
```
**What happened:** `sorted` returned a new list in ascending order.

Example 2 — the original is untouched
```python
original = [3, 1, 2]
result = sorted(original)
print(result)
print(original)
```
**Output:**
```
[1, 2, 3]
[3, 1, 2]
```
**What happened:** `sorted` makes a new list; the original list stays as it was.

Example 3 — sort biggest first
```python
print(sorted([3, 1, 2], reverse=True))
```
**Output:**
```
[3, 2, 1]
```
**What happened:** `reverse=True` flips the order to descending.

Example 4 — sort words ignoring case
```python
print(sorted(["banana", "Apple", "cherry"], key=str.lower))
```
**Output:**
```
['Apple', 'banana', 'cherry']
```
**What happened:** `key=str.lower` compares lowercased versions, so capitalization doesn't push `Apple` to the front by accident.

Example 5 — sort dictionaries by a field
```python
servers = [{"name": "b", "cpu": 90}, {"name": "a", "cpu": 30}]
print(sorted(servers, key=lambda s: s["cpu"]))
```
**Output:**
```
[{'name': 'a', 'cpu': 30}, {'name': 'b', 'cpu': 90}]
```
**What happened:** `key=lambda s: s["cpu"]` sorts by the `cpu` value, lowest first.

**Common mistakes (and the fix):**
- ❌ Confusing `sorted(x)` (returns a new list) with `x.sort()` (changes the list in place and returns `None`).
  ✅ Use `sorted` when you want a new list; use `.sort()` to reorder in place.
- ❌ Sorting mixed types like `sorted([1, "a"])` → error.
  ✅ Sort items of the same type, or provide a `key` that maps them to comparable values.

**Real-world use case (with full solution):**

**The problem:** You're cleaning up old snapshots and must process them oldest-first, so you delete the most stale ones before newer ones.

**The solution:**
```python
def cleanup_order(snapshots):
    return sorted(snapshots, key=lambda s: s["created"])

snaps = [
    {"id": "snap-A", "created": "2024-06-01"},
    {"id": "snap-B", "created": "2024-01-01"},
    {"id": "snap-C", "created": "2024-03-01"},
]
for snap in cleanup_order(snaps):
    print(snap["id"], snap["created"])
```
**How it works, step by step:**
1. `key=lambda s: s["created"]` tells `sorted` to compare by the creation date.
2. Dates in `YYYY-MM-DD` form sort correctly as text (earlier = smaller).
3. The result is oldest-first, which is the safe order to clean up.

**Output:**
```
snap-B 2024-01-01
snap-C 2024-03-01
snap-A 2024-06-01
```

**Mini-project (with solution):**

**Your task:** Report the top 2 most expensive services from a cost breakdown.

**Solution:**
```python
def top_spenders(costs, n=2):
    ranked = sorted(costs.items(), key=lambda pair: pair[1], reverse=True)
    return ranked[:n]

costs = {"ec2": 120, "s3": 8, "rds": 60, "lambda": 2}
print(top_spenders(costs))
```
**Output:**
```
[('ec2', 120), ('rds', 60)]
```
**Explanation:** `costs.items()` gives `(service, amount)` pairs. We sort them by amount (`pair[1]`) in descending order (`reverse=True`), then slice the first `n` to get the biggest spenders.

---

## `staticmethod()`

**What it does (plain English):** Marks a method inside a class as a plain helper function — one that doesn't need `self` (the instance) or `cls` (the class). It's just a related function kept tidily inside the class. Usually written with the `@staticmethod` decorator.

**Syntax:** `@staticmethod` above a method.

**Parameters:** (as a decorator) none — you decorate a normal function.

**What you get back:** A method you can call on the class without creating an instance.

**Examples (with solutions):**

Example 1 — a helper that needs no instance
```python
class Network:
    @staticmethod
    def cidr_size(prefix):
        return 2 ** (32 - prefix)

print(Network.cidr_size(24))
```
**Output:**
```
256
```
**What happened:** We called `cidr_size` straight on the class, no `Network()` needed, and it took no `self`.

Example 2 — no self parameter
```python
class Math:
    @staticmethod
    def double(x):
        return x * 2

print(Math.double(21))
```
**Output:**
```
42
```
**What happened:** A static method is just a function living in the class; it only takes the arguments you give it.

Example 3 — call it on an instance too (still works)
```python
class Math:
    @staticmethod
    def double(x):
        return x * 2

m = Math()
print(m.double(5))
```
**Output:**
```
10
```
**What happened:** You can call a static method on an instance as well; it behaves the same.

Example 4 — group related text helpers
```python
class Text:
    @staticmethod
    def slugify(s):
        return s.lower().replace(" ", "-")

print(Text.slugify("My Cool App"))
```
**Output:**
```
my-cool-app
```
**What happened:** `slugify` is a pure helper organized under `Text`, keeping related utilities together.

Example 5 — a static method is a normal function you can pass around
```python
class Network:
    @staticmethod
    def cidr_size(prefix):
        return 2 ** (32 - prefix)

operations = {"size": Network.cidr_size}
print(operations["size"](16))
```
**Output:**
```
65536
```
**What happened:** Because it's just a function, we stored it in a dictionary and called it later.

**Common mistakes (and the fix):**
- ❌ Adding `self` to a static method out of habit.
  ✅ Static methods take no `self` — only the arguments you actually use.
- ❌ Using `@staticmethod` when you need to build instances or support subclassing.
  ✅ For "alternate constructors" use `@classmethod` (which receives the class); use `@staticmethod` only for pure helpers.

**Real-world use case (with full solution):**

**The problem:** You have several small, stateless AWS helpers (like building an ARN string) and want them grouped logically without needing to create an object first.

**The solution:**
```python
class Aws:
    @staticmethod
    def arn(service, region, account, resource):
        return f"arn:aws:{service}:{region}:{account}:{resource}"

print(Aws.arn("s3", "", "", "my-bucket"))
print(Aws.arn("ec2", "us-east-1", "123456789012", "instance/i-001"))
```
**How it works, step by step:**
1. `arn` is a pure function: same inputs always give the same output, no object state needed.
2. Marking it `@staticmethod` lets us call `Aws.arn(...)` directly.
3. Grouping it under `Aws` keeps all your AWS string helpers in one obvious place.

**Output:**
```
arn:aws:s3:::my-bucket
arn:aws:ec2:us-east-1:123456789012:instance/i-001
```

**Mini-project (with solution):**

**Your task:** Build a small validation toolkit class with stateless checks (valid region? valid port?).

**Solution:**
```python
class Validate:
    @staticmethod
    def region(r):
        return r in {"us-east-1", "eu-west-1", "ap-south-1"}

    @staticmethod
    def port(p):
        return 1 <= p <= 65535

print(Validate.region("us-east-1"))
print(Validate.region("mars-1"))
print(Validate.port(8080))
print(Validate.port(99999))
```
**Output:**
```
True
False
True
False
```
**Explanation:** Each validator is a self-contained check that needs no object state, so `@staticmethod` is perfect. Grouping them under `Validate` gives you a clean namespace: `Validate.region(...)`, `Validate.port(...)`.

---

## `str()` 🔧

**What it does (plain English):** Turns a value into human-readable text (a string). Numbers, lists, `None` — anything can be converted to its text form.

**Syntax:** `str(value)` or `str(bytes, encoding)`

**Parameters:**
- `value` — any value to convert to text.
- `encoding` — only when converting `bytes` to text (e.g. `"utf-8"`).

**What you get back:** A string.

**Examples (with solutions):**

Example 1 — number to text
```python
print(str(42))
print(type(str(42)))
```
**Output:**
```
42
<class 'str'>
```
**What happened:** `str(42)` produced the text `"42"` — note the type is now `str`, not `int`.

Example 2 — combine a number into a message
```python
count = 3
print("There are " + str(count) + " servers")
```
**Output:**
```
There are 3 servers
```
**What happened:** You can't add a number directly to text, so `str(count)` converts it first.

Example 3 — None becomes "None"
```python
print(str(None))
```
**Output:**
```
None
```
**What happened:** Even `None` has a text form: the word `"None"`.

Example 4 — a list becomes its text representation
```python
print(str([1, 2, 3]))
```
**Output:**
```
[1, 2, 3]
```
**What happened:** The whole list is turned into one text string.

Example 5 — decode bytes into text
```python
print(str(b"hi", "utf-8"))
```
**Output:**
```
hi
```
**What happened:** Given an encoding, `str` decodes raw `bytes` into normal text.

**Common mistakes (and the fix):**
- ❌ `str(b"hi")` *without* an encoding gives the literal `"b'hi'"`, not `"hi"`.
  ✅ Pass the encoding: `str(b"hi", "utf-8")`, or use `b"hi".decode("utf-8")`.
- ❌ Trying to add text and numbers directly: `"count: " + 3` → error.
  ✅ Convert first: `"count: " + str(3)`, or use an f-string: `f"count: {3}"`.

**Real-world use case (with full solution):**

**The problem:** Cloud tags must be strings, but the values you're tagging with are a mix of numbers, booleans, and lists. You need them all safely turned into text.

**The solution:**
```python
def tagify(value, max_length=256):
    return str(value)[:max_length]

print(tagify(12345))
print(tagify(True))
print(tagify(["a", "b"]))
```
**How it works, step by step:**
1. `str(value)` converts whatever you pass into text.
2. `[:max_length]` trims it to the maximum tag length (AWS tags have a 256-char limit).
3. The result is always a safe string, no matter the input type.

**Output:**
```
12345
True
['a', 'b']
```

**Mini-project (with solution):**

**Your task:** Build a CSV row from mixed-type values, making sure each value is text and any commas inside values won't break the format.

**Solution:**
```python
def to_csv_row(values, separator=","):
    safe = [str(v).replace(separator, " ") for v in values]
    return separator.join(safe)

print(to_csv_row(["i-1", 3, True, None]))
print(to_csv_row(["has, comma", 5]))
```
**Output:**
```
i-1,3,True,None
has  comma,5
```
**Explanation:** Each value is converted to text with `str(v)`, and any comma inside a value is replaced with a space so it doesn't create a fake column. Then `join` stitches them into one comma-separated line.

---

## `sum()` 🔧

**What it does (plain English):** Adds up all the numbers in a list (or other iterable). Optionally starts the total from a value you choose.

**Syntax:** `sum(iterable)` or `sum(iterable, start)`

**Parameters:**
- `iterable` — numbers to add.
- `start` — optional starting value for the total (default 0).

**What you get back:** The total.

**Examples (with solutions):**

Example 1 — add a list of numbers
```python
print(sum([1, 2, 3, 4]))
```
**Output:**
```
10
```
**What happened:** `sum` added 1+2+3+4 to get 10.

Example 2 — sum a range
```python
print(sum(range(1, 101)))
```
**Output:**
```
5050
```
**What happened:** `range(1, 101)` is 1–100; their total is 5050.

Example 3 — start the total from a value
```python
print(sum([10, 20], 100))
```
**Output:**
```
130
```
**What happened:** The `start` of 100 is added to the list's total (30), giving 130.

Example 4 — sum with a generator (no list needed)
```python
words = ["a", "bb", "ccc"]
print(sum(len(w) for w in words))
```
**Output:**
```
6
```
**What happened:** We summed the lengths (1+2+3) directly from a generator expression — no temporary list.

Example 5 — decimals add up too
```python
print(sum([1.5, 2.5, 1.0]))
```
**Output:**
```
5.0
```
**What happened:** `sum` works with floats; the total is `5.0`.

**Common mistakes (and the fix):**
- ❌ Trying to `sum` a list of strings to join them: `sum(["a", "b"], "")` → error.
  ✅ Use `"".join(["a", "b"])` to combine strings.
- ❌ Worrying about precision when adding many decimals.
  ✅ For high-precision needs, use `math.fsum(...)` or the `decimal` module.

**Real-world use case (with full solution):**

**The problem:** A cloud bill lists many line items, each with an amount (as text). You need the total cost, rounded to cents.

**The solution:**
```python
def total_cost(line_items):
    return round(sum(float(item["amount"]) for item in line_items), 2)

bill = [
    {"service": "ec2", "amount": "120.50"},
    {"service": "s3",  "amount": "8.00"},
    {"service": "rds", "amount": "45.25"},
]
print(total_cost(bill))
```
**How it works, step by step:**
1. The generator `float(item["amount"]) for item in line_items` turns each text amount into a number.
2. `sum(...)` adds them all up.
3. `round(..., 2)` tidies the total to two decimal places (cents).

**Output:**
```
173.75
```

**Mini-project (with solution):**

**Your task:** Roll up total storage used per bucket and report it in gigabytes.

**Solution:**
```python
def storage_rollup(objects):
    totals = {}
    for obj in objects:
        totals[obj["bucket"]] = totals.get(obj["bucket"], 0) + obj["bytes"]
    return {bucket: round(b / 1024**3, 2) for bucket, b in totals.items()}

data = [
    {"bucket": "logs", "bytes": 2 * 1024**3},
    {"bucket": "logs", "bytes": 1 * 1024**3},
    {"bucket": "backups", "bytes": 5 * 1024**3},
]
print(storage_rollup(data))
```
**Output:**
```
{'logs': 3.0, 'backups': 5.0}
```
**Explanation:** We tally bytes per bucket into a dictionary (using `.get(bucket, 0)` to start each at zero). Then we convert each total from bytes to GiB by dividing by `1024**3` and rounding. (Here `sum`-style accumulation is done with `+`; you could also `sum` a per-bucket list.)

---

## `super()`

**What it does (plain English):** Inside a subclass, `super()` lets you call the parent class's version of a method — so you can build on what the parent already does instead of rewriting it. Most common in `__init__`.

**Syntax:** `super().method(...)`

**Parameters:** (modern form) none — Python figures out the parent automatically.

**What you get back:** A proxy that forwards your call to the parent class.

**Examples (with solutions):**

Example 1 — extend a parent method
```python
class Animal:
    def describe(self):
        return "I am an animal"

class Dog(Animal):
    def describe(self):
        return super().describe() + " (a dog)"

print(Dog().describe())
```
**Output:**
```
I am an animal (a dog)
```
**What happened:** `Dog.describe` called the parent's `describe()` via `super()`, then added its own text.

Example 2 — call the parent's __init__
```python
class Base:
    def __init__(self, region):
        self.region = region

class Child(Base):
    def __init__(self, region, tier):
        super().__init__(region)     # let Base set up region
        self.tier = tier

c = Child("us-east-1", "gold")
print(c.region, c.tier)
```
**Output:**
```
us-east-1 gold
```
**What happened:** `super().__init__(region)` ran the parent's setup, so `region` was stored; then the child added `tier`.

Example 3 — forgetting super skips parent setup
```python
class Base:
    def __init__(self):
        self.ready = True

class Good(Base):
    def __init__(self):
        super().__init__()

print(Good().ready)
```
**Output:**
```
True
```
**What happened:** Because we called `super().__init__()`, the parent's `ready` attribute was set up correctly.

Example 4 — add behavior around the parent's
```python
class Service:
    def start(self):
        return "service started"

class LoggedService(Service):
    def start(self):
        print("logging: starting")
        return super().start()

print(LoggedService().start())
```
**Output:**
```
logging: starting
service started
```
**What happened:** The subclass added a log line, then delegated the real work to the parent with `super().start()`.

Example 5 — the parent value is reused, not duplicated
```python
class A:
    greeting = "hello"
    def greet(self):
        return self.greeting

class B(A):
    def greet(self):
        return super().greet().upper()

print(B().greet())
```
**Output:**
```
HELLO
```
**What happened:** `B` reused `A`'s `greet()` result and just uppercased it.

**Common mistakes (and the fix):**
- ❌ Forgetting `super().__init__(...)` in a subclass — the parent's setup never runs, so attributes go missing.
  ✅ Call `super().__init__(...)` early in your subclass's `__init__`.
- ❌ Hardcoding the parent's name like `Base.__init__(self, ...)`.
  ✅ Use `super()` — it keeps working correctly even with more complex inheritance.

**Real-world use case (with full solution):**

**The problem:** You want a cloud client that behaves exactly like a base client but also carries a set of default tags — without rewriting the base setup.

**The solution:**
```python
class BaseClient:
    def __init__(self, region):
        self.region = region

class TaggedClient(BaseClient):
    def __init__(self, region, default_tags):
        super().__init__(region)          # keep the base setup
        self.default_tags = default_tags

client = TaggedClient("us-east-1", {"managed_by": "python"})
print(client.region)
print(client.default_tags)
```
**How it works, step by step:**
1. `TaggedClient` extends `BaseClient`.
2. `super().__init__(region)` runs the base setup, so `region` is stored exactly as before.
3. Then the subclass adds its own `default_tags` — building on the parent rather than replacing it.

**Output:**
```
us-east-1
{'managed_by': 'python'}
```

**Mini-project (with solution):**

**Your task:** Create a "timing" wrapper using a mixin that measures how long a job's `execute()` takes, by wrapping the parent's method with `super()`.

**Solution:**
```python
import time

class TimedMixin:
    def execute(self, *args, **kwargs):
        start = time.perf_counter()
        result = super().execute(*args, **kwargs)   # run the real work
        elapsed = time.perf_counter() - start
        print(f"took {elapsed:.4f}s")
        return result

class Job:
    def execute(self):
        return "job done"

class TimedJob(TimedMixin, Job):
    pass

print(TimedJob().execute())
```
**Output:**
```
took 0.0000s
job done
```
**Explanation:** `TimedJob` combines the mixin and the real `Job`. When you call `execute()`, the mixin runs first, records the start time, calls `super().execute()` (which reaches `Job.execute`), then prints the elapsed time — adding timing without touching `Job` itself. (Your exact timing number will vary.)

---

## `tuple()`

**What it does (plain English):** Makes a **tuple** — like a list, but **unchangeable** (immutable). Great for fixed groups of values and for use as dictionary keys.

**Syntax:** `tuple()` or `tuple(iterable)`

**Parameters:**
- `iterable` — optional; items to put in the tuple.

**What you get back:** A tuple.

**Examples (with solutions):**

Example 1 — make a tuple from a list
```python
print(tuple([1, 2, 3]))
```
**Output:**
```
(1, 2, 3)
```
**What happened:** The list became a tuple, shown with parentheses instead of square brackets.

Example 2 — tuples can't be changed
```python
point = (10, 20)
try:
    point[0] = 99
except TypeError as e:
    print("error:", e)
```
**Output:**
```
error: 'tuple' object does not support item assignment
```
**What happened:** Tuples are immutable, so trying to change an item raises an error. (That immutability is the point — it keeps fixed data safe.)

Example 3 — the single-item tuple needs a comma
```python
one = (5,)
not_a_tuple = (5)
print(type(one))
print(type(not_a_tuple))
```
**Output:**
```
<class 'tuple'>
<class 'int'>
```
**What happened:** `(5,)` (with a comma) is a one-item tuple; `(5)` is just the number 5 in parentheses.

Example 4 — unpack a tuple into variables
```python
host, port = ("db.internal", 5432)
print(host)
print(port)
```
**Output:**
```
db.internal
5432
```
**What happened:** A tuple of two values was unpacked neatly into two variables.

Example 5 — a tuple as a dictionary key
```python
usage = {}
usage[("us-east-1", "t3.micro")] = 42
print(usage[("us-east-1", "t3.micro")])
```
**Output:**
```
42
```
**What happened:** Because tuples are immutable, they can be dictionary keys — here a combined (region, type) key.

**Common mistakes (and the fix):**
- ❌ Writing `(5)` and expecting a tuple — it's just `5`.
  ✅ Add a trailing comma for a single-item tuple: `(5,)`.
- ❌ Trying to change a tuple's contents.
  ✅ If you need to change it, use a list; use a tuple only for fixed data.

**Real-world use case (with full solution):**

**The problem:** You want to group metrics by a **combination** of fields (region *and* instance type). A single combined key makes the grouping clean — and dictionary keys must be immutable.

**The solution:**
```python
def group_cpu(samples):
    groups = {}
    for s in samples:
        key = (s["region"], s["instance_type"])   # immutable composite key
        groups.setdefault(key, []).append(s["cpu"])
    return groups

data = [
    {"region": "us-east-1", "instance_type": "t3.micro", "cpu": 40},
    {"region": "us-east-1", "instance_type": "t3.micro", "cpu": 60},
    {"region": "eu-west-1", "instance_type": "m5.large", "cpu": 25},
]
print(group_cpu(data))
```
**How it works, step by step:**
1. For each sample we build a `(region, instance_type)` tuple as the group key.
2. Because tuples are immutable, they're valid dictionary keys.
3. `setdefault(key, [])` starts a fresh list per group, and we append each cpu reading.

**Output:**
```
{('us-east-1', 't3.micro'): [40, 60], ('eu-west-1', 'm5.large'): [25]}
```

**Mini-project (with solution):**

**Your task:** Given a set of map coordinates as `(lat, lon)` tuples, compute the bounding box (the min and max corners).

**Solution:**
```python
def bounding_box(points):
    lats = tuple(p[0] for p in points)
    lons = tuple(p[1] for p in points)
    bottom_left = (min(lats), min(lons))
    top_right   = (max(lats), max(lons))
    return bottom_left, top_right

print(bounding_box([(40.0, -74.0), (41.5, -73.0), (40.5, -75.0)]))
```
**Output:**
```
((40.0, -75.0), (41.5, -73.0))
```
**Explanation:** We pull all latitudes and longitudes into tuples, then take the smallest of each for the bottom-left corner and the largest for the top-right. The result is two `(lat, lon)` tuples marking the box that contains every point.

---

## `type()` 🔧

**What it does (plain English):** Tells you what kind of thing a value is (its type, like `int`, `str`, or `list`). It has an advanced second job — creating classes on the fly — but as a beginner you'll mostly use the simple "what is this?" form.

**Syntax:** `type(value)` (simple) or `type(name, bases, attributes)` (advanced)

**Parameters:**
- Simple form: `value` — any value.
- Advanced form: `name`, `bases` (parent classes), `attributes` (a dict) — to build a new class.

**What you get back:** The value's type (or, in the advanced form, a new class).

**Examples (with solutions):**

Example 1 — what type is this?
```python
print(type(42))
print(type("hello"))
print(type([1, 2]))
```
**Output:**
```
<class 'int'>
<class 'str'>
<class 'list'>
```
**What happened:** `type` reported the kind of each value.

Example 2 — compare against a known type
```python
value = 3.14
print(type(value) is float)
```
**Output:**
```
True
```
**What happened:** We checked whether the value's type is exactly `float`. (For flexible checks that also accept subclasses, prefer `isinstance` — see below.)

Example 3 — types of dictionary values
```python
config = {"replicas": 3, "region": "us-east-1", "tls": True}
for key, val in config.items():
    print(key, "->", type(val).__name__)
```
**Output:**
```
replicas -> int
region -> str
tls -> bool
```
**What happened:** `type(val).__name__` gives the short type name as text — handy for reports.

Example 4 — None has a type too
```python
print(type(None))
```
**Output:**
```
<class 'NoneType'>
```
**What happened:** Even `None` has a type: `NoneType`.

Example 5 — booleans are a kind of integer
```python
print(type(True))
print(isinstance(True, int))
```
**Output:**
```
<class 'bool'>
True
```
**What happened:** `True`'s exact type is `bool`, but `bool` is built on top of `int`, so `isinstance(True, int)` is `True`.

**Common mistakes (and the fix):**
- ❌ Using `type(x) == int` for checks — it fails for subclasses.
  ✅ Prefer `isinstance(x, int)`, which correctly accepts subclasses.
- ❌ Comparing types with `==` instead of `is`.
  ✅ Use `type(x) is int` for an exact-type check.

**Real-world use case (with full solution):**

**The problem:** Config values come in different types, and each type needs to be turned into a tag string differently (a list should become `"a,b"`, a bool should become `"true"/"false"`).

**The solution:**
```python
def to_tag_value(value):
    converters = {
        bool: lambda b: "true" if b else "false",
        list: lambda l: ",".join(map(str, l)),
        int:  str,
    }
    converter = converters.get(type(value), str)   # default: plain str()
    return converter(value)

print(to_tag_value(True))
print(to_tag_value([1, 2, 3]))
print(to_tag_value("prod"))
```
**How it works, step by step:**
1. We map each type to a small conversion function.
2. `type(value)` looks up the right converter for this value's type.
3. If the type isn't in the map, we fall back to plain `str()`.

**Output:**
```
true
1,2,3
prod
```
> Note: we check `bool` before `int` here because every `bool` is also an `int`. (Dictionary lookup by exact type avoids that trap.)

**Mini-project (with solution):**

**Your task:** Validate that each config field has the expected type, reporting any mismatches.

**Solution:**
```python
def check_schema(config, schema):
    errors = []
    for field, expected_type in schema.items():
        actual = config.get(field)
        if not isinstance(actual, expected_type):
            errors.append(
                f"{field}: expected {expected_type.__name__}, "
                f"got {type(actual).__name__}"
            )
    return errors

schema = {"replicas": int, "region": str}
print(check_schema({"replicas": "3", "region": "us-east-1"}, schema))
print(check_schema({"replicas": 3, "region": "us-east-1"}, schema))
```
**Output:**
```
['replicas: expected int, got str']
[]
```
**Explanation:** For each field we compare its actual type to the expected one with `isinstance`. The first config has `replicas` as text instead of a number, so we report it; the second config is valid, so the error list is empty.

---

## `vars()`

**What it does (plain English):** Shows an object's attributes as a dictionary (its internal `__dict__`). A quick way to peek inside an object or turn it into a plain dictionary.

**Syntax:** `vars(object)` (or `vars()` with no argument, like `locals()`)

**Parameters:**
- `object` — optional; an object that stores attributes.

**What you get back:** A dictionary of `{attribute_name: value}`.

**Examples (with solutions):**

Example 1 — see an object's attributes
```python
class Box:
    pass

b = Box()
b.width = 10
b.height = 5
print(vars(b))
```
**Output:**
```
{'width': 10, 'height': 5}
```
**What happened:** `vars(b)` returned the attributes you set on `b`, as a dictionary.

Example 2 — attributes set in __init__
```python
class Server:
    def __init__(self):
        self.region = "us-east-1"
        self.cpu = 4

print(vars(Server()))
```
**Output:**
```
{'region': 'us-east-1', 'cpu': 4}
```
**What happened:** The attributes assigned in `__init__` show up in `vars`.

Example 3 — just the attribute names
```python
class Server:
    def __init__(self):
        self.region = "us-east-1"
        self.cpu = 4

print(list(vars(Server())))
```
**Output:**
```
['region', 'cpu']
```
**What happened:** Listing `vars(...)` gives just the attribute names (the dictionary's keys).

Example 4 — it's the live dictionary
```python
class Box:
    pass

b = Box()
vars(b)["color"] = "blue"      # modifies the object!
print(b.color)
```
**Output:**
```
blue
```
**What happened:** `vars(b)` is the object's actual attribute store, so writing into it added a real attribute.

Example 5 — turn an object into JSON
```python
import json

class Config:
    def __init__(self):
        self.region = "us-east-1"
        self.replicas = 3

print(json.dumps(vars(Config())))
```
**Output:**
```
{"region": "us-east-1", "replicas": 3}
```
**What happened:** `vars(...)` gave a plain dictionary that `json.dumps` could serialize directly.

**Common mistakes (and the fix):**
- ❌ Calling `vars(42)` or `vars("text")` — basic values don't have a `__dict__`, so it errors.
  ✅ Use `vars` on your own class instances, not on plain numbers/strings.
- ❌ Forgetting that editing the returned dict edits the object.
  ✅ If you want an independent copy, do `dict(vars(obj))`.

**Real-world use case (with full solution):**

**The problem:** You have a config **object** but your API or log needs a plain dictionary (or JSON). You want the conversion without listing every attribute by hand.

**The solution:**
```python
import json

class DeployConfig:
    def __init__(self):
        self.region = "us-east-1"
        self.replicas = 3
        self.canary = True

config = DeployConfig()
print(json.dumps(vars(config)))
```
**How it works, step by step:**
1. `vars(config)` collects all the object's attributes into a dictionary.
2. `json.dumps(...)` turns that dictionary into a JSON string.
3. You get a ready-to-send payload without manually writing each field.

**Output:**
```
{"region": "us-east-1", "replicas": 3, "canary": true}
```

**Mini-project (with solution):**

**Your task:** Compare two config objects and report which attributes differ.

**Solution:**
```python
def diff_objects(a, b):
    a_attrs, b_attrs = vars(a), vars(b)
    all_keys = set(a_attrs) | set(b_attrs)
    return {
        key: (a_attrs.get(key), b_attrs.get(key))
        for key in all_keys
        if a_attrs.get(key) != b_attrs.get(key)
    }

class C:
    pass

old = C(); old.region = "us-east-1"; old.replicas = 3
new = C(); new.region = "eu-west-1"; new.replicas = 3
print(diff_objects(old, new))
```
**Output:**
```
{'region': ('us-east-1', 'eu-west-1')}
```
**Explanation:** `vars(...)` turns each object into a dictionary. We gather all attribute names, then keep only those where the two objects disagree — showing the old and new values side by side. Here only `region` changed.

---

## `zip()` 🔧

**What it does (plain English):** Pairs up items from two (or more) lists, position by position — first with first, second with second, and so on. Perfect for combining related lists.

**Syntax:** `zip(iterable1, iterable2, ...)` (optionally `strict=True`)

**Parameters:**
- `iterable1, iterable2, ...` — two or more lists/sequences to combine.
- `strict` — if `True` (Python 3.10+), raises an error when the lengths don't match.

**What you get back:** A lazy `zip` object of tuples — wrap in `list()` or `dict()` to use it.

**Examples (with solutions):**

Example 1 — pair two lists
```python
names = ["web", "db"]
ports = [80, 5432]
print(list(zip(names, ports)))
```
**Output:**
```
[('web', 80), ('db', 5432)]
```
**What happened:** `zip` matched each name with the port at the same position.

Example 2 — build a dictionary from two lists
```python
keys = ["region", "replicas"]
values = ["us-east-1", 3]
print(dict(zip(keys, values)))
```
**Output:**
```
{'region': 'us-east-1', 'replicas': 3}
```
**What happened:** Zipping keys with values and passing to `dict()` builds a dictionary instantly.

Example 3 — loop over two lists together
```python
servers = ["i-1", "i-2"]
states = ["running", "stopped"]
for server, state in zip(servers, states):
    print(f"{server}: {state}")
```
**Output:**
```
i-1: running
i-2: stopped
```
**What happened:** `zip` let us walk both lists in step inside one clean loop.

Example 4 — it stops at the shortest list
```python
print(list(zip([1, 2, 3], ["a", "b"])))
```
**Output:**
```
[(1, 'a'), (2, 'b')]
```
**What happened:** The second list had only 2 items, so `zip` stopped there (the `3` was ignored).

Example 5 — catch length mismatches with strict
```python
try:
    list(zip([1, 2, 3], ["a", "b"], strict=True))
except ValueError as e:
    print("error:", e)
```
**Output:**
```
error: zip() argument 2 is shorter than argument 1
```
**What happened:** `strict=True` turned the silent truncation into a clear error — great for catching bugs.

**Common mistakes (and the fix):**
- ❌ Not noticing that `zip` silently drops extra items when lists are different lengths.
  ✅ Use `strict=True` when the lists *should* be the same length.
- ❌ Printing `zip(...)` directly and seeing `<zip object ...>`.
  ✅ Wrap it: `list(zip(...))` or `dict(zip(...))`, or loop over it.

**Real-world use case (with full solution):**

**The problem:** Two separate API calls gave you a list of instance IDs and a matching list of their states. You need them combined into one ID→state map — and you want to be warned if the lists don't line up.

**The solution:**
```python
def merge_status(ids, states):
    return dict(zip(ids, states, strict=True))

print(merge_status(["i-1", "i-2", "i-3"], ["running", "stopped", "running"]))
```
**How it works, step by step:**
1. `zip(ids, states)` pairs each ID with the state at the same position.
2. `strict=True` raises an error if the two lists are different lengths (a sign something went wrong).
3. `dict(...)` turns the pairs into an ID→state lookup.

**Output:**
```
{'i-1': 'running', 'i-2': 'stopped', 'i-3': 'running'}
```

**Mini-project (with solution):**

**Your task:** Given a header and rows of metric data, find the maximum value in each column (a mini "transpose" trick).

**Solution:**
```python
def column_maxes(header, rows):
    columns = list(zip(*rows))                 # turn rows into columns
    return dict(zip(header, (max(col) for col in columns)))

header = ["cpu", "mem"]
rows = [(40, 70), (90, 65), (55, 80)]
print(column_maxes(header, rows))
```
**Output:**
```
{'cpu': 90, 'mem': 80}
```
**Explanation:** `zip(*rows)` is the clever part: it "transposes" the rows into columns, so all cpu values group together and all mem values group together. We take `max` of each column, then zip those maxes back to their header names.

---

## `__import__()`

**What it does (plain English):** The low-level function that the `import` statement uses behind the scenes. You rarely call it yourself — when you need to import a module whose name is decided at runtime, use the friendlier `importlib.import_module()` instead. It's included here because it's the 71st built-in.

**Syntax:** `__import__(name)` — but prefer `importlib.import_module(name)`.

**Parameters:**
- `name` — the module name, as text. (Plus advanced options you'll rarely touch.)

**What you get back:** The imported module.

**Examples (with solutions):**

Example 1 — normal import (what you should usually write)
```python
import math
print(math.sqrt(16))
```
**Output:**
```
4.0
```
**What happened:** The everyday `import` statement is what `__import__` powers under the hood — you normally just write `import math`.

Example 2 — the friendly way to import by name
```python
import importlib
module = importlib.import_module("math")
print(module.sqrt(25))
```
**Output:**
```
5.0
```
**What happened:** `importlib.import_module("math")` imports a module chosen at runtime (from a string) — the recommended approach.

Example 3 — __import__ does work, but is clunky
```python
json_module = __import__("json")
print(json_module.dumps({"a": 1}))
```
**Output:**
```
{"a": 1}
```
**What happened:** `__import__("json")` returned the `json` module, which we used to make JSON. It works, but `importlib.import_module` is clearer.

Example 4 — choose a module name from a variable
```python
import importlib
name = "statistics"
stats = importlib.import_module(name)
print(stats.mean([10, 20, 30]))
```
**Output:**
```
20
```
**What happened:** The module name lived in a variable; `import_module` loaded it dynamically.

Example 5 — import a specific function safely
```python
import importlib
collections = importlib.import_module("collections")
Counter = collections.Counter
print(Counter("banana"))
```
**Output:**
```
Counter({'a': 3, 'n': 2, 'b': 1})
```
**What happened:** We imported `collections` by name, then grabbed `Counter` from it.

**Common mistakes (and the fix):**
- ❌ Using `__import__` for everyday imports.
  ✅ Just write `import module` normally. Use dynamic import only when the name is decided at runtime.
- ❌ Reaching for `__import__` for dynamic imports (it has confusing rules for sub-modules).
  ✅ Use `importlib.import_module(name)` — it's clearer and does the right thing.

**Real-world use case (with full solution):**

**The problem:** Your tool supports multiple cloud backends (AWS, Azure, GCP), and which one to load is set in config. You want to import the right backend module by name at runtime.

**The solution:**
```python
import importlib

def load_backend(module_name):
    return importlib.import_module(module_name)

# In real life: "backends.aws" / "backends.azure" / "backends.gcp".
# Here we use a standard module as a stand-in:
backend = load_backend("json")
print(backend.dumps({"backend": "loaded"}))
```
**How it works, step by step:**
1. The backend's module name comes from config (text).
2. `importlib.import_module(module_name)` loads exactly that module at runtime.
3. We use the loaded module like any normal import — your code stays the same regardless of which backend was chosen.

**Output:**
```
{"backend": "loaded"}
```

**Mini-project (with solution):**

**Your task:** Build a tiny "plugin selector" that loads a storage backend by name and calls a shared function on it.

**Solution:**
```python
import importlib, sys, types

# Create two pretend backend modules in memory:
s3 = types.ModuleType("s3");   s3.store  = lambda key: f"s3://{key}"
gcs = types.ModuleType("gcs"); gcs.store = lambda key: f"gs://{key}"
sys.modules["s3"] = s3
sys.modules["gcs"] = gcs

def store_with(backend_name, key):
    backend = importlib.import_module(backend_name)
    return backend.store(key)

print(store_with("s3", "report.csv"))
print(store_with("gcs", "report.csv"))
```
**Output:**
```
s3://report.csv
gs://report.csv
```
**Explanation:** Each backend module exposes the same `store` function. `import_module(backend_name)` loads whichever one the caller asked for by name, and we call its `store` — so switching backends is just a change of string, with no `if/else` chain.

---

# Appendix — Quick Reference

## All 71 built-ins, grouped by what they do

**Turn one type into another (conversions):** `bool` `int` `float` `complex` `str` `bytes` `bytearray` `memoryview` `list` `tuple` `set` `frozenset` `dict` (plus `object`)

**Loop, count, and reshape collections:** `len` `range` `enumerate` `zip` `map` `filter` `sorted` `reversed` `iter` `next` `all` `any` `slice` `aiter` `anext`

**Do math:** `abs` `round` `min` `max` `sum` `pow` `divmod`

**Show, read, and format:** `print` `input` `open` `format` `repr` `ascii` `bin` `oct` `hex` `chr` `ord`

**Inspect objects (introspection):** `type` `isinstance` `issubclass` `id` `hash` `dir` `vars` `getattr` `setattr` `hasattr` `delattr` `callable` `globals` `locals`

**Build classes (object-oriented helpers):** `super` `property` `staticmethod` `classmethod` `object`

**Run code / import (advanced — handle with care):** `eval` ⚠️ `exec` ⚠️ `compile` `__import__`

**Developer tools:** `help` `breakpoint`

## The 15 you'll use most as a DevOps beginner

Start by getting comfortable with these — they cover the vast majority of real scripts:

`print` · `len` · `int` · `str` · `list` · `dict` · `range` · `enumerate` · `sorted` · `sum` · `min` · `max` · `open` · `zip` · `set`

## Beginner safety notes

- **Parsing booleans:** never trust `bool("False")` — it's `True`! Any non-empty string is "truthy." Parse env flags explicitly (check if the text is `"1"`, `"true"`, `"yes"`, …).
- **Empty collections:** `all([])` is `True` and `any([])` is `False`. Guard for emptiness before trusting a "pass."
- **Money:** don't use floats and `round` for currency — tiny errors creep in. Use the `decimal` module.
- **Never run untrusted input** through `eval`, `exec`, `compile`, or `__import__`. For data, use `json.loads` or `ast.literal_eval` instead.
- **Always use `with open(...)`** so files close themselves, and pass `encoding="utf-8"` for consistent behavior across computers.

## Handy beginner patterns to copy

- **Count things:** `len(items)` — but to check "is it empty?", just use `if not items:`.
- **First match or nothing:** `next((x for x in items if condition), None)`.
- **Biggest/smallest by a field:** `max(items, key=lambda x: x["field"])` / `min(...)`.
- **What changed between two groups:** `set(new) - set(old)` (added) and `set(old) - set(new)` (removed).
- **Combine two lists:** `dict(zip(keys, values))`.
- **Retry delays that grow:** `min(pow(2, attempt), cap)`.

---

*A beginner-friendly companion to the `python-for-devops` Chapter 02 handbook.
Every example shows its output and explains what happened; every use case and
mini-project includes a full solution. Python 3.10+. Cloud SDK lines are
illustrative — add real credentials/clients to run them for real.*