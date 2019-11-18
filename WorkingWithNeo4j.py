import EnteringIntoNeo4j


def main(patientInfo, reviewFile, patientFile):
    info = patientInfo.split(',')
    patient_limits_file = patientFile
    review_file = reviewFile
    EnteringIntoNeo4j.main(info, review_file, patient_limits_file)


if __name__ == '__main__':
    main()
