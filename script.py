# Import packages
import requests
from PyDyTuesday import get_date
import pandas as pd
import plotnine as p9
from plotnine import ggplot, geom_boxplot, theme_minimal, geom_map, aes, theme, scale_fill_gradient, theme_void, element_text, element_rect
import matplotlib.font_manager as fm
from great_tables import GT, md, html

# Import font
prop = fm.FontProperties(fname='Gelasio-VariableFont_wght.ttf')

# Download TidyTuesday data
# get_date('2025-01-28')

# Clean data
wi_2023 = pd.read_csv('water_insecurity_2023.csv')
wi_2023['state'] = wi_2023['name'].str.rsplit(', ', n=1).str[-1]

# Filter for western states
west_states = ['Washington', 'Oregon', 'California', 'Idaho', 'Nevada', 'Utah', 'Arizona', 'Montana', 'Wyoming', 'Colorado', 'New Mexico', 'North Dakota', 'South Dakota', 'Nebraska', 'Kansas', 'Oklahoma', 'Texas', 'Minnesota', 'Iowa', 'Missouri', 'Arkansas', 'Louisiana']
wi_west_2023 = wi_2023[wi_2023['state'].isin(west_states)]