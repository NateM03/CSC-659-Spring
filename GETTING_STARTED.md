# Getting Started with HW 2

This guide will help you complete HW 2 and get full points.

## Step-by-Step Instructions

### Step 1: Install Dependencies

First, make sure you have Python installed, then install the required packages:

```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install pandas numpy scikit-learn
```

### Step 2: Run the Pipeline

Execute the main script to generate all results:

```bash
python hw2_rf_pipeline.py
```

This will:
- ✅ Load and audit the database
- ✅ Create training and verification databases
- ✅ Run Method 1 (OOB) with grid search
- ✅ Run Method 2 (Manual 3-fold CV)
- ✅ Generate feature rankings
- ✅ Run predictions on verification set
- ✅ Save all results to CSV files

**Note:** The grid search may take 10-30 minutes depending on your computer. The script uses a reduced grid for faster execution, but you can modify it in the code if needed.

### Step 3: Generate Report Tables (Optional)

After running the pipeline, you can generate formatted tables:

```bash
python generate_report_tables.py
```

This will output markdown tables you can copy into your report.

### Step 4: Fill in the Report Template

1. Open `HW2_Report_Template.md`
2. Fill in your personal information (name, email, date)
3. Copy results from the script output into the appropriate sections
4. Copy code snippets from `hw2_rf_pipeline.py` where indicated
5. Add your analysis and discussion

### Step 5: Review the Checklist

Use `HW2_Checklist.md` to ensure you haven't missed anything:
- All sections are complete
- All tables have captions
- All accuracy measures are to 5 decimal places
- Feature ranking is compared with ground truth
- Code is properly documented

### Step 6: Convert to PDF

Convert your completed report to PDF:
- If using Markdown: Use a tool like Pandoc or online converters
- If using Word: Save as PDF
- If using Jupyter: Export to PDF

### Step 7: Submit

1. Name your file: `CSC 659-859 Spring 2026 HW 2 [Your Last Name].PDF`
2. Email to: Petkovic@sfsu.edu
3. Subject line: `CS 659 859 Spring 2026 HW 2 [Your Last Name]`
4. Include courtesy text in email body

## Key Points to Remember

### Critical Requirements

1. **Manual CV Implementation**: You MUST implement 3-fold CV manually (not using sklearn's built-in CV). The script does this correctly.

2. **5 Decimal Places**: All accuracy measures must be shown to 5 decimal places (e.g., 0.98765, not 0.99).

3. **Full Confusion Matrices**: Show actual counts, not percentages. Label axes (True vs Predicted).

4. **Ground Truth Comparison**: In Section 7, you MUST discuss how your top features compare with:
   - COL5A2 (and COL5A2 family variants)
   - NDNF
   - FAT1

5. **Data Provenance**: Every table and chart needs:
   - A caption explaining what it shows
   - All parameters and settings used
   - Data source description

### What the Script Does

The `hw2_rf_pipeline.py` script implements:

- **Database Audit**: Checks all 8 audit checklist items
- **Data Splitting**: Randomly selects 1 class 0 and 1 class 1 sample for verification
- **Method 1**: Grid search with OOB scoring (finds best hyperparameters)
- **Method 2**: Manual 3-fold CV (splits data manually, trains 3 models)
- **Feature Ranking**: Uses Gini importance, identifies top 10 features
- **Runtime Prediction**: Tests best model on 2 verification samples

### Output Files

After running the script, you'll have:

- `verification_db.csv` - The 2 samples for verification
- `feature_ranking.csv` - All features ranked by importance
- `method1_results.csv` - Method 1 summary
- `method2_results.csv` - Method 2 summary

### Common Issues and Solutions

**Issue: ModuleNotFoundError for sklearn**
- Solution: Run `pip install scikit-learn`

**Issue: Script takes too long**
- Solution: The grid search is already reduced. You can further reduce it by editing the `reduced_param_grid` in the script.

**Issue: Results look different each run**
- Solution: The script uses `random_state=42` for reproducibility. Make sure you're using the same seed.

**Issue: Feature ranking doesn't show COL5A2, NDNF, FAT1**
- Solution: Check the full ranking file. These genes might appear with variants (e.g., COL5A2.1, COL5A2.2). Also check if they appear in the top 20-30 features, not just top 10.

## Need Help?

1. Check the script output - it prints detailed information at each step
2. Review `HW2_Checklist.md` to ensure completeness
3. Read the assignment instructions carefully
4. Use GenAI as a tutor (document in Appendix I if you do)

## Final Checklist Before Submission

- [ ] All sections completed
- [ ] All tables have captions with data provenance
- [ ] All accuracy measures to 5 decimal places
- [ ] Confusion matrices show full counts
- [ ] Feature ranking compared with ground truth
- [ ] Code snippets included in main body
- [ ] Full code in Appendix II (PDF format)
- [ ] GenAI usage documented (if used)
- [ ] Report is one PDF file
- [ ] File named correctly
- [ ] Email sent with correct subject line

Good luck! 🚀

