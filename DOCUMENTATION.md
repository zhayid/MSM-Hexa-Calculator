# MSM Hexa Calculator - Project Documentation

## Project Need

This project addresses the need for a tool to calculate and validate **Hexa stat probabilities** in the game **MapleStory M (MSM)**. Players need a reliable way to determine the probability of achieving desired Hexa stat combinations given their current stat values, helping them make informed decisions about their progression.

---

## Problem Statement
build a python backend that takes 
TARGET_MAIN, TARGET_SUB, CURRENT_MAIN, CURRENT_SUB_1 
and CURRENT_SUB_2 in a python function and returns a probability

build a html that has TARGET_MAIN, TARGET_SUB, CURRENT_MAIN, CURRENT_SUB_1 
and CURRENT_SUB_2  as input and probability as output\

TARGET_MAIN, TARGET_SUB, CURRENT_MAIN, CURRENT_SUB_1 
and CURRENT_SUB_2 need to be int
---

## Inputs

| Field | Minimum Value | Description |
|-------|--------------|-------------|
| `TARGET_MAIN` | 7 | The desired main stat target |
| `TARGET_SUB` | 9 | The desired sub stat target |
| `CURRENT_MAIN` | 3 | The player's current main stat |
| `CURRENT_SUB_1` | - | The player's first current sub stat |
| `CURRENT_SUB_2` | - | The player's second current sub stat |

---

## Output

- A **probability percentage** representing how close the current stats are to the target values.

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Frontend | HTML, JavaScript |
| Backend | Python (Flask) |
| API | REST (JSON) |
| CORS | flask-cors |

---

## How to Run

1. Install dependencies:
   ```bash
   pip install flask flask-cors
   ```

2. Start the backend:
   ```bash
   python app.py
   ```

3. Open `index.html` in a browser and enter your Hexa stat values.

---

## Future Improvements

- Add support for more complex probability formulas specific to MSM game mechanics
- Improve the UI with stat breakdowns and visual feedback
- Deploy as a hosted web app for easy community access
