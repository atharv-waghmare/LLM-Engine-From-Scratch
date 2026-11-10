from agent_control.fsm import AgentFSM

def test_fsm_transitions():
    fsm = AgentFSM()
    assert fsm.state == "PLAN"
    
    fsm.step({})
    assert fsm.state == "ACT"
    
    fsm.step({})
    assert fsm.state == "OBSERVE"
    
    fsm.step({})
    assert fsm.state == "REFLECT"
    
    fsm.step({"task_complete": True})
    assert fsm.state == "DONE"

def test_fsm_run():
    fsm1 = AgentFSM()
    history1 = fsm1.run({"task_complete": False}, max_steps=5)
    assert len(history1) == 5
    assert fsm1.state != "DONE"
    
    fsm2 = AgentFSM()
    history2 = fsm2.run({"task_complete": True}, max_steps=10)
    assert len(history2) == 4
    assert fsm2.state == "DONE"