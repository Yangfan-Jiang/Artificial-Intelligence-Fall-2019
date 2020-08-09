import numpy as np
import random

# initialize R table and Q table
R = np.array([[-1, -1, -1, -1,  0, -1  ],
              [-1, -1, -1,  0, -1,  100],
              [-1, -1, -1,  0, -1, -1  ],
              [-1,  0,  0, -1,  0, -1  ],
              [ 0, -1, -1,  0, -1,  100],
              [-1,  0, -1, -1,  0,  100]])
               
Q = np.zeros((6, 6))

alpha = 0.8
max_iteration = 35
goal_state = 5

def valid_action(R, state):
    action_list = []
    for action in range(6):
        if R[state][action] != -1:
            action_list.append(action)
    return action_list

def max_Q(R, state):
    curr_Q = -1
    for action in valid_action(R, state):
        if Q[state][action] > curr_Q:
            curr_Q = Q[state][action]
    return curr_Q

for episode in range(max_iteration):
    state = random.randint(0, 5)
    while state != goal_state:
        next_state = random.sample(valid_action(R, state), 1)[0]
        Q[state][next_state] = R[state][next_state] + alpha * max_Q(R, next_state)
        state = next_state 
        
print('------ Q table -------')
print(Q)
# generate path
init_state = 2
curr_state = init_state
path = [init_state]

while curr_state != goal_state:
    curr_state = np.argmax(Q[curr_state])
    path.append(curr_state)
print('\n------ path -------')
print(path)