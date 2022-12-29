# File: main.py

from parse_args import parse_args
from read_config import read_config, print_config
from check_pacs import check_pacs
from parse_reports import read_reports
from load_pacs import create_movescu_cmd, create_folder, run_pacs_move

# Parse the command line arguments
args = parse_args()

# Print the config file
if args.config:
    print_config()
    exit()

# Read the config file values
conf = read_config()

# Check PACS availability
if not args.dry_run:
    if check_pacs(conf.get('PACS', 'PACS_IP_ADRESS'), conf.get('PACS', 'PACS_PORT'), args.verbose) == True:
        print("The PACS at IP adress: {} and port: {} is available".format(conf.get('PACS', 'PACS_IP_ADRESS'), conf.get('PACS', 'PACS_PORT')))
    else:
        print("\033[31mThe PACS at IP adress: {} and port: {} is unavailable\033[0m".format(conf.get('PACS', 'PACS_IP_ADRESS'), conf.get('PACS', 'PACS_PORT')))
        print("Aborting")
        exit()
    # Exit, if only pacs availability check
    if args.pacs_check:
        exit()
else:
    print("Dry run: only printing out the commands")

# Read in the csv file with the study instances
if args.csv_file_name:
    result = read_reports(args.csv_file_name)

    # Check the status of the function call
    if result['status'] == 'failure':
        # If the function returned a failure status, print the reason for the failure
        print(result['reason'])
    else:
        # If the function returned a success status, print the data
        for item in result['data']:
            # Access the values in the dictionary using the keys
            procedurestudyinstanceuid = item['procedurestudyinstanceuid']
            cmd = create_movescu_cmd(port_number_inc_assoc=conf.get('LOCAL', 'PORT_NUMBER_INC_ASSOC'), 
                        study_instance_uid=procedurestudyinstanceuid, 
                        target_directory='./images/' + procedurestudyinstanceuid, 
                        aet_name=conf.get('LOCAL', 'AET'), 
                        aec_name=conf.get('PACS', 'AEC'), 
                        pacs_ip_adress=conf.get('PACS', 'PACS_IP_ADRESS'), 
                        pacs_port=conf.get('PACS', 'PACS_PORT'))
            if args.dry_run or args.verbose:
                print("Created movescu command:")
                print(" ".join(cmd))
            if args.dry_run:
                continue
            if create_folder(procedurestudyinstanceuid):
                if args.verbose:
                    print("Will now start download into folder.")
            else:
                exit()
            run_pacs_move(cmd, args.verbose)

            
else:
    print("\033[31mNo input csv file specified\033[0m")