"""Draw the README figures of debruijn-newman-degree-two from the data the repository ships.

Usage:  python figures/make_figures.py <repo root>
Needs Python 3.11 and matplotlib 3.11 (standard library otherwise). Writes figures/*.svg next to this script.

Every plotted number is read from shipped files (paths relative to the repository root):
  bundle/AB/leadA/cert/g45_b*.json, g45_t*.json, g45_q*.json, pieces45.txt
        the 87 certified walks of Theorem 1(a): heat setting t, and the corner points of every walk
  bundle/AB/leadA/cert/g45b_combine.json   combined result: winding number, walks, evaluations, holds
  bundle/AB/leadA/cert/BAR-A14.md          the classical start Delta = 1 and the stated bound 0.449938
  bundle/AB/leadA/p11/fin_b1.json, fin_combine.log   Theorem 1(b): heat setting t = 21/50, inner edge 374/1000
  bundle/AB/leadA/tail/tail_run045b_out.json, tail_run045_out.json   tail boxes: y range, start x, box counts
The curves are de Bruijn's rule (README "A worked example"): if every zero lies within Delta of the line, then after
turning the dial by s every zero lies within sqrt(Delta^2 - 2 s).
"""
import json
import os
import re
import sys
from fractions import Fraction as Fr
from math import sqrt

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
from matplotlib.lines import Line2D

# ---------------------------------------------------------------- brand style (figures/STYLE.md)
BG, BORDER, GRID, AXC, TXT, ACC = "#1c2026", "#2f353d", "#22272e", "#9aa4ae", "#e8edf2", "#39ff14"
CAT = ["#3987e5", "#d95926", "#199e70", "#c98500", "#d55181", "#0ca30c", "#9085e9", "#e66767"]
W_IN = 12.5  # 900 pt viewBox width

plt.rcParams.update({
    "svg.fonttype": "none", "svg.hashsalt": "moki-julio",
    "font.family": "sans-serif", "font.sans-serif": ["Segoe UI", "Helvetica", "Arial", "DejaVu Sans"],
    "font.size": 16, "axes.labelsize": 17, "xtick.labelsize": 15, "ytick.labelsize": 15,
    "axes.facecolor": BG, "figure.facecolor": "none", "savefig.facecolor": "none",
    "axes.edgecolor": AXC, "axes.labelcolor": TXT, "xtick.color": AXC, "ytick.color": AXC,
    "text.color": TXT, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 1.0,
    "axes.spines.top": False, "axes.spines.right": False, "legend.frameon": False,
    "legend.fontsize": 14, "lines.linewidth": 2.0, "axes.axisbelow": True,
})


def new_fig(h_in):
    fig = plt.figure(figsize=(W_IN, h_in))
    fig.patches.append(FancyBboxPatch((0.004, 0.006), 0.992, 0.988, boxstyle="round,pad=0,rounding_size=0.015",
                                      transform=fig.transFigure, facecolor=BG, edgecolor=BORDER, linewidth=1.5,
                                      zorder=-10))
    return fig


def title(fig, main, sub):
    h = fig.get_figheight()
    fig.text(0.035, 1 - 0.33 / h, main, fontsize=21, fontweight="bold", color=TXT, va="top")
    fig.text(0.035, 1 - 0.78 / h, sub, fontsize=15, color=AXC, va="top")


def save(fig, out, name):
    fig.savefig(os.path.join(out, name), format="svg", metadata={"Date": None, "Creator": None})
    plt.close(fig)
    print("wrote figures/" + name)


def jload(root, rel):
    with open(os.path.join(root, rel), encoding="utf-8") as fh:
        return json.load(fh)


def text(root, rel):
    with open(os.path.join(root, rel), encoding="utf-8") as fh:
        return fh.read()


CERT = "bundle/AB/leadA/cert/"


def path_points(walk):
    return [tuple(Fr(c) for c in p.split(",")) for p in walk["path"].split(";")]


def walks_a(root):
    """The 87 walks combined by cert_combine45b.py: g45_b1..b9, g45_t1, t2, t5, and the pieces in pieces45.txt."""
    names = ["g45_b%d" % k for k in range(1, 10)] + ["g45_t1", "g45_t2", "g45_t5"]
    names += [l.split()[0] for l in text(root, CERT + "pieces45.txt").splitlines() if l.strip()]
    return [jload(root, CERT + n + ".json") for n in names]


