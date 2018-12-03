#!/usr/bin/env python2.7

"""
state-flow api
"""


##region data structure
pass


class StateFlow:
  def __init__(self): pass

  id=''
  name=''
  states=[] #list of State objects

  def save(self): pass #save object to database

  @staticmethod
  def getById(id): pass #get object in database by id


class State:
  def __init__(self): pass

  id=''
  name=''
  stateflow=None #the StateFlow object that this state belongs to
  actions=[] #list of StateAction objects

  def save(self): pass #save object to database

  @staticmethod
  def getById(id): pass #get object in database by id

  def hasAction(self, action):
    for a in self.actions:
      if a.id == action.id: return True
    return False


class StateAction:
  def __init__(self): pass

  id=''
  name=''
  fromState=None #the current State that owns the action
  switchToState=None #the target State to switch to when the action is triggered
  handlers=[] #list of registered StateActionHandler objects to run when the action is triggered

  def save(self): pass #save object to database

  @staticmethod
  def getById(id): pass #get object in database by id


class StateActionHandler:
  def __init__(self): pass

  id=''
  code='' #contain code to run e.g. python code
  action=None #the StateAction that this handler attachs to


  def save(self): pass #save object to database

  def run(self): pass #the execution method to run it

  @staticmethod
  def getById(id): pass #get object in database by id


class StateFlowInstance:
  def __init__(self): pass

  id=''
  stateflow=None #the StateFlow object where this instance is created from
  state=None #the current State object of this instance

  def save(self): pass #save object to database

  @staticmethod
  def getById(id): pass #get object in database by id


pass
##endregion data structure


##region the API
pass


#region requirement R1

def createStateFlow(name):
  """
  E1a create the state-flow
  """
  newStateFlow = StateFlow()
  newStateFlow.name=name
  newStateFlow.save()


def createState(stateflowId, stateName):
  """
  E1b add states to the state-flow
  """
  state = State()
  state.name=stateName
  state.stateflow = StateFlow.getById(stateflowId)
  state.save()


def addStateAction(stateId_from, stateId_to, actionName):
  """
  E1c add actions to a state
  """
  action = StateAction()
  action.name = actionName
  action.fromState = StateAction.getById(stateId_from)
  action.switchToState = StateAction.getById(stateId_to)


def addStateActionHandler(actionId, handlerCode):
  """
  E1d add action-handlers to an action
  """
  handler = StateActionHandler()
  handler.code = handlerCode
  handler.action = StateAction.getById(actionId)
  handler.save()

#endregion requirement R1


#region requirement R2

def createInstance(stateflowId):
  """
  E2a create state-flow instance given a specific state-flow name
  """
  instance = StateFlowInstance()
  instance.stateflow = StateFlow.getById(stateflowId)
  instance.save()


def setInstanceState(instanceId, stateId):
  """
  E2b set state for a state-flow instance
  """
  instance = StateFlowInstance.getById(instanceId)
  instance.state = State.getById(stateId)
  instance.save()

#endregion requirement R2


#region requirement R3


def fireAction(instanceId, actionId):
  """
  E3 fire action on a given instance
  We need
  - check if the action is applicable on the instance i.e. its current state has that action registered
  - if yes, then apply the action
  - take care of the state
  """
  instance = StateFlowInstance.getById(instanceId)
  action = StateAction.getById(actionId)
  if not instance.state: return #current state is empty => do nothing

  #check if the action is applicable on the instance i.e. its current state has that action registered
  if instance.state.hasAction(action):
    #apply the action
    for handler in action.handlers:
      handler.run()

    #switch to new state
    instance.state = action.switchToState


#endregion requirement R3


pass
##endregion the API
