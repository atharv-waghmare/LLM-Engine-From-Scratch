import copy 
import pytest
from agent_control.lifo_stack import LIFOStack

def test_stack_basics():
  stack = LIFOStack()
  assert stack.is_empty()

  stack.push(1)
  stack.push(2)
  assert len(stack) == 2
  assert stack.peek() == 2

  assert stack.pop() == 2
  assert stack.pop() == 1
  assert stack.is_empty()

  with pytest.raises(IndexError):
    stack.pop()
    
def test_agent_state_rollback():
  stack = LIFOStack()
  state = {'turn': 0, 'context': []}

 
  stack.push(copy.deepcopy(state))
  state['turn'] = 1
  state['context'].append('tool_1_success')

  
  state.push(copy.deepcopy(state))
  try:
    state['turn'] = 2
    state['context'].append('tool_2_crash')
    raise RuntimeError()
  except RuntimeError:
    state = stack.pop()

  
  assert state == {'turn': 1, 'context': ['tool_1_success']}

  stack.push(copy.deepcopy(state))
  state['turn'] = 2
  state['context'].append('tool_3_success)

  assert state == {'turn': 2, 'context': ['tool_1_success', 'tool_3_success']}
  
