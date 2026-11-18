# Platform compatibility and adoption status

This document distinguishes **starter integration** from **native platform adoption**. No SDK vendor has been verified as adopting ASPM.

| Platform | Repo artifact | Actual capability | Missing for a working demo | Vendor adoption |
|---|---|---|---|---|
| Python / OpenCV | `SDK/python/aspm_detection.py` | ORB + RANSAC still-image candidate detection | Real-world test dataset, accuracy report, video pipeline | N/A |
| Android / ARCore | existing marker SVG and policy | Reference material only | Kotlin/Java Augmented Images adapter, camera/anchor guards, device tests | Not verified |
| Apple / ARKit | `SDK/mobile/ASPMReferenceImage.arresourcegroup` | Xcode asset catalog scaffold | Raster `marker.png`, Swift ARSession integration, iOS tests | Not verified |
| Unity / AR Foundation | protocol documentation | Integration design only | C# XRTrackedImage adapter and AR session restrictions | Not verified |
| WebXR | `SDK/webxr/aspm_guard.js` | App-controlled policy hooks, accepts detector boolean | Image tracker, app-specific operation gates, browser tests | Not verified |
| TikTok Effect House | protocol documentation | Proposed feature request only | Native effect-tool event support and policy approval | Not verified |
| Meta Spatial SDK | protocol documentation | Proposed feature request only | Platform-native tracking/anchor adapter and policy approval | Not verified |

## Common adapter contract (draft)

- **Input:** validated image-recognition event carrying ASPM marker identity
- **Policy:** versioned object; typed opt-out restrictions from `policy.json`
- **Decision:** restrict only operations explicitly listed in the policy and under app control
- **Output:** on-restricted/on-cleared events plus operation gate decisions
- **Safety:** prevent false legal or property-boundary claims; local processing preferred

## Validation milestones

1. Validate JSON policy and documentation (repository checks).
2. Test Python image detection with realistic positives and negative controls.
3. Demonstrate in one Android ARCore app, with on-device recording of observed behavior.
4. Add Apple, Unity, and WebXR adapters with platform-specific test evidence.
5. Submit adoption proposal, track vendor feedback and acceptance in GitHub issues.

An implementation or sample in this repo does **not** imply endorsement by Google, Apple, Unity, W3C, TikTok, or Meta.
