# SimpleDCMTKReceiver

## Purpose

The purpose of this program is to download studies from a specified PACS system. As input serves a csv file containing Study Instance UID(s).

## Usage

### config file
Please fill the config.ini file before execution in the following way

    [PACS]
    PACS_IP_ADRESS = IP Adress or URL of the PACS Server
    PACS_PORT = Port of the PACS Server
    AEC = AEC of the PACS

    [LOCAL]
    PORT_NUMBER_INC_ASSOC = The port number of the receiving machine, where you accept incoming connections
    AET = Your AET

There is an example config file given in this repository.
The AET must be known to the PACS, from which you want to receive images.

### Command line options
    usage: main.py [-h] [-c] [-p] [-f CSV_FILE_NAME] [-d] [-v]

    options:
    -h, --help            show this help message and exit
    -c, --config          Read and print out the configuration and exit
    -p, --pacs-check      Check PACS availability and exit
    -f CSV_FILE_NAME, --file-name CSV_FILE_NAME
                            Specify the filename of the CSV file containing the study instance uids
    -d, --dry-run         Create and print out the movescu commands, but do not initiate move
    -v, --verbose         Print out additional information

The CSV file specified in the -f option has to be put into the `reports` folder. The CSV file has to contain a field `procedurestudyinstanceuid`, but can also contain additional fields. Separator is `;`. All Study Instance UIDs will tried to be downloaded from the PACS
The received images are being stored to the images folder in the convention `images/study_instance_uid`
