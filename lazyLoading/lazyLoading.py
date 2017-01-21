#!/usr/bin/env python
import math
def main():
    fo = open("lazy_loading.txt", "r")
    data = fo.read()
    lines = data.splitlines()
    lines = [int(x) for x in lines]
    result = []
    dayData = []
    itemIndex = 0
    currentDayItemsCount = 0

    for i in range(int(lines[0])):
        currentDayItems = lines[itemIndex+currentDayItemsCount+1]
        itemIndex = itemIndex + currentDayItemsCount + 1
        day = i+1
        items = []
        for j in range(currentDayItems):
            items.append(lines[itemIndex+j+1])

        sortedItems = sorted(items,reverse=True)
        tripCount = 0
        itemsTaken = []
        for idx, val in enumerate(sortedItems):
            #process the logic for each day max trips
            itemsTaken.append(idx)
            if val >= 50:
                tripCount += 1
            else:
                currentTripTopWt = val #top weight
                currentTripWt = val #initialize

                for idz, otherVal in enumerate(sortedItems):
                    revIdz = len(sortedItems) - (idz + 1)
                    if revIdz not in itemsTaken:
                        currentTripWt += currentTripTopWt
                        itemsTaken.append(revIdz)
                        if (currentTripWt >= 50):
                            tripCount += 1
                            break
        result.append('Case #'+str(day)+': '+ str(tripCount))

        currentDayItemsCount = currentDayItems

    text_file = open("Output.txt", "w")
    text_file.write('\n'.join(result))
    text_file.close()

    fo.close()
    print('done!')

main()