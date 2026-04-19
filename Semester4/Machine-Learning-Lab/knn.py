import pandas as pd
import numpy as np
import math

dataset={
    "Customer":['C1','C2','C3','C4','C5','C6','C7','C8','C9'],
    "Age": [25,35,45,20,30,40,50,28,42],
    "Income":[30000,40000,50000,20000,35000,28000,48000,40000,50000],
    "Gender":["Male","Female","Male","Female","Female","Male","Female","Male","Male"],
    "Region":["Urban","Rural","Urban","Urban","Rural","Urban","Rural","Urban","Urban"],
    "Buys Product":["No","Yes","Yes","No","Yes","Yes","No","Yes","Yes"]
}

# Step 1: Convert to DataFrame
df = pd.DataFrame(dataset)

print("Original DataFrame:\n")
print(df)

def manual_encode(column):
    unique_vals = []
    
    for val in column:
        if val not in unique_vals:
            unique_vals.append(val)
    
    mapping = {}
    for i in range(len(unique_vals)):
        mapping[unique_vals[i]] = i
    
    encoded_column = []
    for val in column:
        encoded_column.append(mapping[val])
    
    return encoded_column, mapping


categorical_columns = ["Customer", "Gender", "Region", "Buys Product"]

mappings = {}

for col in categorical_columns:
    df[col], mappings[col] = manual_encode(df[col])

print("\nEncoded DataFrame:\n")
print(df)

print("\nMappings Used:\n")
for col, mapping in mappings.items():
    print(f"{col}: {mapping}")

max_vals=df.max()
min_vals=df.min()
df_normalized=(df-min_vals)/(max_vals-min_vals)
print(df_normalized)
print(max_vals.Gender)

last_cust=df["Customer"].iloc[-1]

def normalize_new_point(new_point, df):
    normalized_point = {}
    
    for col in new_point:
        print(col)
        if col == "Age" or col == "Income":
            max_val = max_vals[col]
            min_val = min_vals[col]

            if max_val == min_val:
                normalized_point[col] = 0
            else:
                normalized_point[col] = (new_point[col] - min_val) / (max_val - min_val)
        elif col in categorical_columns:
            normalized_point[col] = mappings[col][new_point[col]]
    
    return normalized_point



def euclidean_distance(row1, row2, features):
    distance = 0
    for f in features:
        distance += (row1[f] - row2[f]) ** 2
    return math.sqrt(distance)



def knn(df, new_point, k=3):
    distances = []
    
    
    features = list(df.columns)
    features.remove("Buys Product")
    features.remove("Customer")
    new_point.pop("Customer", None)
    new_point_normalized=normalize_new_point(new_point,df)
    
    for i in range(len(df)):
        row = df.iloc[i]
        dist = euclidean_distance(row, new_point_normalized, features)
        distances.append((dist, row["Buys Product"]))
    
    
    distances.sort(key=lambda x: x[0])
    
    
    neighbors = distances[:k]
    
    
    count = {}
    for _, label in neighbors:
        if label not in count:
            count[label] = 0
        count[label] += 1
    
    
    majority_class = max(count, key=count.get)
    
    return majority_class, neighbors



new_point = {
    "Customer": 9,   
    "Age": 32,      
    "Income": 45000,   
    "Gender": "Male",
    "Region": "Rural"
}


result, neighbors = knn(df, new_point, k=3)

print("Nearest Neighbors (distance, class):")
for n in neighbors:
    print(n)
    
for key,value in mappings["Buys Product"].items():
    if value == result:
        print("\nPredicted Class:", key)


#