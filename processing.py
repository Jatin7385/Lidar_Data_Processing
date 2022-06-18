import numpy as np
import open3d as o3d

print("Load a ply point cloud, print it, and render it")
pcd = o3d.io.read_point_cloud("./Room_lidar.ply")
print(pcd)
print(np.asarray(pcd.points))
o3d.visualization.draw_geometries([pcd])