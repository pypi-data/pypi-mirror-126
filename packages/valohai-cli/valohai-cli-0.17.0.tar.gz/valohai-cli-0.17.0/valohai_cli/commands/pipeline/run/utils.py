from typing import List

import click
from valohai_yaml.objs import Config, ExecutionNode, Pipeline, Step

from valohai_cli.utils import match_prefix


def build_nodes(commit: str, config: Config, pipeline: Pipeline) -> List[dict]:
    nodes = []
    for node in pipeline.nodes:
        if isinstance(node, ExecutionNode):
            step = config.steps[node.step]
            template = build_node_template(commit, step)
            nodes.append({
                "name": node.name,
                "type": node.type,
                "template": template,
            })
            continue
        raise NotImplementedError(f"{node.type} nodes are not supported by the CLI at present")
    return nodes


def build_node_template(commit: str, step: Step) -> dict:
    template = {
        "commit": commit,
        "step": step.name,
        "image": step.image,
        "command": step.command,
        "inputs": {
            name: (input.default or []) for (name, input) in step.inputs.items()
        },
        "parameters": {
            key: step.parameters[key].default for key in
            list(step.parameters)
        },
        "inherit_environment_variables": True,
        "environment_variables": dict(step.environment_variables),
    }
    if step.environment:
        template["environment"] = step.environment
    return template


def build_edges(pipeline: Pipeline) -> List[dict]:
    return [
        {
            "source_node": edge.source_node,
            "source_key": edge.source_key,
            "source_type": edge.source_type,
            "target_node": edge.target_node,
            "target_type": edge.target_type,
            "target_key": edge.target_key,
        }
        for edge in pipeline.edges
    ]


def match_pipeline(config: Config, pipeline_name: str) -> str:
    """
    Take a pipeline name and try and match it to the configs pipelines.
    Returns the match if there is only one option.
    """
    if pipeline_name in config.pipelines:
        return pipeline_name
    matching_pipelines = match_prefix(config.pipelines, pipeline_name, return_unique=False)
    if not matching_pipelines:
        raise click.BadParameter(
            '"{pipeline}" is not a known pipeline (try one of {pipelines})'.format(
                pipeline=pipeline_name,
                pipelines=', '.join(click.style(t, bold=True) for t in sorted(config.pipelines))
            ), param_hint='pipeline')
    if len(matching_pipelines) > 1:
        raise click.BadParameter(
            '"{pipeline}" is ambiguous.\nIt matches {matches}.\nKnown pipelines are {pipelines}.'.format(
                pipeline=pipeline_name,
                matches=', '.join(click.style(t, bold=True) for t in sorted(matching_pipelines)),
                pipelines=', '.join(click.style(t, bold=True) for t in sorted(config.pipelines)),
            ), param_hint='pipeline')
    return str(matching_pipelines[0])
