import pandas as pd
import numpy as np


hornet_data_upper_annular_train = pd.read_csv(r'hornet_data_upper_annular_train.csv')
data = np.array(hornet_data_upper_annular_train['open_current_states_kmean'])

annular_state = []
for i in range(0, len(data) - 1):
    lst = data[0+i:2+i]
    pattern = '_'.join(map(str, lst)) + str('_')
    if pattern == '0_2_':
        annular_state.append(1)
    else:
        annular_state.append(0)
    print(i)

annular_state = [0] + annular_state
hornet_data_upper_annular_train['annular_state'] = annular_state