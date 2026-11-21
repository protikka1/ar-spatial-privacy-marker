# ASPM SDK engineering proposal (draft)

**Title:** Feature request: interoperable visual spatial-privacy opt-out for AR SDKs

**Repository:** https://github.com/protikka1/ar-spatial-privacy-marker

## Problem and scope

Current AR clients may create persistent anchors, 3D maps and upload spatial data. Property occupants and owners need a consistent *signal* to request that participating AR software refrain from particular activities. ASPM-V1-OPT-OUT is a proposed printed image signal, not an existing platform standard or legal enforcement mechanism.

## Request to SDK/platform maintainers

1. **Optional reference-image recognition** of the physical ASPM marker in supported camera pipelines, with documented confidence and false-positive handling.
2. **Standard event**: `spatial-privacy-opt-out`, containing `marker_id`, `detected_at`, `confidence` (where supported), `tracking_state`, and `policy_version`. Do not infer property ownership or coordinates from an image alone.
3. **App-controlled restriction hooks** to stop newly generated meshes, persistent anchors and uploads after detection, and to clear app-owned anchors where appropriate.
4. **Boundary and authority model**: expose only locally verifiable scope (e.g. visible marker / consented, trusted area metadata); do not infer a property-wide geofence or exclusion radius without an authenticated authority and reliable boundaries.
5. **Privacy defaults**: detection on-device, no automatic image/mesh upload, minimal logging, and clear user notice; documented reset/lost-tracking behavior.
6. **Conformance tests** for robust detection, false positives, temporary occlusion, policy handling and privacy behavior.
7. **Standards discussion** about whether opt-out should become a recommended or enforced SDK/platform policy, with security and accessibility review.

## Normative interpretation (proposal only)

- Detection is a signal of an opt-out **request**, not proof of ownership or applicable law.
- Applications must explicitly opt in to and implement the enforcement behavior; this repository cannot disable SDKs or third-party apps.
- Failure to recognize a marker must not be reported as verification that unrestricted scanning is lawful.
- Remote uploads and persistent anchors are separate capabilities with separately enforced controls.
- If authenticated scope is unavailable, only local, clearly disclosed restrictions can be applied.

## Proposed test acceptance criteria

- A participating demo reads the repository `policy.json` and validates `marker_id` and restriction field types.
- A real-world printed-marker test records positive detections and negative controls, under varied lighting and perspective, without claiming a specific accuracy until measured.
- Once a trusted detection event arrives, demo app refuses new restricted operations and stops app-owned spatial uploads.
- On marker loss, restrictions do not silently disappear until the app's explicit, user-visible reset policy is satisfied.
- No frame or spatial map is uploaded as part of marker recognition.
- Unknown policy versions and malformed policies fail validation, with explicit diagnostics.

## Platform-specific requests

| Ecosystem | Suggested integration |
|---|---|
| Google ARCore | Augmented Images reference image + application-side session/anchor/upload control; request optional core privacy event |
| Apple ARKit | ARReferenceImage image detection + ARSession delegate and application-owned anchor controls |
| Unity AR Foundation | Shared C# opt-out event and XR image tracking adapter; platform-specific implementation of restricted operations |
| WebXR | Browser standards discussion plus app-provided image tracker and JavaScript guard; no assumed built-in universal marker recognition |
| TikTok Effect House | Privacy marker input/event and effects publishing guidance |
| Meta XR/Spatial SDK | Image tracking adapter, scene/anchor restrictions and clear user policy |

## Requested engineering response

Please advise whether the SDK can support the proposed detection event, the minimum API surface, security/authority expectations, and whether a shared conformance suite would be useful. We welcome technical review and platform-specific pull requests.

## Open engineering questions

- Who may claim an area and how is that claim verified?
- How are occlusion, malicious marker placement, and conflicting policy signals handled?
- How is an opt-out scoped without falsely implying a property-wide prohibition?
- Should restrictions persist per session or until explicit re-authorization?
- Which SDK operations can be stopped, versus capabilities that the host application does not control?
