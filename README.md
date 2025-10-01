# Sourdough Tracker

A simple command-line tool to help bakers track and manage their sourdough starter feedings.
It calculates discard targets, flour and water amounts, and logs each feeding in an Excel file for easy review.

Built with **Python**, **argparse**, and **openpyxl**.

This is my first real Python project. Hope you enjoy it. ;)

---

## Features

* Configure your jar weight, keep target, and feeding ratio once (`init`).
* Log each feeding with jar weight, smell notes, peak hours, and more (`feed`).
* Automatically calculates discard target and flour/water amounts.
* Saves all feedings in an Excel spreadsheet (`starter_log.xlsx`).
* Review your recent feedings with a simple stats command (`stats`).

---

## Installation

Clone the repo and install locally:

```bash
git clone https://github.com/<your-username>/sourdough-tracker.git
cd sourdough-tracker
pip install .
```

This installs the CLI tool globally as `starter`.

---

## Usage

### 1. Initialize

Set up your starter config and create the Excel log file:

```bash
starter init --jar-weight 350 --keep-target 50 --ratio 1:2:2
```

* **jar-weight**: empty jar weight in grams
* **keep-target**: how much starter to keep after discarding
* **ratio**: feeding ratio (starter\:flour\:water), default `1:2:2`

---

### 2. Log a feeding

Weigh your jar and log a feeding:

```bash
starter feed --weight 450 --smell fruity --peak-hours 6 --notes "bubbly and doubled in size"
```

Example output:

```
Target jar weight: 400
Add flour and water: (100, 100)
Logged feeding on 2025-09-18
```

This also appends a new row to `starter_log.xlsx`.

---

### 3. Review stats

View the last 5 feedings:

```bash
starter stats
```

Example output:

```
Date: 2025-09-17
Jar Weight Total: 450
Starter Weight: 100
Target Weight: 400
Flour (calc): 100
Water (calc): 100
Smell: fruity
Peak Hours: 6
Notes: bubbly and doubled in size
---
```

---

## Project Structure

```
sourdough-tracker/
├── src/
│   └── sourdough_tracker/
│       ├── __init__.py
│       └── commands.py
│       └── main.py
├── pyproject.toml
├── LICENSE
├── README.md
```
