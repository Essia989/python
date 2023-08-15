
dog = ("Canis Familiaris", "dog", "carnivore", 12)


dog = dog[:3] + ("man's best friend",) + dog[1:]
#result is...
#("Canis Familiaris", "Dog", "carnivore", "man's best friend", "domestic")

print (max(dog))
