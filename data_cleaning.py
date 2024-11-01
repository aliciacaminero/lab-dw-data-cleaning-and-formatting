
import pandas as pd

def load_data(filepath):
    """Carga el DataFrame desde un archivo CSV."""
    return pd.read_csv(filepath)

def identify_nulls(df):
    """Identifica y muestra el número de valores nulos por columna."""
    return df.isnull().sum()

def handle_nulls(df):
    """Maneja los valores nulos en el DataFrame."""
    for column in df.columns:
        if df[column].dtype == 'object':  # Categórica
            moda = df[column].mode()[0]  # Tomar la moda
            df[column].fillna(moda, inplace=True)
        else:  # Numérica
            mediana = df[column].median()  # Tomar la mediana
            df[column].fillna(mediana, inplace=True)
    return df

def handle_duplicates(df):
    """Elimina filas duplicadas y devuelve el DataFrame depurado."""
    df = df.drop_duplicates(keep='first')
    return df

def normalize_column_names(df):
    """Normaliza los nombres de las columnas en el DataFrame."""
    # Renombrar columnas específicas
    df.rename(columns={'GENDER': 'Gender', 'ST': 'State'}, inplace=True)
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(' ', '_')
    return df

def convert_data_types(df):
    """Convierte tipos de datos en el DataFrame."""
    df['customer_lifetime_value'] = pd.to_numeric(df['customer_lifetime_value'], errors='coerce')
    df['number_of_open_complaints'] = (
        df['number_of_open_complaints']
        .str.split('/')
        .str[1]
        .astype(float)
        .fillna(0)
        .astype(int)
    )
    numerical_cols = df.select_dtypes(include=['float64']).columns
    df[numerical_cols] = df[numerical_cols].fillna(0).astype(int)
    return df

def save_data(df, filepath):
    """Guarda el DataFrame en un archivo CSV."""
    df.to_csv(filepath, index=False)
