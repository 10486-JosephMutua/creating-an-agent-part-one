from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Now you can access the environment variables
tavily_api_key = os.getenv('TAVILY_API_KEY')

# If the key is missing, it will return None
from langchain_community.tools.tavily_search import TavilySearchResults
search = TavilySearchResults(max_results=2)
search_results = search.invoke("when was the kenya kcse results released and which school topped in mombasa county")
#print(search_results[0]['content'])
# If we want, we can create other tools.
# Once we have all the tools we want, we can put them in a list that we will reference later.
tools = [search]

#interacting mith mistaralai llm
from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model="open-mistral-7b")
from langchain_core.messages import HumanMessage
#response = model.invoke([HumanMessage(content="hi! who is the president of kenya")])
#print(response.content)
#We can now see what it is like to enable this model to do tool calling. In order to enable that we use .bind_tools to give the language model knowledge of these tools
model_with_tools = model.bind_tools(tools)
#Now, let's try calling it with some input that would expect a tool to be called.
#We can see that there's now no text content, but there is a tool call! It wants us to call the Tavily Search tool.

#This isn't calling that tool yet - it's just telling us to. In order to actually call it, we'll want to create our agent.

response = model_with_tools.invoke([HumanMessage(content="What's the weather in SF?")])


#print(f"ContentString: {response.content}")
#print(f"ToolCalls: {response.tool_calls}")

from langgraph.prebuilt import create_react_agent
agent_executor = create_react_agent(model, tools)

#response = agent_executor.invoke(
   # {"messages": [HumanMessage(content="whats the weather in sf?")]}
#)
#print(response["messages"])

from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()
agent_executor = create_react_agent(model, tools, checkpointer=memory)

config = {"configurable": {"thread_id": "abc123"}}
for chunk in agent_executor.stream(
    {"messages": [HumanMessage(content="hi who is current president of kenya")]}, config
):
    print(chunk)
    print("----")

    config = {"configurable": {"thread_id": "xyz123"}}
    config = {"configurable": {"thread_id": "xyz123"}}
config = {"configurable": {"thread_id": "xyz123"}}

