# DRAFT reply to Prof. Garret Moddel — for operator review, NOT sent

> This is the load-bearing reply. It must hold the pre-registration line without being
> combative, honor the real materials-sensitivity point, and ask him for specific deposition
> parameters. Sending is the operator's act. Recommend governing the underlying methodology
> decision (the Phase-A/Phase-B split) as a zpe-lab intent + pressure-test before/alongside
> sending, so the public record carries the reasoning.

---

Dear Prof. Moddel,

Thank you — genuinely — for being willing to help. Having the original author engaged is
more than I expected, and I want to use it well.

Your point about materials sensitivity is well taken, and it's exactly the kind of thing I'd
have gotten wrong without hearing it: these are very thin films, the interfaces are delicate,
and a device that isn't fabricated competently tells you nothing. I agree completely that I
have to be able to make *working* devices before any test of the cavity effect means
anything.

Where I want to propose a small but important refinement is on the sequencing. If I develop
the fabrication by iterating until I observe the zero-bias current and *then* register the
replication, I've unfortunately built exactly the study your critics would dismiss —
"they tuned until they saw it, then declared success." That framing would waste the effort,
and it wouldn't move anyone who is currently skeptical. A pre-registered replication that
*confirms* the effect is far stronger evidence for your claim than any amount of
tuned-then-reported data, precisely because it forecloses that objection.

So here's the structure I'd like to use, which I think honors your point without giving up
that strength:

1. **Fabrication development, qualified against your published baseline device characteristics
   — not against the anomalous current.** I iterate the recipe freely until my junctions match
   what you report for ordinary device behavior: the differential-resistance range, the linear
   low-bias I(V), the Fowler-Nordheim barrier heights, and the layer thicknesses (verified by
   ellipsometry/AFM). This is the "develop a working protocol first" step you're describing.

   I want to be precise about one thing rather than overclaim it, because you'd rightly catch
   it otherwise: these qualification criteria are *not* fully independent of the effect's
   expected size. Your Fig. 4(b)/5(b) show the current scaling exponentially with insulator
   thickness, which is the same parameter that sets the junction resistance I'm qualifying on —
   so hitting your resistance band tends to select the thin-barrier, higher-signal end of your
   own curves. I'm not claiming otherwise. What the qualification *does* protect against is the
   specific failure mode of tuning fabrication while watching the anomalous output and adjusting
   toward more of it — because the target values are locked to your published baselines before
   fabrication starts and never moved toward "more signal," and because the test itself is a
   within-device cavity-open vs cavity-closed contrast (retractable mirror, same junction), which
   device selection can't tune. To keep the residual coupling honest rather than hidden, I commit
   the full qualification distribution publicly — every device, pass and fail, with its measured
   resistance and thickness — so anyone (including you) can check whether I'm quietly cherry-picking
   the low-resistance devices.

2. **Only devices with a sealed, pre-cavity qualification record enter the blinded
   cavity-open/closed test** — the pre-registered part, where the analysis is frozen and the
   cavity state is withheld from the analyst until after the per-device statistics are recorded.

The one thing this needs from you to be fair to your work: **the specific deposition
conditions you consider necessary** — rates, pressures, substrate temperatures, timings,
anneal steps, the parameters that matter for the thin barrier and the interfaces. If those
conditions are specifiable, I'll pre-register exactly them and follow them faithfully, so a
null result can't be blamed on my having deviated from your recipe. If the working window
genuinely can't be written down except as "iterate until you see the effect," that's
important for me to understand too, and we should talk about what a fair test looks like in
that case.

On your question about my facilities and experience: I should be straight with you — I'm an
independent researcher, not a thin-film group, and I don't have hands-on deposition
experience. I'm outsourcing fabrication to an established nanofabrication facility (I'm
getting quotes now) precisely to get competent devices, and I'm qualifying every device
against your published baselines before it's tested. My contribution is rigorous, transparent
measurement and an honest, pre-committed analysis — everything is public at
github.com/meanmod3/zpe-lab before any device exists — rather than fabrication expertise I
don't have. I'd rather tell you that plainly than oversell it.

I'd welcome any raw device data you're able to share (I know the published figures are the
only public form) — even the anomalous-offset dataset from the PRR supplement would help me
set my measurement expectations honestly.

Thank you again for engaging. I'll take a "this design still won't work" as valuable input if
that's your read.

Best wishes,
Ben Davis
Independent researcher
interplore.media@gmail.com
github.com/meanmod3/zpe-lab
