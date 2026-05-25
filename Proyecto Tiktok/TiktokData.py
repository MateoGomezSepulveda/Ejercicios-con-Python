import numpy as ap
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt

data = pd.read_csv("tiktok_dataset.csv")

data.head()

data.size

data.shape

data.info()

data.describe()

plt.figure(figsize=(10,2))
plt.title('Video Duration Sec')
sns.boxplot(data=None, x=data['video_duration_sec'], fliersize=1)

plt.figure(figsize=(10,2))
plt.title('Histrogram of Video duration sec')
sns.histplot(data['video_duration_sec'], bins=range(0,26,1))

plt.figure(figsize=(10,2))
plt.title('video view count')
sns.boxplot(data=None, x=data['video_view_count'], fliersize=1)

plt.figure(figsize=(10,2))
plt.title('Histogram video view count')
sns.histplot(data['video_view_count'], bins=range(0,26,1))

plt.figure(figsize=(10,2))
plt.title('video like count')
sns.boxplot(data=None, x=data['video_like_count'], fliersize=1)

plt.figure(figsize=(10,2))
plt.title('Histogram video like count')
sns.histplot(data['video_like_count'], bins=range(0,26,1))

plt.figure(figsize=(10,2))
plt.title('boxplot video comment count')
sns.boxplot(data=None, x=data['video_comment_count'], fliersize=1)

plt.figure(figsize=(10,2))
plt.title('Histogram video comment count')
sns.histplot(data['video_comment_count'], bins=range(0,26,1))

plt.figure(figsize=(10,2))
plt.title(' boxplot video share count')
sns.boxplot(data=None, x=data['video_share_count'], fliersize=1)

plt.figure(figsize=(10,2))
plt.title('Histogram video share count')
sns.histplot(data['video_share_count'], bins=range(0,26,1) )

plt.figure(figsize=(10,2))
plt.title('Boxplot video download count')
sns.boxplot(data=None, x=data['video_download_count'], fliersize=1)

plt.figure(figsize=(10,2))
plt.figure('Histogram video download count')
sns.histplot(data['video_download_count'], bins=range(0,26,1))

plt.figure(figsize=(8,4))
plt.title('Histogram Claim status')
sns.countplot(x="claim_status", data=data)

plt.figure(figsize=(10,2))
plt.title('Claim Status by Author Ban Status')
sns.countplot(data=data, x='claim_status', hue='author_ban_status')

median_views = data.groupby('author_ban_status')['video_view_count'].median()
plt.figure(figsize=(10,2))
plt.title('Median View Counts by Author Ban Status')
sns.barplot(x=median_views.index, y=median_views.values)
plt.xlabel('Author Ban status')
plt.ylabel('Median view count')

median_views_clain = data.groupby('claim_status')['video_view_count'].median()
plt.figure(figsize=(10,2))
plt.title('Median vew counts by claim status')
sns.barplot(x=median_views_clain.index, y=median_views_clain.values)
plt.xlabel('claim status')
plt.ylabel('median view count')

views_by_claim = data.groupby('claim_status')['video_view_count'].sum()
plt.figure(figsize=(6,6))
plt.title('Proportion of total view by claim status')
plt.pie(views_by_claim.values, labels=views_by_claim.index, autopct='%1.1f%%', startangle=90, colors=["#66b3ff","#ff9999"])

count_colums = [
    'video_view_count',
    'video_like_count',
    'video_share_count',
    'video_download_count',
    'video_comment_count'
]

for col in count_colums:
    #calcular IQR
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1
    
    #calcular mediana
    median = data[col].median()
    
    #umbral de outlier ( median + 1.5 * IQR)
    
    threshold = median + 1.5 * IQR
    
    #contar cuantos valores superan el umbral
    outlier_count = (data[col] > threshold).sum()
    
    print(f'Number of outlers, {col}: {outlier_count}')



plt.figure(figsize=(8,6))
plt.title('video views vs likes by claim status')
sns.scatterplot(data=data, x='video_view_count', y='video_like_count', hue='claim_status', alpha=0.6)

plt.xlabel('video view count')
plt.ylabel('video like count')



plt.figure(figsize=(8,6))
plt.title('video views vs likes (opinion videos only)')

sns.scatterplot(data=data[data['claim_status'] == 'opinion'], x='video_view_count', y='video_like_count', color='orange', alpha=0.6)

plt.xlabel('video view count')
plt.ylabel('video like count')