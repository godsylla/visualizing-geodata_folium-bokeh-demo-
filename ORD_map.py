import pandas as pd

path = '/home/'
# /home/ec2-user/ord/hours_aps_ord
hours_aps_ord = pd.read_pickle('../data/processed/hours_aps_ord') # need to revise path - log onto EC2 and cp files back over

from bokeh.io import output_file, show, save, curdoc
from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, Range1d, PanTool, 
    WheelZoomTool, BoxSelectTool, LinearColorMapper, ContinuousColorMapper, LogColorMapper, HoverTool,
    Plot, Circle, LinearAxis, Text,
    SingleIntervalTicker, Slider, CustomJS, Select
)
from bokeh.palettes import Reds5, Blues9 as blu
from bokeh.layouts import column, row, widgetbox
from bokeh.models.widgets import Slider


source = ColumnDataSource(data={
    'long'  : hours_aps_ord.long,
    'lat'   : hours_aps_ord.lat,
    'clients' : hours_aps_ord.client_mac_address,
    'size': hours_aps_ord.client_mac_address_sized,
    'time': hours_aps_ord.session_time_m,
    'ap': hours_aps_ord.ap_mac,
    'avg_time': hours_aps_ord.avg_time_client
})



map_options = GMapOptions(lat=41.977170, lng=-87.903596, map_type="roadmap", zoom=16)

plot = GMapPlot(x_range=Range1d(), y_range=Range1d(), 
                map_options=map_options, plot_width=900, plot_height=800)
plot.title.text = "O'Hare Airport (ORD)"
plot.api_key = ""

# map colors to session time
mapper = LogColorMapper(
    palette=blu,
    low=hours_aps_ord.avg_time_client.min(),
    high=hours_aps_ord.avg_time_client.max()
)

# define circles
circle = Circle(x="long", y="lat", size='size', 
                fill_color={'field': 'avg_time', 'transform': mapper}, 
                fill_alpha=1, line_color=None)

# add circles and source to plot
plot.add_glyph(source, circle)

# add interactive tools to plot
hover = HoverTool(tooltips=[("number of passengers", '@clients'), 
                    ("avg minutes per passenger", '@avg_time')],
                    )

plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool(), hover)


# Make a slider object
slider = Slider(start=0, end=23, value=0, step=1, title="Time") # this breaks when index of df is datetime/string, not 0-23 numeric!

# make a dropdown object
select = Select(
    options=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 
    value='Monday', title="Day")


# Define the callback function
def update_plot(attr, old, new):
    new_h = slider.value
    new_hour = {
             'long'  : hours_aps_ord.loc[hours_aps_ord['hour']==new_h].long,
             'lat'   : hours_aps_ord.loc[hours_aps_ord['hour']==new_h].lat,
             'clients' : hours_aps_ord.loc[hours_aps_ord['hour']==new_h].client_mac_address,
             'size': hours_aps_ord.loc[hours_aps_ord['hour']==new_h].client_mac_address_sized,
             'time': hours_aps_ord.loc[hours_aps_ord['hour']==new_h].session_time_m,
             'ap': hours_aps_ord.loc[hours_aps_ord['hour']==new_h].ap_mac,
             'avg_time': hours_aps_ord.loc[hours_aps_ord['hour']==new_h].avg_time_client
         }

   
    source.data = new_hour
    
# Attach the callback to the 'value' property of slider
slider.on_change('value', update_plot)

