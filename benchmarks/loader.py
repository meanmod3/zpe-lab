"""Benchmark loader + comparison utilities (intent 520).

Figure-read benchmarks from the two Moddel papers — a COMPARISON layer for the
frozen analysis pipeline (bd81f70), which this module never modifies. Every
dataset is same-group / non-independent and approximate by construction; the
file-level provenance note governs interpretation.
"""

import json
import math
import os

BENCH_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "benchmarks.json")

REQUIRED_DATASET_FIELDS = ("id", "paper", "figure", "x_label", "x_unit",
                           "y_label", "y_unit", "x_scale", "y_scale",
                           "read_uncertainty", "points", "notes")


def load():
    with open(BENCH_PATH, encoding="utf-8") as f:
        data = json.load(f)
    validate(data)
    return data


def validate(data):
    assert data["schema_version"] == 1
    assert "NOT independent" in data["provenance_note"], \
        "file-level non-independence label is mandatory"
    ids = set()
    for ds in data["datasets"]:
        for field in REQUIRED_DATASET_FIELDS:
            assert field in ds and ds[field] != "", (ds.get("id"), field)
        assert ds["id"] not in ids, f"duplicate dataset id {ds['id']}"
        ids.add(ds["id"])
        assert ds["x_scale"] in ("log", "linear") and ds["y_scale"] in ("log", "linear")
        for p in ds["points"]:
            assert len(p) == 2 and all(isinstance(v, (int, float)) for v in p), (ds["id"], p)
    assert len(data["datasets"]) >= 8
    return True


def dataset(data, ds_id):
    for ds in data["datasets"]:
        if ds["id"] == ds_id:
            return ds
    raise KeyError(ds_id)


def interp(ds, x):
    """Piecewise interpolation honoring the dataset's axis scales."""
    pts = sorted(ds["points"])
    if not (pts[0][0] <= x <= pts[-1][0]):
        raise ValueError(f"{x} outside {ds['id']} range [{pts[0][0]}, {pts[-1][0]}]")
    fx = math.log10 if ds["x_scale"] == "log" else (lambda v: v)
    fy = math.log10 if ds["y_scale"] == "log" else (lambda v: v)
    gy = (lambda v: 10 ** v) if ds["y_scale"] == "log" else (lambda v: v)
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if x0 <= x <= x1:
            t = 0.0 if x1 == x0 else (fx(x) - fx(x0)) / (fx(x1) - fx(x0))
            return gy(fy(y0) + t * (fy(y1) - fy(y0)))
    raise AssertionError("unreachable")


def isc_at_zero_bias_nA(data, cavity_nm):
    """Expected short-circuit current (nA) at a PMMA cavity thickness, from the
    SYM Fig 4(b) trend — the primary claimed-signal benchmark."""
    return interp(dataset(data, "sym-fig4b-pmma"), cavity_nm)


def g_at_cavity_S(data, cavity_nm):
    """Expected differential conductance (S) vs PMMA cavity thickness (PRR 3b)."""
    return interp(dataset(data, "prr-fig3b-pmma"), cavity_nm) * 1e-3  # mS -> S
