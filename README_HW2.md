# HW 2 - Random Forest ML Pipeline

This repository contains the complete solution for CSC 659/859 Spring 2026 HW 2: ML Pipeline Experiment with Random Forest.

## Files

- `hw2_rf_pipeline.py` - Main Python script implementing the complete RF pipeline
- `HW2_Report_Template.md` - Report template with all required sections
- `requirements.txt` - Python package dependencies
- `Original training DB i1 cluster.csv` - Original dataset (provided)

## Setup

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Ensure the data file `Original training DB i1 cluster.csv` is in the same directory

## Running the Pipeline

Execute the main script:
```bash
python hw2_rf_pipeline.py
```

This will:
- Load and audit the original database
- Create training and verification databases
- Perform Method 1: OOB accuracy estimation with grid search
- Perform Method 2: Manual 3-fold cross-validation
- Generate feature rankings
- Run predictions on verification database
- Save all results to CSV files

## Output Files

After running the script, you'll get:
- `verification_db.csv` - Verification database (2 samples)
- `feature_ranking.csv` - Full feature ranking with importance scores
- `method1_results.csv` - Method 1 results summary
- `method2_results.csv` - Method 2 results summary

## Report Generation

1. Run the pipeline script to generate all results
2. Fill in the `HW2_Report_Template.md` with:
   - Your name, email, date
   - Results from the script output
   - Code snippets from `hw2_rf_pipeline.py`
   - Analysis and discussion
3. Convert to PDF for submission

## Important Notes

- The script uses random seed 42 for reproducibility
- Grid search may take some time - the script uses a reduced grid for faster execution
- All accuracy measures are computed to 5 decimal places
- Feature ranking uses Gini importance (scikit-learn default)
- Ground truth genes to look for: COL5A2, NDNF, FAT1

## Assignment Requirements Checklist

- [x] Database audit
- [x] Training/verification DB split (2 random samples)
- [x] Method 1: OOB accuracy estimation
- [x] Method 2: Manual 3-fold CV
- [x] Feature ranking (top 10)
- [x] Runtime prediction on verification DB
- [ ] Report with all sections (use template)
- [ ] Appendix I: GenAI usage (if applicable)
- [ ] Appendix II: Full code in PDF

