import warnings
import xml.etree.ElementTree as ET
import xml.etree.ElementTree as etree
from io import BytesIO, StringIO
import io

from lxml import etree
from SpiffWorkflow import Task, Workflow
from SpiffWorkflow.bpmn.parser.BpmnParser import BpmnParser
from SpiffWorkflow.bpmn.serializer.BpmnSerializer import BpmnSerializer
from SpiffWorkflow.serializer.prettyxml import XmlSerializer
from SpiffWorkflow.serializer.xml import XmlSerializer
from SpiffWorkflow.specs import *
from SpiffWorkflow.specs.WorkflowSpec import WorkflowSpec
from SpiffWorkflow.workflow import Workflow
from tensorflow.python.keras.initializers import deserialize
from SpiffWorkflow.bpmn.storage.Packager import Packager

warnings.warn('A Helpful Message !')

# wily report 

# workflow
# SpiffWorkflow
xml_str = """<?xml version="1.0" encoding="UTF-8"?>
<:definitions xmlns:="http://www.omg.org/spec//20100524/MODEL" xmlns:di="http://www.omg.org/spec//20100524/DI" xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" xmlns:di="http://www.omg.org/spec/DD/20100524/DI" xmlns:camunda="http://camunda.org/schema/1.0/" id="Definitions_18q2bcz" targetNamespace="http://.io/schema/" exporter="Camunda Modeler" exporterVersion="3.4.1">
  <:process id="simple_" name="process_101" isExecutable="true" camunda:versionTag="1">
    <:startEvent id="StartEvent_1" name="start">
      <:outgoing>SequenceFlow_1qhm1a6</:outgoing>
    </:startEvent>
    <:sequenceFlow id="SequenceFlow_1qhm1a6" sourceRef="StartEvent_1" targetRef="Task_0jhfra5" />
    <:endEvent id="EndEvent_058zt36" name="end">
      <:incoming>SequenceFlow_0xqsox7</:incoming>
    </:endEvent>
    <:sequenceFlow id="SequenceFlow_0xqsox7" sourceRef="Task_0jhfra5" targetRef="EndEvent_058zt36" />
    <:userTask id="Task_0jhfra5" name="Manual Step">
      <:documentation>manual_step</:documentation>
      <:incoming>SequenceFlow_1qhm1a6</:incoming>
      <:outgoing>SequenceFlow_0xqsox7</:outgoing>
    </:userTask>
  </:process>
  <di:Diagram id="Diagram_1">
    <di:Plane id="Plane_1" Element="simple_">
      <di:Shape id="_Shape_StartEvent_2" Element="StartEvent_1">
        <dc:Bounds x="179" y="99" width="36" height="36" />
        <di:Label>
          <dc:Bounds x="186" y="142" width="22" height="14" />
        </di:Label>
      </di:Shape>
      <di:Edge id="SequenceFlow_1qhm1a6_di" Element="SequenceFlow_1qhm1a6">
        <di:waypoint x="215" y="117" />
        <di:waypoint x="270" y="117" />
      </di:Edge>
      <di:Shape id="EndEvent_058zt36_di" Element="EndEvent_058zt36">
        <dc:Bounds x="432" y="99" width="36" height="36" />
        <di:Label>
          <dc:Bounds x="441" y="142" width="19" height="14" />
        </di:Label>
      </di:Shape>
      <di:Edge id="SequenceFlow_0xqsox7_di" Element="SequenceFlow_0xqsox7">
        <di:waypoint x="370" y="117" />
        <di:waypoint x="432" y="117" />
      </di:Edge>
      <di:Shape id="UserTask_0zmnlxj_di" Element="Task_0jhfra5">
        <dc:Bounds x="270" y="77" width="100" height="80" />
      </di:Shape>
    </di:Plane>
  </di:Diagram>
</:definitions>"""



parser = etree.XMLParser(recover=True)
root = etree.fromstring(xml_str.encode('utf-8'), parser=parser)

bpmn_packaged = io.BytesIO()
package = Packager(bpmn_packaged, 'Process_1')
package.add_bpmn_file(xml_str.encode("utf-8"))
package.create_package()

wf_spec = WorkflowSpec.deserialize(BpmnSerializer(), xml_str.encode('utf-8'))
workflow = Workflow(wf_spec)

parser = BpmnParser()
parser.add_bpmn_xml(root)

# Create an instance of the workflow, according to the specification.
wf = Workflow(spec)

tasks = wf.get_tasks(Task.READY)
    task_start = tasks[0]
    workflow.complete_task_from_id(task_start.id)
 
    tasks = workflow.get_tasks(Task.READY)
    multichoice = tasks[0]
    workflow.complete_task_from_id(multichoice.id)
 
    tasks = workflow.get_tasks(Task.READY)
    task_a1 = tasks[0]
    workflow.complete_task_from_id(task_a1.id)