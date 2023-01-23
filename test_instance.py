
import pytest


#import input_read


def test_max_trip_done(sequence,school_node,max_trip):
    trip_counter=0
    for i in range(1,len(sequence)):
        if sequence[i] in school_node and sequence[i-1] not in school_node:
            trip_counter+=1
    return trip_counter==max_trip

def test_school_visit(sequence,school_nodes):
    test_nodes=list()
    for i in range(len(sequence)):
        if sequence[i] in school_nodes:
            test_nodes.append(sequence[i])
    return len(test_nodes)==len(school_nodes)

def test_all_students_same_school():
    pass


def test_bus_capacity(sequence,capacity,school_nodes):
    min_capacity=0.7
    total_capacity=0
    drop_off=0
    pick_up=0
    for i in range(len(sequence)):
        if sequence[i] in school_nodes:
            drop_off+=1
            if drop_off==pick_up!=0  :
                if total_capacity<=min_capacity:
                    return '{} percent capacity not reached on bus '.format(min_capacity*100)
                total_capacity=0
                pick_up=0
                drop_off=0
        elif sequence[i] not in school_nodes:
            pick_up+=1
            total_capacity+=1/capacity 
  
def test_bus_capacity_average(sequence,capacity,school_nodes):
    total_capacity=0
    drop_off=0
    pick_up=0
    trip_counter=0
    average=0
    buses_capacities=list()
    for i in range(len(sequence)):
        if sequence[i] in school_nodes:
            drop_off+=1
            if drop_off==pick_up!=0  :
                average+=total_capacity/capacity
                total_capacity=0
                trip_counter+=1
                pick_up=0
                drop_off=0
        elif sequence[i] not in school_nodes:
            pick_up+=1
            total_capacity+=1
    return average/trip_counter


print(test_bus_capacity([3, 8, 1, 2, 6, 7],2,[ 8,  6, 7]))
print(test_bus_capacity_average([3, 8, 1, 2, 6, 7],2,[ 8,  6, 7]))