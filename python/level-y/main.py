import statistics
import numpy as np
def compute_temperature_data(temperature_data):
    
    average = statistics.mean(temperature_data)
    median = statistics.median(temperature_data)
    x = min(temperature_data)
    y = max(temperature_data)
    results = (median,average,x,y)
    return np.round(results, 1)