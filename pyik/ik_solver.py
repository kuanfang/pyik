"""Inverse kinematics (IK) solvers.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from pyik.chain import Chain


class IKSolver(object):
    """IK solver implemented with scipy.
    """

    def __init__(self, urdf_path, active_links=None):
        """Initialize.

        Args:
            urdf_path: Path to the URDF file.
            active_links: Mask of active links as a list.
        """
        self._chain = Chain.from_urdf_file(urdf_path, active_links=active_links)

    def inverse_kinematics(self, target, ee_link=-1, initial_positions=None):
        """Compute the IK results.

        Args:
            target: The target pose as a matrix of shape [4, 4].

        Returns:
            positions: The IK results as a list of joint positions.
        """
        assert ee_link == -1 or ee_link == len(self._chain.links) - 1, (
                'Arbitrary links as the end effector is not supported yet.')

        ik_result = self._chain.inverse_kinematics(
                target=target, initial_positions=initial_positions)
        positions = ik_result.tolist()

        return positions

    def forward_kinematics(self, positions, ee_link=-1):
        """Compute the forward kinematics.

        Args:
            position: The specified joint positions. 

        Returns:
            The pose of the end effector as a matrix of shape [4, 4].
        """
        assert ee_link == -1 or ee_link == len(self._chain.links) - 1, (
                'Arbitrary links as the end effector is not supported yet.')

        matrix4 = self._chain.forward_kinematics(positions)
        return matrix4
