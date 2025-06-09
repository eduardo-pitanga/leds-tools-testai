from crewai import Agent, Task, Crew, Process, LLM
import os
from dotenv import load_dotenv

load_dotenv()

json = open("data.json", "r", encoding="utf-8").read()

llm_low_temp = LLM(
    #model="ollama/llama3.1:8b",
    model='gemini/gemini-1.5-flash',
    temperature=0.0,
    #base_url="http://localhost:11434"
    api_key=os.getenv("GOOGLE_API_KEY"),
)

llm_high_temp = LLM(
    #model="ollama/llama3.1:8b",
    model='gemini/gemini-1.5-flash',
    temperature=0.8,
    #base_url="http://localhost:11434"
    api_key=os.getenv("GOOGLE_API_KEY"),
)

debatedores = []

for i in range(1, 7):
    debatedor = Agent(
        role=f"Escritor de cenários Gherkin e Debatedor {i}",
        goal="""Criar cenários Gherkin compreensivos, claros e concisos para descrever o comportomaneto do sistema. 
        Propor e aprimorar soluções para os cenários criados""",
        backstory="""Esse agente tem conhecimento extensivo em behavioral-drive development e possui um entendimento profundo
                        em histórias de usuários e requisitos de sistemas. Se esforça em garantir que os cenários Gherkin descrevam
                        precisamente comportamentos do sistema esperados, fazendo que os requisitos sejam entendidos por técnicos
                        e não técnicos. Como um bom debatedor, você consegue propor soluções e apromorá-las.""",
        llm=llm_high_temp,
        verbose=True,
        allow_delegation=False
    )
    debatedores.append(debatedor)



manager = Agent(
    role="Gerente e revisor de códigos Gherkin",
    goal="Responsável por gerar a versão final dos cenários gherkin contendo os pontos positivos de todos os outros exemplos",
    backstory="""Você, no papel de um especialista em código Gherkin deve revisar os cenários gerados e produzir uma 
    versão final sem erros e com melhores pontos de cada um""",
    llm=llm_low_temp
)

tasks = []
for rodada in range(6):
    for i in range(1, 7):
        task_gherkin_code = Task(
            description=f"""
            Rodada {rodada+1}, Debatedor {i}:
            Transforme o seguinte caso de uso em arquivos BDD com cenários outlines para casos de sucesso e erro.
            Para cada atributo gerar uma mensagem de erro personalizada quando ela não for informada.
            Caso exista uma regra de integridade, gera uma mensagem de erro personalizada quando ela não for obedecida:
            {json}
            Exemplo de formato de saída:
            Scenario Outline: Incluir modalidade com sucesso
                    Given o servidor informa os dados da modalidade <sigla>, <nome>, <descrição>, <percentual>, <data_início>, <modalidades_bolsa>
                    And o servidor seleciona a resolução <resolução>
                    When o sistema valida e salva a modalidade
                    Then o sistema deve salvar a modalidade com status "Em edição"
                    
                Examples:
                    | sigla | nome | descrição | percentual | data_início | modalidades_bolsa | resolução |
                    | ABC   | Nome | Desc      | 10         | 2024-01-01  | Bolsa1            | Res1      |
            
                Scenario Outline: Incluir modalidade com erro
                    Given o servidor informa os dados da modalidade <sigla>, <nome>, <descrição>, <percentual>, <data_início>, <modalidades_bolsa>
                    And o servidor seleciona a resolução <resolução>
                    When o sistema valida e não pode salvar a modalidade
                    Then o sistema deve retornar uma mensagem de erro "<mensagem_erro>"
                    
                Examples:
                    | sigla | nome | descrição | percentual | data_início | modalidades_bolsa | resolução | mensagem_erro               |
                    | ABC   | Nome | Desc      | -10        | 2024-01-01  | Bolsa1            | Res1      | Percentual não pode ser negativo |
            Após isso, leia e reflita sobre as soluções dos outros debatedores. Atualize sua solução com base nessas reflexões.
            """,
            expected_output="ONLY the gherkin code generated without the code block like ```, DO NOT USE ANY MARKDOWN TAG",
            # context=[tasks_review1[-1]] if len(tasks_review1) > 0 else None,
            #output_file=f"solucao_debatedor{i}_rodada{rodada+1}.txt",
            agent=debatedores[i-1],
            async_execution=False
        )
        tasks.append(task_gherkin_code)




final_task = Task(
    description="""Leia e compare todos os códigos Gherkin gerados pelos debatedores e desenvolva uma versão final com base neles""",
    expected_output="ONLY the gherkin code generated without the code block like ```, DO NOT USE ANY MARKDOWN TAG",
    output_file="features/analise_evento.feature",
    agent=manager,
    async_execution=False,
    context=tasks
)


crew = Crew(
    agents=debatedores + [manager],
    tasks=tasks + [final_task],
    max_rpm=10,
    output_log_file="crew_log.txt",
    #manager_agent=manager_agent,
    manager_llm=llm_low_temp,
    process=Process.sequential,
    verbose=True,
    
)
resultado = crew.kickoff()
