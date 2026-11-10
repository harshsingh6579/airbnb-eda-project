# 🏙️ Airbnb Open Data Exploratory Data Analysis (EDA)

An exploratory data analysis project examining New York City Airbnb listings, pricing variations, room types, geographic distributions, and review trends using Python.

## 📊 Project Overview
This project cleans and analyzes an Airbnb open dataset to uncover structural housing market insights:
- **Data Cleaning:** Handled missing values, formatted currency strings for prices and service fees into numerical floats, and parsed datetime fields.
- **Key Visualizations & Visual Insights:**
  - **Price Distribution (`Images/price_distribution.png`):** Analyzed listing price frequencies via histograms, highlighting right-skewed pricing clusters where the majority of listings concentrate at lower nightly rates with long tails for luxury stays.
  - **Room Type Distribution (`Images/room_type_distribution.png`):** Evaluated the proportion of entire homes, private rooms, and shared spaces, showing dominant market shares for entire apartments and private rooms.
  - **Neighbourhood Group Analysis (`Images/room_type_distribution.png`):** Mapped listing density across NYC borough groupings, illustrating clear geographic hotspots and inventory concentration.
  - **Price vs. Room Type (`Images/price_vs_room_type.png`):** Compared cost disparities using customized Seaborn box plots, demonstrating how entire homes command significantly higher median prices and wider interquartile ranges than private or shared rooms.
  - **Review Activity Over Time (`Images/reviews_over_time.png`):** Tracked customer review trends temporally using Pandas period transformations (`.to_period('M')`), highlighting temporal growth trajectories and seasonal surges in user engagement.

## 🛠️ Tech Stack & Libraries
- **Python** 3.x
- **Data Manipulation:** `pandas`, `numpy`
- **Data Visualization:** `matplotlib`, `seaborn`

