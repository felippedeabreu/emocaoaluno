import streamlit as st


st.title("Análise de Emoções de Alunos no Ambiente Educacional")
st.write("Desenvolvido por: Felippe de Abreu")



st.sidebar.title("Navegação")
selecao = st.sidebar.radio("Ir para", ["Introdução", "Dados", "Gráficos (em breve)", "Sobre"])

if selecao == "Introdução":
    st.header("Tema: Emoções dos Alunos e Mineração de Dados Educacionais")
    st.write("Objetivo: Explorar dados emocionais para identificar padrões de comportamento e possíveis intervenções.")
elif selecao == "Dados":
    st.header("Bases de Dados Utilizadas ou Planejadas")
    st.write("Aqui será carregada a base de dados (real ou exemplo).")
elif selecao == "Gráficos (em breve)":
    st.header("Análises Visuais (em breve)")
    st.write("Esta seção trará visualizações das emoções detectadas nos alunos ao longo do tempo.")
elif selecao == "Sobre":
    st.header("Sobre o Projeto")
    st.write("Projeto desenvolvido para a disciplina de Mineração de Dados Educacionais.")
