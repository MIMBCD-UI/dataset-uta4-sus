#!/usr/bin/env python

"""demo.py: a small and simple demo for this dataset."""

__author__      = "Francisco Maria Calisto"
__maintainer__  = "Francisco Maria Calisto"
__email__       = "francisco.calisto@tecnico.ulisboa.pt"
__license__     = "ACADEMIC & COMMERCIAL"
__version__     = "0.1.0"
__status__      = "Production"
__copyright__   = "Copyright 2020, Instituto Superior Técnico (IST)"
__credits__     = [
	"Hugo Lencastre",
	"Nádia Mourão",
	"Bruno Dias",
	"Luís Ribeiro Gomes",
	"Bruno Oliveira",
  "Carlos Santiago",
  "Jacinto C. Nascimento",
  "Pedro Miraldo",
  "Nuno Nunes"
]

import csv
with open('dataset/main_sheet_sus.csv', 'r') as file:
  reader = csv.reader(file)
  for row in reader:
    print(row)

# ==================== END File ==================== #