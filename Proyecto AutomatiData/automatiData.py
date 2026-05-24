import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt

df = pd.read_csv('automatiData.csv')

df.head()

df.dtypes

df.describe()

df.info()

df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])


plt.figure(figsize=(10,2))
plt.title('Trip Distance')
sns.boxplot(data=None, x=df['trip_distance'], fliersize=1);


plt.figure(figsize=(15,5))
plt.title('Histogram of Trip Distance')
sns.histplot(df['trip_distance'], bins=range(0,26,1))


plt.figure(figsize=(10,2))
plt.title('Total Amount')
sns.boxplot(data=None, x=df['total_amount'], fliersize=2)


plt.figure(figsize=(10,2))
plt.title('Histogram of Total Amount')
sns.histplot(df['total_amount'], bins=range(0,26,1))


plt.figure(figsize=(10,2))
plt.title('Tip Amount')
sns.boxplot(data=None, x=df['tip_amount'], fliersize=1)


plt.figure(figsize=(10,2))
plt.title('Histogram of Tip Amount')
sns.histplot(df['tip_amount'], bins=range(0,16,1))


plt.figure(figsize=(12,7))
plt.title('Tip Amount By Vendor')
ax = sns.histplot(
    data=df,
    x="tip_amount",
    bins=range(0,21,1),
    hue="VendorID",
    multiple="stack",
)

ax.set_xticks(range(0,21,1))
ax.set_xticklabels(range(0,21,1));


tips_over_ten = df[df['tip_amount'] > 10]
plt.figure(figsize=(12,7))
plt.title('Tip amount by vendor histogram');

ax = sns.histplot(
    data=tips_over_ten, x='tip_amount', bins=range(10,21,1), 
    hue='VendorID', 
    multiple='stack'
    )

ax.set_xticks(range(10,21,1))
ax.set_xticklabels(range(10,21,1));


df["passenger_count"].value_counts()


mean_tips_by_passenger_count = df.groupby(['passenger_count']).mean()[['tip_amount']]
mean_tips_by_passenger_count


data = mean_tips_by_passenger_count.tail(-1)
pal = sns.color_palette("Greens_d", len(data))
rank = data['tip_amount'].argsort().argsort()
plt.figure(figsize=(12,7))
ax = sns.barplot(x=data.index,
            y=data['tip_amount'],
            palette=np.array(pal[::-1])[rank])
ax.axhline(df['tip_amount'].mean(), ls='--', color='red', label='global mean')
ax.legend()
plt.title('Mean tip amount by passenger count', fontsize=16);

df['month'] = df['tpep_pickup_datetime'].dt.month_name()


df['day'] = df['tpep_pickup_datetime'].dt.day_name()


monthly_rides = df['month'].value_counts()
monthly_rides


month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December']

monthly_rides = monthly_rides.reindex(index=month_order)
monthly_rides

monthly_rides.index


plt.figure(figsize=(12,7))
ax = sns.barplot(x=monthly_rides.index, y=monthly_rides)
ax.set_xticklabels(month_order)
plt.title('Ride count by month', fontsize=16);


daily_rides = df['day'].value_counts()
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
daily_rides = daily_rides.reindex(index=day_order)
daily_rides


plt.figure(figsize=(12,7))
ax = sns.barplot(x=daily_rides.index, y=daily_rides)
ax.set_xticklabels(day_order)
ax.set_ylabel('Count')
plt.title('Ride count by day', fontsize=16);


day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
total_amount_day = df.groupby('day').sum()[['total_amount']]
total_amount_day = total_amount_day.reindex(index=day_order)
total_amount_day


plt.figure(figsize=(12,7))
ax = sns.barplot(x=total_amount_day.index, y=total_amount_day['total_amount'])
ax.set_xticklabels(day_order)
ax.set_ylabel('Revenue (USD)')
plt.title('Total revenue by day', fontsize=16);


total_amount_month = df.groupby('month').sum()[['total_amount']]
total_amount_month = total_amount_month.reindex(index=month_order)
total_amount_month


plt.figure(figsize=(12,7))
ax = sns.barplot(x=total_amount_month.index, y=total_amount_month['total_amount'])
plt.title('Total revenue by month', fontsize=16);


df['DOLocationID'].nunique()


distance_by_dropoff = df.groupby('DOLocationID').mean()[['trip_distance']]


distance_by_dropoff = distance_by_dropoff.sort_values(by='trip_distance')
distance_by_dropoff 


plt.figure(figsize=(14,6))
ax = sns.barplot(x=distance_by_dropoff.index, 
                 y=distance_by_dropoff['trip_distance'],
                 order=distance_by_dropoff.index)
ax.set_xticklabels([])
ax.set_xticks([])
plt.title('Mean trip distance by drop-off location', fontsize=16);




test = np.round(np.random.normal(10, 5, (3000, 2)), 1)
midway = int(len(test)/2)  # Calculate midpoint of the array of coordinates
start = test[:midway]      # Isolate first half of array ("pick-up locations")
end = test[midway:]        # Isolate second half of array ("drop-off locations")


distances = (start - end)**2           
distances = distances.sum(axis=-1)
distances = np.sqrt(distances)

test_df = pd.DataFrame({'start': [tuple(x) for x in start.tolist()],
                   'end': [tuple(x) for x in end.tolist()],
                   'distance': distances})
data = test_df[['end', 'distance']].groupby('end').mean()
data = data.sort_values(by='distance')

plt.figure(figsize=(14,6))
ax = sns.barplot(x=data.index,
                 y=data['distance'],
                 order=data.index)
ax.set_xticklabels([])
ax.set_xticks([])
ax.set_xlabel('Endpoint')
ax.set_ylabel('Mean distance to all other points')
ax.set_title('Mean distance between points taken randomly from normal distribution');



df['DOLocationID'].max() - len(set(df['DOLocationID'])) 


plt.figure(figsize=(16,4))
# DOLocationID column is numeric, so sort in ascending order
sorted_dropoffs = df['DOLocationID'].sort_values()
# Convert to string
sorted_dropoffs = sorted_dropoffs.astype('str')

# Plot
sns.histplot(sorted_dropoffs, bins=range(0, df['DOLocationID'].max()+1, 1))
plt.xticks([])
plt.xlabel('Drop-off locations')
plt.title('Histogram of rides by drop-off location', fontsize=16);




df['trip_duration'] = (df['tpep_dropoff_datetime']-df['tpep_pickup_datetime'])


df.head(10)

