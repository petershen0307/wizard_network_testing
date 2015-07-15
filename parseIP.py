import csv


def handle_wire_shark_ip_list(file_name, wire_shark_ip_count):
    try:
        with open(file_name, 'r') as csvFile:
            for row in csv.DictReader(csvFile):
                key_ip = str(row['Source'])
                if key_ip in wire_shark_ip_count:
                    wire_shark_ip_count[key_ip] += 1
                else:
                    wire_shark_ip_count[key_ip] = 1
    except FileNotFoundError:
        pass


def handle_wizard_ip_list(file_name, wizard_ip_count):
    try:
        with open(file_name, 'r') as file:
            for line in file.read().splitlines():
                if line in wizard_ip_count:
                    wizard_ip_count[line] += 1
                else:
                    wizard_ip_count[line] = 1
    except FileNotFoundError:
        pass


def print_result(file_name, result_output_dict, wire_shark_ip_count):
    not_search_list = list()
    with open(file_name, 'w', newline='\n') as file:
        csv_writer = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for ip_address in wire_shark_ip_count:
            if ip_address in result_output_dict:
                if result_output_dict[ip_address] != wire_shark_ip_count[ip_address]:
                    csv_writer.writerow([ip_address, str(result_output_dict[ip_address]), str(wire_shark_ip_count[ip_address])])
                    print(ip_address + ',' + str(result_output_dict[ip_address]) + ',' + str(wire_shark_ip_count[ip_address]))
                else:
                    print(ip_address + 'equal')
            else:
                not_search_list.append(ip_address)
    if len(not_search_list) > 0:
        with open('not' + file_name, 'w', newline='\n') as not_exist_file:
            for line in not_search_list:
                not_exist_file.write(line + '\n')

wireSharkFileName_soap = 'soapWireshark.csv'
soapIPListFileName = 'soapIPList.txt'
wireSharkFileName_qt = 'qtWireshark.csv'
qtIPListFileName = 'qtIPList.txt'
if __name__ == '__main__':
    wireSharkIPCount_soap = dict()
    wizardSoapIPCount = dict()

    handle_wire_shark_ip_list(wireSharkFileName_soap, wireSharkIPCount_soap)
    handle_wizard_ip_list(soapIPListFileName, wizardSoapIPCount)
    print_result('soapOutput.csv', wizardSoapIPCount, wireSharkIPCount_soap)

    wireSharkIPCount_qt = dict()
    wizardQtIPCount = dict()
    handle_wire_shark_ip_list(wireSharkFileName_qt, wireSharkIPCount_qt)
    handle_wizard_ip_list(qtIPListFileName, wizardQtIPCount)
    print_result('qtOutput.csv', wizardQtIPCount, wireSharkIPCount_qt)

