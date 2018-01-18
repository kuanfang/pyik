#!/usr/bin/env python

"""Test the ikpy package.
"""

import time   # NOQA
import logging

import numpy as np   # NOQA

import _init_paths  # NOQA
from pyik import IKSolver


# Create logger.
logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter(
        '%(asctime)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def main():
    IK_URDF = ('data/robot/rethink/sawyer_description/urdf/'
               'sawyer_for_ikpy.urdf')
    NEUTRAL_POSITIONS = [0, -1.18, 0.00, 2.18, 0.00, 0.57, 3.3161, 0]
    ik_solver = IKSolver(IK_URDF)

    target = np.array([
        [1, 0, 0, 0.2],
        [0, 1, 0, -0.5],
        [0, 0, 1, 0.3],
        [0, 0, 0, 1]])
    logger.info('Target Pose: %s' % target)

    logger.info('Running IK with seed: %s...' % NEUTRAL_POSITIONS)
    joint_positions = ik_solver.inverse_kinematics(
            target, initial_positions=NEUTRAL_POSITIONS)
    logger.info('IK results: %s.' % joint_positions)
    result_pose = ik_solver.forward_kinematics(joint_positions)
    logger.info('The end effector pose will be: %s.' % result_pose)

    logger.info('Running IK with seed: %s...' % joint_positions)
    joint_positions = ik_solver.inverse_kinematics(
            target, initial_positions=joint_positions)
    logger.info('IK results: %s.' % joint_positions)
    result_pose = ik_solver.forward_kinematics(joint_positions)
    logger.info('The end effector pose will be: %s.' % result_pose)


if __name__ == '__main__':
    main()
