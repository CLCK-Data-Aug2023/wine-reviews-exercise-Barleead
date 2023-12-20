import pandas as pd

# Unzip the CSV file
!unzip winemag-data-130k-v2.csv.zip

# Read the CSV file
wine_reviews = pd.read_csv("winemag-data-130k-v2.csv")

# Create country counts and points
info = {
    #"country": wine_reviews['country'].unique(),
    "counts": wine_reviews['country'].value_counts(),
    "points": wine_reviews.groupby('country')['points'].mean().round(1)
}
#read the dataframe
output = pd.DataFrame(info)
#save to csv file
output.to_csv('reviews-per-country.csv', index=True)


