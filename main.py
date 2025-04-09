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
    page.title = "Q_Soluções"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = ft.Colors.WHITE
    page.padding = ft.padding.all(10)
    page.expand = True



    # O gerenciador de páginas recebe 
    # a página e a instância do bando de dados
    GerenciadorPaginas(page) 




ft.app(target=main, assets_dir='assets')
