import os,sys
import copy

from argparse import ArgumentParser
def get_the_output(data,index,dep,len):
    string_to_write=[]

    if dep.split(',').__len__() == 2:
        string_to_write.append(hex_string_to_chars(data[index:index + len]))
        string_to_write.append(0) #0 for word
    else:
        string_to_write.append(hex_string_join(data[index:index + len]))
        string_to_write.append(1) #1 for number
    return string_to_write
def hex_string_join(hex_str):
    hex_str=endin_str(hex_str)
    hex_str=str().join(hex_str)
    while  hex_str.__len__()>1 and hex_str[0]=="0":
        hex_str=hex_str[1:]
    return hex_str
def hex_string_to_chars(hex_str):
    chars=""
    for i in hex_str:
        chars+=chr(int(i,16))
    return chars
def endin_str(hex_str):
    hex_str.reverse()
    return hex_str
def endin_int(hex_str):
    hex_str.reverse()
    hex_str=str().join(hex_str)
    return int(hex_str,16)
def Pe_format_sample(file_path,newfilename):
    # getting files binaries
    string_to_write = ""
    if file_path.__contains__("C:")==False:
        file_path=(os.path.join(sys.path[0],file_path))
    with open(file_path, 'rb') as f:
        buffer = f.read()
    buffer = ['{:02X}'.format(b) for b in buffer]
    location_of_Pe_header = endin_int(buffer[0x3c:0x40])
    pointer_to_Pe_Header = location_of_Pe_header  # the pointer to Pe Header
    pe_header=buffer[pointer_to_Pe_Header:] # the Pe header
    machine=hex_string_join(pe_header[0x4:0x6])
    size_of_optional_header=endin_int(pe_header[0x14:0x16])# size of optional header which start in offset 0x18
    location_of_optional_header=0x18 # optional header's location realtive to PE SIG

    optional_header=pe_header[location_of_optional_header:location_of_optional_header+size_of_optional_header]

    number_of_section=endin_int(pe_header[0x6:0x8]) # number of section located in offset 0x6 in PE header
    location_of_saction_table=location_of_optional_header+size_of_optional_header # the location of section table is at the end of the optional header
    size_of_section_table=0x28*number_of_section # every section 0x28 bytes long
    section_table=pe_header[location_of_saction_table:location_of_saction_table+size_of_section_table] # 0x28*number_size of section table
    buffer_list_data=[buffer,pe_header,optional_header,section_table]
    # the Pe header

    with open(os.path.join(sys.path[0],"dataformat.txt"), 'r') as f:
        datastructure = str(f.read())

    splited_format = datastructure.split("@")  # '@' is seperetor bettwen heders
    # format of every header from the datastracute.txt
    DOS_format = splited_format[0]
    pe_header_format = splited_format[1]
    optional_header_format = splited_format[2]
    section_format = splited_format[3]

    for j in range(splited_format.__len__()):
        format = splited_format[j]
        index = 0
        length = 0
        section_identefier=1
        if j==3:
            section_identefier=number_of_section
        for q in range(section_identefier):
            for i in format.split('\n'):
                if i.split("=").__len__() == 2:
                    array_of_i = i.split("=")
                    string_to_write += i.split("=")[0]
                    if array_of_i[1].__contains__('#') == True:
                        if machine.__contains__('64') == True:
                            array_of_i[1] = array_of_i[1].split('#')[1]
                        else:
                            array_of_i[1] = array_of_i[1].split('#')[0]
                    if j == 0 and i == (format.split('\n'))[-2]:
                        string_to_write += str(hex(pointer_to_Pe_Header))
                    else:
                        length = int(array_of_i[1].split(',')[0])
                        value_format=get_the_output(buffer_list_data[j], index, array_of_i[1], length)

                        if value_format[1]==1 :
                            if int(value_format[0],16)>9:
                                value_format[0]+="h ("+str(int(value_format[0],16))+")"
                            value_format[0] = " = " + value_format[0]

                        string_to_write += value_format[0]
                    index += length
                elif i.__len__() > 2:
                    string_to_write += i
                string_to_write += "\n"

    with open(os.path.join(sys.path[0],newfilename+".txt"), 'w') as n:
        n.write(string_to_write)
        copy.copy("123")
        print("\n---------------------------------------------------------------\n--"
              "-------------------------------------------------------------\n--\n--   "
              +newfilename+".txt"+" has been created int location : ""\n--   "
              +(os.path.join(sys.path[0],newfilename+".txt"))+"\n--\n-----------------"
            "----------------------------------------------\n---------------------------------------------------------------\n")

if __name__ == '__main__':
    parser = ArgumentParser(argument_default="proper use : Python <filepath> <newfilename>",
                            description='Pe Header Parser',
                            epilog="Python PE_Parser.py <filepath> <newfilename>")
    parser.add_argument("filepath", help="path of file to parse",
                        type=str)
    parser.add_argument("filename", help="name of the new data file",
                        type=str)
    args = parser.parse_args()
    filepath=args.filepath
    filename=args.filename
    Pe_format_sample(str(filepath),str(filename))






