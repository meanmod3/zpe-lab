"""Benchmark tests (intent 520 metrics #1-#3): schema, anchors, cross-figure
consistency, and consistency with the frozen pipeline's sourced constants."""

import os
import sys

import pytest

from loader import load, validate, dataset, interp, isc_at_zero_bias_nA, g_at_cavity_S

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sim"))
import config as cfg  # noqa: E402


@pytest.fixture(scope="module")
def data():
    return load()


def test_schema_validates(data):
    assert validate(data)
    assert len(data["datasets"]) >= 8
    assert "NOT independent" in data["provenance_note"]

def test_every_dataset_carries_uncertainty_and_provenance(data):
    for ds in data["datasets"]:
        assert ds["read_uncertainty"].strip()
        assert ds["paper"] in ("SYM", "PRR") and ds["figure"]
        assert ds["x_unit"] and ds["y_unit"]

def test_anchor_prr_caption_values(data):
    """Metric #2: digitized PRR Fig 3(b) curve must be consistent with the
    caption-exact anchors (1 mS at 33 nm, 20 uS at 1100 nm) within the stated
    ~25% read uncertainty."""
    a = data["anchors_verified"]
    assert g_at_cavity_S(data, 33) == pytest.approx(a["prr_fig3a_G_33nm_S"], rel=0.25)
    assert g_at_cavity_S(data, 1100) == pytest.approx(a["prr_fig3a_G_1100nm_S"], rel=0.25)

def test_anchor_sym_max_power(data):
    """Isc*|Voc|/4 from the digitized 33 nm I-V must bracket the paper's stated
    1.4 pW within read uncertainty (figure-read gives ~1.76 pW, a 26% gap; rel=0.5 discriminates while allowing the read error — tightened per PT-520 #7)."""
    ds = dataset(data, "sym-fig4a-Iv-33nm")
    isc_nA = interp(ds, 0.0)                     # I at V=0
    voc_mV = 0.088                               # from dataset notes (read: ~-0.088 mV)
    p_W = abs(isc_nA * 1e-9 * voc_mV * 1e-3) / 4
    assert p_W == pytest.approx(data["anchors_verified"]["sym_max_power_W"], rel=0.5)
    assert p_W > 0

def test_cross_figure_consistency_fig4a_vs_4b(data):
    """The 33 nm Isc read from the I-V panel must match the same device's point
    on the thickness-scaling panel."""
    from_iv = interp(dataset(data, "sym-fig4a-Iv-33nm"), 0.0)
    from_scaling = isc_at_zero_bias_nA(data, 33)
    assert from_iv == pytest.approx(from_scaling, rel=0.15)

def test_area_scaling_consistency(data):
    """SYM Fig 6(b) linear-scaling slope vs PRR Fig 4(c): both must show
    signal increasing with area (order/trend benchmark)."""
    sym = sorted(dataset(data, "sym-fig6b-area")["points"])
    prr = sorted(dataset(data, "prr-fig4c-area")["points"])
    assert sym[-1][1] > sym[0][1] and prr[-1][1] > prr[0][1]
    # SYM slope ~5.3 pA/um^2 per the dataset notes
    slope = (sym[-1][1] - sym[0][1]) / (sym[-1][0] - sym[0][0])  # nA per um^2
    assert slope * 1e3 == pytest.approx(5.3, rel=0.3)            # pA/um^2

def test_frozen_config_claims_sit_inside_benchmark_range(data):
    """The frozen sim config's figure-read claimed signals must lie within the
    digitized ranges they were sourced from (config vs benchmark coherence)."""
    pmma = dataset(data, "sym-fig4b-pmma")["points"]
    ys = [p[1] for p in pmma]
    assert min(ys) * 1e-9 <= cfg.I_CLAIMED_GSM_A <= max(ys) * 1e-9
    assert min(ys) * 1e-9 <= cfg.I_CLAIMED_PHOTOLITHO_A <= max(ys) * 1e-9

def test_temperature_flatness_benchmark(data):
    """SYM Fig 11: Isc variation across the 3.2 degC stage sweep must be small
    (<10% of mean) — the pre-registered expectation for our own row-1 tests."""
    pts = dataset(data, "sym-fig11-isc-temp")["points"]
    ys = [p[1] for p in pts]
    mean = sum(ys) / len(ys)
    assert (max(ys) - min(ys)) / mean < 0.10

def test_em_environment_separation_recorded(data):
    """SYM Fig 10 finding: the three shielding environments are NOT within a
    line width (max separation ~30 nA) — recorded, benchmark-relevant to our
    EMI row. The dataset must carry that quantification in its notes."""
    ds = dataset(data, "sym-fig10-em-environments")
    assert "30 nA" in ds["notes"] and "NOT within" in ds["notes"]
