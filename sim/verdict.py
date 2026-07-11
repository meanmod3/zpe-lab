"""GO/NO-GO detectability verdict logic for the C1 rig.

The pre-registered criterion (promoted 511 dossier): a claimed signal is
detectable-and-attributable only if it exceeds 3x the RSS artifact floor.
Phase 1 asks the PROSPECTIVE version: given predicted artifact magnitudes
and the published claimed-signal scale, does the rig have >= 3x margin?
NO-GO is a valid outcome and must be reported as plainly as GO.
"""

from dataclasses import dataclass

@dataclass
class VerdictInput:
    label: str
    i_claimed_A: float          # claimed cavity-correlated signal, current-equivalent
    i_artifact_rss_A: float     # RSS of artifact rows (current-equivalent, post-mitigation)
    i_johnson_1Hz_A: float      # junction Johnson noise density (A/rtHz)
    integration_time_s: float   # lock-in time for white noise alone to reach 3 sigma

@dataclass
class Verdict:
    label: str
    margin: float               # i_claimed / (3 * i_artifact_rss)
    go: bool
    limiting_factor: str
    integration_time_s: float

MAX_PRACTICAL_INTEGRATION_S = 24 * 3600.0  # one day per blinded run segment

def decide(v: VerdictInput) -> Verdict:
    floor = 3.0 * v.i_artifact_rss_A
    margin = v.i_claimed_A / floor if floor > 0 else float("inf")
    time_ok = v.integration_time_s <= MAX_PRACTICAL_INTEGRATION_S
    go = margin >= 1.0 and time_ok
    if not time_ok:
        limiting = "white-noise integration time exceeds 24 h/run"
    elif margin < 1.0:
        limiting = "artifact RSS floor exceeds claimed signal / 3"
    else:
        limiting = "none — margin %.1fx" % margin
    return Verdict(v.label, margin, go, limiting, v.integration_time_s)
