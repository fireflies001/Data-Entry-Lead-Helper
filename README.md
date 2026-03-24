# Lead Helper

Lead Helper is a small desktop app built with PySide6 to speed up lead processing from CSV files. It lets you upload a CSV, normalize address data, review records in a table, fill in number values, and copy the final number column for pasting into Google Sheets.

## Features

- Upload CSV files from the desktop app
- Transform uploaded lead data into a table view
- Edit the `Number` column directly in the table
- Click cells to copy useful values
- Copy all numbers at once for quick Google Sheets pasting
- Run as a lightweight desktop workflow tool

## Tech Stack

- Python
- PySide6
- Qt Stylesheets (`.qss`)

## Project Structure

```text
app.py
components/
pages/
mainTable/
style/
```

## Getting Started

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install PySide6
```

3. Run the app:

```bash
python app.py
```

## Packaging

Example PyInstaller command for Windows:

```powershell
.\myvenv\Scripts\python -m PyInstaller --windowed --onefile --name "Lead Helper" --add-data "style/main.qss;style" app.py
```

## What It Does

The app is designed for a simple workflow:

1. Upload a CSV file.
2. Process owner and address fields into a table-friendly format.
3. Enter or update number values in the table.
4. Copy the full number column for use in Google Sheets or other tools.

## Notes

This project was built as a practical PySide6 desktop app for learning reusable components, page-based UI structure, CSV processing, and packaging Python applications for end users.
