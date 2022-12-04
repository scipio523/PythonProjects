#target = {'x':[117, 164], 'y':[-140, -89]}
target = {'x':[281, 311], 'y':[-74, -54]}
#target = {'x':[20, 30], 'y':[-10, -5]}
result = (1, 1)
for x in range(target['x'][1]+1):
    for y in range(target['y'][0]*-2):
        velocity = {'x':x, 'y':y} # initial velocity
        new_velocity = velocity.copy()
        position = {'x':0, 'y':0} # initial position
        this_max_y = 0
        while True:
            if target['x'][0] <= position['x'] <= target['x'][1] and target['y'][0] <= position['y'] <= target['y'][1]: # reached target
                if velocity['y'] > result[1]:
                    result = (velocity['x'], velocity['y'])
                    max_y = this_max_y
                break 
            elif position['x'] > target['x'][1] or position['y'] < target['y'][0]: # missed target
                break 
            position['x'] += new_velocity['x']
            if new_velocity['x'] > 0:
                new_velocity['x'] -= 1
            position['y'] += new_velocity['y']
            new_velocity['y'] -= 1
            this_max_y = max(this_max_y, position['y'])
print(result, max_y)