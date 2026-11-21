# AR Spatial Privacy Marker (ASPM-V1-OPT-OUT)

ASPM is an experimental, open-source proposal for a printed marker that asks participating AR apps to limit spatial mapping, persistent anchors, and spatial-data uploads. Restrictions apply to operations the participating app controls. Marker recognition identifies an opt-out request. Property authority and geographic scope require separate verification.

**Status:** Protocol draft and starter code. Native adapters and device conformance tests are pending. Vendor adoption remains unverified.

## SDK engineering review

Review the [protocol draft](docs/ASPM-PROTOCOL.md), [engineering proposal](docs/ASPM-SDK-PROPOSAL.md), [compatibility matrix](docs/SDK-COMPATIBILITY.md), and [sample policy](policy.json). Share feedback in [PR #2](https://github.com/protikka1/ar-spatial-privacy-marker/pull/2).

1. **Detection and event.** Which supported SDK and device versions can recognize the reference image on-device? Which tracking states or confidence signals can an adapter reliably expose? Help align the event fields in the two drafts.
2. **App controls.** Which APIs can pause app-controlled plane or mesh processing, block new persistent anchors and spatial uploads, or remove app-owned anchors? Which operations remain SDK-managed?
3. **Scope and lifecycle.** What scope can the app verify from its available inputs? How should it handle temporary tracking loss, conflicting signals, and explicit reset?
4. **Conformance.** What sample app, devices, and fixtures would you accept to demonstrate recognition and policy behavior without uploading camera frames?

The proposed flow is to detect and verify the reference image, validate the policy and its version, establish the scope the app can verify, and apply supported restrictions. The draft calls for holding restrictions through temporary tracking loss until an explicit reset.

## Platform integration status

| Platform | Current repository support | Integration to review |
| --- | --- | --- |
| Google ARCore | Marker and policy assets | Kotlin Augmented Images adapter, app-owned anchor and upload controls, Android device tests |
| Apple ARKit | Xcode reference-image catalog scaffold | Add `marker.png`, wire Swift ARSession callbacks to app controls, test on iPhone |
| Unity AR Foundation | Proposed integration | C# tracked-image adapter and operation controls, tests on Android and iOS providers |
| WebXR | JavaScript guard and example driven by a detection boolean | Connect an image tracker and host operation gates. Align the guard's immediate clear on `false` with the draft's explicit reset, then test in browsers. |
| TikTok Effect House | Proposed integration | Confirm available marker events, effect controls, and publishing requirements before building a sample effect |
| Meta XR / Spatial SDK | Proposed integration | Select a target SDK and device, confirm image tracking and scene or anchor controls, then build a device demo |

See the [SDK starter files](SDK/README.md) for the Python/OpenCV still-image detector, WebXR guard, and ARKit scaffold.

## Local validation

Run the standard-library checks for the bundled policy and marker asset:

```sh
python3 -m unittest discover -s tests -v
```

For a first detection smoke test, export the [marker SVG](assets/ar-privacy-marker-v1.svg) to `marker.png` and print it about 30 cm (12 in) wide on matte paper. Take a photo with the printed marker and a comparable photo without it. Run from the repository root in a Python environment with OpenCV and NumPy:

```sh
python3 -m pip install -r requirements.txt
python3 SDK/python/aspm_detection.py --reference marker.png --image printed-marker.jpg
python3 SDK/python/aspm_detection.py --reference marker.png --image control.jpg
```

Expect `"detected": true` and exit status 0 for the marker photo, and `"detected": false` and exit status 1 for the control. A device conformance test should additionally exercise varied lighting and angles, verify that restricted app operations are blocked after detection, and confirm that restrictions persist through temporary tracking loss until explicit reset.

## Notice

> Private property: Please respect this spatial privacy opt-out request. No AR mapping, persistent anchoring, or spatial-data upload without authorization.

Applicable legal rights and restrictions vary by jurisdiction and circumstances.
