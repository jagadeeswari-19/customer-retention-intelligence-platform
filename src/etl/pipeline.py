from src.etl.extract import extract_data
from src.etl.transform import transform_data
from src.etl.load import load_processed_data
from src.data.validate import validate_dataset


def run_pipeline():
    df = extract_data()

    validate_dataset(df)

    clean_df = transform_data(df)

    load_processed_data(clean_df)