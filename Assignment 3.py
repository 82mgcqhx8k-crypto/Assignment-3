import pandas as pd

df_petal = pd.read_csv('Petal_Data.csv')
df_sepal = pd.read_csv('Sepal_Data.csv')

#merge the two datasets into one, with the merge starting at sample_id
merge_data = pd.merge(df_petal, df_sepal, on='sample_id', suffixes= ('_petal', '_sepal'))

df_col = merge_data[['sample_id', 'species_sepal', 'species_petal', 'sepal_length', 'sepal_width', 'petal_length', 'petal_width']]

corr_matrix = df_col[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].corr()

# compare 6 variables with different correlations
compare_corr = {
    'sepal_length vs sepal_width': corr_matrix.loc['sepal_length', 'sepal_width'],
    'sepal_length vs petal_length': corr_matrix.loc['sepal_length', 'petal_length'],
    'sepal_length vs petal_width': corr_matrix.loc['sepal_length', 'petal_width'],
    'sepal_width vs petal_length': corr_matrix.loc['sepal_width', 'petal_length'],
    'sepal_width vs petal_width': corr_matrix.loc['sepal_width', 'petal_width'],
    'petal_length vs petal_width': corr_matrix.loc['petal_length', 'petal_width']
}

# calculate average, median, and standard deviation for each variable
average = df_col[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].mean()

medians = df_col[['sepal_length' , 'sepal_width', 'petal_length', 'petal_width']].median()

std_dev = df_col[['sepal_length' , 'sepal_width', 'petal_length', 'petal_width']].std()

print('Correlations between all variables:')
for pair, value in compare_corr.items():
    print(f'{pair} : {value:.4f}')

print('\nAverage:')
print(average)

print('\nMedian:')
print(medians)

print('\nStandard Deviation:')
print(std_dev)

# for question 2 in the homework
# First, most similiar species would be Virginica and Versicolor
# they both fairly simillar petal width and length
# (around 4-5.6 petal length) and (petal width, around 1-2.2)
# The measurements are much more close with the two irises mentioned

# For least similiar is probably Setosa, it has very distinct measurements
# The petal and sepal numbers much smaller than the other two species
# (1.4 - for petal length and 0.2-0.3 in petal width)