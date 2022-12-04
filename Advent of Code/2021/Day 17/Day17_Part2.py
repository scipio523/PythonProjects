#target = {'x':[117, 164], 'y':[-140, -89]}
target = {'x':[281, 311], 'y':[-74, -54]}
#target = {'x':[20, 30], 'y':[-10, -5]}
velocity_list = []
for x in range(target['x'][1]+1):
    for y in range(target['y'][0], target['y'][1]*-2, 1):
        velocity = {'x':x, 'y':y} # initial velocity
        new_velocity = velocity.copy()
        position = {'x':0, 'y':0} # initial position
        while True:
            if target['x'][0] <= position['x'] <= target['x'][1] and target['y'][0] <= position['y'] <= target['y'][1]: # reached target
                velocity_list.append((velocity['x'], velocity['y']))
                break 
            elif position['x'] > target['x'][1] or position['y'] < target['y'][0]: # missed target
                break 
            position['x'] += new_velocity['x']
            if new_velocity['x'] > 0:
                new_velocity['x'] -= 1
            position['y'] += new_velocity['y']
            new_velocity['y'] -= 1
print(len(velocity_list))