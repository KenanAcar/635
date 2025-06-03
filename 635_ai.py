
from langchain_community.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import time

# User-defined problem
problem_statement = "Evlerde enerji verimliliğini arttırmak için neler yapılmalı? Cevaplar Türkçe olmalı!"
ai_model ="gemma3:1b"
ollama_base_url="http://localhost:11434"
# Define personas
personas = [
    ("girişimci", "Sen, ölçeklenebilir iş fikirlerine odaklanan pratik bir girişimcisin. Yalnızca bir cümleyle ve Türkçe cevap ver!"),
    ("düşünür", "Sen, fikirlerin etik ve ahlaki sonuçlarıyla ilgilenen derin bir düşünürsün. Yalnızca bir cümleyle ve Türkçe cevap ver!"),
    ("fütürist", "Sen, dünyanın 50 yıl sonra nasıl görünebileceğini hayal eden bir fütüristsin. Yalnızca bir cümleyle ve Türkçe cevap ver!"),
    ("mühendis", "Sen, teknik uygulanabilirliğe önem veren, detay odaklı bir mühendissin. Yalnızca bir cümleyle ve Türkçe cevap ver!"),
    ("çevreci", "Sen, sürdürülebilirlik ve çevresel etki konusunda derin endişeler taşıyan bir çevrecisin. Yalnızca bir cümleyle ve Türkçe cevap ver!"),
    ("sanatçı", "Sen, her zaman zamanının ötesinde fikirlere sahip yaratıcı bir sanatçısın. Yalnızca bir cümleyle ve Türkçe cevap ver!")
]


# Dictionary to hold all markdown tables
all_markdown_tables = []

# Run for each persona as initiator
for initiator_index, (initiator_name, initiator_prompt) in enumerate(personas):
    print(f"\n🚀 Initiator: {initiator_name}")
    table = []  # Holds rows of the table

    # Row 0: Problem statement
    table.append(["", "", ""])
    
    # Row 1: Initial ideas (initiator generates 3)
    table.append(["**İlk fikirler**"] * 3)
    row1 = []
    for i in range(3):
        prompt = PromptTemplate(
            input_variables=["problem"],
            template=f"You are {initiator_name}. {initiator_prompt}\n\nProblem: {{problem}}\n\nPlease propose one innovative solution in one sentence only."
        )
        chain = LLMChain(llm=Ollama(model=ai_model, base_url=ollama_base_url), prompt=prompt)
        idea = chain.run(problem=problem_statement).strip()
        print(f"✍️  Initial Idea {i+1}: {idea}")
        row1.append(idea)
        time.sleep(1)
    table.append(row1)

    # Rows 2–5: Improvement by others
    current_ideas = row1.copy()
    for round_num in range(4):
        improver_index = (initiator_index + round_num + 1) % len(personas)
        improver_name, improver_prompt = personas[improver_index]
        print(f"🔁 Round {round_num+1} by: {improver_name}")
        row = []
        for col in range(3):
            prompt = PromptTemplate(
                input_variables=["idea"],
                template=f"You are {improver_name}. {improver_prompt}\n\nImprove this idea in one sentence only:\n\"{{idea}}\""
            )
            chain = LLMChain(llm=Ollama(model=ai_model, base_url=ollama_base_url), prompt=prompt)
            new_idea = chain.run(idea=current_ideas[col]).strip()
            print(f"   💡 Col {col+1}: {new_idea}")
            new_idea_by = f"**{improver_name}:** {new_idea}"
            row.append(new_idea_by)
            time.sleep(1)
        table.append(row)
        current_ideas = row.copy()

    # Row 6: Finalization by initiator
    row = []
    for col in range(3):
        idea_chain = "\n".join([f"- {table[i][col]}" for i in range(2, 7)])
        prompt = PromptTemplate(
            input_variables=["ideas"],
            template=f"You are {initiator_name}.\n\nHere is a chain of evolved ideas:\n{{ideas}}\n\nPlease finalize it in one sentence only in Turkish!"
        )
        chain = LLMChain(llm=Ollama(model=ai_model, base_url=ollama_base_url), prompt=prompt)
        final_idea = chain.run(ideas=idea_chain).strip()
        print(f"✅ Finalized Col {col+1}: {final_idea}")
        row.append(final_idea)
        time.sleep(1)
    table.append(["**Fikirlerin birleştirilmiş hali**"] * 3)
    table.append(row)

    # Convert table to markdown manually
    markdown = f"## Tablo -> {initiator_name.capitalize()}\n\n"
    markdown += "| Fikir 1 | Fikir 2 | Fikir 3 |\n"
    markdown += "|--------|--------|--------|\n"
    for r in table:
        markdown += "|" + "|".join(r) + "|\n"
    all_markdown_tables.append(markdown)

# Save final markdown output
markdown_path="ideation_output.md"
new_filename = f"{markdown_path.rsplit('.', 1)[0]}_{__import__('datetime').datetime.now().strftime('%Y-%m-%d_%H-%M')}.md"

print("\n📄 Saving all tables to Markdown...")
with open(new_filename, "w", encoding="utf-8") as f:
    f.write("# 6-3-5 Ideation Summary\n\n")
    f.write(f"**Problem:** {problem_statement}\n\n\n")
    f.write("\n\n".join(all_markdown_tables))

print(f"✅ Markdown file saved to {new_filename}")
