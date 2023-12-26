import streamlit as st

def calcular_media(nota1, nota2):
    return (2 * nota1 + 3 * nota2) / 5

def calcular_nota2_para_aprovacao(nota1):
    return (5 * 60 - 2 * nota1) / 3

def calcular_media_final_opcao1(nota1, nota2, notafinal):
    return (calcular_media(nota1, nota2) + notafinal) / 2

def calcular_media_final_opcao2(nota1, nota2, notafinal):
    return (2 * notafinal + 3 * nota2) / 5

def calcular_media_final_opcao3(nota1, nota2, notafinal):
    return (2 * nota1 + 3 * notafinal) / 5

def escolher_melhor_formula(nota1, nota2, notafinal):
    opcao1 = calcular_media_final_opcao1(nota1, nota2, notafinal)
    opcao2 = calcular_media_final_opcao2(nota1, nota2, notafinal)
    opcao3 = calcular_media_final_opcao3(nota1, nota2, notafinal)

    melhores_resultados = {'1': opcao1, '2': opcao2, '3': opcao3}
    melhor_opcao = max(melhores_resultados, key=melhores_resultados.get)
    
    return melhor_opcao, melhores_resultados[melhor_opcao]

st.title('Calculadora de Notas IFRN')
st.write('Uma calculadora simples para saber se você será aprovado em alguma disciplina do IFRN. Digite suas notas nos campos abaixo e clique em "Calcular média" para ver os resultados.')
st.text('(Se aparecer uma dízima periódica, arredonde para cima)')

nota1 = st.number_input('Nota 1', min_value=0, max_value=100, step=1)
nota2 = st.number_input('Nota 2', min_value=0, max_value=100, step=1)
notafinal = st.number_input('Nota Final', min_value=0, max_value=100, step=1)

media = calcular_media(nota1, nota2)
nota2_aprovacao = calcular_nota2_para_aprovacao(nota1)

if st.button('Calcular média'):
    if media >= 60:
        st.success(f'Sua média é **{media:.0f}**. Parabéns, você foi aprovado! :sunglasses:')
    else:
        st.error(f'Sua média atual é **{media:.0f}**. :white_frowning_face:')
        st.warning(f'Para ser aprovado, você precisaria tirar **{nota2_aprovacao:.2f}** na segunda nota ou fazer a **prova final**.')

if st.button('Calcular média final'):
    melhor_opcao, media_final = escolher_melhor_formula(nota1, nota2, notafinal)
    if media_final >= 60:
        st.success(f'Sua média final usando a fórmula **{melhor_opcao}** é: **{media_final:.2f}**. Parabéns, você foi aprovado! :pray:')
    else:
        st.error(f'Sua média final usando a fórmula **{melhor_opcao}** seria: {media_final:.2f}.')

st.markdown('---')
st.header('Sobre')
st.text('Média para aprovação: 60')
st.text('Fórmula para a média: (2 * N1 + 3 * N2) / 5')
st.text('Fórmula para a média apenas com a primeira nota: (5 * 60 - 2 * N1) / 3')
st.text('Fórmulas para a média final: \n(MD + NAF) / 2\n(2 * NAF + 3 * N2) / 5\n(2 * N1 + 3 * NAF) / 5')
st.text('Para a média final é usado a fórmula que resultar na maior média.')