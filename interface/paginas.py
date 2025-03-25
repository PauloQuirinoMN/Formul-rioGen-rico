import flet as ft
from servicos.criacao import CriadorFormulario


class GerenciadorFormulario:
    def __init__(self, page: ft.Page):
        """
        Inicializa o gerenciador do app.
        :param page: Referência à pagina do flet (obrogatório para atualizar a UI)
        """
        self.page = page
        self.CriadorFormulario(page) #Armazena os dados do formulário sendo criado
        self._pagina_inicial() # Renderiza a primeira página auto

    def _pagina_inicial(self):
        # ------------------------------------------------------------
        # Método 1: Página Inicial (Tutorial + Botão criar formulário)
        # ------------------------------------------------------------
        titulo = ft.Text(
            value="Bem-vindo ao gerador de Formulário",
            size=30,
            weight=ft.FontWeight.BOLD,            
        )

        instrucoes = ft.Text(
            value="Como usar:\n"
            "1. Clique em 'Novo Formulário' para começar\n"
            "2. Defina o nome e os campos\n"
            "3. Salve e use seu formulário personalizado!"
            "você pode adicionar, alterar, limpar e excluir dados e o formulário",
            size=12,
            color=ft.Colors.WHITE12,
        )

        botao = ft.ElevatedButton(
            text="Novo Formulário",
            on_click=CriadorFormulario, # chama o Método 2   
        )

        self.page.clean()
        # Organiza os elementos na página
        self.page.add(
            ft.Column(
                expand=True,
                controls=[
                    titulo,
                    instrucoes,
                    ft.Row([botao], alignment=ft.MainAxisAlignment.CENTER), 
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=30,
            )
        )
        self.page.update()
    

