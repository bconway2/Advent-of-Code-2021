import pandas as pd

def get_input(inputfile):
    puzinput = []
    with open(inputfile) as file:
        for line in file:
            puzinput.append(line.strip())
    return puzinput


def part_one(data):
    reshape_data = [list(i) for i in data]
    data_df = pd.DataFrame(reshape_data)
    data_mode = ''.join(data_df.mode().values.tolist()[0])
    data_least = ''
    for i in data_mode:
        if i =='1': 
            data_least += '0'
        else: 
            data_least += '1'
    return int(data_least,2) * int(data_mode,2)

def part_two(data):
    reshape_data = [list(i) for i in data]
    data_df = pd.DataFrame(reshape_data)
    CO2_scrubber = data_df
    O2_scrubber = data_df
    for col in data_df:
        nmost_common_CO2 = CO2_scrubber[col].value_counts().max()
        nleast_common_CO2 = CO2_scrubber[col].value_counts().min()
        nmost_common_O2 = O2_scrubber[col].value_counts().max()
        nleast_common_O2 = O2_scrubber[col].value_counts().min()
        if CO2_scrubber.shape[0] > 1:
            if nmost_common_CO2 == nleast_common_CO2:
                CO2_scrubber = CO2_scrubber[CO2_scrubber[col] == '0']
                #delete 1s
            else:
                least_common_CO2 = CO2_scrubber[col].value_counts().idxmin()
                CO2_scrubber = CO2_scrubber[CO2_scrubber[col] == least_common_CO2]
        
        if O2_scrubber.shape[0] > 1:
            if nmost_common_O2 == nleast_common_O2:
                #delete 0s
                O2_scrubber = O2_scrubber[O2_scrubber[col] == '1']
            else:
                most_common_O2 = O2_scrubber[col].value_counts().idxmax()
                O2_scrubber = O2_scrubber[O2_scrubber[col] == most_common_O2]
    CO2_rating = int(''.join(CO2_scrubber.values.tolist()[0]),2)
    O2_rating = int(''.join(O2_scrubber.values.tolist()[0]),2)
    return CO2_rating * O2_rating
   

d = get_input('input3.txt')
print(part_one(d))
print(part_two(d))