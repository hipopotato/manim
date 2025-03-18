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
        #self.scene3(axes,y_label,x_label,origin,origin_label,sz,tt,grid)
        self.scene4(axes, y_label, x_label, origin, origin_label, sz, tt, grid)


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

        # Adicionando rótulos aos eixos
        x_label = MathTex("x").next_to(new_axes, RIGHT)
        y_label = MathTex("y").next_to(new_axes, UP)

        # Textos explicativos
        texto10 = Tex('Para representar um polígono no plano cartesiano, podemos associar seus vértices a pares ordenados, unir esses pontos com segmentos de reta e, por fim, pintar o interior da figura.').shift(UP * 3).scale(0.5)

        # Definição manual dos pontos do polígono no plano cartesiano
        p0 = new_axes.c2p(-5, 2)
        p1 = new_axes.c2p(3, 4)
        p2 = new_axes.c2p(6, -3)
        p3 = new_axes.c2p(-2, -5)

        # Criando o polígono
        poligono = Polygon(p0, p1, p2, p3, p0, color=YELLOW, fill_color=YELLOW, fill_opacity=0.2)

        # Criando pontos manualmente
        ponto_0 = Dot(p0, color=RED)
        ponto_1 = Dot(p1, color=RED)
        ponto_2 = Dot(p2, color=RED)
        ponto_3 = Dot(p3, color=RED)

        # Criando rótulos manualmente com as coordenadas
        rotulo_0 = MathTex("(-5,2)").scale(sz).next_to(p0, UP)
        rotulo_1 = MathTex("(3,4)").scale(sz).next_to(p1, UP)
        rotulo_2 = MathTex("(6,-3)").scale(sz).next_to(p2, DOWN)
        rotulo_3 = MathTex("(-2,-5)").scale(sz).next_to(p3, DOWN)

        # Criando as linhas perpendiculares aos eixos
        ponto_p0_anim_x = DashedLine(new_axes.c2p(-5, 2), new_axes.c2p(-5, 0), color=PINK)
        ponto_p0_anim_y = DashedLine(new_axes.c2p(-5, 2), new_axes.c2p(0, 2), color=PINK)
        ponto_p1_anim_x = DashedLine(new_axes.c2p(3, 4), new_axes.c2p(3, 0), color=PINK)
        ponto_p1_anim_y = DashedLine(new_axes.c2p(3, 4), new_axes.c2p(0, 4), color=PINK)
        ponto_p2_anim_x = DashedLine(new_axes.c2p(6, -3), new_axes.c2p(6, 0), color=PINK)
        ponto_p2_anim_y = DashedLine(new_axes.c2p(6, -3), new_axes.c2p(0, -3), color=PINK)
        ponto_p3_anim_x = DashedLine(new_axes.c2p(-2, -5), new_axes.c2p(-2, 0), color=PINK)
        ponto_p3_anim_y = DashedLine(new_axes.c2p(-2, -5), new_axes.c2p(0, -5), color=PINK)

        # Adicionando ao cenário
        self.play(Write(texto10))
        self.play(FadeIn(new_axes), FadeIn(new_grid), Write(x_label), Write(y_label), run_time=2)
        self.play(Create(poligono), run_time=1)
        
        self.play(FadeIn(ponto_0), Write(rotulo_0), FadeIn(ponto_p0_anim_x, ponto_p0_anim_y), run_time=tt)
        self.play(FadeIn(ponto_1), Write(rotulo_1), FadeIn(ponto_p1_anim_x, ponto_p1_anim_y), run_time=tt)
        self.play(FadeIn(ponto_2), Write(rotulo_2), FadeIn(ponto_p2_anim_x, ponto_p2_anim_y), run_time=tt)
        self.play(FadeIn(ponto_3), Write(rotulo_3), FadeIn(ponto_p3_anim_x, ponto_p3_anim_y), run_time=tt)
        self.wait(2)
        self.clear()

    def scene4(self, axes, y_label, x_label, origin, origin_label, sz, tt, grid):
        # Criando eixos e grid
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

        # Adicionando rótulos aos eixos
        x_label = MathTex("x").next_to(new_axes, RIGHT)
        y_label = MathTex("y").next_to(new_axes, UP)

        # Texto explicativo
        texto = Tex('Ampliação e redução de figuras planas no plano cartesiano').shift(UP * 3).scale(0.6)

        # Definição dos pontos dos triângulos
        A = new_axes.c2p(-2, 2)
        B = new_axes.c2p(-4, -4)
        C = new_axes.c2p(2, 4)
        tri_original = Polygon(A, B, C, color=WHITE)
        
        D = new_axes.c2p(-1, 1)
        E = new_axes.c2p(-2, -2)
        F = new_axes.c2p(1, 2)
        tri_reducao = Polygon(D, E, F, color=GREEN)
        
        G = new_axes.c2p(-4, 4)
        H = new_axes.c2p(-8, -8)
        I = new_axes.c2p(4, 8)
        tri_ampliado = Polygon(G, H, I, color=RED)
        texto12=Tex('Triângulo ABC').shift(LEFT * 3.5).scale(0.6)
        texto13=Tex('Ampliação do r"\\" Triângulo ABC').shift(LEFT * 3).scale(0.6)
        texto14=Tex('Redução do Triângulo ABC').shift(LEFT * 3).scale(0.6)
        # Animações
        self.play(Write(texto))
        self.play(FadeIn(new_axes), FadeIn(new_grid), Write(x_label), Write(y_label), run_time=2)
        self.play(Create(tri_original),Write(texto12), run_time=2)
        self.play(FadeOut(texto12), run_time=1)
        self.wait(1)
        self.play(Transform(tri_original, tri_ampliado), Write(texto13))
        self.wait(2)
        self.wait(2)
