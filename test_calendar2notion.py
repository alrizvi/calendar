import pytest
from calendar2notion import ics_to_csv

def test_ics_to_csv():
    # Configura los datos de prueba
    ics_file = 'basic.ics'
    csv_file = 'tareas.csv'

    # Llama a la función
    ics_to_csv(ics_file, csv_file)

    # Verifica que el archivo CSV se haya creado y contiene los datos esperados
    with open(csv_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        assert len(lines) > 1  # Verifica que no esté vacío
