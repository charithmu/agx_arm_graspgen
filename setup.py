from setuptools import find_packages, setup
import os
from glob import glob
from pathlib import Path

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
            glob("config/*.yaml"),
        ),
        (
            os.path.join("share", package_name, "launch"),
            [f for f in glob("launch/*") if Path(f).is_file()],
        ),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Charith Munasinghe",
    maintainer_email="mung@zhaw.ch",
    description="Grasp candidate generation package for Piper Studio.",
    license="Apache-2.0",
)