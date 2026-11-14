# AR Spatial Privacy Marker (`ASPM-V1-OPT-OUT`)

An open-source, machine-readable physical visual marker and spatial opt-out specification designed to protect physical locations from unauthorized Augmented Reality (AR) object mapping, 3D surface meshing, and persistent spatial anchoring.

## Legal & Spatial Notice
> **Private Property No AR application Mapping object , Unauthorized 3D mapping or unauthorized landing is prohibited and against the law**

## How It Works
1. **Asymmetric Visual Feature Emblem:** Designed with high-contrast, non-repeating corners and internal geometric features to achieve rapid detection in ARCore (`Augmented Images`), ARKit (`ARReferenceImage`), and WebXR/MindAR trackers.
2. **Immediate Session Lockout:** When an AR client detects `ASPM-V1-OPT-OUT` in the camera frame, it reads `policy.json` rules and:
   - Pauses plane detection and 3D mesh generation.
   - Detaches and removes any active virtual anchors in the local scene.
   - Displays the property owner's privacy restriction notice to the user.

## Physical Deployment
- Print `assets/ar-privacy-marker-v1.svg` on matte paper or vinyl (recommended physical width: **30 cm / 12 inches**).
- Avoid glossy lamination that causes specular glare over the central feature emblem.
- Mount at eye level near entrances, walls, or restricted zones.
