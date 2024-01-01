import csv
import os
from datetime import datetime  # Import the datetime module

from gdx import gdx
gdx = gdx.gdx()

gdx.open(connection='ble')

gdx.select_sensors()

# Generate timestamp
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

# Modify the filename to include the timestamp
filename = f'/Users/rishiraj/Github/godirect-examples/python/data_{timestamp}.csv'

with open(filename, 'w', newline='') as my_data_file:
    csv_writer = csv.writer(my_data_file)

    gdx.start(period=200)
    column_headers = gdx.enabled_sensor_info()
    csv_writer.writerow(column_headers)

    try:
        while True:
            measurements = gdx.read()
            if measurements is None:
                break
            csv_writer.writerow(measurements)
            print(measurements)
    except KeyboardInterrupt:
        print("Recording stopped by user.")

gdx.stop()
gdx.close()
