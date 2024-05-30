# school_data.py
# AUTHOR NAME
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


import numpy as np
import pandas as pd
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Declare any global variables needed to store the data here


# You may add your own additional classes, functions, variables, etc.

def massage_data():
    file_path = 'specifications/Assignment3Data.csv'
    df = pd.read_csv(file_path)

    school_names = list(df['School Name'].unique())
    school_codes = list(df['School Code'].unique())
    schools = dict(zip(school_names, school_codes))

    all_years = [year_2013,
                 year_2014,
                 year_2015,
                 year_2016,
                 year_2017,
                 year_2018,
                 year_2019,
                 year_2020,
                 year_2021,
                 year_2022]

    all_years_reshaped = [np.array(year).reshape(20, 3) for year in all_years]
    data = np.array(all_years_reshaped)
    return data, schools

def main():
    print("ENSF 692 School Enrollment Statistics")

    # Print Stage 1 requirements here
    data, schools = massage_data()
    print(f'Shape of full data array:  {data.shape}')
    print(f'Dimensions of full data array:  {data.ndim}')

    # Prompt for user input

    print(schools.items())

    while True:
        try: 
            input_high_school = input("Please enter the high school name or"
                                    " school code: ").strip()
            if input_high_school in schools.keys() or \
               int(input_high_school) in schools.values():
                print("school found")
                break
            else:
                raise ValueError
        except ValueError:
            print('You must enter a valid school name or code.')
    
    print(input_high_school)

    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")

    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")


if __name__ == '__main__':
    main()

