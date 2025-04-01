import flet as ft
from visualizacoes.display import Display

class GerenciadorPaginas:
    def __init__(self, page: ft.Page):
        """
        Inicializa o gerenciador do app.
        :param page: Referência à pagina do flet (obrigatório para atualizar a UI)
        
        """
        self.page = page
        self._pagina_inicial()
        
        

    def _pagina_inicial(self):
        # ------------------------------------------------------------
        # Método 1: Página Inicial (Tutorial + Botão criar formulário)
        # ------------------------------------------------------------



        titulo = ft.Text(
            value="Bem-vindo ao Controle Financeiro",
            size=25,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.WHITE,            
        )

        instrucoes = ft.Text(
            value="Como usar:\n"
            "1. Clique em 'Nova transação' para começar\n"
            "2. Preencha os campos\n"
            "3. Salve o registro!\n"
            "4. Veja um resumo dos seus registros!\n"
            "5. Uma análise inicial de seus dados!\n"
            "6. Exportar para seu dispositivo!\n"
            "você pode adicionar, alterar, limpar e excluir dados do seu banco de dados!",
            size=12,
            color=ft.Colors.WHITE38,
        )

        botao = ft.ElevatedButton(
            text="Nova Transação",
            on_click=lambda e:self._chama_formulario(), # chama o Método 2   
            color=ft.Colors.BLACK38,
        )

        rodape = ft.Container(
            content=ft.Row(
            controls=[
                ft.IconButton(
                content=ft.Image(
                    src='001-instagram.png', height=15, color=ft.Colors.WHITE,     
                ),
                url='https://www.instagram.com/pauloqneto/',
                ),
                ft.IconButton(
                    content=ft.Image(
                        src='002-linkedin.png', height=15, color=ft.Colors.WHITE,   
                    ),
                    url='https://www.linkedin.com/feed/',
                ),
                ft.IconButton(
                    content=ft.Image(
                        src='003-github.png', height=15, color=ft.Colors.WHITE,
                           
                    ),
                    url='https://github.com/PauloQuirinoMN',
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
        ))


        # instância do display
        displayrs = Display(page=self.page)

        self.page.clean()
        # Organiza os elementos na página
        self.page.add(
            ft.Column(
                expand=True,
                controls=[
                    titulo,
                    instrucoes,
                    ft.Row([botao], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(controls=[]),
                    displayrs.componente,
                    rodape,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=30,
            )
        )
        self.page.update()
    

    def _chama_formulario(self):
        self.page.clean()

        self.comp_descricao = ft.TextField(
            label="Descrição",
        )

        self.comp_qt = ft.Container(
            alignment=ft.alignment.center,
            expand=True,
            padding=0,
            content=ft.Row(
                controls=[
                    ft.Text(value='1', size=20, color=ft.Colors.WHITE),
                    ft.Column(
                        controls=[
                            ft.Icon(name=ft.Icons.EXPAND_LESS, size=30, color=ft.Colors.WHITE38),
                            ft.Icon(name=ft.Icons.EXPAND_MORE, size=30, color=ft.Colors.WHITE38),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=0,
                    )
                ],
                alignment=ft.alignment.center
            )
        )

        # Botões
        botoes = ft.Row(
            controls=[
                #ft.ElevatedButton("Salvar", on_click=self._salvar_formulario),
                ft.ElevatedButton("Voltar", on_click=lambda e: self._pagina_inicial())
            ],
            alignment=ft.MainAxisAlignment.END
        )

        

        formulario = ft.Column(
            controls=[  # Lista de controles diretamente aqui
                ft.Row(
                    controls=[self.comp_descricao, self.comp_qt],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                ),
                ft.Container(expand=True),  # Espaço vazio simplificado
                botoes
            ],
            expand=True,
            spacing=20,
        )

        self.page.add(formulario)  

        self.page.update()
            