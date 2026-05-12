from setuptools import find_packages, setup
import os
from glob import glob

package_name = "agx_arm_graspgen"

setup(
    name=package_name,
    version="0.1.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        (
            "share/ament_index/resource_index/packages",
            ["resource/" + package_name],
        ),
        ("share/" + package_name, ["package.xml"]),
        (
            os.path.join("share", package_name, "config"),
            glob("config/*"),
        ),
        (
            os.path.join("share", package_name, "launch"),
            glob("launch/*"),
        ),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Agilex Robotics",
    maintainer_email="maintainer@agilexrobotics.com",
    description="Grasp candidate generation package for Piper Studio.",
    license="Apache-2.0",
)