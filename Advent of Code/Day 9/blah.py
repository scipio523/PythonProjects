def fillBasin(rowIndex, colIndex):
    target = heatMap[rowIndex][colIndex]
    if target == 9:
        return
    heatMap[rowIndex][colIndex] = 9
    basin.append(target)
    if rowIndex > 0:
        fillBasin(rowIndex-1, colIndex)
    if rowIndex < len(heatMap) - 1:
        fillBasin(rowIndex+1, colIndex)
    if colIndex > 0:
        fillBasin(rowIndex, colIndex-1)
    if colIndex < len(heatMap[rowIndex]) - 1:
        fillBasin(rowIndex, colIndex+1)
    return

with open("Advent of Code/Day 9/Input.txt") as f:
    data = f.read()
data = data[:-1]

data = data.split('\n')
heatMap = [[int(char) for char in row] for row in data]
basins = []
basin = []
for rowIndex in range(len(heatMap)):
    for colIndex in range(len(heatMap[rowIndex])):
        fillBasin(rowIndex,colIndex)
        if basin:
            basins.append(basin)
            basin = []
print(basins)
basinSizes = [len(basin) for basin in basins]
basinSizes.sort()
largestBasins = basinSizes[-3:]
finalProduct = 1
for basin in largestBasins:
    finalProduct *= basin
print(finalProduct)