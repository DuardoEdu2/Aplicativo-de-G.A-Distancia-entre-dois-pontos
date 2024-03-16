import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

#st.title cria um titulo centralizado com uma fonte grande em negrito
st.title("Calculadora de distância entre dois pontos")

#st.markdown cria um texto em markdown mas com o unsafe_allow_html=True permite ser escrito em html
st.markdown("<h3>Informe a posição dos dois pontos específicos para que a distância seja calculada</h3>", unsafe_allow_html=True)

#st.text cria um texto
st.text("Posição do primeiro ponto:")
Px1 = st.number_input("Digite o valor de x1") #st.text_input cria um campo onde o ususario pode digitar um texto
Py1 = st.number_input("Digite o valor de y1") #st.number_input cria um campo onde o ususario pode digitar um numero float

st.text("Posição do segundo ponto:")
Px2 = st.number_input("Digite o valor de x2")
Py2 = st.number_input("Digite o valor de y2")


if st.button("Verificar"):
    #calculo da distancia entre dois pontos
    distancia = np.sqrt((Px2 - Px1)**2 + (Py2 - Py1)**2)
    
    #passo a passo da equação mostrada acima
    st.write("Passo a passo da equação:") #st.write pode exibir uma string e um valor de alguma variavel
    st.latex(r"\text{Distância} = \sqrt{(x2 - x1)^2 + (y2 - y1)^2}") #st.latex exibi expressoes matematicas formatadas
    st.latex(r"\text{Distância} = \sqrt{(" + str(Px2) + " - " + str(Px1) + ")^2 + (" + str(Py2) + " - " + str(Py1) + ")^2}")
    st.latex(r"\text{Distância} = \sqrt{(" + str(Px2 - Px1) + ")^2 + (" + str(Py2 - Py1) + ")^2}")
    st.latex(r"\text{Distância} = \sqrt{" + str((Px2 - Px1)**2) + " + " + str((Py2 - Py1)**2) + "}")
    st.latex(r"\text{Distância} = \sqrt{" + str((Px2 - Px1)**2 + (Py2 - Py1)**2) + "}")
    st.write("A distância entre os dois pontos é:", distancia)
    st.write("A distância entre os dois pontos arredondada:", np.round(distancia))

    #Usando a biblioteca matplotlib com o submodulo .pyplot criamos o grafico dos dois pontos conectados
    plt.figure(figsize=(8, 6))
    plt.plot([Px1, Px2], [Py1, Py2], marker='o')
    plt.title("Gráfico dos Pontos e Segmento de Linha")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.grid(True)

    #adiciona linhas adiconais oara formar um triangulo rentagulo para um melhor entedimento
    plt.plot([Px2, Px2], [Py1, Py2], linestyle='--', color='blue')
    plt.plot([Px1, Px2], [Py1, Py1], linestyle='--', color='blue')

    st.pyplot(plt)
        
    if st.button("Limpar"):
        st.write("A tela foi limpa")
        plt.clf()
        plt.close()
        st.write("A tela foi limpa")