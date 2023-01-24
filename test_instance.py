
import pytest
import pandas as pd



import input_read


def test_max_trip(sequence,school_node,max_trip):
    trip_counter=0
    for i in range(1,len(sequence)):
        if sequence[i] in school_node and sequence[i-1] not in school_node:
            trip_counter+=1
    if trip_counter>max_trip:
        return trip_counter
    return trip_counter


def test_school_visit(sequence,school_nodes):
    test_nodes=list()
    for i in range(len(sequence)):
        if sequence[i] in school_nodes:
            test_nodes.append(sequence[i])
    return len(test_nodes)==len(school_nodes)

def test_all_students_same_school():
    pass


def test_bus_capacity(sequence,capacity,school_nodes,min_capacity):
    trip_capacity=list()
    total_capacity=0
    trip=0
    passenger_percentage=list()
    for i in range(len(sequence)):
        if sequence[i] in school_nodes:
            trip+=1
            #passenger_percentage.append(total_capacity)
            if (total_capacity*100)/capacity < min_capacity: 
                #return '  minimum utilization not reached , {} percent  maximum capacity  reached on trip {}'.format((total_capacity*100)/capacity,trip)
                passenger_percentage.append(total_capacity)
            # else:
            #     total_capacity=0
        elif sequence[i] not in school_nodes:
            total_capacity+=1
    #return 'reached {}  capacity during all trips'.format((total_capacity*100)/capacity)
    return passenger_percentage
    
    
  
def test_bus_capacity_average(sequence,capacity,school_nodes):
    total_capacity=0
    trip_counter=0
    average=0
    buses_capacities=list()
    for i in range(len(sequence)):
        if sequence[i] not in school_nodes:
            total_capacity+=1
        elif sequence[i] in school_nodes and sequence[i-1] not in school_nodes:
            average+=total_capacity
            total_capacity=0
            trip_counter+=1
           
    return "average capacity of {} percent of  available places".format(trip_counter,(average/trip_counter)*(100/capacity))

def iterate_solution_sequences(instance_file,solution_file):
    file=list()
    solution_sequences,buses_capacitites,school_nodes,\
    max_trip,min_bus_utilization=input_read.main(instance_file,solution_file)
  
    #log_file = open("log2.txt", "w")
    #log_file.write("--input parameters-- \n-- minimum utilization {} -- \n".format(min_bus_utilization))
    # log_file.write("{} \n".format())
    # log_file.write("{} \n".format())
    # log_file.write("{} \n".format())
    # log_file.write("{} \n".format())
    solution_sequences.pop(0)
    # print(len([i+1 for i in range(len(solution_sequences))]))
    # print(len([buses_capacitites[solution_sequences.index(sequence)] for sequence in solution_sequences]))
    # print(len([test_max_trip(sequence,school_nodes,buses_capacitites[solution_sequences.index(sequence)]) for sequence in solution_sequences]))
    Buses={
         'Bus_ID':[i+1 for i in range(len(solution_sequences))],
         'Bus_Capacity':[buses_capacitites[solution_sequences.index(sequence)] for sequence in solution_sequences],
         'Trips_made':[test_max_trip(sequence,school_nodes,buses_capacitites[solution_sequences.index(sequence)]) for sequence in solution_sequences]
     }
    result=pd.DataFrame(Buses)
    result.to_csv("/Users/juinihamadi/Downloads/aziz/test-fedi/buses.csv")
    
    # for sequence in range(1,len(solution_sequences)):
    #     print(test_bus_capacity(solution_sequences,buses_capacitites,school_nodes,min_bus_utilization))
    #     log_file.write("---------- Bus No: {} ,capacity: {}----------\n".format(sequence,buses_capacitites[sequence-1]))
    #     log_file.write(str(test_bus_capacity_average(solution_sequences[sequence],buses_capacitites[sequence-1],school_nodes))+"\n")
    #     log_file.write(str(test_bus_capacity(solution_sequences[sequence],buses_capacitites[sequence-1],school_nodes,min_bus_utilization))+"\n" )
    #     log_file.write(str(test_max_trip(solution_sequences[sequence],school_nodes,max_trip))+"\n")
    # log_file.close()
    #print(Buses)
    




instance_file="lc101_instance2.txt"
soltion_file="lc101_instance2_S.txt"
iterate_solution_sequences(instance_file,soltion_file)