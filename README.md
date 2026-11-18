# AR Spatial Privacy Marker (ASPM-V1-OPT-OUT)

ASPM is an **experimental, open-source visual spatial privacy opt-out proposal**. Its physical marker communicates a request to participating augmented reality (AR) applications not to map or persist spatial information at a location without authorization.

**Important:** The marker is not recognized by AR platforms by default. It cannot turn off another application's camera, prevent scanning by itself, verify property ownership or boundaries, or establish a universal legal prohibition. The SDK providers and app developers must choose to implement the proposal.

## Files

- [Visual marker](assets/ar-privacy-marker-v1.svg) for printing
- [Policy](policy.json) describing requested application-level restrictions
- [SDK starter integrations](SDK/README.md) for Python/OpenCV, WebXR, and Apple ARKit assets
- [Proposed protocol](docs/ASPM-PROTOCOL.md)
- [SDK compatibility matrix](docs/SDK-COMPATIBILITY.md)
- [Engineering adoption proposal](docs/ASPM-SDK-PROPOSAL.md)

## How participating applications may implement it

1. Detect the designated printed marker using a trusted image-tracking implementation.
2. Validate the marker identity and the policy format.
3. Establish the requested scope without assuming that a printed marker proves geographic boundaries or legal authority.
4. Restrict the application's own mapping, anchor creation, and spatial data uploads according to the adopted policy.
5. Explain restrictions to the user, handle loss of tracking conservatively, and provide a documented reset/dispute process.

## Physical deployment

- Print `assets/ar-privacy-marker-v1.svg` on matte paper or vinyl, around **30 cm (12 inches)** wide.
- Avoid glare and obstruction.
- Place where visitors can see the sign. A sign does not make third-party applications technically compliant.

## Development

Python dependencies are in `SDK/python/requirements.txt`; the root `requirements.txt` references them. On Android Termux, use platform-compatible packages as needed.

Run the no-dependency policy contract tests:

```sh
python -m unittest discover -s tests -v
```

For engineering feedback, see [the SDK proposal](docs/ASPM-SDK-PROPOSAL.md). Vendor adoption is not claimed or implied.

## Notice

> Private property: Please respect this spatial privacy opt-out request. No AR mapping, persistent anchoring, or spatial-data upload without authorization.

The notice communicates an opt-out request. Applicable legal rights and restrictions vary by jurisdiction and circumstances.
