# Dataset Visualizer

Web application for exploring CSV datasets through interactive charts. The backend uses Python and Flask, while the frontend leverages D3.js for visualizations. Upload your own data or load the included Titanic sample to experiment.

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

### CSV requirements

The app automatically detects numeric and categorical columns. Scatter plots require two numeric columns for the X and Y axes. Bar charts count occurrences of a selected categorical column.

