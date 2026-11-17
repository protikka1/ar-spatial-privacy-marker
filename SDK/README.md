# ASPM SDK starters

These are *integration examples*, not a platform-enforced privacy standard.
The marker only has an effect when an AR application **chooses to detect and
respect it**. A printed sign cannot force other AR apps to stop scanning.

## Python prototype

Install: `python -m pip install -r SDK/python/requirements.txt`

Export the existing SVG as a PNG:
`python -c "import cairosvg; cairosvg.svg2png(url='assets/ar-privacy-marker-v1.svg',write_to='marker.png')"`
(Requires `pip install cairosvg`; alternatively export PNG from an image editor.)

Run:
`python SDK/python/aspm_detection.py --reference marker.png --image photo.jpg`

Uses ORB + homography to identify a *likely* match. False positives/negatives
are possible; validate against multiple angles, lighting and distances.
This script does not inspect a live camera stream or enforce restrictions.

## WebXR (JavaScript)

`SDK/webxr/aspm_guard.js` is a framework-neutral, application-level guard.
Connect a real image tracker to `guard.update(true/false)`, then enforce
`guard.permits(operation)` before app-controlled scanning, anchor creation,
and uploading. There is **no universal WebXR marker tracking or SDK opt-out
enforcement API**. The provided callbacks do not pause the browser or other
applications on their own.

Host `policy.json` at the same origin, or update the policy URL explicitly.
See `example.js` for integration points.

## ARKit (iOS)

The `ASPMReferenceImage.arresourcegroup` directory is a **starter** for an
Xcode asset catalog (typically inside `Assets.xcassets`). Apple requires a
*raster image*, not an SVG, for `ARReferenceImage`.

**Required step before building:** Export `assets/ar-privacy-marker-v1.svg`
as `marker.png` at a suitable resolution, put it inside:
`SDK/mobile/ASPMReferenceImage.arresourcegroup/ASPMMarker.arreferenceimage/`.
Set the image's physical width to **0.30 m** in Xcode and verify Xcode recognizes
the asset. Add the folder to an Xcode `Assets.xcassets` asset catalog.

This resource group does not implement detection/enforcement. In your Swift
ARKit app, load the reference images from `ARReferenceImage.referenceImages(
inGroupNamed: "ASPMReferenceImage", bundle: nil)`, configure image detection,
and remove your app's anchors/disable its mapping in the relevant callbacks.
It cannot change ARKit behavior in third-party apps.

## Privacy and safety

Do not upload camera frames, scene meshes or coordinates without explicit
consent. The existing notice in the SVG/README should not be interpreted as a
blanket statement of law in every jurisdiction.
