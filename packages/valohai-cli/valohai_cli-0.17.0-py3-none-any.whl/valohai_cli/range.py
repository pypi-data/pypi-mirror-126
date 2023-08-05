from typing import Iterable, Set, Union


class IntegerRange:
    def __init__(self, includes: Set[Iterable[int]], excludes: Set[Iterable[int]]):
        self.includes = set(includes)
        self.excludes = set(excludes)

    @classmethod
    def parse(cls, atoms: Iterable[Union[str, int]]) -> 'IntegerRange':
        includes: Set[Iterable[int]] = set()
        excludes: Set[Iterable[int]] = set()
        for atom in atoms:
            if isinstance(atom, int):
                includes.add((atom,))
                continue
            if isinstance(atom, str):
                if atom[0] == '!':
                    negate = True
                    atom = atom[1:]
                else:
                    negate = False
                target = (excludes if negate else includes)
                atom = atom.lstrip('#')
                if atom.isdigit():
                    target.add((int(atom),))
                    continue
                elif '-' in atom:
                    start, end = map(int, atom.split('-', 1))
                    target.add(range(start, end + 1))
                    continue
            raise ValueError(f'Not a valid range atom: {atom}')  # pragma: no cover
        return cls(includes=includes, excludes=excludes)

    def as_set(self) -> Set[int]:
        values = set()
        for inc in self.includes:
            values |= set(inc)
        for exc in self.excludes:
            values -= set(exc)
        return values
