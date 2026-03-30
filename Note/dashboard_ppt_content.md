# PPT Content for Log Analytics Monitoring Engine

## Slide 1: Project Title
**Python Based High Throughput Log Analytics Monitoring Engine**

- Developed to monitor large-scale application logs in near real time
- Uses Dask for scalable parallel log processing
- Uses Streamlit for interactive visualization and analysis
- Detects abnormal error spikes for proactive monitoring

## Slide 2: Project Objective
- Build a system that can ingest and process continuous log data efficiently
- Classify logs into INFO, WARN, ERROR, and DEBUG levels
- Visualize system health through dashboards
- Detect anomalies in error patterns for faster issue identification
- Support operational monitoring for distributed services

## Slide 3: Technology Stack
- Python for implementation
- Dask Bag and Dask DataFrame for parallel log ingestion and processing
- Dask Distributed for worker scheduling and execution monitoring
- Streamlit for dashboard development
- Plotly for interactive charts
- Pandas for final in-memory analytics and formatting

## Slide 4: System Workflow
- Raw log file is read using Dask Bag
- Each line is parsed into structured fields: timestamp, service, level, message
- Cleaned data is converted into Dask DataFrame using schema metadata
- Error logs are analyzed for anomaly detection using z-score
- Final processed data is shown in Streamlit dashboard
- Parallel execution is monitored in the Dask dashboard

## Slide 5: Dask Dashboard Overview
- Dask dashboard is used for backend execution monitoring
- It shows how distributed tasks are executed across workers
- It helps track performance during large-scale log processing
- Dashboard URL: `http://127.0.0.1:8790/status`
- Useful for debugging slow tasks, worker load imbalance, and memory issues

## Slide 6: Dask Dashboard Main Content
- **Workers tab**: shows number of workers, CPU usage, and memory usage
- **Task Stream**: shows live task execution over time
- **Graph view**: shows dependency graph of processing tasks
- **Progress view**: shows completion progress of running computations
- **Memory view**: helps identify memory pressure or heavy partitions

## Slide 7: Why Dask Dashboard is Important
- Confirms that the pipeline is running in parallel
- Gives visibility into worker health and task scheduling
- Helps improve system performance and resource utilization
- Useful for scaling from local testing to larger workloads
- Supports troubleshooting when processing becomes slow or unstable

## Slide 8: Streamlit Dashboard Overview
- Streamlit dashboard is the user-facing analytics layer
- It converts processed logs into interactive charts and tables
- It helps developers and operators understand system behavior quickly
- It refreshes the output from the latest log file
- It simplifies monitoring without requiring command-line analysis

## Slide 9: Streamlit Dashboard Main Content
- Operational KPI cards for total logs, errors, warnings, services, and anomalies
- Pie chart for log level distribution
- Service-wise log volume bar chart
- Service severity heatmap for service vs log level counts
- Time-based histograms for ERROR, INFO, WARN, and DEBUG logs
- Error trend chart for monitoring spikes over time
- Anomaly table showing abnormal error intervals
- Recent error and warning logs in tabular form
- Top error-prone services chart

## Slide 10: Key Insights from Streamlit Dashboard
- Quickly identifies the most active services in the system
- Highlights which log level dominates system activity
- Shows whether errors are isolated or increasing over time
- Helps teams find which services generate the most issues
- Makes anomaly investigation faster through charts and tables

## Slide 11: Anomaly Detection Logic
- Only ERROR logs are used for anomaly detection
- Logs are grouped minute by minute
- Error counts are compared against the average behavior
- Z-score is calculated for each interval
- If z-score crosses threshold, the interval is marked as anomaly
- This helps detect sudden abnormal spikes in failures

## Slide 12: Advantages of the Project
- Supports scalable processing using Dask
- Provides real-time style monitoring for log analytics
- Makes backend and frontend monitoring available in one project
- Helps reduce manual analysis effort
- Improves observability for service-based applications

## Slide 13: Future Enhancements
- Add live log streaming from Kafka or APIs
- Add alert notifications through email or messaging tools
- Add filtering by service, date range, and log level
- Add predictive analytics for failure forecasting
- Deploy on cloud infrastructure for larger production workloads

## Slide 14: Conclusion
- The project combines distributed processing and interactive analytics
- Dask handles scalable computation and execution visibility
- Streamlit provides a simple and effective monitoring interface
- The solution helps teams monitor logs, detect anomalies, and improve reliability

## Short Viva Explanation
**What is the role of Dask dashboard?**
- It is used to monitor worker activity, task execution, memory consumption, and computation progress in the backend.

**What is the role of Streamlit dashboard?**
- It is used to present processed log analytics visually through charts, KPIs, and anomaly reports.

**Why are both dashboards needed?**
- Dask dashboard is for technical execution monitoring.
- Streamlit dashboard is for user-friendly operational monitoring.
