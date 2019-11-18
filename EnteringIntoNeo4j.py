from py2neo import Graph
gdb = Graph(host='localhost', password='brains')


def main(info, review_file, patient_limits_file):
    # setting up the new patient

    query = """ match (d:Diagnosis {principle_diagnosis: 'Tremor'}) 
                match (t:Target {target: 'STN'})
                merge (p:Patient {patient_id: '%s'})
                merge (p)-[:DIAGNOSIS]->(d)
                merge (data:DataSet {dataset_name: 'TestingNewData'})
                merge (p)-[:DATASET]->(data)
                merge (p)-[:GOES_TO]->(v:Visit)
                merge (p)-[:LEFT_TARGET]->(t)
                return p""" % info[0]

    print(gdb.run(query).data())

    create_patient_limits(info[0], patient_limits_file)
    create_test_settings(info[0], review_file)


# This function creates the patient limits node and assumes that the visit  and patient node is already created in Neo4j
def create_patient_limits(patient_id, patient_limits_file):
    query = """load csv with headers from '%s' as line 
                match (p:Patient {patient_id: '%s'})-[:GOES_TO]->(v:Visit)
                merge (v)-[:HAS]->(:DBSFinalSettings {StepSize:line.StepSize, 
                Minimum:line.Minimum, Maximum: line.Maximum})""" % (patient_limits_file, patient_id)

    print(gdb.run(query).data())


# This function creates the test settings nodes also assuming the visit and patient are already created in Neo4j
def create_test_settings(patient_id, review_file):
    query = """ load csv with headers from '%s' as line
                match (p:Patient {patient_id: '%s'})-[:GOES_TO]->(v:Visit)
                merge (v)-[:TESTED]->(b:TestedSettings)
                on create set b.tag = 'SideEffect'
                create (t:TestSetting {Effect: line.Effect,Contact: line.Contact,Intensity: line.Intensity,
                PulseWidth: line.PulseWidth, Frequency: line.Frequency,
                Impedance: line.Impedance,Target: line.Target,Stim: line.StimulationONOFF})
                merge (b)-[:TRIED]->(t)""" % (review_file, patient_id)

    # if this is run multiple times it will re-create nodes. In the process of fixing this but not totally sure
    print(gdb.run(query).data())




