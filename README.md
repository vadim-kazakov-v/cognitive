
# Dataset Visualizer

Web application for exploring CSV datasets through interactive charts. The backend uses Python and Flask, while the frontend leverages D3.js and Three.js for visualizations. Upload your own data or load the included Titanic sample to experiment.


## Development

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Run the server

```bash
python app.py
```

Visit `http://localhost:5000` and either upload a CSV file or click "Load Titanic Sample" to explore the dataset.

### Visualization modes

* **Scatter Plot** – choose two numeric columns for a 2D plot.
* **Bar Chart** – select a categorical column to count occurrences.
* **3D WebGL Scatter** – pick three numeric columns to render rotating spheres in WebGL.
* **K-Means Clusters** – apply a simple AI/ML clustering algorithm on two numeric columns and color code the resulting groups.
* **Correlation Matrix** – compute Pearson correlations across all numeric fields and display them in a heatmap.
* **PCA 2D Scatter** – reduce multiple numeric dimensions into two principal components for scientific analysis.


### CSV requirements

The app automatically detects numeric and categorical columns. Scatter plots require two numeric columns for the X and Y axes. Bar charts count occurrences of a selected categorical column.

