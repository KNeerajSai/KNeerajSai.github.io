# Licenses Dataset Analysis

## Project Description
This project analyzes the Licenses Dataset using Python, Altair, and Vega-Lite. Two visualizations are created to explore the data:
1. A bar chart showing the number of licenses by type.
2. A line chart tracking the number of licenses issued over time.

## Visualizations
- [Licenses by Type (Bar Chart)](https://kneerajsai.github.io/licenses-assignment/licenses_by_type_filtered.html)
- [Licenses Over Time (Line Chart)](https://kneerajsai.github.io/licenses-assignment/licenses_over_time_filtered.html)

## Dataset
The dataset used for this analysis is publicly available:
- [Licenses Dataset](https://github.com/UIUC-iSchool-DataViz/is445_data/raw/main/licenses_fall2022.csv)

## Analysis
The Python notebook used for this project is available here:
- [Analysis Notebook](https://github.com/KNeerajSai/licenses-assignment/blob/main/app.py)

## Visualization Details
### 1. Licenses by Type (Bar Chart)
- **Description**: This bar chart shows the number of licenses issued for each license type.
- **Design Choices**:
  - X-axis: License type (categorical).
  - Y-axis: Number of licenses (quantitative).
  - Color: License type to visually differentiate categories.
- **Interactivity**:
  - Tooltips show the exact count for each license type when hovering over a bar.
- **Data Transformations**:
  - Aggregated data to calculate the total number of licenses for each type.

### 2. Licenses Over Time (Line Chart)
- **Description**: This line chart displays the trend of licenses issued over time, grouped by type.
- **Design Choices**:
  - X-axis: Year (temporal).
  - Y-axis: Number of licenses (quantitative).
  - Color: License type to distinguish trends.
- **Interactivity**:
  - Tooltips display the year, license type, and exact count for each point.
  - Pan and zoom functionality allow for detailed exploration of the data.
- **Data Transformations**:
  - Aggregated data by year and license type.

## How to Reproduce
1. Clone the repository:
   ```bash
   git clone https://github.com/KNeerajSai/licenses-assignment.git
