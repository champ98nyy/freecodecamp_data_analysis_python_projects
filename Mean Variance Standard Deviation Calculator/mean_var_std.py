import numpy as np

def calculate(list):
  # Check that input list contains 9 elements
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")

  # convert list into 2D numpy array
  np_array = np.array(list).reshape(3,3)

  # Calculate means of each column, row and the flattened array
  mean_cols, mean_rows, mean_flat = np.mean(np_array, axis=0).tolist(), np.mean(np_array, axis=1).tolist(), np.mean(np_array)

  # Calculate variance of each column, row and the flattened array
  var_cols, var_rows, var_flat = np.nanvar(np_array, axis=0).tolist(), np.nanvar(np_array, axis=1).tolist(), np.nanvar(np_array)

  # Calculate standard deviation of each column, row and the flattened array
  std_cols, std_rows, std_flat = np.std(np_array, axis=0).tolist(), np.std(np_array, axis=1).tolist(), np.std(np_array)

  # Calculate the max of each column, row and the flattened array
  max_cols, max_rows, max_flat = np.max(np_array, axis=0).tolist(), np.max(np_array, axis=1).tolist(), np.max(np_array)

  # Calculate the min of each column, row and the flattened array
  min_cols, min_rows, min_flat = np.min(np_array, axis=0).tolist(), np.min(np_array, axis=1).tolist(), np.min(np_array)

  # Calculate the sum of each column, row and the flattened array
  sum_cols, sum_rows, sum_flat = np.sum(np_array, axis=0).tolist(), np.sum(np_array, axis=1).tolist(), np.sum(np_array)

  # Dictionary for all calculations
  calculations = {
    'mean': [mean_cols, mean_rows, mean_flat],
    'variance': [var_cols, var_rows, var_flat],
    'standard deviation': [std_cols, std_rows, std_flat],
    'max': [max_cols, max_rows, max_flat],
    'min': [min_cols, min_rows, min_flat],
    'sum': [sum_cols, sum_rows, sum_flat]
  }

  return calculations