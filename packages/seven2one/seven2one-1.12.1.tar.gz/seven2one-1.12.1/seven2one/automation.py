import pandas as pd
from datetime import datetime, timedelta
from gql import Client
from gql.transport.requests import RequestsHTTPTransport
from loguru import logger

from .utils.ut_core import Utils
from .utils.ut_autprog import AutProgUtils

class Scheduler():
    def __init__(self, accessToken:str, endpoint:str) -> None:
        #endpoint = 'http://172.16.2.206:8130/graphql/'
        
        header = {
            'authorization': 'Bearer ' + Automation.accessToken
        }
        
        transport =  RequestsHTTPTransport(url=endpoint, headers=header, verify=False)
        self.client = Client(transport=transport, fetch_schema_from_transport=True)

    def schedules(self):
        "List schedules of all workflows"

        graphQLString = f'''query schedules {{
            schedules     
                {{
                scheduleId
                name
                description
                workflowId
                businessKey
                cron
                isActive
                nextFireTime
            }}
        }}
        '''

        result = Utils._executeGraphQL(self, graphQLString)
        if result == None: return

        df = pd.json_normalize(result['schedules'])
        return df

    def createSchedule(self, name:str, workflowId:str, businessKey:str, cron:str, 
        isActive:bool=True, description:str=None, variables:dict=None) -> str:

        if isActive == True:
            isActive = 'true'
        else:
            isActive = 'false'

        if description != None:
            description = description
        else: 
            description = ''

        if variables != None:
            _variables = 'variables: [\n'
            for k,v in variables.items():
                _variables += f'{{key: "{k}", value: "{v}"}}\n'
            _variables += ']'
        else: _variables = ''


        graphQLString = f'''mutation createSchedule {{
            createSchedule(input:{{
                name: "{name}"
                workflowId: "{workflowId}"
                businessKey: "{businessKey}"
                cron: "{cron}"
                description: "{description}"
                isActive: {isActive}
                {_variables}
                
                
            }})
            {{
                schedule {{
                    scheduleId
                    nextFireTime
                }}
                errors {{
                    message
                }}
            }}
        }}'''

        result = Utils._executeGraphQL(self, graphQLString)
        logger.debug(graphQLString)
        if result == None: return

        key = 'createSchedule'
        if result[key]['errors']:
            Utils._listGraphQlErrors(result, key)
        else:
            scheduleId = result[key]['schedule']['scheduleId']
            logger.info(f"New schedule {scheduleId} created.")

        return scheduleId

    def deleteSchedule(self, scheduleId):
        """Deletes a schedule"""

        graphQLString = f'''mutation deleteSchedule {{
            deleteSchedule (scheduleId: "{scheduleId}")
            {{
                errors {{
                message
                }}
            }}
        }}
        '''      

        result = Utils._executeGraphQL(self, graphQLString)
        if result == None: return

        key = 'deleteSchedule'
        if result[key]['errors']:
            Utils._listGraphQlErrors(result, key)
        else:
            logger.info(f"Schedule {scheduleId} deleted")
            return None


    def nextFireTimes(self, workflowId:str, fromTimepoint:str=None, toTimepoint:str=None, count:int=None):
        """Show next fire times of a workflow"""

        if fromTimepoint == None:
            fromTimepoint = datetime.today().isoformat()

        if toTimepoint == None:
            toTimepoint = datetime.today() + timedelta(days=3)

        if count == None:
            _count = ''
        else: 
            _count = f'count: {count}'

        graphQLString = f'''query nextFireTimes {{
            nextFireTimes (
                workflowId: "{workflowId}",
                from: "{fromTimepoint}", 
                to: "{toTimepoint}",
                {_count}
                
                ) {{
                scheduleId
                fireTime
                }}
            }}
        '''
        
        result = Utils._executeGraphQL(self, graphQLString)
        if result == None: return

        return result

