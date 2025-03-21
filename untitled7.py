# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1krFQsyYbQpP6CyoAaCEpPSzsB8Xd-lg_
"""

from google.colab import files
uploaded = files.upload()

# Load the titanic dataset
import pandas as pd
df = pd.read_csv('titanic.csv')
df

#Columns Details

#PassengerId: A unique identifier for each passenger.

#Survived: Indicates whether the passenger survived (1) or did not survive (0). This is the target variable in many predictive modeling tasks.

#Pclass: The passenger's ticket class (1 = 1st class, 2 = 2nd class, 3 = 3rd class). This is a proxy for socio-economic status.

#Name: The name of the passenger.

#Sex: The gender of the passenger (male or female).

#Age: The age of the passenger. Note that some ages are missing (NaN).

#SibSp: The number of siblings or spouses aboard the Titanic.

#Parch: The number of parents or children aboard the Titanic.

#Ticket: The ticket number.

#Fare: The fare paid for the ticket.

#Cabin: The cabin number. Note that many values are missing (NaN).

#Embarked: The port where the passenger boarded the Titanic (C = Cherbourg, Q = Queenstown, S = Southampton).

#Summary Statistics
df.isnull().sum()

#Age: Some passengers have missing age values. This can be handled by imputation .

#Cabin: A large number of cabin values are missing. This column might be dropped or used creatively.

#Embarked: A few passengers have missing Embarked values, which can be filled with the most common port.

#Numerical Columns
#PassengerId: Unique identifier (not useful for analysis).

#Survived: Binary outcome (0 = did not survive, 1 = survived).

#Pclass: Ticket class (1 = 1st class, 2 = 2nd class, 3 = 3rd class).

#Age: Age of the passenger.

#SibSp: Number of siblings/spouses aboard.

#Parch: Number of parents/children aboard.

#Fare: Fare paid for the ticket.

df.describe()

#Survived:
#Mean (0.3838): Approximately 38.38% of passengers survived.
#Binary Column: The column only contains 0 (did not survive) and 1 (survived), so the mean represents the survival rate.
#Imbalanced Data: The dataset is imbalanced, with more non-survivors (61.62%) than survivors (38.38%). This is important for predictive modeling, as imbalanced data can affect model performance.

#Pclass:
#Mean (2.3086): Most passengers were in 3rd class (median = 3).
#Distribution:25% of passengers were in 2nd class or lower.75% of passengers were in 3rd class.
#Implication: Lower-class passengers (3rd class) were more common, and survival rates might vary significantly by class.

#Age:
#Mean (29.6991): The average age of passengers was 29.7 years.
#Missing Values: Only 714 out of 891 rows have age data (177 missing values).
#Distribution:25% of passengers were younger than 20.125 years.50% of passengers were younger than 28 years.75% of passengers were younger than 38 years.
#Range: Ages range from 0.42 years (infants) to 80 years.
#Implication: Age is an important feature, but missing values need to be handled

#SibSp:
#Mean (0.5230): Most passengers traveled without siblings or spouses.
#Distribution:75% of passengers had 1 or fewer siblings/spouses aboard.
#Maximum: 8 siblings/spouses (outliers likely exist).
#Implication: Family size (combined with Parch) could influence survival rates.

#Parch:
#Mean (0.3816): Most passengers traveled without parents or children.
#Distribution:75% of passengers had 0 parents/children aboard.
#Maximum: 6 parents/children (outliers likely exist).
#Implication: Similar to SibSp, this feature could be combined with SibSp to create a "family size" feature.

#Fare:
#Mean (32.2042): The average fare paid was $32.20.
#High Variability: The standard deviation is 49.6934, indicating a wide range of fares.
#Distribution:25% of passengers paid $7.91 or less.50% of passengers paid $14.45 or less.75% of passengers paid $31.00 or less.
#Maximum fare: $512.33 (likely an outlier).
#Implication: Fare is highly skewed, with a few passengers paying significantly more than others. This could be due to differences in class or cabin type.

#PassengerId:
#Count (891): There are 891 unique passengers in the dataset.
#Range: Passenger IDs range from 1 to 891.
#Implication: This is just an identifier and not useful for analysis.

#Categorical Columns:
#Name: Full name of the passenger (unique for each passenger).
#Sex: Gender of the passenger (male or female).
#Ticket: Ticket number (can be alphanumeric).
#Cabin: Cabin number (many missing values).
#Embarked: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton).

# Select categorical columns
categorical_columns = ['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked']

# Generate summary statistics for categorical columns
categorical_summary = df[categorical_columns].describe(include='object')

# Display the summary
print(categorical_summary)

#Name:
#The Name column is not useful as-is for analysis because all values are unique.
#Recommendation: Extract titles (e.g., Mr., Mrs., Miss) from the names to create a new feature, as titles often correlate with survival rates.

#Sex:
#Males significantly outnumber females in the dataset.
#Recommendation: Use this feature as-is, as gender is a strong predictor of survival (females had higher survival rates).

#Ticket:
#Many passengers traveled alone (unique tickets), but some traveled in groups (shared tickets).
#Recommendation:Analyze shared tickets to identify family groups or traveling companions.Consider grouping rare ticket numbers or creating a feature for "group size" based on shared tickets.

#Cabin:
#The Cabin column has a high percentage of missing values (77% missing).The available cabin data is sparse and mostly unique.
#Recommendation:Extract deck information from the cabin numbers (e.g., the first letter represents the deck).Consider dropping the column if deck information is not useful.

#Embarked:
#The majority of passengers boarded at Southampton.
#Recommendation:Impute the 2 missing values with the mode (S).Use this feature as-is, as the port of embarkation might correlate with survival rates.

#EDA for Numerical Columns
#Distribution of Numerical Features
# Plot histograms for numerical columns
import matplotlib.pyplot as plt
import numpy as np
df.hist(figsize=(12, 10), bins=20)
plt.suptitle("Distribution of Numerical Features")
plt.show()

#PassengerId:This is likely a unique identifier for each passenger and does not provide meaningful insights for analysis.
#Age:The distribution of age shows that most passengers were between 20 and 40 years old.There is a peak in the younger age group, indicating a significant number of young adults and children.
#Fare:The fare distribution is right-skewed, meaning most passengers paid lower fares, with a few paying significantly higher amounts.This suggests that the majority of passengers were in lower classes (e.g., 3rd class).
#Survival:The survival distribution indicates that a significant portion of passengers did not survive (0), with a smaller portion surviving (1).This highlights the imbalanced nature of the target variable.
#SibSp (Siblings/Spouses):Most passengers traveled with 0 or 1 sibling/spouse.The distribution decreases as the number of siblings/spouses increases.
#Pclass (Passenger Class):The distribution shows that the majority of passengers were in the 3rd class, followed by 1st and 2nd classes.This reflects the socio-economic distribution of passengers on the Titanic.
#Parch (Parents/Children):Similar to SibSp, most passengers traveled with 0 parents/children.The number of passengers decreases as the number of parents/children increases.

#Correlation Between Numerical Features
# Correlation matrix
import seaborn as sns
corr_matrix = df.corr(numeric_only=True)
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Matrix for Numerical Features")
plt.show()

#Strongest Correlations:
#Pclass vs. Fare: -0.55 (higher class = higher fare).
#Pclass vs. Survived: -0.34 (higher class = higher survival rate).
#SibSp vs. Parch: 0.41 (larger families tend to have both siblings/spouses and parents/children).

#Survival Insights:
#Survival is most strongly correlated with Pclass and Fare.
#Age, SibSp, and Parch have weak or negligible correlations with survival.

#Family Size:
#SibSp and Parch are moderately correlated (0.41), indicating that passengers with larger families often traveled with both siblings/spouses and parents/children.

#Fare and Class:
#Fare is strongly influenced by Pclass, with higher-class passengers paying significantly more.

#Survival Rate by Numerical Features
# Survival rate by age
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Age', hue='Survived', bins=30, kde=True, multiple='stack')
plt.title("Survival Rate by Age")
plt.show()

# Survival rate by fare
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Fare', hue='Survived', bins=30, kde=True, multiple='stack')
plt.title("Survival Rate by Fare")
plt.show()

#Children (Age < 10):
#Higher survival rate compared to other age groups.
#This aligns with the "women and children first" protocol during the evacuation.

#Young Adults (Age 20-40):
#This age group has the highest number of passengers.
#Survival rates are mixed, with a significant number of both survivors and non-survivors.

#Middle-Aged and Older Passengers (Age 40+):
#Survival rates decrease with increasing age.
#Older passengers (age 60+) had lower survival rates.

#Peak in Non-Survivors:
#The highest number of non-survivors is observed in the 20-40 age range, which is also the most populous age group on the ship.

#Peak in Survivors:
#Survivors are more evenly distributed across age groups, with a noticeable peak among children and young adults.

#EDA for Categorical Columns
#Distribution of Categorical Features
# Plot count plots for categorical columns
categorical_columns = ['Survived', 'Pclass', 'Sex', 'Embarked']

plt.figure(figsize=(15, 10))
for i, col in enumerate(categorical_columns, 1):
    plt.subplot(2, 2, i)
    sns.countplot(data=df, x=col, palette='Set2')
    plt.title(f"Distribution of {col}")
plt.tight_layout()
plt.show()

#Distribution of Survived:
#Count of Survived (0 and 1):0 (Did Not Survive): Higher count, indicating more passengers did not survive.1 (Survived): Lower count, indicating fewer passengers survived.

#Observation:
#The dataset is imbalanced, with more non-survivors than survivors.
#This imbalance should be addressed during modeling to avoid bias.

#Distribution of Sex:
#Count of Males and Females:
#Male: Significantly higher count than females.
#Female: Lower count compared to males.

#Observation:
#Males outnumbered females on the Titanic.
#This is important because survival rates were significantly higher for females.

#Distribution of Pclass:
#Count of Passengers by Class:
#3rd Class (Pclass = 3): Highest count, indicating most passengers were in 3rd class.
#1st Class (Pclass = 1): Moderate count.
#2nd Class (Pclass = 2): Lowest count among the three classes.

#Observation:
#The majority of passengers were in 3rd class, which is consistent with historical records.
#Survival rates were higher for 1st and 2nd class passengers compared to 3rd class.

#Distribution of Embarked:
#Count of Passengers by Embarkation Port:
#S (Southampton): Highest count, indicating most passengers boarded from Southampton.
#C (Cherbourg): Moderate count.
#Q (Queenstown): Lowest count.

#Observation:
#Southampton was the most common embarkation point.
#Passengers from Cherbourg had higher survival rates compared to those from Southampton and Queenstown.

#Survival Rate by Categorical Features
# Survival rate by Pclass
plt.figure(figsize=(8, 6))
sns.barplot(data=df, x='Pclass', y='Survived', palette='Set2')
plt.title("Survival Rate by Pclass")
plt.show()

# Survival rate by Sex
plt.figure(figsize=(8, 6))
sns.barplot(data=df, x='Sex', y='Survived', palette='Set2')
plt.title("Survival Rate by Sex")
plt.show()

# Survival rate by Embarked
plt.figure(figsize=(8, 6))
sns.barplot(data=df, x='Embarked', y='Survived', palette='Set2')
plt.title("Survival Rate by Embarked")
plt.show()

#The y-axis represents the survival rate (proportion of passengers who survived), and the x-axis represents the passenger class (Pclass).
#1st Class (Pclass = 1):
#Highest Survival Rate: Approximately 60-70% of 1st class passengers survived.
#Observation: 1st class passengers had the best chance of survival, likely due to their proximity to lifeboats and priority during evacuation.

#2nd Class (Pclass = 2):
#Moderate Survival Rate: Approximately 40-50% of 2nd class passengers survived.
#Observation: 2nd class passengers had a lower survival rate compared to 1st class but higher than 3rd class.

#3rd Class (Pclass = 3):
#Lowest Survival Rate: Approximately 20-30% of 3rd class passengers survived.
#Observation: 3rd class passengers had the lowest chance of survival, likely due to their location on the ship (lower decks) and limited access to lifeboats.

#The y-axis represents the survival rate (proportion of passengers who survived), and the x-axis represents the gender (Sex).
#Female Passengers:
#High Survival Rate: Approximately 70-80% of female passengers survived.
#Observation: Females had a significantly higher chance of survival, consistent with the "women and children first" protocol during the evacuation.

#Male Passengers:
#Low Survival Rate: Approximately 20-30% of male passengers survived.
#Observation: Males had a much lower chance of survival compared to females.

#The y-axis represents the survival rate (proportion of passengers who survived), and the x-axis represents the embarkation port (Embarked).
#Cherbourg (C):
#Highest Survival Rate: Approximately 50-60% of passengers who embarked from Cherbourg survived.
#Observation: Passengers from Cherbourg had the highest chance of survival among the three ports.

#Southampton (S):
#Moderate Survival Rate: Approximately 30-40% of passengers who embarked from Southampton survived.
#Observation: Passengers from Southampton had a moderate chance of survival.

#Queenstown (Q):
#Lowest Survival Rate: Approximately 20-30% of passengers who embarked from Queenstown survived.
#Observation: Passengers from Queenstown had the lowest chance of survival.

#Cabin Analysis
# Extract deck information from Cabin
df['Deck'] = df['Cabin'].str[0]

# Plot survival rate by deck
plt.figure(figsize=(8, 6))
sns.barplot(data=df, x='Deck', y='Survived', palette='Set2', order=sorted(df['Deck'].dropna().unique()))
plt.title("Survival Rate by Deck")
plt.show()

#The y-axis represents the survival rate (proportion of passengers who survived), and the x-axis represents the deck (Deck).
#Decks with Higher Survival Rates:
#Decks B, C, D, and E: These decks had higher survival rates compared to others.
#Observation: Passengers on these decks were likely closer to lifeboats or in higher-class accommodations, which improved their chances of survival.

#Decks with Lower Survival Rates:
#Decks A, F, G, and T: These decks had lower survival rates.
#Observation: Passengers on these decks might have been farther from lifeboats or in lower-class accommodations, reducing their chances of survival.

#Deck T:
#Very Low Survival Rate: Deck T had the lowest survival rate.
#Observation: Deck T might have been a less accessible or less prioritized area during the evacuation.

#Feature Engineering
#Extract Titles from Names
# Extract titles from names
df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)

# Plot survival rate by title
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Title', hue='Survived', palette='Set2')
plt.title("Survival Rate by Title")
plt.xticks(rotation=45)
plt.show()

#The y-axis represents the count of passengers, and the x-axis represents the titles extracted from passenger names.The bars are divided into two categories: Survived (1) and Did Not Survive (0).

#High Survival Rates:
#Miss, Mrs, Master, Mme, Ms, Lady, Countess:
#These titles had higher survival rates.
#Observation: Females (Miss, Mrs, Mme, Ms, Lady, Countess) and young boys (Master) were prioritized during the evacuation, leading to higher survival rates.

#Low Survival Rates:
#Mr, Rev, Don, Col, Capt, Jonkheer:
#These titles had lower survival rates.
#Observation: Males with these titles (e.g., Mr, Rev, Col, Capt) had lower survival rates, consistent with the "women and children first" protocol.

#Titles with Mixed Survival Rates:
#Dr, Major, Sir:
#These titles had moderate survival rates.
#Observation: Survival rates for these titles varied, possibly due to their specific roles or circumstances during the evacuation.

#Rare Titles:
#Countess, Jonkheer, Capt:
#These titles had very few passengers, making it difficult to draw strong conclusions.
#Observation: Titles with low counts may not be statistically significant but can provide interesting insights into specific passenger groups.

#Create Family Size Feature
# Create family size feature
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

# Plot survival rate by family size
plt.figure(figsize=(8, 6))
sns.barplot(data=df, x='FamilySize', y='Survived', palette='Set2')
plt.title("Survival Rate by Family Size")
plt.show()

#The y-axis represents the survival rate (proportion of passengers who survived), and the x-axis represents the family size (FamilySize), which is calculated as the sum of SibSp (siblings/spouses) and Parch (parents/children) plus 1 (the passenger themselves).

#Family Size = 1 (Passengers Traveling Alone):
#Low Survival Rate: Approximately 20-30% of passengers traveling alone survived.
#Observation: Passengers traveling alone had the lowest chance of survival, possibly because they lacked family support during the evacuation.

#Family Size = 2-4:
#Higher Survival Rates: Passengers with family sizes of 2-4 had significantly higher survival rates, peaking around 50-60%.
#Observation: Families of moderate size (2-4 members) had better chances of survival, likely because they could assist each other during the evacuation.

#Family Size ≥ 5:
#Declining Survival Rates: Passengers with larger families (5 or more members) had lower survival rates, dropping to around 20-30%.
#Observation: Larger families faced challenges during evacuation, possibly due to difficulties in coordinating or finding space on lifeboats.

#Family Size = 11:
#Very Low Survival Rate: Passengers with a family size of 11 had the lowest survival rate.
#Observation: Extremely large families faced the greatest challenges during the evacuation, leading to very low survival rates.

# Check column names
print("Columns before handling missing values:", df.columns)

# Drop Cabin column (if it exists)
if 'Cabin' in df.columns:
    df.drop(columns=['Cabin'], inplace=True)

# Impute Age with median
df['Age'].fillna(df['Age'].median(), inplace=True)

# Impute Embarked with mode
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Verify no missing values remain
print(df.isnull().sum())

#Univariate Analysis:
# Histogram for Age
sns.histplot(df['Age'], bins=30, kde=True)
plt.title("Distribution of Age")
plt.show()

# Bar plot for Sex
sns.countplot(data=df, x='Sex')
plt.title("Distribution of Sex")
plt.show()

#The x-axis represents the age of passengers, and the y-axis represents the count of passengers in each age group.

#Peak in Young Adults:
#The highest number of passengers are in the 20-40 age range.
#Observation: This age group represents the majority of passengers on the Titanic.

#Children (Age < 10):
#There is a noticeable number of children, particularly in the 0-10 age range.
#Observation: Families with children were present on the ship.

#Middle-Aged and Older Passengers (Age 40+):
#The number of passengers decreases steadily as age increases beyond 40.
#Observation: Older passengers (age 60+) are fewer in number.

#Infants and Toddlers:
#A small but significant number of infants and toddlers (age < 5) are present.
#Observation: Very young children were also on board.

#The y-axis represents the count of passengers, and the x-axis represents the gender (Sex).
#Male Passengers:
#Higher Count: The number of male passengers is significantly higher than female passengers.
#Observation: Males outnumbered females on the Titanic.

#Female Passengers:
#Lower Count: The number of female passengers is much lower than male passengers.
#Observation: Females were a smaller proportion of the passenger population.

#Bivariate Analysis:
# Box plot: Age vs. Survived
sns.boxplot(data=df, x='Survived', y='Age')
plt.title("Age Distribution by Survival")
plt.show()

# Bar plot: Survival Rate by Sex
sns.barplot(data=df, x='Sex', y='Survived')
plt.title("Survival Rate by Sex")
plt.show()

#Female Passengers:
#High Survival Rate: Approximately 70-80% of female passengers survived.
#Observation: Females had a significantly higher chance of survival, consistent with the "women and children first" protocol during the evacuation.

#Male Passengers:
#Low Survival Rate: Approximately 20-30% of male passengers survived.
#Observation: Males had a much lower chance of survival compared to females.

# Box plot of Age to visualize outliers
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Age')
plt.title("Box Plot of Age (Before Handling Outliers)")
plt.show()

# Calculate IQR for Age
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1

# Define lower and upper bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Cap outliers in Age
df['Age'] = df['Age'].apply(lambda x: lower_bound if x < lower_bound else (upper_bound if x > upper_bound else x))

# Box plot of Age after handling outliers
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Age')
plt.title("Box Plot of Age (After Handling Outliers)")
plt.show()

# Verify the changes
print("Age Statistics After Handling Outliers:")
print(df['Age'].describe())

#Age Distribution:
#The majority of passengers were young adults (20-35 years old).
#Infants and toddlers (age < 5) were present but in smaller numbers.
#Older passengers (age > 50) were fewer in number.

#Outlier Handling:
#The maximum age is now 54.5 years, indicating that extreme ages (e.g., > 70) have been capped.
#The minimum age is 2.5 years, confirming the presence of very young children.

#Survival Implications:
#Children (age < 10) had higher survival rates due to the "women and children first" protocol.
#Older passengers (age > 50) had lower survival rates, possibly due to physical limitations during evacuation.

#Outliers detection:

# Box plot of Fare to visualize outliers
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Fare')
plt.title("Box Plot of Fare (Before Handling Outliers)")
plt.show()

# Calculate IQR for Fare
Q1 = df['Fare'].quantile(0.25)
Q3 = df['Fare'].quantile(0.75)
IQR = Q3 - Q1

# Define lower and upper bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Cap outliers in Fare
df['Fare'] = df['Fare'].apply(lambda x: upper_bound if x > upper_bound else x)

# Box plot of Fare after handling outliers
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Fare')
plt.title("Box Plot of Fare (After Handling Outliers)")
plt.show()

# Verify the changes
print("Fare Statistics After Handling Outliers:")
print(df['Fare'].describe())

#Fare Distribution:
#The majority of passengers paid lower fares (median = 14.45), likely corresponding to 3rd class tickets.
#Higher fares (e.g., > 31.00) were paid by a smaller proportion of passengers, likely corresponding to 1st and 2nd class tickets.

#Outlier Handling:
#The maximum fare is now 65.63, indicating that extreme fares (e.g., > 100) have been capped.
#The minimum fare is 0.00, which may represent special cases (e.g., crew members or complimentary tickets).

#Survival Implications:
#Passengers who paid higher fares (e.g., 1st class) had higher survival rates, likely due to better access to lifeboats and evacuation resources.
#Passengers who paid lower fares (e.g., 3rd class) had lower survival rates.

#Visualize Insights
# Survival rate by Pclass and Sex
sns.barplot(data=df, x='Pclass', y='Survived', hue='Sex')
plt.title("Survival Rate by Pclass and Sex")
plt.show()

#The y-axis represents the survival rate (proportion of passengers who survived).
#The x-axis represents the passenger class (Pclass), with separate bars for each gender (Sex).

#Female Passengers:
#1st Class: Very high survival rate (close to 100%).
#2nd Class: High survival rate (around 90%).
#3rd Class: Moderate survival rate (around 50%).
#Observation: Females in higher classes (1st and 2nd) had significantly higher survival rates compared to those in 3rd class.

#Male Passengers:
#1st Class: Moderate survival rate (around 40%).
#2nd Class: Low survival rate (around 20%).
#3rd Class: Very low survival rate (around 10%).
#Observation: Males in higher classes had better survival rates than those in lower classes, but their survival rates were still much lower than females in the same classes.

#Class Disparity:
#1st Class: Highest survival rates for both genders.
#3rd Class: Lowest survival rates for both genders.
#Observation: Passenger class had a significant impact on survival, with higher-class passengers having better access to lifeboats and evacuation resources.

#Gender Disparity:
#Females had significantly higher survival rates than males across all classes.
#Observation: The "women and children first" protocol strongly favored females, regardless of class.

#Multivariate Analysis:
# Correlation matrix heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Matrix")
plt.show()

# Pair plot for numerical features
sns.pairplot(df[['Age', 'Fare', 'SibSp', 'Parch', 'Survived']], hue='Survived')
plt.show()

#Strongest Correlations:
#Pclass vs. Fare: -0.72 (higher class = higher fare).
#Pclass vs. Survived: -0.34 (higher class = higher survival rate).
#SibSp vs. FamilySize: 0.89 (strong relationship between siblings/spouses and family size).
#Parch vs. FamilySize: 0.78 (strong relationship between parents/children and family size).

#Survival Insights:
#Survival is most strongly correlated with Pclass and Fare.
#Age, SibSp, and Parch have weak or negligible correlations with survival.

#Family Size:
#SibSp and Parch are strongly correlated with FamilySize, indicating that family size is a meaningful derived feature.

#Fare and Class:
#Fare is strongly influenced by Pclass, with higher-class passengers paying significantly more.

#Range of Values:
#The values range from 0,000 to 381,000, indicating a wide range of data points.
#Observation: The dataset likely contains a large number of observations or a wide range of numerical values.

#Incremental Steps:
#The values increase by 1,000 at each step.
#Observation: The increments suggest that the data is binned or grouped into intervals of 1,000 units.

