# Code Snippets Screenshot Guide

This guide tells you exactly which code sections to screenshot from `hw2_rf_pipeline.py` for your report.

## How to Take Screenshots

1. Open `hw2_rf_pipeline.py` in your code editor
2. Navigate to the line numbers specified below
3. Take a screenshot of the code section
4. Save the screenshot with the filename indicated
5. Insert the screenshot into your report where indicated

---

## Screenshot 1: Database Audit (Section 2.2)

**File:** `hw2_rf_pipeline.py`  
**Lines:** 40-70  
**Save as:** `screenshots/db_audit_code.png`  
**Report Location:** Section 2.2 - Database Audit Checklist

**What to screenshot:**
- Lines showing: `df_original = pd.read_csv(...)`
- Label distribution check
- Missing values check
- Data types check
- Class balance check
- Sample-to-feature ratio check

---

## Screenshot 2: Data Splitting (Section 3.1)

**File:** `hw2_rf_pipeline.py`  
**Lines:** 85-100  
**Save as:** `screenshots/data_split_code.png`  
**Report Location:** Section 3.1 - Methodology

**What to screenshot:**
- Lines showing: `class_0_samples = df_original[df_original['Label'] == 0]`
- Random selection of verification samples
- Creation of verification_db and training_db

---

## Screenshot 3: Method 1 - OOB Training (Section 6.1.2)

**File:** `hw2_rf_pipeline.py`  
**Lines:** 168-202  
**Save as:** `screenshots/method1_oob_code.png`  
**Report Location:** Section 6.1.2 - Key Code Snippet

**What to screenshot:**
- The `for params in ParameterGrid(reduced_param_grid):` loop
- RandomForestClassifier creation with `oob_score=True`
- Model training: `rf.fit(X_train, y_train)`
- OOB score retrieval: `oob_score = rf.oob_score_`
- Best model tracking

---

## Screenshot 4: Accuracy Measures (Section 6.1.4)

**File:** `hw2_rf_pipeline.py`  
**Lines:** 209-217  
**Save as:** `screenshots/accuracy_measures_code.png`  
**Report Location:** Section 6.1.4 - All Accuracy Measures

**What to screenshot:**
- `y_train_pred = best_rf_oob.predict(X_train)`
- `cm_train = confusion_matrix(...)`
- All accuracy measure calculations (accuracy, precision, recall, F1)
- OOB accuracy retrieval

---

## Screenshot 5: Method 2 - Manual CV (Section 6.2.5)

**File:** `hw2_rf_pipeline.py`  
**Lines:** 236-305  
**Save as:** `screenshots/method2_cv_code.png`  
**Report Location:** Section 6.2.5 - Key Code Snippet

**What to screenshot:**
- Manual fold splitting: `folds = [...]`
- The `for fold_num in range(3):` loop
- Train/test split for each fold
- RandomForestClassifier training for each fold
- Prediction and metric computation for each fold

---

## Screenshot 6: Feature Ranking (Section 7.2)

**File:** `hw2_rf_pipeline.py`  
**Lines:** 341-369  
**Save as:** `screenshots/feature_ranking_code.png`  
**Report Location:** Section 7.2 - Key Code Snippet

**What to screenshot:**
- `rf_for_ranking = best_rf_oob`
- `feature_importances = rf_for_ranking.feature_importances_`
- DataFrame creation and sorting
- Ground truth gene checking loop (COL5A2, NDNF, FAT1)

---

## Screenshot 7: Runtime Prediction (Section 8.2)

**File:** `hw2_rf_pipeline.py`  
**Lines:** 382-401  
**Save as:** `screenshots/runtime_prediction_code.png`  
**Report Location:** Section 8.2 - Key Code Snippet

**What to screenshot:**
- `runtime_rf = best_rf_oob`
- `y_verification_pred = runtime_rf.predict(...)`
- `y_verification_proba = runtime_rf.predict_proba(...)`
- The results display loop

---

## Quick Steps

1. Create a folder called `screenshots` in your project directory
2. Open `hw2_rf_pipeline.py` in your editor
3. For each screenshot above:
   - Go to the specified line numbers
   - Select/highlight the code section
   - Take a screenshot (Windows: Win+Shift+S, then paste)
   - Save with the specified filename in the `screenshots` folder
4. In your report, replace the code blocks with the screenshot images

## Alternative: Use the Display Script

You can also run:
```bash
python display_code_snippets.py
```

This will display each code section one at a time, and you can screenshot them from the terminal/console output.

---

## Note for Report

In your report template, I've already replaced the code blocks with placeholders like:
- `*[Screenshot of code from hw2_rf_pipeline.py, lines X-Y]*`
- `![Image Name](screenshots/filename.png)`

Just replace these with your actual screenshots when you add them to the PDF.

