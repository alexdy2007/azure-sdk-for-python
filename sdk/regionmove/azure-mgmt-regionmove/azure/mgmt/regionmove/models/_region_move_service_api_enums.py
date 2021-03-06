# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class DependencyType(str, Enum):
    """Defines the dependency type.
    """

    required_for_prepare = "RequiredForPrepare"
    required_for_move = "RequiredForMove"

class MoveResourceInputType(str, Enum):
    """Defines the move resource input type.
    """

    move_resource_id = "MoveResourceId"
    move_resource_source_id = "MoveResourceSourceId"

class MoveState(str, Enum):
    """Defines the MoveResource states.
    """

    assignment_pending = "AssignmentPending"
    prepare_pending = "PreparePending"
    prepare_in_progress = "PrepareInProgress"
    prepare_failed = "PrepareFailed"
    move_pending = "MovePending"
    move_in_progress = "MoveInProgress"
    move_failed = "MoveFailed"
    discard_in_progress = "DiscardInProgress"
    discard_failed = "DiscardFailed"
    commit_pending = "CommitPending"
    commit_in_progress = "CommitInProgress"
    commit_failed = "CommitFailed"
    committed = "Committed"

class ProvisioningState(str, Enum):
    """Defines the provisioning states.
    """

    succeeded = "Succeeded"
    updating = "Updating"
    creating = "Creating"
    failed = "Failed"

class ResolutionType(str, Enum):
    """Defines the resolution type.
    """

    manual = "Manual"
    automatic = "Automatic"

class ResourceIdentityType(str, Enum):
    """The type of identity used for the region move service.
    """

    none = "None"
    system_assigned = "SystemAssigned"
    user_assigned = "UserAssigned"

class TargetAvailabilityZone(str, Enum):
    """Gets or sets the target availability zone.
    """

    one = "1"
    two = "2"
    three = "3"
    na = "NA"

class ZoneRedundant(str, Enum):
    """Defines the zone redundant resource setting.
    """

    enable = "Enable"
    disable = "Disable"
