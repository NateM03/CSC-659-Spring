# How to Convert Report to Word

## ✅ Easiest Method: Open Directly in Word

**Microsoft Word can open Markdown files directly!**

1. Open Microsoft Word
2. File → Open
3. Navigate to `HW2_Report_Template.md`
4. Word will convert it automatically
5. Review and format as needed
6. Save as: `CSC 659-859 Spring 2026 HW 2 Moreno.docx`

**Note:** You may need to:
- Adjust table formatting
- Insert your code screenshots where indicated
- Verify all formatting looks correct

---

## Alternative Methods

### Method 2: Online Converter (Recommended if Word doesn't work well)

1. Go to: https://cloudconvert.com/md-to-docx
2. Upload `HW2_Report_Template.md`
3. Convert to DOCX
4. Download the file
5. Rename to: `CSC 659-859 Spring 2026 HW 2 Moreno.docx`
6. Open in Word to review and add screenshots

### Method 3: Install Pandoc (Best Quality)

1. Download Pandoc: https://pandoc.org/installing.html
2. Install it
3. Run this command:
   ```bash
   pandoc HW2_Report_Template.md -o "CSC 659-859 Spring 2026 HW 2 Moreno.docx" --standalone
   ```

### Method 4: VS Code Extension

1. Install VS Code extension: "Markdown PDF" or "Docs Markdown"
2. Open `HW2_Report_Template.md` in VS Code
3. Use the extension to export to Word/DOCX

---

## After Conversion - Important Steps

1. **Add Screenshots:** Replace all `![Image Name](screenshots/...)` placeholders with actual screenshots of your code
2. **Check Tables:** Verify all tables are properly formatted
3. **Check Code Blocks:** Ensure code snippets are readable (or use screenshots)
4. **Add Full Code:** Copy the full code from `hw2_rf_pipeline.py` into Appendix II
5. **Final Review:** Use the submission checklist at the end of the report
6. **Save as PDF:** File → Save As → PDF (for submission)

---

## Quick Command (if Pandoc is installed)

```bash
pandoc HW2_Report_Template.md -o "CSC 659-859 Spring 2026 HW 2 Moreno.docx" --standalone
```

