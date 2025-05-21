import numpy as np
from datetime import datetime as dt
from numpy.lib import recfunctions

np.random.seed(42)
rows = 50
array_structure = [
    ('date', 'U10'), 
    ('price', 'i4'), 
    ('category', 'U8')
]

dates = np.arange('2023-01-01', '2023-04-30', dtype=np.datetime64)
random_dates = np.random.choice(dates, rows)

# Generate random prices (3-digit integers)
prices = np.random.randint(1, 999, rows)

# Generate categories with specified probabilities
categories = np.random.choice(['food', 'clothes', 'tech'], rows, p=[0.5, 0.3, 0.2])

# Create structured array
purchases = np.empty(rows, dtype=array_structure)

# Fill the array
purchases['date'] = random_dates.astype(str)
purchases['price'] = prices
purchases['category'] = categories

# Convert to 2D array view (if needed)
purchases = purchases[purchases[:]["date"].argsort()]

revenue_per_month = {}

for i in purchases:
    month = dt.strptime(i["date"], "%Y-%m-%d").month

    if not month in revenue_per_month:
        revenue_per_month[month] = 0
    
    revenue_per_month[month] += int(i["price"])

# ---[TESTING FIELD]---
print(recfunctions.structured_to_unstructured(purchases))
print(revenue_per_month)

# ---[TESTING FIELD]---

