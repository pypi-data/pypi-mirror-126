# Streamlit Pollination

A collection of objects to facilitate working with Pollination in Streamlit.

## Quickstart

```python
import json
import pathlib

import hiplot
import numpy as np
import streamlit as st
from honeybee_vtk.model import HBModel, Model
from streamlit_pollination.selectors import job_selector
from streamlit_vtkjs import st_vtkjs

job = job_selector()

if job is not None:
    df = job.runs_dataframe

    st.markdown("## Runs Dataframe")
    plt = hiplot.Experiment.from_dataframe(df)
    plt.display_st()

    run_number = st.select_slider(
        'Select a run',
        options=range(0, df.shape[0])
    )

    run_row = df.iloc[run_number]
    model_path = run_row.model
    model_dict = json.load(job.download_artifact(model_path))
    hb_model = HBModel.from_dict(model_dict)
    vtk_model = Model(hb_model)
    key = run_row['run-id']
    file = pathlib.Path(vtk_model.to_vtkjs('data', key))
    st_vtkjs(file.read_bytes(), menu=True, key=key)
```