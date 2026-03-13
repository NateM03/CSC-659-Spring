"""
Script to help regenerate PDF from updated markdown template.
This ensures all Gemini fixes are included in the final PDF.
"""

import os
import subprocess
import sys

def check_pandoc():
    """Check if pandoc is installed"""
    try:
        result = subprocess.run(['pandoc', '--version'], 
                              capture_output=True, text=True)
        return True
    except FileNotFoundError:
        return False

def convert_with_pandoc():
    """Convert markdown to PDF using pandoc"""
    input_file = 'HW2_Report_Template.md'
    output_file = 'CSC 659-859 Spring 2026 HW 2 Moreno.pdf'
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found!")
        return False
    
    cmd = [
        'pandoc',
        input_file,
        '-o', output_file,
        '--standalone',
        '--pdf-engine=pdflatex',  # or 'xelatex' if you have it
        '--variable=geometry:margin=1in'
    ]
    
    try:
        print(f"Converting {input_file} to PDF...")
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Success! PDF created: {output_file}")
            return True
        else:
            print(f"Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"Error running pandoc: {e}")
        return False

def main():
    print("=" * 60)
    print("PDF Regeneration Helper")
    print("=" * 60)
    print()
    
    if check_pandoc():
        print("✅ Pandoc is installed!")
        print()
        if convert_with_pandoc():
            print()
            print("Next steps:")
            print("1. Open the PDF and verify formatting")
            print("2. Add your code screenshots where indicated")
            print("3. Add full code to Appendix II")
            print("4. Final review using submission checklist")
        else:
            print("Conversion failed. Try opening in Word instead.")
    else:
        print("❌ Pandoc is not installed.")
        print()
        print("RECOMMENDED: Open HW2_Report_Template.md in Microsoft Word")
        print("Word will convert it automatically, then:")
        print("1. Add your code screenshots")
        print("2. Add full code to Appendix II")
        print("3. Save as PDF: 'CSC 659-859 Spring 2026 HW 2 Moreno.PDF'")
        print()
        print("Alternative: Install Pandoc from https://pandoc.org/installing.html")
        print("Then run this script again.")

if __name__ == "__main__":
    main()

