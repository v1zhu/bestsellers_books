import pandas as pd

bestsellers = pd.read_csv("bestsellers.csv")

# Get the first 5 rows of the spreadsheet
print(bestsellers.head())

# Get the shape of the spreadsheet
print(bestsellers.shape)

# Get the column names of the spreadsheet
print(bestsellers.columns)

# Get summary statistics for each column
print(bestsellers.describe())

#cleaning the data
bestsellers.drop_duplicates(inplace=True)
bestsellers.rename(columns={"Name": "Title", "Year": 
                            "Publication Year", "User Rating": "Rating"}, inplace=True)
bestsellers["Price"] = bestsellers["Price"].astype(float)

#analysis
author_counts = bestsellers['Author'].value_counts()
print(author_counts)

avg_rating_by_genre = bestsellers.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)

# Export top selling authors to a CSV file
author_counts.head(10).to_csv("top_authors.csv")

# Export average rating by genre to a CSV file
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")
