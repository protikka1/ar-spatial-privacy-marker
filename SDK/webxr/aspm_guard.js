/**
 * ASPM guard for opt-in WebXR applications.
 * WebXR does not provide a universal built-in ASPM marker detector.
 * Supply detections from an image-tracking implementation, and provide
 * callbacks that pause mapping / remove anchors in YOUR own application.
 */
export class ASPMGuard {
  constructor({ policy, onRestricted, onCleared, onPauseMapping, onRemoveAnchors } = {}) {
    if (!policy || policy.marker_id !== "ASPM-V1-OPT-OUT") {
      throw new Error("Valid ASPM policy with marker_id is required");
    }
    this.policy = policy;
    this.restricted = false;
    this.onRestricted = onRestricted ?? (() => {});
    this.onCleared = onCleared ?? (() => {});
    this.onPauseMapping = onPauseMapping ?? (() => {});
    this.onRemoveAnchors = onRemoveAnchors ?? (() => {});
  }

  /**
   * Feed a trusted marker-detection result from an image tracker.
   * Explicitly pass true ONLY after tracking/validating the designated marker.
   * False resets the guard; apps may choose a longer retention policy.
   */
  update(markerDetected) {
    if (typeof markerDetected !== "boolean") {
      throw new TypeError("update expects a boolean");
    }
    if (markerDetected === this.restricted) return;
    this.restricted = markerDetected;
    if (markerDetected) {
      this.onPauseMapping(this.policy.restrictions);
      if (this.policy.restrictions?.detach_existing_anchors) {
        this.onRemoveAnchors();
      }
      this.onRestricted(this.policy);
    } else {
      this.onCleared(this.policy);
    }
  }

  /** Call before adding planes, meshes, or anchors in the host application. */
  permits(operation) {
    const restrictionByOperation = {
      plane: "block_plane_detection",
      mesh: "block_3d_meshing",
      anchor: "block_persistent_anchors",
      vpsUpload: "block_vps_upload",
    };
    const key = restrictionByOperation[operation];
    if (!key) throw new Error(`Unknown operation: ${operation}`);
    return !(this.restricted && this.policy.restrictions?.[key]);
  }
}

/** Fetch a policy from a trusted same-origin/static URL controlled by the app. */
export async function loadASPMPolicy(url = "/policy.json") {
  const response = await fetch(url);
  if (!response.ok) throw new Error(`ASPM policy fetch failed: ${response.status}`);
  const policy = await response.json();
  if (policy.marker_id !== "ASPM-V1-OPT-OUT") throw new Error("Unexpected marker_id");
  return policy;
}
