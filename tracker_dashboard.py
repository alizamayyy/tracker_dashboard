import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import io
import base64

# Load your dataset
file_path = "C:/Users/Aliza May/OneDrive - Cebu Institute of Technology University/Desktop/3rd yr/IT365 - Data Analytics/tracker/Bataluna_Tracker.csv"
df = pd.read_csv(file_path)

margins_css = """
    <style>
        .main > div {
            margin-top: -80px;
            text-align: center;
            margin-left: 2px;
        }
    </style>
"""

st.markdown(margins_css, unsafe_allow_html=True)

# Streamlit app title
st.markdown("<h1 style='text-align: center; margin-bottom: 20px'>What Happened in the Span of Two Weeks?</h1>", unsafe_allow_html=True)


sleep_data = df[df['Activity'] == 'sleep']
# Calculate total sleep hours
total_sleep_hours = sleep_data['Duration in Hrs'].sum()
average_sleep_hours = total_sleep_hours / len(sleep_data)

# Filter the DataFrame for "review" activity
study_data = df[df['Activity'].str.contains('review', case=False, na=False)]

# Calculate the total study hours for "review"
total_study_hours = study_data['Duration in Hrs'].sum()

# Calculate the average study hours for "review"
average_study_hours = total_study_hours / len(study_data)

# Filter the DataFrame for "me-time (tiktok and social media)" activity
me_time_data = df[df['Activity'].str.contains('me-time', case=False, na=False)]

# Calculate the total "me-time" hours
total_me_time_hours = me_time_data['Duration in Hrs'].sum()

# Calculate the average "me-time" hours
average_me_time_hours = total_me_time_hours / len(me_time_data)

travel_to_school_data = df[df['Activity'].str.contains('travel to school', case=False, na=False)]
total_travel_to_school_hours = travel_to_school_data['Duration in Hrs'].sum()
average_travel_to_school_hours = total_travel_to_school_hours / len(travel_to_school_data)

# Calculate the total "Travel to Home" hours
travel_to_home_data = df[df['Activity'].str.contains('go home', case=False, na=False)]
total_travel_to_home_hours = travel_to_home_data['Duration in Hrs'].sum()

# Calculate the average "Travel to Home" hours
average_travel_to_home_hours = total_travel_to_home_hours / len(travel_to_home_data)

# Calculate the total "Travel to Home" hours
travel_to_home_data = df[df['Activity'].str.contains('go home', case=False, na=False)]
total_travel_to_home_hours = travel_to_home_data['Duration in Hrs'].sum()

# Filter the data for "Travel to School" and "Go Home" activities
travel_data = df[df['Activity'].str.contains('travel to school', case=False, na=False) | df['Activity'].str.contains('go home', case=False, na=False)]

# Create a word cloud with a fully transparent background
wordcloud = WordCloud(width=600, height=500, background_color='white').generate(' '.join(df['Activity']))

