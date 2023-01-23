
import pytest


import input_read


def test_max_trip(sequence,school_node,max_trip):
    trip_counter=0
    for i in range(1,len(sequence)):
        if sequence[i] in school_node and sequence[i-1] not in school_node:
            trip_counter+=1
    if trip_counter!=max_trip:
        return "max trips surpassed, reached {}".format(trip_counter)
    return "max trips not surpassed, reached {}".format(trip_counter)


def test_school_visit(sequence,school_nodes):
    test_nodes=list()
    for i in range(len(sequence)):
        if sequence[i] in school_nodes:
            test_nodes.append(sequence[i])
    return len(test_nodes)==len(school_nodes)

def test_all_students_same_school():
    pass


def test_bus_capacity(bus_number,sequence,capacity,school_nodes):
    min_capacity=0.7
    total_capacity=0
    drop_off=0
    pick_up=0
    for i in range(len(sequence)):
        if sequence[i] in school_nodes:
            drop_off+=1
            if drop_off==pick_up!=0  :
                if total_capacity<=min_capacity:
                    return '{} percent capacity not reached on bus {}'.format(min_capacity*100,bus_number)
                total_capacity=0
                pick_up=0
                drop_off=0
        elif sequence[i] not in school_nodes:
            pick_up+=1
            total_capacity+=1/capacity 
    return 'reached 70 percent capacity during all trips'
  
def test_bus_capacity_average(bus_number,sequence,capacity,school_nodes):
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
        else:
            pick_up+=1
            total_capacity+=1
    return "total trips {} , average cpacity of {} percent".format(trip_counter,bus_number,average/trip_counter*100)

def iterate_solution_sequences(instance_file,solution_file):
    file=list()
    solution_sequences,buses_capacitites,school_nodes,max_trip=input_read.main(instance_file,solution_file)
    for sequence in range(1,len(solution_sequences)):
        print(test_bus_capacity_average(sequence,solution_sequences[sequence],buses_capacitites[sequence-1],school_nodes))
        print(test_bus_capacity(sequence,solution_sequences[sequence],buses_capacitites[sequence-1],school_nodes)) 
        print(test_max_trip(solution_sequences[sequence],school_nodes,max_trip))
        print("////////////////")
    




instance_file="lc101_instance1.txt"
soltion_file="lc101_instance_S.txt"
iterate_solution_sequences(instance_file,soltion_file)