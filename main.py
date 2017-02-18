# conventional way to import pandas
import pandas as pd
# read CSV file directly from a URL and save the results
data = pd.read_csv('diabetes-training.csv', index_col=0)

# display the first 5 rows
print(data.shape)
