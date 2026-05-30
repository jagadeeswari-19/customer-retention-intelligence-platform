from src.data.preprocess import DataPreprocessor


preprocessor = DataPreprocessor()


def transform_data(df):
    return preprocessor.clean_data(df)