def life(reality, word):
    reality_copy = reality.copy()
    for item in reality_copy:
        if item == word:
            reality.remove(item)
    return reality

reality = ["Me", "Toxisity", "MY Life"]
print(life(reality, "Toxisity"))