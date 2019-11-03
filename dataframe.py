'''
Homework 3: testing a dataframe

'''
# Brandon Pratt, 10/ 26/ 2019
# Import pandas package
import pandas as pd

# Module that replicates the tests from homework 2
def test_HW2(dataframe, column_names):
    """
    This function tests the clauses outlined in hw 2.
    Returns True if all clauses pass.
    """
    try:
        # The DataFrame contains only the columns that you specified as the second argument
        if not pd.Series(column_names).isin(dataframe.columns).all():
        #if column_names[0] in dataframe.columns:
            raise ValueError("DataFrame does not contains columns")
    except ValueError as err:
        print("Got an exception: %s"%err)
        return False

    try:
        # The values in each column have the same python type
        col_types = dataframe.dtypes
        comparison_number = 0 #
        # compare the first column type to the rest
        for type in col_types:
            # increase comparison number for each iteration
            comparison_number = comparison_number+1

            # Check to see if column types are different
            if type != col_types[0]:
                raise TypeError("DataFrame column types are not the same")
    except TypeError as err:
        print("Got an exception: %s"%err)
        return False

    try:
        # There are at least 10 rows in the DataFrame
        if len(dataframe.index) < 10:
            raise ValueError("DataFrame does not have more than 10 rows")
    except ValueError as err:
        print("Got an exception: %s"%err)
        return False
    return True

# 1) Check that all columns have values of the correct (same?) type
def test_col_val_types(dataframe, column_names):
    """
    This function checks if variable types are the same in a column of the dataframe.
    Returns True if clause pass.
    """
    for col in column_names:
        # get the type of the first value in that column to compare to the other values
        comparison_type = type(dataframe[col].values[0])
        # compare the data type of this element to that in other rows within the column
        for val in dataframe[col].values:
            try:
                if type(val) != comparison_type:
                    raise TypeError("Values within column are not of the same type")
            except TypeError as err:
                print("Got an exception: %s"%err)
                return False
    return True

# 2) Check for nan values
def test_nan(dataframe, column_names):
    """
    This function checks for nans in the dataframe.
    Returns True if clause pass.
    """
    try:
        if dataframe.isnull().values.any(): #is null() finds nan values
            raise ValueError("NaN is contained in DataFrame")
    except ValueError as err:
        print("Got an exception: %s"%err)
        return False
    return True



# 3) Verify that the dataframe has at least one row
def test_row_number(dataframe, column_names):
    """
    This function checks if there is at least one row in the dataframe.
    Returns True if clause pass.
    """
    try:
        # There are at least 10 rows in the DataFrame
        if len(dataframe.index) == 0:
            raise ValueError("DataFrame does not have at least one row")
    except ValueError as err:
        print("Got an exception: %s"%err)
        return False
    return True
