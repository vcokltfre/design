from json import loads, dumps
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import TypedDict


    class Design(TypedDict):
        name: str
        description: str
        url: str
else:
    Design = dict


def generate() -> None:
    designs_dir = Path("./designs")

    designs: list[Design] = []

    for design in designs_dir.iterdir():
        if not design.is_dir():
            continue

        manifest_file = design / "design.json"
        if not manifest_file.exists():
            continue

        data = loads(manifest_file.read_text())

        designs.append(Design(**data, url=f"/designs/{design.name}"))

    designs.sort(key=lambda design: design["name"])

    Path("./static/meta/design-manifest.json").write_text(dumps(designs))


if __name__ == "__main__":
    generate()
