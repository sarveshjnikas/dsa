import pandas as pd

# .iloc[k] = position k, always.
# []/.loc[k] = label k -- after sort_values(), labels stick to their original values while row order changes, so s[k] can silently be wrong.
# reset_index(drop=True) realigns labels to positions -- but don't rely on it; default to .iloc.
# pd.DataFrame({'col': [x]}) -- value must be list-like; list len = #rows.

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salaries = employee['salary'].drop_duplicates().sort_values(ascending=False).reset_index(drop=True)
    return salaries[N-1]
