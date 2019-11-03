"""
This python module runs the tests on a dataframe.

"""
import pandas as pd

import dataframe

# define url associated with dataset
URL = "https://data.cms.gov/api/views/97k6-zzx3/rows.csv?accessType=DOWNLOAD"

# load csv file into a dataframe
DF = pd.read_csv(URL)

# Obtain a list of column names
COLS = list(DF)

# test hw2 tests
def test_hw2():
    """
    This function tests the clauses outlined in hw 2.
    Returns True if all clauses pass.
    """
    value = dataframe.test_HW2(DF, COLS)
    assert value is True

# 1) Check that all columns have values of the correct (same?) type test
def test_col_val_types():
    """
    This function checks if variable types are the same in a column of the dataframe.
    Returns True if clause pass.
    """
    value = dataframe.test_col_val_types(DF, COLS)
    assert value is True

# 2) Check for nan values test
def test_nan():
    """
    This function checks for nans in the dataframe.
    Returns True if clause pass.
    """
    value = dataframe.test_nan(DF, COLS)
    assert value is True

# 3) Verify that the dataframe has at least one row test
def test_row_number():
    """
    This function checks if there is at least one row in the dataframe.
    Returns True if clause pass.
    """
    value = dataframe.test_row_number(DF, COLS)
    assert value is True
