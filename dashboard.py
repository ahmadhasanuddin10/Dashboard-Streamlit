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


