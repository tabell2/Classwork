# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Tyler Abell
# Section: ENGR-102:538,560
# Assignment: LAB 12b
# Date: 17 Nov 2025

import numpy as np
import matplotlib.pyplot as plt


def read_data():
    # Read in the data from the file
    WxData = "WeatherDataCLL.csv"
    data = {}
    data_list = []
    with open(WxData, 'r') as file:
        next(file)
        # check for null/invalid data
        for line in file:
            parts = line.strip().split(',')
            if len(parts) != 8 or any(part == '' for part in parts):
                continue
            data = {
                'date': parts[0],
                'max_temp': float(parts[5]),
                'min_temp': float(parts[6]),
                'avg_temp': float(parts[2]),
                'total_precip': float(parts[7]),
                'avg_wind_speed': float(parts[4]),
                'avg_humidity': float(parts[3])
            }
            data_list.append(data)
    return data_list


# 1) Line graph of max temperature and average wind speed
# Create a line graph that shows both the maximum temperature and average wind speed plotted
# over the period of time. Both lines should be plotted on the same graph, with date on the x-axis,
# and different y axes for the two different measurements. (Please do not spend time dealing
# with “date data type.” Please just consider the dates in the data to be strings, or, you may
# simply consider the days as integers for plotting.)

def line_graph(data_list):
    dates = [data['date'] for data in data_list]
    max_temps = [data['max_temp'] for data in data_list]
    avg_wind_speeds = [data['avg_wind_speed'] for data in data_list]

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Max Temperature (°F)', color=color)
    ax1.plot(dates, max_temps, color=color, label='Max Temperature')
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Average Wind Speed (mph)', color=color)
    ax2.plot(dates, avg_wind_speeds, color=color, label='Average Wind Speed')
    ax2.tick_params(axis='y', labelcolor=color)

    plt.title('Max Temperature and Average Wind Speed Over Time')
    fig.tight_layout()
    # create legend
    artists = ax1.get_lines() + ax2.get_lines()
    labels = [line.get_label() for line in artists]
    plt.legend(artists, labels, loc='lower left')
    plt.show()


# 2) Histogram of average wind speed
# Create a histogram of the average wind speed. The x-axis should cover a reasonable range of
# average wind speeds, and the y-axis should show the number of days that had an average wind
# speed in the specific range.
def histogram_avg_wind_speed(data_list):
    avg_wind_speeds = [data['avg_wind_speed'] for data in data_list]

    plt.figure()
    plt.hist(avg_wind_speeds, bins=20, color='g', edgecolor='black')
    plt.title('Histogram of Average Wind Speed')
    plt.xlabel('Average Wind Speed (mph)')
    plt.ylabel('Number of Days')
    plt.show()


# 3) Scatterplot of average wind speed vs minimum temperature
# Create a scatterplot indicating the relationship (or lack thereof) between average wind speed
# and minimum temperature (one on each axis).
def scatterplot_wind_vs_min_temp(data_list):
    avg_wind_speeds = [data['avg_wind_speed'] for data in data_list]
    min_temps = [data['min_temp'] for data in data_list]

    plt.figure()
    plt.scatter(min_temps, avg_wind_speeds, color='m')
    plt.title('Scatterplot of Average Wind Speed vs Minimum Temperature')
    plt.xlabel('Minimum Temperature (°F)')
    plt.ylabel('Average Wind Speed (mph)')
    plt.show()


# 4) Bar chart of average temperature per month with highest high and lowest low
# Create a bar chart, with one bar per calendar month (each month from all 3 years), showing the
# average temperature, along with lines indicating the highest high and lowest low temperatures
# from that month.
# a. Note: You may want to create new lists of data, but you may find it useful to use the
# max/min/sum functions on lists.
# b. This is a great problem to practice using dictionaries!
def bar_chart_avg_temp_per_month(data_list):
    monthly_data = {}

    for data in data_list:
        month = data['date'].split('/')[0]
        if month not in monthly_data:
            monthly_data[month] = {
                'avg_temps': [],
                'max_temp': [],
                'min_temp': []
            }
        monthly_data[month]['avg_temps'].append(data['avg_temp'])
        monthly_data[month]['max_temp'].append(data['max_temp'])
        monthly_data[month]['min_temp'].append(data['min_temp'])

    # Convert month keys (strings like '1') to sorted integers for plotting,
    # but use the string keys when indexing the dictionary.
    months_int = sorted(int(m) for m in monthly_data.keys())
    avg_temps = [np.mean(monthly_data[str(month)]['avg_temps']) for month in months_int]
    max_temps = [max(monthly_data[str(month)]['max_temp']) for month in months_int]
    min_temps = [min(monthly_data[str(month)]['min_temp']) for month in months_int]

    plt.bar(months_int, height=avg_temps, color='c', label='Average Temperature')
    plt.plot(months_int, max_temps, color='r', marker='o', label='Highest High Temperature')
    plt.plot(months_int, min_temps, color='b', marker='o', label='Lowest Low Temperature')
    plt.title('Average Temperature per Month with Highest High and Lowest Low')
    plt.xlabel('Month')
    # set tick positions
    plt.xticks(months_int)
    plt.ylabel('Temperature (°F)')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    data_list = read_data()
    line_graph(data_list)
    histogram_avg_wind_speed(data_list)
    scatterplot_wind_vs_min_temp(data_list)
    bar_chart_avg_temp_per_month(data_list)
