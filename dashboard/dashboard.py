import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import datetime as dt
sns.set(style='dark')

hour_df = pd.read_csv("dashboard/hour.csv")

#  Mengubah tipe data pada kolom 'dteday' menjadi datetime
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Membuat Komponen Filter
min_date = hour_df["dteday"].min()
max_date = hour_df["dteday"].max()

with st.sidebar:
    st.title("Bike Sharing Dashboard")

    # Menambahkan logo perusahaan
    st.image("https://img.freepik.com/free-vector/ride-bicycle-concept-illustration_114360-28292.jpg")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu', min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

# Filter data berdasarkan tanggal
hour_df = hour_df[(hour_df['dteday'] >= start_date) & (hour_df['dteday'] <= end_date)]

# Melengkapi Dashboard dengan Berbagai Visualisasi Data
st.header('Bike Sharing Dashboard :sparkles:')

# Pertanyaan 1
st.subheader('Bagaimana pengaruh hari kerja dan hari libur terhadap jumlah peminjaman sepeda?')

# Menampilkan Total Hari Kerja dan Hari Libur
col1, col2 = st.columns(2)
with col1:
    total_workday = hour_df[hour_df["workingday"] == 1].shape[0]
    st.metric("Total Hari Kerja", value=total_workday)
with col2:
    total_holiday = hour_df[hour_df["workingday"] == 0].shape[0]
    st.metric("Total Hari Libur", value=total_holiday)

# Mengelompokkan data berdasarkan tanggal dan hari kerja
time_series_df = hour_df.groupby(['dteday', 'workingday'])['cnt'].sum().reset_index()
time_series_df['workingday'] = time_series_df['workingday'].replace({0: 'No', 1: 'Yes'})

# Membuat visualisasi time series
fig, ax = plt.subplots(figsize=(14, 7))
sns.lineplot(x='dteday', y='cnt', hue='workingday', data=time_series_df, palette='viridis', ax=ax)
ax.set_title('Jumlah Peminjaman Sepeda Berdasarkan Hari Kerja dan Hari Libur (Time Series)')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Total Peminjaman Sepeda')
ax.legend(title='Hari Kerja')

# Menampilkan visualisasi di Streamlit
st.pyplot(fig)

# Mengelompokkan data berdasarkan workingday
grouped_df = hour_df.groupby('workingday')['cnt'].sum().reset_index()
grouped_df.columns = ['Hari Kerja', 'Total']
grouped_df['Hari Kerja'] = grouped_df['Hari Kerja'].replace({0: 'No', 1: 'Yes'})

# Membuat visualisasi jumlah peminjaman sepeda berdasarkan hari kerja dan hari libur
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='Hari Kerja', y='Total', data=grouped_df, palette='viridis', ax=ax)
ax.set_title('Jumlah Peminjaman Sepeda Berdasarkan Hari Kerja dan Hari Libur')
ax.set_xlabel('Hari Kerja')
ax.set_ylabel('Total Peminjaman Sepeda')
st.pyplot(fig)

# Pertanyaan 2
st.subheader('Bagaimana pengaruh pengguna sepeda berlangganan dan tidak berlangganan terhadap jumlah peminjaman sepeda?')

# Menampilkan Total Pengguna Sepeda Berlangganan dan Tidak Berlangganan
col1, col2 = st.columns(2)
with col1:
    total_registered = hour_df["registered"].sum()
    st.metric("Total Peminjam Berlangganan", value=total_registered)
with col2:
    total_casual = hour_df["casual"].sum()
    st.metric("Total Peminjam Tidak Berlangganan", value=total_casual)

# Mengelompokkan data berdasarkan tanggal dan jenis pengguna
time_series_user_df = hour_df.groupby(['dteday'])[['casual', 'registered']].sum().reset_index()

# Membuat visualisasi time series
fig, ax = plt.subplots(figsize=(14, 7))
sns.lineplot(x='dteday', y='casual', data=time_series_user_df, label='Non-Registered', color='blue', ax=ax)
sns.lineplot(x='dteday', y='registered', data=time_series_user_df, label='Registered', color='green', ax=ax)
ax.set_title('Jumlah Peminjaman Sepeda Berdasarkan Jenis Pengguna (Time Series)')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Total Peminjaman Sepeda')
ax.legend(title='Jenis Pengguna')

# Menampilkan visualisasi di Streamlit
st.pyplot(fig)

# Mengelompokkan data berdasarkan pengguna berlangganan dan tidak berlangganan
grouped_user_df = hour_df[['casual', 'registered']].sum().reset_index()
grouped_user_df.columns = ['User Type', 'Count']
grouped_user_df['User Type'] = grouped_user_df['User Type'].replace({'casual': 'Non-Registered', 'registered': 'Registered'})

