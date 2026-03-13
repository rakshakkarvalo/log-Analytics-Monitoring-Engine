# from datetime import time

# # import the actual client creator and correct loader path
# from backend.config.dask_config import create_dask_client
# from backend.injection.loader import load_logs
# from backend.pipeline.processing import process_pipeline       
# # from processing.pipeline import build_pipeline


# # def main():
# #     # Create a Dask client
# #     client = start_dask()
# #     print(client)
# #     print(f"Dashboard: {client.dashboard_link}")
    
# #     # df = load_logs("backend/sample_data/log_data.log")
    
# #     start = time.time()
# #     # df = build_pipeline("data/sample_log.log")
# #     df = load_logs("data/sample_log.log")
# #     total_logs = df.count().compute()
# #     end = time.time()
    
# #     # Now you can use the client to submit tasks to the Dask cluster
# #     # For example, you can use client.submit() to run a function on the cluster
# #     # result = client.submit(your_function, your_arguments)
# #     input("Press Enter to stop the cluster...") # give this line in code
# #     # Don't forget to close the client when you're done
# #     client.close()  

# def main():
#     print("Starting Log Processing...")
#     client = create_dask_client()
#     print("Dask Started Successfully")

#     # use the existing sample log under backend/sample_data
#     df = process_pipeline("backend/sample_data/log_data.log")
#     print("Logs Loaded Successfully")

#     print("\nLog Count by Level:")
#     result = df.count().compute()
#     print(result)

#     client.close()
#     print("\nProcessing Finished Successfully!")
    
    
# if __name__ == "__main__":
#     main()

import time
from backend.config.dask_config import create_dask_client
from backend.pipeline.processing import process_pipeline


def main():
    print("Starting Log Processing...\n")

    # Start Dask
    client = create_dask_client()
    print("Dask Started Successfully")
    print(f"Dashboard: {client.dashboard_link}")
    print("-" * 50)

    start = time.time()

    # Build pipeline
    df = process_pipeline("backend/sample_data/log_data.log")
    print("Logs Loaded & Parsed Successfully\n")

    # ✅ SHOW DATAFRAME OUTPUT (TABLE FORMAT)
    print("Parsed Log Data (Table Format):")
    print(df.compute())   # <-- THIS LINE SHOWS TABLE OUTPUT

    # ✅ Count total rows correctly
    total_logs = df.shape[0].compute()

    end = time.time()

    print("\nTotal Logs Processed:", total_logs)
    print("Time Taken:", round(end - start, 4), "seconds")
    print("Throughput:", round(total_logs / (end - start), 2), "logs/sec")

    print("-" * 50)

    client.close()
    print("Processing Finished Successfully!")


if __name__ == "__main__":
    main()