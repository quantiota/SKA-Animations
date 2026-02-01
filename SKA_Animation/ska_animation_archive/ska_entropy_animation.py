"""
SKA Entropy as a Local Field - Manim Animation
Author: Based on paper by Bouarfa Mahi, Quantiota (January 2026)

Requirements:
    pip install manim
    
Run with:
    manim -pqh ska_entropy_animation.py SKAEntropyVideo
    
For lower quality preview:
    manim -pql ska_entropy_animation.py SKAEntropyVideo
"""

from manim import *
import numpy as np

# Color palette - deep blues, purples, cyan accents (as ManimColor)
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
            # Random position in 3D-like distribution
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


class ConnectionLines(VGroup):
    """Creates connection lines between nearby neural points"""
    
    def __init__(self, points, max_dist=1.2, **kwargs):
        super().__init__(**kwargs)
        
        positions = [p.get_center() for p in points]
        
        for i, p1 in enumerate(positions[:50]):  # Limit for performance
            for j, p2 in enumerate(positions[:50]):
                if i < j:
                    dist = np.linalg.norm(np.array(p1) - np.array(p2))
                    if dist < max_dist:
                        line = Line(
                            p1, p2,
                            stroke_width=0.5,
                            stroke_opacity=0.2 * (1 - dist / max_dist),
                            color=CYAN
                        )
                        self.add(line)


