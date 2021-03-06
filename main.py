import csv

rows = []

with open("data.csv", "r", encoding="UTF-8") as f:
  reader = csv.reader(f)

  for row in reader:
    rows.append(row)

headers = rows[0]
planet_data_rows = rows[1:]
headers[0] = "row_num"
headers.append("Gravity")

gravity = []

for planet_data in planet_data_rows: 
  mass = planet_data[3]
  radius = planet_data[4]
  
  if mass:
    planet_data[3] = float(mass) * 1.989e+30

  if radius:
    planet_data[4] = float(radius) * 6.957e+8

  if mass and radius:
    gravity = 6.674e-11 * (float(mass) / (float(radius) * float(radius)))
    planet_data.append(gravity)

with open("final.csv", "w", newline="", encoding="utf-8") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data_rows)
