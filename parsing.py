import pandas as pd
import re
import sys

filename = sys.argv[1]
output_filename = sys.argv[2]
df = pd.read_csv(filename, on_bad_lines='skip')

def transfrom_metrices(name, unit, added_metrices, pre_string):
    name = name.replace(' ', '_')
    if unit == 'Avg':
        name+='_avg'
    elif unit == 'Min':
        name += '_min'
    elif unit == 'Max':
        name += '_max'
    elif unit == 'Mean':
        name += '_mean'
    elif unit == 'Std Dev':
        name += '_std'

    
    name = pre_string + '_' + name
    return name

new_df = pd.DataFrame(columns=['Metrics', 'Value'])
default_names = ['Value','Avg','Min','Max','Mean','Std Dev']
default_values = [-1,-1,-1,-1,-1,-1]
pre_string = ''
metrics_units = dict()
for val in df.iloc[:,0]:
    is_section = re.search('^\s*([\d.]+)\s*([^|]+)',str(val))
    if is_section:
        val = re.sub('^\d+\.\d*', '', val)
        section_names = re.sub(' +', ' ', val.replace('-',' ')).strip().split(' ')
        # pre_string = ''.join(x[0] if x[0]!='(' else x[1] for x in section_names)
        for word in ['L2','L1','L1D']:
            if word in section_names:
                pos = section_names.index(word)
                section_names[pos:len(word)-1] = [x for x in word]
        if len(section_names)==1:
            is_sol_pre_string = section_names[0]
        else:
            is_sol_pre_string = ''.join(x[0] if x[0]!='(' else x[1] for x in section_names)
        if is_sol_pre_string=='SoL':
            pre_string+=is_sol_pre_string
        else:
            pre_string=is_sol_pre_string

        # print(pre_string) 
    # print(val)
        continue

    has_units = re.search('^\│\s*([^\d.]+)\s*│\s*([^\d.]+)\s*│\s*([^│]+)',str(val))
    if has_units:
        metrics_units = dict(zip(default_names,default_values))
        # print(val)
        units = [x.strip() for x in str(val).split('│')]
        # print(units)
        # print(metrics_units.keys())
        for unit in metrics_units.keys():
            # print(units)
            if unit in units:
                metrics_units[unit] = units.index(unit)
        continue
    
    x = re.search('^\│\s*([\d.]+)\s*│\s*([^│]+)\s*│',str(val))
    if x:
        # print(val)
        vals = [x.strip() for x in str(val).split('│')]
        for unit in metrics_units.keys():
            if metrics_units[unit] != -1 :
                # if vals[metrics_units[unit]] == '':
                #     print('Yes')
                # else:
                #     print('No')
                new_df.loc[len(new_df.index)] = [transfrom_metrices(vals[2],unit,new_df['Metrics'], pre_string),0.0 if vals[metrics_units[unit]]=='' else vals[metrics_units[unit]]]
# print(new_df.head())
print(new_df.head())
new_df.to_csv(output_filename)