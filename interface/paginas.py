import flet as ft
from visualizacoes.display import Display
from utilitarios.funcoes_auxiliares import Contador, GeraTipo, GeraProgresso



paleta = {
    "azul_escuro": "#000020",
    "azul_medio": "#171a4a",
    "azul_claro": "#2f2c79",
    "laranja_forte": "#ff9800",
    "laranja_fraco": "#ffcc50",
}



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

        cabecalho = ft.ListTile(
            title=ft.Text(value="Controle Financeiro", weight=ft.FontWeight.BOLD, size=20, color=paleta["azul_claro"]),
            subtitle=ft.Text(value="Ajuda Organizar as despesas pessoais", weight=ft.FontWeight.NORMAL, size=10, color=paleta["azul_claro"]),
            leading=ft.Image(src="Q.png", fit=ft.ImageFit.CONTAIN, height=100, border_radius=100)
        )
        

        comp_saldo = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(value="Saldo", weight=ft.FontWeight.BOLD, size=10, color=paleta["laranja_fraco"]),
                    ft.Row(
                        [
                            ft.Image(src="real.png", fit=ft.ImageFit.CONTAIN, height=30, border_radius=30), 
                            ft.Text(value="10,000", size=40, color=paleta["azul_claro"], weight=ft.FontWeight.BOLD, text_align=ft.alignment.center_right)
                        ], 
                        alignment=ft.MainAxisAlignment.START),
                ],
                alignment=ft.alignment.center_right,
                expand=True,
                spacing=0,
            )
        )

        botao = ft.IconButton(
            icon=ft.Icons.ADD,
            icon_size=40,
            on_click=lambda e:self._chama_formulario(), # chama o Método 2   
            icon_color=paleta["laranja_forte"],
            bgcolor=paleta["azul_claro"]
        )

        rodape = ft.Container(
            expand=True,
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
                    cabecalho,
                    ft.Row([comp_saldo, botao], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, spacing=5),
                    ft.Column([displayrs.componente], alignment=ft.MainAxisAlignment.CENTER,spacing=5, expand=True),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=30,
            )
        )

        self.page.update()
    

    def _chama_formulario(self):
        self.page.clean()
        #self.page.bgcolor = paleta["laranja_forte"]

        comp_descricao = ft.TextField(
            expand=True,
            border=ft.InputBorder.UNDERLINE,
            label="Descrição",
            label_style=ft.TextStyle(size=20, color=paleta["azul_medio"]),
        )


        
        comp_valor = ft.TextField(
            expand=True,
            border_radius=ft.border_radius.all(15),
            bgcolor=paleta["azul_claro"],
            border=ft.InputBorder.NONE,
            label="Valor",
            suffix_icon=ft.Image(src="real.png", fit=ft.ImageFit.CONTAIN,width=20,height=20, border_radius=100),
            label_style=ft.TextStyle(size=20, color=paleta["azul_medio"])
        )

        # Botões
        botoes = ft.Row(
            controls=[
                #ft.ElevatedButton("Salvar", on_click=self._salvar_formulario),
                ft.ElevatedButton(text="Voltar", color=paleta["laranja_fraco"], on_click=lambda e: self._pagina_inicial(), bgcolor=paleta["azul_medio"])
            ],
            alignment=ft.MainAxisAlignment.END
        )

        qtd = Contador()

        comp_desc_valor_qt = ft.Row(
            [
                comp_descricao,
                ft.Text(value=" X ", size=15, color=paleta["azul_medio"]),
                qtd,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=5,
            expand=True,
        )

        
        comp_forma = GeraTipo(['Dinheiro', 'Pix', 'Cartão', 'Fiado'])
        comp_categoria = GeraTipo(['Pessoais', 'Vestuário', 'Lazer', 'Educação', 'Saúde', 'Transporte', 'Alimentação', 'Moradia'])

        barra_preco = GeraProgresso(titulo="Preço")
        barra_satisfacao = GeraProgresso(titulo="Satisfação")
        barra_felicidade = GeraProgresso(titulo="Felicidade")


        formulario = ft.Container(
            content=ft.Column(
                [
                    comp_desc_valor_qt,
                    comp_valor,
                    ft.Text(value="Tipo"),
                    ft.Row([ft.TextButton(icon=ft.Icons.SAVINGS, text="Receitas"), ft.TextButton(icon=ft.Icons.MONEY_OFF, text="Despesas")], alignment=ft.MainAxisAlignment.SPACE_AROUND),
                    ft.Text(value="Forma", size=12, color=paleta["azul_claro"]),
                    comp_forma,
                    ft.Text(value="Categoria", size=12, color=paleta["azul_claro"]),
                    comp_categoria,
                    ft.Text(value="Sua Percepção"),
                    barra_preco,
                    barra_satisfacao,
                    barra_felicidade,
                    botoes,
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                spacing=15,
                scroll=ft.ScrollMode.HIDDEN,
                expand=True,
            ),
            expand=True
        )

        self.page.add(formulario)  

        self.page.update()
            