"""
SKA: The Trilogy - Manim Animation
Structured Knowledge Accumulation Framework by Bouarfa Mahi, Quantiota

Requirements:
    pip install manim

Run with:
    manim -pqh ska_trilogy_animation.py SKATrilogyVideo

For lower quality preview:
    manim -pql ska_trilogy_animation.py SKATrilogyVideo
"""

from manim import *
import numpy as np

# Color palette - same as previous animations
DEEP_BLUE = ManimColor("#0a1628")
PURPLE = ManimColor("#6b5b95")
CYAN = ManimColor("#00d4ff")
SOFT_CYAN = ManimColor("#7fefff")
PINK_ACCENT = ManimColor("#ff6b9d")
WHITE_GLOW = ManimColor("#ffffff")
DIM_WHITE = ManimColor("#aaaaaa")


class NeuralField(VGroup):
    """Creates a field of glowing neural points"""

    def __init__(self, n_points=200, radius=4, **kwargs):
        super().__init__(**kwargs)

        for _ in range(n_points):
            theta = np.random.uniform(0, 2 * PI)
            phi = np.random.uniform(0, PI)
            r = np.random.uniform(0.5, radius) * np.random.uniform(0.3, 1) ** 0.5

            x = r * np.sin(phi) * np.cos(theta)
            y = r * np.sin(phi) * np.sin(theta)
            z = r * np.cos(phi) * 0.3

            point = Dot(
                point=[x, y + z, 0],
                radius=np.random.uniform(0.02, 0.06),
                color=interpolate_color(PURPLE, CYAN, np.random.uniform(0, 1)),
            ).set_opacity(np.random.uniform(0.3, 0.9))

            self.add(point)


