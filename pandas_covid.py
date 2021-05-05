import pandas as pd
import matplotlib.pyplot as plt


illinois_covid_numbers = pd.read_json(
    path_or_buf='https://idph.illinois.gov/DPHPublicInformation/api/COVIDExport/GetIllinoisCases')


#illi_nums = pd.DataFrame(illinois_covid_numbers)

#pd.plotting.andrews_curves(illi_nums, 'confirmed_cases')
illinois_covid_numbers.plot.pie(figsize=(6, 6))
plt.show()