class SKAEntropyVideo(Scene):
    """Main animation scene for SKA Entropy as a Local Field"""
    
    def construct(self):
        # Set dark background
        self.camera.background_color = DEEP_BLUE
        
        # Run all sections
        self.intro_section()
        self.volume_element_section()
        self.density_encoding_section()
        self.universality_section()
        self.finale_section()
        self.end_card()
    
    def intro_section(self):
        """0-15s: Cosmic zoom into neural field"""

        # Create neural field
        neural_field = NeuralField(n_points=300, radius=5)
        neural_field.scale(0.1).set_opacity(0)

        # Title text
        title = Text(
            "SKA Entropy as a Local Field",
            font_size=48,
            color=WHITE_GLOW
        ).to_edge(UP, buff=0.8)

        author = Text(
            "Bouarfa Mahi • Quantiota • 2026",
            font_size=24,
            color=DIM_WHITE
        ).next_to(title, DOWN, buff=0.3)

        # Narration text 1
        narration1 = Text(
            "In classical information theory, entropy measures\nglobal uncertainty over an entire distribution.",
            font_size=28,
            color=WHITE_GLOW,
            line_spacing=1.2
        ).to_edge(DOWN, buff=0.3)

        # Animate intro
        self.play(
            neural_field.animate.scale(10).set_opacity(1),
            run_time=3,
            rate_func=smooth
        )

        # Add subtle pulsing
        self.play(
            FadeIn(title, shift=DOWN * 0.3),
            FadeIn(author, shift=DOWN * 0.2),
            run_time=1.5
        )

        # Audio 1: 6.72s
        self.add_sound("/home/coder/manim/audio/01_intro_classical.mp3")
        self.play(FadeIn(narration1), run_time=1)
        self.wait(5.72)  # 6.72 - 1 for fade

        # Narration text 2
        narration2 = Text(
            "SKA takes a different approach: entropy is defined locally,\nat each point in the neural medium.",
            font_size=28,
            color=WHITE_GLOW,
            line_spacing=1.2
        ).to_edge(DOWN, buff=0.3)

        # Audio 2: 6.58s
        self.add_sound("/home/coder/manim/audio/02_intro_ska.mp3")
        self.play(
            FadeOut(narration1),
            FadeIn(narration2),
            run_time=1
        )
        self.wait(5.58)  # 6.58 - 1 for fade

        # Clear for next section
        self.play(
            FadeOut(title),
            FadeOut(author),
            FadeOut(narration2),
            FadeOut(neural_field),
            run_time=1.5
        )
    
    def volume_element_section(self):
        """15-35s: Volume element with tensors"""
        
        # Create a cube representing volume element
        cube = Cube(side_length=2.5, fill_opacity=0.1, stroke_width=2)
        cube.set_color(CYAN)
        cube.set_stroke(CYAN, opacity=0.6)
        cube.shift(UP * 0.8)
        
        # Position label
        r_label = MathTex(r"\text{position } \mathbf{r}", font_size=36, color=WHITE_GLOW)
        r_label.next_to(cube, UP, buff=0.5)
        
        # Neurons inside cube
        neurons = VGroup()
        for _ in range(25):
            pos = np.random.uniform(-1, 1, 3)
            pos[2] *= 0.3  # Flatten z
            neuron = Dot(
                point=pos[:2].tolist() + [0],
                radius=0.08,
                color=SOFT_CYAN
            ).set_opacity(0.8)
            neurons.add(neuron)
        neurons.shift(UP * 0.8)
        
        self.play(
            Create(cube),
            FadeIn(r_label),
            run_time=1.5
        )
        self.play(FadeIn(neurons, lag_ratio=0.05), run_time=1)

        # Narration
        narration1 = Text(
            "Consider a volume element at position r,\ncontaining n(r) neurons.",
            font_size=28,
            color=WHITE_GLOW,
            line_spacing=1.2
        ).to_edge(DOWN, buff=0.3)

        # Audio 3: 5.28s
        self.add_sound("/home/coder/manim/audio/03_volume_element.mp3")
        self.play(FadeIn(narration1), run_time=0.8)
        self.wait(4.48)  # 5.28 - 0.8
        
        # Knowledge tensor visualization (arrows)
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
                max_tip_length_to_length_ratio=0.3
            )
            z_arrows.add(arrow)
        
        z_label = MathTex(r"\mathbf{z}(\mathbf{r})", font_size=32, color=PINK_ACCENT)
        z_label.to_corner(UL, buff=0.8).shift(RIGHT * 1.5)
        z_text = Text("Knowledge Tensor", font_size=20, color=PINK_ACCENT)
        z_text.next_to(z_label, DOWN, buff=0.2)
        
        self.play(
            FadeOut(narration1),
            Create(z_arrows, lag_ratio=0.1),
            FadeIn(z_label),
            FadeIn(z_text),
            run_time=1.5
        )
        
        # Decision probability tensor (clouds)
        d_clouds = VGroup()
        for neuron in neurons[:12]:
            cloud = Circle(
                radius=0.25,
                fill_opacity=0.2,
                stroke_opacity=0.4,
                color=PURPLE
            ).move_to(neuron.get_center())
            d_clouds.add(cloud)
        
        d_label = MathTex(r"D(\mathbf{r})", font_size=32, color=PURPLE)
        d_label.to_corner(UR, buff=0.8).shift(LEFT * 1.5)
        d_text = Text("Decision Probability Tensor", font_size=20, color=PURPLE)
        d_text.next_to(d_label, DOWN, buff=0.2)
        
        narration2 = Text(
            "We define the knowledge tensor z(r)\nand the decision probability tensor D(r).",
            font_size=28,
            color=WHITE_GLOW,
            line_spacing=1.2
        ).to_edge(DOWN, buff=0.3)

        # Audio 4: 5.57s
        self.add_sound("/home/coder/manim/audio/04_tensors.mp3")
        self.play(
            FadeIn(d_clouds, lag_ratio=0.1),
            FadeIn(d_label),
            FadeIn(d_text),
            FadeIn(narration2),
            run_time=1.5
        )
        self.wait(4.07)  # 5.57 - 1.5
        
        # Show delta D (learning step)
        delta_arrows = VGroup()
        for arrow in z_arrows:
            start = arrow.get_end()
            direction = np.random.uniform(-1, 1, 2) * 0.2
            delta = Arrow(
                start,
                start + [direction[0], direction[1], 0],
                buff=0,
                stroke_width=2,
                color=CYAN,
                max_tip_length_to_length_ratio=0.4
            )
            delta_arrows.add(delta)
        
        narration3 = Text(
            "During a learning step, decisions shift by ΔD.",
            font_size=28,
            color=WHITE_GLOW
        ).to_edge(DOWN, buff=0.3)

        # Audio 5: 3.82s
        self.add_sound("/home/coder/manim/audio/05_learning_step.mp3")
        self.play(
            FadeOut(narration2),
            FadeIn(narration3),
            Create(delta_arrows, lag_ratio=0.1),
            run_time=1.5
        )
        self.wait(2.32)  # 3.82 - 1.5
        
        # Show the formula
        formula = MathTex(
            r"h(\mathbf{r}) = -\frac{1}{\ln 2} \, \mathbf{z}(\mathbf{r}) \cdot \Delta D(\mathbf{r})",
            font_size=40,
            color=WHITE_GLOW
        )
        formula_box = SurroundingRectangle(formula, color=CYAN, buff=0.3, stroke_width=2)
        formula_group = VGroup(formula, formula_box).to_edge(DOWN, buff=1.5)
        
        narration4 = Text(
            "The local entropy density is their dot product.",
            font_size=26,
            color=WHITE_GLOW
        ).next_to(formula_group, DOWN, buff=0.3)

        # Audio 6: 3.31s
        self.add_sound("/home/coder/manim/audio/06_dot_product.mp3")
        self.play(
            FadeOut(narration3),
            FadeIn(formula_group),
            FadeIn(narration4),
            run_time=1.5
        )
        self.wait(1.81)  # 3.31 - 1.5
        
        # Clear
        self.play(
            FadeOut(cube), FadeOut(r_label), FadeOut(neurons),
            FadeOut(z_arrows), FadeOut(z_label), FadeOut(z_text),
            FadeOut(d_clouds), FadeOut(d_label), FadeOut(d_text),
            FadeOut(delta_arrows), FadeOut(formula_group), FadeOut(narration4),
            run_time=1.5
        )
    
    def density_encoding_section(self):
        """35-55s: Implicit density encoding"""
        
        # Title
        section_title = Text(
            "Implicit Encoding of Neuron Density",
            font_size=36,
            color=CYAN
        ).to_edge(UP, buff=0.5)
        
        self.play(FadeIn(section_title), run_time=1)
        
        # Sparse region (left)
        sparse_box = Square(side_length=2.5, color=PURPLE, stroke_width=2)
        sparse_box.set_fill(PURPLE, opacity=0.1)
        sparse_box.shift(LEFT * 3)
        
        sparse_neurons = VGroup()
        for _ in range(8):
            pos = np.random.uniform(-1, 1, 2)
            neuron = Dot(point=[pos[0] - 3, pos[1], 0], radius=0.1, color=DIM_WHITE)
            neuron.set_opacity(0.5)
            sparse_neurons.add(neuron)
        
        sparse_label = Text("Sparse Region", font_size=24, color=DIM_WHITE)
        sparse_label.next_to(sparse_box, DOWN, buff=0.3)
        
        sparse_h = MathTex(r"|h(\mathbf{r})| \approx \text{small}", font_size=24, color=DIM_WHITE)
        sparse_h.next_to(sparse_label, DOWN, buff=0.2)
        
        # Dense region (right)
        dense_box = Square(side_length=2.5, color=CYAN, stroke_width=2)
        dense_box.set_fill(CYAN, opacity=0.15)
        dense_box.shift(RIGHT * 3)
        
        dense_neurons = VGroup()
        for _ in range(50):
            pos = np.random.uniform(-1, 1, 2)
            neuron = Dot(point=[pos[0] + 3, pos[1], 0], radius=0.08, color=SOFT_CYAN)
            neuron.set_opacity(0.9)
            dense_neurons.add(neuron)
        
        dense_label = Text("Dense Region", font_size=24, color=SOFT_CYAN)
        dense_label.next_to(dense_box, DOWN, buff=0.3)
        
        dense_h = MathTex(r"|h(\mathbf{r})| \approx \text{large}", font_size=24, color=SOFT_CYAN)
        dense_h.next_to(dense_label, DOWN, buff=0.2)
        
        # Animate
        self.play(
            Create(sparse_box), Create(dense_box),
            run_time=1
        )
        self.play(
            FadeIn(sparse_neurons, lag_ratio=0.1),
            FadeIn(dense_neurons, lag_ratio=0.02),
            run_time=1.5
        )
        self.play(
            FadeIn(sparse_label), FadeIn(sparse_h),
            FadeIn(dense_label), FadeIn(dense_h),
            run_time=1
        )
        
        # Narration
        narration1 = Text(
            "Neuron density needs no explicit variable.",
            font_size=28,
            color=WHITE_GLOW
        ).to_edge(DOWN, buff=0.3)

        # Audio 7: 3.38s
        self.add_sound("/home/coder/manim/audio/07_density_intro.mp3")
        self.play(FadeIn(narration1), run_time=0.8)
        self.wait(2.58)  # 3.38 - 0.8
        
        # Show equation
        eq1 = MathTex(
            r"n(\mathbf{r}) = \rho(\mathbf{r}) \cdot dV",
            font_size=32,
            color=WHITE_GLOW
        ).shift(DOWN * 0.5)
        
        narration2 = Text(
            "The dot product sums over n(r) terms automatically.",
            font_size=28,
            color=WHITE_GLOW
        ).to_edge(DOWN, buff=0.3)

        # Audio 8: 3.96s
        self.add_sound("/home/coder/manim/audio/08_density_sum.mp3")
        self.play(
            FadeOut(narration1),
            FadeIn(eq1),
            FadeIn(narration2),
            run_time=1
        )
        self.wait(2.96)  # 3.96 - 1
        
        # Expanded sum
        eq2 = MathTex(
            r"h(\mathbf{r}) = -\frac{1}{\ln 2} \sum_{i=1}^{n(\mathbf{r})} z_i(\mathbf{r}) \cdot \Delta D_i(\mathbf{r})",
            font_size=32,
            color=WHITE_GLOW
        ).shift(DOWN * 0.5)
        
        narration3 = Text(
            "Denser regions produce proportionally smaller entropy—\ndensity is implicit in the structure itself.",
            font_size=26,
            color=WHITE_GLOW,
            line_spacing=1.2
        ).to_edge(DOWN, buff=0.3)

        # Audio 9: 6.58s
        self.add_sound("/home/coder/manim/audio/09_density_implicit.mp3")
        self.play(
            TransformMatchingTex(eq1, eq2),
            FadeOut(narration2),
            FadeIn(narration3),
            run_time=1.5
        )

        # Pulse dense region
        self.play(
            dense_box.animate.set_stroke(width=4),
            dense_neurons.animate.set_opacity(1),
            run_time=0.5
        )
        self.play(
            dense_box.animate.set_stroke(width=2),
            run_time=0.5
        )

        self.wait(4.08)  # 6.58 - 1.5 - 0.5 - 0.5
        
        # Clear
        self.play(
            FadeOut(section_title),
            FadeOut(sparse_box), FadeOut(sparse_neurons),
            FadeOut(sparse_label), FadeOut(sparse_h),
            FadeOut(dense_box), FadeOut(dense_neurons),
            FadeOut(dense_label), FadeOut(dense_h),
            FadeOut(eq2), FadeOut(narration3),
            run_time=1.5
        )
    
    def universality_section(self):
        """55-70s: Universality across dimensions"""
        
        # Title
        title = Text("Universality", font_size=42, color=CYAN)
        title.to_edge(UP, buff=0.5)
        
        self.play(FadeIn(title), run_time=1)
        
        # Discrete layered network
        layers = VGroup()
        layer_positions = [-3, -1.5, 0, 1.5, 3]
        
        for i, x in enumerate(layer_positions):
            n_nodes = [4, 6, 8, 6, 4][i]
            layer = VGroup()
            for j in range(n_nodes):
                y = (j - (n_nodes - 1) / 2) * 0.6
                node = Circle(radius=0.15, color=PURPLE, fill_opacity=0.6)
                node.move_to([x, y, 0])
                layer.add(node)
            layers.add(layer)
        
        # Connections between layers
        connections = VGroup()
        for i in range(len(layers) - 1):
            for node1 in layers[i]:
                for node2 in layers[i + 1]:
                    line = Line(
                        node1.get_center(), node2.get_center(),
                        stroke_width=0.5, stroke_opacity=0.3, color=CYAN
                    )
                    connections.add(line)
        
        discrete_label = Text("Discrete Layers", font_size=24, color=DIM_WHITE)
        discrete_label.to_edge(DOWN, buff=2)
        
        discrete_eq = MathTex(
            r"h^{(l)} = -\frac{1}{\ln 2} \mathbf{z}^{(l)} \cdot \Delta D^{(l)}",
            font_size=28,
            color=WHITE_GLOW
        ).to_edge(DOWN, buff=1)
        
        self.play(
            Create(connections),
            FadeIn(layers, lag_ratio=0.1),
            FadeIn(discrete_label),
            FadeIn(discrete_eq),
            run_time=2
        )
        self.wait(1.5)
        
        # Transform to continuous field
        continuous_field = VGroup()
        for _ in range(150):
            x = np.random.uniform(-4, 4)
            y = np.random.uniform(-2, 2)
            dot = Dot(
                point=[x, y, 0],
                radius=np.random.uniform(0.03, 0.08),
                color=interpolate_color(PURPLE, CYAN, np.random.uniform(0, 1))
            ).set_opacity(np.random.uniform(0.4, 0.9))
            continuous_field.add(dot)
        
        continuous_label = Text("Continuous Field (D=3)", font_size=24, color=DIM_WHITE)
        continuous_label.to_edge(DOWN, buff=2)
        
        continuous_eq = MathTex(
            r"h(\mathbf{r}) = -\frac{1}{\ln 2} \mathbf{z}(\mathbf{r}) \cdot \Delta D(\mathbf{r})",
            font_size=28,
            color=WHITE_GLOW
        ).to_edge(DOWN, buff=1)
        
        self.play(
            ReplacementTransform(layers, continuous_field),
            FadeOut(connections),
            ReplacementTransform(discrete_label, continuous_label),
            TransformMatchingTex(discrete_eq, continuous_eq),
            run_time=2
        )
        self.wait(1)
        
        # Higher dimensions
        dim_labels = ["D = 4", "D = 5", "D = ..."]
        
        for dim_text in dim_labels:
            new_label = Text(f"Continuous Field ({dim_text})", font_size=24, color=DIM_WHITE)
            new_label.to_edge(DOWN, buff=2)
            
            # Subtle field shift
            self.play(
                continuous_field.animate.shift(UP * 0.1).shift(DOWN * 0.1),
                ReplacementTransform(continuous_label, new_label),
                run_time=0.8
            )
            continuous_label = new_label
            self.wait(0.5)
        
        # Final narration
        narration = Text(
            "The identical equation—in any spatial dimension.\nOne formula. Any geometry.",
            font_size=26,
            color=WHITE_GLOW,
            line_spacing=1.2
        ).shift(UP * 2.5)

        # Audio 10: 6.12s
        self.add_sound("/home/coder/manim/audio/10_universality.mp3")
        self.play(FadeIn(narration), run_time=1)
        self.wait(5.12)  # 6.12 - 1
        
        # Clear
        self.play(
            FadeOut(title), FadeOut(continuous_field),
            FadeOut(continuous_label), FadeOut(continuous_eq),
            FadeOut(narration),
            run_time=1.5
        )
    
    def finale_section(self):
        """70-90s: Entropy field and gradients"""
        
        # Create a scalar field visualization
        field_dots = VGroup()
        gradient_arrows = VGroup()
        
        # Create field with varying "entropy" values
        for i in range(-8, 9):
            for j in range(-4, 5):
                x, y = i * 0.5, j * 0.5
                
                # Higher values near center-right (hub)
                hub_x, hub_y = 1.5, 0
                dist_to_hub = np.sqrt((x - hub_x)**2 + (y - hub_y)**2)
                intensity = np.exp(-dist_to_hub / 2)
                
                dot = Dot(
                    point=[x, y, 0],
                    radius=0.08 + 0.1 * intensity,
                    color=interpolate_color(PURPLE, CYAN, intensity)
                ).set_opacity(0.4 + 0.5 * intensity)
                field_dots.add(dot)
                
                # Gradient arrows pointing toward hub
                if dist_to_hub > 0.5 and np.random.random() > 0.7:
                    direction = np.array([hub_x - x, hub_y - y, 0])
                    direction = direction / np.linalg.norm(direction) * 0.3 * intensity
                    arrow = Arrow(
                        [x, y, 0],
                        [x + direction[0], y + direction[1], 0],
                        buff=0,
                        stroke_width=1.5,
                        color=PINK_ACCENT,
                        max_tip_length_to_length_ratio=0.3
                    ).set_opacity(0.6)
                    gradient_arrows.add(arrow)
        
        # Hub glow
        hub_glow = Circle(radius=1, color=CYAN, fill_opacity=0.3, stroke_opacity=0.8)
        hub_glow.move_to([1.5, 0, 0])
        
        hub_label = Text("Knowledge Hub", font_size=20, color=CYAN)
        hub_label.next_to(hub_glow, UP, buff=0.3)
        
        # Animate
        self.play(FadeIn(field_dots, lag_ratio=0.005), run_time=2)
        
        narration1 = Text(
            "High-density regions have greater capacity to reduce entropy—\nbecoming natural hubs for knowledge accumulation.",
            font_size=24,
            color=WHITE_GLOW,
            line_spacing=1.2
        ).to_edge(DOWN, buff=0.3)

        # Audio 11: 7.51s
        self.add_sound("/home/coder/manim/audio/11_hubs.mp3")
        self.play(
            FadeIn(hub_glow),
            FadeIn(hub_label),
            FadeIn(narration1),
            run_time=1.5
        )
        self.wait(6.01)  # 7.51 - 1.5
        
        # Show gradient
        grad_label = MathTex(r"\nabla h(\mathbf{r})", font_size=32, color=PINK_ACCENT)
        grad_label.to_corner(UL, buff=0.5).shift(RIGHT * 1.5)
        grad_text = Text("Entropy Gradient", font_size=20, color=PINK_ACCENT)
        grad_text.next_to(grad_label, DOWN, buff=0.2)
        
        narration2 = Text(
            "The gradient ∇h(r) guides information flow.",
            font_size=26,
            color=WHITE_GLOW
        ).to_edge(DOWN, buff=0.3)

        # Audio 12: 2.98s
        self.add_sound("/home/coder/manim/audio/12_gradient.mp3")
        self.play(
            FadeOut(narration1),
            Create(gradient_arrows, lag_ratio=0.02),
            FadeIn(grad_label),
            FadeIn(grad_text),
            FadeIn(narration2),
            run_time=2
        )
        self.wait(0.98)  # 2.98 - 2
        
        # Final statement
        narration3 = Text(
            "The system self-regulates—\nby local capacity.",
            font_size=28,
            color=WHITE_GLOW,
            line_spacing=1.2
        ).to_edge(DOWN, buff=0.3)

        # Audio 13: 3.36s
        self.add_sound("/home/coder/manim/audio/13_self_regulates.mp3")
        self.play(
            FadeOut(narration2),
            FadeIn(narration3),
            hub_glow.animate.scale(1.2).set_opacity(0.5),
            run_time=1.5
        )
        self.wait(1.86)  # 3.36 - 1.5
        
        # Final poetic line
        final_text = Text(
            "Entropy, reimagined—\nnot as a global summary,\nbut as a living, breathing field.",
            font_size=30,
            color=WHITE_GLOW,
            line_spacing=1.3
        ).shift(UP * 2)

        # Audio 14: 5.93s
        self.add_sound("/home/coder/manim/audio/14_finale.mp3")
        self.play(
            FadeOut(narration3),
            FadeIn(final_text),
            run_time=1.5
        )
        self.wait(4.43)  # 5.93 - 1.5
        
        # Clear
        self.play(
            FadeOut(field_dots), FadeOut(gradient_arrows),
            FadeOut(hub_glow), FadeOut(hub_label),
            FadeOut(grad_label), FadeOut(grad_text),
            FadeOut(final_text),
            run_time=2
        )
    
    def end_card(self):
        """End card with title and credits"""
        
        title = Text(
            "SKA Entropy as a Local Field",
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
            "January 2026",
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
        
        self.wait(3)
        
        # Fade out
        self.play(FadeOut(end_group), run_time=2)


# Additional scene for just the formula animation
class FormulaHighlight(Scene):
    """Standalone scene highlighting the main formula"""
    
    def construct(self):
        self.camera.background_color = DEEP_BLUE
        
        formula = MathTex(
            r"h(\mathbf{r}) = -\frac{1}{\ln 2} \, \mathbf{z}(\mathbf{r}) \cdot \Delta D(\mathbf{r})",
            font_size=56,
            color=WHITE_GLOW
        )
        
        box = SurroundingRectangle(formula, color=CYAN, buff=0.4, stroke_width=3)
        
        # Labels
        h_label = Text("Local Entropy Density", font_size=24, color=CYAN)
        h_label.next_to(formula, UP, buff=1)
        h_arrow = Arrow(h_label.get_bottom(), formula[0][0].get_top(), color=CYAN, buff=0.2)
        
        z_label = Text("Knowledge Tensor", font_size=24, color=PINK_ACCENT)
        z_label.next_to(formula, DOWN, buff=1).shift(LEFT * 2)
        
        d_label = Text("Decision Change", font_size=24, color=PURPLE)
        d_label.next_to(formula, DOWN, buff=1).shift(RIGHT * 2)
        
        self.play(Write(formula), Create(box), run_time=2)
        self.wait(1)
        
        self.play(
            FadeIn(h_label), Create(h_arrow),
            FadeIn(z_label), FadeIn(d_label),
            run_time=1.5
        )
        
        self.wait(3)


if __name__ == "__main__":
    # This allows running directly with: python ska_entropy_animation.py
    import subprocess
    subprocess.run(["manim", "-pqh", __file__, "SKAEntropyVideo"])