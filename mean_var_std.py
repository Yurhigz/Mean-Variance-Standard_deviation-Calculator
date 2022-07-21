import numpy as np


def calculate(list):

  calculations = {'mean':[],'variance':[],'standard deviation':[],'max':[],'min': [],'sum':[]}
  dict_argument = {'mean':np.mean,'variance':np.var,'standard deviation': np.std,'max':np.max,'min':np.min,'sum':np.sum}
  list_axis = (0,1,None)
  if len(list) != 9 :
    raise ValueError('List must contain nine numbers.')
  else :
    array_list = np.array([list[:3],list[3:6],list[6:]])
    for i in dict_argument:
        for element in list_axis :
          calculations[i].append(dict_argument[i](array_list, axis=element).tolist())
    return calculations