# Synoptic charts for the EUREC4A field campaign

With this package you can add synoptic charts to any cartographic matplotlib
plot. The charts were provided by Cécile MARIE-LUCE at Meteo-France, Guadeloupe
and generated as part of the [forecasting
testbed](http://eurec4a.uk/forecast_testbed/) during the
[EUREC4A](https://eurec4a.eu/) field-campaign by the
[EUREC4A-UK](https://eurec4a.uk/) team. The synoptic charts were created from
analysis at 00:00UTC and cover January 1st to February 29th 2020.


## Installation

The package can be installed with pip from pypi

```bash
python -m pip install eurec4a_synop
```

To use it simply import `eurec4a_synop` and call `add_synop`

```python
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import eurec4a_synop

crs = ccrs.AzimuthalEquidistant(central_latitude=10.0, central_longitude=-45.0)
fig, ax = plt.subplots(subplot_kw=dict(projection=crs), figsize=(14, 16))

ax.set_extent([-80, -10, 0, 30], crs=ccrs.PlateCarree())
add_synop(ax=ax, date=datetime.datetime(year=2020, month=2, day=2))
ax.coastlines()
ax.gridlines(draw_labels=True)

```

![](docs/example_plot.png)
