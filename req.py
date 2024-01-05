import pandas as pd
from  main import Scraper
# Define a list of product names to search for
products = ["rtx 4060", "pantalla 4k", "macbook pro"]

# Create a dictionary to store the results of each search
results = {}

# Loop through each product in the list and search for it on a search engine
for product in products:
    print(product)
    s2=Scraper()
    s2.menu(mode="Argentina")
    s2.scraping(product=product)
    s2.export_to_csv()

    df = pd.read_csv("/workspaces/trading-bots/MercadoLibre-Scraper/data/mercadolibre_scraped_data.csv",delimiter='|')

    # Extract the column containing the buyer information (e.g., email address)
    buyer_col = 'seller'

    # Create a dictionary to keep track of how many products each buyer has
    product_counts = {}
    for index, row in df.iterrows():
        # Convert all products into a set to remove duplicates
        for product in set(row['title'].split(' ')):
            if product not in product_counts:
                product_counts[product] = {buyer: 1 for buyer in row.index.tolist()}
            # Iterate through each buyer in the current row and add their corresponding quantity to the dictionary
            print("hey")
            for buyer in row.index.tolist():
                product_counts[product][buyer] += int(row[f'Quantity_{buyer}'])
for product in products:
    if product in results: print(results[product])
print(*[results[i] for i in results]) 