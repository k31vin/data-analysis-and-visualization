# Dataset Analysis Project

This project performs basic data analysis and visualization on the Iris dataset using Python. It includes data loading, cleaning, statistical analysis, and various visualizations.

## Prerequisites

Before you begin, ensure you have Python 3.9 or higher installed on your system. You can check your Python version by running:
```bash
python --version
```

## Installation

1. Clone the repository or download the project files:
```bash
git clone <repository-url>
# or create a new directory and copy the files manually
```

2. Navigate to the project directory:
```bash
cd "Replace with Your project directory"
```

3. Create a virtual environment:

**Using venv (recommended):**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

**Using conda:**
```bash
conda create -n iris_analysis python=3.9
conda activate iris_analysis
```

4. Install required packages:
```bash
pip install -r requirements.txt
```

## Project Structure
```
iris_analysis/
├── README.md
├── requirements.txt
└── analysis.py
```

## Running the Analysis

To run the analysis, make sure your virtual environment is activated, then execute:
```bash
python analysis.py
```

The script will:
1. Load the Iris dataset
2. Display basic data exploration results in the terminal
3. Show data cleaning steps and results
4. Present basic statistical analysis
5. Open a window with four visualizations:
   - Line chart of sepal and petal lengths
   - Bar chart of average sepal length by species
   - Histogram of sepal length distribution
   - Scatter plot of sepal length vs petal length

## Troubleshooting

If you encounter any issues:

1. **ImportError or ModuleNotFoundError:**
   - Verify that your virtual environment is activated
   - Try reinstalling the requirements:
     ```bash
     pip install -r requirements.txt --force-reinstall
     ```

2. **Visualization window doesn't appear:**
   - Ensure you're running the script in an environment that supports GUI windows
   - If using VS Code, try running from the terminal instead

3. **Other Issues:**
   - Make sure all files are in the correct directory
   - Verify that Python path is correctly set
   - Check that all required files are present

## Dependencies

The project requires the following Python packages:
- pandas >= 2.0.0
- matplotlib >= 3.5.0
- seaborn >= 0.12.0
- scikit-learn >= 1.0.0
- numpy >= 1.20.0

## Additional Notes

- The script adds random missing values to demonstrate data cleaning techniques
- All visualizations are customizable through the code
- The analysis includes basic statistical measures and grouped analysis by species

## Contributing

Feel free to fork this project and submit improvements through pull requests.

## License

This project is open source and available under the MIT License.
