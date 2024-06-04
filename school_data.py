# school_data.py
# AUTHOR NAME: Andy Allard

import numpy as np
import pandas as pd
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, \
                       year_2018, year_2019, year_2020, year_2021, year_2022


def prepare_data():
    """
    Reads data from a CSV file, processes school information, generates a 3D data array and 
    generates "label" dictionaries

    The function performs the following steps:
    1. Reads the CSV file located at 'specifications/Assignment3Data.csv' into a pandas DataFrame.
    2. Extracts unique school names and codes from the DataFrame and creates a dictionary mapping 
       each school name to its code.
    3. Generates the three "label" dictionaries

    Returns:
        tuple: A tuple containing:
            - data (numpy.ndarray): A 3D numpy array where each element is a reshaped year array.
            - schools (dict): A dictionary mapping school names (str) to school codes (str).
            - year_labels (dict): A dictionary containing all years (int) with their 
                                  corresponding index (int) in the 3D array
            - grade_labels (dict): A dictionary containing all grades (int) with their 
                                   corresponding index (int) in the 3D array
            - school_labels (dict): A dictionary containing all school codes (int) with their 
                                    corresponding (int) index in the 3D array

    Example:
        data, schools, year_labels, grade_labels, school_labels = prepare_data()
    """

    # read school names and codes from the .csv file and combine them into a dict named schools
    file_path = 'specifications/Assignment3Data.csv'
    df = pd.read_csv(file_path)

    school_names = list(df['School Name'].unique())
    school_names = [name.strip() for name in school_names]  # extra step to clean up the strings

    school_codes = list(df['School Code'].unique())
    school_codes = [str(code) for code in school_codes]  # convert the codes to strings

    schools = dict(zip(school_codes, school_names))

    all_years = [year_2013, year_2014, year_2015, year_2016, year_2017,
                 year_2018, year_2019, year_2020, year_2021, year_2022]

    # reshape data into a 3D np.array named data
    all_years_reshaped = [np.array(year).reshape(20, 3) for year in all_years]
    data = np.array(all_years_reshaped)

    # Create 3 dicts to store the labels of the data in the 3D array. Each dict will have the 
    # user friendly version of the data as the key and the index as the value. This will allow
    # an easier way to access the data which should make the code more readable.
    #
    # Ex. Grade 11 data is stored in the 3D array, 3rd dimension, index 1
    #     So the grade_labels dict can easily find the index 1 of grade 11 data
    #     with grade_labels[11] (which will return 1)

    year_labels = dict(zip(range(2013, 2023), range(10)))
    grade_labels = {10: 0, 11: 1, 12: 2}
    school_labels = dict(zip(school_codes, range(20)))

    return data, schools, year_labels, grade_labels, school_labels


def print_school_list(schools):
    """
    Prints a formatted list of all school names and codes

    Arguments: schools (dict): Dictionary of school codes and names
    Returns: None
    """
    max_school_name_length = max([len(name) for name in schools.values()])

    print('School Code'.center(15) + '|' + 'School Name'.center(max_school_name_length + 6))
    print('-' * (16 + max_school_name_length + 6))
    for key, value in schools.items():
        print(str(key).center(15) + '|' + value.center(max_school_name_length + 6))
    print()


def prompt_user(schools):
    """
    Prompt user for the school. User can enter either the school name or school code

    Arguments: schools (dict): Dictionary of school codes and names
    Returns: 
        - school_code (int): school code for user's choice
        - school_name (str): school name for user's choice
    """
    while True:
        try:
            input_high_school = input("Please enter the high school name or"
                                      " school code: ").strip()
            if input_high_school in schools.keys():  # check for the school code
                school_name = schools[input_high_school]
                school_code = input_high_school
                break
            elif input_high_school in schools.values():  # check for the school name
                for key, value in schools.items():
                    if input_high_school == value:
                        school_name = input_high_school
                        school_code = key
                break
            else:
                raise ValueError
        except ValueError:
            print('You must enter a valid school name or code.\n')
    return school_code, school_name



def main():
    # Format to access items in the 3D array is 
    # data[year_index, school_index, grade_index]

    # Format to access a single item in the 3D array using the label dicts is
    #     data[year_labels[year]], school_labels[school], grade_labels[grade])
    # Ex. data[year_labels[2019]], school_labels[9857], grade_labels[12]) ... 
    # ... will return enrollment in 2019 for school 9857, grade 12
    # 
    # Ex. data[:, school_labels[1224], grade_labels[10]) ...
    # ... will return enrollment for all years, school 1224, grade 10

    print("ENSF 692 School Enrollment Statistics\n")


    
    # Print Stage 1 requirements here
    # -------------------------------
    data, schools, year_labels, grade_labels, school_labels = prepare_data()
    print_school_list(schools)
    print(f'Shape of full data array:  {data.shape}')
    print(f'Dimensions of full data array:  {data.ndim}')
    school_code, school_name = prompt_user(schools)  # get user input
    


    # Print Stage 2 requirements here
    # -------------------------------
    print("\n***Requested School Statistics***\n")
    print(f"School Name: {school_name}, School Code: {school_code}")
 
    # Prints mean enrollment for grades 10, 11, and 12
    for grade, grade_index in grade_labels.items():
        mean_enrollment = int(np.nanmean(data[:, school_labels[school_code], grade_index]))
        print(f'Mean enrollment for Grade {grade}: {mean_enrollment}')

    # Prints max and min enrollment for a single grade
    max_enrollment = int(np.nanmax(data[:, school_labels[school_code], :]))
    print(f'Highest enrollment for a single grade: {max_enrollment}')
    min_enrollment = int(np.nanmin(data[:, school_labels[school_code], :]))
    print(f'Lowest enrollment for a single grade: {min_enrollment}')

    # Prints total enrollment for all grades for each year
    for year, year_index in year_labels.items():
        total_enrollment = int(np.nansum(data[year_index, school_labels[school_code], :]))
        print(f'Total enrollment for {year}: {total_enrollment}')                       

    # Print statistics for 10-year enrollment
    total_ten_year_enrollment = np.nansum(data[:, school_labels[school_code], :])
    print(f'Total ten year enrollment: {int(total_ten_year_enrollment)}')
    print(f'Mean total enrollment over ten years: {int(total_ten_year_enrollment / 10)}')
    
    # Print median enrollments over 500
    this_school = data[:, school_labels[school_code], :]
    enrollment_over_500 = this_school[this_school > 500]  # Masking operation
    if len(enrollment_over_500) == 0:
        print("No enrollments over 500.")
    else:
        print(f'For all enrollments over 500, the median value was: {int(np.median(enrollment_over_500))}')



    # Print Stage 3 requirements here
    # -------------------------------
    print("\n***General Statistics for All Schools***\n")
    mean_enrollment = int(np.mean(data[year_labels[2013], :, :]))
    print(f'Mean enrollment in 2013: {mean_enrollment}')
    mean_enrollment = int(np.nanmean(data[year_labels[2022], :, :]))
    print(f'Mean enrollment in 2022: {mean_enrollment}')
    total_2022 = int(np.nansum(data[year_labels[2022], :, grade_labels[12]]))
    print(f'Total graduating class of 2022: {total_2022}')
    print(f'Highest enrollment for a single grade: {int(np.nanmax(data))}')
    print(f'Lowest enrollment for a single grade: {int(np.nanmin(data))}')



if __name__ == '__main__':
    main()