class Automation():
    accessToken = ''

    def __init__(self, accessToken:str, endpoint:str) -> None:
        
        Automation.accessToken = accessToken
        
        header = {
            'authorization': 'Bearer ' + accessToken
        }
        
        transport =  RequestsHTTPTransport(url=endpoint, headers=header, verify=False)
        self.client = Client(transport=transport, fetch_schema_from_transport=True)

    def workflows(self) -> pd.DataFrame:
        """Returns a DataFrame of all Workflows"""

        graphQLString = f'''query workflows {{
            workflows {{
                id
                name
                description
                }}
            }}
            '''

        result = Utils._executeGraphQL(self, graphQLString)
        if result == None: return

        df = pd.json_normalize(result['workflows'])
        return df

    def workflowInstances(self, workflowId:bool=None, showTasks=False) -> pd.DataFrame:
        """Shows Instances of a workflow. If workflowId=None, all Instances of all 
        workflows will be returned."""

        meta = ['id', 'name', 'businessKey', 'version', 'startTime', 'endTime', 'state']

        if workflowId != None:
            _workflowId = f'workflowId: "{workflowId}"'
        else:
            _workflowId = f'all: true'

        if showTasks != False:
            _tasks = f'''tasks {{
                            id
                            topic
                            workerId
                            timestamp
                            state
                            retries
                            errorMessage
                        }}'''
        else:
            _tasks = ''

        graphQLString = f'''query Instances {{
            workflowInstances({_workflowId}) {{
                id
                name
                businessKey
                version
                startTime
                endTime
                state
                {_tasks}
                }}
            }}
            '''
     
        result = Utils._executeGraphQL(self, graphQLString)
        if result == None: return

        if showTasks != False:
            df = pd.json_normalize(result['workflowInstances'], meta=meta, record_path=['tasks'], record_prefix='task.', errors='ignore')
            df = df.sort_values(by='startTime', ascending=False)
        else:
            df = pd.json_normalize(result['workflowInstances'])
            df = df.sort_values(by='startTime', ascending=False)
        return df
    
    def createWorkflow(self, id, name, description:str=None):

        graphQLString = f'''mutation createWorkflow {{
            createWorkflow(
                input: {{
                    id: "{id}"
                    name: "{name}"
                    description: "{description}"
                }}
                ) {{
                    ...on CreateWorkflowError {{
                    message
                    }}
                    ... on WorkflowCreated {{
                        workflow {{
                            id
                        }}
                    }}
                }}
            }}
        '''
        
        result = Utils._executeGraphQL(self, graphQLString)
        if result == None: return

        return result
                        
    def deployWorkflow(self, workflowId:str, filePath:str) -> None:
        """Deploys a Camunda XML to an existing workflow"""

        fileContent = Utils._encodeBase64(filePath)
        logger.debug(f"fileContent: {fileContent[:10]}")

        graphQLString = f'''mutation deployWorkflow {{
            deployWorkflow(
                input: {{
                    fileContentBase64: "{fileContent}"
                    workflowId: "{workflowId}"
                }}
            ) {{
                ... on DeployWorkflowError {{
                    message
                }}
                ... on InvalidWorkflowProcessId {{
                    processId
                    workflowId
                    message
                }}
                ... on WorkflowDeployed {{
                    version
                }}
            }}
        }}
        '''

        result = Utils._executeGraphQL(self, graphQLString)
        if result == None: return

        return result

    def startWorkflow(self, workflowId:str, businessKey:str, inputVariables:dict=None):
        """Starts a workflow"""

        if inputVariables == None:
            _vars = ''
        else:
            _vars = AutProgUtils._varsToString(inputVariables, 'input')

        graphQLString = f'''
            mutation ExecuteWF {{
                startWorkflow(input: {{ 
                    businessKey: "{businessKey}"
                    workflowId: "{workflowId}" 
                    {_vars}
                    }}
                ) {{
                    ... on ProcessDefinitionNotFound {{
                        workflowId
                        message
                        }}
                    ... on StartWorkflowError {{
                            message
                            }}
                    ... on WorkflowStarted {{
                        workflowInstanceId
                        }}
                    }}
                }}
            '''

        result = Utils._executeGraphQL(self, graphQLString)
        if result == None: return

        return result

    def deleteWorkflow(self, workflowId):
        """Deletes a workflow"""

        graphQLString = f'''mutation deleteWorkflow {{
            deleteWorkflow (id: "{workflowId}")
            {{
                ... on DeleteWorkflowError {{
                    message
                    }}
                ...on WorkflowDeleted {{
                    success
                    }}
                ... on WorkflowNotFound {{
                    workflowId
                    message
                    }}
                
                }}
            }}
        '''

        result = Utils._executeGraphQL(self, graphQLString)
        if result == None: return

        return result

    def terminateWorkflowInstance(self, workflowInstanceId):
        """Terminates a workflow instance"""

        graphQLString = f'''mutation terminateWorkflowInstance {{
            terminateWorkflowInstance(
                workflowInstanceId:"{workflowInstanceId}") {{
                ...on TerminateWorkflowInstanceError {{
                    message
                    }}
                ...on WorkflowInstanceNotFound {{
                    workflowInstanceId
                    message
                    }}
                ...on WorkflowInstanceTerminated {{
                    success
                    }}
                }}
            }}
        '''

        result = Utils._executeGraphQL(self, graphQLString)
        if result == None: return

        return result


