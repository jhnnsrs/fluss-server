from email.policy import default
import json
from balder.types import BalderMutation
import graphene
from flow import models, types
from lok import bounced
import logging
from flow.inputs import GraphInput, NodeInput, EdgeInput
from graphene.types.generic import GenericScalar
from balder.types.scalars import ImageFile
import namegenerator
import hashlib

logger = logging.getLogger(__name__)


def graph_hash(graph_hash) -> str:
    """MD5 hash of a dictionary."""
    dhash = hashlib.md5()
    # We need to sort arguments so {'a': 1, 'b': 2} is
    # the same as {'b': 2, 'a': 1}
    encoded = json.dumps(graph_hash, sort_keys=True).encode()
    dhash.update(encoded)
    return dhash.hexdigest()


class UpdateDiagram(BalderMutation):
    class Arguments:
        id = graphene.ID(required=True)
        graph = graphene.Argument(GraphInput, required=False)
        brittle = graphene.Boolean(default_value=False)
        screenshot = ImageFile(required=False)

    @bounced(anonymous=False)
    def mutate(root, info, id, graph=None, brittle=False, screenshot=None):

        diagram = models.Diagram.objects.get(id=id)

        flow, cr = models.Flow.objects.get_or_create(
            diagram=diagram,
            hash=graph_hash(graph),
            defaults={"graph": graph, "brittle": brittle},
        )

        flow.brittle = brittle or flow.brittle
        flow.screenshot = screenshot or flow.screenshot
        flow.save()

        return diagram

    class Meta:
        type = types.Diagram
        operation = "updatediagram"


class DrawVanilla(BalderMutation):
    class Arguments:
        name = graphene.String(required=False)
        brittle = graphene.Boolean(default_value=False)

    @bounced(anonymous=False)
    def mutate(
        root,
        info,
        name=None,
        brittle=False,
    ):

        x = name or namegenerator.gen()

        nodes = [
            {
                "id": "1",
                "typename": "ArgNode",
                "instream": [[]],
                "outstream": [[]],
                "constream": [[]],
                "position": {"x": 0, "y": 50},
            },
            {
                "id": "2",
                "typename": "ReturnNode",
                "instream": [[]],
                "outstream": [[]],
                "constream": [[]],
                "position": {"x": 1500, "y": 50},
            },
            {
                "id": "3",
                "typename": "KwargNode",
                "instream": [[]],
                "outstream": [[]],
                "constream": [[]],
                "position": {"x": 750, "y": 100},
            },
        ]

        graph = {
            "nodes": nodes,
            "edges": [],
            "globals": [],
            "args": [],
            "kwargs": [],
            "returns": [],
        }

        diagram = models.Diagram.objects.create(name=x, creator=info.context.user)

        flow = models.Flow.objects.create(
            diagram=diagram,
            graph=graph,
            hash=graph_hash(graph),
            name=name,
            creator=info.context.user,
            brittle=brittle or False,
        )
        return diagram

    class Meta:
        type = types.Diagram
        operation = "drawvanilla"


class DeleteFlowReturn(graphene.ObjectType):
    id = graphene.ID()


class DeleteFlow(BalderMutation):
    class Arguments:
        id = graphene.ID(required=True, description="The Id of the Graph")

    @bounced(anonymous=False)
    def mutate(root, info, id=None):

        graph = models.Flow.objects.get(id=id)
        graph.delete()
        return {"id": id}

    class Meta:
        type = DeleteFlowReturn
