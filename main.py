import flet as ft
from interface.paginas import GerenciadorPaginas

def main(page: ft.Page):
    # page.title = "FormuláriosDinâmicos"
    # page.horizontal_alignment = "center"
    # page.vertical_alignment = "center"
    # page.bgcolor = ft.Colors.BLACK12
    # page.padding = ft.padding.all(20)
    # GerenciadorPaginas(page) # gerencia as telas e os seus widgts
    # Exemplo 2: Simular formulário existente (sem banco de dados)
    criador = GerenciadorPaginas(page)
    # criador.nome_formulario = "Cadastro Rápido"  # Simula dados existentes
    # criador.campos = ["Nome Completo", "Data Nasc.", "CPF"]
    # criador.renderizar_formulario_existente()  # Renderiza diretamente




ft.app(target=main)
