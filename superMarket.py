
import pandas as pd
import plotly.express  as plexp
import plotly.graph_objects as go

df = pd.read_csv('/Sample - Superstore.csv',encoding = 'latin-1')

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

new_categ = df.groupby('Sub-Category')['Sales'].sum().reset_index()

fig_3 = plexp.bar(new_categ,
                  x='Sub-Category',  # Use 'Sub-Category' for x-axis
                  y='Sales',
                  title='Sales Distribution by Sub-Category',
                  )
fig_3.show()

a = df.groupby('Order Month')['Profit'].sum().reset_index()
fig_4 = plexp.line(a,
                   x='Order Month',
                   y='Profit',
                   title='Profit by Month',
                   )
fig_4.show()

b = df.groupby('Category')['Profit'].sum().reset_index()

fig_5 = plexp.pie(b,
                  values = 'Profit',
                  names = 'Category',
                  hole=0.7
                  )
fig_5.show()

c = df.groupby('Sub-Category')['Profit'].sum().reset_index()
Fig_6 = plexp.bar(c,
                  x='Sub-Category',  # Use 'Sub-Category' for x-axis
                  y='Profit',
                  title='Profit by Sub-Category',
                  )
Fig_6.show()


d = df.groupby('Segment')['Sales', 'Profit'].sum().reset_index()
fig_7 = plexp.bar(d,
                  x='Segment',  # x-axis will represent the segments
                  y=['Sales', 'Profit'],  # Sales and Profit will be displayed on the y-axis
                  title='Profit and Sales by Segment'  # Title for the chart
                  )
fig_7.show()
