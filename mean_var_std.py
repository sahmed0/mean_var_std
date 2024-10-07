# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:57:25 2024

@author: ahmed
"""

import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert the input list to a 3x3 numpy array
    matrix = np.array(list).reshape(3, 3)
    
    # Create the dictionary following the required format
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),  # Mean of columns
            matrix.mean(axis=1).tolist(),  # Mean of rows
            matrix.mean().tolist()         # Mean of entire matrix (flattened)
        ],
        'variance': [
            matrix.var(axis=0).tolist(),   # Variance of columns
            matrix.var(axis=1).tolist(),   # Variance of rows
            matrix.var().tolist()          # Variance of entire matrix (flattened)
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),   # Standard deviation of columns
            matrix.std(axis=1).tolist(),   # Standard deviation of rows
            matrix.std().tolist()          # Standard deviation of entire matrix (flattened)
        ],
        'max': [
            matrix.max(axis=0).tolist(),   # Max of columns
            matrix.max(axis=1).tolist(),   # Max of rows
            matrix.max().tolist()          # Max of entire matrix (flattened)
        ],
        'min': [
            matrix.min(axis=0).tolist(),   # Min of columns
            matrix.min(axis=1).tolist(),   # Min of rows
            matrix.min().tolist()          # Min of entire matrix (flattened)
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),   # Sum of columns
            matrix.sum(axis=1).tolist(),   # Sum of rows
            matrix.sum().tolist()          # Sum of entire matrix (flattened)
        ]
    }
    
    return calculations
