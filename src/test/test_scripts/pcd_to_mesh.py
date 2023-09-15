import os
import numpy as np
import open3d as o3d  # >= 0.14.1
from pymeshfix import _meshfix
import pyvista as pv

script_path = os.path.dirname(os.path.abspath(__file__))
pcd_path = os.path.join(script_path, '..', 'objects', 'pcd_to_mesh', 'pcd_0.ply')
bounding_box_array = np.load(os.path.join(script_path, 'transformation_matrices', 'reconstruction_bounding_box_array_in_base.npy'))

bounding_box = o3d.geometry.OrientedBoundingBox.create_from_points(points=o3d.utility.Vector3dVector(bounding_box_array))
world_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.1, origin=[0, 0, 0])
pcd = o3d.io.read_point_cloud(pcd_path).crop(bounding_box)
pcd = pcd.voxel_down_sample(voxel_size=0.003)  # 0.003 is a good value for downsampling

pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.005, max_nn=30))
pcd.orient_normals_consistent_tangent_plane(50)

radii = [0.003]
mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(pcd, o3d.utility.DoubleVector(radii))

mesh_path = os.path.join(script_path, '..', 'objects', 'pcd_to_mesh', 'mesh_0.obj')
o3d.io.write_triangle_mesh(mesh_path, mesh)
mesh = pv.read(mesh_path)
mesh_path = os.path.join(script_path, '..', 'objects', 'pcd_to_mesh', 'mesh_0.ply')
mesh.save(mesh_path)

mesh_to_fix = _meshfix.PyTMesh()
mesh_to_fix.load_file(mesh_path)
mesh_to_fix.fill_small_boundaries()
repaired_mesh_path = os.path.join(script_path, '..', 'objects', 'pcd_to_mesh', 'mesh_0_repaired.obj')
mesh_to_fix.save_file(repaired_mesh_path)

repaired_mesh_0 = o3d.io.read_triangle_mesh(repaired_mesh_path)
o3d.visualization.draw_geometries([pcd, world_frame, repaired_mesh_0, bounding_box],
                                  width=800, height=800,
                                  mesh_show_back_face=True,
                                  mesh_show_wireframe=True)
