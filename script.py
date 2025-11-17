import pandas as pd
import numpy as np

def make_valid_row():
    return {
        'id': np.random.randint(100000, 999999),
        'name': f'Name{np.random.randint(1, 100000)}',
        'age': np.random.randint(18, 90),
        'score': np.random.uniform(0, 100)
    }

# 1 million valid rows
valid_rows_1m = [make_valid_row() for _ in range(1000000)]
pd.DataFrame(valid_rows_1m).to_csv('million_rows_valid.csv', index=False)

# 50k valid rows
valid_rows_50k = [make_valid_row() for _ in range(50000)]
pd.DataFrame(valid_rows_50k).to_csv('50k_valid.csv', index=False)

# 50k with 20% errors
error_rows_50k = []
for i in range(50000):
    if np.random.rand() < 0.2:
        # introduce error: missing or wrong type
        error_rows_50k.append({
            'id': '', # missing
            'name': f'Name{np.random.randint(1, 100000)}',
            'age': 'invalid', # wrong type
            'score': np.random.uniform(0, 100)
        })
    else:
        error_rows_50k.append(make_valid_row())
pd.DataFrame(error_rows_50k).to_csv('50k_with_errors.csv', index=False)

# Header mismatch file
header_mismatch = pd.DataFrame([make_valid_row() for _ in range(10)])
header_mismatch.to_csv('header_mismatch.csv', index=False, header=['user_id','full_name','years','exam_score'])

# Show confirmation of file creation
output_files = [
    'million_rows_valid.csv',
    '50k_valid.csv',
    '50k_with_errors.csv',
    'header_mismatch.csv'
]
output_files
