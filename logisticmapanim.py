from manim import *

class LogisticMapConvergence(Scene):
    def construct(self):
        r = 4
        xi = 0.611260467
        def func(x): return r*x*(1 - x)

        axis_params = {
            'x_range': [0, 1.5, 0.5],
            'y_range': [0, 1.5, 0.5],
            'x_length': 6,
            'y_length': 6,
        }
        x_axes = Axes(**axis_params)
        y_axes = x_axes.copy().rotate(PI/2).flip()

        x_curve = x_axes.get_graph(func, [0, 1]).set_color(RED)
        y_curve = y_axes.get_graph(func, [0, 1]).set_color(BLUE)

        self.play(Create(x_axes), Create(y_axes))
        self.play(Create(x_curve), Create(y_curve))

        x_cur = xi
        init_pt = x_axes.coords_to_point(x_cur, 0)

        dot = Dot(init_pt)
        
        def update_trace(trace: Line):
            curr_start = trace.get_start()
            if np.all(curr_start == dot.get_center()): return
            trace.put_start_and_end_on(curr_start, dot.get_center())

        def start_trace():
            trace = Line(dot.get_center(), dot.get_center()).scale(1)
            trace.add_updater(update_trace)
            self.add(trace)
            return trace

        def stop_trace(trace: Line):
            trace.clear_updaters()

        self.play(Create(dot))

        traces = []
        current_axes = x_axes

        def switch_axes(axes):
            if axes == x_axes:
                return y_axes
            elif axes == y_axes:
                return x_axes
            else:
                raise ValueError('invalid axes')

        def move_to_axes_coord(dot, axes, x, y):
            current_loc = dot.get_center()
            target_loc = axes.coords_to_point(x, y)
            shift_vector = target_loc - current_loc
            return dot.animate.shift(shift_vector)

        for _ in range(15):
            animations = [move_to_axes_coord(
                dot,
                current_axes,
                x_cur,
                func(x_cur),
            )]
            if len(traces) > 6:
                animations.append(FadeOut(traces.pop(0)))

            traces.append(start_trace())
            self.play(*animations)
            stop_trace(traces[-1])

            current_axes = switch_axes(current_axes)
            x_cur = func(x_cur)
        
        self.wait()