# Membuat visualisasi pie chart untuk pengguna sepeda berlangganan dan tidak berlangganan
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(grouped_user_df['Count'], labels=grouped_user_df['User Type'], autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff'])
ax.set_title('Pengaruh Pengguna Sepeda Berlangganan dan Tidak Berlangganan terhadap Jumlah Peminjaman Sepeda')
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Menampilkan visualisasi di Streamlit
st.pyplot(fig)

# Pertanyaan 3
st.subheader('Bagaimana pengaruh cuaca terhadap jumlah peminjaman sepeda?')

# Menampilkan metrik cuaca
col1, col2, col3, col4 = st.columns(4)
with col1:
    total_clear = hour_df[hour_df["weathersit"] == 1].shape[0]
    st.metric("Clear", value=total_clear)
with col2:
    total_cloudy = hour_df[hour_df["weathersit"] == 2].shape[0]
    st.metric("Cloudy", value=total_cloudy)
with col3:
    total_snow = hour_df[hour_df["weathersit"] == 3].shape[0]
    st.metric("Snow", value=total_snow)
with col4:
    total_rain = hour_df[hour_df["weathersit"] == 4].shape[0]
    st.metric("Rain", value=total_rain)

# Mengelompokkan data berdasarkan tanggal dan kondisi cuaca
time_series_weather_df = hour_df.groupby(['dteday', 'weathersit'])['cnt'].sum().reset_index()
time_series_weather_df['weathersit'] = time_series_weather_df['weathersit'].map({1: 'Clear', 2: 'Cloudy', 3: 'Snow', 4: 'Rain'})

# Membuat visualisasi time series
fig, ax = plt.subplots(figsize=(14, 7))
sns.lineplot(x='dteday', y='cnt', hue='weathersit', data=time_series_weather_df, palette='viridis', ax=ax)
ax.set_title('Jumlah Peminjaman Sepeda Berdasarkan Kondisi Cuaca (Time Series)')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Total Peminjaman Sepeda')
ax.legend(title='Kondisi Cuaca')

# Menampilkan visualisasi di Streamlit
st.pyplot(fig)

# Mengelompokkan data berdasarkan kondisi cuaca
weather_grouped_df = hour_df.groupby('weathersit')['cnt'].sum().reset_index()
weather_grouped_df.columns = ['Weather Situation', 'Total Rides']
weather_grouped_df['Weather Situation'] = weather_grouped_df['Weather Situation'].map({1: 'Clear', 2: 'Cloudy', 3: 'Snow', 4: 'Rain'})

# Membuat visualisasi jumlah peminjaman sepeda berdasarkan kondisi cuaca
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='Weather Situation', y='Total Rides', data=weather_grouped_df, palette='viridis', ax=ax)
ax.set_title('Jumlah Peminjaman Sepeda Berdasarkan Kondisi Cuaca')
ax.set_xlabel('Kondisi Cuaca')
ax.set_ylabel('Total Peminjaman Sepeda')
st.pyplot(fig)

# Pertanyaan 4
st.subheader('Bagaimana pengaruh musim terhadap jumlah peminjaman sepeda?')

# Menampilkan metrik musim
col1, col2, col3, col4 = st.columns(4)
with col1:
    total_winter = hour_df[hour_df["season"] == 1].shape[0]
    st.metric("Winter", value=total_winter)
with col2:
    total_spring = hour_df[hour_df["season"] == 2].shape[0]
    st.metric("Spring", value=total_spring)
with col3:
    total_summer = hour_df[hour_df["season"] == 3].shape[0]
    st.metric("Summer", value=total_summer)
with col4:
    total_fall = hour_df[hour_df["season"] == 4].shape[0]
    st.metric("Fall", value=total_fall)

