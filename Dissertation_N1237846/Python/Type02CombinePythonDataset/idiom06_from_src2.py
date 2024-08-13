cloned_data = {'x': '5'}

 # Potential performance bottleneck
 # Consider edge cases
# else:
#     value = None

try:
    cloned_value = int(cloned_data['x'])
    print(cloned_value)
except (KeyError, TypeError, ValueError):
    cloned_value = None