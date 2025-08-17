import streamlit as st


st.set_page_config(page_title="Análise de Emoções em Alunos", page_icon="📊")


# Menu lateral
st.sidebar.title("Navegação")
pagina = st.sidebar.radio("Escolha uma seção:", 
                          ["Introdução", "Base de Dados", "Visualizações", "Futuras Expansões"])

# Conteúdo das páginas
if pagina == "Introdução":
    st.header("Introdução")

    st.title("Análise de Emoções em Alunos")

    st.markdown("""
    Esta aplicação apresenta um projeto desenvolvido como parte da avaliação da disciplina 
    de **Ferramentas e Soluções em Nuvem** na Pós-graduação em **Mineração de Dados Educacionais** do **Instituto Federal do Espírito Santo - Campus Serra**.

    **Professor:** Maxwell Monteiro  
    **Aluno:** Felippe de Abreu  

    ---
    ### Objetivo do Projeto
    O objetivo é criar um painel interativo para visualização e análise das emoções dos alunos, 
    buscando identificar padrões emocionais que possam estar relacionados ao desempenho acadêmico 
    e ao risco de evasão escolar.

    ---
    ### Fonte dos Dados
    Para este protótipo inicial, estão sendo utilizados:
    - **Dataset simulado** contendo expressões faciais (feliz, medo, nervoso, neutro, nojo e triste), 
      junto com indicadores de frequência e desempenho escolar;
    - Bases públicas como **FER2013** (reconhecimento de emoções) e **Student Performance Dataset** (UCI), 
      que poderão ser integradas em versões futuras.
    """)


elif pagina == "Base de Dados":
    st.header("Base de Dados")
    st.write("""
        Neste projeto, inicialmente serão utilizadas duas abordagens:
        - Um conjunto de imagens simuladas de expressões faciais (feliz, medo, nervoso, neutro, nojo e triste);
        - Bases públicas como **FER2013** (reconhecimento de emoções) e **Student Performance Dataset** (UCI).
    """)
    st.write("No futuro, os dados coletados de alunos reais poderão ser integrados.")



elif pagina == "TESTES":
    st.header("TESTES")
    st.write("""
        TESTES
    """)
    st.write("")
    
    
    import pandas as pd

    # Carregar dataset
    df = pd.read_csv("alunos_emocoes_100.csv")

    st.header("Exemplo de Base de Dados")
    st.dataframe(df)

    # Exemplo de gráfico: distribuição das emoções
    st.subheader("Distribuição das Emoções")
    st.bar_chart(df["expressao"].value_counts())


    

elif pagina == "Visualizações":
    st.header("Visualizações")
    st.write("Aqui serão apresentados gráficos interativos, por exemplo:")
    st.bar_chart({"Feliz": 12, "Triste": 5, "Medo": 3, "Neutro": 20, "Nojo": 2, "Nervoso": 8})

elif pagina == "Futuras Expansões":
    st.header("Futuras Expansões")
    st.write("""
        - Aplicação de modelos de Machine Learning para identificar emoções automaticamente;
        - Correlação entre emoções, desempenho acadêmico e evasão escolar;
        - Dashboard interativo com filtros por turma, disciplina e período.
    """)

