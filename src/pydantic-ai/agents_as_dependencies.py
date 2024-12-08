from dataclasses import dataclass

from pydantic_ai import Agent, RunContext


@dataclass
class MyDeps:
    factory_agent: Agent[None, list[str]]


joke_agent = Agent(
    'openai:gpt-4o',
    deps_type=MyDeps,
    system_prompt=(
        'Use the "joke_factory" to generate some jokes, then choose the best. '
        'You must return just a single joke.'
    ),
)

factory_agent = Agent('openai:gpt-4o', result_type=list[str])


@joke_agent.tool
async def joke_factory(ctx: RunContext[MyDeps], count: int) -> str:
    r = await ctx.deps.factory_agent.run(f'Please generate {count} jokes.')
    return '\n'.join(r.data)


result = joke_agent.run_sync('Tell me a joke.', deps=MyDeps(factory_agent))
print(result.data)
#> Did you hear about the toothpaste scandal? They called it Colgate.