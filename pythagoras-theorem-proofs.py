from manim import *

class SquareInTriangles(MovingCameraScene):
    def construct(self):
        math_scale_value = 1.5
        title_text = Tex(r"\textsc{Pythagoras Theorem}", font_size=65)
        title_text.shift([3.5, 8.5, 0])
        bottom_left, top_right = Dot([-2, -1, 0]), Dot([9, 9, 0])
        group = VGroup(bottom_left, top_right)
        self.play(self.camera.auto_zoom(group, margin=1, animate=True),
                  run_time=0.1)

        rightTriangle1 = VGroup(Polygon([0, 0, 0], [4, 0, 0], [0, 3, 0], color=PURPLE),
                                Elbow(width=0.5, color=PURPLE))
        rightTriangle2 = VGroup(Polygon([4, 3, 0], [4, 0, 0], [0, 3, 0], color=PURPLE),
                                Elbow(width=0.5, angle=PI, color=PURPLE).shift([4,3,0]))
        rightTriangle3 = rightTriangle1.copy()
        rightTriangle4 = rightTriangle2.copy()
        square = Polygon([4,0,0], [7, 4, 0], [3, 7, 0], [0, 3, 0], color=PURPLE)
        a_text = MathTex("a", color=PURPLE)
        b_text = MathTex("b", color=PURPLE)
        c_text = MathTex("c", color=PURPLE)
        a_text.next_to(rightTriangle1, LEFT).scale(math_scale_value)
        b_text.next_to(rightTriangle1, DOWN).scale(math_scale_value)
        c_text.shift([1.5, 1.5, 0]).scale(math_scale_value)

        self.play(GrowFromEdge(rightTriangle1, LEFT))
        self.play(Write(a_text))
        self.play(Write(b_text))
        self.play(Write(c_text))
        self.play(Write(title_text), run_time=2)

        self.play(GrowFromEdge(rightTriangle2, RIGHT))
        self.wait(0.5)
        self.play(Rotate(rightTriangle2, angle=-PI/2, about_point=[4, 0, 0]))
        # a_other_selection = a_text.copy()
        # a_other_selection.next_to(rightTriangle2, DOWN)
        self.play(Write(a_text.copy().next_to(rightTriangle2, DOWN)))

        self.play(GrowFromEdge(rightTriangle4, UP))
        self.wait(0.5)
        self.play(Rotate(rightTriangle4, angle=PI/2, about_point=[0, 3, 0]))
        # b_other_selection = b_text.copy()
        # b_other_selection.next_to(rightTriangle4, LEFT)
        self.play(Write(b_text.copy().next_to(rightTriangle4, LEFT)))

        self.add(rightTriangle3)
        self.wait(0.25)
        self.play(Rotate(rightTriangle3, angle=-PI/2, about_point=[4, 0, 0]))
        self.wait(0.25)
        self.play(Rotate(rightTriangle3, angle=-PI/2, about_point=[7, 4, 0]))


        triangleArea1 = MathTex(r"{{\frac{1}{2}}} ab", color=BLUE)
        triangleArea1.shift([8, 6, 0]).scale(math_scale_value)
        triangleArea2 = MathTex(r"{{\frac{2}{2}}} ab", color=BLUE)
        triangleArea2.shift([8, 6, 0]).scale(math_scale_value)
        triangleArea3 = MathTex(r"{{\frac{3}{2}}} ab", color=BLUE)
        triangleArea3.shift([8, 6, 0]).scale(math_scale_value)
        triangleArea4 = MathTex(r"{{\frac{4}{2}}} ab", color=BLUE)
        triangleArea4.shift([8, 6, 0]).scale(math_scale_value)
        triangleAreaTotal = MathTex(r"{{2}} ab", color=BLUE)
        triangleAreaTotal.shift([8, 6, 0]).scale(math_scale_value)

        start_shade_opacity=0.2
        end_shade_opacity=0.3
        group.add(triangleArea1)
        self.play(self.camera.auto_zoom(group, margin=1, animate=True))
        self.play(rightTriangle1.animate.set_fill(BLUE, start_shade_opacity),
                  Write(triangleArea1),
                  run_time=2)
        self.play(rightTriangle2.animate.set_fill(BLUE, start_shade_opacity),
                  TransformMatchingTex(triangleArea1,triangleArea2),
                  run_time=2)
        self.play(rightTriangle3.animate.set_fill(BLUE, start_shade_opacity),
                  TransformMatchingTex(triangleArea2,triangleArea3),
                  run_time=2)
        self.play(rightTriangle4.animate.set_fill(BLUE, start_shade_opacity),
                  TransformMatchingTex(triangleArea3,triangleArea4),
                  run_time=2)
        self.wait()
        self.play(rightTriangle1.animate.set_fill(BLUE, end_shade_opacity),
                  rightTriangle2.animate.set_fill(BLUE, end_shade_opacity),
                  rightTriangle3.animate.set_fill(BLUE, end_shade_opacity),
                  rightTriangle4.animate.set_fill(BLUE, end_shade_opacity),
                  TransformMatchingTex(triangleArea4,triangleAreaTotal),
                  run_time=2)

        squareArea = MathTex(r"c^2", color=ORANGE)
        squareArea.shift([-1, 6, 0]).scale(math_scale_value)
        group.add(squareArea)
        self.play(Write(squareArea),
                  square.animate.set_fill(ORANGE, end_shade_opacity),
                  c_text.animate.set_color(ORANGE))
        self.wait()

        totalArea1 = MathTex(r"{{c^2}} + 2ab = (a+b)^2",
                             tex_to_color_map={"c^2":ORANGE,
                                               "2ab":BLUE,
                                               "(a+b)^2":PURPLE})
        totalArea2 = MathTex(r"{{c^2}} + {{2ab}} = {{a^2}} + {{2ab}} + {{b^2}}")
        totalAreaLast = MathTex(r"{{c^2}} = {{a^2}} + {{b^2}}",
                                tex_to_color_map={"c^2":ORANGE,
                                                  "a^2":PURPLE,
                                                  "b^2":PURPLE})

        totalArea1.shift([3.5, 7.5, 0]).scale(math_scale_value*1)
        totalArea2.shift([3.5, 7.5, 0]).scale(math_scale_value*0.75)
        totalAreaLast.shift([3.5, 7.5, 0]).scale(math_scale_value*1)

        self.play(Write(totalArea1), run_time=3)
        self.wait(2)
        self.play(TransformMatchingTex(totalArea1, totalArea2), run_time=3)
        self.wait()
        self.play(TransformMatchingTex(totalArea2, totalAreaLast),
                  Unwrite(squareArea), Unwrite(triangleAreaTotal), run_time=3)
        self.wait(5)
