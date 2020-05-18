# first process the inputs
# convert the inputs to integers

def process_inputs(cal1, cal2):

    processed_cal2 = []
    processed_cal1 = []

    for i in range(len(cal1)):
        time_slots = [int(cal1[i][0]),int(cal1[i][1])]
        processed_cal2.append(time_slots)
        # to optimize for space complexity maybe try:
        #cal1_availableSlots = [int(cal1[i][1]), int(cal1[i])]

    for i in range(len(cal2)):
        time_slots = [int(cal2[i][0]),int(cal2[i][1])]
        processed_cal2.append(time_slots)

    return processed_cal1, processed_cal2

def get_available_slots(l,s):
    cal1, cal2 = process_inputs(l,s)

    cla1_available_slots = []
    cal2_available_slots = []
    for i in range(1, len(cal1)):
        available_slots = [cal1[i][0], cal1[i-1][1]]
        cla1_available_slots.append(available_slots)

    for i in range(1, len(cal2)):
        available_slots = [cal2[i][0], cal2[i-1][1]]
        cal2_available_slots.append(available_slots)

    

    return cla1_available_slots, cal2_available_slots

def merge_slots(slot1, slot2):
    cal1, cal2 = get_available_slots(slot1,slot2)
    shortest_list = min(len(cal1), len(cal2))

    for i in range(0, shortest_list):
        bvbvb



