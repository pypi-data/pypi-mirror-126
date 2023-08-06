# ------------------------- Imports ------------------------ #


import click

from mltrace import (
    set_address,
    get_recent_run_ids,
    get_component_run_information,
    get_component_information,
    get_history,
    web_trace,
    flag_output_id,
    unflag_output_id,
    review_flagged_outputs,
    get_all_tags,
    get_components,
    unflag_all,
    clean_db,
)
import textwrap


# ------------------------- Utilities ------------------------ #


def show_info_card(run_id: int, count: int = None, num_outputs: int = None):
    """
    Prints the info cards corresponding to run ids.

    Args:
        run_id: The component run id.
        count: A number to display next to the title (used for review.)
        num_outputs: The total number of outputs flagged (used for review.)
    """
    cr_info = get_component_run_information(run_id)
    c_info = get_component_information(cr_info.component_name)

    click.echo(f"Name: {c_info.name}")
    if count:
        time_or_times = "time" if count == 1 else "times"
        coverage = str(round(float(count / num_outputs) * 100, 2))
        click.echo(
            click.style(
                f"├─This component has {coverage}% coverage: it was used "
                + f"{count} {time_or_times} in producing the flagged outputs.",
                fg="cyan",
                bg="black",
            )
        )
    if cr_info.stale and len(cr_info.stale) > 0:
        click.echo(
            click.style(
                f"├─Some dependencies may be stale:", fg="yellow", bg="black"
            )
        )
        for idx, warning in enumerate(cr_info.stale):
            if idx == len(cr_info.stale) - 1:
                click.echo(
                    click.style(f"│  └─{warning}", fg="yellow", bg="black")
                )
            else:
                click.echo(
                    click.style(f"│  ├─{warning}", fg="yellow", bg="black")
                )
    click.echo(f"├─Owner: {c_info.owner}")
    click.echo(f"├─Desc: {c_info.description}")
    click.echo(f"├─Run ID: {run_id}")
    click.echo(f"├─Tags: {' '.join(c_info.tags)}")
    click.echo(f"├─Started: {cr_info.start_timestamp}")
    click.echo(f"├─Git commit: {cr_info.git_hash}")
    if cr_info.git_tags is not None:
        click.echo(f"|-Git Tags: {cr_info.git_tags.split(',')}")
    elapsed_time = cr_info.end_timestamp - cr_info.start_timestamp
    min, sec = divmod(elapsed_time.total_seconds(), 60)
    min = min + 1e-1 * sec
    click.echo(f"├─Duration: {min:0.3f} mins")
    click.echo("├─Inputs:")
    inputs = cr_info.inputs
    for idx, inp in enumerate(inputs):
        if idx == len(inputs) - 1:
            click.echo(f"│  └─{inp['name']}")
        else:
            click.echo(f"│  ├─{inp['name']}")
    click.echo("├─Outputs:")
    outputs = cr_info.outputs
    for idx, out in enumerate(outputs):
        if idx == len(outputs) - 1:
            click.echo(f"│  └─{out['name']}")
        else:
            click.echo(f"│  ├─{out['name']}")
    code = textwrap.indent(cr_info.code_snapshot, "│  ")
    click.echo(f"├─Code Snapshot:\n{code.rstrip()}")
    dependencies = (
        " ".join(cr_info.dependencies) if cr_info.dependencies else "None"
    )
    click.echo(f"└─Dependencies: {dependencies}")
    click.echo()


