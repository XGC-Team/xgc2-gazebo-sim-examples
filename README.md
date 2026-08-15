# gazebo_sim_examples

Launch-only Gazebo Classic example bringup for XGC2.

This repository is not a product. It is not in CI, not in the Gazebo
release set, and not published to APT. It only composes already-released
robot, controller, estimator, and simulator packages so a developer can
start a known demo from one `roslaunch`.

ROS package name: `gazebo_sim_examples`  
Catalog checkout: `xgc2-gazebo-sim/examples`

## Examples

Single Scout Mini, unicycle NMPC, circle of radius 3 m:

```bash
roslaunch gazebo_sim_examples scout_ugv1_nmpc_tracking.launch
```

Gazebo GUI and RViz start by default. RViz uses `RobotModel` plus the TF
tree (`odom` → `base_link` → wheel links). It does not hard-draw wheels.

Single FS150, PX4 SITL, multirotor NMPC torus-knot tracking:

```bash
roslaunch gazebo_sim_examples fs150_uav1_nmpc_tracking.launch
```

## Notes

- Do not add `.github/workflows`, `.xgc2/product.yml`, or an APT payload.
- Visualization is TF + URDF. Do not re-enable the Gazebo marker overlay
  as the robot model.
