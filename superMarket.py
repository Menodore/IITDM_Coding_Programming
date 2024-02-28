import pandas as pd
import plotly.express  as plexp
import plotly.graph_objects as go

df = pd.read_csv('/home/iiitdmk-sic05/Downloads/Sample - Superstore.csv',encoding='windows-1254')
print(df.head(10))
df['Order Date'] = pd.to_datetime(df['Order Date'])

df['Order Month'] = df['Order Date'].dt.month
df['Order Year'] = df['Order Date'].dt.year
df['Order Day'] = df['Order Date'].dt.day

print(df.head())

monthly_sales = df.groupby(['Order Year', 'Order Month'])['Sales'].sum()

monthly_sales = monthly_sales.reset_index()

fig_1= plexp.line(monthly_sales, x="Order Month", y="Sales", color="Order Year")
fig_1.update_layout(title="Monthly Sales Trend in Superstore",xaxis_title="Month",yaxis_title="Total Sale")
fig_1.show()

sub_categ = df.groupby('Category')['Sales'].sum().reset_index()

fig_2= plexp.pie(sub_categ,
                 values='Sales',
                 names='Category',
                 hole=0.5
                 )
fig_2.update_layout(title='label+percent+value')
fig_2.show()
