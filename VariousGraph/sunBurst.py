# import plotly.express as px
# import pandas as pd
# data = [
#     ['Wii Sports', 82.53, 'Wii', 82.53],
#     ['Mario Kart Wii', 35.52, 'Wii', 35.52],
#     ['Wii Sports Resort', 32.77, 'Wii', 32.77],
#     ['New Super Mario Bros.', 29.8, 'DS', 29.8],
#     ['Wii Play', 28.92, 'Wii', 28.92],
#     ['New Super Mario Bros. Wii', 28.32, 'Wii', 28.32],
#     ['Mario Kart DS', 23.21, 'DS', 23.21],
#     ['Wii Fit', 22.7, 'Wii', 22.7],
#     ['Kinect Adventures!', 21.81, 'X360', 21.81],
#     ['Wii Fit Plus', 21.79, 'Wii', 21.79],
#     ['Grand Theft Auto V', 21.04, 'PS3', 21.04]
# ]

# df = pd.DataFrame(data, columns=['Name', 'Global_Sales', 'parent', 'value'])

# fig = px.sunburst(df, path=['parent', 'Name'], values='value')
# fig.show()

# import pandas as pd
# import plotly.express as px

# # Read the CSV file into a DataFrame
# df = pd.read_csv('../Data/Sunburst2.csv')

# # Create the Sunburst chart
# fig = px.sunburst(df, path=['parent', 'id'], values='value')

# # Update the layout
# fig.update_layout(
#     title='Game Sales Sunburst Chart',
#     title_x=0.5,
#     width=800,
#     height=800
# )

# # Show the plot
# fig.show()


import pandas as pd
import plotly.express as px

# Read the CSV file into a DataFrame
df = pd.read_csv('../Data/Sunburst.csv')

# Create the Sunburst chart
fig = px.sunburst(df, path=['parent', 'id'], values='value')

# Update the layout
fig.update_layout(
    title='Game Sales Sunburst Chart',
    title_x=0.5,
    width=800,
    height=800
)

# Save the plot as an HTML file with interactivity
fig.write_html("sunburstHelper.html")