# Convert the WordCloud image to Base64
buffer = io.BytesIO()
plt.figure(figsize=(6, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig(buffer, format='png')
plt.tight_layout(pad=0)
wordcloud_base64 = base64.b64encode(buffer.getvalue()).decode()

c1, c2, c3 = st.columns(3)

# Nested columns in c1
with c1:
    c1_col1, c1_col2 = st.columns([1, 1])

    # Add box shadow with the color fbb1bd and remove the border
    c1_col1.markdown(f"""
        <div style="height: 150px; padding: 20px; border-radius: 20px; background-color: #fbb1bd; box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5);">
            <div style="text-align: center; margin-top: 20px">
                <h3 style="line-height: 0.3;">Average Sleep:</h3>
                <h4 style="line-height: 0.3;">{average_sleep_hours:.2f} hours</h4>
            </div>
        </div>
    """, unsafe_allow_html=True)

    c1_col2.markdown(f"""
        <div style="height: 150px; padding: 20px; border-radius: 20px; background-color: #ff99ac; box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5);">
            <div style="text-align: center; margin-top: 20px">
                <h3 style="line-height: 0.3;">Average Study:</h3>
                <h4 style="line-height: 0.3;">{average_study_hours:.2f} hours</h4>
            </div>
        </div>
    """, unsafe_allow_html=True)


# Add the Location Check pie chart in a new row
with c1:
    st.markdown("<h3 style='text-align: center; margin-top: 20px'>Location Check</h3>", unsafe_allow_html=True)
    location_counts = df['Location'].value_counts().reset_index()
    location_counts.columns = ['Location', 'Count']
    
    # Define a custom color palette
    custom_colors = ['#EC0B43', '#fbb1bd', '#58355E', '#D6FFB7', '#ff5c8a', '#FFF689']
    
#     EC0B43
# 58355E
# 7AE7C7
# D6FFB7
# FFF689
    
    location_fig = px.pie(
        location_counts,
        names='Location',
        values='Count',
        title='',
        color_discrete_sequence=custom_colors  # Set the custom color palette
    )
    location_fig.update_layout(
        title_text='Where I Spent Portions of My Time',
        title_x=0.28,
        height=350,  # Set the height of the chart (in pixels)
        width=300,  # Set the width of the chart (in pixels)
    )
    st.plotly_chart(location_fig, use_container_width=True)
    
with c1:
    
    st.markdown("<h3 style='text-align: center; margin-top: 15px'>Hours of Sleep per Day</h3>", unsafe_allow_html=True)
    # Display the "Sleep Check" bar chart
    sleep_bar_fig = px.bar(
        sleep_data,
        x='Date',
        y='Duration in Hrs',
        title='How Many Hours Did I Sleep per Day in 2 Weeks?',
        labels={'Duration in Hrs': 'Hours'},  # Customize the y-axis label
        color_discrete_sequence=['#ff477e'],  # Set the bar color
    )

    # Customize the layout
    sleep_bar_fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Hours',
        title_x=0.18,  # Set the title position
        height=400,  # Set the height of the chart (in pixels)
        width=550,   # Set the width of the chart (in pixels)
        barmode='group',  # Set the bar mode to "group"
        xaxis=dict(
            categoryorder='category ascending',  # Display all dates
        ),
    )

    # Display the bar chart
    st.plotly_chart(sleep_bar_fig, use_container_width=False)


    



# Nested columns in c2
c2_col1, c2_col2 = c2.columns([1, 1])

# Add box shadow with the color fbb1bd and remove the border
c2_col1.markdown(f"""
    <div style="height: 150px; padding: 20px; border-radius: 20px; background-color: #ff7096; box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5);">
        <div style="text-align: center; margin-top: 1px">
            <h3 style="line-height: 1;">Average Travel to School:</h3>
            <h4 style="line-height: 0;">{average_travel_to_school_hours:.2f} hours</h4>
        </div>
    </div>
""", unsafe_allow_html=True)

c2_col2.markdown(f"""
    <div style="height: 150px; padding: 20px; border-radius: 20px; background-color: #ff5c8a; box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5);">
        <div style="text-align: center; margin-top: 1px">
            <h3 style="line-height: 1;">Average Travel to Home:</h3>
            <h4 style="line-height: 0;">{average_travel_to_home_hours:.2f} hours</h4>
        </div>
    </div>
""", unsafe_allow_html=True)

# Add the Feelings in a Pie chart in a new row
with c2:
    st.markdown("<h3 style='text-align: center; margin-top: 20px; margin-bottom: -10px'>Time of Sleep per Day</h3>", unsafe_allow_html=True)
    # Display the first "Sleep Check" chart
    df['Date'] = pd.to_datetime(df['Date'])
    sleep_data = df[df['Activity'] == 'sleep']

    # Customize the line color and style
    sleep_fig1 = px.line(
        sleep_data,
        x='Date',
        y='Time',
        title=''
    )
    sleep_fig1.update_layout(
        title_text='What Time Did I Sleep?',
        title_x=0.38,
        height=340,  # Set the height of the chart (in pixels)
        width=550,  # Set the width of the chart (in pixels)
    )

    # Use update_traces to customize the line appearance
    sleep_fig1.update_traces(
        line=dict(
            shape='linear',  # You can use 'linear', 'spline', or other values
            dash='solid',  # You can use 'solid', 'dash', 'dot', or other values
            color='#ff477e'  # Set the line color to blue
        )
    )

    sleep_fig1.update_xaxes(tickformat="%Y-%m-%d", tickvals=sleep_data['Date'].dt.date.unique())
    st.plotly_chart(sleep_fig1, use_container_width=False)

    
# Nested columns in c2
with c2:

    st.markdown("<h3 style='text-align: center; margin-top: 20px; margin-bottom: -10px'>Hours of Commute per School Day</h3>", unsafe_allow_html=True)

    # Specific dates from 10/09/2023 to 10/23/2023
    specific_dates = pd.date_range(start='2023-10-09', end='2023-10-23')

    # Filter the data for the "Go Home" and "Travel" activities
    go_home_data = df[df['Activity'].str.contains('go home', case=False, na=False)]
    travel_data = df[df['Activity'].str.contains('travel', case=False, na=False)]

    # Extract the common dates from both datasets
    common_dates = set(go_home_data['Date']).intersection(set(travel_data['Date']))

    # Filter the data to include only the common dates and specific dates
    go_home_data = go_home_data[go_home_data['Date'].isin(common_dates) | go_home_data['Date'].isin(specific_dates)]
    travel_data = travel_data[travel_data['Date'].isin(common_dates) | travel_data['Date'].isin(specific_dates)]

    # Create a grouped bar plot for "Travel" and "Go Home" activities on specific dates with hours
    fig = px.bar(travel_data, x='Date', y='Duration in Hrs', color_discrete_sequence=['#fbb1bd'], title='Hours I Spent Traveling to and from School', height=400, width=800)

    # Add "Go Home" data to the grouped bar plot with the custom color
    fig.add_trace(px.bar(go_home_data, x='Date', y='Duration in Hrs', color_discrete_sequence=['#ff5c8a'], title='Hours I Spend Traveling to and from School').data[0])

    # Customize the layout and axis labels
    fig.update_layout(
        xaxis=dict(
            categoryorder='category ascending',
            tickvals=specific_dates,
            ticktext=[date.strftime('%Y-%m-%d') for date in specific_dates]
        ),
        xaxis_title='Date',
        yaxis_title='Hours',
        title_x=0.22  # Set the title to the middle
    )
    fig.update_layout(barmode='group')  # Set the bar mode to "group" for grouped bars

    # Display the plot
    st.plotly_chart(fig, use_container_width=True)

    # Display a legend outside the plot
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 50px">
            <span style="background-color: #fbb1bd; border-radius: 5px; display: inline-block; padding: 5px 10px; margin-right: 10px;"></span> Travel to School
            <span style="background-color: #ff5c8a; border-radius: 5px; display: inline-block; padding: 5px 10px; margin-left: 20px; "></span> Go Home
        </div>
        """,
        unsafe_allow_html=True
    )



# Add box shadow with the color fbb1bd and remove the border
c3.markdown(f"""
    <div style="width: 630px; height: 560px; padding: 20px; border-radius: 20px; background-color: white; box-shadow: 5px 5px 10px #EC0B43;">
        <div style="text-align: center; margin-top: 15px">
            <h2 style="line-height: 1; color: #EC0B43; margin-bottom: -50px">My Activities Word Cloud</h2>
            <img src="data:image/png;base64,{wordcloud_base64}" alt="activity word cloud" />
        </div>
    </div>
""", unsafe_allow_html=True)

c3_col1, c3_col2 = c3.columns([1, 1])

# Nested columns in c3_col1
with c3_col1:
    st.markdown("<h3 style='text-align: center; margin-top: 55px; margin-bottom: -10px'>Student-Life Balance</h3>", unsafe_allow_html=True)
    
    # Filter the DataFrame for "review" activity
    study_data = df[df['Activity'].str.contains('review|class', case=False, na=False)]
    
    # Calculate the total study hours for "review"
    total_study_hours = study_data['Duration in Hrs'].sum()
    
    # Filter the DataFrame for "me-time (tiktok and social media)" activity
    me_time_data = df[df['Activity'].str.contains('me-time', case=False, na=False)]
    
    # Calculate the total "me-time" hours
    total_me_time_hours = me_time_data['Duration in Hrs'].sum()
    
    # Values for the pie chart
    values = [total_study_hours, total_me_time_hours]
    
    # Create a pie chart with custom colors and move the legend below
    fig = go.Figure(data=[go.Pie(labels=['Student Life', 'Me-time'], values=values, marker=dict(colors=['#EC0B43', '#fbb1bd']))])
    
    # Calculate the percentages
    percentages = [f'{val / sum(values) * 100:.2f}%' for val in values]
    
    # Customize the layout and move the legend below
    fig.update_layout(
        title='Hours Being Me and a Student',
        title_x=0.12,
        height=400,  # Set the height of the chart (in pixels)
        width=300,  # Set the width of the chart (in pixels)
        legend=dict(orientation='h', x=0.14, y=-0.2)  # Move the legend below (horizontal orientation)
    )
    
    # Update the pie chart labels with percentages (bold)
    fig.update_traces(textinfo='percent', textfont_size=14)
    
    # Display the pie chart
    st.plotly_chart(fig, use_container_width=True)

# Nested columns in c3_col2
with c3_col2:
    st.markdown("<h3 style='text-align: center; margin-top: 55px'>Feelings Distribution</h3>", unsafe_allow_html=True)
    
    
    feelings_counts = df['Feelings'].value_counts().reset_index()
    feelings_counts.columns = ['Feelings', 'Count']
    
    # Get the top 6 feelings
    top_6_feelings = feelings_counts.head(6)
    # Create a pie chart for "Feelings" with custom colors and move the legend below
    feelings_fig = px.pie(
        top_6_feelings,
        names='Feelings',
        values='Count',
        title='How I Felt From Time to Time',
        color_discrete_sequence=custom_colors  # Set the custom color palette
    )
    
    # Customize the layout and move the legend below
    feelings_fig.update_layout(
        title_x=0.12,
        height=400,  # Set the height of the chart (in pixels)
        width=300,  # Set the width of the chart (in pixels)
        legend=dict(orientation='h', y=-0.2),  # Move the legend below (horizontal orientation)
    )
    
    # Update the pie chart labels with percentages (bold)
    feelings_fig.update_traces(textinfo='percent', textfont_size=14)
    
    # Display the pie chart
    st.plotly_chart(feelings_fig, use_container_width=True)


# Define your custom color palette
custom_colors = ["#fbb1bd", "#ff99ac", "#ff7096", "#ff5c8a", "#ff477e"]

# fbb1bd
# ff99ac
# ff85a1
# ff7096
# ff5c8a
# ff477e



st.markdown("---")

