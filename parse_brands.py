#find a parser
#loop thorugh the list and within each dictionary, grab the id, name, slug, and image
#create a csv
#create headers
#store in csv
import json
import csv

with open('all_brands.txt') as f:
    brands = json.load(f)

csv_file = 'brands.csv'

with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['id','name','slug','image'])
    writer.writeheader()

    for brand in brands:
        writer.writerow({
            'id': brand.get('id',''),
            'name':
        })

print(f"Data written to {csv_file}")
