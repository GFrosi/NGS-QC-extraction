import logging
import json

logger = logging.getLogger(__name__)

# def read_config(file_name):

#     '''This function receives a config file and it will return a 
#     dictionary with all information from the config file. The config file
#     should have all specified information from the template.'''

#     config = {}

#     with open(file_name,'r') as file:
        
#         try:
        
#             for line in file:
                    
#                 k,v = line.strip().split('=')
#                 v = v.replace('+','=').replace('$',';')
                    
#                 config[k] = v

#         except:
            
#             logger.error('Check if you did the replacement of = by + and ; by $ symbols in the strings provided by the NGS-QC site (uid, cookies and Accept-Language)')
#             print('Check the symbols in the config.ini file (uid, cookies and Accept-Language fields)')
#             print('check symbols in this  :' + line)

#     return config
    

def open_json(file_n):

    '''Receives a file in a json format and returns a json file '''

    with open(file_n) as f:
        conf = json.load(f) 
        return conf
