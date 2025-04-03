import flet as ft
from interface.paginas import GerenciadorPaginas


paleta = {
    "azul_escuro": "#000020",
    "azul_medio": "#171a4a",
    "azul_claro": "#2f2c79",
    "laranja_forte": "#ff9800",
    "laranja_fraco": "#ffcc50",
}

def main(page: ft.Page):
    page.title = "FormuláriosDinâmicos"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = "#ff9800"
    page.padding = ft.padding.all(20)



    # O gerenciador de páginas recebe 
    # a página e a instância do bando de dados
    GerenciadorPaginas(page) 




ft.app(target=main, assets_dir='assets')
