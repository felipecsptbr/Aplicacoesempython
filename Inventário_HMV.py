import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados do arquivo Excel
file_path = (
    r"Caminho_do_arquivo"
)
df = pd.read_excel(file_path)

# Dicionário de emojis para marcas
emoji_dict = {
    "HP": "",
    "Dell": "",
    "Lenovo": "",
    "Megaware": "",
    "PCware": "",
    "Itautec S.A.": "",
}

# Configurar página para largura total
st.set_page_config(layout="wide")

# Barra lateral com opção de menu usando radio
selected_page = st.sidebar.radio(
    "Selecione uma Página",
    ["🏠 Página Inicial", "🔍 Consulta de Dados", "📊 Estatísticas"],
)

# Página Inicial
if "Página Inicial" in selected_page:
    st.image(
        "http://hospitalmestrevitalino.com.br//images/loghmv.png", width=100
    )  # Substitua pelo URL ou caminho da sua imagem
    st.title("Consulta de Inventário de Máquinas")

    st.markdown(
        """
        Esta aplicação permite a consulta do inventário de máquinas do Hospital Mestre Vitalino (HTRI). 
        Você pode visualizar informações sobre as máquinas com base na marca e explorar estatísticas gerais.

        **Instruções:**
        - Selecione 'Consulta de Dados' no menu para explorar as máquinas por marca.
        - Selecione 'Estatísticas' para ver estatísticas gerais com base nos dados.

        Sinta-se à vontade para explorar e analisar os dados disponíveis!
        """
    )

# Página de Consulta de Dados
elif "Consulta de Dados" in selected_page:
    st.title("Consulta de Dados por Marca")

    # Verificar se as colunas 'HOST' e 'MARCA' existem no DataFrame
    if "HOST" in df.columns and "MARCA" in df.columns:
        # Obter a lista única de marcas
        marcas = df["MARCA"].unique()

        # Criar um menu com as marcas
        selected_marca = st.selectbox(
            "Selecione uma Marca", ["Selecione uma Marca"] + list(marcas)
        )

        # Mostrar dados apenas se uma marca válida for selecionada
        if selected_marca and selected_marca != "Selecione uma Marca":
            # Filtrar o DataFrame pela marca selecionada
            filtered_df = df[df["MARCA"] == selected_marca]

            # Adicionar emojis ao lado do nome das marcas
            emoji = emoji_dict.get(selected_marca, "")
            info_header = f"🖥️ {emoji} Informações de Máquinas  {selected_marca}"
            st.subheader(info_header)
            st.table(filtered_df[["HOST", "MARCA"]])
        else:
            st.info("Selecione uma marca para visualizar os dados.")
    else:
        st.error("Erro: Os dados não contêm as colunas 'HOST' e 'MARCA'.")

# Página de Estatísticas
else:
    st.title("Estatísticas Gerais")

    # Gráfico de barras mostrando a quantidade de máquinas por marca
    fig = px.bar(
        df["MARCA"].value_counts(),
        x=df["MARCA"].value_counts().index,
        y=df["MARCA"].value_counts().values,
        labels={"y": "Quantidade", "x": "Marca"},
    )
    fig.update_layout(
        title="Quantidade de Máquinas por Marca",
        xaxis_title="Marca",
        yaxis_title="Quantidade",
    )
    st.plotly_chart(fig)
