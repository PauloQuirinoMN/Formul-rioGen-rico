import flet as ft

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
                scrollable=False,
                indicator_tab_size=True,
                indicator_padding=2,
                label_color=ft.Colors.WHITE,
                divider_height=2,
                indicator_thickness=2,
                tab_alignment=ft.TabAlignment.CENTER,
                selected_index=0,
                animation_duration=300,
                tabs=[
                    ft.Tab(
                        icon=ft.Icon(ft.Icons.ABC, size=30),
                        content=ft.Text(
                        value="Bem-vindo ao Controle Financeiro\n"
                        "O objetivo: ajudar organizar as despesas\n"
                        "Como usar:\n"
                        "1. Clique em '+' para começar\n"
                        "2. Preencha os campos\n"
                        "3. Salve o registro!\n"
                        "4. Terá análise inicial de seus dados!\n",
                        size=10,
                        color=ft.Colors.WHITE38,)
                    ),
                    ft.Tab(
                        tab_content=ft.Icon(ft.Icons.EXIT_TO_APP, size=30),
                        content=ft.Text("resumo", color='white')
                    ),
                    ft.Tab(
                        tab_content=ft.Icon(ft.Icons.EXIT_TO_APP, size=30),
                        content=ft.Text("análise dados", color='white')
                    ),
                    ft.Tab(
                        tab_content=ft.Icon(ft.Icons.AC_UNIT, size=30),
                        content=ft.Text("powerbi", color='white')
                    ),
                ],

                
            )
        )
            