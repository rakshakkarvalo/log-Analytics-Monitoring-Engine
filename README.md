# log-Analytics-Monitoring-Engine
Infosys Springboard Project
All log data are fetching as per the requirement and i for some cases we are having some exception which is causing unwanted error 

## Setup

Use the project virtual environment so Dask, Streamlit, Plotly, and the Dask dashboard dependencies all come from the same Python installation.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run Dask Processing

```powershell
.venv\Scripts\python.exe main.py
```

If you run `python main.py` without activating `.venv`, Windows may use your global Python instead. That can cause dashboard errors such as missing or incompatible `bokeh`.

## Run Streamlit Dashboard

```powershell
.venv\Scripts\python.exe -m streamlit run dashboard/app.py
```
