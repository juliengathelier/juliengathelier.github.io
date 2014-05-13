# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from pandas import read_json, set_option

set_option('display.max_columns', 500)
cal = read_json("http://www.elysee.fr/chronologie/download/json",convert_dates=False)
cal

# <codecell>

from geopandas import GeoSeries, GeoDataFrame
from geopandas.geocode import geocode as gc
import time
import random

latlon = []
for i in range(len(cal["place"])):
    place = gc(cal["place"][i])
    latlon.append(place)
    print place #to see if it's working
    time.sleep(random.randrange(1,5))

latlon

# <codecell>


