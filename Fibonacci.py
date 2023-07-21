'''
Various Fibonacci sequence related animations, particularly to find recurrences of related or derived sequences.
'''
from manim import *

class EvenFibonacci(MovingCameraScene):
    def construct(self):
        tex_font_size = 60
        title_text=Tex(r"\textsc{Recurrence for Even Fibonacci Numbers}",
                       font_size=tex_font_size+10)

        d = {"font_size": 60, "color": BLACK}
        E_list = [MathTex("{{E_{n-"+str(i)+"}}}", **d)
                  for i in range(2, 0, -1)] + [MathTex("E_n", **d)]
        Es = VGroup(*E_list)

        F_list = [MathTex("F_{3n-"+str(i)+"}", **d)
                  for i in range(6, 0, -1)] + [MathTex("F_{3n}", **d)]
        Fs = VGroup(*F_list)

        del d["color"]
        NullMob = MathTex("")
        t = MobjectTable(
            [[Es[0], NullMob.copy(), NullMob.copy(),
              Es[1], NullMob.copy(), NullMob.copy(), Es[2]],
             [F_list[0], F_list[1], F_list[2],
              F_list[3], F_list[4], F_list[5], F_list[6]]])
        t.remove(*t.get_vertical_lines())
        t.remove(*t.get_horizontal_lines())
        title_text.next_to(t.get_top()+6*UP+7.5*LEFT)

        self.play(self.camera.auto_zoom([t, Es, Fs, title_text, Dot(t.get_bottom()+3.5*DOWN)],
                                        margin=2, animate=True), run_time=0.1)
        self.play(Write(title_text), FadeIn(t))
        for i, f in enumerate(reversed(F_list)):
            self.play(f.animate.set_color(BLUE), run_time=0.2)
        self.fibonacci_text = MathTex(r"F_n = F_{n-1} + F_{n-2}",
                                 color=BLUE, **d).next_to(t.get_top()+4*UP+LEFT)
        self.play(Write(self.fibonacci_text))
        self.wait(0.5)
        self.play(GrowFromPoint(E_list[-1].set_color(RED), F_list[-1].get_center()))
        self.play(GrowFromPoint(E_list[1].set_color(RED), F_list[3].get_center()))
        self.play(GrowFromPoint(E_list[0].set_color(RED), F_list[0].get_center()))
        self.wait()
        even_text = MathTex(r"E_n = {{\dots}}",
                            color=RED, **d).next_to(t.get_top()+2*UP+LEFT)
        self.play(Write(even_text))
        self.wait()

        tally = Dot(F_list[-1].get_bottom()+DOWN)
        self.play(Indicate(E_list[-1]),
                  Indicate(F_list[-1]),
                  Create(tally))
        self.wait()
        l1, r1 = self.split(F_list[-1], F_list[-2], F_list[-3], tally)
        l2, r2 = self.split(F_list[-3], F_list[-4], F_list[-5], l1)
        l3, r3 = self.split(F_list[-2], F_list[-3], F_list[-4], r1,
                            l_down_factor=2, r_down_factor=1)
        l4, r4 = self.split(F_list[-5], F_list[-6], F_list[-7], l2)
        l5, r5 = self.split(F_list[-3], F_list[-4], F_list[-5], r3,
                            r_down_factor=3)

        unsplit_point = self.unsplit(F_list[-6], F_list[-5], F_list[-4],
                                     r4, l5, down_factor=4)

        # Rearrangements finished

        # Box 1
        one_box = SurroundingRectangle(VGroup(l4, E_list[0]), buff=0.25)
        self.play(Create(one_box))
        one_text = MathTex(r"1\cdot {{E_{n-2}}}", color=RED, **d).next_to(E_list[0].get_left()+LEFT)
        self.play(TransformMatchingTex(E_list[0], one_text),
                  Uncreate(one_box), run_time=2)
        self.wait()

        # Other box
        four_box = SurroundingRectangle(VGroup(unsplit_point, E_list[1]), buff=0.25)
        self.play(Create(four_box))
        four_text = MathTex(r"4\cdot {{E_{n-1}}}", color=RED, **d).next_to(E_list[1].get_left()+LEFT)
        self.play(TransformMatchingTex(E_list[1], four_text),
                  Uncreate(four_box), run_time=2)
        self.wait()

        # Writing recurrence
        even_text_final = MathTex(r"E_n = {{4\cdot E_{n-1}}} + {{E_{n-2}}}", color=RED, **d).align_to(even_text, LEFT).align_to(even_text, DOWN)
        self.play(TransformMatchingTex(even_text, even_text_final),
                  Indicate(one_text, scale_factor=1.5),
                  Indicate(four_text, scale_factor=1.5),
                  run_time=4)
        self.play(even_text_final.animate.scale(1.5),
                  VGroup(*F_list[1:3], *F_list[4:6], l1, l2, l5,
                         r1, r3, r4).animate.set_opacity(0.1),
                  self.fibonacci_text.animate.set_opacity(0.5))
        self.wait(2)

    def split(self, f2, f1, f0, point,
              l_down_factor=1, r_down_factor=1, time=1, factor=1):
        left, right = point, point.copy()
        new_left_point = Dot(f0.get_bottom()+l_down_factor*0.5*DOWN, color=GREEN)
        new_right_point = Dot(f1.get_bottom()+r_down_factor*0.5*DOWN, color=GREEN)

        self.add(TracedPath(left.get_center,
                            stroke_color=left.get_color(), dissipating_time=1),
                 TracedPath(right.get_center,
                            stroke_color=right.get_color(), dissipating_time=1))
        self.play(Indicate(self.fibonacci_text, color=GREEN, scale_factor=1.1),
                  Indicate(left, color=GREEN, scale_factor=2.5),
                  Indicate(right, color=GREEN, scale_factor=2.5))
        self.play(ReplacementTransform(left, new_left_point,
                                       path_func=utils.paths.clockwise_path()),
                  ReplacementTransform(right, new_right_point,
                            path_func=utils.paths.clockwise_path()),
                  run_time=time/factor)
        self.play(new_left_point.animate.set_color(WHITE),
                  new_right_point.animate.set_color(WHITE),
            Uncreate(left), Uncreate(right), run_time=0.1)
        self.wait()
        return new_left_point, new_right_point

    def unsplit(self, f0, f1, f2, point1, point2,
                down_factor=1, time=1, factor=1):
        unsplit_point = Dot(f2.get_bottom()+down_factor*0.5*DOWN, color=GREEN)
        # left, right = point, point.copy()
        # new_left_point = Dot(f0.get_bottom()+l_down_factor*0.5*DOWN, color=GREEN)
        # new_right_point = Dot(f1.get_bottom()+r_down_factor*0.5*DOWN, color=GREEN)

        self.add(TracedPath(point1.get_center,
                            stroke_color=point1.get_color(), dissipating_time=1),
                 TracedPath(point2.get_center,
                            stroke_color=point2.get_color(), dissipating_time=1))
        self.play(Indicate(self.fibonacci_text, color=GREEN, scale_factor=1.1),
                  Indicate(point1, color=GREEN, scale_factor=2),
                  Indicate(point2, color=GREEN, scale_factor=2))
        self.play(ReplacementTransform(point1, unsplit_point,
                                       path_func=utils.paths.counterclockwise_path()),
                  ReplacementTransform(point2, unsplit_point,
                            path_func=utils.paths.counterclockwise_path()),
                  run_time=time/factor)
        self.play(unsplit_point.animate.set_color(WHITE),
                  Uncreate(point1), Uncreate(point2), run_time=0.1)
        self.wait()
        return unsplit_point
