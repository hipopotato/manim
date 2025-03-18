from manim import *
#manim -pql t1.py PlanoCartesiano
class PlanoCartesiano(Scene):

    def construct(self):
        sz =0.75#parametro para escala, para todos as construções terem o mesmo tamanho dentro da tela.
        tt=6 #parametro para usar dentro do runtime, que indica o tempo que vai durar a animação, parametro da função play
        # Criando o plano cartesiano
        axes = Axes(
            x_range=[-5, 5], y_range=[-5, 5], axis_config={"color": BLUE,},x_length=6.0,y_length=6.0,
        ).scale(sz)#descrição da classe axes documentação: https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.NumberPlane.html
        
        # Adicionando as labels dos eixos manualmente
        x_label = axes.get_x_axis_label("x").scale(sz)
        y_label = axes.get_y_axis_label("y").scale(sz)
        
        # Marcando a origem
        origin = Dot(axes.c2p(0, 0), color=RED)
        origin_label = MathTex("O").next_to(origin,DR)#Donw+Right
        grid = NumberPlane(x_range=[-5, 5], y_range=[-5, 5], axis_config={"stroke_color": BLUE, "stroke_width": 6},x_length=6.0,y_length=6.0).scale(sz)
        grid.set_opacity(0.4)

        #self.scene1(axes,y_label,x_label,origin,origin_label,sz,tt)
        #self.scene2(axes,y_label,x_label,origin,origin_label,sz,tt)
        self.scene3(axes,y_label,x_label,origin,origin_label,sz,tt,grid)

    def scene1(self,axes,y_label,x_label,origin,origin_label,sz,tt):
        text1=Tex('O plano cartesiano é composto de duas retas numéricas perpendiculares, chamadas de eixos.').shift(UP * 3.4).scale(sz)
        text2=Tex('O  eixo horizontal, é o eixo das abscissas ou eixo x').to_edge(DOWN).scale(sz)#shift(ajustefino, ajusta na posição para cima)
        text3=Tex('O  eixo vertical, é o eixo das ordenadas ou eixo y').to_edge(DOWN).scale(sz)
        text4=Tex('O ponto de intersecção destes dois eixos é chamado de Origem').to_edge(DOWN).scale(sz)
        self.play(Write(text1 ), run_time=2)
        self.play(FadeIn(text2 ),Create(axes.x_axis),Write(x_label), run_time=6)
        self.play(FadeOut(text2) , run_time=4)
        self.play(FadeIn(text3 ),Create(axes.y_axis),Write(y_label), run_time=6)
        self.play(FadeOut(text3) , run_time=6)
        self.play(FadeIn(text4 ),FadeIn(origin), Write(origin_label), run_time=6)
        self.play(FadeOut(text4) , run_time=6)

        self.play(FadeOut(text1,axes, origin, origin_label,y_label,x_label),run_time=1)
        self.wait(2)

    def scene2(self,axes,y_label,x_label,origin,origin_label,sz,tt,grid):
        text5=Tex('Par Ordenado').shift(UP * 3.4).scale(sz)
        text6=Tex('Um par ordenado (x,y) é dado pelas coordenadas x e y, sendo x a abscissa e y a ordenada.').to_edge(DOWN).scale(sz)
        text7=Tex('Observe o par ordenado (4,2)').to_edge(DOWN).scale(sz)
        text8=Tex('A abscissa é 4').to_edge(DOWN).scale(sz)
        text9=Tex('A ordenada é 2').to_edge(DOWN).scale(sz)
        self.play(FadeIn(text5 ),Create(axes),Write(x_label),Write(y_label), run_time=2)
        # Adicionando as grades
        self.play(FadeIn(grid))
        self.play(FadeIn(text6), run_time=6)
        self.play(FadeOut(text6 ), run_time=2)
        self.play(FadeIn(text7 ), run_time=2)
        self.wait(2)
        self.play(FadeOut(text7 ), run_time=2)
        ponto_p_anim_x= Line(axes.c2p(0, 0), axes.c2p(4, 0), color=GREEN)
        ponto_p_anim_x1= DashedLine(axes.c2p(4, 0), axes.c2p(4, 2), color=PINK)
        ponto_p_anim_y = Line(axes.c2p(0, 0), axes.c2p(0, 2), color=PINK)
        ponto_p_anim_y1=DashedLine(axes.c2p(0, 2), axes.c2p(4, 2), color=GREEN)#DashedLine linha traçejada
        
        pontop1=Dot(axes.c2p(4,0),color=YELLOW)
        pontop2=Dot(axes.c2p(0,2),color=YELLOW).scale(sz)
        ponto_p = Dot(axes.c2p(4, 2), color=YELLOW)
        ponto_p_label = MathTex("(4, 2)").next_to(ponto_p, RIGHT)
        pontopx_label = MathTex("4").next_to(pontop1,DOWN)
        pontopy_label = MathTex("2").next_to(pontop2,LEFT)
        self.play(FadeIn(text8),Create(ponto_p_anim_x),FadeIn(pontop1),FadeIn(pontopx_label), run_time=4)
        self.play(FadeOut(text8), run_time=4)
        self.play(FadeIn(text9),Create(ponto_p_anim_y),FadeIn(pontop2),FadeIn(pontopy_label), run_time=4)
        self.play(FadeOut(text9), run_time=4)
        # Marcando a linha no eixo X primeiro
        # Aumento do tempo para a animação ficar mais devagar
        self.play(Create(ponto_p_anim_x1), run_time=tt)
        self.play(Create(ponto_p_anim_y1), run_time=tt)

        # Marcando o ponto final P
        self.play(FadeIn(ponto_p))
        self.play(Write(ponto_p_label))

        self.wait(2)

    def scene3(self, axes, y_label, x_label, origin, origin_label, sz, tt, grid):
            # Criando um novo plano cartesiano com intervalo de -10 a 10
            new_axes = Axes(
            x_range=[-10, 10], y_range=[-10, 10],
            axis_config={"color": BLUE}, x_length=6.0, y_length=6.0
            ).scale(sz)

            new_grid = NumberPlane(
            x_range=[-10, 10], y_range=[-10, 10],
            axis_config={"stroke_color": BLUE, "stroke_width": 6},
            x_length=6.0, y_length=6.0
            ).scale(sz)
            new_grid.set_opacity(0.4)

            # Definição dos pontos do polígono no plano cartesiano
            pontos = [
            new_axes.c2p(-5, 2),
            new_axes.c2p(3, 4),
            new_axes.c2p(6, -3),
            new_axes.c2p(-2, -5),
            new_axes.c2p(-5, 2)  # Voltando ao ponto inicial para fechar o polígono
            ]

            # Criando o polígono
            poligono = Polygon(*pontos, color=YELLOW)

            # Criando pontos e rótulos
            pontos_obj = [Dot(p, color=RED) for p in pontos[:-1]]  # Último ponto é repetido
            rotulos = [
            MathTex(f"P_{i}").next_to(p, UP if i % 2 == 0 else DOWN)
            for i, p in enumerate(pontos[:-1])
            ]

            # Adicionando ao cenário
            self.play(FadeIn(new_axes), FadeIn(new_grid), run_time=2)
            self.play(Create(poligono), run_time=tt)

            for ponto, rotulo in zip(pontos_obj, rotulos):
                self.play(FadeIn(ponto), Write(rotulo), run_time=tt / 2)
            self.wait(2)
