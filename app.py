import streamlit as st
import pandas as pd
import plotly.express as px

st.write("""
### Reading info on our dataset
""")
st.write("""
#### head of data
""")
try:
    df = pd.read_csv(r'C:\Users\Rami\anaconda3\Project\vehicles_us.csv')

except:
    df = pd.read_csv('vehicles_us.csv') 

#df = pd.read_csv('c/Users/Rami/anaconda3/Project/vehicles_us.csv')
st.table(df.head())

st.header("Histogram using streamlit plotly_chart method")
fig1 = px.histogram(df, x='paint_color', title='Body_Color')
# Use st.plotly_chart to display the Plotly figure in Streamlit
st.plotly_chart(fig1)

st.header("scatter plot using streamlit write method")
Top_model = df.groupby('model')['price'].count().sort_values(ascending=False)[:15].reset_index()
fig2 = px.scatter(Top_model, y='model', x='price', title='Top 15 Models', labels={'price': 'count', 'y': 'Y-axis'})
st.write(fig2)

# Create a checkbox to control the behavior of the plot
customize_plot = st.checkbox("Customize Plot")

# Create a scatter plot using Plotly Express
#scatter_fig = px.scatter(data, x='X-axis', y='Y-axis', title='Sample Scatter Plot')
# fig2

# Conditional statements to change plot behavior based on checkbox state
if customize_plot:
    # Customize the plot behavior here
    # For example, you can add or modify plot elements
    #scatter_fig.update_traces(marker=dict(size=10, opacity=0.7))
    fig2.update_traces(marker=dict(size=10, opacity=0.7))
else:
    # Restore the default plot behavior here
    # You can reset any changes made when the checkbox is unchecked
    #scatter_fig.update_traces(marker=dict(size=5, opacity=1.0))
    fig2.update_traces(marker=dict(size=5, opacity=1.0))

# Display the scatter plot using st.plotly_chart
st.write(fig2)


    ## filtering the data
st.write("""## 
         Block with Filtered Data
""")
st.text('You can filter the data however you want')


#creating options to choose from
rest_type=df['type'].unique() 
# create a parameter that is a final choice
make_choice = st.selectbox('Select your Model Type:', rest_type)

filtered_type=df[df.type==make_choice]
st.table(filtered_type)
