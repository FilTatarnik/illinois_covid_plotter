# Importing dependencies
import pandas as pd
import matplotlib.pyplot as plt

# Reading JSON Object of Total_Tested
illinois_covid_numbers = pd.read_json(
    path_or_buf='https://idph.illinois.gov/DPHPublicInformation/api/COVIDExport/GetIllinoisCases')

# Plotting Data from 5 different sources
illinois_covid_numbers.plot(figsize=(6, 6), subplots=True)

# Showing plotted data
plt.show()
