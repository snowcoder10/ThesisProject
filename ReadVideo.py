import cv2
import FindAndReadText
import csv


def main(video,reviewFile,patientLimitsFile):
    break_into_frames(video,reviewFile,patientLimitsFile)


def break_into_frames(video, reviewFile,patientLimitsFile):
    v = cv2.VideoCapture(video)

    # find the length of the video
    v.set(cv2.CAP_PROP_POS_AVI_RATIO, 1)
    duration = v.get(cv2.CAP_PROP_POS_MSEC)

    # looping through the video at 1000 time stamps
    v.set(cv2.CAP_PROP_POS_AVI_RATIO, 0)
    cur = 0
    step = duration/100
    test = SettingsList([])

    while cur < 100:
        v.set(cv2.CAP_PROP_POS_MSEC, cur*step)
        ret, frame = v.read()

        if not ret:
            break

        # go through until there is a frame that we are able to read text from
        op = False

        while not op:
            # send the frame as well as a time stamp just to make sure we are in a good spot
            op, text = FindAndReadText.main(frame, duration - v.get(cv2.CAP_PROP_POS_MSEC),reviewFile, patientLimitsFile)

            # check to see if this is a new setting
            if text is None:
                break

            if (len(test.settings) == 0) or (not text[1] == test.settings[1]) \
                    or (not text[2][0:4] == test.settings[2][0:4]) \
                    or (not text[0] == test.settings[0]):
                # writing to the csv file
                review_file = open(reviewFile, 'a', newline='')
                writer = csv.writer(review_file)
                writer.writerow(text)
                test.settings = text
                review_file.close()

            ret, frame = v.read()
            if not ret:
                break

        cur += 1


class SettingsList:
    def __init__(self, settings):
        self.settings = settings
