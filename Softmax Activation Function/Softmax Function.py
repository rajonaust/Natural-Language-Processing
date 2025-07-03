# Softmax Function
import numpy as np

vector = [5, 2, -1] #[10, 20, 5, 8, 7, 7, 6]

T = 1 # Here temperature = 1, means uniform distribution
exp_vector = [np.exp((1/T)*vector[i]) for i in range(len(vector))]
exp_sum = sum(exp_vector)

pro_vector = []
for i in range(len(vector)):
    pro_vector.append(round(exp_vector[i]/exp_sum, 6))

print(pro_vector)
