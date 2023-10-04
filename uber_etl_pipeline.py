import os
import argparse
import numpy as np
from time import time
from pathlib import Path
import pandas as pd
import sqlalchemy as sa
from sqlalchemy import create_engine, event
import pyarrow.parquet as pq
import common_lib as cl
import os
#from prefect import flow, task
#from prefect_sqlalchemy import SqlAlchemyConnector



def extract_data(filename:str) -> None:
    parquet_file = pq.ParquetFile(source=f'C:/Users/mcarrasco/Downloads/{filename}.parquet')
    engine = cl.get_engine()
    for batch in parquet_file.iter_batches(batch_size=100000,use_threads=True):
        print("RecordBatch")
        batch_df = batch.to_pandas()
        batch_df.columns = batch_df.columns.str.lower()
        
        batch_df.rename(columns={'lpep_pickup_datetime':'tpep_pickup_datetime','lpep_dropoff_datetime':'tpep_dropoff_datetime'},inplace=True)
        
        dtyp = {c: sa.types.VARCHAR(batch_df[c].str.len().max())
            for c in batch_df.columns[batch_df.dtypes == 'object'].tolist()}
        batch_df.tpep_pickup_datetime   = pd.to_datetime(batch_df.tpep_pickup_datetime)
        batch_df.tpep_dropoff_datetime  = pd.to_datetime(batch_df.tpep_dropoff_datetime)
        
        batch_df.head(n=0).to_sql(name='green_taxi_raw_data', con=engine, if_exists='append',index=False,dtype=dtyp)
        batch_df.to_sql(name='taxi_raw_data', con=engine, if_exists='append',index=False,dtype=dtyp)
        
        print("batch_df:", str(len(batch_df.index)))