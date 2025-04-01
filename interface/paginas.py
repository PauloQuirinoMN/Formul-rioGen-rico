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
            size=20,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.WHITE,            
        )

        sub_titulo = ft.Text(
            value=("O objetivo: ajudar organizar as despesas"),
            size=10,
            weight=ft.FontWeight.W_500,
            color=ft.Colors.WHITE,            
        )

        instrucoes = ft.Text(
            value="Como usar:\n"
                "1. Clique em '+' para começar\n"
                "2. Preencha os campos\n"
                "3. Salve o registro!\n"
                "4. Terá análise inicial de seus dados!\n",
            size=10,
            color=ft.Colors.WHITE38,
        )

        botao = ft.IconButton(
            icon=ft.Icons.ADD,
            icon_size=40,
            on_click=lambda e:self._chama_formulario(), # chama o Método 2   
            icon_color=ft.Colors.BLACK38,
            bgcolor=ft.Colors.WHITE38
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
                    sub_titulo,
                    instrucoes,
                    ft.Row([botao], alignment=ft.MainAxisAlignment.END),
                    ft.Row(controls=[]),
                    displayrs.componente,
                    rodape,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=5,
            )
        )
        self.page.update()
    

    def _chama_formulario(self):
        self.page.clean()



        comp_descricao = ft.TextField(
            label="Descrição",
        )

        comp_qt = ft.Container(
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


        comp_valor = ft.Container(
            content=ft.Row([
                ft.TextField(label=0.00, text_size=45, color=ft.Colors.WHITE),
                ft.Text(value="R$", color=ft.Colors.WHITE, size=35)
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND)
        )
        # comp_tipo = ft.Container(
        #     content=ft.Row(
        #         [
        #             ft.IconButton(icon=ft.Icons.)
        #         ],
        #         alignment=ft.MainAxisAlignment.SPACE_AROUND)
        # )
        comp_categoria = ft.Container()
        comp_perc_preço = ft.Container()
        comp_necessidade = ft.Container()
        comp_felicidade = ft.Container()
        comp_data_hora = ft.Container()

        
        # Botões
        botoes = ft.Row(
            controls=[
                #ft.ElevatedButton("Salvar", on_click=self._salvar_formulario),
                ft.ElevatedButton("Voltar", on_click=lambda e: self._pagina_inicial())
            ],
            alignment=ft.MainAxisAlignment.END
        )


        formulario = ft.Column(
            controls=[ 
                ft.Row(
                    controls=[
                        comp_descricao, 
                        comp_qt,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                ),
                comp_valor,

                botoes,
            ],
            expand=True,
            spacing=20,
        )

        self.page.add(formulario)  

        self.page.update()
            