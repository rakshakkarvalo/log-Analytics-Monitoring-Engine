import dask.bag as db

from backend.injection.parser import parse_log_line
from backend.schema.schema import log_schema


def load_logs(file_path):
    bag = db.read_text(file_path)
    parsed_bag = bag.map(parse_log_line).filter(lambda row: row is not None)
    df = parsed_bag.to_dataframe(meta=log_schema)
    return df.astype(log_schema)
