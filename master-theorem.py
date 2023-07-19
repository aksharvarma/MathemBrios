from manim import *

class MasterTheorem(MovingCameraScene):
    def construct(self):
        text = MathTex(r"\xrightarrow{\hspace*{3em}} T(n) = a \cdot T\left(\frac{n}{b}\right) + n^c")

        title_text = Tex(r"\textsc{Master Theorem}", font_size=60)
        title_text.shift(text.get_center() + [-1, 2, 0])
        master_text = Tex(r"Asymptotic analysis of\\the runtime recurrence\\for recursive algorithms\\with input size $n$ and\\constants $c,\, a \geq 1,\, b > 1$",
                          tex_environment='raggedright', font_size=40)
        master_text.shift(title_text.get_corner(LEFT+DOWN) + [-2, -2.25, 0])
        self.add(title_text)
        self.wait()
        auto_zoom_group = VGroup(title_text, master_text)
        self.play(Write(master_text, run_time=7),
                  self.camera.auto_zoom(auto_zoom_group, margin=1, animate=True))
        self.wait()
        self.play(Write(text),
                  self.camera.auto_zoom([title_text, master_text,
                                         text], margin=1, animate=True))
        # self.add(index_labels(text[0]))
        arrow_selection = text[0][:11]
        master_text_a_selection = master_text[0][90:93]
        a_selection = text[0][11]
        a_color = RED
        master_text_b_selection = master_text[0][94:]
        b_selection = text[0][17]
        b_color = BLUE
        recursion_selection = text[0][11:19]
        nb_selection = text[0][15:18]
        master_text_c_selection = master_text[0][88]
        c_selection = text[0][21]
        c_color = GREEN
        split_recombine_selection = text[0][20:]

        a = SurroundingRectangle(a_selection, buff = .05, color=a_color)
        a_other = SurroundingRectangle(master_text_a_selection, buff = .05, color=a_color)
        self.play(Create(a), Create(a_other),
                  master_text_a_selection.animate.set_color(a_color),
                  a_selection.animate.set_color(a_color))
        a_text = Text("Number of subproblems", font_size=16, color=a_color)
        a_text.next_to(a, UP, buff=0.5)
        self.play(FadeIn(a_text),
                  self.camera.auto_zoom([title_text, master_text,
                                         text, a, a_text], margin=1, animate=True))

        b = SurroundingRectangle(b_selection, buff = .05, color=b_color)
        b_other = SurroundingRectangle(master_text_b_selection, buff = .05, color=b_color)
        b_full = SurroundingRectangle(nb_selection, buff = .1, corner_radius=0.1)
        self.play(Create(b), Create(b_other), Create(b_full),
                  master_text_b_selection.animate.set_color(b_color),
                  b_selection.animate.set_color(b_color))
        b_full_text = Text("Size of subproblems", font_size=16, color=b_color)
        b_full_text.next_to(b_full, DOWN, buff = .5)
        self.play(FadeIn(b_full_text),
                  self.camera.auto_zoom([title_text, master_text,
                                         text, a, a_text, b, b_full_text],
                                        margin=1, animate=True))


        c = SurroundingRectangle(c_selection, buff = .05, color=c_color)
        c_other = SurroundingRectangle(master_text_c_selection, buff = .05, color=c_color)
        ck = SurroundingRectangle(split_recombine_selection, corner_radius=0.1)
        self.play(Create(c), Create(c_other), Create(ck),
                  master_text_c_selection.animate.set_color(c_color),
                  c_selection.animate.set_color(c_color))
        ck_text = Text("Split/Recombine work", font_size=16, color=c_color)
        ck_text.next_to(ck, UP, buff=0.2)
        self.play(FadeIn(ck_text),
                  self.camera.auto_zoom([title_text, master_text,
                                         text, a, b, c, ck_text], margin=1, animate=True))
        self.wait()

        self.play(FadeOut(a_text, scale=0.25),
                  FadeOut(b_full_text, scale=0.25),
                  FadeOut(ck_text, scale=0.25),
                  Uncreate(a), Uncreate(a_other),
                  master_text_a_selection.animate.set_color(WHITE),
                  a_selection.animate.set_color(WHITE),
                  Uncreate(b), Uncreate(b_other),
                  master_text_b_selection.animate.set_color(WHITE),
                  b_selection.animate.set_color(WHITE),
                  Uncreate(b_full),
                  Uncreate(c), Uncreate(c_other),
                  master_text_c_selection.animate.set_color(WHITE),
                  c_selection.animate.set_color(WHITE),
                  Uncreate(ck),)


        recursion_brace = Brace(recursion_selection, direction=[0, 1, 0], buff=0.1)
        recursion_brace_text = recursion_brace.get_text("Recursion")
        recursion_brace_text.move_to(recursion_brace.get_corner(UP+LEFT) + [-0.5, 0.3, 0])

        split_recombine_brace = Brace(split_recombine_selection, direction=[0, 1, 0], buff=0.1)
        split_recombine_brace_text = split_recombine_brace.get_text("Split/Recombine")
        split_recombine_brace_text.move_to(split_recombine_brace.get_corner(UP+RIGHT) + [1.5, 0.3, 0])

        unfocus_group = VGroup(title_text, master_text, arrow_selection)

        self.play(Create(recursion_brace), Write(recursion_brace_text),
                  unfocus_group.animate.set_color(GRAY_E),
                  self.camera.auto_zoom([text, recursion_brace, recursion_brace_text],
                                        margin=1, animate=True))
        self.wait()
        self.play(Create(split_recombine_brace), Write(split_recombine_brace_text),
                  self.camera.auto_zoom([text, recursion_brace, recursion_brace_text,
                                         split_recombine_brace, split_recombine_brace_text],
                                        margin=1, animate=True))
        self.wait()

        c_crit_vs_c = MathTex(r"\log_b a \text{  vs.  } c")
        c_crit_vs_c.next_to(text, DOWN, buff=1)
        a_other_selection = c_crit_vs_c[0][4]
        b_other_selection = c_crit_vs_c[0][3]
        c_other_selection = c_crit_vs_c[0][-1]

        unfocus_group = VGroup(title_text, master_text, arrow_selection,
                          recursion_brace, recursion_brace_text,
                          split_recombine_brace, split_recombine_brace_text)

        self.play(Write(c_crit_vs_c),
                  unfocus_group.animate.set_color(GRAY_E),
                  self.camera.auto_zoom([text, c_crit_vs_c], margin=0.25, animate=True),
                  c_crit_vs_c.animate.scale(1.5))

        self.play(Circumscribe(a_selection, Rectangle, fade_out=True, color=a_color,
                               run_time=2),
                  Circumscribe(a_other_selection, Rectangle, fade_in=True, color=a_color,
                               run_time=2),
                  a_selection.animate.set_color(a_color),
                  a_other_selection.animate.set_color(a_color))
        self.wait()
        self.play(Circumscribe(b_selection, Rectangle, fade_out=True, color=b_color,
                               run_time=2),
                  Circumscribe(b_other_selection, Rectangle, fade_in=True, color=b_color,
                               run_time=2),
                  b_selection.animate.set_color(b_color),
                  b_other_selection.animate.set_color(b_color))
        self.wait()
        self.play(Circumscribe(c_selection, Rectangle, fade_out=True, color=c_color,
                               run_time=2),
                  Circumscribe(c_other_selection, Rectangle, fade_in=True, color=c_color,
                               run_time=2),
                  c_selection.animate.set_color(c_color),
                  c_other_selection.animate.set_color(c_color))
        self.wait()

        case_1_words = Text("Recursion bigger", font_size=30)
        case_1 = MathTex(r"\log_{b} a > c")
        case_1_solution = MathTex(r"\Theta(n^{\log_b a})")

        case_2_words = Text("Recursion smaller", font_size=30)
        case_2 = MathTex(r"\log_{b} a < c")
        case_2_solution = MathTex(r"\Theta(n^c)")

        case_3_words = Text("Draw", font_size=30)
        case_3 = MathTex(r"\log_{b} a = c")
        case_3_solution = MathTex(r"\Theta(n^c \log n)")


        cases = MobjectTable([[case_1_words, case_1.scale(1.5), case_1_solution.scale(1.5)],
                              [case_2_words, case_2.scale(1.5), case_2_solution.scale(1.5)],
                              [case_3_words, case_3.scale(1.5), case_3_solution.scale(1.5)]],
                             col_labels=[Text("Intuition"), Text("Condition"), Text("Solution")],
                             arrange_in_grid_config={"cell_alignment": LEFT})
        cases.remove(*cases.get_vertical_lines())
        cases.get_horizontal_lines().set_color(GRAY)
        cases.next_to(c_crit_vs_c, DOWN, buff=0.3)

        self.play(unfocus_group.animate.set_color(WHITE),
                  self.camera.frame.animate.move_to(case_2_words),
                  self.camera.auto_zoom([title_text, master_text,
                                         text, c_crit_vs_c,
                                         recursion_brace, recursion_brace_text,
                                         split_recombine_brace, split_recombine_brace_text,
                                         case_1_words, case_2_words, case_3_words],
                                        margin=1, animate=True))

        master_text_a_selection.set_color(a_color),
        master_text_b_selection.set_color(b_color),
        master_text_c_selection.set_color(c_color),
        cases.scale(0.75).set_color(BLACK)
        self.add(cases)


        for num, row in enumerate(cases.get_rows()):
            if num==0:
                self.play(row.animate.scale(1.25).set_color(PINK))
                self.play(Circumscribe(row[0], Rectangle, True, True, run_time=4),
                          Circumscribe(recursion_brace_text, Rectangle, True, True, run_time=4),
                          Circumscribe(split_recombine_brace_text, Rectangle, True, True, run_time=4))
                self.play(Circumscribe(row[1], Rectangle, True, True, run_time=4),
                          Circumscribe(c_crit_vs_c, Rectangle, True, True, run_time=4))
                self.play(row.animate.scale(4/5).set_color(WHITE))
            else:

                # self.play(row[1:].animate.set_color(GRAY_B),
                #           ApplyWave(row))
                self.play(VGroup(row[1:]).animate.scale(1.6).set_color("#FF00FF"))
                self.wait()
                if num==1:
                    self.play(row[1][0][5:].animate.set_color(GRAY_B),
                              row[2][0][0:3].animate.set_color(GRAY_B),
                              row[2][0][8:].animate.set_color(GRAY_B))
                elif num==2:
                    self.play(row[1][0][:6].animate.set_color(GRAY_B),
                              row[2][0][0:3].animate.set_color(GRAY_B),
                              row[2][0][4:].animate.set_color(GRAY_B))
                else:
                    self.play(row[1][0][:6].animate.set_color(GRAY_B),
                              row[2][0][0:3].animate.set_color(GRAY_B),
                              row[2][0][4:8].animate.set_color(GOLD_E),
                              row[2][0][8].animate.set_color(GRAY_B),)
                self.wait()
                self.play(VGroup(row[1:]).animate.scale(2/3),
                          row[0].animate.set_color(GRAY_B))
                # self.add(index_labels(row[1][0]))
                # self.add(index_labels(row[2][0]))
        self.wait(5)
