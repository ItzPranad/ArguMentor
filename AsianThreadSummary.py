import os
from rich.console import Console
from webscout import Sambanova

console = Console()

# Speeches text for each speaker
pm = """The proposal for one nation, one election will bring much-needed stability and efficiency to Indian democracy. Frequent elections drain the country’s resources, disrupt governance, and stall development projects. Synchronizing elections will reduce costs significantly, save time, and allow the government to focus entirely on policy implementation without constant election interruptions. Additionally, it will curb voter fatigue and improve voter turnout by consolidating all elections into one.The proposal for one nation, one election will bring much-needed stability and efficiency to Indian democracy. Frequent elections drain the country’s resources, disrupt governance, and stall development projects. Synchronizing elections will reduce costs significantly, save time, and allow the government to focus entirely on policy implementation without constant election interruptions. Additionally, it will curb voter fatigue and improve voter turnout by consolidating all elections into one."""
ol = """While the idea of one nation, one election sounds appealing, it threatens the federal structure of India. States have diverse political, social, and economic contexts, and forcing synchronized elections undermines their autonomy. It risks centralizing power and weakening regional voices. Moreover, holding simultaneous elections could overwhelm voters with too many choices at once, confusing them and diluting the quality of democratic participation."""
dpm = """The government recognizes the challenges but believes the benefits outweigh the drawbacks. One nation, one election will promote uniformity and reduce the policy paralysis caused by staggered elections. It will help the bureaucracy work more efficiently without frequent transfers and interruptions. Coordination between central and state governments will improve, fostering greater political stability, which is vital for long-term economic growth."""
dlo = """One nation, one election is a flawed approach that disregards the complexity of Indian democracy. The diversity of India’s states requires elections to reflect local aspirations independently. Forcing synchronization risks undermining minority interests and regional parties, which are essential for representing diverse communities. Moreover, logistical challenges and increased electoral malpractices are inevitable when holding multiple elections simultaneously."""
gw = """We support the government’s stance. Combining elections will not only save huge amounts of public money but also reduce the burden on security forces deployed during elections. It will lessen disruptions in administration and education as election time often leads to school closures and loss of working days. A synchronized election cycle will help in the long-term planning and implementation of development policies across states."""
ow = """The opposition strongly opposes the motion. The proposal threatens to erode the checks and balances essential for democracy. It concentrates power in the hands of the central government and sidelines opposition voices. Furthermore, there is no guarantee that synchronized elections will increase voter participation or reduce expenses as claimed. It may even discourage political debate and reduce accountability."""

# Combine all speeches into one input string with labels for the model
all_speeches_text = f"""
Prime Minister: {pm}

Leader of Opposition: {ol}

Deputy Prime Minister: {dpm}

Deputy Leader of Opposition: {dlo}

Government Whip: {gw}

Opposition Whip: {ow}
"""

# System prompt with only instructions, NOT including speeches
system_prompt = """
You are an expert summarizer specialized in the Asian Parliamentary debate format.

You will receive a single input that contains the speeches of six debate members, each clearly labeled, for example:

Prime Minister: [speech text]
Leader of Opposition: [speech text]
Deputy Prime Minister: [speech text]
Deputy Leader of Opposition: [speech text]
Government Whip: [speech text]
Opposition Whip: [speech text]

Your task is to:

1. Identify each speaker by their label.
2. For each speech, generate exactly 10 detailed bullet points summarizing the key arguments, evidence, rebuttals, and important ideas.
3. Each bullet point must be distinct, insightful, and concise.
4. Avoid repeating any ideas.
5. Format the output exactly like this:

Prime Minister:
- Bullet point 1
- Bullet point 2
- ...
- Bullet point 10

Leader of Opposition:
- Bullet point 1
- ...
- Bullet point 10

Deputy Prime Minister:
- Bullet point 1
- ...
- Bullet point 10

Deputy Leader of Opposition:
- Bullet point 1
- ...
- Bullet point 10

Government Whip:
- Bullet point 1
- ...
- Bullet point 10

Opposition Whip:
- Bullet point 1
- ...
- Bullet point 10

Make sure the summary is clear, professional, and helpful for debate preparation and review.
"""

def Speech_Gen(all_speeches_text: str):
    model = Sambanova(
        is_conversation=True,
        timeout=1000000,
        max_tokens=8028,
        intro=system_prompt,
        system_prompt=system_prompt,
        model='Meta-Llama-3.1-8B-Instruct',
        api_key="8bb1f2ae-f908-42cb-878e-cafacb8fb893"
    )

    console.print("[bold green]Generating summaries...[/bold green]")
    summary = model.chat(all_speeches_text)
    console.print("\n[bold yellow]Debate Summary with Bullet Points:[/bold yellow]\n")
    print(summary)

if __name__ == "__main__":
    # Directly use the prepared speeches string, no input loop needed
    Speech_Gen(all_speeches_text)