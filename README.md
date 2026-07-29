<div align="center">

```
██████╗  █████╗ ████████╗ █████╗ 
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
██║  ██║███████║   ██║   ███████║
██║  ██║██╔══██║   ██║   ██╔══██║
██████╔╝██║  ██║   ██║   ██║  ██║
╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝

 █████╗ ███╗   ██╗ █████╗ ██╗  ██╗   ██╗███████╗███████╗██████╗ 
██╔══██╗████╗  ██║██╔══██╗██║  ╚██╗ ██╔╝╚══███╔╝██╔════╝██╔══██╗
███████║██╔██╗ ██║███████║██║   ╚████╔╝   ███╔╝ █████╗  ██████╔╝
██╔══██║██║╚██╗██║██╔══██║██║    ╚██╔╝   ███╔╝  ██╔══╝  ██╔══██╗
██║  ██║██║ ╚████║██║  ██║███████╗██║   ███████╗███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝

████████╗██████╗  █████╗ ███╗   ██╗███████╗███████╗ ██████╗ ██████╗ ███╗   ███╗███████╗██████╗ 
╚══██╔══╝██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔════╝██╔═══██╗██╔══██╗████╗ ████║██╔════╝██╔══██╗
   ██║   ██████╔╝███████║██╔██╗ ██║███████╗█████╗  ██║   ██║██████╔╝██╔████╔██║█████╗  ██████╔╝
   ██║   ██╔══██╗██╔══██║██║╚██╗██║╚════██║██╔══╝  ██║   ██║██╔══██╗██║╚██╔╝██║██╔══╝  ██╔══██╗
   ██║   ██║  ██║██║  ██║██║ ╚████║███████║██║     ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗██║  ██║
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
```

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=20&duration=2200&pause=500&color=E76F51&center=true&vCenter=true&multiline=true&repeat=true&width=780&height=100&lines=Data+Analyzer+and+Transformer+Program;Functions+%E2%80%A2+Recursion+%E2%80%A2+Lambda+%E2%80%A2+*args+%E2%80%A2+**kwargs;Built-in+Functions+%E2%80%A2+Sorting+%E2%80%A2+Filtering;Built+for+Red+%26+White+Skill+Education)](https://git.io/typing-svg)

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)
![Libraries](https://img.shields.io/badge/External_Libraries-None_Required-black?style=for-the-badge)
![Assignment](https://img.shields.io/badge/Assignment-Data_Analyzer_%26_Transformer-E76F51?style=for-the-badge)

</div>

## 🧭 Table of Contents

[Overview](#-project-overview) • [Objective](#-objective) • [Data Storage](#-data-storage) • [Functions](#-functions-overview) • [Features](#-features) • [Flow](#-program-flow) • [Example Output](#-example-output) • [Skills](#-skills-demonstrated) • [Known Behaviors](#-known-behaviors--notes) • [Getting Started](#-getting-started) • [Structure](#-project-structure) • [Tech Stack](#-tech-stack) • [Author](#-author) • [Full Code](#-full-source-code)

---

## 📌 Project Overview

**Data Analyzer and Transformer** is a menu-driven Python console program that lets a user load a 1D array or a simple 2D matrix, then run analysis and transformation operations on it — summary statistics, a recursive factorial calculator, threshold filtering with a `lambda`, ascending/descending sorting, and a multi-value statistics report built with `*args`/`**kwargs`.

Every operation lives in its own function with a proper docstring, and the main loop simply reads the user's choice, prints that function's documentation, and calls it — a clean demonstration of writing modular, well-documented Python.

<div align="center">

| 🔢 1D Array | 🧮 2D Matrix | 🔁 Recursion | 🧬 Lambda | 📦 \*args / \*\*kwargs |
|:---:|:---:|:---:|:---:|:---:|
| flat list of numbers | 2 rows of numbers | factorial | filter by threshold | flexible function calls |

</div>

> Built for **Data Analyzer and Transformer — Red & White Skill Education.**
> *"Quality is our Motto."*

---

## 🎯 Objective

Create a Python program called **Data Analyzer and Transformer** that manages 1D and 2D numeric datasets, applying:

- User-defined functions with docstrings
- Built-in functions — `len()`, `min()`, `max()`, `sum()`
- Recursion (factorial calculation)
- A `lambda` function combined with `filter()`
- Sorting with `.sort()` (in-place) and `sorted()` (returns a new list)
- Functions that **return multiple values** via tuple unpacking
- `*args` and `**kwargs` in function signatures
- Type casting (`int()` on user input) and `match` / `case` menu routing

---

## 🗂️ Data Storage

Two **global lists** hold all program data:

```python
array_1d = []   # e.g. [4, 8, 15, 16, 23, 42]
array_2d = []   # e.g. [[4, 8, 15], [16, 23, 42]]  → always exactly 2 rows
```

`array_1d` is a flat list of integers. `array_2d` is a **list of two lists** (`[row1, row2]`), so it behaves like a simple 2-row matrix. Every analysis function that needs "all 2D values" combines the rows with `array_2d[0] + array_2d[1]`.

---

## 🧩 Functions Overview

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=16&pause=600&color=2A9D8F&center=true&vCenter=true&width=750&lines=match+menu_choice%3A;case+1%3A+%E2%86%92+input_data();case+2%3A+%E2%86%92+display_data();case+3%3A+%E2%86%92+find_factorial();case+4%3A+%E2%86%92+filter_data();case+5%3A+%E2%86%92+sort_data();case+6%3A+%E2%86%92+display_multipledata()+%2B+print_summary_kwargs();case+7%3A+%E2%86%92+break" alt="Match Case Typing SVG" />

</div>

| Function | Concept it demonstrates | What it does |
|---|---|---|
| `input_data()` | Global variables, type casting | Asks for 1D or 2D, reads space-separated numbers, casts them with `map(int, ...)`, stores them in `array_1d` or `array_2d` |
| `display_data()` | Built-in functions | Prints element count, min, max, sum, and average — for `array_1d`, and for the combined 2D rows if present |
| `find_factorial(factorial)` | Recursion | Calls itself with `factorial - 1` until it hits the `0`/`1` base case |
| `filter_data()` | `lambda` + `filter()` | Asks for a threshold, then filters 1D or 2D data down to values `>= threshold` |
| `sort_data()` | `.sort()` vs `sorted()`, `match`/`case` | Sorts `array_1d` in place, or sorts each row of `array_2d` with a list comprehension, ascending or descending |
| `display_multipledata(*args)` | Returning multiple values, `*args` | Computes min/max/sum/average for 1D or 2D data and `return`s all four at once |
| `print_summary_kwargs(**kwargs)` | `**kwargs` | Takes the four stats as keyword arguments and prints them in a formatted report |

---

## ✨ Features

- Numbered **7-option main menu** that loops until the user exits
- Prints each function's **docstring** before running it, right from `function.__doc__`
- **Input Data:** load a 1D array or a 2-row 2D matrix
- **Display Data Summary:** count, min, max, sum, average — for 1D and combined 2D data
- **Calculate Factorial:** recursive factorial of any non-negative integer, with a guard against negative input
- **Filter Data by Threshold:** keep only values greater than or equal to a chosen threshold, using `filter()` + `lambda`
- **Sort Data:** ascending or descending, for either the 1D array or every row of the 2D matrix
- **Display Dataset Statistics:** one call returns four stats at once, another prints them from `**kwargs`
- **Exit Program:** clean goodbye message and loop `break`
- Falls back to a friendly *"Enter numbers 1 to 7"* message on an invalid menu choice

---

## 🌊 Program Flow

<details open>
<summary><b>Click to collapse / expand the flow diagram</b></summary>

```mermaid
flowchart TD
    A([▶ Program Starts]) --> B[📋 Main Menu Is Shown]
    B --> C{match menu_choice}
    C -->|1| D["input_data()\nload 1D / 2D data"]
    C -->|2| E["display_data()\nstats via built-ins"]
    C -->|3| F["find_factorial()\nrecursion"]
    C -->|4| G["filter_data()\nlambda + filter()"]
    C -->|5| H["sort_data()\n.sort() / sorted()"]
    C -->|6| I["display_multipledata()\n→ print_summary_kwargs()"]
    C -->|7| J([👋 Print goodbye & break])
    C -->|case _| K["Invalid choice message"]
    D --> B
    E --> B
    F --> B
    G --> B
    H --> B
    I --> B
    K --> B

    style A fill:#0f2027,stroke:#E76F51,color:#fff
    style J fill:#0f2027,stroke:#E76F51,color:#fff
    style B fill:#264653,stroke:#0f2027,color:#fff
    style C fill:#E9C46A,stroke:#b38f2e,color:#222
    style D fill:#16323f,stroke:#2A9D8F,color:#fff
    style E fill:#16323f,stroke:#2A9D8F,color:#fff
    style F fill:#16323f,stroke:#2A9D8F,color:#fff
    style G fill:#16323f,stroke:#2A9D8F,color:#fff
    style H fill:#16323f,stroke:#2A9D8F,color:#fff
    style I fill:#16323f,stroke:#2A9D8F,color:#fff
    style K fill:#16323f,stroke:#E76F51,color:#fff
```

</details>

| Step | Stage | Description |
|:---:|---|---|
| 1 | **Show Menu** | Print the seven menu options |
| 2 | **Take Choice** | Read the user's number and route it with `match menu_choice:` |
| 3 | **Print Docstring** | `print("Documantation : ", <function>.__doc__)` runs first |
| 4 | **Call Function** | The matching function executes |
| 5 | **Repeat** | Loop back to Step 1 unless the user chose `7` (Exit) |

---

## 🎬 Example Output

<details open>
<summary><b>▶ Input Data + Display Summary</b></summary>

```
Welcome to the Data Analyzer and Transformer Program

Main Menu:
1. Input Data (1D & 2D)
2. Display Data Summary (Built-in Functions)
3. Calculate Factorial (Recursion)
4. Filter Data by Threshold (Lambda Function)
5. Sort Data
6. Display Dataset Statistics (Return Multiple Values)
7. Exit Program

Please enter your choice: 1
Documantation :  Inputs data for 1D and 2D arrays.
1. 1D array
2. 2D array
Choice the number: 1
Enter data for a 1D array (separated by spaces) : 4 8 15 16 23 42
1D Array: [4, 8, 15, 16, 23, 42]

Please enter your choice: 2
Documantation :  Displays data summary using built-in functions.
--- 1D Data Summary ---
- Total elements:  6
- Minimum value:  4
- Maximum value:  42
- Sum of all values:  108
- Average value:  18.0
First input 2D array.
```

</details>

<details open>
<summary><b>▶ Factorial, Filter, Sort & Multi-Stat Report</b></summary>

```
Please enter your choice: 3
Documantation :  Calculates factorial using recursion.
Enter a number to calculate its factorial: 5
Factorial of 5 is: 120

Please enter your choice: 4
Documantation :  None
Select Option:
1. 1D array
2. 2D array
Select your Option : 1
Enter a threshold value to filter out data above this value: 15
Filtered Data (values >= 15):
[16, 23, 42]

Please enter your choice: 5
Documantation :  None
Select Option:
1. 1D sort array
2. 2D sort array
Select your Option : 1
Choose sorting option:
1. Ascending
2. Descending
Enter your choice: 2
Sorted Data: [42, 23, 16, 15, 8, 4]

Please enter your choice: 6
Documantation :  None
Select Option:
1. 1D  display array
2. 2D display array
Select your Option : 1
Dataset Statistics:
- Minimum value: 4
- Maximum value: 42
- Sum of all values: 108
- Average value: 18.0

Please enter your choice: 7
Thank you for using the Data Analyzer and Transformer Program. Goodbye!
```

</details>

---

## 🎯 Skills Demonstrated

<div align="center">

![Functions](https://img.shields.io/badge/User_Defined_Functions-████████████-E76F51?style=flat-square)
![Recursion](https://img.shields.io/badge/Recursion-███████████-E76F51?style=flat-square)
![Lambda](https://img.shields.io/badge/Lambda_%2B_filter()-██████████-E76F51?style=flat-square)
![Args Kwargs](https://img.shields.io/badge/*args_%2F_**kwargs-███████████-E76F51?style=flat-square)
![Match Case](https://img.shields.io/badge/match_%2F_case-███████████-E76F51?style=flat-square)
![Builtins](https://img.shields.io/badge/Built--in_Functions-████████████-E76F51?style=flat-square)

</div>

- Splitting a program into small, well-documented, single-purpose functions
- Using recursion instead of a loop to compute a factorial
- Combining `lambda` with `filter()` to select data by condition
- Comparing in-place sorting (`list.sort()`) with the non-mutating `sorted()`
- Returning several values from one function and unpacking them into separate variables
- Accepting flexible arguments with `*args` and flexible keyword arguments with `**kwargs`
- Reading a function's own documentation at runtime via `__doc__`

---

## 📝 Known Behaviors & Notes

A few honest notes for anyone reading or grading this code:

- **Docstrings that don't count as docstrings:** In `filter_data()`, `sort_data()`, and `display_multipledata()`, the `"""..."""` description is written *after* other statements (or nested inside an `if`/`case` block) instead of being the very first line in the function body. Python only treats a string literal as a function's real docstring when it's the first statement, so `filter_data.__doc__`, `sort_data.__doc__`, and `display_multipledata.__doc__` all print `None` at runtime — only `input_data()`, `display_data()`, `find_factorial()`, and `print_summary_kwargs()` have properly positioned docstrings.
- **Name shadowing in `display_multipledata()`:** its local variable `display_data` (the user's 1D/2D choice) shares its name with the global `display_data()` function. This doesn't crash anything since it's local to that function, but it does hide the outer function's name for the rest of that call.
- **Unused `*args`:** `display_multipledata(*args)` declares a variadic parameter it never reads — it works fine because it's always called with no arguments, but `*args` here is currently just syntax, not functionality.
- **No input validation:** menu numbers, array values, and thresholds are all cast straight through `int()`. Non-numeric input will raise a `ValueError` and stop the program rather than showing a friendly error.
- **2D data is fixed at 2 rows:** `input_data()` only ever collects exactly `row1` and `row2` — there's no current option to load a matrix with more (or fewer) rows.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+ (for `match` / `case` support)
- No external libraries required

### Installation

```bash
git clone https://github.com/anghanshrey/data-analyzer-transformer.git
cd data-analyzer-transformer
```

### Usage

```bash
python data_analyzer_transformer.py
```

When it runs, type:
- `1` to input a 1D or 2D dataset
- `2` to view a data summary
- `3` to calculate a factorial
- `4` to filter data by a threshold
- `5` to sort your data
- `6` to view multi-value dataset statistics
- `7` to exit the program

---

## 📁 Project Structure

```
data-analyzer-transformer/
├── data_analyzer_transformer.py   # Main script
└── README.md                      # Project documentation
```

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Concepts demonstrated:** user-defined functions & docstrings, `while` loop, `match`/`case`, recursion, `lambda`, `filter()`, `.sort()` / `sorted()`, `*args`, `**kwargs`, type casting, returning multiple values

---

## 👤 Author

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&pause=1000&color=E76F51&center=true&vCenter=true&width=500&lines=Made+by+Shrey+Anghan;Red+%26+White+Skill+Education;Quality+is+our+Motto." alt="Author Typing SVG" />

**Shrey Anghan**
🎓 Red & White Skill Education — *Shaping skills for scaling higher...!!!*
🔗 GitHub: [@anghanshrey](https://github.com/anghanshrey)

![Profile Views](https://komarev.com/ghpvc/?username=anghanshrey&label=Profile%20Views&color=E76F51&style=flat)
![GitHub followers](https://img.shields.io/github/followers/anghanshrey?label=Follow&style=social)

</div>
