import streamlit as st
import importlib
import requests
from io import BytesIO
from PIL import Image, ImageDraw

# Função para arredondar a imagem
def make_rounded(image):
    image = image.convert("RGBA")
    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)
    width, height = image.size
    radius = min(width, height) // 3
    center = (width // 2, height // 2)
    draw.ellipse([center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius], fill=255)
    mask = mask.convert("L")
    rounded_image = Image.new("RGBA", image.size)
    rounded_image.paste(image, (0, 0), mask=mask)
    return rounded_image

# Função para mostrar o conteúdo da página selecionada


def show_pages(page_name):

 # Mapeia o nome da página para o módulo

    modules={
        'Início':'inicio',
        'Projetos':'projetos',
        'Contatos':'contatos',
        'Sobre':'sobre',
    }
    
    modulo_name = modules.get(page_name)
    if modulo_name:
        module =importlib.import_module(modulo_name)

      #  Assumindo que o módulo tenha uma função `run` para executar o conteúdo

        if hasattr(module, 'run'):
            module.run()
        else:
            st.write("o módulo não tem uma função 'run' para exibir o conteúdo. ")
    else:
        st.write('Página não encontrada.')
# criando aba de navegação

page = st.sidebar.selectbox(
    'Navegação',
    ['Inicio','Sobre',
    'Projetos','Contatos']
)

# Exibe o conteúdo da página selecionada ou a página inicial

if page == "Inicio":

    # Carrega a imagem e aplica a função para torná-la arredondada
    
    url = 'https://i.postimg.cc/6pgG3rns/richard-image.jpg'
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))

    # Arredondar a imagem
    rounded_image = make_rounded(image)

    # Exibe a imagem arredondada
    st.image(rounded_image, caption="Rcihard Sivla Murila", use_column_width=False, width=150)

    st.title('Potifólio')
    st.write("""
    Eu sou o Richard técnico em TI




    """)
else:
    show_pages(page)