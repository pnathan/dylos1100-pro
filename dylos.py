import serial
import json
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s  %(message)s')


with serial.Serial('/dev/ttyUSB0', 9600, timeout=31) as ser:
    # one emit per 60s
    # this sets up a number that doesn't go into 60 for the timeoutm
    logging.info("reading, timeout 31s")
    line=ser.readline().decode('ascii').strip().split(',')
    if line != '':
        try:
            # units are in microns, according to the dylos-1100-pro
            # manual
            d = { '>pm0.5': line[0],
                  '>pm2.5' : line[1] }
            print(json.dumps(d))
        except IndexError:
            print('')
            logging.info(line)
