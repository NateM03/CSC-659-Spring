"""
Helper script to generate formatted tables for the HW 2 report.
Run this after hw2_rf_pipeline.py to generate markdown tables.
"""

import pandas as pd
import numpy as np

def generate_markdown_table(df, title="", caption=""):
    """Generate a markdown table from a DataFrame."""
    md = []
    if title:
        md.append(f"### {title}\n")
    if caption:
        md.append(f"*{caption}*\n")
    
    # Header
    md.append("| " + " | ".join(df.columns) + " |")
    md.append("|" + "|".join(["---"] * len(df.columns)) + "|")
    
    # Rows
    for _, row in df.iterrows():
        md.append("| " + " | ".join([str(val) for val in row.values]) + " |")
    
    return "\n".join(md)

# Load results if they exist
try:
    method1_results = pd.read_csv('method1_results.csv')
    method2_results = pd.read_csv('method2_results.csv')
    feature_ranking = pd.read_csv('feature_ranking.csv')
    
    print("=" * 80)
    print("GENERATED REPORT TABLES")
    print("=" * 80)
    
    # Method 1 Results Table
    print("\n" + generate_markdown_table(
        method1_results[['Method', 'OOB_Accuracy', 'Training_Accuracy', 'Precision', 'Recall', 'F1_Score']],
        title="Method 1 - Accuracy Measures",
        caption="All values to 5 decimal places"
    ))
    
    # Method 2 Results Table
    print("\n" + generate_markdown_table(
        method2_results[['Method', 'Avg_Accuracy', 'Avg_Precision', 'Avg_Recall', 'Avg_F1_Score']],
        title="Method 2 - Average CV Accuracy Measures",
        caption="All values to 5 decimal places"
    ))
    
    # Top 10 Features
    top10 = feature_ranking.head(10).copy()
    top10['Rank'] = range(1, len(top10) + 1)
    top10 = top10[['Rank', 'Feature', 'Importance']]
    
    print("\n" + generate_markdown_table(
        top10,
        title="Top 10 Ranked Features",
        caption="Features ranked by Gini importance"
    ))
    
    print("\n" + "=" * 80)
    print("Copy the tables above into your report!")
    print("=" * 80)
    
except FileNotFoundError as e:
    print(f"Error: {e}")
    print("Please run hw2_rf_pipeline.py first to generate the results files.")

