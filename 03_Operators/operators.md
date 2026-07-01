# 🐍 Python Operators — Master Guide

> A single, beginner-friendly `operators.py` that teaches **every Python operator** with **200+ commented examples** and **6 mini-projects** — from absolute basics to advanced operator overloading.
>
> 📦 **Part of the beginner series** — the companion to `variables.py`, built in the exact same explained-and-commented style (ASCII banner, per-concept `DESCRIPTION / SYNTAX / WHEN TO USE / ⚠️ COMMON MISTAKE` blocks, a **Mini Reference**, and a **Your turn** practice list).

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Level](https://img.shields.io/badge/Level-Beginner%20→%20Advanced-brightgreen)]()
[![Examples](https://img.shields.io/badge/Examples-200%2B-orange)]()
[![Runs](https://img.shields.io/badge/Runs-No%20errors-success)]()

---

## ✨ What's inside

Everything lives in one file: **`operators.py`**. Just read top to bottom.

| Level | Examples | Topics |
|-------|:--------:|--------|
| 🟢 **1 · Basics** | 1–50 | Arithmetic `+ - * / // % **`, comparison `== != < >`, assignment `=` |
| 🔵 **2 · Intermediate** | 51–100 | Augmented `+= -=`, logical `and or not`, membership `in`, identity `is` |
| 🟣 **3 · Intermediate+** | 101–150 | Bitwise `& \| ^ ~ << >>`, precedence, ternary, walrus `:=`, chaining |
| 🔴 **4 · Advanced** | 151–200 | Operator overloading (dunders), `@`, unpacking `* **`, `operator` module |

Plus **6 mini-projects**: Calculator · Number Inspector · Temperature Converter · Bitwise Permissions · Grade Calculator · Vector Playground.

---

## 🚀 How to run

```bash
python operators.py
```

That's it — every example prints to your screen, grouped by level.

## 📁 Suggested repo layout (matches the series)

If you're following on from `variables.py`, keep the chapters side by side:

```text
your-python-repo/
├── 02_variables_and_builtins/
│   └── variables.py
└── 03_operators/
    ├── operators.py
    └── README.md
```

Add it to GitHub:

```bash
git add 03_operators/operators.py 03_operators/README.md
git commit -m "Add beginner-friendly operators.py with 200+ explained examples"
git push
```

---

## 📚 How to study this file

1. **Read the comments** (lines starting with `#`). They explain *what*, *why*, *when*, and *common mistakes* for each operator.
2. **Run the file** and match the printed output to the code.
3. **Change a value** and re-run to see what happens. Breaking things on purpose is a great way to learn. 💡
4. Keep the **cheat-sheet** at the bottom of the file open for quick reference.

---

## 🧠 Top beginner mistakes (also in the file)

1. `=` **assigns**, `==` **compares** — mixing them is the #1 bug.
2. `/` always gives a decimal (float); use `//` for whole-number division.
3. Never divide by zero — check the divisor first.
4. Use `==` for values; use `is` only for `None`, `True`, `False`.
5. `&` is **bitwise**, `and` is **logical** — they are different.
6. When precedence is unclear, add parentheses. Always.

---

## 🗺️ Operator cheat-sheet

```text
ARITHMETIC : +  -  *  /  //  %  **
COMPARISON : ==  !=  >  <  >=  <=
ASSIGNMENT : =  +=  -=  *=  /=  //=  %=  **=   (& | ^ << >> variants too)
LOGICAL    : and  or  not
MEMBERSHIP : in  not in
IDENTITY   : is  is not
BITWISE    : &  |  ^  ~  <<  >>
SPECIAL    : :=  (walrus)   @ (matmul)   * ** (unpack)   x if c else y (ternary)
```

---

Happy learning! ⭐ Star the repo if it helped you understand operators..