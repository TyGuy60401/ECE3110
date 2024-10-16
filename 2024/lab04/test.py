import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample DataFrame with x and y columns
df = pd.DataFrame({
    'x': [1, 3, 2, 1, 4, 3, 5],
    'y': [10, 15, 5, 20, 25, 30, 35]
})

# Step 1: Sort by x values
df_sorted = df.sort_values(by='x')

# Step 2: Group by x and average the y values for duplicates
df_grouped = df_sorted.groupby('x').mean().reset_index()

# Step 3: Create evenly spaced x values
x_new = np.linspace(df_grouped['x'].min(), df_grouped['x'].max(), num=100)  # adjust num for the number of points you want

# Step 4: Interpolate the y values for the new x values
y_new = np.interp(x_new, df_grouped['x'], df_grouped['y'])

# Step 5: Create a new DataFrame with the interpolated values
df_result = pd.DataFrame({'x': x_new, 'y': y_new})

df_plot = df.sort_values(by='x')
plt.plot(df_plot['x'], df_plot['y'])
plt.plot(df_result['x'], df_result['y'])
plt.show()

print(df_result)
