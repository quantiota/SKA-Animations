"""
The Three Laws of Intelligence - Manim Animation
SKA Framework by Bouarfa Mahi, Quantiota

Requirements:
    pip install manim

Run with:
    manim -pqh three_laws_animation.py ThreeLawsVideo

For lower quality preview:
    manim -pql three_laws_animation.py ThreeLawsVideo
"""

from manim import *
import numpy as np

# Color palette - same as SKA Entropy animation
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


class ThreeLawsVideo(Scene):
    """Main animation scene for The Three Laws of Intelligence"""

    def construct(self):
        self.camera.background_color = DEEP_BLUE

        # Run all sections
        self.intro_section()
        self.law1_probabilistic_decision()
        self.law2_knowledge_accumulation()
        self.law3_entropic_least_action()
        self.unified_section()
        self.end_card()

    def intro_section(self):
        """Intro with title and neural field background"""

        # Create neural field
        neural_field = NeuralField(n_points=250, radius=5)
        neural_field.scale(0.1).set_opacity(0)

        # Title
        title = Text(
            "The Three Laws of Intelligence",
            font_size=44,
            color=WHITE_GLOW
        ).to_edge(UP, buff=0.8)

        author = Text(
            "Bouarfa Mahi • Quantiota • 2026",
            font_size=24,
            color=DIM_WHITE
        ).next_to(title, DOWN, buff=0.3)

        tagline = Text(
            "Unifying Physics, Cognition, and Artificial Intelligence",
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
            FadeIn(author, shift=DOWN * 0.2),
            run_time=1.5
        )

        self.play(
            FadeIn(tagline),
            run_time=1
        )

        # Audio: 4.46s
        self.add_sound("/home/coder/project/manim_the_three_laws_of_intelligence/audio/01_intro.mp3")
        self.wait(4.5)

        # Clear
        self.play(
            FadeOut(title), FadeOut(author),
            FadeOut(tagline), FadeOut(neural_field),
            run_time=1.5
        )

    def law1_probabilistic_decision(self):
        """Law 1: Probabilistic Decision-Making with sigmoid visualization"""

        # Section title
        law_number = Text("Law 1", font_size=28, color=PINK_ACCENT)
        law_title = Text(
            "Probabilistic Decision-Making",
            font_size=38,
            color=WHITE_GLOW
        ).next_to(law_number, DOWN, buff=0.2)

        title_group = VGroup(law_number, law_title).to_edge(UP, buff=0.5)

        self.play(FadeIn(title_group), run_time=1)

        # Principle text
        principle = Text(
            "Intelligence is the capacity to make\ndecisions under uncertainty.",
            font_size=24,
            color=DIM_WHITE,
            line_spacing=1.2
        ).next_to(title_group, DOWN, buff=0.4)

        # Audio: 7.39s
        self.add_sound("/home/coder/project/manim_the_three_laws_of_intelligence/audio/02_law1_principle.mp3")
        self.play(FadeIn(principle), run_time=1)
        self.wait(6.5)  # 7.39 - 1 = 6.39

        self.play(FadeOut(principle), run_time=0.5)

        # Create axes for sigmoid
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[0, 1.2, 0.2],
            x_length=8,
            y_length=4,
            axis_config={"color": DIM_WHITE, "stroke_width": 2},
            tips=False
        ).shift(DOWN * 0.3)

        # Labels
        x_label = MathTex("z", font_size=32, color=CYAN).next_to(axes.x_axis, RIGHT, buff=0.2)
        y_label = MathTex("D", font_size=32, color=PINK_ACCENT).next_to(axes.y_axis, UP, buff=0.2)
        x_label_text = Text("(Knowledge)", font_size=18, color=DIM_WHITE).next_to(x_label, DOWN, buff=0.1)
        y_label_text = Text("(Decision)", font_size=18, color=DIM_WHITE).next_to(y_label, RIGHT, buff=0.1)

        # Sigmoid function
        sigmoid = axes.plot(
            lambda x: 1 / (1 + np.exp(-x)),
            x_range=[-6, 6],
            color=CYAN,
            stroke_width=4
        )

        # Formula
        formula = MathTex(
            r"D = \sigma(z) = \frac{1}{1 + e^{-z}}",
            font_size=36,
            color=WHITE_GLOW
        )
        formula_box = SurroundingRectangle(formula, color=CYAN, buff=0.2, stroke_width=2)
        formula_group = VGroup(formula, formula_box).to_edge(DOWN, buff=0.4)

        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label), run_time=1.5)
        self.play(FadeIn(x_label_text), FadeIn(y_label_text), run_time=0.5)

        # Audio: 11.83s - need total 12s of animation/wait time
        self.add_sound("/home/coder/project/manim_the_three_laws_of_intelligence/audio/03_law1_sigmoid.mp3")
        self.play(Create(sigmoid), run_time=2)  # 2s
        self.play(FadeIn(formula_group), run_time=1)  # 3s

        # Animate a point moving along sigmoid
        dot = Dot(color=PINK_ACCENT, radius=0.12)
        dot.move_to(axes.c2p(-5, 1 / (1 + np.exp(5))))

        # Uncertainty region (left)
        uncertainty_label = Text("Uncertainty", font_size=18, color=PURPLE).move_to(axes.c2p(-4, 0.8))
        # Confidence region (right)
        confidence_label = Text("Confidence", font_size=18, color=SOFT_CYAN).move_to(axes.c2p(4, 0.8))

        self.play(FadeIn(uncertainty_label), FadeIn(confidence_label), run_time=0.5)  # 3.5s
        self.play(FadeIn(dot), run_time=0.5)  # 4s

        # Move dot along curve
        self.play(
            MoveAlongPath(dot, sigmoid),
            run_time=4,  # 8s total
            rate_func=smooth
        )

        self.wait(4)  # 12s total - audio 03 is 11.83s

        # Audio: 7.06s
        self.add_sound("/home/coder/project/manim_the_three_laws_of_intelligence/audio/04_law1_meaning.mp3")
        self.wait(7)

        # Clear
        self.play(
            FadeOut(title_group), FadeOut(axes), FadeOut(sigmoid), FadeOut(formula_group),
            FadeOut(x_label), FadeOut(y_label), FadeOut(x_label_text), FadeOut(y_label_text),
            FadeOut(dot), FadeOut(uncertainty_label), FadeOut(confidence_label),
            run_time=1.5
        )

    def law2_knowledge_accumulation(self):
        """Law 2: Knowledge Accumulation with entropy visualization"""

        # Section title
        law_number = Text("Law 2", font_size=28, color=PINK_ACCENT)
        law_title = Text(
            "Knowledge Accumulation",
            font_size=38,
            color=WHITE_GLOW
        ).next_to(law_number, DOWN, buff=0.2)

        title_group = VGroup(law_number, law_title).to_edge(UP, buff=0.5)

        self.play(FadeIn(title_group), run_time=1)

        # Principle
        principle = Text(
            "Knowledge grows forward-only by reducing\nuncertainty through structured accumulation.",
            font_size=24,
            color=DIM_WHITE,
            line_spacing=1.2
        ).next_to(title_group, DOWN, buff=0.4)

        # Audio: 8.26s
        self.add_sound("/home/coder/project/manim_the_three_laws_of_intelligence/audio/05_law2_principle.mp3")
        self.play(FadeIn(principle), run_time=1)
        self.wait(7.5)  # 8.26 - 1 = 7.26

        self.play(FadeOut(principle), run_time=0.5)

        # Formula
        formula = MathTex(
            r"H = -\frac{1}{\ln 2} \int z \, dD",
            font_size=40,
            color=WHITE_GLOW
        )
        formula_box = SurroundingRectangle(formula, color=CYAN, buff=0.25, stroke_width=2)
        formula_group = VGroup(formula, formula_box).shift(UP * 0.5)

        # Labels
        h_label = Text("H: Entropy (uncertainty)", font_size=20, color=SOFT_CYAN)
        z_label = Text("z: Knowledge trajectory", font_size=20, color=CYAN)
        d_label = Text("dD: Change in decision probability", font_size=20, color=PINK_ACCENT)
        labels = VGroup(h_label, z_label, d_label).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        labels.next_to(formula_group, DOWN, buff=0.5)

        # Audio: 7.22s
        self.add_sound("/home/coder/project/manim_the_three_laws_of_intelligence/audio/06_law2_formula.mp3")
        self.play(FadeIn(formula_group), run_time=1)
        self.play(FadeIn(labels, lag_ratio=0.3), run_time=1.5)
        self.wait(5)  # 7.22 - 1 - 1.5 = 4.72

        self.play(FadeOut(formula_group), FadeOut(labels), run_time=0.5)

        # Entropy visualization - chaos to order
        # Left side: high entropy (chaotic particles)
        chaos_particles = VGroup()
        np.random.seed(42)
        for _ in range(40):
            x = np.random.uniform(-5, -2)
            y = np.random.uniform(-2, 1.5)
            particle = Dot(
                point=[x, y, 0],
                radius=0.08,
                color=interpolate_color(PURPLE, PINK_ACCENT, np.random.uniform(0, 1))
            ).set_opacity(0.8)
            chaos_particles.add(particle)

        # Right side: low entropy (structured grid)
        order_particles = VGroup()
        for i in range(5):
            for j in range(5):
                x = 2 + i * 0.6
                y = -1.5 + j * 0.6
                particle = Dot(
                    point=[x, y, 0],
                    radius=0.08,
                    color=CYAN
                ).set_opacity(0.9)
                order_particles.add(particle)

        # Labels
        chaos_label = Text("High Entropy", font_size=22, color=PINK_ACCENT).move_to([-3.5, 2.2, 0])
        order_label = Text("Low Entropy", font_size=22, color=CYAN).move_to([3.5, 2.2, 0])

        # Arrow showing transformation
        arrow = Arrow(
            start=[-0.5, 0, 0],
            end=[1, 0, 0],
            color=WHITE_GLOW,
            stroke_width=3
        )
        arrow_label = Text("Learning", font_size=18, color=WHITE_GLOW).next_to(arrow, UP, buff=0.1)

        self.play(FadeIn(chaos_particles, lag_ratio=0.02), FadeIn(chaos_label), run_time=1.5)

        # Audio: 11.18s
        self.add_sound("/home/coder/project/manim_the_three_laws_of_intelligence/audio/07_law2_entropy.mp3")
        self.play(
            GrowArrow(arrow),
            FadeIn(arrow_label),
            run_time=1
        )
        self.play(FadeIn(order_particles, lag_ratio=0.02), FadeIn(order_label), run_time=1.5)

        self.wait(8)  # 11.18 - 1 - 1.5 = 8.68

        # Clear
        self.play(
            FadeOut(title_group), FadeOut(chaos_particles), FadeOut(order_particles),
            FadeOut(chaos_label), FadeOut(order_label),
            FadeOut(arrow), FadeOut(arrow_label),
            run_time=1.5
        )

    def law3_entropic_least_action(self):
        """Law 3: Entropic Least Action with trajectory visualization"""

        # Section title
        law_number = Text("Law 3", font_size=28, color=PINK_ACCENT)
        law_title = Text(
            "Entropic Least Action",
            font_size=38,
            color=WHITE_GLOW
        ).next_to(law_number, DOWN, buff=0.2)

        title_group = VGroup(law_number, law_title).to_edge(UP, buff=0.5)

        self.play(FadeIn(title_group), run_time=1)

        # Principle
        principle = Text(
            "Intelligence follows the path of least action\nthrough knowledge space.",
            font_size=24,
            color=DIM_WHITE,
            line_spacing=1.2
        ).next_to(title_group, DOWN, buff=0.4)

        # Audio: 8.38s
        self.add_sound("/home/coder/project/manim_the_three_laws_of_intelligence/audio/08_law3_principle.mp3")
        self.play(FadeIn(principle), run_time=1)
        self.wait(7.5)  # 8.38 - 1 = 7.38

        self.play(FadeOut(principle), run_time=0.5)

        # Create knowledge space visualization
        # Start and end points
        start_point = Dot([-5, -1.5, 0], radius=0.15, color=PURPLE)
        start_label = Text("Start", font_size=18, color=PURPLE).next_to(start_point, DOWN, buff=0.15)

        end_point = Dot([5, 1.5, 0], radius=0.15, color=CYAN)
        end_label = Text("Goal", font_size=18, color=CYAN).next_to(end_point, UP, buff=0.15)

        # Multiple possible paths (suboptimal)
        path1 = CubicBezier(
            [-5, -1.5, 0], [-2, 2.5, 0], [2, -2.5, 0], [5, 1.5, 0]
        ).set_stroke(PURPLE, width=2, opacity=0.4)

        path2 = CubicBezier(
            [-5, -1.5, 0], [-3, -2.5, 0], [3, 2.5, 0], [5, 1.5, 0]
        ).set_stroke(PURPLE, width=2, opacity=0.4)

        path3 = CubicBezier(
            [-5, -1.5, 0], [0, 3, 0], [2, -1, 0], [5, 1.5, 0]
        ).set_stroke(PURPLE, width=2, opacity=0.4)

        # Optimal path (least entropy)
        optimal_path = CubicBezier(
            [-5, -1.5, 0], [-1.5, 0, 0], [1.5, 0.5, 0], [5, 1.5, 0]
        ).set_stroke(CYAN, width=4)

        # Glow effect for optimal path
        optimal_glow = optimal_path.copy().set_stroke(SOFT_CYAN, width=8, opacity=0.3)

        self.play(
            FadeIn(start_point), FadeIn(start_label),
            FadeIn(end_point), FadeIn(end_label),
            run_time=1
        )

        # Audio: 7.99s
        self.add_sound("/home/coder/project/manim_the_three_laws_of_intelligence/audio/09_law3_paths.mp3")

        # Show suboptimal paths
        self.play(
            Create(path1), Create(path2), Create(path3),
            run_time=2
        )

        suboptimal_label = Text("Suboptimal paths", font_size=18, color=PURPLE).move_to([0, 2.0, 0])
        self.play(FadeIn(suboptimal_label), run_time=0.5)
        self.wait(1)

        # Show optimal path
        self.play(
            Create(optimal_glow),
            Create(optimal_path),
            run_time=2
        )

        optimal_label = Text("Optimal path (least action)", font_size=18, color=CYAN).move_to([0, -2, 0])
        self.play(FadeIn(optimal_label), run_time=0.5)

        self.wait(2)  # 7.99 - 2 - 0.5 - 1 - 2 - 0.5 = 1.99

        # Animate a particle along optimal path
        particle = Dot(color=PINK_ACCENT, radius=0.12)
        particle.move_to([-5, -1.5, 0])

        self.play(FadeIn(particle), run_time=0.3)
        self.play(MoveAlongPath(particle, optimal_path), run_time=2, rate_func=smooth)

        self.wait(0.5)

        # Clear paths, show formulas
        self.play(
            FadeOut(path1), FadeOut(path2), FadeOut(path3),
            FadeOut(optimal_path), FadeOut(optimal_glow),
            FadeOut(start_point), FadeOut(start_label),
            FadeOut(end_point), FadeOut(end_label),
            FadeOut(particle), FadeOut(suboptimal_label), FadeOut(optimal_label),
            run_time=1
        )

        # Lagrangian formula
        lagrangian = MathTex(
            r"\mathcal{L}(z, \dot{z}, t) = -z \cdot \sigma(z)(1 - \sigma(z)) \cdot \dot{z}",
            font_size=32,
            color=WHITE_GLOW
        ).shift(UP * 0.5)
        lagrangian_label = Text("Entropic Lagrangian", font_size=20, color=CYAN).next_to(lagrangian, UP, buff=0.3)

        # Euler-Lagrange
        euler = MathTex(
            r"\frac{d}{dt}\left(\frac{\partial \mathcal{L}}{\partial \dot{z}}\right) - \frac{\partial \mathcal{L}}{\partial z} = 0",
            font_size=32,
            color=WHITE_GLOW
        ).next_to(lagrangian, DOWN, buff=0.6)
        euler_label = Text("Euler-Lagrange Equation", font_size=20, color=PINK_ACCENT).next_to(euler, DOWN, buff=0.3)

        # Audio: 14.02s
        self.add_sound("/home/coder/project/manim_the_three_laws_of_intelligence/audio/10_law3_physics.mp3")
        self.play(FadeIn(lagrangian_label), FadeIn(lagrangian), run_time=1.5)
        self.play(FadeIn(euler_label), FadeIn(euler), run_time=1.5)

        self.wait(11)  # 14.02 - 1.5 - 1.5 = 11.02

        # Clear
        self.play(
            FadeOut(title_group), FadeOut(lagrangian), FadeOut(lagrangian_label),
            FadeOut(euler), FadeOut(euler_label),
            run_time=1.5
        )

    def unified_section(self):
        """Summary showing all three laws unified"""

        # Title
        title = Text(
            "Unified Beauty",
            font_size=42,
            color=CYAN
        ).to_edge(UP, buff=0.5)

        self.play(FadeIn(title), run_time=1)

        # Create summary table
        law1_name = Text("Law 1", font_size=20, color=PINK_ACCENT)
        law1_concept = Text("Probabilistic Decision", font_size=18, color=WHITE_GLOW)
        law1_eq = MathTex(r"D = \sigma(z)", font_size=24, color=SOFT_CYAN)

        law2_name = Text("Law 2", font_size=20, color=PINK_ACCENT)
        law2_concept = Text("Knowledge Accumulation", font_size=18, color=WHITE_GLOW)
        law2_eq = MathTex(r"H = -\frac{1}{\ln 2}\int z\,dD", font_size=24, color=SOFT_CYAN)

        law3_name = Text("Law 3", font_size=20, color=PINK_ACCENT)
        law3_concept = Text("Entropic Least Action", font_size=18, color=WHITE_GLOW)
        law3_eq = MathTex(r"H = \frac{1}{\ln 2}\int \mathcal{L}\,dt", font_size=24, color=SOFT_CYAN)

        # Arrange in rows
        row1 = VGroup(law1_name, law1_concept, law1_eq).arrange(RIGHT, buff=0.8)
        row2 = VGroup(law2_name, law2_concept, law2_eq).arrange(RIGHT, buff=0.8)
        row3 = VGroup(law3_name, law3_concept, law3_eq).arrange(RIGHT, buff=0.8)

        table = VGroup(row1, row2, row3).arrange(DOWN, buff=0.5).shift(UP * 0.3)

        # Box around table
        table_box = SurroundingRectangle(table, color=PURPLE, buff=0.4, stroke_width=2)

        # Audio: 9.17s
        self.add_sound("/home/coder/project/manim_the_three_laws_of_intelligence/audio/11_unified.mp3")
        self.play(
            FadeIn(row1),
            run_time=1
        )
        self.play(FadeIn(row2), run_time=1)
        self.play(FadeIn(row3), run_time=1)
        self.play(Create(table_box), run_time=0.5)

        self.wait(6)  # 9.17 - 1 - 1 - 1 - 0.5 = 5.67

        # Paradigm shift quote
        quote1 = Text(
            '"AI works because it learns patterns"',
            font_size=22,
            color=DIM_WHITE,
            slant=ITALIC
        ).to_edge(DOWN, buff=1.5)

        arrow = MathTex(r"\Downarrow", font_size=36, color=CYAN).next_to(quote1, DOWN, buff=0.2)

        quote2 = Text(
            '"AI works because intelligence is the physical\nreduction of entropy along a probabilistic path"',
            font_size=22,
            color=SOFT_CYAN,
            slant=ITALIC,
            line_spacing=1.2
        ).next_to(arrow, DOWN, buff=0.2)

        # Audio: 12.22s
        self.add_sound("/home/coder/project/manim_the_three_laws_of_intelligence/audio/12_paradigm.mp3")
        self.play(FadeIn(quote1), run_time=1)
        self.play(FadeIn(arrow), run_time=0.5)
        self.play(FadeIn(quote2), run_time=1)

        self.wait(10)  # 12.22 - 1 - 0.5 - 1 = 9.72

        # Audio: 4.32s
        self.add_sound("/home/coder/project/manim_the_three_laws_of_intelligence/audio/13_final.mp3")
        self.wait(4.5)

        self.play(
            FadeOut(title), FadeOut(table), FadeOut(table_box),
            FadeOut(quote1), FadeOut(arrow), FadeOut(quote2),
            run_time=1.5
        )

    def end_card(self):
        """End card with credits"""

        title = Text(
            "The Three Laws of Intelligence",
            font_size=38,
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
            run_time=1.5
        )
        self.play(
            FadeIn(author),
            FadeIn(org),
            FadeIn(email),
            FadeIn(year),
            run_time=1.5
        )

        self.wait(3)

        self.play(FadeOut(end_group), run_time=2)


if __name__ == "__main__":
    import subprocess
    subprocess.run(["manim", "-pqh", __file__, "ThreeLawsVideo"])
