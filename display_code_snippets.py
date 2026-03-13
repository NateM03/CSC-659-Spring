"""
Helper script to display code snippets for screenshots in the report.
Run this script and take screenshots of each section as it displays.
"""

import sys

# Code snippet 1: Database Audit
print("=" * 80)
print("CODE SNIPPET 1: Database Audit (Section 2.2)")
print("=" * 80)
print("""
# Load the original database
df_original = pd.read_csv('Original training DB i1 cluster.csv')

# Check label distribution
label_counts = df_original['Label'].value_counts()

# Check for missing values
missing_values = df_original.isnull().sum().sum()

# Check data types
all_numerical = df_original.iloc[:, :-1].dtypes.apply(lambda x: pd.api.types.is_numeric_dtype(x)).all()

# Check if class is unbalanced
minority_class_pct = min(label_counts) / len(df_original) * 100
is_unbalanced = minority_class_pct < 10

# Check sample-to-feature ratio
n_features = len(df_original.columns) - 1
n_samples = len(df_original)
ratio = n_samples / n_features
""")
input("\nPress Enter to continue to next snippet...")

# Code snippet 2: Data Splitting
print("\n" + "=" * 80)
print("CODE SNIPPET 2: Training/Verification DB Split (Section 3.1)")
print("=" * 80)
print("""
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
""")
input("\nPress Enter to continue to next snippet...")

# Code snippet 3: Method 1 - OOB Training
print("\n" + "=" * 80)
print("CODE SNIPPET 3: Method 1 - OOB Training (Section 6.1.2)")
print("=" * 80)
print("""
# Grid search with OOB scoring
for params in ParameterGrid(reduced_param_grid):
    # Create RF with OOB scoring enabled
    rf = RandomForestClassifier(
        n_estimators=params['n_estimators'],
        max_features=params['max_features'],
        max_depth=params['max_depth'],
        min_samples_split=params['min_samples_split'],
        min_samples_leaf=params['min_samples_leaf'],
        class_weight=params['class_weight'],
        oob_score=True,  # Enable OOB scoring
        random_state=42,
        n_jobs=-1
    )
    
    # Train the model
    rf.fit(X_train, y_train)
    
    # Get OOB score
    oob_score = rf.oob_score_
    
    # Track best model
    if oob_score > best_oob_score:
        best_oob_score = oob_score
        best_params = params.copy()
        best_rf_oob = rf
""")
input("\nPress Enter to continue to next snippet...")

# Code snippet 4: Accuracy Measures
print("\n" + "=" * 80)
print("CODE SNIPPET 4: Computing Accuracy Measures (Section 6.1.4)")
print("=" * 80)
print("""
# Get predictions on training set
y_train_pred = best_rf_oob.predict(X_train)
cm_train = confusion_matrix(y_train, y_train_pred)

# Calculate all accuracy measures
accuracy_train = accuracy_score(y_train, y_train_pred)
precision_train = precision_score(y_train, y_train_pred, zero_division=0)
recall_train = recall_score(y_train, y_train_pred, zero_division=0)
f1_train = f1_score(y_train, y_train_pred, zero_division=0)

# OOB accuracy is already available from the model
oob_accuracy = best_rf_oob.oob_score_
""")
input("\nPress Enter to continue to next snippet...")

# Code snippet 5: Method 2 - Manual CV
print("\n" + "=" * 80)
print("CODE SNIPPET 5: Method 2 - Manual 3-Fold CV (Section 6.2.5)")
print("=" * 80)
print("""
# Manual 3-fold CV implementation
# Shuffle and split indices into 3 folds
train_indices = np.arange(len(training_db))
np.random.seed(42)
np.random.shuffle(train_indices)

fold_size = n_samples // 3
folds = [
    train_indices[0:fold_size],
    train_indices[fold_size:2*fold_size],
    train_indices[2*fold_size:]
]

# For each fold
for fold_num in range(3):
    # Create test and train indices for this fold
    test_indices = folds[fold_num]
    train_indices_fold = np.concatenate([folds[i] for i in range(3) if i != fold_num])
    
    # Split data
    X_train_fold = X_train.iloc[train_indices_fold]
    y_train_fold = y_train.iloc[train_indices_fold]
    X_test_fold = X_train.iloc[test_indices]
    y_test_fold = y_train.iloc[test_indices]
    
    # Train RF model with best parameters from Method 1
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
    
    # Predict and compute metrics
    y_pred_fold = rf_cv.predict(X_test_fold)
    accuracy_fold = accuracy_score(y_test_fold, y_pred_fold)
    precision_fold = precision_score(y_test_fold, y_pred_fold, zero_division=0)
    recall_fold = recall_score(y_test_fold, y_pred_fold, zero_division=0)
    f1_fold = f1_score(y_test_fold, y_pred_fold, zero_division=0)
    cm_fold = confusion_matrix(y_test_fold, y_pred_fold)
""")
input("\nPress Enter to continue to next snippet...")

# Code snippet 6: Feature Ranking
print("\n" + "=" * 80)
print("CODE SNIPPET 6: Feature Ranking (Section 7.2)")
print("=" * 80)
print("""
# Feature ranking using Gini importance
# Use the best model from Method 1
rf_for_ranking = best_rf_oob

# Get feature importances (Gini importance)
feature_importances = rf_for_ranking.feature_importances_
feature_names = X_train.columns

# Create DataFrame and sort by importance
importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': feature_importances
}).sort_values('Importance', ascending=False)

# Get top 10 features
top_10_features = importance_df.head(10)

# Check for ground truth genes (COL5A2, NDNF, FAT1)
ground_truth_genes = ['COL5A2', 'NDNF', 'FAT1']
for gene in ground_truth_genes:
    # Find all features containing this gene name
    matching_features = importance_df[importance_df['Feature'].str.contains(gene, case=False, na=False)]
    if len(matching_features) > 0:
        print(f"\\n{gene} family features found:")
        for idx, row in matching_features.iterrows():
            rank = importance_df.index.get_loc(idx) + 1
            print(f"  {row['Feature']}: Rank {rank}, Importance {row['Importance']:.5f}")
""")
input("\nPress Enter to continue to next snippet...")

# Code snippet 7: Runtime Prediction
print("\n" + "=" * 80)
print("CODE SNIPPET 7: Runtime Prediction (Section 8.2)")
print("=" * 80)
print("""
# Runtime prediction using best model
runtime_rf = best_rf_oob  # Use best model from Method 1

# Predict on verification samples
y_verification_pred = runtime_rf.predict(X_verification)
y_verification_proba = runtime_rf.predict_proba(X_verification)

# Display results
for i in range(len(verification_db)):
    true_label = y_verification.iloc[i]
    pred_label = y_verification_pred[i]
    proba = y_verification_proba[i]
    
    print(f"Sample {i+1}:")
    print(f"  True Label: {true_label}")
    print(f"  Predicted Label: {pred_label}")
    print(f"  Probability Class 0: {proba[0]:.5f}")
    print(f"  Probability Class 1: {proba[1]:.5f}")
    print(f"  Confidence: {max(proba):.5f}")
""")
print("\n" + "=" * 80)
print("All code snippets displayed! Take screenshots of each section above.")
print("=" * 80)

