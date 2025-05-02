import pandas as pd
from datetime import datetime
from django.utils import timezone


def validate_cols(df: pd.DataFrame, cols: list) -> bool:
    """
    Validate if the columns in the DataFrame are present in the specified list of columns.

    Args:
        df (pd.DataFrame): The DataFrame to validate.
        cols (list): The list of columns to check against.

    Returns:
        bool: True if all columns are present, False otherwise.
    """
    return all(col in df.columns for col in cols) if cols else True


def format_date():
    pass


def format_dataframe(df: pd.DataFrame, format: str = '%Y-%m-%d') -> pd.DataFrame:
    """
    Format the published_date column in the DataFrame to YYY-MM-DD.

    """

    df['published_date'] = pd.to_datetime(
        df['published_date'], errors='coerce'
    ).dt.strftime(format)

    df['category'] = df.apply(
        lambda x: x['category'] if x['category'] != 'default' else None, axis=1
    )

    df['published_date'] = df.apply(
        lambda x: x['published_date'] if not pd.isna(x['published_date']) else timezone.now().strftime(format), axis=1
    )

    return df