# Mengelompokkan data berdasarkan musim
season_grouped_df = hour_df.groupby('season')['cnt'].sum().reset_index()
season_grouped_df.columns = ['Season', 'Total']
season_grouped_df['Season'] = season_grouped_df['Season'].map({1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'})

# Membuat visualisasi pie chart untuk jumlah peminjaman sepeda berdasarkan musim
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(season_grouped_df['Total'], labels=season_grouped_df['Season'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('viridis', 4))
ax.set_title('Jumlah Peminjaman Sepeda Berdasarkan Musim')
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Menampilkan visualisasi di Streamlit
st.pyplot(fig)

# Pertanyaan 5
st.subheader('Bagaimana distribusi jumlah peminjaman sepeda pada tahun 2011 dan 2012?')

# Menampilkan metrik jumlah peminjaman sepeda pada tahun 2011 dan 2012
col1, col2 = st.columns(2)
with col1:
    total_2011 = hour_df[hour_df["yr"] == 0]["cnt"].sum()
    st.metric("Total Peminjaman Sepeda Tahun 2011", value=total_2011)
with col2:
    total_2012 = hour_df[hour_df["yr"] == 1]["cnt"].sum()
    st.metric("Total Peminjaman Sepeda Tahun 2012", value=total_2012)

# Mengelompokkan data berdasarkan tanggal dan tahun
time_series_year_df = hour_df.groupby(['dteday', 'yr'])['cnt'].sum().reset_index()
time_series_year_df['yr'] = time_series_year_df['yr'].map({0: 2011, 1: 2012})

# Membuat visualisasi time series
fig, ax = plt.subplots(figsize=(14, 7))
sns.lineplot(x='dteday', y='cnt', hue='yr', data=time_series_year_df, palette='viridis', ax=ax)
ax.set_title('Jumlah Peminjaman Sepeda Berdasarkan Tahun (Time Series)')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Total Peminjaman Sepeda')
ax.legend(title='Tahun')

# Menampilkan visualisasi di Streamlit
st.pyplot(fig)

# Mengelompokkan data berdasarkan tahun
year_grouped_df = hour_df.groupby('yr')['cnt'].sum().reset_index()
year_grouped_df.columns = ['Year', 'Total']
year_grouped_df['Year'] = year_grouped_df['Year'].map({0: 2011, 1: 2012})

# Membuat visualisasi jumlah peminjaman sepeda berdasarkan tahun
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='Year', y='Total', data=year_grouped_df, palette='viridis', ax=ax)
ax.set_title('Jumlah Peminjaman Sepeda Berdasarkan Tahun')
ax.set_xlabel('Tahun')
ax.set_ylabel('Total Peminjaman Sepeda')
st.pyplot(fig)

# RFM Analysis
st.subheader('RFM Analysis')

# Menghitung Recency
snapshot_date = hour_df['dteday'].max() + dt.timedelta(days=1)
rfm_df = hour_df.groupby('registered').agg({
    'dteday': lambda x: (snapshot_date - x.max()).days,
    'instant': 'count',
    'cnt': 'sum'
}).reset_index()

# Mengganti nama kolom
rfm_df.columns = ['registered', 'Recency', 'Frequency', 'Monetary']

# Menentukan skor untuk setiap metrik RFM
rfm_df['R_Score'] = pd.qcut(rfm_df['Recency'], 5, labels=[5, 4, 3, 2, 1])
rfm_df['F_Score'] = pd.qcut(rfm_df['Frequency'], 5, labels=[1, 2, 3, 4, 5])
rfm_df['M_Score'] = pd.qcut(rfm_df['Monetary'], 5, labels=[1, 2, 3, 4, 5])

# Menggabungkan skor RFM menjadi satu skor RFM
rfm_df['RFM_Score'] = rfm_df['R_Score'].astype(str) + rfm_df['F_Score'].astype(str) + rfm_df['M_Score'].astype(str)

# Define RFM segments
seg_map = {
    r'[1-2][1-2]': 'Hibernating',
    r'[1-2][3-4]': 'At Risk',
    r'[1-2]5': 'Can\'t Lose',
    r'3[1-2]': 'About to Sleep',
    r'33': 'Need Attention',
    r'[3-4][4-5]': 'Loyal Customers',
    r'41': 'Promising',
    r'51': 'New Customers',
    r'[4-5][2-3]': 'Potential Loyalists',
    r'5[4-5]': 'Champions'
}

# Menggabungkan seg_map dengan RFM_Score
rfm_df['Segment'] = rfm_df['R_Score'].astype(str) + rfm_df['F_Score'].astype(str)
rfm_df['Segment'] = rfm_df['Segment'].replace(seg_map, regex=True)

# Visualisasi Segmentasi Pelanggan Berdasarkan RFM Score
fig, ax = plt.subplots(figsize=(12, 6))
sns.countplot(x='Segment', data=rfm_df, palette='viridis', order=rfm_df['Segment'].value_counts().index, ax=ax)
ax.set_title('Segmentasi Pelanggan Berdasarkan RFM Score')
ax.set_xlabel('Segment')
ax.set_ylabel('Jumlah Pelanggan')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)

# Menampilkan Footer
st.caption('[Bima Rakajati](https://github.com/bimarakajati/Bike-Sharing-Data-Analysis) - 2024')