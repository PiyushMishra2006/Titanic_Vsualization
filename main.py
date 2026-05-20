import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")

# print(df.isnull().sum())
# 688-empty in deck and 177 empty in age
#Remove deck
df.drop(columns="deck",inplace=True)
# Assign median value of age to empty ones
df["age"] = df["age"].fillna(df["age"].median())
# print(df.isnull().sum()) # 0

#Countplot - Survival Count
sns.countplot(x="survived",data=df)
plt.title("Survival Count")
plt.xlabel("Survived")
plt.ylabel("Number of Passengers")
# plt.show()
plt.close()

#Countplot - Gender Distribution
sns.countplot(x="sex",data=df)
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Passenger Count")
# plt.show()
plt.close()

#Countplot - Survival based on Gender
sns.countplot(x="sex",hue="survived",data=df)
plt.title("Survival based on Gender")
plt.xlabel("Gender")
plt.ylabel("Passenger count")
# plt.show()
plt.close()

#Countplot - Passenger counts based on classes
sns.countplot(x="class",data=df)
plt.title("Passenger Count based on class")
plt.xlabel("Class")
plt.ylabel("Passenger Count")
# plt.show()
plt.close()

#Countplot - Survival based on class facilities
sns.countplot(x="class",hue="survived",data=df)
plt.title("Survival based on Class")
plt.xlabel("Class")
plt.ylabel("Passenger count")
# plt.show()
plt.close()

#Histogram - Age Distribution
sns.histplot(df["age"],bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
# plt.show()
plt.close()

# Boxplot - Survival based on Age
plt.figure(figsize=(8,5))
sns.boxplot(x="survived",y="age",data=df)
plt.title("Survival Based on Age")
plt.xlabel("Survived")
plt.ylabel("Age")
# plt.show()
plt.close()

#Histogram - Fare Distribution
sns.histplot(df["fare"],bins=10)
plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Passenger Count")
# plt.show()
plt.close()

#Boxplot - Fare Outliers
plt.figure(figsize=(8,5))
sns.boxplot(x=df["fare"])
plt.title("Fare Outliers")
# plt.show()
plt.close()

#Boxplot - Fare Vs Survival
plt.figure(figsize=(8,5))
sns.boxplot(x="survived",y="fare",data=df)
plt.title("Survival based on fare")
plt.xlabel("Survived")
plt.ylabel("Fare")
# plt.show()
plt.close()

#Correlation Heatmap
plt.figure(figsize=(10,8))
corr = df.corr(numeric_only=True)
sns.heatmap(corr,annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap")
# plt.show()
plt.close()

#Pairplot
sns.pairplot(df[["survived","age","fare","pclass"]],hue="survived")
# plt.show()
plt.close()

#Violin Plot - Survival vs Age
plt.figure(figsize=(10,6))
sns.violinplot(x="survived",y="age",data=df)
plt.title("Violin Plot ; Age vs Survival")
plt.xlabel("Survived")
plt.ylabel("Age")
# plt.show()
plt.close()

#FacetGrid - Age Distribution based on Gender
g1 = sns.FacetGrid(df,col="sex",height=5)
g1.map(sns.histplot,"age")
# plt.show()
plt.close()

#FacetGrid - Gender + Survival + Histplot
g2 = sns.FacetGrid(df,col="sex",hue="survived",height=5)
g2.map(sns.histplot,"age")
g2.add_legend()
# plt.show()
plt.close()

#Scatterplot - Age vs Fare
plt.figure(figsize=(10,6))
sns.scatterplot(x='age',y='fare',hue='survived',data=df)
plt.title(" Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
# plt.show()
plt.close()

#Regression Plot - Age vs Fare
plt.figure(figsize=(10,6))
sns.regplot(x='age',y='fare',data=df)
plt.title("Regression - Age Vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
# plt.show()
plt.close()

#Swarm Plot - Class vs Age
plt.figure(figsize=(10,6))
sns.swarmplot(x='class',y='age',data=df)
plt.title("Age Distribution Among Passenger Class")
plt.ylabel("Age")
plt.xlabel("Passenger Class")
# plt.show()
plt.close()

#Catplot - Class vs Survived ( Can Call Any Other Plot Internally Using Kind)
sns.catplot(x='class',hue='survived',kind='count',data=df,height=6,aspect=1.2)
plt.title("Survival Count Across Passenger Classes")
# plt.show()
plt.close()

# Subplot - 2x2 Visualization Dashboard
fig,axes = plt.subplots(2,2,figsize=(14,10))
sns.countplot(x='survived',data=df,ax=axes[0,0])
sns.countplot(x='sex',hue='survived',data=df,ax=axes[0,1])
sns.histplot(df['age'],bins=20,kde=True,ax=axes[1,0])
sns.boxplot(x='class',y='fare',data=df,ax=axes[1,1])
plt.tight_layout()
# plt.show()
plt.close()

#Styling
sns.set_style('whitegrid')
sns.set_context('talk')
sns.set_palette('pastel')
sns.countplot(x='class',data=df)
plt.show()
plt.close()
