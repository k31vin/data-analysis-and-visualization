import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import numpy as np

def load_and_prepare_data():
    """
    Load the Iris dataset and convert it to a pandas DataFrame
    """
    try:
        # Load iris dataset
        iris = load_iris()
        
        # Create DataFrame
        df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
        df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
        
        # Add some random missing values to sepal length column
        df.loc[np.random.choice(df.index, 5), 'sepal length (cm)'] = np.nan
        
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def explore_data(df):
    """
    Perform initial data exploration
    """
    print("First 5 rows of the dataset:")
    print(df.head())
    print("\nDataset Info:")
    print(df.info())
    print("\nMissing Values:")
    print(df.isnull().sum())

def clean_data(df):
    """
    Clean the dataset by handling missing values
    """
    # Create a copy of the dataframe
    df_cleaned = df.copy()
    
    # Fill missing values with mean of the column - fixed warning
    for column in df_cleaned.select_dtypes(include=[np.number]).columns:
        column_mean = df_cleaned[column].mean()
        df_cleaned[column] = df_cleaned[column].fillna(column_mean)
    
    return df_cleaned

def basic_analysis(df):
    """
    Perform basic statistical analysis
    """
    print("\nBasic Statistics:")
    print(df.describe())
    
    print("\nMean values by species:")
    # Fixed the groupby warning by explicitly setting observed parameter
    print(df.groupby('species', observed=True).mean())

def create_visualizations(df):
    """
    Create and save various visualizations
    """
    # Set the style for all plots - using a built-in style instead of seaborn
    plt.style.use('classic')
    
    # Create a figure with subplots
    fig = plt.figure(figsize=(20, 15))
    
    # 1. Line Chart - Average measurements over sorted sepal length
    plt.subplot(2, 2, 1)
    sorted_df = df.sort_values('sepal length (cm)')
    plt.plot(range(len(df)), sorted_df['sepal length (cm)'], label='Sepal Length')
    plt.plot(range(len(df)), sorted_df['petal length (cm)'], label='Petal Length')
    plt.title('Trend of Sepal and Petal Lengths')
    plt.xlabel('Sample Index')
    plt.ylabel('Length (cm)')
    plt.legend()
    
    # 2. Bar Chart - Average measurements by species
    plt.subplot(2, 2, 2)
    species_means = df.groupby('species', observed=True)['sepal length (cm)'].mean()
    species_means.plot(kind='bar')
    plt.title('Average Sepal Length by Species')
    plt.xlabel('Species')
    plt.ylabel('Average Sepal Length (cm)')
    plt.xticks(rotation=45)
    
    # 3. Histogram - Distribution of sepal length
    plt.subplot(2, 2, 3)
    plt.hist(df['sepal length (cm)'], bins=20, edgecolor='black')
    plt.title('Distribution of Sepal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Frequency')
    
    # 4. Scatter Plot - Sepal length vs Petal length
    plt.subplot(2, 2, 4)
    for species in df['species'].unique():
        species_data = df[df['species'] == species]
        plt.scatter(species_data['sepal length (cm)'], 
                species_data['petal length (cm)'],
                label=species, alpha=0.6)
    plt.title('Sepal Length vs Petal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.legend()
    
    # Adjust layout and display
    plt.tight_layout()
    return fig

def main():
    """
    Main function to run the analysis
    """
    # Load and prepare data
    df = load_and_prepare_data()
    if df is None:
        return
    
    # Explore raw data
    print("=== Data Exploration ===")
    explore_data(df)
    
    # Clean data
    print("\n=== Data Cleaning ===")
    df_cleaned = clean_data(df)
    print("Missing values after cleaning:")
    print(df_cleaned.isnull().sum())
    
    # Perform basic analysis
    print("\n=== Basic Analysis ===")
    basic_analysis(df_cleaned)
    
    # Create visualizations
    print("\n=== Creating Visualizations ===")
    fig = create_visualizations(df_cleaned)
    plt.show()

if __name__ == "__main__":
    main()