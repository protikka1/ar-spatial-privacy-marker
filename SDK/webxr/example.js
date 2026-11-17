// Integration example only; connect a real image tracker to guard.update(...).
import { ASPMGuard, loadASPMPolicy } from "./aspm_guard.js";

const policy = await loadASPMPolicy("/policy.json");
export const guard = new ASPMGuard({
  policy,
  onPauseMapping: () => {
    // Pause your application's plane/mesh processing here.
    console.warn("ASPM restricted zone: pause app-controlled mapping");
  },
  onRemoveAnchors: () => {
    // Dispose of anchors created by YOUR application.
    console.warn("ASPM: remove app-controlled anchors");
  },
  onRestricted: () => console.warn("Privacy marker recognized"),
});

// In a real detector callback:
// guard.update(detectedMarkerId === "ASPM-V1-OPT-OUT");
// Before creating an anchor: if (!guard.permits("anchor")) return;
