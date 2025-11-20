
# #ko can chay cai nay



# #!/usr/bin/env python3
# """
# Quick Start Script - Delivery Route Optimization
# Run this to validate the setup and execute the optimization notebook
# """

# import os
# import sys
# import subprocess
# from pathlib import Path

# def check_dependencies():
#     """Check if all required packages are installed"""
#     required_packages = {
#         'pyspark': 'PySpark',
#         'pandas': 'Pandas',
#         'numpy': 'NumPy',
#         'sklearn': 'Scikit-learn',
#         'ortools': 'Google OR-Tools',
#         'statsmodels': 'Statsmodels',
#         'matplotlib': 'Matplotlib'
#     }
    
#     missing = []
#     for package, name in required_packages.items():
#         try:
#             __import__(package)
#             print(f"✓ {name} installed")
#         except ImportError:
#             print(f"✗ {name} NOT installed")
#             missing.append(package)
    
#     if missing:
#         print(f"\nInstalling missing packages: {', '.join(missing)}")
#         subprocess.run([sys.executable, '-m', 'pip', 'install'] + missing, check=True)
    
#     return len(missing) == 0

# def check_data_files():
#     """Verify all required data files exist"""
#     base_path = Path('/home/sirin/BIGDATA')
    
#     required_paths = [
#         'Datapack/Delivery/delivery_cq.csv',
#         'Datapack/Delivery/delivery_hz.csv',
#         'Datapack/Delivery/delivery_jl.csv',
#         'Datapack/Delivery/delivery_sh.csv',
#         'Datapack/Delivery/delivery_yt.csv',
#         'Datapack/PickUp/pickup_cq.csv',
#         'Datapack/PickUp/pickup_hz.csv',
#         'Datapack/PickUp/pickup_jl.csv',
#         'Datapack/PickUp/pickup_sh.csv',
#         'Datapack/PickUp/pickup_yt.csv',
#         'Datapack/Roadmap/roads.csv',
#     ]
    
#     print("\nChecking data files:")
#     all_exist = True
#     for path in required_paths:
#         full_path = base_path / path
#         if full_path.exists():
#             size = full_path.stat().st_size / 1024 / 1024  # MB
#             print(f"✓ {path} ({size:.2f} MB)")
#         else:
#             print(f"✗ {path} NOT FOUND")
#             all_exist = False
    
#     return all_exist

# def check_output_directories():
#     """Create output and model directories if they don't exist"""
#     base_path = Path('/home/sirin/BIGDATA')
    
#     directories = [
#         'TrainedModel',
#         'TrainedModel/eta_model',
#         'TrainedModel/route_model',
#         'TrainedModel/stg_model',
#         'output',
#     ]
    
#     print("\nChecking directories:")
#     for directory in directories:
#         dir_path = base_path / directory
#         dir_path.mkdir(parents=True, exist_ok=True)
#         print(f"✓ {directory} ready")

# def print_notebook_info():
#     """Print notebook information"""
#     notebook_path = Path('/home/sirin/BIGDATA/Optimize-Delivery-Routes.ipynb')
    
#     if notebook_path.exists():
#         size = notebook_path.stat().st_size / 1024  # KB
#         print(f"\n✓ Notebook exists: {notebook_path}")
#         print(f"  Size: {size:.2f} KB")
#         print(f"  Cells: 13 sections")
#     else:
#         print(f"\n✗ Notebook not found!")
#         return False
    
#     return True

# def main():
#     """Main execution"""
#     print("="*60)
#     print("DELIVERY ROUTE OPTIMIZATION - SETUP VERIFICATION")
#     print("="*60)
    
#     # Check dependencies
#     print("\n1. Checking Python dependencies...")
#     deps_ok = check_dependencies()
    
#     # Check data files
#     print("\n2. Checking data files...")
#     data_ok = check_data_files()
    
#     # Check directories
#     print("\n3. Checking output directories...")
#     check_output_directories()
    
#     # Check notebook
#     print("\n4. Checking notebook...")
#     notebook_ok = print_notebook_info()
    
#     # Final status
#     print("\n" + "="*60)
#     if deps_ok and data_ok and notebook_ok:
#         print("ALL CHECKS PASSED - Ready to run!")
#         print("\nTo run the notebook:")
#         print("  jupyter notebook /home/sirin/BIGDATA/Optimize-Delivery-Routes.ipynb")
#         print("\nOr convert to Python script:")
#         print("  jupyter nbconvert --to script Optimize-Delivery-Routes.ipynb --output optimization.py")
#         print("  python optimization.py")
#     else:
#         print("Some checks failed - Please resolve issues above")
#         sys.exit(1)
    
#     print("="*60)

# if __name__ == "__main__":
#     main()
