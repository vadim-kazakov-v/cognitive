# Cognitive Bias Visualizer

A simple web application that visualizes cognitive bias data. The backend is built with Python and Flask, while the frontend uses D3.js and Three.js for interactive visualizations. Users can upload their own CSV files and switch between a circle-packing chart, a bar chart, and a 3D WebGL view.

## Development

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Run the server

```bash
python app.py
```

Visit `http://localhost:5000` to view the visualization.

### Uploading your own data

Use the upload form on the page to provide a CSV file with columns `bias`, `category`, and `description`. After uploading, choose a visualization type from the dropdown to explore the data.
