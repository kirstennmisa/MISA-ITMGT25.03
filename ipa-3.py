#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Relationship Status

social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}

def relationship_status(from_member, to_member, social_graph):
    
    from_following = social_graph.get(from_member, {}).get("following", [])
    to_following = social_graph.get(to_member, {}).get("following", [])

    if to_member in from_following and from_member in to_following:
        return "Friends"
    elif to_member in from_following:
        return "follower"
    elif from_member in to_following:
        return "followed by"
    else:
        return "no relationship"


# In[2]:


# Tic Tac Toe

board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]

def tic_tac_toe(board):

    for row in board:
        if all(cell == row[0] and cell for cell in row):
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        if all(board[row][col] == board[0][col] and board[row][col] for row in range(len(board))):
            return board[0][col]

    # Check diagonal (top-left to bottom-right)
    if all(board[i][i] == board[0][0] and board[i][i] for i in range(len(board))):
        return board[0][0]

    # Check diagonal (top-right to bottom-left)
    if all(board[i][len(board)-1-i] == board[0][len(board)-1] and board[i][len(board)-1-i] for i in range(len(board))):
        return board[0][len(board)-1]

    return "No Winner"


# In[3]:


# ETA

legs1 = {
     ("upd","admu"): {
         "travel_time_mins": 10
     },
     ("admu","dlsu"): {
         "travel_time_mins": 35
     },
     ("dlsu","upd"): {
         "travel_time_mins": 55
     }
}

legs2 = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
    }
}

def eta(first_stop, second_stop, route_map):
    # Checks stops in route map
    if first_stop in route_map or second_stop in route_map:
        return "Invalid stops."

    # Checks connection between stops
    if (first_stop, second_stop) in route_map:
        return route_map[(first_stop, second_stop)]['travel_time_mins']

    for stop in route_map:
        if stop[0] == first_stop and stop[1] != second_stop:
            intermediate_stop = stop[1]
            if (intermediate_stop, second_stop) in route_map:
                travel_time = route_map[(first_stop, intermediate_stop)]['travel_time_mins'] + \
                              route_map[(intermediate_stop, second_stop)]['travel_time_mins']
                return travel_time

    return "No valid route found."

