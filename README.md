# 📊 Operational Research Project

This project explores two optimization problems modeled and solved using **Gurobi** in **Python**, aiming to minimize total production time under different constraints and sequencing requirements.

---

## 🏭 Problem 1: Optimal Scheduling of Paint Shades

A factory produces five special paint shades (labeled 1 through 5) for key customers. The demand for each shade is stable and the shades are produced weekly.

### 🧪 Problem Description

- Each shade is produced by a dedicated mixing machine that **must be cleaned** before switching to a different shade.
- Mixing durations (in minutes) for shades 1 to 5 are:  
  `40, 35, 45, 32, 50` respectively.
- Cleaning times between shades depend on the transition and are given by the following table:

| From \ To | 1  | 2  | 3  | 4  | 5  |
|-----------|----|----|----|----|----|
| **1**     | 0  | 11 | 7  | 13 | 11 |
| **2**     | 5  | 0  | 13 | 15 | 15 |
| **3**     | 13 | 15 | 0  | 23 | 11 |
| **4**     | 9  | 13 | 5  | 0  | 3  |
| **5**     | 3  | 7  | 7  | 7  | 0  |

> Note: The machine **must also be cleaned between the last and the first shades** of each weekly cycle.

### 🎯 Objective

Find the optimal production order of the five shades that **minimizes the total time** (mixing + cleaning). This order will repeat weekly.

---

## 🎨 Problem 2: Wallpaper Coloring with Sequencing Constraints

The factory must color three types of wallpaper designs: **T1**, **T2**, and **T3**, each requiring a specific sequence of color applications.

### 🧪 Wallpaper Details

- **T1**: Blue background → Yellow patterns  
- **T2**: Green background → Blue designs → Yellow designs  
- **T3**: Yellow background → Blue designs → Green designs  

Each color is applied by a **dedicated machine** (Blue, Green, Yellow), and:
- Each machine can process only one wallpaper at a time.
- A wallpaper can only be worked on by **one machine at a time** (no parallel color application).

### 🕒 Processing Times (in minutes)

| Machine | Color  | T1 | T2 | T3 |
|---------|--------|----|----|----|
| M1      | Blue   | 45 | 20 | 12 |
| M2      | Green  |    | 10 | 17 |
| M3      | Yellow | 10 | 34 | 28 |

### 🎯 Objective

Determine the optimal coloring schedule that **minimizes the total production time** for all three wallpapers, considering:
- Task sequences per wallpaper
- Machine availability and exclusivity

---

## 🧰 Tools & Technologies

- **Language**: Python  
- **Solver**: [Gurobi Optimizer](https://www.gurobi.com/)  
- **Modeling**: Linear/Integer Programming

---

## 🚀 How to Run

Make sure you have Python and Gurobi installed.

```bash
pip install gurobipy
python problem1_factory_paint_scheduling.py
python problem2_wallpaper_coloring_schedule.py
```

> This project explores **theoretical and algorithmic aspects of combinatorial optimization**, applying both **analytical modeling** and **computational tools** to solve real-world scheduling and sequencing problems efficiently using modern solvers like **Gurobi**.
