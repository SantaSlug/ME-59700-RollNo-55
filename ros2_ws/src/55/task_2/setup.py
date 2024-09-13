from setuptools import find_packages, setup

package_name = 'task_2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Soham Rawal',
    maintainer_email='rawal2@purdue.edu',
    description='Publisher and subscriber and service and client nodes using custom message JointData',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher_node = task_2.publisher_node:main',
            'subscriber_node = task_2.subscriber_node:main',
            'service_server_node = task_2.service_server_node:main',
            'service_client_node = task_2.service_client_node:main',
        ],
    },
    package_data={
        '': ['*.srv', '*.msg', 'launch/*.py'],
    },
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/service_launch.py']), 
    ],
)

