# real-life-patch-notes: round 3 entry.
# A changelog note for a very small, very specific fix.
# The joke lives in the version number and the nerf.
# Mondays were overpowered. This patch addresses that.
# Nothing else is printed. The output is one line only.
# Round 3: written fresh in this session, verified deterministic.


def main():
    # Build the line from two parts, then print it once.
    prefix = "v2.1.0: Nerfed Mondays"
    suffix = "they were dealing too much damage to the weekend."
    # Join with an em dash and a space, exactly as written.
    line = prefix + " — " + suffix
    print(line)


if __name__ == "__main__":
    main()
