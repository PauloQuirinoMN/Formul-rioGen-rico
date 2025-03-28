import flet as ft

class GeradorFormulario:
    def __init__(self, page: ft.Page, callback_voltar:callable):
        """
        Inicializa o gerador de formulários.
        :param page: Referência à página do Flet
        """
        self.page = page
        self.callback_voltar = callback_voltar
        self.nome_formulario = ""
        self.campos = []
        

        self.campo_nome_formulario = None
        self.campo_novo_campo = None
        self.lista_campos = None
        self.botao_adicionar = None
        self.botao_ok = None
        self.botao_cancelar = None

        self._inicializar_ui()
        self._renderizar()
    
    def _inicializar_ui(self):
        """Inicializa todos os componentes da interface do usuário"""
       
        # 1. Campo para nome do formulário
        self.campo_nome_formulario = ft.TextField(
            label="Nome do formulário",
            color=ft.Colors.WHITE38,
        )
        
        # 2. Campo para novo campo + botão adicionar
        self.campo_novo_campo = ft.TextField(
            label="Novo Campo",
            color=ft.Colors.WHITE38,
        )
        self.botao_adicionar = ft.IconButton(
            icon=ft.Icons.ADD,
            icon_color=ft.Colors.WHITE,
            icon_size=30,
            on_click=self._adicionar_campo
        )
        
        # 3. Lista visual dos campos adicionados
        self.lista_campos = ft.Column([])
        
        # 4. Botões de ação
        self.botao_ok = ft.ElevatedButton(
            text="OK",
            color=ft.Colors.WHITE,
            bgcolor=ft.Colors.BLACK,
            on_click=self._finalizar_formulario
        )
        self.botao_cancelar = ft.ElevatedButton(
            text="Cancelar",
            color=ft.Colors.WHITE,
            bgcolor=ft.Colors.BLACK,
            on_click=self._voltar_pagina_inicial
        )

    def _renderizar(self):
        """ Renderiza todos os componentes na página """
        self.page.exepand = True
        self.page.vertical_alignment = ft.alignment.center
        self.page.horizontal_alignment = ft.alignment.top_center
        self.page.clean()
        self.page.add(
            ft.Column([
                self.campo_nome_formulario,
                ft.Row([
                    self.campo_novo_campo, 
                    self.botao_adicionar,
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND),
                ft.Text(value="Campos do Formulário"),
                self.lista_campos,
                ft.Row([
                    self.botao_ok,
                    self.botao_cancelar
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
            run_spacing=20,
            )
        )
        self.page.update()


    def _adicionar_campo(self, e):
        """Adiciona um novo campo à lista de campos"""
        # 1. Validar entrada-
        if not self.campo_novo_campo.value:
            return
        # 2. Adicionar à lista self.campos
        novo_campo = self.campo_novo_campo.value
        self.campos.append(novo_campo)
        # 3. Atualizar a visualização self.lista_campos
        self.lista_campos.controls.append(
            ft.Text(novo_campo, color=ft.Colors.WHITE)
        )
        # 4. Limpar o campo de entrada
        self.campo_novo_campo.value = ""

        # Atualizar a página
        self.page.update()
        pass

    def _finalizar_formulario(self, e):
        """Finaliza a criação do formulário"""
        # 1. Validar se tem nome e pelo menos um campo
        if not self.campo_nome_formulario.value:
            self.campo_nome_formulario.error_text = "Digite um nome para o formulário"
            self.page.update()
            return

        if not self.campos:
            self.campo_novo_campo.error_text = 'Adicione pelo menos um campo',
            self.page.update()
            return

         # Salva no banco de dados
        sucesso = self.db.salvar_formulario(
            nome_formulario=self.campo_nome_formulario.value,
            campos=self.campos
        )
        
        if sucesso:
            # Mostrar mensagem de sucesso
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text("Formulário salvo com sucesso!"),
                bgcolor=ft.colors.GREEN
            )
            self.page.snack_bar.open = True
            self.page.update()
        else:
            # Mostrar mensagem de erro
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text("Erro ao salvar formulário!"),
                bgcolor=ft.colors.RED
            )
            self.page.snack_bar.open = True
            self.page.update() 
    
    # 3. Voltar à página inicial ou avançar para próxima tela
    def _voltar_pagina_inicial(self, e=None):
        """ Volta a página inicial """
        self.page.clean()
        if self.callback_voltar:
            self.callback_voltar()
        
        self.page.update()