#!/usr/bin/env python3
"""
Notebook Format Validator

This script validates that Jupyter Notebook files have correct format,
specifically ensuring that source array elements have proper newlines.

According to Jupyter Notebook specification:
- When source is an array of strings, elements are joined WITHOUT separators
- Each element MUST end with '\n' if a newline is needed between elements
- This prevents code concatenation issues (e.g., 'import osexit_code')

Usage:
    python3 validate_notebook_format.py notebook.ipynb
    python3 validate_notebook_format.py *.ipynb
"""

import argparse
import json
import sys
from pathlib import Path
from typing import List, Tuple


def validate_notebook_source_format(notebook_path: Path) -> Tuple[bool, List[str]]:
    """
    Validate notebook source format.
    
    Returns:
        (is_valid, error_messages)
    """
    errors = []
    
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
    except json.JSONDecodeError as e:
        return False, [f"Invalid JSON: {e}"]
    except Exception as e:
        return False, [f"Failed to read notebook: {e}"]
    
    cells = nb.get('cells', [])
    if not cells:
        return True, []  # Empty notebook is valid
    
    for cell_idx, cell in enumerate(cells):
        if cell.get('cell_type') != 'code':
            continue  # Only validate code cells
        
        source = cell.get('source', [])
        if not source:
            continue  # Empty source is valid
        
        # Check if source is an array
        if isinstance(source, list):
            # Validate each element (except the last one)
            for elem_idx in range(len(source) - 1):
                elem = source[elem_idx]
                if isinstance(elem, str):
                    # Check if element should end with newline
                    # Rule: If next element exists and is not empty, current should end with \n
                    next_elem = source[elem_idx + 1]
                    if isinstance(next_elem, str) and next_elem.strip():
                        # Check if current element ends with newline
                        if not elem.endswith('\n'):
                            # Check if this would cause concatenation issues
                            # Common problematic patterns:
                            problematic_patterns = [
                                ('import os', 'exit_code'),
                                ('import os', 'exit_code'),
                                ('}', 'check_'),
                                ('}', 'echo'),
                                ('}', 'for'),
                                ('}', 'done'),
                                ('done', 'echo'),
                                ('done', 'for'),
                                ('done', '#'),
                            ]
                            
                            # Check if concatenation would create problematic patterns
                            concatenated = elem + next_elem
                            has_problem = False
                            for pattern_start, pattern_end in problematic_patterns:
                                if pattern_start in elem.rstrip() and pattern_end in next_elem.lstrip():
                                    # Check if they would be concatenated
                                    if elem.rstrip().endswith(pattern_start) and next_elem.lstrip().startswith(pattern_end):
                                        has_problem = True
                                        break
                            
                            if has_problem or (elem.strip() and next_elem.strip()):
                                errors.append(
                                    f"Cell {cell_idx}: Element {elem_idx} missing newline. "
                                    f"Content: {repr(elem[:50])}... → {repr(next_elem[:30])}..."
                                )
        elif isinstance(source, str):
            # Single string format is always valid
            pass
    
    return len(errors) == 0, errors


def validate_notebook_structure(notebook_path: Path) -> Tuple[bool, List[str]]:
    """
    Validate basic notebook structure.
    
    Returns:
        (is_valid, error_messages)
    """
    errors = []
    
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
    except json.JSONDecodeError as e:
        return False, [f"Invalid JSON: {e}"]
    except Exception as e:
        return False, [f"Failed to read notebook: {e}"]
    
    # Check required fields
    if 'cells' not in nb:
        errors.append("Missing 'cells' field")
    
    if 'cells' in nb and not isinstance(nb['cells'], list):
        errors.append("'cells' must be a list")
    
    return len(errors) == 0, errors


def main():
    parser = argparse.ArgumentParser(
        description='Validate Jupyter Notebook format',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Validate a single notebook
  %(prog)s notebook.ipynb

  # Validate multiple notebooks
  %(prog)s *.ipynb

  # Validate with verbose output
  %(prog)s -v notebook.ipynb
        """
    )
    
    parser.add_argument(
        'notebooks',
        nargs='+',
        help='Notebook file(s) to validate'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Show detailed validation information'
    )
    
    parser.add_argument(
        '--skip-structure-check',
        action='store_true',
        help='Skip basic structure validation (only check source format)'
    )
    
    args = parser.parse_args()
    
    # Collect all notebook files
    notebook_files = []
    for pattern in args.notebooks:
        path = Path(pattern)
        if path.exists() and path.is_file():
            notebook_files.append(path)
        elif '*' in pattern or '?' in pattern:
            # Handle glob patterns
            import glob
            notebook_files.extend([Path(f) for f in glob.glob(pattern) if Path(f).suffix == '.ipynb'])
        else:
            print(f"Warning: File not found: {pattern}", file=sys.stderr)
    
    if not notebook_files:
        print("Error: No notebook files found", file=sys.stderr)
        sys.exit(1)
    
    # Validate each notebook
    all_valid = True
    total_errors = 0
    
    for notebook_path in notebook_files:
        if args.verbose:
            print(f"\nValidating: {notebook_path}")
            print("=" * 60)
        
        # Structure validation
        if not args.skip_structure_check:
            struct_valid, struct_errors = validate_notebook_structure(notebook_path)
            if not struct_valid:
                all_valid = False
                total_errors += len(struct_errors)
                print(f"\n✗ {notebook_path}: Structure validation failed")
                for error in struct_errors:
                    print(f"  - {error}")
                continue
        
        # Source format validation
        format_valid, format_errors = validate_notebook_source_format(notebook_path)
        
        if format_valid:
            if args.verbose:
                print(f"✓ {notebook_path}: Format is valid")
        else:
            all_valid = False
            total_errors += len(format_errors)
            print(f"\n✗ {notebook_path}: Format validation failed ({len(format_errors)} error(s))")
            for error in format_errors:
                print(f"  - {error}")
    
    # Summary
    print("\n" + "=" * 60)
    if all_valid:
        print(f"✓ All {len(notebook_files)} notebook(s) passed validation")
        sys.exit(0)
    else:
        print(f"✗ Validation failed: {total_errors} error(s) found in {len(notebook_files)} notebook(s)")
        print("\nFix suggestions:")
        print("  1. Ensure each source array element ends with '\\n' if a newline is needed")
        print("  2. Use a notebook editor that properly formats source arrays")
        print("  3. Run: python3 -c \"import json; nb=json.load(open('notebook.ipynb')); ...\" to fix format")
        sys.exit(1)


if __name__ == '__main__':
    main()

