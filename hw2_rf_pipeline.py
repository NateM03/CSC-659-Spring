"""
CSC 659/859 Spring 2026 - HW 2
Random Forest ML Pipeline for i1 Cluster Classification
Author: [Your Name]
Date: [Date]

Purpose:
This script implements a complete Random Forest pipeline for classifying i1 nerve cluster
data from JCV experiment. It includes:
- Database audit and splitting
- OOB accuracy estimation (Method 1)
- Manual 3-fold CV (Method 2)
- Feature ranking analysis
- Runtime prediction on verification set
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import ParameterGrid
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import warnings
warnings.filterwarnings('ignore')

# Set random seed for reproducibility
np.random.seed(42)

print("=" * 80)
print("CSC 659/859 Spring 2026 - HW 2: Random Forest Pipeline")
print("=" * 80)

# ============================================================================
# SECTION 1: Load and Audit Original Database
# ============================================================================
print("\n" + "=" * 80)
print("SECTION 1: Loading and Auditing Original Database")
print("=" * 80)

# Load the original database
df_original = pd.read_csv('Original training DB i1 cluster.csv')
print(f"\nOriginal Database Statistics:")
print(f"  Total samples: {len(df_original)}")
print(f"  Total features: {len(df_original.columns) - 1}")  # Excluding label column
print(f"  Total columns: {len(df_original.columns)}")

# Check label distribution
label_counts = df_original['Label'].value_counts()
print(f"\nLabel Distribution:")
print(f"  Class 0 (non-i1): {label_counts[0]} samples ({label_counts[0]/len(df_original)*100:.2f}%)")
print(f"  Class 1 (i1 cluster): {label_counts[1]} samples ({label_counts[1]/len(df_original)*100:.2f}%)")

# Check for missing values
missing_values = df_original.isnull().sum().sum()
print(f"\nMissing Values: {missing_values}")

# Check data types
print(f"\nData Types:")
print(f"  All features are numerical: {df_original.iloc[:, :-1].dtypes.apply(lambda x: pd.api.types.is_numeric_dtype(x)).all()}")

# Check if class is unbalanced (less than 10% in minority class)
minority_class_pct = min(label_counts) / len(df_original) * 100
is_unbalanced = minority_class_pct < 10
print(f"\nClass Balance Check:")
print(f"  Minority class percentage: {minority_class_pct:.2f}%")
print(f"  Is unbalanced (<10%): {is_unbalanced}")

# Check sample-to-feature ratio
n_features = len(df_original.columns) - 1
n_samples = len(df_original)
ratio = n_samples / n_features
print(f"\nSample-to-Feature Ratio:")
print(f"  Ratio: {ratio:.2f}:1")
print(f"  Meets requirement (>=10:1): {ratio >= 10}")

# ============================================================================
# SECTION 2: Create Training and Verification Databases
# ============================================================================
print("\n" + "=" * 80)
print("SECTION 2: Creating Training and Verification Databases")
print("=" * 80)

# Separate class 0 and class 1 samples
class_0_samples = df_original[df_original['Label'] == 0].copy()
class_1_samples = df_original[df_original['Label'] == 1].copy()

# Randomly select 1 sample from each class for verification
np.random.seed(42)
verification_class_0_idx = np.random.choice(class_0_samples.index, size=1, replace=False)
verification_class_1_idx = np.random.choice(class_1_samples.index, size=1, replace=False)

# Create verification database
verification_db = pd.concat([
    df_original.loc[verification_class_0_idx],
    df_original.loc[verification_class_1_idx]
], ignore_index=True)

# Create training database (original minus verification samples)
training_db = df_original.drop(index=verification_class_0_idx).drop(index=verification_class_1_idx).reset_index(drop=True)

print(f"\nTraining Database Statistics:")
print(f"  Total samples: {len(training_db)}")
print(f"  Class 0: {len(training_db[training_db['Label'] == 0])} samples")
print(f"  Class 1: {len(training_db[training_db['Label'] == 1])} samples")

print(f"\nVerification Database Statistics:")
print(f"  Total samples: {len(verification_db)}")
print(f"  Class 0: {len(verification_db[verification_db['Label'] == 0])} samples")
print(f"  Class 1: {len(verification_db[verification_db['Label'] == 1])} samples")

# Save verification database
verification_db.to_csv('verification_db.csv', index=False)
print(f"\nVerification database saved to 'verification_db.csv'")

# Prepare features and labels for training
X_train = training_db.drop('Label', axis=1)
y_train = training_db['Label']
X_verification = verification_db.drop('Label', axis=1)
y_verification = verification_db['Label']

# ============================================================================
# SECTION 3: Method 1 - OOB Accuracy Estimation
# ============================================================================
print("\n" + "=" * 80)
print("SECTION 3: Method 1 - OOB Accuracy Estimation with Grid Search")
print("=" * 80)

# Define hyperparameter grid
param_grid = {
    'n_estimators': [100, 200, 300, 500],
    'max_features': ['sqrt', 'log2', 0.3, 0.5],
    'max_depth': [10, 20, 30, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'class_weight': ['balanced', None]
}

print(f"\nHyperparameter Grid Search Space:")
print(f"  n_estimators: {param_grid['n_estimators']}")
print(f"  max_features: {param_grid['max_features']}")
print(f"  max_depth: {param_grid['max_depth']}")
print(f"  min_samples_split: {param_grid['min_samples_split']}")
print(f"  min_samples_leaf: {param_grid['min_samples_leaf']}")
print(f"  class_weight: {param_grid['class_weight']}")

# Note: Full grid search would be computationally expensive
# We'll do a reduced grid search for demonstration
# In practice, you might want to use RandomizedSearchCV or a smaller grid

# Reduced grid for faster execution (you can expand this)
reduced_param_grid = {
    'n_estimators': [200, 300, 500],
    'max_features': ['sqrt', 0.3, 0.5],
    'max_depth': [20, 30, None],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2],
    'class_weight': ['balanced']
}

print(f"\nUsing reduced grid for faster execution...")
print(f"  Total combinations to test: {len(list(ParameterGrid(reduced_param_grid)))}")

best_oob_score = 0
best_params = None
best_rf_oob = None
results_method1 = []

print("\nPerforming grid search with OOB scoring...")
for i, params in enumerate(ParameterGrid(reduced_param_grid)):
    if i % 10 == 0:
        print(f"  Testing combination {i+1}/{len(list(ParameterGrid(reduced_param_grid)))}...")
    
    # Create RF with OOB scoring enabled
    rf = RandomForestClassifier(
        n_estimators=params['n_estimators'],
        max_features=params['max_features'],
        max_depth=params['max_depth'],
        min_samples_split=params['min_samples_split'],
        min_samples_leaf=params['min_samples_leaf'],
        class_weight=params['class_weight'],
        oob_score=True,
        random_state=42,
        n_jobs=-1
    )
    
    # Train the model
    rf.fit(X_train, y_train)
    
    # Get OOB score
    oob_score = rf.oob_score_
    
    # Store results
    results_method1.append({
        'params': params.copy(),
        'oob_score': oob_score,
        'model': rf
    })
    
    # Update best model
    if oob_score > best_oob_score:
        best_oob_score = oob_score
        best_params = params.copy()
        best_rf_oob = rf

print(f"\nBest OOB Score: {best_oob_score:.5f}")
print(f"Best Parameters:")
for key, value in best_params.items():
    print(f"  {key}: {value}")

# Get predictions on training set for confusion matrix
y_train_pred = best_rf_oob.predict(X_train)
cm_train = confusion_matrix(y_train, y_train_pred)

# Calculate all accuracy measures
accuracy_train = accuracy_score(y_train, y_train_pred)
precision_train = precision_score(y_train, y_train_pred, zero_division=0)
recall_train = recall_score(y_train, y_train_pred, zero_division=0)
f1_train = f1_score(y_train, y_train_pred, zero_division=0)

print(f"\nMethod 1 - Training Set Results:")
print(f"  OOB Accuracy: {best_oob_score:.5f}")
print(f"  Training Accuracy: {accuracy_train:.5f}")
print(f"  Precision: {precision_train:.5f}")
print(f"  Recall: {recall_train:.5f}")
print(f"  F1 Score: {f1_train:.5f}")
print(f"\nConfusion Matrix (Training Set):")
print(f"  True Negative: {cm_train[0,0]}, False Positive: {cm_train[0,1]}")
print(f"  False Negative: {cm_train[1,0]}, True Positive: {cm_train[1,1]}")

# ============================================================================
# SECTION 4: Method 2 - Manual 3-Fold Cross-Validation
# ============================================================================
print("\n" + "=" * 80)
print("SECTION 4: Method 2 - Manual 3-Fold Cross-Validation")
print("=" * 80)

# Shuffle the training data
train_indices = np.arange(len(training_db))
np.random.seed(42)
np.random.shuffle(train_indices)

# Split into 3 folds manually
n_samples = len(train_indices)
fold_size = n_samples // 3
folds = [
    train_indices[0:fold_size],
    train_indices[fold_size:2*fold_size],
    train_indices[2*fold_size:]
]

print(f"\nFold sizes: {[len(fold) for fold in folds]}")

cv_results = []
best_cv_score = 0
best_rf_cv = None
best_cv_params = None

# Use best parameters from Method 1 as starting point, or use a fixed set
# For CV, we'll use the best params from Method 1
cv_params = best_params.copy()

for fold_num in range(3):
    print(f"\n--- Fold {fold_num + 1} ---")
    
    # Create test and train indices for this fold
    test_indices = folds[fold_num]
    train_indices_fold = np.concatenate([folds[i] for i in range(3) if i != fold_num])
    
    # Split data
    X_train_fold = X_train.iloc[train_indices_fold]
    y_train_fold = y_train.iloc[train_indices_fold]
    X_test_fold = X_train.iloc[test_indices]
    y_test_fold = y_train.iloc[test_indices]
    
    print(f"  Train: {len(X_train_fold)} samples (Class 0: {sum(y_train_fold==0)}, Class 1: {sum(y_train_fold==1)})")
    print(f"  Test: {len(X_test_fold)} samples (Class 0: {sum(y_test_fold==0)}, Class 1: {sum(y_test_fold==1)})")
    
    # Train RF model
    rf_cv = RandomForestClassifier(
        n_estimators=cv_params['n_estimators'],
        max_features=cv_params['max_features'],
        max_depth=cv_params['max_depth'],
        min_samples_split=cv_params['min_samples_split'],
        min_samples_leaf=cv_params['min_samples_leaf'],
        class_weight=cv_params['class_weight'],
        random_state=42,
        n_jobs=-1
    )
    
    rf_cv.fit(X_train_fold, y_train_fold)
    
    # Predict on test set
    y_pred_fold = rf_cv.predict(X_test_fold)
    
    # Calculate metrics
    accuracy_fold = accuracy_score(y_test_fold, y_pred_fold)
    precision_fold = precision_score(y_test_fold, y_pred_fold, zero_division=0)
    recall_fold = recall_score(y_test_fold, y_pred_fold, zero_division=0)
    f1_fold = f1_score(y_test_fold, y_pred_fold, zero_division=0)
    cm_fold = confusion_matrix(y_test_fold, y_pred_fold)
    
    print(f"  Accuracy: {accuracy_fold:.5f}")
    print(f"  Precision: {precision_fold:.5f}")
    print(f"  Recall: {recall_fold:.5f}")
    print(f"  F1 Score: {f1_fold:.5f}")
    print(f"  Confusion Matrix: TN={cm_fold[0,0]}, FP={cm_fold[0,1]}, FN={cm_fold[1,0]}, TP={cm_fold[1,1]}")
    
    cv_results.append({
        'fold': fold_num + 1,
        'accuracy': accuracy_fold,
        'precision': precision_fold,
        'recall': recall_fold,
        'f1': f1_fold,
        'confusion_matrix': cm_fold
    })
    
    # Track best model (highest F1 score)
    if f1_fold > best_cv_score:
        best_cv_score = f1_fold
        best_rf_cv = rf_cv
        best_cv_params = cv_params.copy()

# Calculate average CV metrics
avg_accuracy = np.mean([r['accuracy'] for r in cv_results])
avg_precision = np.mean([r['precision'] for r in cv_results])
avg_recall = np.mean([r['recall'] for r in cv_results])
avg_f1 = np.mean([r['f1'] for r in cv_results])

print(f"\n--- CV Summary ---")
print(f"Average Accuracy: {avg_accuracy:.5f}")
print(f"Average Precision: {avg_precision:.5f}")
print(f"Average Recall: {avg_recall:.5f}")
print(f"Average F1 Score: {avg_f1:.5f}")

# ============================================================================
# SECTION 5: Feature Ranking
# ============================================================================
print("\n" + "=" * 80)
print("SECTION 5: Feature Ranking Analysis")
print("=" * 80)

# Use the best model from Method 1 for feature ranking
rf_for_ranking = best_rf_oob

# Get feature importances (Gini importance)
feature_importances = rf_for_ranking.feature_importances_
feature_names = X_train.columns

# Create DataFrame for easier handling
importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': feature_importances
}).sort_values('Importance', ascending=False)

print(f"\nTop 10 Features by Gini Importance:")
print(importance_df.head(10).to_string(index=False))

# Check for ground truth genes (COL5A2, NDNF, FAT1)
ground_truth_genes = ['COL5A2', 'NDNF', 'FAT1']
print(f"\nGround Truth Gene Analysis:")
for gene in ground_truth_genes:
    # Find all features containing this gene name
    matching_features = importance_df[importance_df['Feature'].str.contains(gene, case=False, na=False)]
    if len(matching_features) > 0:
        print(f"\n  {gene} family features found:")
        for idx, row in matching_features.iterrows():
            rank = importance_df.index.get_loc(idx) + 1
            print(f"    {row['Feature']}: Rank {rank}, Importance {row['Importance']:.5f}")
    else:
        print(f"  {gene}: Not found in top features")

# Save feature ranking
importance_df.to_csv('feature_ranking.csv', index=False)
print(f"\nFull feature ranking saved to 'feature_ranking.csv'")

# ============================================================================
# SECTION 6: Runtime Prediction on Verification Database
# ============================================================================
print("\n" + "=" * 80)
print("SECTION 6: Runtime Prediction on Verification Database")
print("=" * 80)

# Use best model from Method 1 for runtime prediction
runtime_rf = best_rf_oob

# Predict on verification samples
y_verification_pred = runtime_rf.predict(X_verification)
y_verification_proba = runtime_rf.predict_proba(X_verification)

print(f"\nVerification Sample Predictions:")
for i in range(len(verification_db)):
    true_label = y_verification.iloc[i]
    pred_label = y_verification_pred[i]
    proba = y_verification_proba[i]
    
    print(f"\nSample {i+1}:")
    print(f"  True Label: {true_label} ({'i1 cluster' if true_label == 1 else 'non-i1'})")
    print(f"  Predicted Label: {pred_label} ({'i1 cluster' if pred_label == 1 else 'non-i1'})")
    print(f"  Probability Class 0: {proba[0]:.5f}")
    print(f"  Probability Class 1: {proba[1]:.5f}")
    print(f"  Correct: {'Yes' if true_label == pred_label else 'No'}")
    print(f"  Confidence: {max(proba):.5f}")

# ============================================================================
# SECTION 7: Save Results Summary
# ============================================================================
print("\n" + "=" * 80)
print("SECTION 7: Saving Results Summary")
print("=" * 80)

# Create summary DataFrame for Method 1
method1_summary = pd.DataFrame([{
    'Method': 'OOB',
    'OOB_Accuracy': best_oob_score,
    'Training_Accuracy': accuracy_train,
    'Precision': precision_train,
    'Recall': recall_train,
    'F1_Score': f1_train,
    'n_estimators': best_params['n_estimators'],
    'max_features': str(best_params['max_features']),
    'max_depth': str(best_params['max_depth']),
    'min_samples_split': best_params['min_samples_split'],
    'min_samples_leaf': best_params['min_samples_leaf'],
    'class_weight': str(best_params['class_weight'])
}])

# Create summary DataFrame for Method 2
method2_summary = pd.DataFrame([{
    'Method': '3-Fold CV',
    'Avg_Accuracy': avg_accuracy,
    'Avg_Precision': avg_precision,
    'Avg_Recall': avg_recall,
    'Avg_F1_Score': avg_f1,
    'Fold1_Accuracy': cv_results[0]['accuracy'],
    'Fold2_Accuracy': cv_results[1]['accuracy'],
    'Fold3_Accuracy': cv_results[2]['accuracy'],
    'Fold1_F1': cv_results[0]['f1'],
    'Fold2_F1': cv_results[1]['f1'],
    'Fold3_F1': cv_results[2]['f1']
}])

# Save summaries
method1_summary.to_csv('method1_results.csv', index=False)
method2_summary.to_csv('method2_results.csv', index=False)

print("\nResults saved:")
print("  - method1_results.csv")
print("  - method2_results.csv")
print("  - feature_ranking.csv")
print("  - verification_db.csv")

print("\n" + "=" * 80)
print("Pipeline execution completed successfully!")
print("=" * 80)

