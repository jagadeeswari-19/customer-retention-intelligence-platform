def validate_dataset(df):

    if df.empty:
        raise Exception("Dataset is empty")

    if df.isnull().sum().sum() > 0:
        print("Warning: Missing values found")

    print("Dataset validation completed")