import csv

entry = ["fermi_swift_grb_catalog.csv", "Fermi and Swift GRB combined catalog", 
         "data/registry/fermi_swift_grb_catalog_schema.yaml", "True"]

with open("data/registry/Bruno_Engine_Registry.csv", "a", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(entry)

print("✅ Entry added to registry.")
