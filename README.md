# Explorative-Viz-Project

This is the codebase for the CS-E4450 - Explorative Information Visualization D course. 

The data and the visualizations are handled inside the `preprocessing.ipynb` notebook. The website is built inside `app.py`. 

To start the project, it is recommended to create a virtual environment. In Windows:
```
py -m venv .venv
.venv/Scripts/activate
```

Then, install the packages required for the project:
```
pip install -r requirements.txt
```

To start the website locally:
```
streamlit run app.py
```