class SKATrilogyVideo(Scene):
    """Main animation scene for SKA: The Trilogy"""

    def construct(self):
        self.camera.background_color = DEEP_BLUE

        # Run all sections
        self.intro_section()
        self.part1_foundation()
        self.part2_dynamics()
        self.part3_geometry()
        self.key_insight()
        self.unified_vision()
        self.mathematical_unity()
        self.end_card()

    def intro_section(self):
        """Intro with title and neural field background"""

        # Create neural field
        neural_field = NeuralField(n_points=250, radius=5)
        neural_field.scale(0.1).set_opacity(0)

        # Title
        title = Text(
            "Structured Knowledge Accumulation",
            font_size=40,
            color=WHITE_GLOW
        ).to_edge(UP, buff=0.8)

        subtitle = Text(
            "The Trilogy",
            font_size=48,
            color=CYAN
        ).next_to(title, DOWN, buff=0.3)

        author = Text(
            "Bouarfa Mahi • Quantiota • 2026",
            font_size=24,
            color=DIM_WHITE
        ).next_to(subtitle, DOWN, buff=0.3)


        tagline = Text(
            "Unifying Information Theory, Physics, and Geometry",
            font_size=22,
            color=SOFT_CYAN,
            slant=ITALIC
        ).next_to(author, DOWN, buff=0.5)

        # Animate intro
        self.play(
            neural_field.animate.scale(10).set_opacity(1),
            run_time=3,
            rate_func=smooth
        )

        self.play(
            FadeIn(title, shift=DOWN * 0.3),
            FadeIn(subtitle, shift=DOWN * 0.2),
            run_time=1.5
        )

        self.play(
            FadeIn(author),
            run_time=1
        )

        self.play(
            FadeIn(tagline),
            run_time=1
        )

        # Audio: 12.58s
        self.add_sound("/home/coder/project/manim_the_trilogy/audio/01_intro.mp3")
        self.wait(11)  # 12.58 - 1.5 (fadeout)

        # Clear
        self.play(
            FadeOut(title), FadeOut(subtitle), FadeOut(author), FadeOut(tagline),
            FadeOut(neural_field),
            run_time=1.5
        )

    def part1_foundation(self):
        """Part I: The Foundation - Entropy equation and weight update"""

        # Part title
        part_num = Text("Part I", font_size=32, color=PINK_ACCENT)
        part_title = Text(
            "The Foundation",
            font_size=44,
            color=WHITE_GLOW
        ).next_to(part_num, DOWN, buff=0.2)

        part_group = VGroup(part_num, part_title).move_to(ORIGIN)

        # Audio: 2.02s
        self.add_sound("/home/coder/project/manim_the_trilogy/audio/02_part1_title.mp3")
        self.play(FadeIn(part_group), run_time=1)
        self.wait(0.5)
        self.play(FadeOut(part_group), run_time=1)

        # Subtitle
        subtitle = Text(
            "Layer-Wise Entropy Reduction in Neural Learning",
            font_size=24,
            color=SOFT_CYAN
        ).to_edge(UP, buff=0.5)

        self.play(FadeIn(subtitle), run_time=0.5)

        # Audio: 14.02s
        self.add_sound("/home/coder/project/manim_the_trilogy/audio/03_part1_content.mp3")

        # Main entropy equation
        equation = MathTex(
            r"H = -\frac{1}{\ln 2} \int z \, dD",
            font_size=56,
            color=CYAN
        ).move_to(UP * 0.8)

        equation_box = SurroundingRectangle(equation, color=CYAN, buff=0.3, stroke_width=2)

        self.play(Write(equation), run_time=2)
        self.play(Create(equation_box), run_time=1)

        # Labels
        h_label = Text("H: Entropy", font_size=20, color=SOFT_CYAN)
        z_label = Text("z: Knowledge tensor", font_size=20, color=CYAN)
        d_label = Text("dD: Decision probability shift", font_size=20, color=PINK_ACCENT)

        labels = VGroup(h_label, z_label, d_label).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        labels.next_to(equation_box, DOWN, buff=0.4)

        self.play(FadeIn(labels), run_time=1)
        self.wait(10)  # Audio 03 is 14.016s: 2+1+1+10=14

        # Audio: 12.888s
        self.add_sound("/home/coder/project/manim_the_trilogy/audio/04_part1_equation.mp3")

        # Weight update rule - THE KEY ADDITION
        weight_update = MathTex(
            r"W \leftarrow W - \eta \, \nabla_{w} H",
            font_size=48,
            color=PINK_ACCENT
        ).next_to(labels, DOWN, buff=0.5)

        weight_box = SurroundingRectangle(weight_update, color=PINK_ACCENT, buff=0.2, stroke_width=2)

        self.play(Write(weight_update), run_time=2)
        self.play(Create(weight_box), run_time=1)

        # Weight update label
        update_label = Text(
            "Forward-only weight update rule",
            font_size=20,
            color=SOFT_CYAN
        ).next_to(weight_box, DOWN, buff=0.3)

        self.play(FadeIn(update_label), run_time=1)
        self.wait(7.5)  # Audio 04 is 12.888s: 2+1+1+7.5+1.5=13

        # Clear
        self.play(
            FadeOut(subtitle), FadeOut(equation), FadeOut(equation_box),
            FadeOut(labels), FadeOut(weight_update), FadeOut(weight_box),
            FadeOut(update_label),
            run_time=1.5
        )

    def part2_dynamics(self):
        """Part II: The Dynamics - Entropic Least Action"""

        # Part title
        part_num = Text("Part II", font_size=32, color=PINK_ACCENT)
        part_title = Text(
            "The Dynamics",
            font_size=44,
            color=WHITE_GLOW
        ).next_to(part_num, DOWN, buff=0.2)

        part_group = VGroup(part_num, part_title).move_to(ORIGIN)

        # Audio: 2.14s
        self.add_sound("/home/coder/project/manim_the_trilogy/audio/05_part2_title.mp3")
        self.play(FadeIn(part_group), run_time=1)
        self.wait(0.5)
        self.play(FadeOut(part_group), run_time=1)

        # Subtitle
        subtitle = Text(
            "The Principle of Entropic Least Action",
            font_size=24,
            color=SOFT_CYAN
        ).to_edge(UP, buff=0.5)

        self.play(FadeIn(subtitle), run_time=0.5)

        # Audio: 13.54s
        self.add_sound("/home/coder/project/manim_the_trilogy/audio/06_part2_content.mp3")

        # THE KEY ADDITION: η ≡ Δt reinterpretation
        eta_reinterpret = MathTex(
            r"\eta \equiv \Delta t",
            font_size=56,
            color=PINK_ACCENT
        ).move_to(UP * 1.5)

        self.play(Write(eta_reinterpret), run_time=1.5)
        self.wait(1)

        # Arrow showing transformation
        arrow_down = MathTex(r"\Downarrow", font_size=48, color=WHITE_GLOW)
        arrow_down.next_to(eta_reinterpret, DOWN, buff=0.3)
        self.play(FadeIn(arrow_down), run_time=0.5)

        # Continuous-time dynamics equation
        continuous_eq = MathTex(
            r"\frac{d{W}}{dt} + \nabla_{{w}} H = 0",
            font_size=48,
            color=CYAN
        ).next_to(arrow_down, DOWN, buff=0.3)

        continuous_box = SurroundingRectangle(continuous_eq, color=CYAN, buff=0.2, stroke_width=2)

        self.play(Write(continuous_eq), run_time=2)
        self.play(Create(continuous_box), run_time=1)

        # Label
        dynamics_label = Text(
            "Continuous-time learning dynamics",
            font_size=20,
            color=DIM_WHITE
        ).next_to(continuous_box, DOWN, buff=0.3)

        self.play(FadeIn(dynamics_label), run_time=1)
        self.wait(5.5)  # Audio 06 is 13.536s: 1.5+1+0.5+2+1+1+5.5+1=13.5

        # Clear first set
        self.play(
            FadeOut(eta_reinterpret), FadeOut(arrow_down),
            FadeOut(continuous_eq), FadeOut(continuous_box),
            FadeOut(dynamics_label),
            run_time=1
        )

        # Audio: 16.512s
        self.add_sound("/home/coder/project/manim_the_trilogy/audio/07_part2_euler.mp3")

        # Lagrangian equation
        lagrangian = MathTex(
            r"\mathcal{L}(z, \dot{z}) = -z \, \sigma(z)(1 - \sigma(z)) \, \dot{z}",
            font_size=44,
            color=CYAN
        ).move_to(UP * 1.2)

        self.play(Write(lagrangian), run_time=2)

        # Labels
        l_label = Text("L: Entropic Lagrangian", font_size=18, color=DIM_WHITE)
        l_label.next_to(lagrangian, DOWN, buff=0.3)

        self.play(FadeIn(l_label), run_time=0.5)
        self.wait(1)

        # Euler-Lagrange equation
        euler = MathTex(
            r"\frac{d}{dt}\left(\frac{\partial \mathcal{L}}{\partial \dot{z}}\right) - \frac{\partial \mathcal{L}}{\partial z} = 0",
            font_size=40,
            color=SOFT_CYAN
        ).next_to(l_label, DOWN, buff=0.4)

        self.play(Write(euler), run_time=2)
        self.wait(1)

        # Collapses to 0=0
        collapse = MathTex(r"\Rightarrow \quad 0 = 0", font_size=44, color=PINK_ACCENT)
        collapse.next_to(euler, DOWN, buff=0.3)

        self.play(Write(collapse), run_time=1)

        # Insight
        insight = Text(
            "Intrinsically optimal — a natural law of motion",
            font_size=22,
            color=SOFT_CYAN,
            slant=ITALIC
        ).to_edge(DOWN, buff=0.6)

        self.play(FadeIn(insight), run_time=1)
        self.wait(6.5)  # Audio 07 is 16.512s: 2+0.5+1+2+1+1+1+6.5+1.5=16.5

        # Clear
        self.play(
            FadeOut(subtitle), FadeOut(lagrangian), FadeOut(l_label),
            FadeOut(euler), FadeOut(collapse), FadeOut(insight),
            run_time=1.5
        )

    def part3_geometry(self):
        """Part III: The Geometry - Riemannian Neural Fields"""

        # Part title
        part_num = Text("Part III", font_size=32, color=PINK_ACCENT)
        part_title = Text(
            "The Geometry",
            font_size=44,
            color=WHITE_GLOW
        ).next_to(part_num, DOWN, buff=0.2)

        part_group = VGroup(part_num, part_title).move_to(ORIGIN)

        # Audio: 2.26s
        self.add_sound("/home/coder/project/manim_the_trilogy/audio/08_part3_title.mp3")
        self.play(FadeIn(part_group), run_time=1)
        self.wait(0.5)
        self.play(FadeOut(part_group), run_time=1)

        # Subtitle
        subtitle = Text(
            "Geodesic Learning Paths in Riemannian Neural Fields",
            font_size=24,
            color=SOFT_CYAN
        ).to_edge(UP, buff=0.5)

        self.play(FadeIn(subtitle), run_time=0.5)

        # Audio: 11.88s
        self.add_sound("/home/coder/project/manim_the_trilogy/audio/09_part3_content.mp3")

        # Metric tensor equation
        metric = MathTex(
            r"g_{ij}(\mathbf{r}) = \alpha \, (\nabla h)_i (\nabla h)_j + \beta \, (\nabla \rho)_i (\nabla \rho)_j + \gamma \, \delta_{ij}",
            font_size=36,
            color=CYAN
        ).move_to(UP * 0.5)

        self.play(Write(metric), run_time=2)

        # Labels
        g_symbol = MathTex(r"g_{ij}", font_size=28, color=SOFT_CYAN)
        g_text = Text(" : Riemannian metric", font_size=20, color=SOFT_CYAN)

        g_label = VGroup(g_symbol, g_text).arrange(RIGHT, buff=0.05)

        h_label = Text("h: Local entropy", font_size=20, color=CYAN)
        rho_label = Text("ρ: Neuron density", font_size=20, color=PINK_ACCENT)

        labels = VGroup(g_label, h_label, rho_label).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        labels.next_to(metric, DOWN, buff=0.5)

        self.play(FadeIn(labels), run_time=1)
        self.wait(9)  # 11.88 - 0.5 - 2 - 1 = 8.38  

        # Audio: 12.02s
        self.add_sound("/home/coder/project/manim_the_trilogy/audio/10_part3_geodesic.mp3")

        # Geodesic equation
        geodesic = MathTex(
            r"\frac{d^2 x^i}{dt^2} + \Gamma^i_{jk} \frac{dx^j}{dt} \frac{dx^k}{dt} = 0",
            font_size=40,
            color=SOFT_CYAN
        ).next_to(labels, DOWN, buff=0.5)

        self.play(Write(geodesic), run_time=2)

        # Insight
        insight = Text(
            "Architectures discovered, not designed",
            font_size=22,
            color=SOFT_CYAN,
            slant=ITALIC
        ).to_edge(DOWN, buff=0.5)

        self.play(FadeIn(insight), run_time=1)
        self.wait(8)  # 12.02 - 2 - 1 - 1.5 = 7.52 

        # Clear
        self.play(
            FadeOut(subtitle), FadeOut(metric), FadeOut(labels),
            FadeOut(geodesic), FadeOut(insight),
            run_time=1.5
        )

    def key_insight(self):
        """Key insight: Discrete architectures are approximations"""

        # Audio: 12.55s
        self.add_sound("/home/coder/project/manim_the_trilogy/audio/11_insight.mp3")

        # Title
        title = Text(
            "Key Insight",
            font_size=36,
            color=PINK_ACCENT
        ).to_edge(UP, buff=0.8)

        self.play(FadeIn(title), run_time=1)

        # Create visual: discrete → continuous
        # Discrete network (left)
        discrete_title = Text("Discrete", font_size=20, color=DIM_WHITE)

        # Simple layered network visualization
        layers = VGroup()
        for i in range(4):
            layer = VGroup()
            n_nodes = [3, 5, 5, 2][i]
            for j in range(n_nodes):
                node = Dot(radius=0.08, color=PURPLE)
                node.move_to([i * 1.0 - 1.5, (j - n_nodes/2 + 0.5) * 0.4, 0])
                layer.add(node)
            layers.add(layer)

        discrete_net = layers.copy().scale(0.8).shift(LEFT * 3.5)
        discrete_title.next_to(discrete_net, UP, buff=0.3)

        # Continuous field (right)
        continuous_title = Text("Continuous", font_size=20, color=DIM_WHITE)

        continuous_field = NeuralField(n_points=100, radius=1.5)
        continuous_field.move_to(RIGHT * 3.5)
        continuous_title.next_to(continuous_field, UP, buff=0.3)

        # Arrow
        arrow = Arrow(LEFT * 1, RIGHT * 1, color=CYAN, stroke_width=3)
        approx_text = Text("approximates", font_size=18, color=SOFT_CYAN)
        approx_text.next_to(arrow, UP, buff=0.1)

        self.play(
            FadeIn(discrete_net), FadeIn(discrete_title),
            run_time=1
        )
        self.wait(1)

        self.play(
            GrowArrow(arrow), FadeIn(approx_text),
            run_time=1
        )

        self.play(
            FadeIn(continuous_field), FadeIn(continuous_title),
            run_time=1
        )

        # Text explanation
        explanation = Text(
            "Classical NN and SKA layered networks\nare discretizations of Riemannian neural fields",
            font_size=22,
            color=WHITE_GLOW,
            line_spacing=1.2
        ).to_edge(DOWN, buff=0.8)

        self.play(FadeIn(explanation), run_time=1)
        self.wait(5)  # 12.55 - 1 - 1 - 1 - 1 - 1 - 1 -1.5 = 5.05

        # Clear
        self.play(
            FadeOut(title), FadeOut(discrete_net), FadeOut(discrete_title),
            FadeOut(arrow), FadeOut(approx_text),
            FadeOut(continuous_field), FadeOut(continuous_title),
            FadeOut(explanation),
            run_time=1.5
        )

    def unified_vision(self):
        """The Unified Vision"""

        # Audio: 15.53s
        self.add_sound("/home/coder/project/manim_the_trilogy/audio/12_unified.mp3")

        # Title
        title = Text(
            "The Unified Vision",
            font_size=40,
            color=WHITE_GLOW
        ).to_edge(UP, buff=0.8)

        self.play(FadeIn(title), run_time=1)

        # Flow diagram: Entropy → Dynamics → Geometry
        entropy = Text("Entropy", font_size=28, color=CYAN)
        dynamics = Text("Dynamics", font_size=28, color=SOFT_CYAN)
        geometry = Text("Geometry", font_size=28, color=PINK_ACCENT)

        entropy.move_to(LEFT * 4)
        dynamics.move_to(ORIGIN)
        geometry.move_to(RIGHT * 4)

        arrow1 = Arrow(entropy.get_right(), dynamics.get_left(), color=WHITE_GLOW, buff=0.3)
        arrow2 = Arrow(dynamics.get_right(), geometry.get_left(), color=WHITE_GLOW, buff=0.3)

        self.play(FadeIn(entropy), run_time=0.5)
        self.play(GrowArrow(arrow1), run_time=0.5)
        self.play(FadeIn(dynamics), run_time=0.5)
        self.play(GrowArrow(arrow2), run_time=0.5)
        self.play(FadeIn(geometry), run_time=0.5)

        self.wait(2)

        # Quote
        quote = Text(
            "Learning is not the correction of error —\nit is the progressive organization of knowledge\nalong geodesic paths.",
            font_size=24,
            color=SOFT_CYAN,
            slant=ITALIC,
            line_spacing=1.3
        ).move_to(DOWN * 1.5)

        self.play(FadeIn(quote), run_time=2)
        self.wait(8)  # 15.53 - 1 - 0.5*5 - 2 - 2 - 1.5 = 6.53

        # Clear
        self.play(
            FadeOut(title), FadeOut(entropy), FadeOut(dynamics), FadeOut(geometry),
            FadeOut(arrow1), FadeOut(arrow2), FadeOut(quote),
            run_time=1.5
        )

    def mathematical_unity(self):
        """Mathematical Unity: H → L → g_ij"""

        # Audio: 15s
        self.add_sound("/home/coder/project/manim_the_trilogy/audio/13_unity.mp3")

        # Title
        title = Text(
            "Mathematical Unity",
            font_size=40,
            color=WHITE_GLOW
        ).to_edge(UP, buff=0.8)

        self.play(FadeIn(title), run_time=1)

        # The complete cycle
        cycle = MathTex(
            r"H \;\Rightarrow\; \mathcal{L} \;\Rightarrow\; G_{ij}",
            font_size=64,
            color=CYAN
        ).move_to(UP * 0.5)

        self.play(Write(cycle), run_time=2)

        # Labels
        h_desc = Text("Entropy", font_size=20, color=DIM_WHITE)
        l_desc = Text("Lagrangian", font_size=20, color=DIM_WHITE)
        g_desc = Text("Metric", font_size=20, color=DIM_WHITE)

        h_desc.next_to(cycle[0][0], DOWN, buff=0.5)
        l_desc.next_to(cycle[0][2], DOWN, buff=0.5)
        g_desc.next_to(cycle[0][4:], DOWN, buff=0.33)

        self.play(FadeIn(h_desc), FadeIn(l_desc), FadeIn(g_desc), run_time=1)

        self.wait(4)

        # Unification text
        unity_text = Text(
            "Entropy • Lagrange's action • Riemann's geometry",
            font_size=22,
            color=SOFT_CYAN
        ).move_to(DOWN * 1.5)

        self.play(FadeIn(unity_text), run_time=1)
        self.wait(6)  # 15 - 1 - 2 - 1 - 4 - 1 = 6

        # Audio: 8.4s
        self.add_sound("/home/coder/project/manim_the_trilogy/audio/14_final.mp3")

        # Final statement
        final = Text(
            "A single law of knowledge accumulation",
            font_size=26,
            color=PINK_ACCENT,
            slant=ITALIC
        ).move_to(DOWN * 2.5)

        self.play(FadeIn(final), run_time=1)
        self.wait(6)  # 8.4 - 1 - 1.5 = 5.9

        # Clear
        self.play(
            FadeOut(title), FadeOut(cycle),
            FadeOut(h_desc), FadeOut(l_desc), FadeOut(g_desc),
            FadeOut(unity_text), FadeOut(final),
            run_time=1.5
        )

    def end_card(self):
        """End card with credits"""

        title = Text(
            "SKA: The Trilogy",
            font_size=42,
            color=WHITE_GLOW
        )

        author = Text(
            "Bouarfa Mahi",
            font_size=32,
            color=CYAN
        ).next_to(title, DOWN, buff=0.5)

        org = Text(
            "Quantiota",
            font_size=28,
            color=PURPLE
        ).next_to(author, DOWN, buff=0.2)

        email = Text(
            "info@quantiota.org",
            font_size=20,
            color=DIM_WHITE
        ).next_to(org, DOWN, buff=0.3)

        year = Text(
            "February 2026",
            font_size=20,
            color=DIM_WHITE
        ).next_to(email, DOWN, buff=0.2)

        end_group = VGroup(title, author, org, email, year)

        self.play(
            FadeIn(title, shift=UP * 0.3),
            run_time=1
        )
        self.play(
            FadeIn(author),
            FadeIn(org),
            FadeIn(email),
            FadeIn(year),
            run_time=1.5
        )

        self.wait(5)

        # Fade out
        self.play(FadeOut(end_group), run_time=2)


if __name__ == "__main__":
    # For command line rendering
    pass