# ---------------------------------------------------------------- data
def setup(root):
    W = walks_a(root)
    comb = jload(root, CERT + "g45b_combine.json")
    assert comb["holds"] and comb["winding"] == 0 and comb["walks"] == len(W) == 87
    ts = {w["t"] for w in W}
    assert len(ts) == 1
    t_a = Fr(ts.pop())
    pts = [p for w in W for p in path_points(w)]
    xs, ys = {p[0] for p in pts}, {p[1] for p in pts}
    x0, x1, y_in, y_top = min(xs), max(xs), min(ys), max(ys)
    bar = text(root, CERT + "BAR-A14.md")
    delta0 = Fr(re.search(r"de Bruijn \(Delta = (\d+) ->", bar).group(1))
    lam_a = t_a + y_in ** 2 / 2
    assert "%.6f" % float(lam_a) in bar                      # 0.449938 as printed in the sealed BAR
    fb = jload(root, "bundle/AB/leadA/p11/fin_b1.json")
    assert "HOLDS" in text(root, "bundle/AB/leadA/p11/fin_combine.log")
    t_b = Fr(fb["t"])
    yb = min(p[1] for p in path_points(fb))
    lam_b = t_b + yb ** 2 / 2
    return dict(W=W, comb=comb, t_a=t_a, x0=x0, x1=x1, y_in=y_in, y_top=y_top, delta0=delta0, lam_a=lam_a,
                t_b=t_b, y_b=yb, lam_b=lam_b)


# ---------------------------------------------------------------- figure 1: the ceiling on zeros, turned down
def fig_ceiling(out, D):
    d0 = float(D["delta0"])
    fig = new_fig(7.2)
    title(fig, "Two turns of the heat dial, with a computer proof in between",
          "Proven ceiling on how far any zero can sit from the line, for two degree-2 L-functions")
    ax = fig.add_axes([0.1, 0.13, 0.62, 0.66])
    n = 400
    t_end = d0 ** 2 / 2                                      # classical: the ceiling reaches 0 at t = 1/2
    tt = [t_end * i / n for i in range(n + 1)]
    ax.plot(tt, [sqrt(max(d0 ** 2 - 2 * t, 0)) for t in tt], color=AXC, lw=2, ls=(0, (5, 4)),
            label="classical: start at distance %g, reach the line at t = %g" % (d0, t_end))

    def chain(t0, y_in, lam, col, lab, z):
        t0, y_in, lam = float(t0), float(y_in), float(lam)
        a = [t0 * i / n for i in range(n + 1)]
        ax.plot(a, [sqrt(d0 ** 2 - 2 * t) for t in a], color=col, lw=2.5, zorder=z, label=lab)
        top = sqrt(d0 ** 2 - 2 * t0)
        ax.plot([t0, t0], [top, y_in], color=col, lw=2.5, zorder=z)
        b = [t0 + (lam - t0) * i / n for i in range(n + 1)]
        ax.plot(b, [sqrt(max(y_in ** 2 - 2 * (t - t0), 0)) for t in b], color=col, lw=2.5, zorder=z)
        ax.plot(lam, 0, marker="o", ms=10, color=col, mec=BG, mew=1.5, zorder=z + 1)
        return top

    top_b = chain(D["t_b"], D["y_b"], D["lam_b"], CAT[1], "η(2z)η(22z), Theorem 1(b)", 3)
    top_a = chain(D["t_a"], D["y_in"], D["lam_a"], CAT[0], "η(z)η(23z), Theorem 1(a)", 4)
    ta, ya = float(D["t_a"]), float(D["y_in"])
    ax.annotate("computer proof at t = %.2f:\nno zeros between %.3f\nand %.4f" % (ta, ya, top_a),
                (ta, (ya + top_a) / 2), xytext=(0.16, 0.2), textcoords="data", fontsize=14, ha="left",
                va="center", arrowprops=dict(arrowstyle="-", color=AXC, lw=1, shrinkB=4))
    ax.set_xlim(0, 0.53)
    ax.set_ylim(0, 1.06)
    ax.set_xlabel("heat dial t")
    ax.set_ylabel("proven ceiling on distance from the line")
    ax.legend(loc="upper right", fontsize=13, handlelength=2.4)
    # side panel: the bounds on a number line
    fig.text(0.75, 0.76, "Every zero is on the line from:", fontsize=15, va="top")
    rows = [(CAT[0], "t = %.6f" % float(D["lam_a"]), "η(z)η(23z)"),
            (CAT[1], "t = %.6f" % float(D["lam_b"]), "η(2z)η(22z)"),
            (AXC, "t = %g" % t_end, "classical bound, free")]
    for i, (col, a, b) in enumerate(rows):
        y = 0.67 - 0.12 * i
        fig.text(0.75, y, a, fontsize=17, fontweight="bold", color=col, va="top")
        fig.text(0.75, y - 0.05, b, fontsize=14, color=TXT, va="top")
    fig.text(0.75, 0.28, "So the de Bruijn-Newman\nconstant Λ is at most that\nvalue (and at least 0).\n"
                         "Nothing here bears on\nthe Riemann hypothesis.", fontsize=14, color=AXC, va="top")
    save(fig, out, "heat-dial-ceiling.svg")


