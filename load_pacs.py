import os
import subprocess

def create_movescu_cmd(port_number_inc_assoc, study_instance_uid, target_directory, aet_name, aec_name, pacs_ip_adress, pacs_port):
    cmd = ['movescu', '-S', '+P', str(port_number_inc_assoc), '-k', '0008,0052="SERIES"','-k', '0020,000D="'+str(study_instance_uid)+'"', '-od', str(target_directory), '-aet', str(aet_name), '-aec', str(aec_name), str(pacs_ip_adress), str(pacs_port), '-d']
    return cmd

def create_folder(study_instance_uid):
    try:
    # Create a new folder called "new_folder"
        os.mkdir('./images/' + study_instance_uid)
        return True
    except FileExistsError:
        print("\033[31mAn error occurred while creating the folder - please check if the folder already exists and delete it\033[0m")
        return False
    except Exception as e:
        print(e.stderr)
        return False



def run_pacs_move(cmd, verbose):
    if verbose:
        print("Starting movescu")
    try:
    # Run the 'ls' command and capture the output
        output = subprocess.check_output(cmd, timeout=1800, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        # The subprocess returned a non-zero exit code
        print("\033[31mAn error occured while trying to recive the images: {} \033[0m".format(" ".join(cmd)))
        print(e.stderr)
