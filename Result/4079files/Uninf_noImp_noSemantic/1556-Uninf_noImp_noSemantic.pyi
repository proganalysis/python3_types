from typing import Any

def add_spheres_to_mayavi_window(sphere_coords: Any, radii: Any, color: Any = ..., resolution: float = ..., mode: str = ...) -> None: ...
def add_synapses_to_mayavi_window(syns: Any, synapse_location: str = ..., color: Any = ..., diameter_scale: float = ..., all_same_size: float = ...) -> None: ...
def get_different_rgba_colors(num_colors: Any, rgb_only: bool = ..., set_alpha: float = ...): ...
def visualize_anno_with_synapses(anno: Any, syns: Any) -> None: ...
def is_iterable_of_iterables(item: Any): ...
def add_anno_to_mayavi_window(anno: Any, node_scaling: float = ..., override_node_radius: float = ..., edge_radius: float = ..., show_outline: bool = ..., dataset_identifier: str = ..., opacity: int = ...) -> None: ...
def visualize_annotation(anno: Any, node_scaling: float = ..., override_node_radius: float = ..., edge_radius: float = ..., bg_color: Any = ..., dataset_identifier: str = ..., show_outline: bool = ..., figure_size_px: Any = ...) -> None: ...