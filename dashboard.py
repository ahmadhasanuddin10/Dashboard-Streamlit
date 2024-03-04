import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Membaca data dari file CSV
customers_df = pd.read_csv('customers_dataset.csv')
sellers_df = pd.read_csv('sellers_dataset.csv')
order_items_df = pd.read_csv('order_items_dataset.csv')
order_payments_df = pd.read_csv('order_payments_dataset.csv')
order_reviews_df = pd.read_csv('order_reviews_dataset.csv')
orders_df = pd.read_csv('orders_dataset.csv')
products_df = pd.read_csv('products_dataset.csv')
product_category_name = pd.read_csv('product_category_name_translation.csv')
geogeo_df = pd.read_csv('geolocation_dataset.csv')

# Merge data sesuai kebutuhan
merged_df = pd.merge(customers_df, orders_df, on='customer_id')
merged_df = pd.merge(merged_df, order_items_df, on='order_id')
merged_df = pd.merge(merged_df, products_df, on='product_id')

# Judul dashboard
st.title('E-Commerce Dashboard')


min_date = merged_df["order_purchase_timestamp"].min()
max_date = merged_df["order_purchase_timestamp"].max()

with st.sidebar:
    # Menambahkan logo 
    st.image("https://bangkit-academy-blogs.netlify.app/assets/logo.png")
    # Teks di bawah logo 
    st.write("Selamat datang di Dashboard E-Commerce")









# Visualisasi dan analisis data
st.subheader('Total Penjualan per Kategori Produk')
# Menghitung total penjualan per kategori produk
sales_by_category = merged_df.groupby('product_category_name')['price'].sum().sort_values(ascending=False)
st.bar_chart(sales_by_category)

st.subheader('Total Penjualan per Kota Pelanggan')
sales_by_city = merged_df.groupby('customer_city')['price'].sum().sort_values(ascending=False)
st.bar_chart(sales_by_city)

# Gabungkan data order_items dengan data orders untuk mendapatkan informasi waktu pengiriman
merged_df = pd.merge(order_items_df, orders_df, on='order_id')

# Gabungkan data yang telah digabungkan dengan data sellers untuk mendapatkan informasi penjual
merged_df = pd.merge(merged_df, sellers_df, on='seller_id')

# Menghitung durasi waktu pengiriman
merged_df['order_purchase_timestamp'] = pd.to_datetime(merged_df['order_purchase_timestamp'])
merged_df['order_delivered_customer_date'] = pd.to_datetime(merged_df['order_delivered_customer_date'])
merged_df['delivery_time'] = merged_df['order_delivered_customer_date'] - merged_df['order_purchase_timestamp']

# Boxplot Waktu Pengiriman per Kota Penjual
plt.figure(figsize=(12, 6))
sns.boxplot(x='seller_state', y='delivery_time', data=merged_df)
plt.title('Delivery Time by Seller State')
plt.xlabel('Seller State')
plt.ylabel('Delivery Time (days)')
plt.xticks(rotation=45)

# Menyimpan gambar sebagai objek gambar dan sumbu
fig, ax = plt.subplots()
sns.boxplot(x='seller_state', y='delivery_time', data=merged_df, ax=ax)
plt.title('Delivery Time by Seller State')
plt.xlabel('Seller State')
plt.ylabel('Delivery Time (days)')
plt.xticks(rotation=45)

# Menampilkan plot menggunakan st.pyplot() dengan objek gambar
st.pyplot(fig)

# Scatterplot Waktu Pengiriman vs Biaya Pengiriman
fig, ax = plt.subplots(figsize=(12, 6))
sns.scatterplot(x='freight_value', y='delivery_time', data=merged_df, ax=ax)
plt.title('Delivery Time vs Freight Value')
plt.xlabel('Freight Value')
plt.ylabel('Delivery Time (days)')
st.pyplot(fig)
