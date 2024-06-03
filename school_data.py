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

def prepare_data():
    """
    Reads data from a CSV file, processes school information, and reshapes year data into a structured format.

    The function performs the following steps:
    1. Reads the CSV file located at 'specifications/Assignment3Data.csv' into a pandas DataFrame.
    2. Extracts unique school names and codes from the DataFrame and creates a dictionary mapping each school name to its code.
    3. Reshapes yearly data arrays into a specific format and combines them into a single array.

    Returns:
        tuple: A tuple containing:
            - data (numpy.ndarray): A 3D numpy array where each element is a reshaped year array.
            - schools (dict): A dictionary mapping school names (str) to school codes (str).

    Example:
        data, schools = prepare_data()
    """

    # read School names and codes from the .csv file and combine them into a dict named schools
    file_path = 'specifications/Assignment3Data.csv'
    df = pd.read_csv(file_path)

    school_names = list(df['School Name'].unique())
    school_codes = list(df['School Code'].unique())
    schools = dict(zip(school_codes, school_names))

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

    # reshape data into a 3D np.array named data
    all_years_reshaped = [np.array(year).reshape(20, 3) for year in all_years]
    data = np.array(all_years_reshaped, dtype=int)

    # Create 3 dicts to store the labels of the data in the 3D array
    # each dict will have the user friendly version of the data as the key
    # and the index as the value. This will allow an easier way to access the data
    # which should make the code much more readable
    # Ex. Grade 11 data is stored in the 3D array, 3rd dimension, index 1
    #     So the grade_labels dict can easily find the index 1 of grade 11 data
    #     with grade_labels[11] (which will return 1)

    # first we 
    # year_labels = [year for year in range(2013, 2023)]
    year_labels = dict(zip(range(2013, 2023), range(10)))
    grade_labels = {10: 0, 11: 1, 12: 2}
    school_labels = dict(zip(school_codes, range(20)))

    return data, schools, year_labels, grade_labels, school_labels

def main():
    # Format to access items in the 3D array is 
    # data[year_index, school_index, grade_index]

    # Format to access a single item in the 3D array using the label dicts is
    # data[year_labels[year]], school_labels[school], grade_labels[grade])

    # Example to access all years for a given school and grade
    # data[:, school_labels[school], grade_labels[grade])



    print("ENSF 692 School Enrollment Statistics")

    # Print Stage 1 requirements here
    data, schools, year_labels, grade_labels, school_labels = prepare_data()
    print(f'Shape of full data array:  {data.shape}')
    print(f'Dimensions of full data array:  {data.ndim}')

    # Prompt for user input

    # print(data)
    print(schools.items())

    while True:
        try: 
            # input_high_school = input("Please enter the high school name or"
                                    # " school code: ").strip()
            # FIX ME LATER!!
            input_high_school = 9857
            if int(input_high_school) in schools.keys():
                print("school found")
                school_name = schools[int(input_high_school)]
                school_code = int(input_high_school)
                break
            elif input_high_school in schools.values():
                print("school found")
                for key, value in schools.items():
                    if input_high_school == value:
                        school_name = input_high_school
                        school_code = key
                break
            else:
                raise ValueError
        except ValueError:
            print('You must enter a valid school name or code.')
    
    # print(input_high_school)

    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")
    print(f"School Name: {school_name}, School Code: {school_code}")
 
    # Prints mean enrollment for grades 10, 11, and 12
    for grade, grade_index in grade_labels.items():
        mean_enrollment = int(np.mean(data[:, school_labels[school_code], grade_index]))
        print(f'Mean enrollment for Grade {grade}: {mean_enrollment}')

    max_enrollment = int(np.max(data[:, school_labels[school_code], :]))
    print(f'Highest enrollment for a single grade: {max_enrollment}')
    min_enrollment = int(np.min(data[:, school_labels[school_code], :]))
    print(f'Lowest enrollment for a single grade: {min_enrollment}')
                         

    # print(data[:, school_labels[school_code], :])

    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")


if __name__ == '__main__':
    main()

