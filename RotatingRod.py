%%manim -qk -v WARNING RotatingRod

class RotatingRod(ThreeDScene):
    def construct(self):
        self.camera.frame_center =2.575*LEFT-0.9*UP
        self.camera.background_color = YELLOW_A
        self.set_camera_orientation(phi = 75*DEGREES, theta = -30*DEGREES, gamma = 1.2*DEGREES,zoom = 1)
        #xyz =ThreeDAxes(axis_config = {"color" : RED_E})
        #self.add(xyz)

        h,r = 2 , 1.75
        Point_A = [0,r,h]
        Point_B = [r,0,-h]

        ball_1 = Sphere([0,0,h],0.1).set_color(RED)
        ball_2 = Sphere([0,0,-h],0.1).set_color(RED)
        Support_1 = Line([0,0,h],[0,0,h+0.5],stroke_width=4,color = RED_E)
        Support = Line([0,0,h],[0,0,-h],stroke_width=5,color = RED)
        Support_2 = Line([0,0,-h],[0,0,-h-0.5],stroke_width=4,color = RED_E)
        self.add(ball_1,ball_2,Support,Support_1,Support_2)

        ball_A =Sphere(Point_A,0.05).set_color(BLUE_E).set_opacity(1)
        ball_B =Sphere(Point_B,0.05).set_color(BLUE_E).set_opacity(1)
        OA = Line([0,0,h], Point_A, color = BLUE_E).set_opacity(1)
        OB = Line([0,0,-h], Point_B, color = BLUE_E).set_opacity(1)
        AB = Line(Point_A,Point_B, color = BLUE_E).set_opacity(1)
        self.play(Create(ball_A),Create(ball_B),Create(AB),Create(OA),Create(OB), run_time = 1.5)

        svg_path = "/content/SokushiFBcolor.svg"
        sokushi = SVGMobject(svg_path).rotate_about_origin(PI*0.5,OUT).rotate_about_origin(PI*0.5,UP)
        sokushi.move_to([-13,-5,0.5]).scale(1.15)
        self.play(Create(sokushi))


        VietTex_1 = Text("Một thanh PQ có chiều dài l cm (hình). Hai thanh PS và QR",font = 'DejaVu Serif', width=12).shift(0.5*DOWN)
        VietTex_2 = Text("vuông góc nhau, mỗi thanh có cùng chiều dài là r cm, được",font = 'DejaVu Serif', width=12).shift(DOWN)
        VietTex_3 = Text("gắn cố định vuông góc với thanh PQ ở hai đầu P và Q tương",font = 'DejaVu Serif', width=12).shift(1.5*DOWN)
        VietTex_4 = Text("ứng. Hai điểm R và S được nối với nhau bằng một thanh RS.",font = 'DejaVu Serif', width=12).shift(2*DOWN)
        VietTex_5 = Text("Toàn bộ hệ thống được quay 360 độ quanh trục PQ. Tính thể ",font = 'DejaVu Serif', width=12).shift(2.5*DOWN)
        VietTex_6 = Text("tích và diện tích xung quanh của khối sinh bởi mặt đóng PQRS.",font = 'DejaVu Serif', width=12).shift(3*DOWN)
        VietTex = VGroup(VietTex_1,VietTex_2,VietTex_3,VietTex_4,VietTex_5,VietTex_6)
        # with register_font("path/to/font_file.ttf"):
        #    a = Text("Hello", font="Custom Font Name")
        VietTex.rotate_about_origin(PI*0.5,OUT).rotate_about_origin(PI*0.5,UP).set_color(MAROON_E).set_opacity(1).move_to([-10,-2.5,-1.5])
        self.play(Write(VietTex))


        P = MathTex(r"P").rotate_about_origin(PI*0.5,OUT).rotate_about_origin(PI*0.5,UP).move_to([0.25,0.25,h-0.3]).set_color(RED_E)
        Q = MathTex(r"Q").rotate_about_origin(PI*0.5,OUT).rotate_about_origin(PI*0.5,UP).move_to([0.25,0.25,-h+0.25]).set_color(RED_E)
        S = MathTex(r"S").rotate_about_origin(PI*0.5,OUT).rotate_about_origin(PI*0.5,UP).move_to([0.25,r+0.25,h+0.25]).set_color(RED_E)
        R = MathTex(r"R").rotate_about_origin(PI*0.5,OUT).rotate_about_origin(PI*0.5,UP).move_to([r+0.25,0.25,-h-0.25]).set_color(RED_E)

        self.play(Create(P),Create(Q),Create(S),Create(R))
        self.wait(2)

        # The strings are raw (r"...") so that backslashes can be used to insert LaTeX commands.
        # The minipage environment replaces the usual center environment.
        # Since minipage requires a width as an argument, that is the first LaTeX code in braces.
        EngTex = Tex(r"{0.95\textwidth}Consider a rod of length l cm, denoted by PQ. Two rods of equal length r cm, denoted by PS and QR, "
              r"are welded perpendicularly to PQ at its ends P and Q, respectively. Rods PS and QR are also perpendicular to "
              r"each other. A thin rod connects points R and S. If the entire apparatus is rotated 360 degrees about the axis RS, "
              r"what are the volume and the surrounding area of the 3D shape enclosed by the curved surface PQRS?",font_size = 41,
              tex_environment="minipage")
        EngTex.rotate_about_origin(PI*0.5,OUT).rotate_about_origin(PI*0.5,UP).set_color(BLUE_E).set_opacity(1).move_to([-13,-1.75,-5.95])
        self.play(Write(EngTex))
        self.wait(1.5)

        My_Group = VGroup(ball_A, ball_B, AB, OA, OB)
        trace_Rod = My_Group.copy().set_opacity(1)

        My_Group_2 = VGroup()
        k = 30
        for i in range (1,k):
            trace_Rod = My_Group.copy().set_color(BLUE_E).set_opacity(1)
            trace_rotate_animation = Rotating(trace_Rod, radians = TAU*(i/k),
                                              about_point = ORIGIN,
                                              about_edge = OUT, run_time = 0.1)
            self.play(trace_rotate_animation)
            My_Group_2.add(trace_Rod)

        trace_rod_WHITE = My_Group.copy().set_color(WHITE).set_opacity(1)
        trace_rotate_animation = Rotating(trace_rod_WHITE, radians = 0, about_point = ORIGIN, about_edge = OUT, run_time = 0.1)
        self.play(trace_rotate_animation)
        My_Group_2.add(trace_rod_WHITE)

        Rotateen = Rotating(My_Group_2, radians = 8*TAU, about_point = ORIGIN, about_edge = OUT, run_time = 9)
        self.play(Rotateen)
        self.wait(1)

        '''
        Xem thêm:
        https://docs.manim.community/en/stable/reference/manim.camera.mapping_camera.SplitScreenCamera.html
        https://docs.manim.community/en/stable/reference/manim.camera.mapping_camera.OldMultiCamera.html
        https://docs.manim.community/en/stable/_modules/manim/camera/mapping_camera.html#SplitScreenCamera
        https://docs.manim.community/en/stable/reference/manim.camera.mapping_camera.SplitScreenCamera.html
        https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.html
        https://docs.manim.community/en/stable/reference.html
        '''