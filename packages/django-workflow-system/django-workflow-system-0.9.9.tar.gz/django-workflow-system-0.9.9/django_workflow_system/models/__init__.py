"""Convenience imports."""

###########
# GENERAL #
###########
from django_workflow_system.models.author import WorkflowAuthor
from django_workflow_system.models.json_schema import JSONSchema

###############
# COLLECTIONS #
###############
from .collections import (
    WorkflowCollectionAssignment,
    WorkflowCollection,
    WorkflowCollectionDependency,
    WorkflowCollectionEngagement,
    WorkflowCollectionEngagementDetail,
    WorkflowCollectionImage,
    WorkflowCollectionImageType,
    WorkflowCollectionMember,
    WorkflowCollectionRecommendation,
)

#############
# WORKFLOWS #
#############
from django_workflow_system.models.step import WorkflowStep
from django_workflow_system.models.step_audio import WorkflowStepAudio
from django_workflow_system.models.step_dependency_detail import (
    WorkflowStepDependencyDetail,
)
from django_workflow_system.models.step_dependency_group import (
    WorkflowStepDependencyGroup,
)
from django_workflow_system.models.step_external_link import WorkflowStepExternalLink
from django_workflow_system.models.step_image import WorkflowStepImage
from django_workflow_system.models.step_user_input import WorkflowStepUserInput
from django_workflow_system.models.step_user_input_type import WorkflowStepUserInputType
from django_workflow_system.models.step_text import WorkflowStepText
from django_workflow_system.models.step_ui_template import WorkflowStepUITemplate
from django_workflow_system.models.step_video import WorkflowStepVideo
from django_workflow_system.models.subscription import WorkflowCollectionSubscription
from django_workflow_system.models.subscription_schedule import (
    WorkflowCollectionSubscriptionSchedule,
)
from django_workflow_system.models.workflow import Workflow
from django_workflow_system.models.metadata import WorkflowMetadata
from django_workflow_system.models.abstract_models import CreatedModifiedAbstractModel
from django_workflow_system.models.workflow_image import WorkflowImage
from django_workflow_system.models.workflow_image_type import WorkflowImageType

__all__ = [
    "WorkflowAuthor",
    "WorkflowCollectionAssignment",
    "WorkflowCollectionDependency",
    "WorkflowCollectionEngagement",
    "WorkflowCollectionEngagementDetail",
    "WorkflowCollection",
    "WorkflowCollectionMember",
    "WorkflowCollectionImageType",
    "WorkflowCollectionImage",
    "WorkflowCollectionRecommendation",
    "JSONSchema",
    "WorkflowStep",
    "WorkflowStepAudio",
    "WorkflowStepExternalLink",
    "WorkflowStepImage",
    "WorkflowStepText",
    "WorkflowStepUserInput",
    "WorkflowStepUserInputType",
    "WorkflowStepUITemplate",
    "WorkflowStepVideo",
    "WorkflowStepDependencyDetail",
    "WorkflowStepDependencyGroup",
    "WorkflowCollectionSubscription",
    "WorkflowCollectionSubscriptionSchedule",
    "Workflow",
    "WorkflowImage",
    "WorkflowImageType",
    "WorkflowMetadata",
    "CreatedModifiedAbstractModel",
]
