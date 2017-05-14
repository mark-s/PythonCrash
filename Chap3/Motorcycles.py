motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# change first item
motorcycles[0] = 'ducati'
print(motorcycles)


# add one
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# insert
motorcycles.insert(0, 'ducati')
print(motorcycles)


# remove
del motorcycles[0]
print(motorcycles)

# pop
print("pop")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)


# remove
motorcycles = ['honda', 'yamaha', 'suzuki']
too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)