# ---------------------------------------------------------------- figure 2: the band the computer proved empty
def fig_band(root, out, D):
    tail_b = jload(root, "bundle/AB/leadA/tail/tail_run045b_out.json")
    tail_a = jload(root, "bundle/AB/leadA/tail/tail_run045_out.json")
    ty0, ty1 = tail_b["params"]["y"]
    assert tail_b["params"]["x_start"] == float(D["x1"]) and tail_b["HOLDS"] and tail_a["HOLDS"]
    nbox = tail_a["A"]["boxes"] + tail_b["A"]["boxes"]
    x0, x1, yi, yt = (float(D[k]) for k in ("x0", "x1", "y_in", "y_top"))
    edge = sqrt(float(D["delta0"]) ** 2 - 2 * float(D["t_a"]))
    comb = D["comb"]

    fig = new_fig(6.8)
    title(fig, "What the computer proved at t = %.2f" % float(D["t_a"]),
          "The quarter x ≥ 0, y ≥ 0 of the complex plane (the rest follows by symmetry); the two axes have different scales")
    ax = fig.add_axes([0.1, 0.14, 0.86, 0.64])
    xr = 15500
    ax.add_patch(Rectangle((x0, yi), x1 - x0, yt - yi, facecolor="#203b24", edgecolor="none", zorder=1))
    for w in D["W"]:                                         # the boundary, drawn walk by walk from the shipped paths
        P = path_points(w)
        ax.plot([float(p[0]) for p in P], [float(p[1]) for p in P], color=ACC, lw=2, zorder=3,
                solid_capstyle="butt")
    ax.add_patch(Rectangle((x1, ty0), xr - x1, ty1 - ty0, facecolor="#1d2c3e", edgecolor=CAT[0], lw=1.5,
                           zorder=1))
    ax.add_patch(Rectangle((0, edge), xr, 0.6 - edge, facecolor="#2a3038", edgecolor="none", zorder=0.5))
    ax.axhline(edge, color=AXC, lw=1.5, ls=(0, (5, 4)), zorder=2)
    ax.axhline(0, color=TXT, lw=3, zorder=2)
    ax.text(6250, (yi + yt) / 2, "certified: no zeros in this box\n%d walks, %s ball-arithmetic evaluations, "
            "winding number %d" % (comb["walks"], format(comb["points"], ","), comb["winding"]),
            ha="center", va="center", fontsize=14, color=TXT, zorder=4)
    ax.text((x1 + xr) / 2, (ty0 + ty1) / 2, "tail lemma:\n%d boxes,\nthen a\nwritten bound" % nbox,
            ha="center", va="center", fontsize=12.5, color=TXT, zorder=4)
    ax.text(6250, 0.555, "no zeros above %.4f (de Bruijn's rule, from the classical start)" % edge,
            ha="center", fontsize=14, color=TXT, va="center")
    ax.text(6250, yi / 2, "zeros may lie anywhere below %.3f;\nthe second turn of the dial, by %.3f²/2, "
            "brings them all to the line" % (yi, yi), ha="center", va="center", fontsize=14, color=AXC)
    ax.text(200, 0.012, "the line (where every zero must end up)", fontsize=13, color=TXT, va="bottom")
    ax.set_xlim(0, xr)
    ax.set_ylim(-0.02, 0.6)
    ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: format(int(v), ",")))
    ax.set_xticks([0, 2500, 5000, 7500, 10000, float(D["x1"])])
    ax.set_xlabel("real part x  (the tail continues to infinity; boxes up to x = 2·10¹², a monotone bound beyond)")
    ax.set_ylabel("imaginary part y")
    save(fig, out, "zero-free-band.svg")
    return nbox, edge


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: python make_figures.py <repo root>")
    root = sys.argv[1]
    here = os.path.dirname(os.path.abspath(__file__))
    out = here if os.path.basename(here) == "figures" else os.path.join(here, "figures")
    os.makedirs(out, exist_ok=True)
    D = setup(root)
    fig_ceiling(out, D)
    nbox, edge = fig_band(root, out, D)
    print("Theorem 1(a): t0 = %s, inner edge %s, top %s, x in [%s, %s], bound %s = %.6f"
          % (D["t_a"], D["y_in"], D["y_top"], D["x0"], D["x1"], D["lam_a"], float(D["lam_a"])))
    print("Theorem 1(b): t0 = %s, inner edge %s, bound %s = %.6f" % (D["t_b"], D["y_b"], D["lam_b"],
                                                                     float(D["lam_b"])))
    print("de Bruijn edge at t0:", edge, " walks:", D["comb"]["walks"], " evaluations:", D["comb"]["points"],
          " tail boxes:", nbox)


if __name__ == "__main__":
    main()
