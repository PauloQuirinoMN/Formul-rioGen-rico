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
            bgcolor=paleta["azul_escuro"],
            expand=True,
            content=ft.Tabs(
                expand=True,
                label_padding=10,
                indicator_tab_size=True,
                indicator_padding=1,
                label_color=paleta["laranja_fraco"],
                divider_height=2,
                divider_color=paleta["laranja_forte"],
                indicator_thickness=2,
                tab_alignment=ft.TabAlignment.CENTER,
                selected_index=0,
                animation_duration=300,
                tabs=[
                    ft.Tab(
                        tab_content=ft.Image(src="inf2.jpg", border_radius=100),
                        content=ft.Text(
                        value="Bem-vindo ao Controle Financeiro\n"
                        "O objetivo: ajudar organizar as despesas\n"
                        "Como usar:\n"
                        "1. Clique em '+' para começar\n"
                        "2. Preencha os campos\n"
                        "3. Salve o registro!\n"
                        "4. Terá análise inicial de seus dados!\n",
                        size=15,
                        color=paleta["azul_claro"],
                        text_align=ft.alignment.center,
                        )
                    ),
                    ft.Tab(
                        tab_content=ft.Image(src="ideia.jpg", border_radius=100),
                        content=ft.Text("resumo", color=paleta["laranja_fraco"])
                    ),
                    ft.Tab(
                        tab_content=ft.Image(src="ans.jpg", border_radius=100),
                        content=ft.Text("análise dados", color=paleta["laranja_fraco"])
                    ),
                    ft.Tab(
                        tab_content=ft.Image(src="anl.jpg", border_radius=100),
                        content=ft.Text("powerbi", color=paleta["laranja_fraco"])
                    ),
                ],

                
            )
        )
            