def show_history(history):
    """
    Prints the history as a info card.

    Args:
        history: History object.
    """
    for hist in history:
        click.echo(f"{hist.component_name}--{hist.id}")
        if hist.stale and len(hist.stale) > 0:
            click.echo(
                click.style(
                    f"├─Some dependencies may be stale:",
                    fg="yellow",
                    bg="black",
                )
            )
            for idx, warning in enumerate(hist.stale):
                if idx == len(hist.stale) - 1:
                    click.echo(
                        click.style(f"│  └─{warning}", fg="yellow", bg="black")
                    )
                else:
                    click.echo(
                        click.style(f"│  ├─{warning}", fg="yellow", bg="black")
                    )
        click.echo(f"├─Started: {hist.start_timestamp}")
        click.echo(f"├─Git commit: {hist.git_hash}")
        elapsed_time = hist.end_timestamp - hist.start_timestamp
        min, sec = divmod(elapsed_time.total_seconds(), 60)
        min = min + 1e-1 * sec
        click.echo(f"├─Duration: {min:0.3f} mins")
        click.echo("├─Inputs:")
        inputs = hist.inputs
        for idx, inp in enumerate(inputs):
            if idx == len(inputs) - 1:
                click.echo(f"│  └─{inp['name']}")
            else:
                click.echo(f"│  ├─{inp['name']}")
        click.echo("├─Outputs:")
        outputs = hist.outputs
        for idx, out in enumerate(outputs):
            if idx == len(outputs) - 1:
                click.echo(f"│  └─{out['name']}")
            else:
                click.echo(f"│  ├─{out['name']}")
        code = textwrap.indent(hist.code_snapshot, "│  ")
        click.echo(f"├─Code Snapshot:\n{code.rstrip()}")
        dependencies = (
            " ".join(hist.dependencies) if hist.dependencies else "None"
        )
        click.echo(f"└─Dependencies: {dependencies}")
        click.echo()


def show_res(res, indent, count, pos, need_stick):
    """
    A recursive method that prints the trace of an output id.

    The response of `web_trace` is a list of nodes. The nodes
    can either be a list of children nodes or a dictionary.

    We will recursively iterate the res, and print the `label`
    field of each node.

    Args:
        res: the node, can either be a list or dict.
        indent: required indentation. (Used for prinitng)
        count: how many children. (Used for prinitng)
        pos: which child. (Used for prinitng)
        need_stick: how many "|" are needed. (Used for prinitng)
    """
    if isinstance(res, dict):
        # dictionary is a node
        # BUILD THE TREE STRUCTURE
        label = f"└─{res['label']}" if count == pos else f"├─{res['label']}"
        pre = "  " if indent > 0 else ""
        sticks = "│ " * (need_stick)
        temp_indent = (indent - 1) - (need_stick)
        post = "  " * (temp_indent)
        label = pre + sticks + post + label
        click.echo(label)
        # NEED STICK LOGIC
        need_stick = need_stick if count == pos else need_stick + 1
        # CALL METHOD RECURSIVELY
        if "childNodes" in res.keys():
            show_res(
                res=res["childNodes"],
                indent=indent + 1,
                count=count,
                pos=pos,
                need_stick=need_stick,
            )

    if isinstance(res, list):
        # list of children
        for index, component in enumerate(res):
            show_res(
                res=component,
                indent=indent,
                count=len(res) - 1,
                pos=index,
                need_stick=need_stick,
            )


# ------------------------- CLI ------------------------ #


@click.group()
def mltrace():
    # Pass
    pass


@mltrace.command("recent")
@click.option("--limit", default=5, help="Limit of recent objects.")
@click.option("--address", help="Database server address")
def recent(limit: int, address: str = ""):
    """
    CLI for recent objects.
    """
    # Set address
    if address and len(address) > 0:
        set_address(address)
    # Get the recent ids
    component_run_ids = get_recent_run_ids()
    for id in component_run_ids[:limit]:
        show_info_card(id)


@mltrace.command("inspect")
@click.option("--address", help="Database server address")
@click.argument("component_run_id")
def inspect(component_run_id, address: str = ""):
    """
    CLI to inspect a specific component run id.
    """
    # Set address
    if address and len(address) > 0:
        set_address(address)

    show_info_card(component_run_id)


