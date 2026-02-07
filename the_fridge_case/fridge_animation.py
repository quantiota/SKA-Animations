"""
The Fridge Case: Why Human Intelligence is Probabilistic, Not Deterministic
SKA — Manim Animation

Uses the everyday scenario of deciding whether to go grocery shopping
to make SKA's probabilistic intelligence framework intuitive.

Requirements:
    pip install manim

Run with:
    manim -qh fridge_animation.py FridgeCaseVideo

For lower quality preview:
    manim -ql fridge_animation.py FridgeCaseVideo
"""

from manim import *
import numpy as np

# Color palette — consistent with SKA series
DEEP_BLUE = ManimColor("#0a1628")
PURPLE = ManimColor("#6b5b95")
CYAN = ManimColor("#00d4ff")
SOFT_CYAN = ManimColor("#7fefff")
PINK_ACCENT = ManimColor("#ff6b9d")
WHITE_GLOW = ManimColor("#ffffff")
DIM_WHITE = ManimColor("#aaaaaa")
GOLD = ManimColor("#ffd700")

AUDIO_DIR = "/home/coder/project/manim_fridge/audio"


class NeuralField(VGroup):
    """Creates a field of glowing neural points — identical to reference animations"""

    def __init__(self, n_points=200, radius=4, **kwargs):
        super().__init__(**kwargs)

        for _ in range(n_points):
            theta = np.random.uniform(0, 2 * PI)
            phi = np.random.uniform(0, PI)
            r = np.random.uniform(0.5, radius) * np.random.uniform(0.3, 1) ** 0.5

            x = r * np.sin(phi) * np.cos(theta)
            y = r * np.sin(phi) * np.sin(theta)
            z = r * np.cos(phi) * 0.3  # Flatten z for 2D projection

            point = Dot(
                point=[x, y + z, 0],
                radius=np.random.uniform(0.02, 0.06),
                color=interpolate_color(PURPLE, CYAN, np.random.uniform(0, 1)),
            ).set_opacity(np.random.uniform(0.3, 0.9))

            self.add(point)


