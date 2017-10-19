from sklearn import tree

# Display the fruit based on index


def displayFruitType(x):
    if x is 0:
        print("Apple!")
    else:
        print("Orange!")


# 1 for smooth and 0 for bumpy
# Other is the weight
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
# 0 for apple and 1 for Orange
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()  # Empty box of rules
clf = clf.fit(features, labels)
a = clf.predict([[150, 0]])  # 150 gms and bumpy
displayFruitType(a)
