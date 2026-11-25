import os

TEXT = "She died as she lived: with 47 tabs open and none of them closed."

MIN_CHARS = 1
MAX_CHARS = 150


def render(text):
    """Validate the epitaph against the kit gate, then return its bytes."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be whitespace-only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text.encode("utf-8")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(render(TEXT) + b"\n")

if __name__ == "__main__":
    main()
