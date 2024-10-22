state = [
    ['74', '65', '61', '6D'],
    ['6F', '52', '61', '66'],
    ['61', '79', '52', '6F'],
    ['62', '65', '73', '73']
]

def shift_rows(state):
    new_state = []
    for i in range(4):
        row = state[i]
        shift = i
        shifted_row = row[shift:] + row[:shift]
        new_state.append(shifted_row)
    return new_state

shifted_state = shift_rows(state)

print("Matriz Final después de ShiftRows:")
for row in shifted_state:
    print('   '.join(row))

'''
Matriz Final después de ShiftRows:
74   65   61   6D
52   61   66   6F
52   6F   61   79
73   62   65   73
'''
