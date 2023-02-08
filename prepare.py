def clean_store_data(df):
    # drop old columns from sql database
    df = df.drop(columns = ["store_id","item_id","sale_id"])
    
    # convert 'sale_date' column to datetime type
    df['sale_date'] = pd.to_datetime(df['sale_date'])
    
    # set 'sale_date' column as index and sort it
    df = df.set_index("sale_date").sort_index()
    
    # feature engineer: add month & day of week using date index
    df['month'] = df.index.month
    df['day_of_week'] = df.index.dayofweek
    
    # feature engineer: add 'sales_total' column multiplying 'sale_amount' & 'item_price'
    df["sales_total"] = df["sale_amount"]*df["item_price"]
    
    return df

def clean_energy_data(df):
    # fix datatype of 'Date' column
    df['Date']=pd.to_datetime(df['Date'])
    
    # set 'Date' column as index and sorted
    df = df.set_index("Date").sort_index()
    
    # feature engineering: added 'month' column using index
    df['month'] = df.index.month
    
    # feature engineering: added 'year' column using index
    df['year'] = df.index.year
    
    # removed nulls from ['Wind','Solar','Wind_Solar'] columns
    # by backfilling and added as new columns
    df = df.assign(Wind_Solar=lambda df: df["Wind+Solar"].bfill())
    df = df.assign(Fixed_Solar=lambda df: df["Solar"].bfill())
    df = df.assign(Fixed_Wind=lambda df: df["Wind"].bfill())
    
    # dropped the old null columns
    df = df.drop(columns = ['Wind','Solar','Wind+Solar'])
    
    # renamed backfilled column names
    df = df.rename(columns={"Fixed_Solar": "Solar", "Fixed_Wind": "Wind"})
