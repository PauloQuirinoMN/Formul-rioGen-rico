import flet as ft
from servicos.criacao import GeradorFormulario


class GerenciadorPaginas:
    def __init__(self, page: ft.Page):
        """
        Inicializa o gerenciador do app.
        :param page: Referência à pagina do flet (obrogatório para atualizar a UI)
        """
        self.page = page
        
        logica_telas = 0
        if logica_telas == 0:
            self._pagina_inicial() # Renderiza a primeira página.
        else:
            GeradorFormulario(self.page) # Renderiza a página de formulário

    def _pagina_inicial(self):
        # ------------------------------------------------------------
        # Método 1: Página Inicial (Tutorial + Botão criar formulário)
        # ------------------------------------------------------------
        titulo = ft.Text(
            value="Bem-vindo ao gerador de Formulário",
            size=30,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.WHITE,            
        )

        instrucoes = ft.Text(
            value="Como usar:\n"
            "1. Clique em 'Novo Formulário' para começar\n"
            "2. Defina o nome e os campos\n"
            "3. Salve e use seu formulário personalizado!"
            "você pode adicionar, alterar, limpar e excluir dados e o formulário",
            size=12,
            color=ft.Colors.WHITE38,
        )

        

        botao = ft.ElevatedButton(
            text="Novo Formulário",
            on_click=lambda e:GeradorFormulario(self.page), # chama o Método 2   
            color=ft.Colors.BLACK38
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
    

        
        