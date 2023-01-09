# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 10:52:53 2023

@author: xxu
"""
#Import the required packages
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, CategoricalColorMapper
from bokeh.plotting import figure
from bokeh.palettes import Spectral5
import pandas as pd
from bokeh.models import HoverTool
#Read the data into the notebook
df = pd.read_csv('all_stocks_5yr.csv')
df['date'] = pd.to_datetime(df['date']).apply(lambda x:x.strftime('%Y'))
#List the tech giants
tech_giants = ['GOOGL', 'FB', 'MSFT', 'AMZN', 'AAPL']
#Create the color map
color_map = CategoricalColorMapper(factors = tech_giants, palette = Spectral5)
#Create the ColumnDataSource Object
data = ColumnDataSource(data = {
'high' : df[df['date'] == '2013'].high,
'low' : df[df['date'] == '2013'].low,
'open' : df[df['date'] == '2013'].open,
'close': df[df['date'] == '2013'].close,
'volume': df[df['date'] == '2013'].volume,
'Name' : df[df['date'] == '2013'].Name
})
#Create ranges for the x and y axis
xmin, xmax = min(df.high), max(df.high)
ymin, ymax = min(df.volume), max(df.volume)
#Create the hover tool
hover_tool = HoverTool(tooltips = [('Company:', '@Name')])
#Create the plot
plot = figure(title = 'Volume traded Vs. High Prices', plot_height = 400, plot_width
= 700, x_range = (xmin, xmax),
y_range = (ymin, ymax))
plot.diamond(x = 'high', y = 'volume', source = data, color = dict(field = 'Name',
transform = color_map))
#Adding the hover tool to the plot
plot.add_tools(hover_tool)
plot.xaxis.axis_label = 'High Prices for 2013'
plot.yaxis.axis_label = 'Volume traded in 2013'
#Add the plot to the application
curdoc().add_root(plot)
curdoc().title = 'Volume and High prices of stocks'