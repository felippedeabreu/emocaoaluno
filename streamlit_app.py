import streamlit as st




# Menu lateral
st.sidebar.title("Navegação")
pagina = st.sidebar.radio("Escolha uma seção:", 
                          ["Introdução", "Base de Dados", "Visualizações", "Futuras Expansões"])

# Conteúdo das páginas
if pagina == "Introdução":
    st.header("Introdução")


    st.title("Análise de Emoções em Alunos")
    st.write("Pós-graduação em Mineração de Dados Educacionais")
    st.write("Instituto Federal do Espírito Santo - Campus Serra")
    st.write("Professor: Maxwell Monteiro")
    st.write("Disciplina: Ferramentas e Soluções em Núvem")
    st.write("Autor: Felippe de Abreu")
    st.write("""
        Este app tem como objetivo analisar as emoções dos alunos
        e relacioná-las com possíveis problemas de desempenho e risco de evasão escolar.
    """)

elif pagina == "Base de Dados":
    st.header("Base de Dados")
    st.write("""
        Neste projeto, inicialmente serão utilizadas duas abordagens:
        - Um conjunto de imagens simuladas de expressões faciais (feliz, medo, nervoso, neutro, nojo e triste);
        - Bases públicas como **FER2013** (reconhecimento de emoções) e **Student Performance Dataset** (UCI).
    """)
    st.write("No futuro, os dados coletados de alunos reais poderão ser integrados.")


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

