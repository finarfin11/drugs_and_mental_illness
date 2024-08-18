# Defining a function which converts the column names to snake_case
def to_snake_case(name):
    ''' Transforms sequence of strings separated by single space to snake_case. 
        If single string is provided, transforms it to lower case. '''
    
    if ' ' in name:
        name = name.replace(' ', '_').lower()
        return name.replace('-', '_')
    return name.lower()

# Defining a function which replaces certain values in a colum
def rplace_col_values(dict, df, col):
    ''' Replaces the values of col in df with dict_values 
        where dict_keys are equal to the current col values. '''
    
    for key, value in dict.items():
        if key in df[col].values:
            df[col].replace(df[df[col] == key][col].values[0], value, inplace = True)