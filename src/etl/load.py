from src.config import CLEAN_DATA_PATH


def load_processed_data(df):
    df.to_csv(CLEAN_DATA_PATH, index=False)
    print("Processed data saved")