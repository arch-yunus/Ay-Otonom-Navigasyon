from setuptools import setup
import os
from glob import glob

package_name = 'ay_otonom_navigasyon'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='arch-yunus',
    maintainer_email='yunus@example.com',
    description='Professional Lunar Autonomous Navigation Stack',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'perception_node = ay_otonom_navigasyon.perception_node:main',
            'navigation_node = ay_otonom_navigasyon.navigation_node:main',
            'estimation_node = ay_otonom_navigasyon.estimation_node:main',
            'mission_manager = ay_otonom_navigasyon.mission_manager:main',
            'teleop_node = ay_otonom_navigasyon.teleop_node:main',
            'fdir_node = ay_otonom_navigasyon.fdir_node:main',
            'swarm_node = ay_otonom_navigasyon.swarm_logic:main',
            'recovery_node = ay_otonom_navigasyon.recovery:main',
        ],
    },
)
