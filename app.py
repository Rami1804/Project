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

st.header("Histogram using streamlit plotly chart method")
fig1 = px.histogram(df, x='paint_color', title='Paint Color Histogram')
fig1.update_xaxes(title_text='Paint Color')
# Remove y-axis tick labels
fig1.update_yaxes(title_text='Number of Vehicale adds')
# Use st.plotly_chart to display the Plotly figure in Streamlit
st.plotly_chart(fig1)

st.header("scatter plot using streamlit write method")
Top_model = df.groupby('model')['type'].count().sort_values(ascending=False)[:15].reset_index()

fig2 = px.scatter(Top_model, y='model', x='type', title='Scatter Plot Most advertised Model',labels={'x': 'Number of advertisments', 'y': None})

fig2.update_xaxes(title_text='Number of advertisments')
# Remove y-axis tick labels
fig2.update_yaxes(title_text=None)

st.write(fig2)

# Create a checkbox to control the behavior of the plot
customize_plot = st.checkbox("Change Plot Points color and size")

# Create a scatter plot using Plotly Express

# Conditional statements to change plot behavior based on checkbox state
if customize_plot:
    # Customize the plot behavior here
    # For example, you can add or modify plot elements
    
    fig2.update_traces(marker=dict(size=10, opacity=0.7))
    fig2.update_traces(marker=dict(color="red"))  # Change all points to red
else:
    # Restore the default plot behavior here
    # You can reset any changes made when the checkbox is unchecked
    
    fig2.update_traces(marker=dict(size=5, opacity=1.0))
    fig2.update_traces(marker=dict(color="blue"))  # Change all points to red

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

filtered_type=df[df.type==make_choice][:20]
st.table(filtered_type)
