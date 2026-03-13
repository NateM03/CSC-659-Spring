# HW 2 - Full Points Checklist

Use this checklist to ensure you get full points on your assignment.

## Pre-Submission Checklist

### 1. Title Page (Required)
- [ ] HW 2 title included
- [ ] Class number (CSC 659/859)
- [ ] Semester (Spring 2026)
- [ ] Date
- [ ] Your name
- [ ] Your email

### 2. Section 2: Audit of Original Database (2 points)
- [ ] Data source described with reference to biology paper
- [ ] All 8 audit checklist items addressed:
  - [ ] Feature description and data format documented
  - [ ] Class label verification explained (reference to paper)
  - [ ] Demography coverage (if applicable)
  - [ ] Class balance analysis (check if unbalanced <10%)
  - [ ] Feature types declared (all numerical)
  - [ ] Missing values checked and explained
  - [ ] Sample-to-feature ratio calculated (must be ≥10:1)
  - [ ] Privacy issues addressed
- [ ] Summary statistics table included
- [ ] All values filled in from actual script output

### 3. Section 3: Training and Verification DB (1 point)
- [ ] Explained how 2 random samples were removed (1 class 0, 1 class 1)
- [ ] Training DB statistics table (samples, classes, features)
- [ ] Verification DB statistics table (2 samples)
- [ ] Random seed mentioned for reproducibility

### 4. Section 4: SW Tools (Not graded, but required)
- [ ] Listed main ML tools used (Python, scikit-learn, etc.)
- [ ] Version numbers if relevant

### 5. Section 5: Experimental Methods and Setup (5 points)
- [ ] **Method 1 (OOB):**
  - [ ] Method briefly explained
  - [ ] Software classes/methods listed
  - [ ] All hyperparameter ranges listed in table
  - [ ] All accuracy measures listed with formulae
- [ ] **Method 2 (CV):**
  - [ ] 3-fold CV explained (manual implementation)
  - [ ] Steps for each fold described
  - [ ] Software classes/methods listed
  - [ ] Accuracy measures to compute listed
- [ ] **Comparison:**
  - [ ] How results will be compared explained

### 6. Section 6: Actual Results (8 points)
- [ ] **Method 1 Results:**
  - [ ] Best hyperparameters shown in table
  - [ ] Key code snippet included
  - [ ] Confusion matrix (full counts, axes labeled)
  - [ ] All accuracy measures (5 decimal places):
    - [ ] OOB Accuracy
    - [ ] Training Accuracy
    - [ ] Precision
    - [ ] Recall
    - [ ] F1 Score
- [ ] **Method 2 Results:**
  - [ ] For each of 3 folds:
    - [ ] Train/test sample counts (class 0 and class 1)
    - [ ] Accuracy and F1 score
    - [ ] Confusion matrix (optional but recommended)
  - [ ] Final average accuracy and F1
  - [ ] Key code snippet included
- [ ] **Comparison:**
  - [ ] Comparison table with both methods
  - [ ] Text discussion comparing results

### 7. Section 7: Feature Ranking (3 points)
- [ ] Explained how feature ranking was obtained (Gini for scikit-learn)
- [ ] Best trained RF model identified
- [ ] Key code snippet included
- [ ] Top 10 ranked features shown in table or plot
- [ ] **Discussion:**
  - [ ] Comparison with ground truth (COL5A2, NDNF, FAT1)
  - [ ] Analysis of feature dominance
  - [ ] Recommendation for production feature count

### 8. Section 8: RF Run Time Test (2 points)
- [ ] Runtime engine creation described
- [ ] Key hyperparameters shown
- [ ] Key code snippet included
- [ ] Verification DB predictions table:
  - [ ] True label
  - [ ] Predicted label
  - [ ] Probability for each class
- [ ] **Discussion:**
  - [ ] Classification correctness
  - [ ] Confidence assessment for each sample
  - [ ] How confidence was determined

### 9. Section 9: Resources (Required)
- [ ] All papers/references listed
- [ ] Tools used listed
- [ ] GenAI usage mentioned (if used)
- [ ] People who helped listed (if any)

### 10. Appendix I: GenAI Use (Required if used)
For each task where GenAI was used:
- [ ] Task description
- [ ] Example prompts shown
- [ ] Key GenAI output shown
- [ ] Usefulness rating (1-5)

### 11. Appendix II: Full Code (Required)
- [ ] Full code included (in PDF format)
- [ ] Header comments (purpose, HW 2, name, date)
- [ ] In-line documentation for major sections
- [ ] Code is readable and well-organized

## Report Quality Checklist (4 points)

### Formatting and Organization
- [ ] All section titles match exactly as specified
- [ ] Sections in correct order
- [ ] Professional formatting
- [ ] Easy to read

### Tables and Figures
- [ ] All key results in tables or charts
- [ ] Every table/chart has:
  - [ ] Enumerated caption
  - [ ] Full data provenance
  - [ ] All parameters and settings described
  - [ ] Axes labeled (for charts)

### Data Presentation
- [ ] All accuracy measures to 5 decimal places
- [ ] Confusion matrices show full counts (not normalized)
- [ ] All parameters clearly marked (ntree, mtry, etc.)
- [ ] Sufficient textual explanations for each step

### Code Presentation
- [ ] Key code snippets in main body
- [ ] Full code in Appendix II
- [ ] Code is documented

## Submission Checklist

- [ ] Report is one PDF file
- [ ] File name: "CSC 659-859 Spring 2026 HW 2 [Your Last Name].PDF"
- [ ] Email subject: "CS 659 859 Spring 2026 HW 2 [Your Last Name]"
- [ ] Email body includes courtesy text
- [ ] Sent to: Petkovic@sfsu.edu
- [ ] Submitted before deadline (or extension approved)

## Common Mistakes to Avoid

1. **Don't use one-liner CV methods** - Must do 3-fold CV manually
2. **Don't round accuracy measures** - Use 5 decimal places
3. **Don't normalize confusion matrices** - Show full counts
4. **Don't forget ground truth comparison** - Must discuss COL5A2, NDNF, FAT1
5. **Don't skip any sections** - All sections are required
6. **Don't forget to label axes** - All charts need labeled axes
7. **Don't forget data provenance** - Every table/chart needs full description
8. **Don't use executable code in report** - Code in PDF format only

## Point Breakdown Reminder

- Section 2 (Audit): 2 points
- Section 3 (DB Split): 1 point
- Section 5 (Methods): 5 points
- Section 6 (Results): 8 points
- Section 7 (Feature Ranking): 3 points
- Section 8 (Runtime Test): 2 points
- Section 9 (Presentation/Organization): 4 points
- **Total: 25 points**

## Final Review

Before submitting, ask yourself:
1. Can an average ML professional understand my report without asking questions?
2. Are all tables/charts fully explained?
3. Are all required sections present and complete?
4. Is the code properly documented?
5. Have I compared my feature ranking with the ground truth?
6. Have I explained my confidence in the predictions?

Good luck! 🎓

