import pandas as pd
from  main import Scraper
# Define a list of product names to search for
products = ["rtx 4060", "pantalla 4k", "ram ddr5"]

# Create a dictionary to store the results of each search
results = []
bestseller=[]
# Loop through each product in the list and search for it on a search engine
for index,product in enumerate(products):
    print(product)
    print(index)
    s2=Scraper()
    s2.menu(mode="Argentina")
    s2.scraping(product=product)
    s2.export_to_csv()

    df = pd.read_csv("/workspaces/trading-bots/MercadoLibre-Scraper/data/mercadolibre_scraped_data.csv",delimiter=';')

    # Extract the column containing the buyer information (e.g., email address)
    
    results.append(df[['seller','post link']])
    #print(results)
    # Create a dictionary to keep track of how many products each buyer has
    product_counts = {}
    optionseller=[]
    
    # Check if 'title' is in df.columns before iterating over rows
    if index>0:
        set1 = set(list(results[index-1]['seller'],results[index-1]['post link']))
        set2 = set(list(results[index]['seller'],results[index]['post link']))
        print(set1)
        print(set2)
        # Encontrar la intersección de los dos conjuntos
        interseccion = set1 & set2

        # Convertir la intersección a una lista
        bestseller = list(interseccion)
        print("bestseller:  ",bestseller)

print(bestseller)
'''
for product in products:
    if product in results: print(results[product])
print(*[results[i] for i in results])
'''