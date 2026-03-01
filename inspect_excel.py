import openpyxl
import pandas as pd

# Leer el archivo
excel_file = r'c:\Users\famia\Downloads\WAGE\Wage11.xlsx'

# Con openpyxl para ver estructura
wb = openpyxl.load_workbook(excel_file)
print("=" * 60)
print("INFORMACIÓN DEL ARCHIVO EXCEL")
print("=" * 60)
print(f"Hojas disponibles: {wb.sheetnames}")
ws = wb.active
print(f"Hoja activa: {ws.title}")
print(f"Dimensiones: {ws.dimensions}")

# Con pandas para ver datos
df = pd.read_excel(excel_file, sheet_name=0)
print("\n" + "=" * 60)
print("ESTRUCTURA DE DATOS")
print("=" * 60)
print(f"Forma del dataset: {df.shape}")
print(f"\nColumnas: {list(df.columns)}")
print(f"\nTipos de datos:\n{df.dtypes}")

print("\n" + "=" * 60)
print("PRIMERAS 5 FILAS")
print("=" * 60)
print(df.head())

print("\n" + "=" * 60)
print("ESTADÍSTICAS BÁSICAS")
print("=" * 60)
print(df.describe())
