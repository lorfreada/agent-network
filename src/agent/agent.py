
from typing import List, Optional



# Need to add input and response validators for both agents and tools
# Need to add concurrency/asynchronicity/parallelism for both agents and tools?
# Should tools be called one by one or should they be called in parallel (i.e. a single tool response, or multiple tool responses)
# Need to add human feedback/human in the loop rules, i.e. (Get repsonse from human or like questions for suer etc.) where?
# Need to make how many iterations to do a certain thing, i.e. how many times to call a tool or agent
# Memory - what memory should be relevant, i.e. during self learning, the agent SHOULD remember what it's learned etc.

class Observability:
    pass

class Tool:
    pass

class Agent:
    def __init__(
        self,
        id: str, # The unique identifier of the agent
        model, # The model that the agent uses to generate responses
        version: str, # The version of the agent
        name: str, # The name of the agent
        responsibility: str, # The responsibility of the agent
        instructions: str, # Instructions on how to achieve the goal
        recommended_process: List[str], # List of steps that the agent should follow to achieve it's goal
        tools: List[Tool], # List of tools that the agent can use to achieve it's goal
        temperature: float, # Temperature controls the randomness of the model's output by adjusting the probability distribution, with lower values producing more focused results and higher values encouraging more diverse and creative outputs.
        top_p: float, # Top p (Nucleus Sampling): Top p determines the size of the token pool for selection by choosing the smallest set of tokens whose cumulative probability exceeds the specified value, with lower values focusing on more probable tokens and higher values allowing for more diverse selections.
        observability: Observability = None, # Takes an observability object which contains information...
        input_guards: List['Agent'] = None, # Agents can be used as a guard for the input of this agent
        output_guards: List['Agent'] = None, # Agents can be used as a guard for the output of this agent
        self_reflection: bool = False, # Agent can reflect on it's own actions and learn from them
        feedback: List['Agent'] = None, # Agent can receive feedback from other agents
        self_learning: bool = False, # Before the agent takes an action, it can learn what it needs to execute the goal better
        self_learning_instructions: str = None, # Instructions on how to learn
        self_learning_tools: List[Tool] = None, # Tools that can be used to help the agent learn
        
        fact_check = None, # Fact checking can be used to verify the information that the agent is using
        ):
        self.id = id
        self.model = model
        self.version = version
        self.name = name
        self.responsibility = responsibility
        self.instructions = instructions
        self.recommended_process = recommended_process
        self.tools = tools
        self.temperature = temperature
        self.top_p = top_p
        self.observability = observability
        self.input_guards = input_guards
        self.output_guards = output_guards
        self.self_reflection = self_reflection
        self.feedback = feedback
        self.self_learning = self_learning
        self.self_learning_instructions = self_learning_instructions
        self.self_learning_tools = self_learning_tools
        
        self.fact_check = fact_check


class AgentOperation:
    def __init__(
        self,
        id: Optional[str] = None,
        agents: List['Agent'] = None,
        input_template: Optional[str] = None,
        output_template: Optional[str] = None,
        goal: Optional[str] = None,
        entry_agents: Optional[List['Agent']] = None,
        policies: Optional[List[str]] = None,
        agent_interaction_rules: Optional[List[str]] = None,
        global_tools: Optional[List['Tool']] = None,
        global_data: Optional[List[str]] = None,
    ):
        self.id = id
        self.agents = agents
        self.input_template = input_template
        self.output_template = output_template
        self.goal = goal
        self.entry_agents = entry_agents
        self.policies = policies
        self.agent_interaction_rules = agent_interaction_rules
        self.global_tools = global_tools
        self.global_data = global_data