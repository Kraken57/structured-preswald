from preswald import text, plotly, connect, get_df, table
import pandas as pd
import plotly.express as px

# Initialize and load data
text("# 🎮 Video Game Sales Dashboard")
connect()
df = get_df('vgsales_csv')

# Basic data cleaning
df = df.dropna(subset=['Year'])
df['Year'] = pd.to_numeric(df['Year'], errors='coerce').astype('Int64')

# 1. Show basic data table
text("## Top 10 Best-Selling Games")
table(df.sort_values('Global_Sales', ascending=False).head(10))

# 2. Create scatter plot of Year vs Global Sales
fig1 = px.scatter(df, 
                 x='Year', 
                 y='Global_Sales', 
                 hover_name='Name',
                 color='Genre',
                 title='Game Sales by Year and Genre',
                 labels={'Global_Sales': 'Global Sales (millions)'})
plotly(fig1)

# 3. Create bar chart of top platforms
text("## Top Gaming Platforms")
platform_sales = df.groupby('Platform')['Global_Sales'].sum().nlargest(10).reset_index()
fig2 = px.bar(platform_sales,
             x='Platform',
             y='Global_Sales',
             title='Total Sales by Platform')
plotly(fig2)

# 4. Show raw data
text("## Full Dataset")
table(df)