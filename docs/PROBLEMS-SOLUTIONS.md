# Problem & Solutions

### Handle simple - complex inputs

1. How does this system perform well for simple inputs but also complex inputs?

A potential solution to this is to allow individual agents handle simple questions, or use a bunch of agents to do it.
This would all be decided and handled by the AgentOperations class could have a built in router

### Agent to agent efficiency

1. How do you decrease latency but maintain accuracy?
2. How do you decrease tokens but maintain accuracy?

For 1 and 2 when an agent calls a tool, it can call another agent at the same time to already get the next agent

### Reduce Hullucinations

1. How do you reduce hullucinations?

### Finetuning specific agents in an agentic system

### How will we handle context window limits and reduction


### Routing problems

Can tools be received through RAG?

### Should constraints be dynamic or static and what do the ylook like?

Given a certain input the constraints are now this etc.

### How can an agent network be deployed? Micro services? how is state carried? etc.

Agent is it's own micro service, communicate via message que, orchestration occurs through main point

### How will you handle error handling?