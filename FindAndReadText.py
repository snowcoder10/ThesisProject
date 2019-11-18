from PIL import Image
import pytesseract
import cv2
import os
import csv

# setting up the tesseract file location, this must be changed based on system
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def main(image, timestamp,reviewFile, patientLimitsFile):

    # check to see if we are looking for settings or patient limits
    if image[275, 600, 2] < 10 and image[275, 600, 1] > 100 and image[275, 600, 0] < 110:
        return read_settings(image)
    elif image[1510, 1015, 2] > 175 and image[1510, 1015, 1] < 5 and image[1510, 1015, 0] < 5 and timestamp < 10000:
         return read_patient_limits(image,patientLimitsFile)
    else:
        return False, None


def read_settings(image):

    # setting up a dictionary with the rois that the settings can be found in
    rois = {
        'intensity': image[548:548+57, 491:491+213],
        'pulse width': image[1207:1207+48, 935:935+114],
        'frequency': image[1312:1312+51, 926:926+138],
        'impedance': image[1084:1084+54, 884:884+210],
        'location': image[249:249+42, 134:134+153],
        'Stimulation': image[246:246+39, 878:878+228],
    }

    # loop through the dictionary of rois and read the text from each
    text = ['Benefit']


    for i in rois:
        roi = rois[i]

        # write the grayscale image to disk as a temporary file so we can
        # apply OCR to it
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        filename = "{}.png".format(os.getpid())
        cv2.imwrite(filename, gray)

        # load the image as a PIL/Pillow image, apply OCR, and then delete
        # the temporary file
        read_text = pytesseract.image_to_string(Image.open(filename))
        text.append(read_text)
        os.remove(filename)

        # determine the location of the lead for the contact number
        if i == 'location':
            # 0 for left
            if 'eft' in read_text:
                location = 0
            # right is 1
            else:
                location = 1

    text.insert(1,find_contact(image, location))

    return True, text


def read_patient_limits(image,patientLimitsFile):
    # set up an roi and simply read the text
    roi = image[1116:1116+147, 455:455+303]

    # write the grayscale image to disk as a temporary file so we can
    # apply OCR to it
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file
    text = pytesseract.image_to_string(Image.open(filename))
    text.replace('\n', '\t')
    os.remove(filename)
    patient_file = open(patientLimitsFile, 'a', newline='')
    writer = csv.writer(patient_file)
    writer.writerow(text.split('\n'))
    patient_file.close()

    return True, None


def find_contact(image, location):
    # left side contact
    if location ==0:
        if image[1494, 188, 2] < image[1494,188,1]:
            contact = '1'
        elif image[1494, 269, 2] < image[1494,269,1]:
            contact = '2ABC'
        elif image[1494, 350, 2] < image[1494,350,1]:
            contact = '3ABC'
        elif image[1494, 425, 2] < image[1494,425,1]:
            contact = '4'
        elif image[1494, 503, 2] < image[1494,503,1]:
            contact = '2A'
        elif image[1494, 581, 2] < image[1494,581,1]:
            contact = '2B'
        elif image[1494, 662, 2] < image[1494,662,1]:
            contact = '2C'
        elif image[1494, 737, 2] < image[1494,737,1]:
            contact = '3A'
        elif image[1494, 818, 2] < image[1494,818,1]:
            contact = '3B'
        elif image[1494, 893, 2] < image[1494,893,1]:
            contact = '3C'
        else:
            contact = 'else'

    # right side contact
    else:
        if image[1494, 188, 2] < image[1494,188,1]:
            contact = '9'
        elif image[1494, 269, 2] < image[1494,269,1]:
            contact = '10ABC'
        elif image[1494, 350, 2] < image[1494,350,1]:
            contact = '11ABC'
        elif image[1494, 425, 2] < image[1494,425,1]:
            contact = '12'
        elif image[1494, 503, 2] < image[1494,503,1]:
            contact = '10A'
        elif image[1494, 581, 2] < image[1494,581,1]:
            contact = '10B'
        elif image[1494, 662, 2] < image[1494,662,1]:
            contact = '10C'
        elif image[1494, 737, 2] < image[1494,737,1]:
            contact = '11A'
        elif image[1494, 818, 2] < image[1494,818,1]:
            contact = '11B'
        elif image[1494, 893, 2] < image[1494,893,1]:
            contact = '11C'
        else:
            contact = 'else'

    return contact
