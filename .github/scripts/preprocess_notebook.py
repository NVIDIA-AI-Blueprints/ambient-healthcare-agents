#!/usr/bin/env python3
"""
Preprocess notebook to make it compatible with papermill parameter injection.

This script creates a copy of the original notebook and modifies it to replace
interactive input() calls with None assignments, which allows papermill to inject
parameters via the -p flag. The original notebook file remains unchanged.

Usage:
    python .github/scripts/preprocess_notebook.py <input_notebook> <output_notebook>
"""

import json
import sys
import re
from pathlib import Path


def preprocess_notebook(input_path: str, output_path: str) -> None:
    """
    Create a copy of notebook and replace input() calls with None assignments.
    
    This allows papermill to inject parameters via -p flag. The modifications include:
    1. Replace VARIABLE_NAME = input("...") with VARIABLE_NAME = None
    2. Replace os.environ["VARIABLE_NAME"] = "<your-api-key>" with os.environ["VARIABLE_NAME"] = None
    3. Ensure 'import os' exists if needed
    
    Args:
        input_path: Path to the original notebook file
        output_path: Path where the preprocessed notebook will be saved
    """
    # Read the original notebook
    with open(input_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Track if we need to add 'import os' at the beginning
    needs_os_import = True
    os_import_added = False
    
    # Process each cell
    for cell in notebook['cells']:
        if cell['cell_type'] != 'code':
            continue
        
        # Join source lines into a single string for easier processing
        source_lines = cell['source']
        source_text = ''.join(source_lines)
        
        # Check if 'import os' already exists in this cell
        if 'import os' in source_text or 'from os import' in source_text:
            needs_os_import = False
        
        # Pattern 1: Replace VARIABLE_NAME = input("...") with VARIABLE_NAME = None
        # This is the standard pattern for papermill parameter injection
        pattern1 = r'(\w+)\s*=\s*input\([^)]+\)'
        if re.search(pattern1, source_text):
            # Replace input() calls with None
            modified_source = re.sub(
                pattern1,
                r'\1 = None',
                source_text
            )
            cell['source'] = modified_source.splitlines(keepends=True)
            
            # Add 'import os' at the beginning of this cell if needed
            if needs_os_import and not os_import_added:
                # Check if this cell already has imports
                first_line = cell['source'][0] if cell['source'] else ''
                if 'import' in first_line.lower():
                    # Find the last import line and add after it
                    import_idx = 0
                    for i, line in enumerate(cell['source']):
                        if 'import' in line.lower():
                            import_idx = i + 1
                    cell['source'].insert(import_idx, 'import os\n')
                else:
                    # Add at the beginning
                    cell['source'] = ['import os\n'] + cell['source']
                os_import_added = True
        
        # Pattern 2: Replace os.environ["VARIABLE"] = "<your-api-key>" with os.environ["VARIABLE"] = None
        # This handles the case in ambient-provider.ipynb
        pattern2 = r'os\.environ\["(\w+)"\]\s*=\s*"[^"]*"'
        if re.search(pattern2, source_text):
            modified_source = re.sub(
                pattern2,
                r'os.environ["\1"] = None',
                source_text
            )
            cell['source'] = modified_source.splitlines(keepends=True)
            
            # Ensure 'import os' exists
            if needs_os_import and not os_import_added:
                if 'import os' not in source_text:
                    # Add import os at the beginning
                    cell['source'] = ['import os\n'] + cell['source']
                os_import_added = True
    
    # Save the preprocessed notebook
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    
    print(f"Preprocessed notebook saved to: {output_path}")


def main():
    """Main entry point for the script."""
    if len(sys.argv) != 3:
        print("Usage: python .github/scripts/preprocess_notebook.py <input_notebook> <output_notebook>")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    # Validate input file exists
    if not Path(input_path).exists():
        print(f"Error: Input notebook not found: {input_path}")
        sys.exit(1)
    
    # Create output directory if it doesn't exist
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        preprocess_notebook(input_path, output_path)
    except Exception as e:
        print(f"Error preprocessing notebook: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()

