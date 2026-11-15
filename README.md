# Number Guessing Game (PS No. 4)

A beginner-friendly Python 3 console game based on the Rungta International Skills University project statement.

## Features
- Computer selects a random integer from 1 to 100.
- Player gets 5 valid attempts.
- Shows `Too low` / `Too high` hints.
- Rejects non-integer and out-of-range input without using an attempt.
- Displays attempts used and asks `Play again? (y/n)`.

## Requirements
- Python 3.8 or newer (no third-party packages required).

## Run
1. Open a terminal in this folder.
2. Run:

   ```bash
   python number_guessing_game.py
   ```

   On some Windows systems, use `py number_guessing_game.py`.

## Test with the fixed number 42
For the assignment test cases, temporarily change the `main()` line `play_game()` to `play_game(secret_number=42)`. Run the program, enter the test guesses, and then restore `play_game()` for normal random gameplay. The optional argument exists only to make testing repeatable.

## Test cases
1. Secret 42; guess 42 -> win in 1 attempt.
2. Secret 42; guesses 1, 100 -> Too low (4 left), Too high (3 left).
3. Secret 42; enter `abc`, then `150` -> invalid whole-number message, then out-of-range message; neither uses an attempt. Attempts left remain 5.
4. Secret 42; guesses 10, 90, 50, 30, 20 -> Too low, Too high, Too high, Too low, Too low; game over and reveal 42.

## Files
- `number_guessing_game.py` — complete source code
- `Project_Report.docx` / `Project_Report.pdf` — project documentation
- `algorithm.txt` — step-by-step algorithm
- `flowchart.mmd` — Mermaid flowchart source
- `test_cases.txt` — test plan and expected results
