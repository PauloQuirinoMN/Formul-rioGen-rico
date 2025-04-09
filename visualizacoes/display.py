import flet as ft



paleta = {
    "azul_escuro": "#000020",
    "azul_medio": "#171a4a",
    "azul_claro": "#2f2c79",
    "laranja_forte": "#ff9800",
    "laranja_fraco": "#ffcc50",
}


class Display:
    """Inicializa o display com menus de acesso """
    def __init__(self, page: ft.Page):
        self.expand = True
        self.page = page
        self.componente = self._menu_display()

        
    def _menu_display(self):
        """Tab para gerenciamneto de conteúdo """
        return  ft.Container(
            expand=True,
            content=ft.Tabs(
                expand=True,
                label_padding=10,
                scrollable=False,
                indicator_tab_size=True,
                indicator_padding=1,
                label_color=paleta["laranja_fraco"],
                divider_height=2,
                divider_color=paleta["laranja_forte"],
                indicator_thickness=2,
                tab_alignment=ft.TabAlignment.FILL,
                selected_index=0,
                animation_duration=300,
                tabs=[
                    ft.Tab(
                        tab_content=ft.Image(src="informar.png", border_radius=100),
                        content=ft.Text(
                            value=
                            "Como usar:\n"
                            "1. Clique em '+' para começar\n"\
                            "2. Preencha os campos\n"\
                            "3. Salve o registro!\n"\
                            "4. Terá análise inicial de seus dados!\n"\
                            "\n" \
                            "📱 Seu Controle Financeiro Inteligente" \
                            "Este app foi desenvolvido para transformar " \
                            "a maneira como você organiza suas finanças pessoais, combinando praticidade e inteligência de dados." \
                            "",
                            size=15,
                            color=paleta["azul_claro"],
                            text_align=ft.alignment.center,
                        )
                    ),
                    ft.Tab(
                        tab_content=ft.Image(src="resumo.png", border_radius=100),
                        content=ft.Text("resumo", color=paleta["azul_claro"])
                    ),
                    ft.Tab(
                        tab_content=ft.Image(src="analise_dd.png", border_radius=100),
                        content=ft.Text("análise dados", color=paleta["azul_claro"])
                    ),
                    ft.Tab(
                        tab_content=ft.Image(src="ideia.png", border_radius=100),
                        content=ft.Text("powerbi", color=paleta["azul_claro"])
                    ),
                ],

                
            )
        )
            