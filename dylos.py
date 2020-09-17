import serial
import json
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s  %(message)s')


with serial.Serial('/dev/ttyUSB0', 9600, timeout=31) as ser:
    logging.info("reading, timeout 31s")
    line=ser.readline().decode('ascii').strip().split(',')
    if line != '':
        try:
            d = { '>pm2.5': line[0],
                  '>pm10' : line[1] }
            print(json.dumps(d))
        except IndexError:
            print('')
            logging.info(line)
