
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data set
file_path = "Data/Airbnb_Open_Data.csv" 
df = pd.read_csv(file_path)
df.head()

# Check column names in the dataset
df.columns

# No. of Missing values in each column
df.isnull().sum()

# Convert 'last review' to datetime and handle errors
df["last review"] = pd.to_datetime(df["last review"], errors="coerce")

# Fill missing values
df.fillna({"reviews per month": 0, "last review": df["last review"].min()}, inplace=True)

# Drop records with missing 'name' or 'host name'
df.dropna(subset=["NAME", "host name"], inplace=True)

# Remove dollar signs and convert to float
df["price"] = df["price"].replace(r"[\$,]", "", regex=True).astype(float)
df["service fee"] = df["service fee"].replace(r"[\$,]", "", regex=True).astype(float)

# Remove any duplicate Records
df.drop_duplicates(inplace=True)


# Chart 1: Distribution of Listing Prices
plt.figure(figsize=(10, 6))
sns.histplot(data=df["price"])
plt.title("Distribution of Prices")
plt.xlabel("Price ($)")
plt.ylabel("Frequency")
plt.savefig("Images/price_distribution.png", dpi=300)
plt.show()

# Chart 2: Room Type Distribution
plt.figure(figsize=(8, 5))
sns.countplot(x=df["room type"], color="lightblue")
plt.title("Room Type Distribution")
plt.xlabel("Room Type")
plt.ylabel("Count")
plt.savefig("Images/room_type_distribution.png", dpi=300)
plt.show()

# Chart 3: Neighbourhood Analysis
plt.figure(figsize=(12, 8))
sns.countplot(y=df["neighbourhood group"], color="lightgreen", order=df["neighbourhood group"].value_counts().index)
plt.title("Number of listings by Neighbourhood Group")
plt.xlabel("Count")
plt.ylabel("Neighbourhood Group")
plt.savefig("Images/room_type_distribution.png", dpi=300)
plt.show()

# Chart 4: Price vs. Room Type
plt.figure(figsize=(10, 6))
sns.boxplot(x="room type", y="price", hue="room type", data=df, palette="Set2")
plt.title("Price vs. Room Type")
plt.xlabel("Room Type")
plt.ylabel("Price ($)")
plt.savefig("Images/price_vs_room_type.png")
plt.show()

# chart 5: Number of Reviews Over Time
df['last review'] = pd.to_datetime(df['last review'])
reviews_over_time = df.groupby(df['last review'].dt.to_period('M')).size()

plt.figure(figsize=(12, 6))
reviews_over_time.plot(kind='line', color='red')
plt.title('Number of Reviews Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Reviews')
plt.savefig('Images/reviews_over_time.png')
plt.show()



