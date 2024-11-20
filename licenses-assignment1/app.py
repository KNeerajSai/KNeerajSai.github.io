# Import required libraries
import pandas as pd
import altair as alt

# Allow larger datasets for Altair
alt.data_transformers.disable_max_rows()

# Load the dataset
url = "https://github.com/UIUC-iSchool-DataViz/is445_data/raw/main/licenses_fall2022.csv"
data = pd.read_csv(url)

# Preprocess the data
data['Expiration Date'] = pd.to_datetime(data['Expiration Date'], errors='coerce')
data = data.dropna(subset=['Expiration Date', 'License Type'])
data['year'] = data['Expiration Date'].dt.year

# --------------------------------------
# Interactivity: Filters for License Types and Years
# --------------------------------------
# Create dropdown filter for license type
license_type_dropdown = alt.binding_select(options=data['License Type'].unique().tolist(), name='License Type: ')
license_type_selection = alt.selection_single(fields=['License Type'], bind=license_type_dropdown, empty='all')

# Create slider filter for years
year_slider = alt.binding_range(min=int(data['year'].min()), max=int(data['year'].max()), step=1, name='Year Range: ')
year_selection = alt.selection_single(fields=['year'], bind=year_slider, empty='all')

# --------------------------------------
# Visualization 1: Advanced Bar Chart for Licenses by Type
# --------------------------------------
bar_chart = alt.Chart(data).mark_bar().encode(
    x=alt.X('License Type:N', title='License Type', sort='-y'),
    y=alt.Y('count():Q', title='Number of Licenses'),
    color=alt.Color('License Type:N', legend=None),
    tooltip=['License Type:N', 'count():Q']
).add_selection(
    license_type_selection
).transform_filter(
    license_type_selection
).properties(
    title="Number of Licenses by Type (Filtered)",
    width=600,
    height=400
)

# --------------------------------------
# Visualization 2: Interactive Line Chart for Licenses Over Time
# --------------------------------------
line_chart = alt.Chart(data).mark_line(point=True).encode(
    x=alt.X('year:O', title='Year'),
    y=alt.Y('count():Q', title='Number of Licenses'),
    color=alt.Color('License Type:N', title='License Type'),
    tooltip=['year:O', 'License Type:N', 'count():Q']
).add_selection(
    year_selection
).transform_filter(
    year_selection
).properties(
    title="Number of Licenses Issued Over Time (Filtered)",
    width=600,
    height=400
).interactive()

# --------------------------------------
# Statistics and Summary
# --------------------------------------
# Calculate total licenses and top license type
total_licenses = data.shape[0]
top_license_type = data['License Type'].value_counts().idxmax()
top_license_count = data['License Type'].value_counts().max()

# Display statistics
print(f"Total Licenses Issued: {total_licenses}")
print(f"Most Common License Type: {top_license_type} ({top_license_count} licenses)")

# --------------------------------------
# Save the Visualizations as HTML
# --------------------------------------
bar_chart.save("licenses_by_type_filtered.html")
line_chart.save("licenses_over_time_filtered.html")

print("Visualizations saved as 'licenses_by_type_filtered.html' and 'licenses_over_time_filtered.html'.")
