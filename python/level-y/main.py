import statistics
import numpy as np
def compute_temperature_data(temps):
    
    average = statistics.mean(temps)
    median = statistics.median(temps)
    x = min(temps)
    y = max(temps)
    results = (median,average,x,y)
    return np.round(results, 1)