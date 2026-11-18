# ASPM-V1-OPT-OUT protocol draft

**Status:** Experimental proposal, not a standard.

## Identification

- Marker ID: `ASPM-V1-OPT-OUT`.
- Physical visual asset: `assets/ar-privacy-marker-v1.svg`.
- Policy format: `policy.json` at the repository root.
- The recommended 0.30 m printed width is a capture guideline; visual detection alone does not prove metric distance or property boundaries.

## Policy fields

| Key | Type | Meaning |
|---|---|---|
| `standard` | string | `AR-Spatial-Privacy-Marker` |
| `version` | string | Currently `1.0.0` |
| `marker_id` | string | `ASPM-V1-OPT-OUT` |
| `physical_width_meters` | positive number | Print guideline |
| `restrictions.block_plane_detection` | boolean | Ask participating app to stop relevant plane operations |
| `restrictions.block_3d_meshing` | boolean | Ask participating app to stop app-controlled meshing |
| `restrictions.block_persistent_anchors` | boolean | Ask participating app to stop new persistent anchors |
| `restrictions.detach_existing_anchors` | boolean | Ask participating app to remove its own anchors |
| `restrictions.block_vps_upload` | boolean | Ask participating app to avoid uploads for VPS/spatial localization |
| `legal_notice` | string | Informational request, not an assertion of universal legal force |

## Event and state model

Suggested states: `unseen`, `candidate`, `verified`, `restricted`, `lost`, `cleared`.

A detector reports a candidate with evidence (feature matches, homography, confidence if calibrated). The host verifies the intended marker and applies its adopted policy, then gates each restricted operation. Marker loss should trigger a conservative hold and explicit documented clear/reset rather than immediately resuming all processing.

Suggested event:

```json
{
  "type": "spatial-privacy-opt-out",
  "marker_id": "ASPM-V1-OPT-OUT",
  "policy_version": "1.0.0",
  "state": "restricted",
  "source": "on-device-image-tracker"
}
```

## Threat model

- **Spoofing:** counterfeit markers could trigger unwanted denial of service; verify scope and allow dispute/reset mechanisms.
- **False positives:** image matching can be wrong; validate geometric consistency and test negatives.
- **False negatives:** poor lighting, occlusion, motion blur, and perspective can prevent recognition.
- **Unauthorized claims:** a sign does not by itself verify property rights or geographic limits.
- **Data retention:** avoid persisting sensitive images and geospatial maps by default.
- **Capability limits:** an app-level guard cannot control the device camera or other apps.

## Versioning and interoperability

Adapters should reject incompatible major protocol versions, log diagnostics without recording frames, and treat unknown restriction keys as unsupported rather than silently claiming compliance. Maintain test cases and a change log before proposing a stable standard.
