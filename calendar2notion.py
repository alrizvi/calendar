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
