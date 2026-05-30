
def traffic_by_contract(df):

    result = df.groupby("Contract").size().reset_index(name="Customers")

    return result