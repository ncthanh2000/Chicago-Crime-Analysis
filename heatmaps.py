#Takes input as a normal dataframe, convert dataframe into json file to plot using bokeh
def heatmap(_gdf, _feature):
    import pandas as pd
    import numpy as np
    import json
    col = _gdf[_feature]
    max_val = np.max(col.to_numpy())
    merged_json = json.loads(_gdf.to_json())
    json_data = json.dumps(merged_json)
    geopd_heatmap_plot(json_data, _feature, max_val)

#Takes input as a json file and features, as well as maxvalue for scale when used in the colormap
def geopd_heatmap_plot(_gdf, _feature, _max_val):
    import json
    import pandas as pd
    import numpy as np
    import bokeh as bk
    from bokeh.io import output_notebook, show, output_file,export_png
    from bokeh.plotting import figure#, save
    from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar
    from bokeh.palettes import brewer, inferno, Plasma
    max_val = _max_val

    #Input GeoJSON source that contains features for plotting.
    geosource = GeoJSONDataSource(geojson = _gdf)

    #Define a sequential multi-hue color palette.
    palette = brewer['YlGnBu'][9]
    #palette = Plasma[10]
    #palette = inferno(10)

    #Reverse color order so that dark blue is highest obesity.
    palette = palette[::-1]
    #Instantiate LinearColorMapper that linearly maps numbers in a range, into a sequence of colors.
    color_mapper = LinearColorMapper(palette = palette, low = 0*max_val, high = 1*max_val)
    #Define custom tick labels for color bar.
    #tick_labels = {'0': '0%', '0.05': '5%', '0.10':'10%', '0.15':'15%', '0.20':'20%', 
    #               '0.25':'25%', '0.30':'30%','0.35':'35%', '0.40': '40%'}
    #Create color bar. 
    color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8,width = 500, height = 20,
                border_line_color=None,location = (0,0),
                orientation = 'horizontal')#, major_label_overrides = tick_labels)
    #Create figure object.
    p = figure(title = _feature, plot_height = 500 , plot_width = 500, 
                toolbar_location = None, x_axis_label='Longitude',
                y_axis_label='Latitude'
        )
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None
    #Add patch renderer to figure. 
    p.patches('xs','ys', source = geosource,
              fill_color = {'field' : _feature, 'transform' : color_mapper},
              line_color = 'black', line_width = 0.25, fill_alpha = 1)
    #Specify figure layout.
    p.add_layout(color_bar, 'below')
    p.title.text = _feature
    p.title.align = "center"
    #Display figure inline in Jupyter Notebook.
    output_notebook()
    #Display figure.
    show(p)
    #Export png
    #export_png(p, filename="heatmapplots\\"+str(_feature)+".png")