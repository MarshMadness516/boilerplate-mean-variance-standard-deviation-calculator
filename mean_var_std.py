import numpy as np


def calculate(list):
    # initialize calculations dict
    calculations = {}
    
    # convert list argument into matrix with numpy
    list_matrix = np.array([list[:3], list[3:6], list[6:]])
    
    # calculate values along both axes and for the entire matrix
    mean = [
      np.mean(list_matrix, axis=0),
      np.mean(list_matrix, axis=1),
      np.mean(list_matrix)
      ]
    var = [np.var(list_matrix, axis=0), np.var(list_matrix, axis=1), np.var(list_matrix)]
    std = [np.std(list_matrix, axis=0), np.std(list_matrix, axis=1), np.std(list_matrix)]
    max = [np.max(list_matrix, axis=0), np.max(list_matrix, axis=1), np.max(list_matrix)]
    min = [np.min(list_matrix, axis=0), np.min(list_matrix, axis=1), np.min(list_matrix)]
    sum = [np.sum(list_matrix, axis=0), np.sum(list_matrix, axis=1), np.sum(list_matrix)]
    
    # add data to calculations dict
    calculations['mean'] = [arr.tolist() for arr in mean]
    calculations['var'] = [arr.tolist() for arr in var]
    calculations['std'] = [arr.tolist() for arr in std]
    calculations['max'] = [arr.tolist() for arr in max]
    calculations['min'] = [arr.tolist() for arr in min]
    calculations['sum'] = [arr.tolist() for arr in sum]
    
    
    return calculations