@mltrace.command("history")
@click.argument("component_name")
@click.option("--limit", default=5, help="Limit of recent objects.")
@click.option("--address", help="Database server address")
def history(component_name: str, limit: int, address: str = ""):
    """
    CLI for history of ComponentName.
    """
    # Set address
    if address and len(address) > 0:
        set_address(address)
    history = (
        get_history(component_name, limit)
        if limit
        else get_history(component_name)
    )
    show_history(history)


@mltrace.command("trace")
@click.argument("output_id")
@click.option("--address", help="Database server address")
def trace(output_id: str, address: str = ""):
    """
    CLI for trace.
    """
    # Set address
    if address and len(address) > 0:
        set_address(address)
    res = web_trace(output_id)
    click.echo(res[0]["label"])
    if "childNodes" in res[0].keys():
        show_res(
            res=res[0]["childNodes"], indent=1, count=0, pos=0, need_stick=0
        )


@mltrace.command("flag")
@click.argument("output_id")
@click.option("--address", help="Database server address")
def flag(output_id: str, address: str = ""):
    """
    Command to set the flag property of an output_id to true.
    """
    # Set address
    if address and len(address) > 0:
        set_address(address)
    flag_output_id(output_id)


@mltrace.command("unflag")
@click.option("--output_id", help="Output ID to unflag")
@click.option("--all", is_flag=True, help="Add flag to unflag all")
@click.option("--address", help="Database server address")
def unflag(output_id: str = "", all: bool = False, address: str = ""):
    """
    Command to set flag property of an output_id or all output_ids to false.
    """
    # Check if set --all and --output_id
    if all and output_id:
        raise click.ClickException(
            "Can set either --all=True or specify an "
            "--output_id. Cannot set both."
        )

    if not all and not output_id:
        raise click.ClickException(
            "Need to either set --all=True or specify "
            "an --output_id to unflag."
        )

    # Set address
    if address and len(address) > 0:
        set_address(address)

    if all:
        unflag_all()

    elif not all and output_id:
        unflag_output_id(output_id)


@mltrace.command("review")
@click.option("--limit", default=5, help="Limit of recent objects.")
@click.option("--address", help="Database server address")
def review(limit: int = 5, address: str = ""):
    """Command to find common component runs in a set of flagged outputs."""
    if address and len(address) > 0:
        set_address(address)
    outputs, component_counts = review_flagged_outputs()

    # Print output ids
    click.echo("Flagged outputs:")
    for idx, out in enumerate(outputs):
        if idx == len(outputs) - 1:
            click.echo(f"└─{out}")
        else:
            click.echo(f"├─{out}")
    click.echo()

    # Print component runs
    for component, count in component_counts[:limit]:
        show_info_card(component.id, count, len(outputs))


@mltrace.command("components")
@click.option("--owner", help="Owner of components")
@click.option("--tag", help="Tag of components")
@click.option("--address", help="Database server address")
def components(owner: str = "", tag: str = "", address: str = ""):
    """
    Command to list the components with options to filter by tag or owner.
    """
    if address and len(address) > 0:
        set_address(address)

    # Make return result
    try:
        result = get_components(tag, owner)
    except RuntimeError:
        raise click.ClickException(
            "No components could be found with the " "flags passed."
        )

    # Display components, one per line
    for comp in result:
        click.echo(f"Name: {comp.name}")
        click.echo()


@mltrace.command("tags")
@click.option("--address", help="Database server address")
def tags(address: str = ""):
    """
    Command to list all the tags currently used.
    """
    # Set address
    if address and len(address) > 0:
        set_address(address)

    # Get all tags, automatically unique
    all_tags = get_all_tags()

    click.echo(all_tags)
    click.echo()


@mltrace.command("clear")
@click.option("--address", help="Database server address")
def clear(address: str = ""):
    """
    Command to delete all elements in the db.
    """
    # Set address
    if address and len(address) > 0:
        set_address(address)

    clean_db()