def callack(attr, old, new):
    if new == 'Monday': 
        source.data = {
             'long'  : hours_aps_ord.loc[hours_aps_ord['date']==22].long,
             'lat'   : hours_aps_ord.loc[hours_aps_ord['date']==22].lat,
             'clients' : hours_aps_ord.loc[hours_aps_ord['date']==22].client_mac_address,
             'size': hours_aps_ord.loc[hours_aps_ord['date']==22].client_mac_address_sized,
             'time': hours_aps_ord.loc[hours_aps_ord['date']==22].session_time_m,
             'ap': hours_aps_ord.loc[hours_aps_ord['date']==22].ap_mac,
             'avg_time': hours_aps_ord.loc[hours_aps_ord['date']==22].avg_time_client
        }
    elif new == 'Tuesday': 
        source.data = {
             'long'  : hours_aps_ord.loc[hours_aps_ord['date']==23].long,
             'lat'   : hours_aps_ord.loc[hours_aps_ord['date']==23].lat,
             'clients' : hours_aps_ord.loc[hours_aps_ord['date']==23].client_mac_address,
             'size': hours_aps_ord.loc[hours_aps_ord['date']==23].client_mac_address_sized,
             'time': hours_aps_ord.loc[hours_aps_ord['date']==23].session_time_m,
             'ap': hours_aps_ord.loc[hours_aps_ord['date']==23].ap_mac,
             'avg_time': hours_aps_ord.loc[hours_aps_ord['date']==23].avg_time_client
        }
    elif new == 'Wednesday': 
        source.data = {
             'long'  : hours_aps_ord.loc[hours_aps_ord['date']==24].long,
             'lat'   : hours_aps_ord.loc[hours_aps_ord['date']==24].lat,
             'clients' : hours_aps_ord.loc[hours_aps_ord['date']==24].client_mac_address,
             'size': hours_aps_ord.loc[hours_aps_ord['date']==24].client_mac_address_sized,
             'time': hours_aps_ord.loc[hours_aps_ord['date']==24].session_time_m,
             'ap': hours_aps_ord.loc[hours_aps_ord['date']==24].ap_mac,
             'avg_time': hours_aps_ord.loc[hours_aps_ord['date']==24].avg_time_client
        }
    elif new == 'Thursday': 
        source.data = {
             'long'  : hours_aps_ord.loc[hours_aps_ord['date']==25].long,
             'lat'   : hours_aps_ord.loc[hours_aps_ord['date']==25].lat,
             'clients' : hours_aps_ord.loc[hours_aps_ord['date']==25].client_mac_address,
             'size': hours_aps_ord.loc[hours_aps_ord['date']==25].client_mac_address_sized,
             'time': hours_aps_ord.loc[hours_aps_ord['date']==25].session_time_m,
             'ap': hours_aps_ord.loc[hours_aps_ord['date']==25].ap_mac,
             'avg_time': hours_aps_ord.loc[hours_aps_ord['date']==25].avg_time_client
        }
    elif new == 'Friday': 
        source.data = {
             'long'  : hours_aps_ord.loc[hours_aps_ord['date']==19].long,
             'lat'   : hours_aps_ord.loc[hours_aps_ord['date']==19].lat,
             'clients' : hours_aps_ord.loc[hours_aps_ord['date']==19].client_mac_address,
             'size': hours_aps_ord.loc[hours_aps_ord['date']==19].client_mac_address_sized,
             'time': hours_aps_ord.loc[hours_aps_ord['date']==19].session_time_m,
             'ap': hours_aps_ord.loc[hours_aps_ord['date']==19].ap_mac,
             'avg_time': hours_aps_ord.loc[hours_aps_ord['date']==19].avg_time_client
        }
    elif new == 'Saturday': 
        source.data = {
             'long'  : hours_aps_ord.loc[hours_aps_ord['date']==20].long,
             'lat'   : hours_aps_ord.loc[hours_aps_ord['date']==20].lat,
             'clients' : hours_aps_ord.loc[hours_aps_ord['date']==20].client_mac_address,
             'size': hours_aps_ord.loc[hours_aps_ord['date']==20].client_mac_address_sized,
             'time': hours_aps_ord.loc[hours_aps_ord['date']==20].session_time_m,
             'ap': hours_aps_ord.loc[hours_aps_ord['date']==20].ap_mac,
             'avg_time': hours_aps_ord.loc[hours_aps_ord['date']==20].avg_time_client
        }
    else:
        source.data = {
             'long'  : hours_aps_ord.loc[hours_aps_ord['date']==21].long,
             'lat'   : hours_aps_ord.loc[hours_aps_ord['date']==21].lat,
             'clients' : hours_aps_ord.loc[hours_aps_ord['date']==21].client_mac_address,
             'size': hours_aps_ord.loc[hours_aps_ord['date']==21].client_mac_address_sized,
             'time': hours_aps_ord.loc[hours_aps_ord['date']==21].session_time_m,
             'ap': hours_aps_ord.loc[hours_aps_ord['date']==21].ap_mac,
             'avg_time': hours_aps_ord.loc[hours_aps_ord['date']==21].avg_time_client
        }

select.on_change('value', callack)

# Make a layout of slider and plot and add it to the current document
layout = column(plot, select, slider)
curdoc().add_root(layout)
