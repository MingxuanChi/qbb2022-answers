#!/usr/bin/env python3

import sys # import sys

def parse_vcf(fname): 
    vcf = [] # create a list that will hold all information needed
    info_description = {} # 
    info_type = {} # create a dictionary that will tell the specific type that each field should be
    format_description = {} # create a dictionary that will tell the genotyping format
    type_map = {
        "Float": float,
        "Integer": int,
        "String": str
        } # matching the types given by .vcf heading with a python type and function
    malformed = 0 # create a variable that will be used to count malform number

    try:
        fs = open(fname) # try to open a file 
    except:
        raise FileNotFoundError(f"{fname} does not appear to exist", file=sys.stderr) # if there is no file by the name, raise an error

    for h, line in enumerate(fs): # go through the file line by line, h is index, line is the content string of each line
        if line.startswith("#"): # if it is a header line
            try: # try to deal with headers and make sure the format is correct
                if line.startswith("##FORMAT"): # find the FORMAT line
                    fields = line.split("=<")[1].rstrip(">\r\n") + "," #
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            name, value = fields[start:i].split('=')
                            if name == "ID":
                                ID = value
                            elif name == "Description":
                                desc = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    format_description[ID] = desc.strip('"')
                elif line.startswith("##INFO"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            name, value = fields[start:i].split('=')
                            if name == "ID":
                                ID = value
                            elif name == "Description":
                                desc = value
                            elif name == "Type":
                                Type = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    info_description[ID] = desc.strip('"')
                    info_type[ID] = Type
                elif line.startswith('#CHROM'):
                    fields = line.lstrip("#").rstrip().split("\t")
                    vcf.append(fields)
            except:
                raise RuntimeError("Malformed header")
        else: # go to deal with the body
            try: # make sure the format of body is correct
                fields = line.rstrip().split("\t") # remove the new line character from each line and split them by TAB, give the result list to 'fields'
                fields[1] = int(fields[1]) # convert the position number into integer
                if fields[5] != ".": # see if the quality exist for this gene, 
                    fields[5] = float(fields[5]) # if quality exist, convert it into float; if '.', no operation
                info = {} # create an empty dictionary for info
                for entry in fields[7].split(";"): # going into a info string and first split by ';' to have a list of ['XX=nn', 'XXX=nnn']
                    temp = entry.split("=") # split each 'XX=nn' into a list of ['info ID','info value']
                    if len(temp) == 1: # if there is no data associated with a specific info id
                        info[temp[0]] = None # if so, give a None as the value to the key 'infoID' in the info dictionary
                    else: # if there is a value associated to the infoID
                        name, value = temp # name for infoID, value for info value
                        Type = info_type[name] # use the infoID to search what type it should be in previously built info_type dictionary from header part 
                        info[name] = type_map[Type](value) # adding a key as infoID to the info dictionary and give the value converted according to the type obtained in the last line. (using the type to search for a type function in type map)
                fields[7] = info # give the info dictionary to the 8 column, where the original info string was
                if len(fields) > 8: # if there are more fields after info (genotype)
                    fields[8] = fields[8].split(":") # to split format string if there are more than one items in format column, which delimited by ':', get a list of format type
                    if len(fields[8]) > 1: # if there are more than one format
                        for i in range(9, len(fields)): # looking through each person in genotype part
                            fields[i] = fields[i].split(':') # split the information string into a list of value of all the format. ['n|n','n|n']
                    else: # if there is only one format
                        fields[8] = fields[8][0] # use the only one item (string) in the format inforamtion list to replace the original list of format information
                vcf.append(fields) # we have properly foomated everything and store it in to vcf list
            except:
                malformed += 1 # if there is any error when running the above script, malformed number plus 1
    vcf[0][7] = info_description
    if len(vcf[0]) > 8: 
        vcf[0][8] = format_description
    if malformed > 0: # if there are at least one malformed line
        print(f"There were {malformed} malformed entries", file=sys.stderr) # print 'There were n malformed entries'; 
    return vcf # give vcf list as the output of this function

if __name__ == "__main__": # if we are running this script
    fname = sys.argv[1] # use the content after the name of the script in command line as fname
    vcf = parse_vcf(fname) # running the function on fname file and store the output into variable
    for i in range(10): # print the first ten lines one by one
        print(vcf[i])
