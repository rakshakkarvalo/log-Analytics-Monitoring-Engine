#which is used to handle the data and reuseable code which is seperate from the dask 
#loading the data
#parsing the data
#structure the data and load the data using injection files
#parser: parser is a python method which is used to convert the raw data into structured data based on 
# the schema which we have defined(translater)
#without parser:no columns are defined 
#no filtering is done
#no anamoloy is detection or no aggregation
#with parsing: we can filter error logs
#detect the unsual patterns
#it converts raw log data to the machine readable language
# import dask.bag as db
# from backend.injection.parser import parse_log_line
# from backend.schema.schema import log_schema as LOG_SCHEMA

# def load_logs(file_path):
#     bag = db.read_text(file_path)
#     parsed = (
#         bag.map(parse_log_line)
#         .filter(lambda x: x is not None)  # Filter out lines that failed to parse
#     )
#     df = parsed.to_dataframe()
#     return df.astype(LOG_SCHEMA)
#####################################################################################################################
# SECOND VERSION
#whuch is used to handle the data and reusable code which is seperate from the dask
#loading the data
#parsing the data
#structure the data and load the data using injection files 
#parser: It is a python method which is used to convert raw data into structured data based on 
#the schema which we have defined (translator) 
# Without parser: No columns are defined
#no filtering is done
#no anamoly is detection or no aggregation
#with parsing: we can filter error logs
#detect the unusual patterns 
#it converts raw log data to the machine readable language
#loader is to inject the log data into the file

import dask.bag as db
from injection.parser import parse_log_line
from schema.schema import log_schema

def load_logs(file_path):
    bag = db.read_text(file_path)
    return bag
    #return df.astype(log_schema)
    #return df 