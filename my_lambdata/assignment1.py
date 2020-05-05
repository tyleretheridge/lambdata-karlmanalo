# my_lambdata/assignment1.py

from pandas import DataFrame


def add_state_names(my_df):
    """
    Converts a dataframe with a column of state abbreviations, adding a 
    corresponding column

    Params: 
        my_df a pandas.DataFrame with a column called "abbrev".
        
    Example: 
        add_state_names(DataFrame({"abbrev":["CA","CO","CT","DC","TX"]}))

    Returns: a pandas.DataFrame with the original col as well as a "name" 
    column.
    """
    # State abbreviation -> Full Name and vice versa.
    # FL -> Florida, etc.

    new_frame = my_df.copy()

    # Need list/dictionary with abbreviation/name mappings
    names_map = {"CA": "Cali", "CO": "Colo", 
                 "CT": "Conn", "DC": "District of Columbia"}
    
    # Create a new column which maps the existing column using our names map
    breakpoint()

    new_frame["name"] = new_frame["abbrev"].map(names_map)

    return new_frame


if __name__ == "__main__":
    
    df = DataFrame({"abbrev":["CA","CO","CT","DC","TX"]})
    print(df.head())

    df2 = add_state_names(df)
    print(df2.head())