# Project

This project will demontrate the common software engineering tasks. we will develop and deploy a web application to a cloud service so that it is accessible to the public.
We will provide the user with the dataset on car sales advertisements. The project is split into several steps from creating a jupyter notebook file called EDA.ipynb in VS Code that will have the Exploratory Data Analysis, then the app.py file to write the code for the web, and using the Render platform instead of Heroku to lunch the app.

# Streamlit App

This is a simple Streamlit app that demonstrates the first five lines of data fram from the vehicles_us.csv file. More over the app shows a histogram for the model color and a scatter plot for the top fiftenn ordered models and how to use checkboxes to change the behavior of plots.

## Description

The Streamlit app showcases the use of Streamlit, Plotly Express, and Pandas to create an interactive scatter plot, histogram plot. The app allows users to toggle customization of the plot by checking or unchecking a checkbox. When the checkbox is checked, the plot's appearance is customized; when it's unchecked, the plot reverts to its default appearance.

## Usage

1. Clone the repository to your local machine:
https://github.com/Rami1804/project.git

2. Navigate to the project directory:
cd /c/Users/Rami/anaconda3/Project

3. Install the required dependencies:
pip install -r requirements.txt

4. Run the Streamlit app:
streamlit run app.py

5. Open a web browser and access the app at `http://localhost:8501`.

## Dependencies

- [Streamlit](https://streamlit.io/)
- [Plotly Express](https://plotly.com/python/plotly-express/)
- [Pandas](https://pandas.pydata.org/)


