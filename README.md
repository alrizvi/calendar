# Calendar to Notion CSV Converter

This script converts events from an `.ics` calendar file to a CSV file. It reads the `.ics` file, extracts event details, and writes them to a CSV file.

## Requirements

- Python 3.x
- `icalendar` library

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/).
2. Install the `icalendar` library using pip:

    ```sh
    pip install icalendar
    ```

## Usage

1. Place your `.ics` file in the same directory as the script.
2. Run the script:

    ```sh
    python calendar2notion.py
    ```

3. The script will read the `basic.ics` file and export the events to `tareas.csv`.

## Example

The script reads events from `basic.ics` and writes them to `tareas.csv` with the following columns:

- Summary
- Start Date
- End Date
- Description
- Location

## Code

```python
import csv
from icalendar import Calendar

def ics_to_csv(ics_file, csv_file):
    # Leer archivo .ics
    with open(ics_file, 'r', encoding='utf-8') as file:
        calendar = Calendar.from_ical(file.read())

    # Crear lista de eventos
    events = []
    for component in calendar.walk():
        if component.name == "VEVENT":
            event = {
                'Summary': component.get('summary', 'No Title'),
                'Start Date': component.get('dtstart').dt,
                'End Date': component.get('dtend').dt if component.get('dtend') else None,
                'Description': component.get('description', ''),
                'Location': component.get('location', '')
            }
            events.append(event)

    # Guardar como CSV
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Summary', 'Start Date', 'End Date', 'Description', 'Location'])
        writer.writeheader()
        writer.writerows(events)

    print(f"Eventos exportados a {csv_file}")

# Uso
ics_to_csv('basic.ics', 'tareas.csv')