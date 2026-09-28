# Hotel Booking Demand Analysis
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pycountry as pc

pd.options.display.max_columns = None
data = pd.read_csv('hotel_bookings.csv')
data.head()
df = data.copy()

# Missing values
df.isnull().sum().sort_values(ascending=False)[:10]
df = df.drop(df[(df.adults + df.babies + df.children) == 0].index)
df[['agent', 'company']] = df[['agent', 'company']].fillna(0.0)
df['country'].fillna(data.country.mode().to_string(), inplace=True)
df['children'].fillna(round(data.children.mean()), inplace=True)

# Data types
df[['children', 'company', 'agent']] = df[['children', 'company', 'agent']].astype('int64')

def plot(x, y, x_label=None, y_label=None, title=None, figsize=(7,5), type='bar'):
    sns.set_style('darkgrid')
    fig, ax = plt.subplots(figsize=figsize)
    if x_label != None: ax.set_xlabel(x_label)
    if y_label != None: ax.set_ylabel(y_label)
    if title != None: ax.set_title(title)
    if type == 'bar': sns.barplot(x, y, ax=ax)
    elif type == 'line': sns.lineplot(x, y, ax=ax)
    plt.show()

def get_count(series, limit=None):
    if limit != None:
        series = series.value_counts()[:limit]
    else:
        series = series.value_counts()
    x = series.index
    y = series / series.sum() * 100
    return x.values, y.values

hotel_counts = df['hotel'].value_counts()
hotel_counts.plot.pie(autopct='%1.1f%%', figsize=(6,6),
                      title='Distribution of Hotel Types', ylabel='')
plt.show()

top_countries = df['country'].value_counts().head(10)
sns.barplot(x=top_countries.values, y=top_countries.index, palette='viridis')
plt.title('Top 10 Countries with Most Bookings')
plt.xlabel('Number of Bookings')
plt.ylabel('Country')
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(df['lead_time'], kde=True, bins=50, color='blue')
plt.title('Lead Time Distribution')
plt.xlabel('Lead Time (days)')
plt.ylabel('Frequency')
plt.show()

sns.countplot(data=df, x='is_canceled', palette='cool')
plt.title('Booking Status')
plt.xlabel('Canceled (0=No, 1=Yes)')
plt.ylabel('Count')
plt.xticks([0,1], ['Not Canceled','Canceled'])
plt.show()

plt.figure(figsize=(10,8))
numeric_df = df.select_dtypes(include=['number'])
corr_matrix = numeric_df.corr()
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# The report screenshots also show analysis using df_not_canceled
# and total_nights. The complete preceding definition of
# df_not_canceled is not exposed in the supplied PDF.
