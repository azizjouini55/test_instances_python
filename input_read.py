# The input files follow the "Li & Lim" format
import sys
def read_elem(filename):
    with open(filename) as f:
        return [str(elem) for elem in f.read().split()]
def read_input_pdptw(filename):
    file_it = iter(read_elem(filename))
    nb_nodes = 0
    while True:
        token = next(file_it)
        if token == "DIMENSION":
            next(file_it)  # Removes the ":"
            nb_nodes = int(next(file_it))
            nb_students = nb_nodes - 1
        elif token == "SERVICE_TIME":
            next(file_it)  # Removes the ":"
            service_time = float(next(file_it))
        elif token == "MAX_TRIP_PER_BUS":
            next(file_it)  # Removes the ":"
            max_trips_per_bus = int(next(file_it))
        elif token == "MAX_SCHOOLS_PER_BUS":
            next(file_it)  # Removes the ":"
            max_schools_per_bus = int(next(file_it))
        elif token == "NUMBER_OF_BUSES":
            next(file_it)  # Removes the ":"
            nb_trucks = int(next(file_it))
        elif token == "SPEED":
            next(file_it)  # Removes the ":"
            speed = int(next(file_it))
        elif token == "NUMBER_OF_SCHOOLS":
            next(file_it)  # Removes the ":"
            nb_schools = int(next(file_it))
        elif token == "BUS_CAPACITIES":
            break
    
    # adding bus capacitites
    truck_capacitites = []
    for truck_index in range(nb_trucks):
        next(file_it)
        truck_capacitites.append(int(next(file_it)))
    
    next(file_it)
    
    # adding school indexes
    school_indexes = []
    for school_index in range(nb_schools):
        next(file_it)
        school_indexes.append(int(next(file_it)))
    
    next(file_it)
    
    # adding school node coordinates
    school_nodes = []
    for school_index in range(nb_schools):
        school_index = int(next(file_it))
        same_school_indexes = []
        for index in range(school_indexes[school_index - 1]):
            same_school_indexes.append(int(next(file_it)))
        school_nodes.append(same_school_indexes)
        
    next(file_it)
    next(file_it)

    depot_x = float(next(file_it))
    depot_y = float(next(file_it))

    for i in range(2):
        next(file_it)

    max_horizon = int(next(file_it))

    customers_x = []
    customers_y = []
    demands = []
    earliest_start = []
    latest_end = []
    service_time_matrix = [service_time] * nb_students
    pick_up_index = []
    delivery_index = []

    while True:
        val = next(file_it, None)
        if val is None:
            break
        i = int(val) - 1
        customers_x.append(float(next(file_it)))
        customers_y.append(float(next(file_it)))
        demands.append(int(next(file_it)))
        ready = int(next(file_it))
        due = int(next(file_it))
        pick = int(next(file_it))
        delivery = int(next(file_it))
        earliest_start.append(ready)
        # in input files due date is meant as latest start time
        latest_end.append(due + service_time)
        pick_up_index.append(pick - 1)
        delivery_index.append(delivery - 1)
    
    
    return nb_students, nb_trucks, truck_capacitites, \
            demands, service_time_matrix, earliest_start, latest_end, pick_up_index, \
            delivery_index, max_horizon,school_nodes, max_trips_per_bus, max_schools_per_bus


def read_file_output(filename):
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    file1.close()
    sequences=list()
    for line in Lines:
        str_sequence=line.strip().split(' ')
        sequences.append( list(map(int, str_sequence)))
    return sequences

def main(solution_file):
    
    #Read instance data
    # nb_students, nb_trucks, truck_capacity, \
    # demands_data, service_time_data, earliest_start_data, latest_end_data, \
    # pick_up_index, delivery_index, max_horizo ,\
    # school_nodes, max_trips_per_bus, max_schools_per_bus = read_input_pdptw(instance_file)
    solution_sequences=read_file_output(solution_file)
    # print("nb of students :"+str(nb_students))
    # print("max trips :"+str( max_trips_per_bus))
    # print("school nodes :"+str( school_nodes))
    # print("pick up index :"+str( pick_up_index))
    # print("delivery index :"+str( delivery_index))
    # print("truck capcity :"+str( truck_capacity))
    # print("nb trucks :"+str( nb_trucks))
    print(solution_sequences)
    
   
if __name__ == "__main__" :

    instance_file = "lc101_instance1.txt"
    soltion_file="Lc101_solution.txt"
main(soltion_file)

  
   