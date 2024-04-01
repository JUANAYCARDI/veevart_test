from sys import stdin
import heapq

#Greedy approach using dijkstra algorithm 
def elevator(startFloor, dictFloors, floors):
    newDictFloors = dict(dictFloors)
    q = []
    ans = []
    #Initialize priority queue with initial states
    for floor in floors:
        newFloorsLeft = set(floors)
        nextFloor = floor
        if floor in newFloorsLeft:
            newFloorsLeft.remove(floor)
            state = [0 + abs(startFloor - nextFloor), len(newFloorsLeft), nextFloor, newFloorsLeft, [startFloor], dict(newDictFloors)]
            heapq.heappush(q, state)
    
    while len(ans) == 0 and len(q): 
        #Current state, taken as the state with the least time used for the elevator movements
        #Time is considered as the difference between a floor the elevator is located and the floor the elevator will go
        time, left, currentFloor, floorsLeft, path, dictFloors = heapq.heappop(q)
        newPath = list(path)
        newPath.append(currentFloor)
        if len(floorsLeft) == 0:
            ans = newPath
        else:     
            if currentFloor in dictFloors:
                floorsLeft.add(dictFloors[currentFloor])
                dictFloors.pop(currentFloor)
            for floor in floorsLeft:         
                newFloorsLeft = set(floorsLeft)
                newDictFloors = dict(dictFloors)
                nextFloor = floor
                if nextFloor in newDictFloors:
                    newFloorsLeft.add(newDictFloors[nextFloor])
                    newDictFloors.pop(nextFloor)
                
                newFloorsLeft.remove(nextFloor)
                #Adding to the queue the new possible next states given the current floor and the floors that have not been visited yet
                state = [time + abs(currentFloor - nextFloor), len(newFloorsLeft), nextFloor, newFloorsLeft, newPath, newDictFloors]
                heapq.heappush(q, state)
    return ans

def main():
    floors = list(map(int, stdin.readline().split()))
    startFloor = int(stdin.readline())
    dictFloors = {}
    n = len(floors)

    for i in range(n):
        key, value = map(int, stdin.readline().split())
        dictFloors[key] = value
    ans = elevator(startFloor, dictFloors, floors)
    previous = -1
    print("Floors: ", floors)
    print()
    for floor in ans:
        if previous == -1:
            previous = floor
            print("Elevator in floor ", floor)
            print("Elevator stops")
            if floor in dictFloors:
                print("Added floor ", dictFloors[floor])
        else:
            if previous < floor:
                print("Elevator going up")
                print("Elevator in floor ", floor)
                print("Elevator stops")
                if floor in dictFloors:
                    print("Added floor ", dictFloors[floor])
            else:
                print("Elevator going down")
                print("Elevator in floor ", floor)
                print("Elevator stops")
                if floor in dictFloors:
                    print("Added floor ", dictFloors[floor])

main()