class FridgeCaseVideo(Scene):
    """The Fridge Case — making SKA intuitive through a concrete everyday example"""

    def construct(self):
        self.camera.background_color = DEEP_BLUE

        self.intro_section()
        self.undecided_state_section()
        self.input_features_section()
        self.sigmoid_decision_section()
        self.knowledge_accumulates_section()
        self.why_it_matters_section()
        self.binary_vs_ska_section()
        self.takeaway_section()
        self.end_card()

    # ─────────────────────────────────────────────────────────────
    # SCENE 1: INTRO (~12s) — NeuralField expansion
    # ─────────────────────────────────────────────────────────────
    def intro_section(self):
        """NeuralField cosmic zoom + title card"""

        # Neural field background
        neural_field = NeuralField(n_points=250, radius=5)
        neural_field.scale(0.1).set_opacity(0)

        # Title block
        title = Text(
            "The Fridge Case",
            font_size=44,
            color=WHITE_GLOW,
        ).to_edge(UP, buff=1.2)

        author = Text(
            "Bouarfa Mahi • Quantiota • 2026",
            font_size=24,
            color=DIM_WHITE,
        ).next_to(title, DOWN, buff=0.3)

        tagline = Text(
            "Why Human Intelligence is Probabilistic, Not Deterministic",
            font_size=22,
            color=SOFT_CYAN,
            slant=ITALIC,
        ).next_to(author, DOWN, buff=0.5)

        # Cosmic zoom (silent visual intro)
        self.play(
            neural_field.animate.scale(10).set_opacity(1),
            run_time=3,
            rate_func=smooth,
        )

        self.play(
            FadeIn(title, shift=DOWN * 0.3),
            run_time=1.5,
        )
        self.play(
            FadeIn(author, shift=DOWN * 0.1),
            FadeIn(tagline, shift=DOWN * 0.1),
            run_time=1,
        )

        # Audio 01: ~5s — narration starts after visuals are on screen
        self.add_sound(f"{AUDIO_DIR}/01_intro.mp3")
        self.wait(5)

        # Clear
        self.play(
            FadeOut(title),
            FadeOut(author), FadeOut(tagline),
            FadeOut(neural_field),
            run_time=1.5,
        )

    # ─────────────────────────────────────────────────────────────
    # SCENE 2: THE UNDECIDED STATE (~18s)
    # ─────────────────────────────────────────────────────────────
    def undecided_state_section(self):
        """Wednesday scenario — sigmoid at midpoint, D = 0.5"""

        # Audio 02: ~8.69s
        self.add_sound(f"{AUDIO_DIR}/02_scenario.mp3")

        # Day label
        day_label = Text("Wednesday", font_size=20, color=DIM_WHITE)
        day_label.to_edge(UP, buff=0.4)
        self.play(FadeIn(day_label), run_time=0.5)

        # Question
        question = Text(
            "Go to the supermarket?",
            font_size=28,
            color=WHITE_GLOW,
        ).move_to(UP * 2.8)
        self.play(FadeIn(question, shift=DOWN * 0.2), run_time=1)

        # Narration subtitle
        narration_02 = Text(
            "At first, the probability is 0.5 \u2014 completely undecided.",
            font_size=20,
            color=DIM_WHITE,
        ).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(narration_02), run_time=0.8)

        # Sigmoid curve with axes (matching three_laws reference design)
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[0, 1.2, 0.2],
            x_length=8,
            y_length=4,
            axis_config={"color": DIM_WHITE, "stroke_width": 2},
            tips=False,
        ).shift(DOWN * 0.3)

        x_label = MathTex("z", font_size=32, color=CYAN).next_to(axes.x_axis, RIGHT, buff=0.2)
        y_label = MathTex("D", font_size=32, color=PINK_ACCENT).next_to(axes.y_axis, UP, buff=0.2)
        x_label_text = Text("(Knowledge)", font_size=18, color=DIM_WHITE).next_to(x_label, DOWN, buff=0.1)
        y_label_text = Text("(Decision)", font_size=18, color=DIM_WHITE).next_to(y_label, RIGHT, buff=0.1)

        sigmoid_curve = axes.plot(
            lambda x: 1 / (1 + np.exp(-x)),
            x_range=[-6, 6],
            color=CYAN,
            stroke_width=4,
        )

        # Threshold line at D = 0.5
        threshold_line = DashedLine(
            start=axes.c2p(-6, 0.5),
            end=axes.c2p(6, 0.5),
            color=GOLD,
            stroke_width=1.5,
            dash_length=0.1,
        )

        # Pink dot at midpoint z=0, D=0.5
        mid_dot = Dot(
            point=axes.c2p(0, 0.5),
            radius=0.12,
            color=PINK_ACCENT,
        )

        # Label
        undecided_label = Text(
            "D = 0.5 \u2014 undecided",
            font_size=18,
            color=GOLD,
        ).next_to(mid_dot, UR, buff=0.2).shift(RIGHT * 0.5)

        # Uncertainty / Confidence labels
        uncertainty_label = Text("Uncertainty", font_size=18, color=PURPLE)
        uncertainty_label.move_to(axes.c2p(-4, 0.8))

        confidence_label = Text("Confidence", font_size=18, color=SOFT_CYAN)
        confidence_label.move_to(axes.c2p(4, 0.8))

        self.play(
            Create(axes),
            FadeIn(x_label), FadeIn(y_label),
            run_time=1.5,
        )
        self.play(
            FadeIn(x_label_text), FadeIn(y_label_text),
            run_time=0.5,
        )
        self.play(Create(sigmoid_curve), run_time=1.5)
        self.play(
            Create(threshold_line),
            FadeIn(mid_dot),
            FadeIn(undecided_label),
            run_time=1,
        )
        self.play(
            FadeIn(uncertainty_label),
            FadeIn(confidence_label),
            run_time=0.5,
        )

        self.wait(2)

        # Audio 03: ~7.13s
        self.add_sound(f"{AUDIO_DIR}/03_undecided.mp3")

        narration_03 = Text(
            "On the sigmoid curve, your decision sits exactly at the midpoint.\n"
            "No information has yet tipped the balance.",
            font_size=22,
            color=WHITE_GLOW,
            line_spacing=1.2,
        ).to_edge(DOWN, buff=0.3)

        self.play(
            FadeOut(narration_02),
            FadeIn(narration_03),
            run_time=1,
        )
        self.wait(5)

        # Clear
        self.play(
            FadeOut(day_label), FadeOut(question),
            FadeOut(axes), FadeOut(x_label), FadeOut(y_label),
            FadeOut(x_label_text), FadeOut(y_label_text),
            FadeOut(sigmoid_curve), FadeOut(threshold_line),
            FadeOut(mid_dot), FadeOut(undecided_label),
            FadeOut(uncertainty_label), FadeOut(confidence_label),
            FadeOut(narration_03),
            run_time=1.5,
        )

    # ─────────────────────────────────────────────────────────────
    # SCENE 3: INPUT FEATURES — THE FRIDGE (~20s)
    # ─────────────────────────────────────────────────────────────
    def input_features_section(self):
        """Cube volume element with neurons, knowledge arrows, decision clouds"""

        # Audio 04: ~5.06s
        self.add_sound(f"{AUDIO_DIR}/04_features.mp3")

        # Narration subtitle
        narration_04 = Text(
            "You open the fridge. You observe what's inside \u2014\n"
            "these are your input features.",
            font_size=20,
            color=DIM_WHITE,
            line_spacing=1.2,
        ).to_edge(DOWN, buff=0.3)

        # Cube representing observation space
        cube = Cube(side_length=2.8, fill_opacity=0.08, stroke_width=2)
        cube.set_color(CYAN)
        cube.set_stroke(CYAN, opacity=0.5)
        cube.shift(LEFT * 0.5 + UP * 0.5)

        # Scattered neurons inside
        neurons = VGroup()
        neuron_positions = []
        for _ in range(20):
            pos = np.random.uniform(-1.1, 1.1, 3)
            pos[2] *= 0.3
            neuron_positions.append(pos[:2])
            neuron = Dot(
                point=[pos[0] - 0.5, pos[1] + 0.5, 0],
                radius=0.07,
                color=SOFT_CYAN,
            ).set_opacity(0.85)
            neurons.add(neuron)

        # Input features label
        input_label = Text("Input features (X)", font_size=18, color=CYAN)
        input_label.next_to(cube, DOWN, buff=0.4)

        self.play(Create(cube), FadeIn(narration_04), run_time=1.5)
        self.play(FadeIn(neurons, lag_ratio=0.05), run_time=1)
        self.play(FadeIn(input_label), run_time=0.5)
        self.wait(2.5)

        # Audio 05: ~9.24s
        self.add_sound(f"{AUDIO_DIR}/05_knowledge.mp3")
        self.play(FadeOut(narration_04), run_time=0.5)

        # Knowledge tensor z(r) — pink arrows from neurons
        z_arrows = VGroup()
        for neuron in neurons[:12]:
            direction = np.random.uniform(-1, 1, 2)
            direction = direction / np.linalg.norm(direction) * 0.4
            arrow = Arrow(
                neuron.get_center(),
                neuron.get_center() + [direction[0], direction[1], 0],
                buff=0,
                stroke_width=3,
                color=PINK_ACCENT,
                max_tip_length_to_length_ratio=0.3,
            )
            z_arrows.add(arrow)

        z_label = MathTex(r"\mathbf{z}(\mathbf{r})", font_size=32, color=PINK_ACCENT)
        z_label.to_corner(UL, buff=0.8).shift(RIGHT * 1.5)
        z_text = Text("Knowledge Tensor", font_size=20, color=PINK_ACCENT)
        z_text.next_to(z_label, DOWN, buff=0.2)

        # Decision probability tensor D(r) — purple circles
        d_clouds = VGroup()
        for neuron in neurons[:12]:
            cloud = Circle(
                radius=0.22,
                fill_opacity=0.15,
                stroke_opacity=0.4,
                color=PURPLE,
            ).move_to(neuron.get_center())
            d_clouds.add(cloud)

        d_label = MathTex(r"D(\mathbf{r})", font_size=32, color=PURPLE)
        d_label.to_corner(UR, buff=0.8).shift(LEFT * 1.5)
        d_text = Text("Decision Probability", font_size=20, color=PURPLE)
        d_text.next_to(d_label, DOWN, buff=0.2)

        self.play(
            Create(z_arrows, lag_ratio=0.1),
            FadeIn(z_label), FadeIn(z_text),
            run_time=1.5,
        )
        self.play(
            FadeIn(d_clouds, lag_ratio=0.1),
            FadeIn(d_label), FadeIn(d_text),
            run_time=1.5,
        )

        # Narration about weighing family needs
        narration_05 = Text(
            "You mentally weigh what your family needs until the end of the week,\n"
            "drawing on past experience. This is your knowledge value, Z.",
            font_size=22,
            color=WHITE_GLOW,
            line_spacing=1.2,
        ).to_edge(DOWN, buff=0.3)

        self.play(FadeIn(narration_05), run_time=0.8)

        # Formula: z(r) → D(r)
        flow_formula = MathTex(
            r"\mathbf{z}(\mathbf{r}) \;\rightarrow\; D(\mathbf{r})",
            font_size=36,
            color=WHITE_GLOW,
        ).shift(DOWN * 1.8, LEFT*0.5)

        self.play(FadeIn(flow_formula), run_time=1)
        self.wait(4)

        # Clear
        self.play(
            FadeOut(cube), FadeOut(neurons),
            FadeOut(input_label),
            FadeOut(z_arrows), FadeOut(z_label), FadeOut(z_text),
            FadeOut(d_clouds), FadeOut(d_label), FadeOut(d_text),
            FadeOut(narration_05), FadeOut(flow_formula),
            run_time=1.5,
        )

    # ─────────────────────────────────────────────────────────────
    # SCENE 4: THE SIGMOID DECISION: D = σ(Z) (~18s)
    # ─────────────────────────────────────────────────────────────
    def sigmoid_decision_section(self):
        """Full sigmoid curve with formula and threshold explanation"""

        # Audio 06: ~9.89s
        self.add_sound(f"{AUDIO_DIR}/06_sigmoid.mp3")

        # Narration subtitle
        narration_06 = Text(
            "The sigmoid function maps accumulated knowledge to a decision probability.\n"
            "D = \u03c3(Z). If D exceeds 0.5, you go.",
            font_size=20,
            color=DIM_WHITE,
            line_spacing=1.2,
        ).to_edge(DOWN, buff=0.3)

        # Full sigmoid axes (matching three_laws reference design)
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[0, 1.2, 0.2],
            x_length=8,
            y_length=4,
            axis_config={"color": DIM_WHITE, "stroke_width": 2},
            tips=False,
        ).shift(DOWN * 0.2)

        x_label = MathTex("z", font_size=32, color=CYAN).next_to(axes.x_axis, RIGHT, buff=0.2)
        y_label = MathTex("D", font_size=32, color=PINK_ACCENT).next_to(axes.y_axis, UP, buff=0.2)
        x_label_text = Text("(Knowledge)", font_size=18, color=DIM_WHITE).next_to(x_label, DOWN, buff=0.1)
        y_label_text = Text("(Decision)", font_size=18, color=DIM_WHITE).next_to(y_label, RIGHT, buff=0.1)

        # Sigmoid curve
        sigmoid = axes.plot(
            lambda x: 1 / (1 + np.exp(-x)),
            x_range=[-6, 6],
            color=CYAN,
            stroke_width=4,
        )

        # Formula with box
        formula = MathTex(
            r"D = \sigma(z) = \frac{1}{1 + e^{-z}}",
            font_size=36,
            color=WHITE_GLOW,
        )
        formula_box = SurroundingRectangle(formula, color=CYAN, buff=0.2, stroke_width=2)
        formula_group = VGroup(formula, formula_box).to_edge(UP, buff=0.5).shift(UP * 0.2)

        # Threshold
        threshold_line = DashedLine(
            start=axes.c2p(-6, 0.5),
            end=axes.c2p(6, 0.5),
            color=GOLD,
            stroke_width=1.5,
            dash_length=0.1,
        )

        threshold_text = Text(
            "If D > 0.5 \u2192 go shopping",
            font_size=20,
            color=GOLD,
        ).next_to(threshold_line, RIGHT, buff=0.3).shift(UP * 0.2 + LEFT * 3.5)

        # Pink dot at midpoint
        mid_dot = Dot(
            point=axes.c2p(0, 0.5),
            radius=0.12,
            color=PINK_ACCENT,
        )

        # Uncertainty / Confidence labels
        uncertainty_label_s4 = Text("Uncertainty", font_size=18, color=PURPLE)
        uncertainty_label_s4.move_to(axes.c2p(-4, 0.8))
        confidence_label_s4 = Text("Confidence", font_size=18, color=SOFT_CYAN)
        confidence_label_s4.move_to(axes.c2p(4, 0.8))

        # Animate
        self.play(
            Create(axes),
            FadeIn(x_label), FadeIn(y_label),
            FadeIn(narration_06),
            run_time=1,
        )
        self.play(
            FadeIn(x_label_text), FadeIn(y_label_text),
            run_time=0.5,
        )
        self.play(
            Create(sigmoid),
            FadeIn(formula_group),
            run_time=2,
        )
        self.play(
            Create(threshold_line),
            FadeIn(threshold_text),
            FadeIn(mid_dot),
            FadeIn(uncertainty_label_s4),
            FadeIn(confidence_label_s4),
            run_time=1,
        )

        self.wait(5)
        self.play(FadeOut(narration_06), run_time=0.5)

        # Clear
        self.play(
            FadeOut(axes), FadeOut(sigmoid),
            FadeOut(formula_group),
            FadeOut(threshold_line), FadeOut(threshold_text),
            FadeOut(mid_dot),
            FadeOut(x_label), FadeOut(y_label),
            FadeOut(x_label_text), FadeOut(y_label_text),
            FadeOut(uncertainty_label_s4), FadeOut(confidence_label_s4),
            run_time=1.5,
        )

    # ─────────────────────────────────────────────────────────────
    # SCENE 5: KNOWLEDGE ACCUMULATES (~25s)
    # ─────────────────────────────────────────────────────────────
    def knowledge_accumulates_section(self):
        """New knowledge arrives, dot moves along sigmoid, chaos-to-order"""

        # Audio 07: ~6s
        self.add_sound(f"{AUDIO_DIR}/07_new_knowledge.mp3")

        # New knowledge text
        new_knowledge = Text(
            "Friends coming for dinner tomorrow!",
            font_size=24,
            color=GOLD,
        ).to_edge(UP, buff=0.6)

        self.play(FadeIn(new_knowledge, shift=UP * 0.3), run_time=1)
        self.wait(4.5)

        # Rebuild sigmoid for dot animation (matching three_laws reference)
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[0, 1.2, 0.2],
            x_length=8,
            y_length=4,
            axis_config={"color": DIM_WHITE, "stroke_width": 2},
            tips=False,
        ).shift(DOWN * 0.5)

        s5_x_label = MathTex("z", font_size=32, color=CYAN).next_to(axes.x_axis, RIGHT, buff=0.2)
        s5_y_label = MathTex("D", font_size=32, color=PINK_ACCENT).next_to(axes.y_axis, UP, buff=0.2)

        sigmoid = axes.plot(
            lambda x: 1 / (1 + np.exp(-x)),
            x_range=[-6, 6],
            color=CYAN,
            stroke_width=4,
        )

        threshold = DashedLine(
            start=axes.c2p(-6, 0.5),
            end=axes.c2p(6, 0.5),
            color=GOLD,
            stroke_width=1.5,
            dash_length=0.1,
        )

        # Pink dot starts at z=0, D=0.5
        moving_dot = Dot(
            point=axes.c2p(0, 0.5),
            radius=0.12,
            color=PINK_ACCENT,
        )

        # Labels for start and end
        start_label = Text("D = 0.5", font_size=16, color=PINK_ACCENT)
        start_label.next_to(axes.c2p(0, 0.5), LEFT, buff=0.3)

        self.play(
            Create(axes), Create(sigmoid), Create(threshold),
            FadeIn(s5_x_label), FadeIn(s5_y_label),
            FadeIn(moving_dot), FadeIn(start_label),
            run_time=1.5,
        )

        # Audio 08: ~8.09s
        self.add_sound(f"{AUDIO_DIR}/08_decision_clears.mp3")

        # Animate dot moving from z=0 to z=3 along sigmoid
        end_label = Text("D \u2248 0.95", font_size=16, color=SOFT_CYAN)
        end_label.next_to(axes.c2p(3, 0.95), RIGHT, buff=0.3)

        # Create path along sigmoid from z=0 to z=3
        sigmoid_path = axes.plot(
            lambda x: 1 / (1 + np.exp(-x)),
            x_range=[0, 3],
            color=PINK_ACCENT,
            stroke_width=0,
        )

        self.play(
            MoveAlongPath(moving_dot, sigmoid_path),
            FadeOut(start_label),
            run_time=3,
            rate_func=smooth,
        )
        self.play(FadeIn(end_label), run_time=0.5)

        self.wait(1)

        # Clear sigmoid part
        self.play(
            FadeOut(axes), FadeOut(sigmoid), FadeOut(threshold),
            FadeOut(s5_x_label), FadeOut(s5_y_label),
            FadeOut(moving_dot), FadeOut(end_label),
            FadeOut(new_knowledge),
            run_time=1,
        )

        # Chaos-to-order transition
        # LEFT: chaotic particles
        chaos_label = Text("Before", font_size=18, color=PINK_ACCENT)
        chaos_label.move_to(LEFT * 3.5 + UP * 2.5)

        chaos_particles = VGroup()
        np.random.seed(42)
        for _ in range(40):
            x = np.random.uniform(-5, -2)
            y = np.random.uniform(-1.5, 1.5)
            color = interpolate_color(PURPLE, PINK_ACCENT, np.random.uniform(0, 1))
            dot = Dot(
                point=[x, y, 0],
                radius=np.random.uniform(0.04, 0.09),
                color=color,
            ).set_opacity(np.random.uniform(0.5, 0.9))
            chaos_particles.add(dot)

        # RIGHT: ordered grid
        order_label = Text("After", font_size=18, color=SOFT_CYAN)
        order_label.move_to(RIGHT * 3.5 + UP * 2.5)

        order_particles = VGroup()
        for i in range(5):
            for j in range(5):
                x = 2 + i * 0.6
                y = -1.2 + j * 0.6
                dot = Dot(
                    point=[x, y, 0],
                    radius=0.06,
                    color=SOFT_CYAN,
                ).set_opacity(0.85)
                order_particles.add(dot)

        # Arrow between
        learning_arrow = Arrow(
            LEFT * 1.2, RIGHT * 1.2,
            color=GOLD,
            stroke_width=3,
        )
        learning_label = Text("Learning", font_size=18, color=GOLD)
        learning_label.next_to(learning_arrow, UP, buff=0.2)

        self.play(
            FadeIn(chaos_label),
            FadeIn(chaos_particles, lag_ratio=0.02),
            run_time=1,
        )
        self.play(
            GrowArrow(learning_arrow),
            FadeIn(learning_label),
            FadeIn(order_label),
            FadeIn(order_particles, lag_ratio=0.03),
            run_time=1.5,
        )

        # Insight text
        insight = Text(
            "Knowledge accumulates \u2192 uncertainty reduces \u2192 decision clears",
            font_size=20,
            color=WHITE_GLOW,
        ).to_edge(DOWN, buff=0.5)

        self.play(FadeIn(insight), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(chaos_label), FadeOut(chaos_particles),
            FadeOut(order_label), FadeOut(order_particles),
            FadeOut(learning_arrow), FadeOut(learning_label),
            FadeOut(insight),
            run_time=1.5,
        )

    # ─────────────────────────────────────────────────────────────
    # SCENE 6: WHY IT MATTERS — THREE PRINCIPLES (~25s)
    # ─────────────────────────────────────────────────────────────
    def why_it_matters_section(self):
        """Sequential reveal of three principles with icons"""

        # Audio 09: ~5.30s
        self.add_sound(f"{AUDIO_DIR}/09_why_matters.mp3")

        header = Text(
            "Why This Matters",
            font_size=36,
            color=WHITE_GLOW,
        ).to_edge(UP, buff=0.7)

        narration_09 = Text(
            "This is not just a shopping story.\n"
            "It is the essence of how human intelligence works.",
            font_size=20,
            color=DIM_WHITE,
            line_spacing=1.2,
        ).to_edge(DOWN, buff=0.3)

        self.play(FadeIn(header), FadeIn(narration_09), run_time=1)
        self.wait(4.5)
        self.play(FadeOut(narration_09), run_time=0.5)

        # ── Principle 1: Forward-only ──
        # Audio 10: ~6.05s
        self.add_sound(f"{AUDIO_DIR}/10_forward.mp3")

        p1_icon = Text("\u2192", font_size=40, color=CYAN)
        p1_icon.move_to(LEFT * 5.5 + UP * 1.0)
        p1_title = Text("Forward-only", font_size=24, color=CYAN)
        p1_detail = Text(
            "Knowledge only accumulates \u2014\nyou don't unsee what's in the fridge.",
            font_size=18,
            color=DIM_WHITE,
            line_spacing=1.2,
        )
        p1_group = VGroup(p1_title, p1_detail).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        p1_group.next_to(p1_icon, RIGHT, buff=0.4).align_to(p1_icon, UP)

        self.play(FadeIn(p1_icon), FadeIn(p1_group), run_time=1)
        self.wait(5.5)

        # ── Principle 2: Probabilistic ──
        # Audio 11: ~5.74s
        self.add_sound(f"{AUDIO_DIR}/11_probabilistic.mp3")

        p2_icon = Text("\u25d0", font_size=40, color=PINK_ACCENT)
        p2_icon.move_to(LEFT * 5.5 + DOWN * 0.5)
        p2_title = Text("Probabilistic", font_size=24, color=PINK_ACCENT)
        p2_detail = Text(
            "Every new piece of knowledge shifts\nthe probability of decision-making.",
            font_size=18,
            color=DIM_WHITE,
            line_spacing=1.2,
        )
        p2_group = VGroup(p2_title, p2_detail).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        p2_group.next_to(p2_icon, RIGHT, buff=0.4).align_to(p2_icon, UP)

        self.play(FadeIn(p2_icon), FadeIn(p2_group), run_time=1)
        self.wait(5.5)

        # ── Principle 3: Entropy reduction ──
        # Audio 14: ~7.30s
        self.add_sound(f"{AUDIO_DIR}/12_entropy.mp3")

        p3_icon = Text("\u25bd", font_size=40, color=GOLD)
        p3_icon.move_to(LEFT * 5.5 + DOWN * 2.0)
        p3_title = Text("Entropy reduction", font_size=24, color=GOLD)
        p3_detail = Text(
            "Intelligence reduces uncertainty\nuntil a choice becomes clear.",
            font_size=18,
            color=DIM_WHITE,
            line_spacing=1.2,
        )
        p3_group = VGroup(p3_title, p3_detail).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        p3_group.next_to(p3_icon, RIGHT, buff=0.4).align_to(p3_icon, UP)

        self.play(FadeIn(p3_icon), FadeIn(p3_group), run_time=1)
        self.wait(5)

        # Clear
        self.play(
            FadeOut(header),
            FadeOut(p1_icon), FadeOut(p1_group),
            FadeOut(p2_icon), FadeOut(p2_group),
            FadeOut(p3_icon), FadeOut(p3_group),
            run_time=1.5,
        )

    # ─────────────────────────────────────────────────────────────
    # SCENE 7: BINARY VS SKA TRAJECTORY (~22s)
    # ─────────────────────────────────────────────────────────────
    def binary_vs_ska_section(self):
        """Split-screen: binary view (left) vs SKA trajectory (right)"""

        # Audio 12: ~11.57s
        self.add_sound(f"{AUDIO_DIR}/13_binary_vs_ska.mp3")

        # Narration subtitle
        narration_12 = Text(
            "Most people explain decisions as binary. But that skips the trajectory \u2014\n"
            "the gradual shift of probability that is the real process of intelligence.",
            font_size=18,
            color=DIM_WHITE,
            line_spacing=1.2,
        ).to_edge(DOWN, buff=0.3)

        # Divider line
        divider = DashedLine(
            UP * 3.5, DOWN * 3.5,
            color=DIM_WHITE,
            stroke_width=1,
            dash_length=0.15,
        )
        self.play(Create(divider), FadeIn(narration_12), run_time=0.5)

        # ── LEFT: Binary view ──
        binary_header = Text("Binary view", font_size=22, color=CYAN)
        binary_header.move_to(LEFT * 3.5 + UP * 2.8)

        # Two state boxes
        state_empty = RoundedRectangle(
            width=2.0, height=0.8, corner_radius=0.1,
            color=DIM_WHITE, stroke_width=1.5,
        ).move_to(LEFT * 4.5 + UP * 0.8)
        state_empty_text = Text("empty", font_size=18, color=DIM_WHITE)
        state_empty_text.move_to(state_empty)

        state_go = RoundedRectangle(
            width=2.0, height=0.8, corner_radius=0.1,
            color=DIM_WHITE, stroke_width=1.5,
        ).move_to(LEFT * 2.0 + UP * 0.8)
        state_go_text = Text("go", font_size=18, color=DIM_WHITE)
        state_go_text.move_to(state_go)

        binary_arrow = Arrow(
            state_empty.get_right(), state_go.get_left(),
            color=DIM_WHITE, stroke_width=2, buff=0.1,
        )

        binary_quote = Text(
            '"I went because the\n fridge was empty."',
            font_size=14,
            color=DIM_WHITE,
            slant=ITALIC,
            line_spacing=1.2,
        ).move_to(LEFT * 3.5 + DOWN * 0.8)

        self.play(
            FadeIn(binary_header),
            FadeIn(state_empty), FadeIn(state_empty_text),
            GrowArrow(binary_arrow),
            FadeIn(state_go), FadeIn(state_go_text),
            run_time=1.5,
        )
        self.play(FadeIn(binary_quote), run_time=0.5)

        # Cross overlay
        cross_target = VGroup(state_empty, binary_arrow, state_go)
        cross = Cross(cross_target, color=PINK_ACCENT, stroke_width=3)
        self.play(Create(cross), run_time=0.8)

        # ── RIGHT: SKA view ──
        ska_header = Text("SKA view", font_size=22, color=CYAN)
        ska_header.move_to(RIGHT * 3.5 + UP * 2.8)

        # Sigmoid curve on right side (compact version of reference design)
        ska_axes = Axes(
            x_range=[-6, 6, 2],
            y_range=[0, 1.2, 0.5],
            x_length=5,
            y_length=2.8,
            axis_config={"color": DIM_WHITE, "stroke_width": 2},
            tips=False,
        ).move_to(RIGHT * 3.5 + UP * 0.3)

        ska_x_label = MathTex("z", font_size=24, color=CYAN).next_to(ska_axes.x_axis, RIGHT, buff=0.15)
        ska_y_label = MathTex("D", font_size=24, color=PINK_ACCENT).next_to(ska_axes.y_axis, UP, buff=0.15)

        ska_sigmoid = ska_axes.plot(
            lambda x: 1 / (1 + np.exp(-x)),
            x_range=[-6, 6],
            color=CYAN,
            stroke_width=4,
        )

        ska_threshold = DashedLine(
            start=ska_axes.c2p(-6, 0.5),
            end=ska_axes.c2p(6, 0.5),
            color=GOLD,
            stroke_width=1.5,
            dash_length=0.1,
        )

        # Traveling dot
        ska_dot = Dot(
            point=ska_axes.c2p(-5, 1 / (1 + np.exp(5))),
            radius=0.12,
            color=PINK_ACCENT,
        )

        self.play(
            FadeIn(ska_header),
            Create(ska_axes),
            FadeIn(ska_x_label), FadeIn(ska_y_label),
            Create(ska_sigmoid),
            Create(ska_threshold),
            run_time=1.5,
        )

        # Animate dot traveling along sigmoid
        ska_path = ska_axes.plot(
            lambda x: 1 / (1 + np.exp(-x)),
            x_range=[-5, 5],
            color=PINK_ACCENT,
            stroke_width=0,
        )

        # Glow trail
        trail = ska_axes.plot(
            lambda x: 1 / (1 + np.exp(-x)),
            x_range=[-5, 5],
            color=PINK_ACCENT,
            stroke_width=4,
        ).set_opacity(0.4)

        self.play(
            FadeIn(ska_dot),
            run_time=0.3,
        )
        self.play(
            MoveAlongPath(ska_dot, ska_path),
            Create(trail),
            run_time=3,
            rate_func=smooth,
        )

        # Insight text (replaces narration subtitle)
        insight = Text(
            "Intelligence = the trajectory of probability updates",
            font_size=20,
            color=WHITE_GLOW,
        ).to_edge(DOWN, buff=0.5)

        self.play(FadeOut(narration_12), FadeIn(insight), run_time=1)
        self.wait(4)

        # Clear
        self.play(
            FadeOut(divider),
            FadeOut(binary_header), FadeOut(binary_quote),
            FadeOut(state_empty), FadeOut(state_empty_text),
            FadeOut(binary_arrow),
            FadeOut(state_go), FadeOut(state_go_text),
            FadeOut(cross),
            FadeOut(ska_header), FadeOut(ska_axes),
            FadeOut(ska_x_label), FadeOut(ska_y_label),
            FadeOut(ska_sigmoid), FadeOut(ska_threshold),
            FadeOut(ska_dot), FadeOut(trail),
            FadeOut(insight),
            run_time=1.5,
        )

    # ─────────────────────────────────────────────────────────────
    # SCENE 8: TAKEAWAY (~15s)
    # ─────────────────────────────────────────────────────────────
    def takeaway_section(self):
        """Final philosophical statement"""

        # Audio 13: ~8s
        self.add_sound(f"{AUDIO_DIR}/14_takeaway.mp3")

        takeaway1 = Text(
            "Every human decision \u2014 from the fridge to life-changing decisions \u2014",
            font_size=22,
            color=WHITE_GLOW,
        ).move_to(UP * 0.8)

        takeaway2 = Text(
            "is probabilistic.",
            font_size=30,
            color=CYAN,
        ).next_to(takeaway1, DOWN, buff=0.4)

        takeaway3 = Text(
            "SKA doesn't mimic this \u2014 it formalizes it.",
            font_size=24,
            color=PINK_ACCENT,
            slant=ITALIC,
        ).next_to(takeaway2, DOWN, buff=0.6)

        self.play(FadeIn(takeaway1, shift=DOWN * 0.2), run_time=1.5)
        self.play(FadeIn(takeaway2, shift=DOWN * 0.2), run_time=1.5)
        self.wait(1)
        self.play(FadeIn(takeaway3, shift=DOWN * 0.2), run_time=1.5)

        self.wait(6)

        self.play(
            FadeOut(takeaway1), FadeOut(takeaway2), FadeOut(takeaway3),
            run_time=1.5,
        )

    # ─────────────────────────────────────────────────────────────
    # SCENE 9: END CARD (~8s)
    # ─────────────────────────────────────────────────────────────
    def end_card(self):
        """Credits"""

        title = Text(
            "The Fridge Case",
            font_size=42,
            color=WHITE_GLOW,
        )

        author = Text(
            "Bouarfa Mahi",
            font_size=32,
            color=CYAN,
        ).next_to(title, DOWN, buff=0.5)

        org = Text(
            "Quantiota",
            font_size=28,
            color=PURPLE,
        ).next_to(author, DOWN, buff=0.2)

        email = Text(
            "info@quantiota.org",
            font_size=20,
            color=DIM_WHITE,
        ).next_to(org, DOWN, buff=0.4)

        year = Text(
            "February 2026",
            font_size=20,
            color=DIM_WHITE,
        ).next_to(email, DOWN, buff=0.2)

        end_group = VGroup(title, author, org, email, year)

        self.play(
            FadeIn(title, shift=UP * 0.3),
            run_time=1,
        )
        self.play(
            FadeIn(author),
            FadeIn(org),
            FadeIn(email),
            FadeIn(year),
            run_time=1.5,
        )

        self.wait(4)
        self.play(FadeOut(end_group), run_time=2)


if __name__ == "__main__":
    import subprocess
    subprocess.run(["manim", "-qh", __file__, "FridgeCaseVideo"])
