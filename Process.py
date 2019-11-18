#!/usr/bin/python

import ReadVideo
import csv
import sys
#import time


def main(video, saveLocation):
   # start_time = time.time()

    # creating the review file to be written to
    directory_1 = saveLocation + '/review_settings.csv'
    review_file = open(directory_1, 'w', newline='')
    writer = csv.writer(review_file)
    header = ['Effect','Contact','Intensity','PulseWidth','Frequency','Impedance','TargetLocation','StimulationONOFF']
    writer.writerow(header)
    review_file.close()

    # create a patient limits new csv file to be written to
    directory_2 = saveLocation + '/patient_limits.csv'
    limits_file = open(directory_2, 'w', newline='')
    writer = csv.writer(limits_file)
    header = ['StepSize', 'Minimum', 'Maximum']
    writer.writerow(header)
    limits_file.close()

    ReadVideo.main(video, directory_1, directory_2)


if __name__ == "__main__":
    main()
