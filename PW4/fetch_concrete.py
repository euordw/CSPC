import os
import pandas as pd
from ucimlrepo import fetch_ucirepo

# Fetch Concrete Compressive Strength dataset (UCI ID = 165)
concrete = fetch_ucirepo(id=165)

X = concrete.data.features.copy()
y = concrete.data.targets.iloc[:, 0].rename("strength")

# Rename columns to standardized short names
X.columns = [
    "cement", "slag", "ash", "water", 
    "superplastic", "coarse_agg", "fine_agg", "age"
]

# Ensure output directory exists
os.makedirs("data", exist_ok=True)

# Combine and save to CSV
df = X.assign(strength=y)
df.to_csv("data/concrete.csv", index=False)
print("SUCCESS: data/concrete.csv saved successfully!")