# Z podanego zbioru danych wyselekcjonuj 5 o największej wartości na jednostkę, znając kategorię obiektu
# Dane znajdują się w folderze "dane" w pliku "zbiór_wejściowy.json" oraz "kategorie.json"
# Wynik przedstaw w czytelnej formie na standardowym wyjściu

import json
from typing import Literal

CARAT_TO_OUNCE_RATIO = 0.00705479239  # 1 ct = 0.00705479239 uncji
GRAM_TO_OUNCE_RATIO = 0.03527396190   # 1 g  = 0.03527396190 uncji

def convertToOunces(unit: Literal['carat', 'gram'], amount: float) -> float:
  match unit:
    case 'carat':
      return amount * CARAT_TO_OUNCE_RATIO
    case 'gram':
      return amount * GRAM_TO_OUNCE_RATIO
    
def getEntryValue(_type: str, purity: str, categories) -> int:
  for entry in categories:
    if entry['Typ'] == _type and entry['Czystość'] == purity:
      return int(entry['Wartość za uncję (USD)'])
    else:
      continue
  return 0

def main() -> None:
  with open('./dane/zbiór_wejściowy.json', 'r', encoding='utf-8') as data_file:
    data = json.load(data_file)
  
  with open('./dane/kategorie.json', 'r', encoding='utf-8') as categories_file:
    categories = json.load(categories_file)

  top_5_entries = []
  entry_value_pairs = []

  for entry in data:
    _type = entry['Typ']
    purity = entry['Czystość']
    mass = entry['Masa'].replace(',', '.')
    amount = 0
    if mass.endswith('g'):
      amount = convertToOunces('gram', float(mass[:-1]))
    else:
      amount = convertToOunces('carat', float(mass[:-2]))
    value = round(getEntryValue(_type, purity, categories) * amount, 2)
    if (value != 0):
      entry_value_pairs.append([entry, value])

  while(len(entry_value_pairs) > 0):
    if (len(top_5_entries) < 5):      
      max_entry = max(entry_value_pairs, key=(lambda predicate : predicate[1]))
      top_5_entries.append(max_entry)
      index = entry_value_pairs.index(max_entry)
      entry_value_pairs.pop(index)
    else:
      break


  for i in range(len(top_5_entries)):
    print(f"{i+1}. {top_5_entries[i][0]['Typ']} {top_5_entries[i][0]['Masa']} {top_5_entries[i][0]['Czystość']} {top_5_entries[i][1]} USD")

if __name__ == '__main__':
  main()